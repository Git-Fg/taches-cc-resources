## Overview
Standard metadata structure for research and plan outputs. Include in all research, plan, and refine prompts.

## Metadata Structure
```xml
### Metadata
  <confidence level="{high|medium|low}">
    {Why this confidence level}
  #### Dependencies
    {What's needed to proceed}
  #### Open Questions
    {What remains uncertain}
  #### Assumptions
    {What was assumed}
```

## Confidence Levels
- **high**: Official docs, verified patterns, clear consensus, few unknowns
- **medium**: Mixed sources, some outdated info, minor gaps, reasonable approach
- **low**: Sparse documentation, conflicting info, significant unknowns, best guess

## Dependencies Format
External requirements that must be met:
```xml
### Dependencies
  - API keys for third-party service
  - Database migration completed
  - Team trained on new patterns
```

## Open Questions Format
What couldn't be determined or needs validation:
```xml
### Open Questions
  - Actual rate limits under production load
  - Performance with >100k records
  - Specific error codes for edge cases
```

## Assumptions Format
Context assumed that might need validation:
```xml
### Assumptions
  - Using REST API (not GraphQL)
  - Single region deployment
  - Node.js/TypeScript stack
```
