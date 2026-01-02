---
description: Create specialized Claude Code subagents with expert guidance
argument-hint: [agent idea or description]
allowed-tools: Skill(create-subagents)
---

# Instruction
The user wants to: $ARGUMENTS

1. Immediately invoke the `create-subagents` skill.
2. Pass the user's request ($ARGUMENTS) into the skill invocation.
3. Do not attempt to gather requirements yourself; let the skill handle the intake process.
