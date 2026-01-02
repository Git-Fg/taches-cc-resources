---
description: Apply strategic thinking frameworks for decision-making, prioritization, and problem analysis
argument-hint: [framework name or skill name, optional]
allowed-tools: Skill(strategic-thinking), Skill(prioritization), Skill(problem-analysis), Task
---

## Objective

Apply strategic thinking frameworks to help with decision-making, prioritization, and problem analysis.

This command unifies 12 thinking frameworks into 3 cohesive skills:
- strategic-thinking: first-principles, inversion, second-order, swot, 10-10-10
- prioritization: pareto, one-thing, eisenhower-matrix
- problem-analysis: 5-whys, opportunity-cost, occams-razor, via-negativa

## Invocation Modes

### Mode 1: Auto-detect (no argument)

Invoke without arguments: `/brainstorm`
Agent analyzes context and suggests appropriate frameworks

### Mode 2: Specific Framework

Invoke with framework name: `/brainstorm pareto`
Applies only that specific framework

Available frameworks:
- Strategic: first-principles, inversion, second-order, swot, 10-10-10
- Prioritization: pareto, one-thing, eisenhower-matrix
- Problem: 5-whys, opportunity-cost, occams-razor, via-negativa

### Mode 3: Skill-level

Invoke with skill name: `/brainstorm strategic`
Applies frameworks from that skill group:
- `/brainstorm strategic` → strategic-thinking frameworks
- `/brainstorm priority` → prioritization frameworks
- `/brainstorm problem` → problem-analysis frameworks

## Process

### Step 1: Analyze Request

Analyze $ARGUMENTS to determine invocation mode:

IF $ARGUMENTS is empty:
→ Use Task tool to launch brainstormer agent with context analysis

IF $ARGUMENTS contains a framework name:
→ Apply only that specific framework via Skill tool

IF $ARGUMENTS contains a skill keyword:
→ Apply frameworks from that skill via Skill tool

Valid framework names (case-insensitive):
- first-principles, principles, fp
- inversion, invert
- second-order, 2nd, second
- swot
- 10-10-10, 1010, time-horizons
- pareto, 80-20
- one-thing, onething, domino
- eisenhower, matrix
- 5-whys, whys, 5whys
- opportunity-cost, opportunity, cost
- occams-razor, occams, razor
- via-negativa, negativa, subtraction

Valid skill keywords:
- strategic, strategy → strategic-thinking
- priority, prioritize → prioritization
- problem, analysis → problem-analysis

### Step 2: Execute

Based on mode from step 1:

Auto-detect mode:
Use Task tool with subagent_type='general-purpose' and model='opus':
```
Apply strategic thinking frameworks to analyze this situation:

**User Request:** $ARGUMENTS

**Context:**
You are a fresh instance with no prior conversation history.
Use your loaded strategic-thinking skills to:
1. Analyze the user's request
2. Detect which framework(s) would be most helpful
3. Apply those frameworks to provide fresh perspectives

**Available Skills:**
- strategic-thinking: first-principles, inversion, second-order, swot, 10-10-10
- prioritization: pareto, one-thing, eisenhower-matrix
- problem-analysis: 5-whys, opportunity-cost, occams-razor, via-negativa

Provide actionable recommendations based on your analysis.
```

Specific framework mode:
Use Skill tool with the appropriate skill and framework reference:
```
Apply the [framework] framework to: $ARGUMENTS
```

Skill mode:
Use Skill tool with the appropriate skill:
```
Apply strategic thinking frameworks from [skill] to: $ARGUMENTS
```

### Step 3: Present Results

After analysis, present results with:
- Framework(s) applied
- Key insights
- Actionable recommendations
- Suggestion for additional frameworks if relevant

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

Example 1 - Auto-detect:
User: `/brainstorm I'm overwhelmed with too many projects`
Agent detects need for prioritization
Applies pareto + one-thing frameworks

Example 2 - Specific framework:
User: `/brainstorm pareto`
Applies only pareto framework to current context

Example 3 - Skill mode:
User: `/brainstorm strategic`
Agent suggests and applies strategic-thinking frameworks

Example 4 - Framework with context:
User: `/brainstorm first-principles Should I switch careers?`
Applies first-principles framework to career decision

## Success Criteria

- Correct invocation mode detected
- Appropriate framework(s) selected and applied
- Analysis provides fresh perspectives
- Output includes actionable recommendations
- User gains clarity on next steps
