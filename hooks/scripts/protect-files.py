#!/usr/bin/env python3
"""
Protect sensitive files from modification.
Warns about edits to production configs, lock files, and sensitive directories.
All edits are allowed but warnings are shown to Claude.
"""
import fnmatch
import json
import logging
import os
import sys
from typing import Optional

logger = logging.getLogger(__name__)

# Files/patterns to warn about (previously blocked, now allowed with warning)
PROTECTED_PATTERNS = [
    # Lock files (usually shouldn't be manually edited)
    'package-lock.json',
    'yarn.lock',
    'pnpm-lock.yaml',
    'Gemfile.lock',
    'poetry.lock',
    'Cargo.lock',

    # Sensitive files
    '.env',
    '.env.local',
    '.env.production',
    'secrets/*',
    '*/secrets/*',
    '*/*/secrets/*',
    'credentials/*',
    '*/credentials/*',
    '*/*/credentials/*',

    # Git internals
    '.git/*',
]

# Files that should warn but not block
WARN_PATTERNS = [
    '.github/workflows/*',
    'docker-compose.yml',
    'Dockerfile',
    'production/*',
    '*/production/*',
    '*/*/production/*',
]


def contains_path_traversal(file_path: str) -> bool:
    """Check if file path contains path traversal attempts."""
    # Check for .. in path components
    if '..' in file_path.split(os.sep):
        return True
    # Also check for URL-encoded traversal
    if '%2e%2e' in file_path.lower() or '%2E%2E' in file_path.lower():
        return True
    return False


def matches_pattern(file_path: str, patterns: list[str]) -> Optional[str]:
    """Check if file matches any protected pattern. Returns matching pattern or None."""
    # Remove leading ./ if present (but don't use lstrip which removes individual chars)
    if file_path.startswith('./'):
        file_path = file_path[2:]
    for pattern in patterns:
        if fnmatch.fnmatch(file_path, pattern):
            return pattern
        if fnmatch.fnmatch(os.path.basename(file_path), pattern):
            return pattern
    return None


def main():
    try:
        input_data = json.load(sys.stdin)
        file_path = input_data.get('tool_input', {}).get('file_path', '')

        # Input validation
        if not file_path:
            sys.exit(0)

        # Security: Check for path traversal attempts (log and skip silently)
        if contains_path_traversal(file_path):
            logger.debug("[protect-files] Path traversal detected: %s", file_path)
            sys.exit(0)

        # Check for protected patterns (previously blocked, now warn only)
        blocked = matches_pattern(file_path, PROTECTED_PATTERNS)
        if blocked:
            warning = (
                f"[protect-files] WARNING: Editing protected file {file_path}\n"
                f"[protect-files]   Matches protected pattern: {blocked}\n"
                f"[protect-files]   This file type should generally not be manually edited."
            )
            output = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "allow",
                    "permissionDecisionReason": warning
                }
            }
            print(json.dumps(output))
            sys.exit(0)

        # Check for warning patterns
        warned = matches_pattern(file_path, WARN_PATTERNS)
        if warned:
            warning = (
                f"[protect-files] NOTE: Editing sensitive file {file_path}\n"
                f"[protect-files]   Matches pattern: {warned}"
            )
            output = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "allow",
                    "permissionDecisionReason": warning
                }
            }
            print(json.dumps(output))
            sys.exit(0)

    except json.JSONDecodeError:
        # Invalid JSON input, don't block
        sys.exit(0)
    except Exception as e:
        # Don't block on errors, but log for debugging
        logger.debug("[protect-files] Unexpected error: %s", e, exc_info=True)
        sys.exit(0)


if __name__ == '__main__':
    main()
