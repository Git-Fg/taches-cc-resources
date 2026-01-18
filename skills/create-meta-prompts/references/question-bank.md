## Overview
Contextual questions for intake, organized by purpose. Use AskUserQuestion tool with these templates.

## Universal Questions

### Topic Identifier
When topic not obvious from description:
```yaml
header: "Topic"
question: "What topic/feature is this for? (used for file naming)"
# Let user provide via "Other" option
# Enforce kebab-case (convert spaces to hyphens)
```

### Chain Reference
When existing research/plan files found:
```yaml
header: "Reference"
question: "Should this prompt reference any existing research or plans?"
options:
  - "{file1}" - Found in .prompts/{folder1}/
  - "{file2}" - Found in .prompts/{folder2}/
  - "None" - Start fresh without referencing existing files
multiSelect: true
```


## Do Questions

### Artifact Type
When unclear what's being created:
```yaml
header: "Output type"
question: "What are you creating?"
options:
  - "Code/feature" - Software implementation
  - "Document/content" - Written material, documentation
  - "Design/spec" - Architecture, wireframes, specifications
  - "Configuration" - Config files, infrastructure setup
```

### Scope Completeness
When level of polish unclear:
```yaml
header: "Scope"
question: "What level of completeness?"
options:
  - "Production-ready" - Ship to users, needs polish and tests
  - "Working prototype" - Functional but rough edges acceptable
  - "Proof of concept" - Minimal viable demonstration
```

### Approach Patterns
When implementation approach unclear:
```yaml
header: "Approach"
question: "Any specific patterns or constraints?"
options:
  - "Follow existing patterns" - Match current codebase style
  - "Best practices" - Modern, recommended approaches
  - "Specific requirement" - I have a constraint to specify
```

### Testing Requirements
When verification needs unclear:
```yaml
header: "Testing"
question: "What testing is needed?"
options:
  - "Full test coverage" - Unit, integration, e2e tests
  - "Core functionality" - Key paths tested
  - "Manual verification" - No automated tests required
```

### Integration Points
For features that connect to existing code:
```yaml
header: "Integration"
question: "How does this integrate with existing code?"
options:
  - "New module" - Standalone, minimal integration
  - "Extends existing" - Adds to current implementation
  - "Replaces existing" - Replaces current implementation
```


## Plan Questions

### Plan Purpose
What the plan leads to:
```yaml
header: "Plan for"
question: "What is this plan leading to?"
options:
  - "Implementation" - Break down how to build something
  - "Decision" - Weigh options, choose an approach
  - "Process" - Define workflow or methodology
```

### Plan Format
How to structure the output:
```yaml
header: "Format"
question: "What format works best?"
options:
  - "Phased roadmap" - Sequential stages with milestones
  - "Checklist/tasks" - Actionable items to complete
  - "Decision framework" - Criteria, trade-offs, recommendation
```

### Constraints
What limits the plan:
```yaml
header: "Constraints"
question: "What constraints should the plan consider?"
options:
  - "Technical" - Stack limitations, dependencies, compatibility
  - "Resources" - Team capacity, expertise available
  - "Requirements" - Must-haves, compliance, standards
multiSelect: true
```

### Granularity
Level of detail needed:
```yaml
header: "Granularity"
question: "How detailed should the plan be?"
options:
  - "High-level phases" - Major milestones, flexible execution
  - "Detailed tasks" - Specific actionable items
  - "Prompt-ready" - Each phase is one prompt to execute
```

### Dependencies
What exists vs what needs creation:
```yaml
header: "Dependencies"
question: "What already exists?"
options:
  - "Greenfield" - Starting from scratch
  - "Existing codebase" - Building on current code
  - "Research complete" - Findings ready to plan from
```


## Research Questions

### Research Depth
How comprehensive:
```yaml
header: "Depth"
question: "How deep should the research go?"
options:
  - "Overview" - High-level understanding, key concepts
  - "Comprehensive" - Detailed exploration, multiple perspectives
  - "Exhaustive" - Everything available, edge cases included
```

### Source Priorities
Where to look:
```yaml
header: "Sources"
question: "What sources should be prioritized?"
options:
  - "Official docs" - Primary sources, authoritative references
  - "Community" - Blog posts, tutorials, real-world examples
  - "Current/latest" - 2024-2025 sources, cutting edge
multiSelect: true
```

### Output Format
How to present findings:
```yaml
header: "Output"
question: "How should findings be structured?"
options:
  - "Summary with key points" - Concise, actionable takeaways
  - "Detailed analysis" - In-depth with examples and comparisons
  - "Reference document" - Organized for future lookup
```

### Research Focus
When topic is broad:
```yaml
header: "Focus"
question: "What aspect is most important?"
options:
  - "How it works" - Concepts, architecture, internals
  - "How to use it" - Patterns, examples, best practices
  - "Trade-offs" - Pros/cons, alternatives, comparisons
```

### Evaluation Criteria
For comparison research:
```yaml
header: "Criteria"
question: "What criteria matter most for evaluation?"
options:
  - "Performance" - Speed, scalability, efficiency
  - "Developer experience" - Ease of use, documentation, community
  - "Security" - Vulnerabilities, compliance, best practices
  - "Cost" - Pricing, resource usage, maintenance
multiSelect: true
```


## Refine Questions

### Target Selection
When multiple outputs exist:
```yaml
header: "Target"
question: "Which output should be refined?"
options:
  - "{file1}" - In .prompts/{folder1}/
  - "{file2}" - In .prompts/{folder2}/
  # List existing research/plan outputs
```

### Feedback Type
What kind of improvement:
```yaml
header: "Improvement"
question: "What needs improvement?"
options:
  - "Deepen analysis" - Add more detail, examples, or rigor
  - "Expand scope" - Cover additional areas or topics
  - "Correct errors" - Fix factual mistakes or outdated info
  - "Restructure" - Reorganize for clarity or usability
```

### Specific Feedback
After type selected, gather details:
```yaml
header: "Details"
question: "What specifically should be improved?"
# Let user provide via "Other" option
# This is the core feedback that drives the refine prompt
```

### Preservation
What to keep:
```yaml
header: "Preserve"
question: "What's working well that should be kept?"
options:
  - "Structure" - Keep the overall organization
  - "Recommendations" - Keep the conclusions
  - "Code examples" - Keep the implementation patterns
  - "Everything except feedback areas" - Only change what's specified
```


## Question Rules
- Only ask about genuine gaps - don't ask what's already stated
- 2-4 questions max per round - avoid overwhelming
- Each option needs description - explain implications
- Prefer options over free-text - when choices are knowable
- User can always select "Other" - for custom input
- Route by purpose - use purpose-specific questions after primary gate
