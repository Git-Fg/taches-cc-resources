---
description: Create or edit Claude Code skills with expert guidance on structure and best practices
allowed-tools: Skill(create-agent-skills), Read, Write, Bash
argument-hint: [skill description or requirements]
---

## Objective

Create a new AI agent skill or improve an existing one with expert guidance.

## Context

Current directory: ! `pwd`

## Process

1. Invoke the create-agent-skills skill for: $ARGUMENTS

2. The skill will guide through the complete process with intake and routing

3. After skill completes, offer to help with:
   - Creating the directory structure
   - Writing initial files based on skill's output

## Guidance

Other creation commands:
- /create-plan - Hierarchical project planning
- /create-meta-prompt - AI→Claude pipelines
- /create-prompt - Single prompts
- /create-subagent - Specialized agents
- /create-slash-command - Commands
- /create-hook - Automation
