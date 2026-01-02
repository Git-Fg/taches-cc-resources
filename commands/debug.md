---
description: Apply expert debugging methodology to investigate a specific issue
argument-hint: [issue description]
allowed-tools: Skill(debug-like-expert), Bash
---

## Context

Before invoking the debug skill, gather system context:

- Git Status: ! `git status --short`
- Recent Log: ! `git log -1 --oneline`
- Node Version: ! `node -v || echo "Not Node"`
- Python Version: ! `python3 --version || echo "Not Python"`
- Rust Version: ! `rustc --version || echo "Not Rust"`
- File Tree (Depth 2): ! `find . -maxdepth 2 -not -path '*/.*'`

## Objective

Load the debug-like-expert skill to investigate: $ARGUMENTS

This applies systematic debugging methodology with evidence gathering, hypothesis testing, and rigorous verification.

## Process

1. Gather system context using the bash commands above
2. Invoke the Skill tool with debug-like-expert
3. Pass both the issue description ($ARGUMENTS) AND the gathered system context
4. Follow the skill's debugging methodology
5. Apply rigorous investigation and verification

**Important:** Do not assume the debugger knows what language or environment it is in. Pass the gathered system context to the debug skill.

## Success Criteria

- System context gathered successfully
- Context passed to skill along with issue description
- Skill successfully invoked with full environment details
