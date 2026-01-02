#!/usr/bin/env python3
"""
Run type checker on Python files after Claude edits them.
Only runs when pyproject.toml is configured with type checking support.

Type checker priority order:
- uv run pyrefly -> pyrefly (global) -> uv run mypy -> mypy (global)

Configuration detection:
- Checks for [tool.pyrefly] in pyproject.toml (uses pyrefly)
- Checks for [tool.mypy] in pyproject.toml (uses mypy)
- Skips silently if no type checker is configured

Results are reported to stderr for AI visibility.
"""
import json
import subprocess
import sys
import os
import shutil
from pathlib import Path
from typing import List, Optional, Tuple, Literal

type TypeChecker = Literal["pyrefly", "mypy"]

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

def find_pyproject_toml(file_path: str) -> Optional[Path]:
    """Find pyproject.toml by searching upward from file_path."""
    path = Path(file_path).resolve()
    seen = set()

    while path != path.parent and str(path) not in seen:
        seen.add(str(path))
        pyproject = path / "pyproject.toml"
        if pyproject.exists():
            return pyproject
        path = path.parent

    return None

def detect_configured_type_checker(pyproject_path: Path) -> Optional[TypeChecker]:
    """Detect which type checker is configured in pyproject.toml."""
    try:
        content = pyproject_path.read_text()
        if "[tool.pyrefly]" in content:
            return "pyrefly"
        if "[tool.mypy]" in content:
            return "mypy"
    except Exception:
        pass
    return None

def get_type_checker_command(checker: TypeChecker, project_root: Path) -> Optional[Tuple[List[str], str]]:
    """
    Return the type checker command for the given checker type.
    Returns (command, description) tuple or None if unavailable.
    """
    if checker == "pyrefly":
        # Try uv run pyrefly first
        if check_command_available("uv"):
            if try_command(["uv", "run", "pyrefly", "--version"], timeout=10):
                return (["uv", "run", "pyrefly", "check"], "uv run pyrefly")
        # Fallback to global pyrefly
        if check_command_available("pyrefly"):
            return (["pyrefly", "check"], "pyrefly")
        return None

    if checker == "mypy":
        # Try uv run mypy first
        if check_command_available("uv"):
            if try_command(["uv", "run", "mypy", "--version"], timeout=10):
                return (["uv", "run", "mypy"], "uv run mypy")
        # Fallback to global mypy
        if check_command_available("mypy"):
            return (["mypy"], "mypy")
        return None

    return None

def should_check_file(file_path: str, project_root: Path) -> bool:
    """Check if file should be type checked based on common exclusion patterns."""
    path = Path(file_path).resolve()

    # Skip if file is not under project root
    try:
        path.relative_to(project_root)
    except ValueError:
        return False

    # Common exclusion patterns
    exclude_parts = {".venv", "venv", "__pycache__", ".attic", "node_modules", ".git", "build", "dist"}
    if any(part in path.parts for part in exclude_parts):
        return False

    # Skip test files if desired (optional - uncomment to enable)
    # if "test" in path.parts or "tests" in path.parts:
    #     return False

    return True

def main():
    try:
        input_data = json.load(sys.stdin)
        file_path = input_data.get("tool_input", {}).get("file_path", "")

        if not file_path or not os.path.exists(file_path):
            sys.exit(0)

        # Only check Python files
        if not file_path.endswith(".py"):
            sys.exit(0)

        # Find pyproject.toml
        pyproject_path = find_pyproject_toml(file_path)
        if not pyproject_path:
            sys.exit(0)  # No pyproject.toml found, skip

        # Detect configured type checker
        checker = detect_configured_type_checker(pyproject_path)
        if not checker:
            sys.exit(0)  # No type checker configured, skip

        project_root = pyproject_path.parent

        # Check if file should be type checked
        if not should_check_file(file_path, project_root):
            sys.exit(0)

        # Get type checker command
        cmd_info = get_type_checker_command(checker, project_root)
        if not cmd_info:
            print(f"[type-check-on-edit] {checker} is configured but not available. Install it or add it to your project.", file=sys.stderr)
            sys.exit(0)

        cmd, checker_name = cmd_info

        # Run type checker on the file
        full_cmd = cmd + [file_path]
        try:
            result = subprocess.run(full_cmd, capture_output=True, timeout=30)

            # Report results to AI via stderr
            if result.returncode != 0:
                print(f"[type-check-on-edit] {checker_name} found issues in {file_path}:", file=sys.stderr)

                # Parse and display errors
                output = result.stdout.decode("utf-8", errors="ignore").strip()
                if output:
                    # Show first few lines of output (not overwhelming)
                    lines = output.split("\n")[:10]
                    for line in lines:
                        print(f"  {line}", file=sys.stderr)
                    if len(output.split("\n")) > 10:
                        print(f"  ... ({len(output.split(chr(10)))} total issues)", file=sys.stderr)
            else:
                print(f"[type-check-on-edit] {checker_name} passed for {file_path}", file=sys.stderr)

        except subprocess.TimeoutExpired:
            print(f"[type-check-on-edit] {checker_name} timed out on {file_path}", file=sys.stderr)
        except FileNotFoundError as e:
            print(f"[type-check-on-edit] {checker_name} not found: {e}", file=sys.stderr)

    except json.JSONDecodeError:
        # Invalid JSON input, skip silently
        sys.exit(0)
    except Exception as e:
        print(f"[type-check-on-edit] Error: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
