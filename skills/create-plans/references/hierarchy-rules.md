## Overview
The planning hierarchy ensures context flows down and progress flows up.
Each level builds on the previous and enables the next.

## Hierarchy
```
BRIEF.md          ← Vision (human-focused)
    ↓
ROADMAP.md        ← Structure (phases)
    ↓
phases/XX/PLAN.md ← Implementation (Claude-executable)
    ↓
prompts/          ← Execution (via create-meta-prompts)
```

<level name="brief">
**Purpose**: Capture vision, goals, constraints
**Audience**: Human (the user)
**Contains**: What we're building, why, success criteria, out of scope
**Creates**: `.planning/BRIEF.md`

**Requires**: Nothing (can start here)
**Enables**: Roadmap creation

This is the ONLY document optimized for human reading.

<level name="roadmap">
**Purpose**: Define phases and sequence
**Audience**: Both human and Claude
**Contains**: Phase names, goals, dependencies, progress tracking
**Creates**: `.planning/ROADMAP.md`, `.planning/phases/` directories

**Requires**: Brief (or quick context if skipping)
**Enables**: Phase planning

Roadmap looks UP to Brief for scope, looks DOWN to track phase completion.

<level name="phase_plan">
**Purpose**: Define Claude-executable tasks
**Audience**: Claude (the implementer)
**Contains**: Tasks with Files/Action/Verification/Done-when
**Creates**: `.planning/phases/XX-name/PLAN.md`

**Requires**: Roadmap (to know phase scope)
**Enables**: Prompt generation, direct execution

Phase plan looks UP to Roadmap for scope, produces implementation details.

<level name="prompts">
**Purpose**: Optimized execution instructions
**Audience**: Claude (via create-meta-prompts)
**Contains**: Research/Plan/Do prompts with metadata
**Creates**: `.planning/phases/XX-name/prompts/`

**Requires**: Phase plan (tasks to execute)
**Enables**: Autonomous execution

Prompts are generated from phase plan via create-meta-prompts skill.

## Navigation Rules
### Looking Up
When creating a lower-level artifact, ALWAYS read higher levels for context:

- Creating Roadmap → Read Brief
- Planning Phase → Read Roadmap AND Brief
- Generating Prompts → Read Phase Plan AND Roadmap

This ensures alignment with overall vision.

### Looking Down
When updating a higher-level artifact, check lower levels for status:

- Updating Roadmap progress → Check which phase PLANs exist, completion state
- Reviewing Brief → See how far we've come via Roadmap

This enables progress tracking.

### Missing Prerequisites
If a prerequisite doesn't exist:

```
Creating phase plan but no roadmap exists.

Options:
1. Create roadmap first (recommended)
2. Create quick roadmap placeholder
3. Proceed anyway (not recommended - loses hierarchy benefits)
```

Always offer to create missing pieces rather than skipping.

## File Locations
All planning artifacts in `.planning/`:

```
.planning/
├── BRIEF.md                    # One per project
├── ROADMAP.md                  # One per project
└── phases/
    ├── 01-phase-name/
    │   ├── PLAN.md             # One per phase
    │   ├── .continue-here.md   # Temporary (when paused)
    │   └── prompts/            # Generated execution prompts
    ├── 02-phase-name/
    │   ├── PLAN.md
    │   └── prompts/
    └── ...
```

Phase directories use `XX-kebab-case` for consistent ordering.

## Scope Inheritance
Each level inherits and narrows scope:

**Brief**: "Build a task management app"
**Roadmap**: "Phase 1: Core task CRUD, Phase 2: Projects, Phase 3: Collaboration"
**Phase 1 Plan**: "Task 1: Database schema, Task 2: API endpoints, Task 3: UI"

Scope flows DOWN and gets more specific.
Progress flows UP and gets aggregated.

## Cross Phase Context
When planning Phase N, Claude should understand:

- What Phase N-1 delivered (completed work)
- What Phase N should build on (foundations)
- What Phase N+1 will need (don't paint into corner)

Read previous phase's PLAN.md to understand current state.
