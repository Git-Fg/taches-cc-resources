---
description: Create or edit a skill using the expert workflow.
allowed-tools: Skill(create-agent-skills)
argument-hint: [description of skill to build]
---

# Instruction
The user wants to: $ARGUMENTS

1. Immediately invoke the `create-agent-skills` skill.
2. Pass the user's request ($ARGUMENTS) into the skill invocation.
3. Do not attempt to gather requirements yourself; let the skill handle the intake process.
