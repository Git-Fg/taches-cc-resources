---
name: create-agent-skills
description: Expert guidance for creating, writing, building, and refining AI agent skills. MUST USE when working with SKILL.md files, authoring new skills, improving existing skills, or understanding skill structure and best practices.
---

# Essential Principles

## Overview

Skills are modular, filesystem-based capabilities that provide domain expertise on demand. This skill teaches how to create effective skills.

## Skills Are Prompts

All prompting best practices apply. Be clear, be direct, use XML structure. Assume Claude is smart - only add context Claude doesn't have.

## SKILL.md Always Loaded

When a skill is invoked, Claude reads SKILL.md. Use this guarantee:
- Essential principles go in SKILL.md (can't be skipped)
- Workflow-specific content goes in workflows/
- Reusable knowledge goes in references/

## Router Pattern

For complex skills, use this structure:

```
skill-name/
├── SKILL.md              # Router + principles
├── workflows/            # Step-by-step procedures (FOLLOW)
├── references/           # Domain knowledge (READ)
├── templates/            # Output structures (COPY + FILL)
└── scripts/              # Reusable code (EXECUTE)
```

SKILL.md asks "what do you want to do?" → routes to workflow → workflow specifies which references to read.

**Folder usage:**
- **workflows/** - Multi-step procedures Claude follows
- **references/** - Domain knowledge Claude reads for context
- **templates/** - Consistent output structures Claude copies and fills (plans, specs, configs)
- **scripts/** - Executable code Claude runs as-is (deploy, setup, API calls)

## Structure Clarity

Use markdown headings for structure (#, ##, ###). Reserve XML only for highly structured elements like routing decisions:

```markdown
# Objective

What this skill does

# Process

Step-by-step procedure

# Success Criteria

How to know it worked
```

Keep markdown formatting within content (bold, lists, code blocks).
XML reserved for complex routing logic in router pattern skills.

## Progressive Disclosure

SKILL.md under 500 lines. Split detailed content into reference files. Load only what's needed for the current workflow.

## Intake

What would you like to do?

1. Create new skill
2. Audit/modify existing skill
3. Add component (workflow/reference/template/script)
4. Get guidance

**Wait for response before proceeding.**

## Routing

| Response | Next Action | Workflow |
|----------|-------------|----------|
| 1, "create", "new", "build" | Ask: "Task-execution skill or domain expertise skill?" | Route to appropriate create workflow |
| 2, "audit", "modify", "existing" | Ask: "Path to skill?" | Route to appropriate workflow |
| 3, "add", "component" | Ask: "Add what? (workflow/reference/template/script)" | workflows/add-{type}.md |
| 4, "guidance", "help" | General guidance | workflows/get-guidance.md |

**Progressive disclosure for option 1 (create):**
- If user selects "Task-execution skill" → workflows/create-new-skill.md
- If user selects "Domain expertise skill" → workflows/create-domain-expertise-skill.md

**Progressive disclosure for option 3 (add component):**
- If user specifies workflow → workflows/add-workflow.md
- If user specifies reference → workflows/add-reference.md
- If user specifies template → workflows/add-template.md
- If user specifies script → workflows/add-script.md

**Intent-based routing (if user provides clear intent without selecting menu):**
- "audit this skill", "check skill", "review" → workflows/audit-skill.md
- "verify content", "check if current" → workflows/verify-skill.md
- "create domain expertise", "exhaustive knowledge base" → workflows/create-domain-expertise-skill.md
- "create skill for X", "build new skill" → workflows/create-new-skill.md
- "add workflow", "add reference", etc. → workflows/add-{type}.md
- "upgrade to router" → workflows/upgrade-to-router.md

**After reading the workflow, follow it exactly.**

## Quick Reference

Simple skill (single file):

```yaml
---
name: skill-name
description: What it does and when to use it.
---

# Objective

What this skill does

# Quick Start

Immediate actionable guidance

# Process

Step-by-step procedure

# Success Criteria

How to know it worked
```

**Example**: Simple skill like "process-pdfs" has single SKILL.md with objective, quick start (extract with pdfplumber), and success criteria.

Complex skill (router pattern):

```
SKILL.md:
  Essential Principles - Always applies
  Intake - Question to ask
  Routing - Maps answers to workflows

workflows/:
  Required Reading - Which refs to load
  Process - Steps
  Success Criteria - Done when...

references/:
  Domain knowledge, patterns, examples

templates/:
  Output structures Claude copies and fills
  (plans, specs, configs, documents)

scripts/:
  Executable code Claude runs as-is
  (deploy, setup, API calls, data processing)
```

**Example**: Router skill like "create-plans" uses intake/routing to delegate to create-brief, create-roadmap, or plan-phase workflows.

## Reference Index

All in `references/`:

Structure: skill-structure.md
Principles: core-principles.md, be-clear-and-direct.md
Patterns: common-patterns.md, workflows-and-validation.md
Assets: using-templates.md, using-scripts.md
Advanced: executable-code.md, api-security.md, iteration-and-testing.md

## Workflows Index

All in `workflows/`:

| Workflow | Purpose |
|----------|---------|
| create-new-skill.md | Build a skill from scratch |
| create-domain-expertise-skill.md | Build exhaustive domain knowledge base for build/ |
| audit-skill.md | Analyze skill against best practices |
| verify-skill.md | Check if content is still accurate |
| add-workflow.md | Add a workflow to existing skill |
| add-reference.md | Add a reference to existing skill |
| add-template.md | Add a template to existing skill |
| add-script.md | Add a script to existing skill |
| upgrade-to-router.md | Convert simple skill to router pattern |
| get-guidance.md | Help decide what kind of skill to build |

## YAML Requirements

Required fields:

```yaml
---
name: skill-name          # lowercase-with-hyphens, matches directory
description: ...          # What it does AND when to use it (third person)
---
```

Name conventions: `create-*`, `manage-*`, `setup-*`, `generate-*`, `build-*`

## Success Criteria

A well-structured skill:
- Has valid YAML frontmatter
- Uses markdown headings for structure
- Has essential principles inline in SKILL.md
- Routes directly to appropriate workflows based on user intent
- Keeps SKILL.md under 500 lines
- Asks minimal clarifying questions only when truly needed
- Has been tested with real usage
