---
name: prompt-engineering-patterns
description: Create effective prompts for AI-to-AI communication through Web UI. Covers meta-prompts, constraint structuring, example-based learning, chain-of-thought, and skill creation patterns.
---

# Path Resolution

This skill can be installed in multiple locations. Before reading any references, locate the skill directory:

```bash
# Search in priority order (project → plugin → user)
SKILL_PATH="$(
  find .claude/skills/prompt-engineering-patterns -maxdepth 0 2>/dev/null && echo "project" ||
  find ~/.claude/skills/prompt-engineering-patterns -maxdepth 0 2>/dev/null && echo "user" ||
  find {plugin_root}/skills/prompt-engineering-patterns -maxdepth 0 2>/dev/null && echo "plugin"
)"

# Use absolute path when reading internal reference files
```

All references to `references/` files must use the discovered absolute path.

# Objective

Create effective prompts for AI-to-AI communication through Web UI. Covers meta-prompts, constraint structuring, example-based learning, chain-of-thought, and skill creation patterns.

The key principle is to reduce XML usage in general prompts - use text-based heuristics and markdown structure, reserving XML only for highly structured workflows and configurations.

# Essential Principles

## Concise Is Key

Every token competes with conversation history. Challenge each piece:
- "Does Claude already know this?"
- "Is this explanation necessary?"
- "Does this justify its token cost?"

Default assumption: Claude is already smart. Only add what it doesn't have.

## Control Degrees of Freedom

Match specificity to task fragility:

| Freedom Level | When to Use | Pattern |
|--------------|-------------|---------|
| High | Multiple valid approaches, context-dependent | Text-based heuristics |
| Medium | Preferred pattern exists, some variation OK | Pseudocode with parameters |
| Low | Error-prone operations, consistency critical | Exact scripts with no parameters |

Example: Database migration = low freedom (one safe path). Code review = high freedom (context determines approach).

## XML Usage

Use XML sparingly and only for highly structured content:

XML is appropriate for:
- Workflow configurations with strict steps
- Agent command definitions with required fields
- Highly structured output specifications

XML is NOT appropriate for:
- General instructions and guidance
- Explanations and descriptions
- Most prompt content

Prefer text-based structure with clear headings and lists.

# Quick Start

For quick prompt patterns:

1. Simple task: Direct instruction
   "Summarize this article"

2. Add constraints: "Summarize in 3 bullet points"

3. Add reasoning: "Identify findings, then summarize in 3 bullets"

4. Add examples: Include 2-3 examples showing desired format

See references/ for detailed patterns and templates.

# Reference Index

All in `references/`:

Patterns: prompt-templates.md
Learning: few-shot-learning.md
Reasoning: chain-of-thought.md
Advanced: advanced-techniques.md
Interaction: agent-interaction.md
Optimization: prompt-optimization.md

# Core Capabilities

## Example-Based Learning

- Zero-shot: Direct requests without examples
- One-shot: Single demonstration
- Few-shot: 3-8 examples for complex patterns
- Best practices: Mix class order for classification, start with 6 examples
- Detailed guide: references/few-shot-learning.md

## Chain-of-Thought Reasoning

- Zero-shot CoT with triggers ("Let's think step by step")
- Step-back prompting (principles before specifics)
- Tree-of-Thought (multiple reasoning branches)
- Least-to-Most (break into subproblems)
- Verification and self-consistency
- Detailed guide: references/chain-of-thought.md

## Meta Prompting

- Creating prompts that generate prompts
- Structuring constraints, goals, objectives
- Skill creation patterns
- Pattern: "Generate a prompt that will {task}..."
- Detailed guide: references/advanced-techniques.md

## Agent Interaction

- Working with pre-configured agents (don't redefine roles)
- Task delegation: "As the {agent}, help me {task}"
- Multi-agent workflows (sequential, parallel, iterative)
- Context propagation across agent boundaries
- Detailed guide: references/agent-interaction.md

## Prompt Templates

- Reusable template patterns
- AI-to-AI specific templates
- Code prompting patterns
- JSON schema templates
- Complete library: references/prompt-templates.md

## Optimization

- Systematic refinement workflows
- A/B testing framework
- Documentation (table-based format)
- Failure analysis and fixes
- Detailed guide: references/prompt-optimization.md

# Best Practices

1. Be specific - Vague prompts produce inconsistent results
2. Show, don't tell - Examples beat lengthy descriptions
3. Test extensively - Evaluate on diverse inputs
4. Iterate rapidly - Small changes can have large impacts
5. Version control - Track what works
6. Document intent - Explain why prompts are structured this way

# Common Pitfalls

- Over-engineering: Starting complex before trying simple
- Example mismatch: Examples don't align with target task
- Information overload: Too many examples or instructions
- Ambiguous instructions: Room for multiple interpretations
- Ignoring edge cases: Not testing boundary conditions

# Success Criteria

Evaluate prompts on:
- Accuracy: Correctness and relevance
- Consistency: Reproducible across similar inputs
- Clarity: How well intent is conveyed
- Completeness: Addresses all task aspects
- Efficiency: Achieves goals without complexity
