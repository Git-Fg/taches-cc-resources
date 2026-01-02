---
description: Create meta-prompts that generate optimized prompts for AI agents (Claude Code, GPT-4, Claude, etc.)
argument-hint: <task-description>
allowed-tools: Skill(create-meta-prompts)
---

# Instruction
The user wants to: $ARGUMENTS

1. Immediately invoke the `create-meta-prompts` skill.
2. Pass the user's request ($ARGUMENTS) into the skill invocation.
3. Do not attempt to gather requirements yourself; let the skill handle the intake process.
