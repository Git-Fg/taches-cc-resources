---
description: Analyze context and launch the Debugger Agent with a targeted investigation plan.
argument-hint: [error description]
allowed-tools: Task
---

# Objective
The user needs to debug: $ARGUMENTS

# System Context
- Git Status: ! `git status --short`
- Recent Log: ! `git log -1 --oneline`
- File Tree: ! `find . -maxdepth 2 -not -path '*/.*' -not -path './node_modules*'`

# Instructions
You are a Lead Engineer handing off a task to a Debugging Specialist. Do not debug it yourself. Instead, prepare a **Targeted Investigation Directive**:

1. **Analyze the Context:** Look at the `Git Status`. Are specific files modified? Mention them explicitly.
2. **Refine the Request:**
   - If the user query is vague (e.g., "it's broken"), combine it with the file context (e.g., "The user reports a break, likely related to the modified `auth.ts` file").
   - If the user query is specific, preserve it.
3. **Delegate:** Call the `debugger` subagent with a prompt that includes:
   - The Refined Issue Description.
   - A list of "Suspect Files" based on the git status.
   - The raw system context for reference.

**Example Task Description:**
"Investigate a crash in the Login flow. The user reports failure after recent changes to `src/auth.ts`. Focus your investigation there first. Context: [Raw Data]"
