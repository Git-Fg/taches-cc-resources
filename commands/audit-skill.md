---
description: Validate and audit a skill for best practices compliance.
argument-hint: <skill-path>
allowed-tools: Task
---

# Objective
Audit the skill: $ARGUMENTS

# Context Injection (Pre-flight)
- Skill exists: ! `test -d "$ARGUMENTS" && echo "VALID" || echo "NOT_FOUND"`
- SKILL.md exists: ! `test -f "$ARGUMENTS/SKILL.md" && echo "EXISTS" || echo "MISSING"`

# Instructions
You are an Audit Coordinator. Prepare the task for the `skill-auditor` agent.

1. **Validate the Checks:**
   - If VALID + EXISTS: Ready for full audit.
   - If VALID + MISSING: SKILL.md is missing (critical issue).
   - If NOT_FOUND: Invalid skill path.

2. **Synthesize the Directive:**
   - If ready: "Audit the skill at `$ARGUMENTS`. Evaluate YAML compliance, structure, and best practices."
   - If MISSING: "The skill directory exists but SKILL.md is missing at `$ARGUMENTS`. This is a critical issue."
   - If NOT_FOUND: "The user wants to audit `$ARGUMENTS` but the path is not valid. Please ask for clarification."

3. **Delegate:** Call the `skill-auditor` subagent with the synthesized directive.
