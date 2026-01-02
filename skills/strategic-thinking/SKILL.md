---
name: strategic-thinking
description: Strategic thinking frameworks for long-term perspective, big-picture analysis, and understanding temporal impact. PROACTIVELY USE for any decision requiring strategic thought, from technical architecture to business planning.
---

# Objective

Provide strategic thinking frameworks that help with long-term perspective, big-picture analysis, and understanding temporal impact for any problem or decision.

These frameworks help you think beyond immediate concerns and consider broader implications and time horizons.

# Frameworks Index

The strategic thinking skill includes these frameworks:

- first-principles: Break down to fundamentals and rebuild from base truths. Use when challenging assumptions or avoiding reasoning by analogy.

- inversion: Solve problems backwards - identify what would guarantee failure, then avoid those things. Use for risk assessment and robust planning.

- second-order: Think through consequences of consequences. Use when understanding ripple effects and unintended consequences.

- swot: Map strengths, weaknesses, opportunities, and threats. Use for strategic positioning and comprehensive situation analysis.

- 10-10-10: Evaluate decisions across three time horizons (10 minutes, 10 months, 10 years). Use when overcoming present bias and clarifying long-term impact.

# Routing Logic

When to use each framework:

- Use **first-principles** when: You need to challenge assumptions about a system's core components, designing from scratch (e.g., a new data structure), understanding fundamental concepts (e.g., event loops, type systems), or breaking down any complex idea to its irreducible minimum.

- Use **inversion** when: Identifying potential failure points in a design (e.g., 'what would make this API break?'), anticipating bugs in a new feature, building robust systems by avoiding known pitfalls, or preventing a project from going off track.

- Use **second-order** when: Making decisions with cascading effects, implementing policies with ripple impacts, evaluating the long-term consequences of a technical choice (e.g., adopting a new framework), or understanding how a bug fix might create new problems elsewhere.

- Use **swot** when: Analyzing the strategic positioning of a new product feature, assessing the competitive landscape, evaluating internal/external factors for a project's success, or understanding the overall context of a problem.

- Use **10-10-10** when: Facing short-term vs long-term conflicts (e.g., quick fix vs. proper refactor), overcoming present bias in architectural decisions, clarifying what actually matters over time in a career path, or evaluating the lasting impact of a design choice.

Multiple frameworks can be combined:
- **first-principles + inversion**: Rebuilding a core system component while systematically avoiding potential failure modes.
- **second-order + 10-10-10**: Understanding the cascading impacts of a platform change across different time horizons.
- **swot + first-principles**: Strategic analysis based on fundamental truths, challenging existing assumptions about the market or technology.

# Integration Notes

This framework is a core component of the `brainstormer` agent, enabling it to provide structured thinking for diverse problem types.

## Example Applications

**Business decision**: Should we expand to new market? (Use swot for positioning, second-order for consequences)

**Product strategy**: Build vs buy for a critical component? (Use first-principles to rebuild from fundamentals, inversion to identify failure modes)

**Technical architecture**: Microservices vs monolith for a new platform? (Use first-principles to challenge assumptions about scale and coupling, inversion for identifying critical points of failure in each approach).

**Personal growth**: How to learn a new programming language effectively? (Use first-principles for core concepts, inversion for common pitfalls to avoid).

**System design**: Designing a caching layer for high-traffic API? (Use first-principles to understand what caching actually needs to accomplish, inversion to identify what would make caching fail or worsen performance).
