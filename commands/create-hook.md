---
description: Invoke create-hooks skill for expert guidance on Claude Code hook development
allowed-tools: Skill(create-hooks)
argument-hint: [hook requirements]
---

# Instruction
The user wants to: $ARGUMENTS

1. Immediately invoke the `create-hooks` skill.
2. Pass the user's request ($ARGUMENTS) into the skill invocation.
3. Do not attempt to gather requirements yourself; let the skill handle the intake process.
