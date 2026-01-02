---
description: Locate and audit a subagent configuration file.
argument-hint: [agent-name]
allowed-tools: Task
---

# Objective
Audit the subagent: $ARGUMENTS

# Context Injection (Pre-flight)
- Agent Search: ! `find .claude/agents agents ~/.claude/agents -name "$(basename "$ARGUMENTS" .md).md" -o -name "$ARGUMENTS" 2>/dev/null | head -1`

# Instructions
You are an Audit Coordinator. Prepare the task for the `subagent-auditor` agent.

1. **Validate the Search Result:**
   - If the search found a path: Note the file location for the auditor.
   - If the search was empty: The agent will need to ask the user for clarification.

2. **Synthesize the Directive:**
   - If path found: "Audit the subagent at `[found path]`. Evaluate it for best practices compliance."
   - If not found: "The user wants to audit `$ARGUMENTS` but the file was not found in standard locations. Please ask for clarification."

3. **Delegate:** Call the `subagent-auditor` subagent with the synthesized directive.
