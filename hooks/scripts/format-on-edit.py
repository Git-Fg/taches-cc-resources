#!/usr/bin/env python3
"""
Auto-format files after Claude edits them.
Detects file type and runs appropriate formatter.

Formatter priority order:
- Python: uv run ruff -> ruff (global)
- Markdown: npx markdownlint-cli2 -> npx prettier
- Other (JS/TS/JSON/CSS/YAML): npx prettier
- Go: gofmt
- Rust: rustfmt

If a formatter is not available, the hook will skip silently.
Results are reported to stderr for AI visibility and via JSON for AI context.
"""
import json
import logging
import os
import shutil
import subprocess
import sys
from typing import Optional, Tuple

logger = logging.getLogger(__name__)


def check_command_available(cmd: str) -> bool:
    """Check if a command is available on the system."""
    return shutil.which(cmd) is not None


def try_command(cmd: list[str], timeout: int = 5) -> bool:
    """Try running a command to check availability. Returns True if successful."""
    try:
        result = subprocess.run(cmd, capture_output=True, timeout=timeout)
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False


def has_markdownlint_config(file_path: str) -> bool:
    """Check if .markdownlint.jsonc exists in the project."""
    path = Path(file_path).resolve()
    seen = set()

    while path != path.parent and str(path) not in seen:
        seen.add(str(path))
        config = path / ".markdownlint.jsonc"
        if config.exists():
            return True
        path = path.parent

    return False


def get_formatter_command(file_path: str) -> Optional[Tuple[list[str], str]]:
    """
    Return the formatter command for a given file type.
    Returns (command, description) tuple or None if unavailable.
    """
    ext = os.path.splitext(file_path)[1].lower()

    # Python: uv run ruff -> ruff (global)
    if ext == '.py':
        # Try uv run ruff first (project-local ruff)
        if check_command_available('uv'):
            if try_command(['uv', 'run', 'ruff', '--version']):
                return (['uv', 'run', 'ruff', 'check', '--fix', '--exit-zero'], 'uv run ruff')
        # Fallback to global ruff
        if check_command_available('ruff'):
            return (['ruff', 'check', '--fix', '--exit-zero'], 'ruff')
        return None

    # Markdown: only use markdownlint-cli2 if .markdownlint.jsonc exists
    if ext == '.md':
        if check_command_available('npx'):
            # Only use markdownlint if config is present
            if has_markdownlint_config(file_path) and try_command(['npx', 'markdownlint-cli2', '--version']):
                return (['npx', 'markdownlint-cli2', '--fix'], 'markdownlint-cli2')
            # Fallback to prettier for markdown
            if try_command(['npx', 'prettier', '--version']):
                return (['npx', 'prettier', '--write'], 'prettier')
        return None

    # Prettier-based formatters (JS/TS/JSON/CSS/YAML)
    prettier_exts = {'.js', '.jsx', '.ts', '.tsx', '.json', '.css', '.scss', '.yaml', '.yml'}
    if ext in prettier_exts:
        if check_command_available('npx') and try_command(['npx', 'prettier', '--version']):
            return (['npx', 'prettier', '--write'], 'prettier')
        return None

    # Go (requires gofmt)
    if ext == '.go':
        if check_command_available('gofmt'):
            return (['gofmt', '-w'], 'gofmt')
        return None

    # Rust (requires rustfmt)
    if ext == '.rs':
        if check_command_available('rustfmt'):
            return (['rustfmt'], 'rustfmt')
        return None

    return None


def contains_path_traversal(file_path: str) -> bool:
    """Check if file path contains path traversal attempts."""
    # Check for .. in path components
    if '..' in file_path.split(os.sep):
        return True
    # Also check for URL-encoded traversal
    if '%2e%2e' in file_path.lower() or '%2E%2E' in file_path.lower():
        return True
    return False


def main():
    try:
        input_data = json.load(sys.stdin)
        file_path = input_data.get('tool_input', {}).get('file_path', '')

        # Input validation
        if not file_path:
            sys.exit(0)

        # Security: Check for path traversal attempts
        if contains_path_traversal(file_path):
            logger.debug("[format-on-edit] Path traversal detected: %s", file_path)
            sys.exit(0)

        # Check if file exists (avoid processing non-existent files)
        if not os.path.exists(file_path):
            sys.exit(0)

        formatter_info = get_formatter_command(file_path)

        if formatter_info:
            cmd, formatter_name = formatter_info
            full_cmd = cmd + [file_path]
            try:
                result = subprocess.run(full_cmd, capture_output=True, timeout=10)

                # Simple, robust: always confirm formatting happened
                base_msg = f"[{formatter_name}] formatted {os.path.basename(file_path)}"

                # Only add detail if formatter returned non-zero (errors)
                if result.returncode != 0 and (result.stderr or result.stdout):
                    stderr = result.stderr.decode('utf-8', errors='ignore').strip()
                    stdout = result.stdout.decode('utf-8', errors='ignore').strip()
                    # Append first meaningful line of error output
                    for line in (stderr + '\n' + stdout).split('\n'):
                        line = line.strip()
                        if line and not any(skip in line.lower() for skip in ['v0.', 'v1.', 'v2.', 'version']):
                            base_msg += f" — {line[:100]}"
                            break

                print(json.dumps({
                    "hookSpecificOutput": {
                        "hookEventName": "PostToolUse",
                        "additionalContext": base_msg
                    }
                }))

            except subprocess.TimeoutExpired:
                print(json.dumps({
                    "hookSpecificOutput": {
                        "hookEventName": "PostToolUse",
                        "additionalContext": f"[{formatter_name}] timed out"
                    }
                }))
            except FileNotFoundError:
                print(json.dumps({
                    "hookSpecificOutput": {
                        "hookEventName": "PostToolUse",
                        "additionalContext": f"[{formatter_name}] not found"
                    }
                }))
        else:
            ext = os.path.splitext(file_path)[1].lower()
            print(json.dumps({
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": f"No formatter for {ext}"
                }
            }))

    except json.JSONDecodeError:
        # Invalid JSON input, skip silently
        sys.exit(0)
    except Exception as e:
        # Log error for debugging
        logger.debug("[format-on-edit] Unexpected error: %s", e, exc_info=True)
        sys.exit(0)


if __name__ == '__main__':
    main()
