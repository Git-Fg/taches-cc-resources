---
description: Audit slash command for YAML frontmatter, argument handling, description clarity, and best practices
argument-hint: <command-path-or-name>
---

## Context

Command: $ARGUMENTS

Pre-flight checks:
- Command exists: ! `find .claude/commands commands ~/.claude/commands -name "$(basename "$ARGUMENTS" .md).md" -o -name "$ARGUMENTS" 2>/dev/null | head -1 | xargs test -f && echo "FOUND" || echo "NOT_FOUND"`
- Plugin commands: ! `ls commands/*.md 2>/dev/null | wc -l`
- Project commands: ! `ls .claude/commands/*.md 2>/dev/null | wc -l`
- User commands: ! `ls ~/.claude/commands/*.md 2>/dev/null | wc -l`

## Objective

Invoke the slash-command-auditor subagent to audit the slash command at `$ARGUMENTS` for compliance with best practices.

This ensures commands follow proper YAML configuration, have clear descriptions, use arguments appropriately, and provide value to users.

## Pre-Flight Validation

Before invoking the auditor, verify:

1. **Command Discovery**
   - If argument is a command name (e.g., "commit"): Find the actual file
   - If argument is a path: Verify it exists and is a .md file
   - If NOT_FOUND: Ask user to provide valid command path/name

2. **Command Type Identification**
   - Built-in command: Inform that built-ins cannot be audited
   - User/project command: Proceed with audit
   - Plugin command: Note the plugin namespace

3. **Scope Assessment**
   - Single command: Direct audit
   - All commands in directory: Ask for confirmation

## Process

1. **Invoke slash-command-auditor subagent** with:
   - Command path: $ARGUMENTS (resolved to full path)
   - Context from pre-flight checks
   - Request for structured findings

2. **Subagent will evaluate:**
   - YAML frontmatter validity (description, allowed-tools, argument-hint)
   - Description quality (clarity, when to use)
   - Argument handling ($ARGUMENTS, $1, $2, etc.)
   - Tool restrictions (allowed-tools appropriateness)
   - Overall value and usefulness

3. **Format the audit output** with:
   - Executive summary
   - Critical issues (invalid YAML, missing required fields)
   - Warnings (unclear descriptions, poor argument use)
   - Suggestions (improvements for value/clarity)
   - Positive observations (what's done well)

## Success Criteria

- Subagent invoked successfully
- Pre-flight validation completed
- Command path resolved correctly
- Audit includes YAML validation
- Audit evaluates description quality
- Audit checks argument handling
- Findings formatted by severity
- Actionable recommendations provided

## Output Format

The audit will be presented as:

```markdown
## Slash Command Audit: [command-name]

### Overall Assessment
[Score/rating and brief summary]

### 🔴 Critical Issues (Must Fix)
1. [Issue] - Line X
   - Problem: [description]
   - Impact: [why this matters]
   - Fix: [specific solution]

### 🟡 Warnings (Should Fix)
[Similar format]

### 🔵 Suggestions (Consider)
[Similar format]

### ✅ Good Practices
[Positive observations]

### Usage Example
[Example of how to use the command effectively]
```
