## Overview
Prompt patterns for creating approaches, roadmaps, and strategies that will be consumed by subsequent prompts.

## Prompt Template
```markdown
## Objective

Create a {plan type} for {topic}.

**Purpose**: {What decision/implementation this enables}
**Input**: {Research or context being used}
**Output**: {topic}-plan.md with actionable phases/steps

## Context

Research findings: @.prompts/metaprompt/{num}-{topic}-research/{topic}-research.md
{Additional context files}

## Planning Requirements

{What the plan needs to address}
{Constraints to work within}
{Success criteria for the planned outcome}

## Output Structure

Save to: `.prompts/metaprompt/{num}-{topic}-plan/{topic}-plan.md`

Structure the plan using this Markdown format:

```markdown
# Summary

{One paragraph overview of the approach}

# Phases

## Phase 1: {phase-name}

**Objective**: {What this phase accomplishes}

**Tasks**:
- [ ] {Specific actionable task} (priority: high)
- [ ] {Another task} (priority: medium)

**Deliverables**:
- {What's produced}

**Dependencies**: {What must exist before this phase}

## Phase 2: {phase-name}
...

# Metadata

**Confidence**: high|medium|low
{Why this confidence level}

**Dependencies**:
- {External dependencies needed}

**Open Questions**:
- {Uncertainties that may affect execution}

**Assumptions**:
- {What was assumed in creating this plan}
```

## Summary Requirements

Create `.prompts/metaprompt/{num}-{topic}-plan/SUMMARY.md`

Load template: [summary-template.md](summary-template.md)

For plans, emphasize phase breakdown with objectives and assumptions needing validation. Next step typically: Execute first phase.

## Success Criteria

- Plan addresses all requirements
- Phases are sequential and logical
- Tasks are specific and actionable
- Metadata captures uncertainties
- SUMMARY.md created with phase overview
- Ready for implementation prompts to consume
```

## Key Principles

### Reference Research
Plans should build on research findings:
```markdown
## Context

Research findings: @.prompts/metaprompt/001-auth-research/auth-research.md

Key findings to incorporate:
- Recommended approach from research
- Constraints identified
- Best practices to follow
```

### Prompt-Sized Phases
Each phase should be executable by a single prompt:
```markdown
## Phase 1: setup-infrastructure

**Objective**: Create base auth structure and types

**Tasks**:
- [ ] Create auth module directory
- [ ] Define TypeScript types for tokens
- [ ] Set up test infrastructure
```

### Execution Hints
Help the next Claude understand how to proceed:
```markdown
## Phase 2: implement-jwt

**Execution Notes**:
This phase modifies files from phase 1.
Reference the types created in phase 1.
Run tests after each major change.
```

## Plan Types

### Implementation Roadmap
For breaking down how to build something:

```markdown
## Objective

Create implementation roadmap for user authentication system.

**Purpose**: Guide phased implementation with clear milestones
**Input**: Authentication research findings
**Output**: auth-plan.md with 4-5 implementation phases

## Context

Research: @.prompts/metaprompt/001-auth-research/auth-research.md

## Planning Requirements

- Break into independently testable phases
- Each phase builds on previous
- Include testing at each phase
- Consider rollback points
```

### Decision Framework
For choosing between options:

```markdown
## Objective

Create decision framework for selecting database technology.

**Purpose**: Make informed choice between PostgreSQL, MongoDB, and DynamoDB
**Input**: Database research findings
**Output**: database-plan.md with criteria, analysis, recommendation

## Output Structure

Structure as decision framework:

# Options

## PostgreSQL

**Pros**:
- {List}

**Cons**:
- {List}

**Fit Scores**:
- Scalability: 8/10
- Flexibility: 6/10

## MongoDB
...

# Recommendation

**Choice**: {Selected option}

**Rationale**: {Why this choice}

**Risks**: {What could go wrong}

**Mitigations**: {How to address risks}

# Metadata

**Confidence**: high
Clear winner based on requirements

**Assumptions**:
- Expected data volume: 10M records
- Team has SQL experience
```

### Process Definition
For defining workflows or methodologies:

```markdown
## Objective

Create deployment process for production releases.

**Purpose**: Standardize safe, repeatable deployments
**Input**: Current infrastructure research
**Output**: deployment-plan.md with step-by-step process

## Output Structure

Structure as process:

# Overview

{High-level flow}

# Steps

## Step 1: Pre-deployment

**Actions**:
- Run full test suite
- Create database backup
- Notify team in #deployments

**Checklist**:
- [ ] Tests passing
- [ ] Backup verified
- [ ] Team notified

**Rollback**: N/A - no changes yet

## Step 2: Deploy
...

# Metadata

**Dependencies**:
- CI/CD pipeline configured
- Database backup system
- Slack webhook for notifications

**Open Questions**:
- Blue-green vs rolling deployment?
- Automated rollback triggers?
```

## Metadata Guidelines
Load: [metadata-guidelines.md](metadata-guidelines.md)
