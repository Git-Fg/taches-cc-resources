## Overview
Standard metadata structure for research and plan outputs. Include in all research, plan, and refine prompts.

## Metadata Structure
```xml
<metadata>
  <confidence level="{high|medium|low}">
    {Why this confidence level}
  </confidence>
  <dependencies>
    {What's needed to proceed}
  </dependencies>
  <open_questions>
    {What remains uncertain}
  </open_questions>
  <assumptions>
    {What was assumed}
  </assumptions>
</metadata>
```

## Confidence Levels
- **high**: Official docs, verified patterns, clear consensus, few unknowns
- **medium**: Mixed sources, some outdated info, minor gaps, reasonable approach
- **low**: Sparse documentation, conflicting info, significant unknowns, best guess

## Dependencies Format
External requirements that must be met:
```xml
<dependencies>
  - API keys for third-party service
  - Database migration completed
  - Team trained on new patterns
</dependencies>
```

## Open Questions Format
What couldn't be determined or needs validation:
```xml
<open_questions>
  - Actual rate limits under production load
  - Performance with >100k records
  - Specific error codes for edge cases
</open_questions>
```

## Assumptions Format
Context assumed that might need validation:
```xml
<assumptions>
  - Using REST API (not GraphQL)
  - Single region deployment
  - Node.js/TypeScript stack
</assumptions>
```
