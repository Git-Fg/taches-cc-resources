---
name: problem-analysis
description: Problem analysis frameworks for deep understanding, root causes, and optimal choices. PROACTIVELY USE when analyzing problems, making constrained choices, or simplifying complexity.
---

# Objective

Provide problem analysis frameworks that help with deep understanding, root cause analysis, trade-off evaluation, and simplicity optimization.

These frameworks help you think clearly about problems, make optimal choices under constraints, and improve by subtraction rather than addition.

# Frameworks Index

The problem-analysis skill includes these frameworks:

- 5-whys: Drill to root cause by asking why repeatedly. Use when troubleshooting or solving recurring problems.

- opportunity-cost: Analyze what you give up by choosing an option. Use when making trade-offs or evaluating true cost of choices.

- occams-razor: Find simplest explanation that fits all facts. Use when evaluating competing explanations or approaches.

- via-negativa: Improve by removing rather than adding. Use when simplifying complexity, reducing bloat, or improving systems.

# Routing Logic

When to use each framework:

- Use **5-whys** when: Deep root cause analysis of software bugs, performance regressions, deployment failures, or understanding *why* a particular design choice leads to issues. Also useful for investigating recurring problems and preventing their return.

- Use **opportunity-cost** when: When making choices with limited resources (time, budget, engineering effort), comparing alternative technical solutions, or evaluating the true cost of choosing one framework over another.

- Use **occams-razor** when: Evaluating competing solutions to a technical problem (e.g., two different algorithms for the same task), simplifying a complex codebase, or finding the most straightforward explanation for a bug. Useful for debugging and system simplification.

- Use **via-negativa** when: Simplifying a complex API, refactoring by removing unnecessary code/features, optimizing performance by eliminating bottlenecks, or improving a system by reducing points of failure.

Multiple frameworks can be combined:
- **5-whys + occams-razor**: Drilling down to the true root cause of a bug, then finding the simplest possible fix.
- **opportunity-cost + via-negativa**: Evaluating trade-offs between solutions, then considering what complexity can be removed.
- **occams-razor + via-negativa**: Finding the simplest approach by removing unnecessary complexity.

# Integration Notes

This framework is a core component of the `brainstormer` agent, enabling it to provide structured thinking for diverse problem types.

## Example Applications

**Root cause analysis**: Production outage keeps happening? (Use 5-whys to drill into root cause, occams-razor to find simplest fix).

**Technology selection**: Choosing between React vs Vue for new project? (Use opportunity-cost to evaluate what you give up with each choice).

**Debugging**: Strange intermittent bug? (Use 5-whys to trace root cause, occams-razor to find simplest explanation that fits all symptoms).

**API simplification**: API is too complex and hard to use? (Use via-negativa to identify what can be removed, occams-razor to find simplest design that works).

**Performance optimization**: System is slow, where to focus? (Use pareto to find bottlenecks, via-negativa to identify what can be removed, occams-razor for simplest optimization).

**Refactoring**: Codebase is bloated and hard to maintain? (Use via-negativa to identify what can be removed, opportunity-cost to weigh refactoring vs rewrite).

**Architecture decision**: Monolith vs microservices? (Use 5-whys to understand actual problem being solved, occams-razor to find simplest solution, opportunity-cost to evaluate trade-offs).
