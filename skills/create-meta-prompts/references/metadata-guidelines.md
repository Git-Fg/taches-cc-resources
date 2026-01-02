## Overview
Standard metadata structure for research and plan outputs. Include in all research, plan, and refine prompts.

## Metadata Structure
```yaml
---
confidence: high|medium|low
confidence_explanation: |
  {Why this confidence level}
dependencies:
  - {What's needed to proceed}
  - {item 2}
open_questions:
  - {What remains uncertain}
  - {question 2}
assumptions:
  - {What was assumed}
  - {assumption 2}
---
```

## Confidence Levels
- **high**: Official docs, verified patterns, clear consensus, few unknowns
- **medium**: Mixed sources, some outdated info, minor gaps, reasonable approach
- **low**: Sparse documentation, conflicting info, significant unknowns, best guess

## Dependencies Format
External requirements that must be met:
```yaml
dependencies:
  - API keys for third-party service
  - Database migration completed
  - Team trained on new patterns
```

## Open Questions Format
What couldn't be determined or needs validation:
```yaml
open_questions:
  - Actual rate limits under production load
  - Performance with >100k records
  - Specific error codes for edge cases
```

## Assumptions Format
Context assumed that might need validation:
```yaml
assumptions:
  - Using REST API (not GraphQL)
  - Single region deployment
  - Node.js/TypeScript stack
```
