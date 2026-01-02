---
name: prioritization
description: Prioritization frameworks for focusing resources on high-impact activities. PROACTIVELY USE when overwhelmed with tasks, need clarity on what to do first, or struggling with focus.
---

# Objective

Provide prioritization frameworks that help focus resources on high-impact activities and reduce overwhelm.

These frameworks help you identify what actually matters, cut through noise, and direct effort toward maximum results.

# Frameworks Index

The prioritization skill includes these frameworks:

- pareto: Apply 80/20 rule to identify vital few factors that drive majority of results. Use when overwhelmed or needing to cut through noise.

- one-thing: Identify single highest-leverage action that makes everything else easier or unnecessary. Use for finding domino actions.

- eisenhower-matrix: Categorize by urgency vs importance (Do First, Schedule, Delegate, Eliminate). Use for task triage and reducing overwhelm.

# Routing Logic

When to use each framework:

- Use **pareto** when: Overwhelmed with many technical issues (e.g., bugs, performance bottlenecks, tech debt) and needing to identify the 20% that cause 80% of the problems. Applicable to prioritizing test cases, refactoring tasks, or security vulnerabilities. Also useful for feature prioritization and resource allocation.

- Use **one-thing** when: A complex technical goal requires a 'domino' action, such as identifying the single most impactful refactoring, the crucial first step in a large migration, or the core component that unlocks multiple features. Also applicable to personal productivity and identifying leverage points.

- Use **eisenhower-matrix** when: Categorizing a backlog of tasks (bugs, features, chores) by urgency and importance to decide what to 'Do First', 'Schedule', 'Delegate', or 'Eliminate'. Useful for sprint planning, issue triage, and managing incoming support requests.

Multiple frameworks can be combined:
- **pareto + one-thing**: Identifying the critical technical debt items and then pinpointing the single refactoring that provides the most leverage.
- **eisenhower-matrix + pareto**: Categorize tasks into quadrants, then apply 80/20 within the "Do First" and "Schedule" quadrants to identify the highest-impact items.

# Integration Notes

This framework is a core component of the `brainstormer` agent, enabling it to provide structured thinking for diverse problem types.

## Example Applications

**Technical debt prioritization**: Which refactoring will give the biggest bang for buck? (Use pareto to identify the 20% of code issues causing 80% of problems, one-thing to find the domino refactoring).

**Bug triage**: Drowning in bug reports? (Use eisenhower-matrix to categorize by urgency/importance, then pareto within Q1 to find highest-impact fixes).

**Feature planning**: Too many feature requests for MVP? (Use pareto to identify 20% of features that deliver 80% of value to users).

**Performance optimization**: Where to focus optimization efforts? (Use pareto to identify the 20% of code paths consuming 80% of resources).

**Test coverage**: Writing tests for large codebase? (Use pareto to identify 20% of functionality that covers 80% of user flows, one-thing to find which test gives the most confidence).

**Sprint planning**: Team overwhelmed with backlog? (Use eisenhower-matrix for task categorization, one-thing to identify the story that unblocks others).
