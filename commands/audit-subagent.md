---
description: Audit subagent configuration for role definition, prompt quality, tool selection, Markdown structure compliance, and effectiveness
argument-hint: <subagent-path-or-name>
---

## Context

Subagent: $ARGUMENTS

Pre-flight checks:
- Agent exists: ! `find .claude/agents agents ~/.claude/agents -name "$(basename "$ARGUMENTS" .md).md" -o -name "$ARGUMENTS" 2>/dev/null | head -1 | xargs test -f && echo "FOUND" || echo "NOT_FOUND"`
- Plugin agents: ! `ls agents/*.md 2>/dev/null | wc -l`
- Project agents: ! `ls .claude/agents/*.md 2>/dev/null | wc -l`
- User agents: ! `ls ~/.claude/agents/*.md 2>/dev/null | wc -l`

## Objective

Invoke the subagent-auditor to audit the subagent at `$ARGUMENTS` for compliance with best practices.

This ensures subagents follow proper structure, role definition, prompt quality, tool selection, and effectiveness patterns.

## Pre-Flight Validation

Before invoking the auditor:

1. **Agent Discovery**
   - If argument is an agent name: Find the actual file
   - If argument is a path: Verify it exists and is an .md file
   - If NOT_FOUND: Ask user for valid agent path/name

2. **Agent Type**
   - Built-in agent: Inform that built-ins cannot be audited
   - User/project/plugin agent: Proceed with audit

## Process

1. **Invoke subagent-auditor** with:
   - Agent path: $ARGUMENTS (resolved to full path)
   - Context from pre-flight checks

2. **Auditor will evaluate:**
   - YAML frontmatter (name, description, tools, model)
   - Role definition clarity
   - Prompt quality and structure
   - Tool appropriateness
   - Workflow specification
   - Constraints definition

3. **Audit output includes:**
   - Assessment summary
   - Critical issues (must-fix)
   - Recommendations (should-fix)
   - Strengths (what works well)
   - Context (agent type, complexity)

## Success Criteria

- Subagent invoked successfully
- Path resolved and validated
- Audit covers all evaluation areas
- Findings include file:line locations
- Contextual judgment applied

## Output Format

```markdown
## Audit Results: [subagent-name]

### Assessment
[1-2 sentence overall assessment]

### Critical Issues (Must Fix)
[Issues that hurt effectiveness]

### Recommendations (Should Fix)
[Improvements for quality]

### Strengths
[What's working well]

### Context
- Subagent type: [simple/complex/delegation]
- Tool access: [appropriate/needs review]
- Estimated effort: [low/medium/high]
```
