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

    # Markdown: markdownlint-cli2 -> prettier
    if ext == '.md':
        # Try markdownlint-cli2 first (better for markdown linting)
        if check_command_available('npx'):
            if try_command(['npx', 'markdownlint-cli2', '--version']):
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

                # Only report if there's meaningful output (errors or changes)
                context_msg = None
                if result.stdout or result.stderr:
                    stdout = result.stdout.decode('utf-8', errors='ignore').strip()
                    stderr = result.stderr.decode('utf-8', errors='ignore').strip()

                    # Filter out boilerplate (version info, "Finding:", "Linting:")
                    meaningful_lines = []
                    for line in (stdout + '\n' + stderr).split('\n'):
                        line = line.strip()
                        # Skip common boilerplate
                        if not line or line.startswith(('Finding:', 'Linting:', 'All checks passed', 'Summary: 0 error')):
                            continue
                        # Skip version lines (e.g. "markdownlint-cli2 v0.20.0")
                        if any(word in line.lower() for word in ['v0.', 'v1.', 'v2.', 'version', 'formatting']):
                            continue
                        meaningful_lines.append(line)

                    if meaningful_lines:
                        context_msg = ' | '.join(meaningful_lines[:3])  # Max 3 lines

                # Build output - only include additionalContext if there's something to say
                output_data = {"hookSpecificOutput": {"hookEventName": "PostToolUse"}}
                if context_msg:
                    output_data["hookSpecificOutput"]["additionalContext"] = f"[{formatter_name}] {file_path}: {context_msg}"
                print(json.dumps(output_data))

            except subprocess.TimeoutExpired:
                msg = f"[format-on-edit] {formatter_name} timed out on {file_path}"
                print(msg, file=sys.stderr)
                output = {
                    "hookSpecificOutput": {
                        "hookEventName": "PostToolUse",
                        "additionalContext": f"Formatter timeout: {formatter_name} timed out on {file_path}"
                    }
                }
                print(json.dumps(output))
            except FileNotFoundError as e:
                msg = f"[format-on-edit] {formatter_name} not found: {e}"
                print(msg, file=sys.stderr)
                output = {
                    "hookSpecificOutput": {
                        "hookEventName": "PostToolUse",
                        "additionalContext": f"Formatter not found: {formatter_name} - {e}"
                    }
                }
                print(json.dumps(output))
        else:
            ext = os.path.splitext(file_path)[1].lower()
            msg = f"[format-on-edit] No formatter available for {ext} files"
            print(msg, file=sys.stderr)
            output = {
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": f"No formatter configured for {ext} files"
                }
            }
            print(json.dumps(output))

    except json.JSONDecodeError:
        # Invalid JSON input, skip silently
        sys.exit(0)
    except Exception as e:
        # Log error for debugging
        logger.debug("[format-on-edit] Unexpected error: %s", e, exc_info=True)
        sys.exit(0)


if __name__ == '__main__':
    main()
