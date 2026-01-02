# Continue-Here Template

Copy and fill this structure for `.planning/phases/XX-name/.continue-here.md`:

```yaml
---
phase: XX-name
task: 3
total_tasks: 7
status: in_progress
last_updated: 2025-01-15T14:30:00Z
---
```

```markdown
## Current State

[Where exactly are we? What's the immediate context?]

## Completed Work

[What got done this session - be specific]

- Task 1: [name] - Done
- Task 2: [name] - Done
- Task 3: [name] - In progress, [what's done on it]

## Remaining Work

[What's left in this phase]

- Task 3: [name] - [what's left to do]
- Task 4: [name] - Not started
- Task 5: [name] - Not started

## Decisions Made

[Key decisions and why - so next session doesn't re-debate]

- Decided to use [X] because [reason]
- Chose [approach] over [alternative] because [reason]

## Blockers

[Anything stuck or waiting on external factors]

- [Blocker 1]: [status/workaround]

## Context

[Mental state, "vibe", anything that helps resume smoothly]

[What were you thinking about? What was the plan?
This is the "pick up exactly where you left off" context.]

## Next Action

[The very first thing to do when resuming]

Start with: [specific action]
```

## YAML Fields

Required YAML frontmatter:

- `phase`: Directory name (e.g., `02-authentication`)
- `task`: Current task number
- `total_tasks`: How many tasks in phase
- `status`: `in_progress`, `blocked`, `almost_done`
- `last_updated`: ISO timestamp

## Guidelines

- Be specific enough that a fresh Claude instance understands immediately
- Include WHY decisions were made, not just what
- The `## Next Action` should be actionable without reading anything else
- This file gets DELETED after resume - it's not permanent storage
