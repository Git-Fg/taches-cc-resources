#!/usr/bin/env python3
"""
Auto-format files after Claude edits them.
Detects file type and runs appropriate formatter.

Requirements:
- Node.js + npx (for prettier-based formatting)
- Python with ruff (for Python files)
- gofmt (for Go files, usually available with Go)
- rustfmt (for Rust files, usually available with Rust)

If a formatter is not available, the hook will skip silently.
"""
import json
import subprocess
import sys
import os
import shutil

def check_command_available(cmd):
    """Check if a command is available on the system."""
    return shutil.which(cmd) is not None

def get_formatter_command(file_path):
    """Return the formatter command for a given file type, or None if unavailable."""
    ext = os.path.splitext(file_path)[1].lower()

    # Prettier-based formatters (require Node.js + npx + prettier)
    prettier_exts = {'.js', '.jsx', '.ts', '.tsx', '.json', '.css', '.scss', '.md', '.yaml', '.yml'}
    if ext in prettier_exts:
        if check_command_available('npx'):
            # Check if prettier is available by running npx prettier --version
            try:
                result = subprocess.run(['npx', 'prettier', '--version'], capture_output=True, timeout=5)
                if result.returncode == 0:
                    return ['npx', 'prettier', '--write']
            except (subprocess.TimeoutExpired, FileNotFoundError):
                pass
        return None  # Prettier not available, skip formatting

    # Python (requires ruff)
    if ext == '.py':
        if check_command_available('ruff'):
            return ['ruff', 'check', '--fix', '--exit-zero']
        return None

    # Go (requires gofmt)
    if ext == '.go':
        if check_command_available('gofmt'):
            return ['gofmt', '-w']
        return None

    # Rust (requires rustfmt)
    if ext == '.rs':
        if check_command_available('rustfmt'):
            return ['rustfmt']
        return None

    return None

def main():
    try:
        input_data = json.load(sys.stdin)
        file_path = input_data.get('tool_input', {}).get('file_path', '')

        if not file_path or not os.path.exists(file_path):
            sys.exit(0)

        formatter = get_formatter_command(file_path)
        if formatter:
            cmd = formatter + [file_path]
            try:
                subprocess.run(cmd, capture_output=True, timeout=10)
            except (subprocess.TimeoutExpired, FileNotFoundError):
                pass  # Skip formatting on error
    except Exception:
        pass  # Don't block on formatter errors

if __name__ == '__main__':
    main()
