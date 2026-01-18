## Overview
Guidelines for determining prompt complexity, tool usage, and optimization patterns.

## Complexity Assessment

### Simple Prompts
Single focused task, clear outcome:

**Indicators:**
- Single artifact output
- No dependencies on other files
- Straightforward requirements
- No decision-making needed

**Prompt characteristics:**
- Concise objective
- Minimal context
- Direct requirements
- Simple verification

### Complex Prompts
Multi-step tasks, multiple considerations:

**Indicators:**
- Multiple artifacts or phases
- Dependencies on research/plan files
- Trade-offs to consider
- Integration with existing code

**Prompt characteristics:**
- Detailed objective with context
- Referenced files
- Explicit implementation guidance
- Comprehensive verification
- Extended thinking triggers


## Extended Thinking Triggers

### When To Include
Use these phrases to activate deeper reasoning in complex prompts:
- Complex architectural decisions
- Multiple valid approaches to evaluate
- Security-sensitive implementations
- Performance optimization tasks
- Trade-off analysis

### Trigger Phrases
```
"Thoroughly analyze..."
"Consider multiple approaches..."
"Deeply consider the implications..."
"Explore various solutions before..."
"Carefully evaluate trade-offs..."
```

### Example Usage
```xml
#### Requirements
Thoroughly analyze the authentication options and consider multiple
approaches before selecting an implementation. Deeply consider the
security implications of each choice.
```

### When Not To Use
- Simple, straightforward tasks
- Tasks with clear single approach
- Following established patterns
- Basic CRUD operations


## Parallel Tool Calling

### When To Include
```xml
#### Efficiency
For maximum efficiency, invoke all independent tool operations
simultaneously rather than sequentially. Multiple file reads,
searches, and API calls that don't depend on each other should
run in parallel.
```

### Applicable Scenarios
- Reading multiple files for context
- Running multiple searches
- Fetching from multiple sources
- Creating multiple independent files


## Context Loading

### When To Load
- Modifying existing code
- Following established patterns
- Integrating with current systems
- Building on research/plan outputs

### When Not To Load
- Greenfield features
- Standalone utilities
- Pure research tasks
- Standard patterns without customization

### Loading Patterns
```xml
#### Context
<!-- Chained artifacts -->
Research: @.prompts/001-auth-research/auth-research.md
Plan: @.prompts/002-auth-plan/auth-plan.md

<!-- Existing code to modify -->
Current implementation: @src/auth/middleware.ts
Types to extend: @src/types/auth.ts

<!-- Patterns to follow -->
Similar feature: @src/features/payments/
```


## Output Optimization

### Streaming Writes
For research and plan outputs that may be large:

**Instruct incremental writing:**
```xml
#### Process
1. Create output file with XML skeleton
2. Write each section as completed:
   - Finding 1 discovered → Append immediately
   - Finding 2 discovered → Append immediately
   - Code example found → Append immediately
3. Finalize summary and metadata after all sections complete
```

**Why this matters:**
- Prevents lost work from token limit failures
- No need to estimate output size
- Agent creates natural checkpoints
- Works for any task complexity

**When to use:**
- Research prompts (findings accumulate)
- Plan prompts (phases accumulate)
- Any prompt that might produce >15k tokens

**When NOT to use:**
- Do prompts (code generation is different workflow)
- Simple tasks with known small outputs

### Claude To Claude
For Claude-to-Claude consumption:

**Use heavy XML structure:**
```xml
#### Findings
  <finding category="security">
    <title>Token Storage</title>
    <recommendation>httpOnly cookies</recommendation>
    <rationale>Prevents XSS access</rationale>
```

**Include metadata:**
```xml
#### Metadata
  <confidence level="high">Verified in official docs</confidence>
  <dependencies>Cookie parser middleware</dependencies>
  <open_questions>SameSite policy for subdomains</open_questions>
```

**Be explicit about next steps:**
```xml
#### Next Actions
  <action priority="high">Create planning prompt using these findings</action>
  <action priority="medium">Validate rate limits in sandbox</action>
```

### Human Consumption
For human consumption:
- Clear headings
- Bullet points for scanning
- Code examples with comments
- Summary at top


## Prompt Depth Guidelines

### Minimal
Simple Do prompts:
- 20-40 lines
- Basic objective, requirements, output, verification
- No extended thinking
- No parallel tool hints

### Standard
Typical task prompts:
- 40-80 lines
- Full objective with context
- Clear requirements and implementation notes
- Standard verification

### Comprehensive
Complex task prompts:
- 80-150 lines
- Extended thinking triggers
- Parallel tool calling hints
- Multiple verification steps
- Detailed success criteria


## Why Explanations

Always explain why constraints matter:

### Bad Example
```xml
#### Requirements
Never store tokens in localStorage.
```

### Good Example
```xml
#### Requirements
Never store tokens in localStorage - it's accessible to any
JavaScript on the page, making it vulnerable to XSS attacks.
Use httpOnly cookies instead.
```

This helps the executing Claude make good decisions when facing edge cases.


## Verification Patterns

### For Code
```xml
#### Verification
1. Run test suite: `npm test`
2. Type check: `npx tsc --noEmit`
3. Lint: `npm run lint`
4. Manual test: [specific flow to test]
```

### For Documents
```xml
#### Verification
1. Validate structure: [check required sections]
2. Verify links: [check internal references]
3. Review completeness: [check against requirements]
```

### For Research
```xml
#### Verification
1. Sources are current (2024-2025)
2. All scope questions answered
3. Metadata captures uncertainties
4. Actionable recommendations included
```

### For Plans
```xml
#### Verification
1. Phases are sequential and logical
2. Tasks are specific and actionable
3. Dependencies are clear
4. Metadata captures assumptions
```


## Chain Optimization

### Research Prompts
Research prompts should:
- Structure findings for easy extraction
- Include code examples for implementation
- Clearly mark confidence levels
- List explicit next actions

### Plan Prompts
Plan prompts should:
- Reference research explicitly
- Break phases into prompt-sized chunks
- Include execution hints per phase
- Capture dependencies between phases

### Do Prompts
Do prompts should:
- Reference both research and plan
- Follow plan phases explicitly
- Verify against research recommendations
- Update plan status when done

