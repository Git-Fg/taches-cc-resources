---
name: run-prompt
description: Delegate one or more prompts to fresh sub-task contexts with parallel or sequential execution
argument-hint: <prompt-number(s)-or-name> [--parallel|--sequential]
allowed-tools: [Read, Task, Bash(ls:*), Bash(mv:*), Bash(git add:*), Bash(git status:*), Bash(git commit:*)]
---

## Context

Git status: ! `git status --short`
Recent prompts: ! `ls -t .prompts/prompts/*.md | head -5`

## Objective

Execute one or more prompts from `.prompts/prompts/` as delegated sub-tasks with fresh context. Supports single prompt execution, parallel execution of multiple independent prompts, and sequential execution of dependent prompts.

## Input

The user will specify which prompt(s) to run via $ARGUMENTS, which can be:

Single prompt:
- Empty (no arguments): Run the most recently created prompt (default behavior)
- A prompt number (e.g., "001", "5", "42")
- A partial filename (e.g., "user-auth", "dashboard")

Multiple prompts:
- Multiple numbers (e.g., "005 006 007")
- With execution flag: "005 006 007 --parallel" or "005 006 007 --sequential"
- If no flag specified with multiple prompts, default to --sequential for safety

## Process

### Step 1: Parse Arguments

Parse $ARGUMENTS to extract:
- Prompt numbers/names (all arguments that are not flags)
- Execution strategy flag (--parallel or --sequential)

Examples:
- "005" → Single prompt: 005
- "005 006 007" → Multiple prompts: [005, 006, 007], strategy: sequential (default)
- "005 006 007 --parallel" → Multiple prompts: [005, 006, 007], strategy: parallel
- "005 006 007 --sequential" → Multiple prompts: [005, 006, 007], strategy: sequential

### Step 2: Resolve Files

For each prompt number/name:
- If empty or "last": Find with `!ls -t .prompts/prompts/*.md | head -1`
- If a number: Find file matching that zero-padded number (e.g., "5" matches "005-_.md", "42" matches "042-_.md")
- If text: Find files containing that string in the filename

Matching rules:
- If exactly one match found: Use that file
- If multiple matches found: List them and ask user to choose
- If no matches found: Report error and list available prompts

### Step 3: Execute

#### Single Prompt

1. Read the complete contents of the prompt file
2. Delegate as sub-task using Task tool with subagent_type="general-purpose"
3. Wait for completion
4. Archive prompt to `.prompts/prompts/completed/` with metadata
5. Commit all work:
   - Stage files YOU modified with `git add [file]` (never `git add .`)
   - Determine appropriate commit type based on changes (fix|feat|refactor|style|docs|test|chore)
   - Commit with format: `[type]: [description]` (lowercase, specific, concise)
6. Return results

#### Parallel Execution

1. Read all prompt files
2. Spawn all Task tools in a SINGLE MESSAGE (this is critical for parallel execution):
   - Use Task tool for prompt 005
   - Use Task tool for prompt 006
   - Use Task tool for prompt 007
   - (All in one message with multiple tool calls)
3. Wait for ALL to complete
4. Archive all prompts with metadata
5. Commit all work:
   - Stage files YOU modified with `git add [file]` (never `git add .`)
   - Determine appropriate commit type based on changes (fix|feat|refactor|style|docs|test|chore)
   - Commit with format: `[type]: [description]` (lowercase, specific, concise)
6. Return consolidated results

#### Sequential Execution

1. Read first prompt file
2. Spawn Task tool for first prompt
3. Wait for completion
4. Archive first prompt
5. Read second prompt file
6. Spawn Task tool for second prompt
7. Wait for completion
8. Archive second prompt
9. Repeat for remaining prompts
10. Archive all prompts with metadata
11. Commit all work:
    - Stage files YOU modified with `git add [file]` (never `git add .`)
    - Determine appropriate commit type based on changes (fix|feat|refactor|style|docs|test|chore)
    - Commit with format: `[type]: [description]` (lowercase, specific, concise)
12. Return consolidated results

## Context Strategy

**CRITICAL: Subagents need ALL relevant context.**

Subagents are like new hires who started 5 seconds ago. They know NOTHING about:
- The project structure or tech stack
- Previous conversation history
- Decisions made earlier
- What files exist or where they are located

**When invoking Task tools, you MUST provide:**

1. **Project State:**
   - What is the tech stack? (Node/Python/Rust/etc.)
   - What frameworks are in use?
   - What is the project structure?

2. **Prompt Contents:**
   - Read the complete prompt file
   - Include the prompt contents in your Task invocation
   - The prompt file should contain context loading instructions (via /create-prompt)

3. **Current Working Directory:**
   - Explicitly state where work should happen
   - Provide paths relative to working directory

4. **Constraints:**
   - What should the subagent NOT do?
   - What patterns must they follow?

**By delegating to a sub-task:** The actual implementation work happens in fresh context while the main conversation stays lean for orchestration and iteration. BUT this only works if you provide complete context in the Task invocation.

**Example Task invocation:**
```
Execute this prompt in a fresh context:

**Project:** Node.js/TypeScript project using Express
**Working Directory:** /path/to/project
**Prompt Contents:** [paste the full prompt file contents here]
**Constraints:** Follow existing code patterns in src/, run tests after changes
```

## Output

### Single Prompt Output

```
✓ Executed: .prompts/prompts/005-implement-feature.md
✓ Archived to: .prompts/prompts/completed/005-implement-feature.md

[Summary of what the sub-task accomplished]
```

### Parallel Output

```
✓ Executed in PARALLEL:

- .prompts/prompts/005-implement-auth.md
- .prompts/prompts/006-implement-api.md
- .prompts/prompts/007-implement-ui.md

✓ All archived to .prompts/prompts/completed/

[Consolidated summary of all sub-task results]
```

### Sequential Output

```
✓ Executed SEQUENTIALLY:

1. .prompts/prompts/005-setup-database.md → Success
2. .prompts/prompts/006-create-migrations.md → Success
3. .prompts/prompts/007-seed-data.md → Success

✓ All archived to .prompts/prompts/completed/

[Consolidated summary showing progression through each step]
```

## Critical Notes

- For parallel execution: ALL Task tool calls MUST be in a single message
- For sequential execution: Wait for each Task to complete before starting next
- Archive prompts only after successful completion
- If any prompt fails, stop sequential execution and report error
- Provide clear, consolidated results for multiple prompt execution
