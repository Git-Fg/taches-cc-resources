---
description: Audit and update AI rule files to synchronize them with code changes through systematic interview
argument-hint: [project-path (optional)]
allowed-tools: AskUserQuestion, Read, Write, Edit, Bash, Grep, Glob
---

## Objective
Audit and update AI rule files for the project at $ARGUMENTS. If no project path is provided, the current directory is used.

Synchronize agent configurations (CLAUDE.md, AGENTS.md, GEMINI.md.claude, .agent, .gemini) with the current codebase by identifying discrepancies between rules and actual implementation/requirements.

Keep the same style, tone, syntax and structure of the original files. Rules files must be clear, concise and use strong language. They should be easy to maintain and avoid using too-precise information that may break easily on a small change.

## Context
- Current directory structure: `ls -la $ARGUMENTS`
- AI rules: $ARGUMENTS/CLAUDE.md, $ARGUMENTS/.claude/rules/, $ARGUMENTS/.agent, $ARGUMENTS/.gemini, $ARGUMENTS/.cursor ...

## Process
1. Load and analyze current agent rules
2. Analyze codebase structure for rule-relevant patterns (linting configs, architecture patterns) using your read, bash and glob tools
3. Perform a thorough autonomous exploration of the project state (git status, recent changes, file structure analysis) to form a ground truth BEFORE engaging the user.
4. Use AskUserQuestion to validate your findings and ask for specific direction. Do not just ask open-ended questions; instead, provide informed suggestions to:
   - Improve: Suggest refinements to existing rules based on better patterns observed in code.
   - Synchronize: Point out discrepancies between rules and code and suggest updates to match reality.
   - Complete: Identify missing guidelines for new tools or patterns found in the exploration.
   - Generalize: Suggest broadening specific constraints if the code shows a more flexible pattern.
5. Document all responses and insights
6. Update rule files to create a comprehensive source of truth for the agents

## Success Criteria
- AI agent configuration files (CLAUDE.md, .claude, .agent, .gemini, .cursor ...) accurately reflect project requirements
- All identified discrepancies between code reality and agent rules resolved
- New best practices encoded into rules
