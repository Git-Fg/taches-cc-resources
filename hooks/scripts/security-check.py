#!/usr/bin/env python3
"""
Pre-commit security check hook.
Warns about edits that might contain secrets or security issues.
All edits are allowed but warnings are shown to Claude.

Uses JSON output with permissionDecision: "allow" to warn without blocking.
"""
import json
import re
import sys
import os

# Patterns that indicate potential secrets
SECRET_PATTERNS = [
    (r'(?i)(api[_-]?key|apikey)\s*[:=]\s*["\']?[a-zA-Z0-9_-]{20,}', "API key"),
    (r'(?i)(secret|password|passwd|pwd)\s*[:=]\s*["\'][^"\']+["\']', "Password/Secret"),
    (r"(?i)bearer\s+[a-zA-Z0-9_-]{20,}", "Bearer token"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub Personal Access Token"),
    (r"github_pat_[a-zA-Z0-9]{22}_[a-zA-Z0-9]{59}", "GitHub PAT (fine-grained)"),
    (r"sk-[a-zA-Z0-9]{48}", "OpenAI API Key"),
    (r"sk-ant-[a-zA-Z0-9-]{90,}", "Anthropic API Key"),
    (r"-----BEGIN (?:RSA |EC |DSA )?PRIVATE KEY-----", "Private key"),
    (r"(?i)aws[_-]?access[_-]?key[_-]?id\s*[:=]\s*[A-Z0-9]{20}", "AWS Access Key"),
    (r"(?i)aws[_-]?secret[_-]?access[_-]?key\s*[:=]\s*[a-zA-Z0-9/+=]{40}", "AWS Secret Key"),
]

# Files to always skip
SKIP_FILES = {
    ".env.example",
    ".env.template",
    ".env.sample",
    "package-lock.json",
    "yarn.lock",
    "pnpm-lock.yaml",
}


def check_for_secrets(content: str, file_path: str) -> list[str]:
    """Check content for potential secrets. Returns list of detected issues."""
    issues = []

    # Skip certain files
    if os.path.basename(file_path) in SKIP_FILES:
        return issues

    # Skip test files checking for secret patterns
    if "test" in file_path.lower() or "spec" in file_path.lower():
        return issues

    for pattern, secret_type in SECRET_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            issues.append(f"Potential {secret_type} detected")

    return issues


def main():
    try:
        input_data = json.load(sys.stdin)
        tool_input = input_data.get("tool_input", {})

        # Get file path and content based on tool type
        file_path = tool_input.get("file_path", "")
        content = tool_input.get("content", "") or tool_input.get("new_string", "")

        if not file_path or not content:
            sys.exit(0)

        issues = check_for_secrets(content, file_path)

        if issues:
            issues_text = "\n".join(f"  - {issue}" for issue in issues)
            warning = (
                f"[security-check] WARNING: Potential security issue detected in {file_path}:\n"
                f"{issues_text}\n"
                f"[security-check]   Please verify this is not a real secret before committing.\n"
                f"[security-check]   If this is a false positive, review and adjust patterns in security-check.py"
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
    except Exception:
        # Don't block on errors
        sys.exit(0)


if __name__ == "__main__":
    main()
