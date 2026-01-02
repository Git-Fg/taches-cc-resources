---
description: Audit skill for YAML compliance, Markdown structure, progressive disclosure, and best practices
argument-hint: <skill-path>
---

## Context

Skill path: $ARGUMENTS

Pre-flight checks:
- Skill exists: ! `test -d "$ARGUMENTS" && echo "VALID" || echo "NOT_FOUND"`
- SKILL.md exists: ! `test -f "$ARGUMENTS/SKILL.md" && echo "EXISTS" || echo "MISSING"`
- File count: ! `find "$ARGUMENTS" -name "*.md" -type f | wc -l`
- Git status: ! `git status --short "$ARGUMENTS" 2>/dev/null || echo "NOT_TRACKED"`

## Objective

Invoke the skill-auditor subagent to audit the skill(s) at `$ARGUMENTS` for compliance with Agent Skills best practices.

This ensures skills follow proper structure (Markdown headings, required sections, progressive disclosure) and effectiveness patterns.

## Pre-Flight Validation

Before invoking the auditor, verify:

1. **Path Accessibility**
   - If skill path is NOT_FOUND: Ask user to provide valid skill path
   - If SKILL.md is MISSING: Warn that this is a critical issue

2. **Scope Assessment**
   - Single skill: Direct audit of provided path
   - Multiple skills: Ask if user wants to audit all or specific one

## Process

1. **Invoke skill-auditor subagent** with:
   - Skill path: $ARGUMENTS
   - Context from pre-flight checks
   - Request for structured findings

2. **Subagent will:**
   - Read best practices and evaluate the skill
   - Check all related files in skill directory
   - Provide detailed findings with file:line locations

3. **Format the audit output** with:
   - Executive summary (overall score/rating)
   - Critical issues (must fix)
   - Warnings (should fix)
   - Suggestions (consider improving)
   - Positive observations (what's done well)

## Success Criteria

- Subagent invoked successfully
- Pre-flight validation completed
- Audit includes YAML evaluation
- Audit includes structural assessment
- Findings are formatted by severity
- Actionable recommendations provided

## Output Format

The audit will be presented as:

```markdown
## Skill Audit: [skill-name]

### Overall Assessment
[Score/rating and brief summary]

### 🔴 Critical Issues (Must Fix)
1. [Issue] - `file:line`
   - Problem: [description]
   - Impact: [why this matters]
   - Fix: [specific solution]

### 🟡 Warnings (Should Fix)
[Similar format]

### 🔵 Suggestions (Consider)
[Similar format]

### ✅ Good Practices
[Positive observations]
```
