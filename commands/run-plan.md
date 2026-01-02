---
description: Execute a PLAN.md file with full project context (BRIEF, ROADMAP)
argument-hint: <plan-path>
allowed-tools: [Read, Write, Task, Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(ls:*)]
---

## Objective

Execute the plan at `$ARGUMENTS` using the context-aware plan-executor agent.

## Process

1. **Verify plan exists:**
   ```bash
   test -f "$ARGUMENTS" || echo "Plan not found: $ARGUMENTS"
   ```

2. **Check if already executed:**
   ```bash
   test -f "$(dirname "$ARGUMENTS")/SUMMARY.md" && echo "Plan already executed (SUMMARY.md exists)"
   ```

3. **Invoke plan-executor agent:**
   Use Task tool with subagent_type="general-purpose" and model="sonnet":
   ```
   Execute the plan located at: $ARGUMENTS

   CRITICAL: Follow your Context Loading protocol explicitly:

   **1. HYDRATE CONTEXT (MANDATORY - Do This First):**
   You are a new instance and know NOTHING about this project.
   Before doing ANY work, you MUST read these files to understand architecture and vision:
   - Read `.prompts/planning/BRIEF.md` for project vision and constraints
   - Read `.prompts/planning/ROADMAP.md` for architecture and phase structure
   - Read any files listed in the plan's `## Execution Context` section

   **2. PARSE PLAN STRUCTURE:**
   The plan uses Markdown structure (NOT XML tags):
   - `# Objective` - The goal
   - `## Execution Context` - Files to read before starting
   - `## Tasks` - Checkbox list of actions
   - `**[CHECKPOINT]**` - Items requiring human verification
   - `## Success Criteria` - Definition of done

   **3. EXECUTE:**
   - Perform Context Hydration: read files mentioned in the plan
   - Execute all tasks sequentially
   - Create SUMMARY.md when complete
   - Update ROADMAP.md to mark plan complete
   - Commit changes with format: `feat({phase}-{plan}): [summary]`

   If the path provided is relative (e.g., "01-auth/PLAN.md" or "phases/01-auth/PLAN.md"),
   look inside `.prompts/planning/` for the file.
   ```

4. **Monitor completion:**
   - Wait for agent to complete
   - Verify SUMMARY.md was created
   - Verify git commit was successful

5. **Report completion:**
   - Show SUMMARY.md contents
   - Display commit hash
   - Suggest next steps based on ROADMAP

## Constraints

- The plan-executor agent handles all context loading automatically
- Do NOT manually read BRIEF.md or ROADMAP.md in this command
- Let the agent establish full context before execution
- Trust the agent's Context Loading protocol

## Success Criteria

- Plan executed by plan-executor agent
- SUMMARY.md created in plan directory
- Git commit successful
- User receives completion report with next steps
