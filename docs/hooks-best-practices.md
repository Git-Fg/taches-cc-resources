# Hooks Best Practices

This guide covers the best practices for implementing and using Claude Code hooks, based on the official hooks documentation and real-world usage patterns.

## Table of Contents

- [Overview](#overview)
- [Hook Events](#hook-events)
- [Output Modes](#output-modes)
- [Permissive vs Blocking](#permissive-vs-blocking)
- [Security Considerations](#security-considerations)
- [Plugin Hooks](#plugin-hooks)
- [Best Practices](#best-practices)

## Overview

Claude Code hooks are event-driven automation that execute shell commands at specific points during Claude's operation. They provide deterministic control over behavior without relying on LLM choice.

**Key Principles:**
- Hooks run automatically - no need for Claude to "remember" to run them
- Use for validation, formatting, logging, notifications, and custom permissions
- Can block actions (PreToolUse) or observe/modify (PostToolUse)

## Hook Events

### PreToolUse
Runs before tool execution. Can block or allow the action.

**Common Uses:**
- File validation (protect sensitive files)
- Content scanning (detect secrets)
- Input sanitization
- Custom permissions

**Output Options:**
- Exit code 0 with JSON: Allow with warning/context
- Exit code 2 with stderr: Block the action

### PostToolUse
Runs after tool completion. Cannot block (action already happened).

**Common Uses:**
- Auto-formatting code
- Logging/auditing
- Type checking
- Notifications

**Output:**
- Exit code 0: Success (log to stderr for visibility)

### UserPromptSubmit
Runs when user submits a prompt, before Claude processes it.

**Common Uses:**
- Add project context
- Validate prompts
- Block certain types of requests

### Stop/SubagentStop
Runs when Claude or subagent finishes.

**Common Uses:**
- Intelligent continuation logic
- Task completion verification

## Output Modes

### Exit Code Mode (Simple)

| Exit Code | Behavior | Use Case |
|-----------|----------|----------|
| 0 | Success | Allow action, provide context |
| 2 | Blocking | Block action, show stderr to Claude |
| Other | Non-blocking error | Show stderr in verbose mode |

### JSON Output Mode (Advanced)

For PreToolUse hooks, JSON output provides structured control:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "Warning message..."
  }
}
```

**Decision Values:**
- `"allow"` - Approve the action (bypasses permission dialog)
- `"deny"` - Block the action (Claude sees the reason)
- `"ask"` - Prompt the user to confirm

**Additional Fields:**
- `updatedInput` - Modify tool parameters before execution
- `suppressOutput` - Hide hook output from transcript
- `systemMessage` - Show warning message to user

## Permissive vs Blocking

### Permissive Mode (Recommended)

Hooks warn but allow actions to proceed. Uses JSON output with `permissionDecision: "allow"`.

**Benefits:**
- User remains in control
- Claude sees context and can adjust
- No workflow interruption
- False positives don't block work

**Example:**
```python
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "permissionDecisionReason": "[security-check] WARNING: Potential API key detected"
    }
}
print(json.dumps(output))
sys.exit(0)
```

### Blocking Mode

Hooks use exit code 2 to completely block actions.

**Use Cases:**
- Critical security violations
- Destructive operations in production
- Hard constraints that must be enforced

**Example:**
```python
print("[security-check] BLOCKED: Real secret detected", file=sys.stderr)
sys.exit(2)
```

**Drawbacks:**
- Can interrupt legitimate work
- False positives block progress
- Requires user intervention

## Security Considerations

### Input Validation

Always validate and sanitize input from hook stdin:

```python
# Bad - doesn't validate file path
file_path = input_data.get('tool_input', {}).get('file_path', '')

# Good - validates path is within project
from pathlib import Path
project_root = Path.cwd())
file_path = Path(file_path).resolve()
try:
    file_path.relative_to(project_root)
except ValueError:
    sys.exit(0)  # Outside project, skip
```

### Path Traversal Prevention

Check for `..` in paths and validate against project root:

```python
if '..' in file_path or file_path.startswith('/'):
    sys.exit(0)  # Skip suspicious paths
```

### Command Injection Prevention

Always use shell-safe patterns:

```python
# Bad - vulnerable to injection
os.system(f"format {file_path}")

# Good - uses subprocess with list arguments
subprocess.run(['formatter', file_path])
```

### Sensitive Data Handling

Never log or output sensitive data:

```python
# Bad - logs content
print(f"Content: {content}", file=sys.stderr)

# Good - only logs metadata
print(f"Checked {file_path} - {len(content)} bytes", file=sys.stderr)
```

## Plugin Hooks

Plugin hooks are defined in `hooks/hooks.json` and use `${CLAUDE_PLUGIN_ROOT}` for paths.

### Structure

```json
{
  "description": "Plugin hooks description",
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "python3 ${CLAUDE_PLUGIN_ROOT}/hooks/scripts/script.py"
          }
        ]
      }
    ]
  }
}
```

### Environment Variables

- `${CLAUDE_PLUGIN_ROOT}` - Plugin directory
- `${CLAUDE_PROJECT_DIR}` - Project root directory
- Standard environment variables available

### uv Integration

Use `uv run` with fallback to `python3`:

```json
{
  "command": "sh -c 'command -v uv >/dev/null 2>&1 && uv run ${CLAUDE_PLUGIN_ROOT}/hooks/scripts/script.py || python3 ${CLAUDE_PLUGIN_ROOT}/hooks/scripts/script.py'"
}
```

## Best Practices

### 1. Use Specific Exception Handling

```python
# Bad - catches everything
try:
    input_data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

# Good - specific exceptions
try:
    input_data = json.load(sys.stdin)
except json.JSONDecodeError:
    sys.exit(0)  # Invalid JSON
except Exception as e:
    print(f"Unexpected error: {e}", file=sys.stderr)
    sys.exit(0)
```

### 2. Provide Clear Feedback

Use `[hook-name]` prefix for stderr messages:

```python
print(f"[security-check] WARNING: Potential secret detected", file=sys.stderr)
print(f"[format-on-edit] Ran prettier on {file_path}", file=sys.stderr)
```

### 3. Check Tool Availability Before Running

```python
def check_command_available(cmd: str) -> bool:
    return shutil.which(cmd) is not None

if check_command_available('ruff'):
    subprocess.run(['ruff', 'check', '--fix', file_path])
```

### 4. Use Appropriate Timeouts

```python
# Format operations: 10 seconds
subprocess.run(cmd, timeout=10)

# Type checking: 30 seconds
subprocess.run(cmd, timeout=30)

# Fast checks: 5 seconds
subprocess.run(cmd, timeout=5)
```

### 5. Handle Missing Input Gracefully

```python
file_path = input_data.get('tool_input', {}).get('file_path', '')
if not file_path:
    sys.exit(0)  # No file path, skip
```

### 6. Use Type Hints

```python
from typing import Optional

def matches_pattern(file_path: str, patterns: list[str]) -> Optional[str]:
    """Check if file matches any pattern. Returns matching pattern or None."""
    ...
```

### 7. Document Hook Behavior

Include docstring with:
- Purpose
- Trigger events
- Output behavior
- Exit codes used

```python
"""
Pre-edit security check hook.
Scans file content for potential secrets before allowing edits.

Trigger: PreToolUse on Edit/Write
Output: JSON with permissionDecision: "allow" + warning
Exit: 0 (always - permissive mode)
"""
```

### 8. Test Hooks Manually

```bash
# Test with JSON input
echo '{"tool_input":{"file_path":"test.py"}}' | python3 hooks/scripts/script.py

# Check for syntax errors
python3 -m py_compile hooks/scripts/script.py

# Validate JSON config
jq . hooks/hooks.json
```

### 9. Use Non-Blocking for PostToolUse

PostToolUse hooks cannot block (action already happened). Use exit code 0:

```python
# PostToolUse - always exit 0
result = subprocess.run(cmd)
if result.returncode != 0:
    print(f"[hook] Issues found", file=sys.stderr)
sys.exit(0)  # Don't block
```

### 10. Prefer Permissive Mode for PreToolUse

Use `permissionDecision: "allow"` with warnings instead of blocking:

```python
# Recommended - warn but allow
output = {
    "hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "allow",
        "permissionDecisionReason": "Warning message"
    }
}
print(json.dumps(output))
sys.exit(0)
```

## Troubleshooting

### Hook Not Running

1. Check JSON syntax: `jq . hooks/hooks.json`
2. Verify matcher pattern matches tool name
3. Check script is executable: `chmod +x script.py`
4. Use `claude --debug` to see hook execution

### Hook Blocking Unexpectedly

1. Check exit codes - should be 0 for permissive mode
2. Review stderr output
3. Test manually with sample input

### Performance Issues

1. Add appropriate timeouts
2. Use fast commands (ripgrep vs grep)
3. Skip unnecessary checks (test files, node_modules)
4. Consider async for long-running operations

## Example Hook

```python
#!/usr/bin/env python3
"""
Example permissive hook that warns but allows.
"""
import json
import sys
import re

def main():
    try:
        input_data = json.load(sys.stdin)
        file_path = input_data.get('tool_input', {}).get('file_path', '')
        content = input_data.get('tool_input', {}).get('content', '')

        if not file_path or not content:
            sys.exit(0)

        # Check for pattern
        if re.search(r'API_KEY\s*=\s*["\']?[a-zA-Z0-9]{20,}', content):
            warning = f"[example-hook] WARNING: Potential API key in {file_path}"
            output = {
                "hookSpecificOutput": {
                    "hookEventName": "PreToolUse",
                    "permissionDecision": "allow",
                    "permissionDecisionReason": warning
                }
            }
            print(json.dumps(output))

    except json.JSONDecodeError:
        sys.exit(0)
    except Exception as e:
        print(f"[example-hook] Error: {e}", file=sys.stderr)

    sys.exit(0)

if __name__ == '__main__':
    main()
```

## References

- [Official Hooks Documentation](https://code.claude.com/docs/hooks)
- [Hooks Reference](https://code.claude.com/docs/hooks-reference)
- [thecattoolkit Hooks](../hooks/)
