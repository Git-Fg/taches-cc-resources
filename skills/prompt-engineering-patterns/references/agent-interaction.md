# Agent Interaction Patterns

Craft effective prompts for pre-configured agents.

## Key Shift

**Don't redefine the agent's role:**
```
You are an expert data analyst...  // Don't do this
```

**Leverage what the agent already knows:**
```
As the data analyst agent, please analyze this dataset and provide insights...
[Leveraging what the agent already knows]
```

## Working with Pre-Configured Agents

### Understand Agent Capabilities

Before prompting, know what your agent can do:
- What tools does it have access to?
- What is its primary expertise area?
- What are its limitations?
- What output formats does it support best?

### Effective Task Framing

**DO:**
```
As the {agent_type}, help me {task} using {relevant_capabilities}.
```

**DON'T:**
```
You are an expert {agent_type}. Your job is to {task}...
```

### Providing Context Without Redefining Roles

**Instead of:**
```
You are a code reviewer. Look for bugs, security issues, and style problems. Check that the code follows PEP-8 standards...
```

**Use:**
```
Review this code focusing on security vulnerabilities and PEP-8 compliance:
```

The agent already knows it's a code reviewer - just tell it what to focus on.

## Task Delegation Patterns

### Single-Purpose Agents

For specialized agents, craft prompts that match their scope:

**Code Reviewer Agent:**
```
Check these recent changes for:
1. Security vulnerabilities
2. Performance issues
3. Code quality concerns

Files changed: {file_list}
```

**Debugger Agent:**
```
This error occurred:
{error_message}

Context:
{relevant_context}

Investigate and provide:
- Root cause
- Fix approach
- Prevention strategy
```

**Test Runner Agent:**
```
Run tests for {module_name} and fix any failures.

Focus on:
- Test failures
- Breaking changes
- Edge cases missed
```

**Docs Writer Agent:**
```
Document the {feature_name} functionality.

Include:
- Overview
- Usage examples
- API reference
- Common use cases
```

### General-Purpose Agents

When using versatile agents, provide more context:

```
I need to {complex_task}.

Context:
- My role: {user_role}
- Domain: {domain}
- Constraints: {constraints}
- Goal: {specific_goal}

Help me accomplish this by:
{steps_or_approach}
```

## Multi-Agent Workflows

### When to Use Multiple Agents

Different tasks benefit from different agent specializations:

1. **Exploration phase** → Use general-purpose agent
2. **Code review** → Use code-reviewer agent
3. **Testing** → Use test-runner agent
4. **Documentation** → Use docs-writer agent

### Sequential Delegation

```
First, use the analyzer agent to understand the current architecture.

Then, use the refactorer agent to propose improvements based on the analysis.

Finally, use the test-architect agent to ensure test coverage for changes.
```

**Example workflow:**
```
Phase 1: Architecture Analysis
[Use general-purpose agent]
Explore the codebase structure and identify the main components.

Phase 2: Security Review
[Use security-auditor agent]
Review the authentication system for vulnerabilities.

Phase 3: Code Review
[Use code-reviewer agent]
Check the recent changes for code quality issues.

Phase 4: Documentation
[Use docs-writer agent]
Document the updated authentication flow.
```

### Parallel Execution

```
Use these agents in parallel:
- Code-reviewer: Check for bugs
- Security-auditor: Check for vulnerabilities
- Performance-optimization: Check for bottlenecks

Then synthesize their findings.
```

## Context Management

### For Long-Running Tasks

Break into stages with checkpoints:

```
Stage 1/3: Analysis
Analyze {subject} and identify key aspects.

[Agent completes stage 1]

Stage 2/3: Deep Dive
Based on stage 1, examine {specific_area} in detail.

[Agent completes stage 2]

Stage 3/3: Synthesis
Combine findings from stages 1 and 2 into recommendations.
```

### Providing Incremental Context

Instead of one massive prompt:

```
Initial prompt: "Analyze the authentication system"

Response: [High-level overview]

Follow-up 1: "Now examine the OAuth implementation specifically"

Follow-up 2: "Check for common security vulnerabilities in the token handling"

Follow-up 3: "What improvements would you recommend?"
```

### Context Templates

**For code-related tasks:**
```
Context:
- Language: {programming_language}
- Framework: {framework}
- Purpose: {what_code_does}
- Recent changes: {changes}

Task:
{what_you_need}
```

**For business tasks:**
```
Context:
- Industry: {industry}
- Company size: {size}
- Target audience: {audience}
- Goal: {business_goal}

Task:
{what_you_need}
```

## Agent Selection Criteria

Choose agents based on:

1. **Task complexity** → Simple tasks may not need specialized agents
2. **Required tools** → Does the task need specific capabilities?
3. **Output format** → Does the agent naturally produce what you need?
4. **Context requirements** → Does the agent have the right domain knowledge?

### Selection Guide

| Task Type | Recommended Agent | Reasoning |
|-----------|------------------|-----------|
| Explore codebase | General-purpose | Needs broad search capability |
| Fix failing tests | Test-runner | Specialized in test patterns |
| Review security | Security-auditor | Domain expertise critical |
| Write docs | Docs-writer | Output format matters |
| Debug issue | Debugger | Systematic investigation needed |
| Refactor code | Refactorer | Requires architecture understanding |
| Review PR | Code-reviewer | Comprehensive code review |
| Plan feature | Architect | Design and structure focus |

### When NOT to Use Specialized Agents

- **Simple questions** → General-purpose is faster
- **Cross-domain tasks** → Specialist might miss broader context
- **Exploratory work** → General-purpose is more flexible
- **Quick iterations** → Switching agents adds overhead

## Prompt Patterns by Agent Type

### For Analysis Agents

```
Analyze {subject} for {specific_focus}.

Consider:
- Aspect 1: {detail}
- Aspect 2: {detail}
- Aspect 3: {detail}

Provide:
1. Key findings
2. Supporting evidence
3. Recommendations
```

### For Creative Agents

```
Generate {content_type} about {topic}.

Style: {style_guidance}
Audience: {target_audience}
Length: {length_constraint}
Tone: {emotional_tone}

{if_examples: Reference style:
{style_examples}}
```

### For Technical Agents

```
{technical_task}

Technical context:
- System: {system_type}
- Stack: {tech_stack}
- Constraints: {technical_constraints}

Output format:
{expected_format}
```

## Best Practices for User Prompts

1. **Assume competence** - The agent knows its job, don't redefine its role
2. **Be specific about your task** - What do YOU need done?
3. **Provide relevant context** - What does the agent need to know?
4. **Use constraints wisely** - Only when necessary for safety or format
5. **Match agent scope** - Don't ask a specialist agent for general tasks
6. **Think iteratively** - Break complex tasks into stages
7. **Leverage agent expertise** - Reference what the agent is good at

## Common Mistakes

- **Over-defining the agent** - "You are an expert..." when the agent already knows its role
- **Asking specialists to do general work** - Using a security-auditor for general questions
- **Ignoring agent capabilities** - Not using the tools and expertise the agent provides
- **Providing too much at once** - Overwhelming agents with massive prompts
- **Not matching output format** - Asking for JSON when the agent specializes in markdown
- **Switching agents unnecessarily** - Adding overhead without benefit

## Testing Agent Interactions

### Evaluating Agent Responses

For each agent interaction, check:
- **Relevance**: Did the agent address your specific request?
- **Quality**: Is the output helpful and accurate?
- **Format**: Does it match expected structure?
- **Completeness**: Were all requirements met?

### Iterating with Agents

```
Attempt 1: {initial_prompt}
Response: {agent_output}

Critique: {what_was_wrong_or_missing}

Attempt 2: {refined_prompt_based_on_critique}
Response: {improved_output}
```

## Quick Reference

### Effective Task Framing

| Pattern | When to Use |
|---------|-------------|
| "As the {agent}, help me {task}" | Clear delegation |
| "Review {code} focusing on {aspect}" | Targeted review |
| "Analyze {subject} for {purpose}" | Analysis tasks |
| "Generate {output} with {requirements}" | Creation tasks |

### Agent Selection Quick Guide

| Need | Use Agent |
|------|-----------|
| Explore | General-purpose |
| Fix tests | Test-runner |
| Security | Security-auditor |
| Debug | Debugger |
| Refactor | Refactorer |
| Review | Code-reviewer |
| Document | Docs-writer |
| Plan | Architect |

### Context Management Tips

1. **Break long tasks into stages** with checkpoints
2. **Provide incremental context** through follow-ups
3. **Match detail to task** - more context for complex tasks
4. **Use context templates** for consistency
5. **Reference previous outputs** to maintain continuity

### Multi-Agent Workflow Patterns

**Sequential:**
```
Agent A → Output → Agent B → Output → Agent C → Final Result
```

**Parallel:**
```
                → Synthesis
              ↗         ↖
Agent A → Output      Output ← Agent B
```

**Iterative:**
```
Agent A → Output → Review → Agent A (refined) → Final
```

## Technical Note: Reproducibility in Agent Systems

In agent systems where prompts are generated programmatically, some implementations use parameters to control output consistency. For Web UI interactions, focus on clear prompt structure and explicit task framing rather than technical parameter tuning. The key to reproducible agent interactions is:

1. **Clear task specification** - Well-defined prompts produce consistent results
2. **Explicit context** - Include all relevant information upfront
3. **Structured output formats** - Specify expected output structure
4. **Verification steps** - Include validation when consistency is critical

For AI-to-AI prompting through Web UI, these structural considerations are more important than any underlying technical configuration.
