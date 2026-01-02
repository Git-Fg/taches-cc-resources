---
description: Apply strategic thinking and problem-solving frameworks to any query, decision, or problem. Acts as an intelligent scratchpad for structured thought, leveraging powerful mental models.
argument-hint: [query or framework name, optional]
allowed-tools: Task
---

## Objective

Delegate any query, problem, or decision to the `brainstormer` subagent for structured thinking using its powerful mental models and frameworks. This command serves as a unified entry point for all thinking processes.

## Invocation Modes

This command supports various ways to engage the `brainstormer` agent:

### Mode 1: Auto-detect (no argument or general query)
**Usage**: `/brainstorm` or `/brainstorm How could I better leverage type safety?`
The `brainstormer` agent will analyze your request and automatically select the most appropriate framework(s) to apply.

### Mode 2: Specific Framework
**Usage**: `/brainstorm pareto` or `/brainstorm first-principles What's the core issue here?`
Applies only the specific framework you name to your query.

Available frameworks:
- **Strategic**: first-principles, inversion, second-order, swot, 10-10-10
- **Prioritization**: pareto, one-thing, eisenhower-matrix
- **Problem**: 5-whys, opportunity-cost, occams-razor, via-negativa

### Mode 3: Skill-level
**Usage**: `/brainstorm strategic` or `/brainstorm problem How can I simplify this system?`
Applies frameworks from the specified skill group:
- `/brainstorm strategic` → Strategic Thinking frameworks
- `/brainstorm priority` → Prioritization frameworks
- `/brainstorm problem` → Problem Analysis frameworks

## Process

### Step 1: Delegate to Brainstormer Agent

The `brainstormer` agent is designed to handle all internal logic for framework selection and application. Your role here is to pass the user's `$ARGUMENTS` directly to this agent.

Use Task tool with `subagent_type='brainstormer'`:

```
Execute a thinking session:

**User Request for Brainstormer:** $ARGUMENTS

**Context for Brainstormer Agent:**
You are acting as the `brainstormer` agent. Your core task is to apply your loaded skills (strategic-thinking, prioritization, problem-analysis) to the user's request.
- If the user provided a specific framework name (e.g., 'pareto', 'first-principles') within the request, identify and apply only that framework.
- If the user provided a skill keyword (e.g., 'strategic', 'priority', 'problem') within the request, apply relevant frameworks from that skill.
- If no specific framework or skill was explicitly mentioned in the request, auto-detect the most helpful framework(s) based on the content of the request.

Provide actionable recommendations and insights based on your analysis.
```

### Step 2: Present Results

The `brainstormer` agent will return a structured output, which you should present directly to the user.

## Framework Quick Reference

Strategic Thinking (5 frameworks):
- first-principles: Challenge assumptions, rebuild from fundamentals
- inversion: Identify failure modes to avoid
- second-order: Understand consequences of consequences
- swot: Strategic positioning (Strengths/Weaknesses/Opportunities/Threats)
- 10-10-10: Time horizon analysis (10 min, 10 mo, 10 yr)

Prioritization (3 frameworks):
- pareto: 80/20 rule - vital few that drive majority of results
- one-thing: Highest leverage action that makes others easier
- eisenhower-matrix: Urgent vs important categorization

Problem Analysis (4 frameworks):
- 5-whys: Root cause drilling
- opportunity-cost: Trade-off analysis
- occams-razor: Simplest explanation
- via-negativa: Improve by removing

## Examples

**Example 1 - Auto-detect (Technical Problem):**
User: `/brainstorm How could I better leverage type safety in my Go application?`
Agent applies `first-principles` (what are the core truths of type safety?) + `inversion` (what would cause type safety to fail?) to generate insights.

**Example 2 - Auto-detect (Problem Solving):**
User: `/brainstorm We are frequently seeing performance regressions after new deployments.`
Agent applies `5-whys` (root cause analysis) + `second-order` (ripple effects of deployments) + `occams-razor` (simplest explanation) to diagnose.

**Example 3 - Specific framework with context:**
User: `/brainstorm pareto What are the 20% of features that deliver 80% of value in our new mobile app MVP?`
Agent applies the Pareto framework to identify high-impact features.

**Example 4 - Skill mode (Strategic Context):**
User: `/brainstorm strategic Should we pivot our product direction?`
Agent applies frameworks from the Strategic Thinking skill to guide the decision.

## Success Criteria

- Correct invocation mode detected (explicit framework/skill or auto-detect).
- Request is successfully delegated to the `brainstormer` subagent.
- The `brainstormer` agent provides a structured output with insights and recommendations.
- User receives clarity and a structured approach to their problem.
