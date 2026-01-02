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
Results are reported to stderr for AI visibility.
"""
import json
import subprocess
import sys
import os
import shutil
from typing import List, Optional, Tuple

def check_command_available(cmd: str) -> bool:
    """Check if a command is available on the system."""
    return shutil.which(cmd) is not None

def try_command(cmd: List[str], timeout: int = 5) -> bool:
    """Try running a command to check availability. Returns True if successful."""
    try:
        result = subprocess.run(cmd, capture_output=True, timeout=timeout)
        return result.returncode == 0
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return False

def get_formatter_command(file_path: str) -> Optional[Tuple[List[str], str]]:
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

def main():
    try:
        input_data = json.load(sys.stdin)
        file_path = input_data.get('tool_input', {}).get('file_path', '')

        if not file_path or not os.path.exists(file_path):
            sys.exit(0)

        formatter_info = get_formatter_command(file_path)
        if formatter_info:
            cmd, formatter_name = formatter_info
            full_cmd = cmd + [file_path]
            try:
                result = subprocess.run(full_cmd, capture_output=True, timeout=10)
                # Report formatting action to AI via stderr (visible in Claude Code output)
                print(f"[format-on-edit] Ran {formatter_name} on {file_path}", file=sys.stderr)
                if result.stdout:
                    # Show formatter output for transparency
                    output = result.stdout.decode('utf-8', errors='ignore').strip()
                    if output:
                        print(f"[format-on-edit] {formatter_name} output:\n{output}", file=sys.stderr)
            except subprocess.TimeoutExpired:
                print(f"[format-on-edit] {formatter_name} timed out on {file_path}", file=sys.stderr)
            except FileNotFoundError as e:
                print(f"[format-on-edit] {formatter_name} not found: {e}", file=sys.stderr)
        else:
            ext = os.path.splitext(file_path)[1].lower()
            print(f"[format-on-edit] No formatter available for {ext} files", file=sys.stderr)
    except json.JSONDecodeError:
        # Invalid JSON input, skip silently
        sys.exit(0)
    except Exception as e:
        print(f"[format-on-edit] Error: {e}", file=sys.stderr)

if __name__ == '__main__':
    main()
