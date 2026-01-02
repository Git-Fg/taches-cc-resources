---
description: Create meta-prompts that generate optimized prompts for AI agents (Claude Code, GPT-4, Claude, etc.)
argument-hint: <task-description>
allowed-tools: Skill(create-meta-prompts)
---

## Objective

Create a meta-prompt: a prompt template that, when given context about a codebase and task, generates an optimized prompt for an AI agent to execute that task.

## Context

Current directory: ! `pwd`
Git status: ! `git status --short`

## Process

1. Invoke the create-meta-prompts skill for: $ARGUMENTS

2. The skill will guide you through creating a meta-prompt that:
   - Takes codebase context as input (file structure, key files, documentation)
   - Takes a task description as input
   - Outputs a highly optimized prompt for an AI agent
   - Is agnostic to the specific AI model being used

3. Meta-prompts are useful for:
   - Generating task-specific prompts from codebase analysis
   - Creating reusable prompt templates for common workflows
   - Building Claude→Claude or other AI→AI pipelines
   - Standardizing prompt generation across teams

## Success Criteria

- Meta-prompt created with clear input/output structure
- Meta-prompt is model-agnostic (works with Claude Code, GPT-4, Claude, etc.)
- Meta-prompt includes instructions for analyzing codebase context
- Meta-prompt produces optimized prompts as output

## Example

Input to meta-prompt:
- Codebase: "React Native e-commerce app with Redux"
- Task: "Add biometric authentication to checkout flow"

Output from meta-prompt:
- Optimized prompt for AI agent with:
  - Relevant files to read (navigation, checkout, auth)
  - Architecture patterns used in the codebase
  - Specific implementation steps
  - Testing requirements
  - Code style conventions

## Guidance
