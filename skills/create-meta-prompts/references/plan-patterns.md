## Overview
Prompt patterns for creating approaches, roadmaps, and strategies that will be consumed by subsequent prompts.

## Prompt Template
```xml
### Objective
Create a {plan type} for {topic}.

Purpose: {What decision/implementation this enables}
Input: {Research or context being used}
Output: {topic}-plan.md with actionable phases/steps

### Context
Research findings: @.prompts/{num}-{topic}-research/{topic}-research.md
{Additional context files}

### Planning Requirements
{What the plan needs to address}
{Constraints to work within}
{Success criteria for the planned outcome}

### Output Structure
Save to: `.prompts/{num}-{topic}-plan/{topic}-plan.md`

Structure the plan using this XML format:

```xml
#### Plan
  ##### Summary
    {One paragraph overview of the approach}

  ##### Phases
    <phase number="1" name="{phase-name}">
      <objective>{What this phase accomplishes}</objective>
      ###### Tasks
        <task priority="high">{Specific actionable task}</task>
        <task priority="medium">{Another task}</task>
      ###### Deliverables
        <deliverable>{What's produced}</deliverable>
      <dependencies>{What must exist before this phase}</dependencies>
    <!-- Additional phases -->

  ##### Metadata
    <confidence level="{high|medium|low}">
      {Why this confidence level}
    ###### Dependencies
      {External dependencies needed}
    ###### Open Questions
      {Uncertainties that may affect execution}
    ###### Assumptions
      {What was assumed in creating this plan}
```

### Summary Requirements
Create `.prompts/{num}-{topic}-plan/SUMMARY.md`

Load template: [summary-template.md](summary-template.md)

For plans, emphasize phase breakdown with objectives and assumptions needing validation. Next step typically: Execute first phase.

### Success Criteria
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
```xml
#### Context
Research findings: @.prompts/001-auth-research/auth-research.md

Key findings to incorporate:
- Recommended approach from research
- Constraints identified
- Best practices to follow
```

### Prompt Sized Phases
Each phase should be executable by a single prompt:
```xml
<phase number="1" name="setup-infrastructure">
  <objective>Create base auth structure and types</objective>
  #### Tasks
    <task>Create auth module directory</task>
    <task>Define TypeScript types for tokens</task>
    <task>Set up test infrastructure</task>
```

### Execution Hints
Help the next Claude understand how to proceed:
```xml
<phase number="2" name="implement-jwt">
  #### Execution Notes
    This phase modifies files from phase 1.
    Reference the types created in phase 1.
    Run tests after each major change.
```


## Plan Types

### Implementation Roadmap
For breaking down how to build something:

```xml
#### Objective
Create implementation roadmap for user authentication system.

Purpose: Guide phased implementation with clear milestones
Input: Authentication research findings
Output: auth-plan.md with 4-5 implementation phases

#### Context
Research: @.prompts/001-auth-research/auth-research.md

#### Planning Requirements
- Break into independently testable phases
- Each phase builds on previous
- Include testing at each phase
- Consider rollback points
```

### Decision Framework
For choosing between options:

```xml
#### Objective
Create decision framework for selecting database technology.

Purpose: Make informed choice between PostgreSQL, MongoDB, and DynamoDB
Input: Database research findings
Output: database-plan.md with criteria, analysis, recommendation

#### Output Structure
Structure as decision framework:

```xml
##### Decision Framework
  ###### Options
    <option name="PostgreSQL">
      <pros>{List}</pros>
      <cons>{List}</cons>
      <fit_score criteria="scalability">8/10</fit_score>
      <fit_score criteria="flexibility">6/10</fit_score>
    <!-- Other options -->

  ###### Recommendation
    <choice>{Selected option}</choice>
    <rationale>{Why this choice}</rationale>
    <risks>{What could go wrong}</risks>
    <mitigations>{How to address risks}</mitigations>

  ###### Metadata
    <confidence level="high">
      Clear winner based on requirements
    ####### Assumptions
      - Expected data volume: 10M records
      - Team has SQL experience
```
```

### Process Definition
For defining workflows or methodologies:

```xml
#### Objective
Create deployment process for production releases.

Purpose: Standardize safe, repeatable deployments
Input: Current infrastructure research
Output: deployment-plan.md with step-by-step process

#### Output Structure
Structure as process:

```xml
##### Process
  <overview>{High-level flow}</overview>

  ###### Steps
    <step number="1" name="pre-deployment">
      ####### Actions
        <action>Run full test suite</action>
        <action>Create database backup</action>
        <action>Notify team in #deployments</action>
      ####### Checklist
        <item>Tests passing</item>
        <item>Backup verified</item>
        <item>Team notified</item>
      <rollback>N/A - no changes yet</rollback>
    <!-- Additional steps -->

  ###### Metadata
    ####### Dependencies
      - CI/CD pipeline configured
      - Database backup system
      - Slack webhook for notifications
    ####### Open Questions
      - Blue-green vs rolling deployment?
      - Automated rollback triggers?
```
```


## Metadata Guidelines
Load: [metadata-guidelines.md](metadata-guidelines.md)
