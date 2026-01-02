# Description Guidelines for AI Agent Discoverability

This document establishes the standard for writing descriptions that AI agents can autonomously discover and invoke.

## The A+D Hybrid Methodology

**Primary Pattern** (80% of tools):
```
[CALLING_CONDITION] when [primary_condition].
```

**Enhanced Pattern** (20% of tools with complex activation logic):
```
[CALLING_CONDITION] when [primary_condition]. Secondary: [edge_case_1], [edge_case_2].
```

## Calling Conditions Hierarchy

| Strength | Pattern | When to Use |
|----------|--------|-------------|
| **Strongest** | MUST USE | Critical tools, debugging errors, creation tasks |
| **Strong** | ALWAYS USE | Post-action requirements, standards compliance |
| **Medium** | PROACTIVELY USE | Proactive optimization, strategic tasks |

## Writing Guidelines

### 1. Trigger-First Approach

Start with WHEN to activate, not WHAT it does.

**Bad**: "Analyze context and launch the Debugger Agent"
**Good**: "MUST USE when investigating bugs, errors, or unexpected behavior requiring systematic root cause analysis."

### 2. Concrete Triggers

Use specific conditions ("when errors occur") not abstract descriptions ("for problems").

**Bad**: "for deep analysis"
**Good**: "when standard troubleshooting fails"

### 3. Strong Calling Conditions

Always include MUST/ALWAYS/PROACTIVELY USE to create unambiguous activation signals.

**Bad**: "Analyze context and launch..."
**Good**: "MUST USE when investigating bugs..."

### 4. Optimize Length

Target: 8-15 words for primary condition. Balance brevity with clarity.

**Bad**: "This tool analyzes context and launches an agent that performs investigation..."
**Good**: "MUST USE when investigating bugs requiring systematic root cause analysis."

### 5. Mutual Exclusivity

Ensure each description is mutually exclusive with alternatives. Avoid overlapping conditions.

## Decision Tree

```
Start: What is the SINGLE most important trigger condition?
    ↓
Can you express it in one clear clause?
    ↓ YES → Use Primary Pattern: "MUST/ALWAYS/PROACTIVELY USE when [condition]."
    ↓ NO
    ↓
Are there 2-3 well-defined edge cases?
    ↓ YES → Use Enhanced Pattern: Add "Secondary: [edge cases]"
    ↓ NO
    ↓
Simplify the tool's scope or split into multiple tools
```

## Validation Checklist

Before finalizing a description:

- [ ] Does it start with MUST/ALWAYS/PROACTIVELY USE?
- [ ] Is the primary condition a single clear clause?
- [ ] Is the condition mutually exclusive with other tools?
- [ ] Are secondary conditions (if any) truly necessary?
- [ ] Is total description under 25 words?
- [ ] Would a binary decision (condition met? yes/no) work?

## Examples

### Commands

| Command | Before | After |
|---------|--------|-------|
| `/debug` | "Analyze context and launch the Debugger Agent..." | "MUST USE when investigating bugs, errors, or unexpected behavior requiring systematic root cause analysis. Secondary: recurring issues, intermittent failures, production outages." |
| `/review` | "Summarize changes and launch the Code Reviewer..." | "ALWAYS USE after completing code changes to review quality, identify issues, and ensure standards compliance. Secondary: before merging PRs, when refactoring, after implementing features." |
| `/brainstorm` | "Frame the user's problem and launch the Brainstormer..." | "PROACTIVELY USE for complex problems requiring structured thinking frameworks, multi-perspective analysis, or strategic insight. Secondary: ambiguous challenges, decisions with trade-offs, situations requiring creative solutions." |

### Skills

| Skill | Before | After |
|-------|--------|-------|
| `api-design` | "Expert guidance for REST and GraphQL API design..." | "MUST USE when designing APIs, creating endpoints, defining error handling, or asked about API patterns. Secondary: planning API versioning, structuring responses, or documenting REST/GraphQL interfaces." |
| `testing-strategy` | Already good | Already good - has "PROACTIVELY USE when..." |

### Subagents

| Subagent | Before | After |
|----------|--------|-------|
| `plan-executor` | "Specialized agent for executing project plans..." | "MUST USE when executing PLAN.md files created by the planning system. Secondary: running plan-executor agent, executing phase plans, or implementing planned tasks. Automatically loads project context..." |

## What to Avoid

### Methodology B: Intent-Based (Avoid)

```
❌ "For debugging issues and investigating problems, use this to launch systematic investigation..."
```

**Why**: Intent matching is subjective and error-prone. Agents hesitate without explicit activation signals.

### Methodology C: Keyword Density (Avoid)

```
❌ "Debug investigate error bug crash failure root cause analyze systematic troubleshooting..."
```

**Why**: Keyword bloat encourages verbose descriptions, causes false positives, and is unmaintainable.

### Weak Verbs (Avoid)

```
❌ "Analyze context..."
❌ "Summarize changes..."
❌ "Frame the problem..."
```

**Why**: These describe process, not trigger. Use domain-specific imperatives instead.

## Anti-Patterns

1. **Process descriptions**: "and launch the X agent" - redundant, implied by tool type
2. **Hedge words**: "helps with", "can be used for" - weak, ambiguous
3. **Generic triggers**: "for problems", "for analysis" - could apply to anything
4. **Missing calling condition**: No MUST/ALWAYS/PROACTIVELY USE - agents hesitate
5. **Overlapping conditions**: Two tools with similar "MUST USE when debugging" - creates conflicts

## Implementation Notes

- **Commands** in `commands/*.md`: Edit `description` field in YAML frontmatter
- **Skills** in `skills/*/SKILL.md`: Edit `description` field in YAML frontmatter
- **Subagents** in `agents/*.md`: Edit `description` field in YAML frontmatter

## Related Skills

- `/audit-skill`: Audit skills for best practices compliance
- `/audit-subagent`: Audit subagents for best practices compliance
- `/audit-slash-command`: Audit commands for best practices compliance

## Version History

- **2026-01-02**: Initial version created based on brainstorming analysis comparing description methodologies.
