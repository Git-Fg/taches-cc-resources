---
description: Summarize changes and launch the Code Reviewer agent.
argument-hint: [focus area, optional]
allowed-tools: Task
---

# User Focus
$ARGUMENTS

# Change Context
! `git diff --stat HEAD~1`

# Instructions
You are the Review Manager. Prepare a briefing for the `code-reviewer` agent.

1. **Analyze the Diff:** Look at the `git diff` output above. Which modules or directories are heavily impacted? (e.g., "Heavy changes in `src/api`").

2. **Synthesize the Directive:**
   - Combine the User's Focus (if any) with the Diff Reality.
   - Formulate a prompt like: "Review the recent changes, focusing specifically on the heavy edits in `src/api`. The user is particularly concerned about [User Focus]."

3. **Delegate:** Call the `code-reviewer` subagent with this synthesized briefing.
