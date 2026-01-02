# Prompt Optimization Guide

## Systematic Refinement Process

### 1. Baseline Establishment

Before optimizing, establish how your current prompt performs:

**Test on diverse inputs:**
- Simple cases
- Edge cases
- Complex cases
- Ambiguous inputs

**Track metrics:**
- Accuracy / Correctness
- Output consistency
- Response quality
- Failure patterns

### 2. Iterative Refinement Workflow

```
Initial Prompt → Test → Analyze Failures → Refine → Test → Repeat
```

**Process:**
1. Test current prompt on representative inputs
2. Identify patterns in failures or weak outputs
3. Make targeted changes to address specific issues
4. Test again to verify improvement
5. Continue until satisfactory performance

**Example refinement cycle:**

*Iteration 1:*
```
"Summarize this article"
```
*Issue:* Summaries vary in length and structure

*Iteration 2:*
```
"Summarize this article in 3 bullet points"
```
*Issue:* Missing key insights

*Iteration 3:*
```
"Summarize this article in 3-5 bullet points, focusing on the main findings and their implications"
```
*Result:* More consistent and comprehensive

### 3. A/B Testing Framework

Test two variations against each other:

1. Create version A and version B of your prompt
2. Test both on the same set of inputs
3. Compare outputs for:
   - Accuracy
   - Consistency
   - Completeness
   - Style/format adherence
4. Select the better performer

**What to test:**
- Different instruction phrasings
- With/without examples
- Different example selections
- Different constraint formulations
- Different output format specifications

## Optimization for AI-to-AI Prompting

When one AI agent creates prompts for another, focus on clarity and context transfer:

### Be Explicit About Intended Audience

```
This prompt is for a {specialized/general-purpose} assistant with expertise in {domain}.
```

### Include Context About the Task Chain

```
Context: This is step {N} of {total} in a larger workflow.
Previous steps: {summary}
```

### Specify Output Format for Agent Consumption

```
Output format: {structured format that next agent can process}
```

### Meta-Prompt Optimization

When generating prompts that generate other prompts:

```
Generate a prompt that will {target_task}.

The generated prompt should:
- Be suitable for {target_agent_type}
- Include {specific_requirements}
- Work in {context_scenario}

Context: {context_information}

Generate the prompt:
```

### Inter-Agent Workflow Optimization

For multi-agent workflows, structure prompts to facilitate handoffs:

```
Stage {N} of {total}: {stage_name}

Your task: {specific_task}

Output will be used by: {next_agent_or_stage}

Provide output in this format:
{structured_output_format}
```

### Testing AI-to-AI Prompts

Evaluate prompts across agent boundaries:
- **Interpretability**: Does the receiving agent understand the intent?
- **Actionability**: Can the receiving agent execute the task?
- **Output compatibility**: Is the output usable by the next agent?
- **Context preservation**: Is important information maintained?

## Prompt Documentation

Track your prompts systematically to learn what works and reproduce success.

### Table-Based Documentation

Use a consistent table format to document prompt iterations:

| Field | Description | Example |
|-------|-------------|---------|
| Name | Prompt identifier and version | summarize_v1 |
| Goal | One-sentence purpose | Summarize articles in 3 bullets |
| Model | AI model used (if applicable) | claude-3-opus |
| Date | When created/modified | 2024-01-15 |
| Prompt | Full prompt text | See below |
| Output | Sample outputs | Good summary |
| Result | Success indicator | ✓ / ✗ / ~ |
| Notes | Observations and next steps | Needs length constraint |

### Example Documentation

| Name | Goal | Prompt | Output | Result | Notes |
|------|------|--------|--------|--------|-------|
| summarize_v1 | Summarize articles | "Summarize this article" | Good content | ~ | Too long sometimes |
| summarize_v2 | Summarize articles | "Summarize in 3 bullets" | Concise | ✓ | Ready for news |
| summarize_v3 | Summarize articles | "Summarize in 3-5 bullets, max 15 words each" | Very consistent | ✓ | Production ready |
| classify_v1 | Sentiment analysis | "Classify sentiment" | Mixed accuracy | ~ | Needs examples |
| classify_v2 | Sentiment analysis | [v1] + 3 examples per class | High accuracy | ✓ | Deploy to prod |

**Result key:**
- ✓ = Success, ready for production
- ✗ = Failure, needs major revision
- ~ = Mixed results, needs refinement

### Why Document Prompts

1. **Learn what works:** See patterns in successful prompts
2. **Reproduce success:** Use working prompts again
3. **Team collaboration:** Share with others
4. **A/B testing:** Compare variations systematically
5. **Debug when models update:** Identify what broke
6. **Build prompt library:** Reuse across projects

### Documentation Best Practices

1. **Document as you go:** Don't rely on memory
2. **Include sample outputs:** Shows what "good" looks like
3. **Note failures too:** Learn from what didn't work
4. **Version your prompts:** Track evolution over time
5. **Be specific:** "Works well" is less useful than "Works well for news articles, struggles with technical papers"
6. **Review periodically:** Clean up outdated entries

### Minimal Documentation Template

If you need something lightweight:

```
## summarize_v3 (2024-01-15) ✓

**Goal:** Summarize articles in 3-5 bullets, max 15 words each

**Prompt:**
```
Summarize this article in 3-5 bullet points.
Each bullet point should be maximum 15 words.
Focus on the main findings and key implications.

Article: {article}
```

**Works for:** News articles, blog posts, reports
**Struggles with:** Highly technical papers, fiction
**Status:** Production ready
```

## Optimization Strategies

### Clarity Improvement
Make instructions clearer and more specific:

**Before:**
```
"Analyze this text"
```

**After:**
```
"Analyze the following text for:
1. Main topic
2. Key arguments
3. Supporting evidence
4. Conclusion"
```

### Reducing Verbosity
Remove unnecessary words while maintaining effectiveness:

**Redundant phrases to remove:**
- "in order to" → "to"
- "due to the fact that" → "because"
- "at this point in time" → "now"
- "basically", "actually", "really"

**Consolidate instructions:**
```
Before:
"First, read the text. Then, identify the main points. Finally, summarize them."

After:
"Read the text, identify main points, and summarize them."
```

### Adding Structure
Use clear formatting to organize information:

```
## Context
{context}

## Task
{task}

## Requirements
- {requirement_1}
- {requirement_2}

## Input
{input}

## Output Format
{format}
```

### Improving Accuracy

**Add constraints for common failures:**
```
"Output must be valid JSON with no additional text outside the JSON structure."
```

**Add examples for edge cases:**
```
Example for empty input:
Input: ""
Output: "No content provided"

Example for ambiguous input:
Input: "bank"
Output: "Clarification needed: financial institution or river bank?"
```

**Add verification step:**
```
"After generating your response, verify it meets these criteria:
1. Directly answers the question
2. Uses only provided information
3. Acknowledges any uncertainty"
```

## Performance Evaluation

### Core Quality Dimensions

**Accuracy:** Does the output correctly address the task?

**Consistency:** Does similar input produce similar output?

**Clarity:** Is the output easy to understand?

**Completeness:** Does it address all aspects of the request?

**Efficiency:** Does it achieve the goal without unnecessary complexity?

### Failure Analysis

Categorize failures to identify patterns:

- **Format errors:** Output doesn't match expected structure
- **Factual errors:** Incorrect information
- **Logic errors:** Flawed reasoning
- **Incomplete responses:** Missing requested content
- **Missing context:** Not using provided information
- **Off-topic:** Addressing wrong subject

### Common Fixes for Failure Patterns

| Failure Type | Fix |
|--------------|-----|
| Format errors | Add explicit format examples and constraints |
| Missing context | Add "Use only the provided information" |
| Incomplete responses | Add "Address all parts of the question" |
| Inconsistent outputs | Add more diverse examples |
| Too verbose | Add length constraint or "Be concise" |

## Version Management

### Track Prompt Versions

Keep a record of prompt iterations:

```
Version 1: Initial prompt
"Summarize the text"

Version 2: Added length constraint
"Summarize the text in 3 bullet points"

Version 3: Added focus area
"Summarize the text in 3 bullet points, focusing on key findings"

Version 4: Added examples
[Version 3] + examples of good summaries

Version 5: Final (current)
[Version 4] + edge case handling
```

### Document What Works

Note successful patterns:

```
Pattern: Using numbered lists for multi-step tasks
Works well for: Analysis tasks, instructions, guides
Example: [reference]

Pattern: Providing 3 examples for format tasks
Works well for: Extraction, transformation, classification
Example: [reference]

Pattern: Adding verification step for accuracy-critical tasks
Works well for: Math, factual queries, data analysis
Example: [reference]
```

## Common Optimization Patterns

### Pattern 1: Add Structure
```
Before: "Analyze this text"
After: "Analyze this text for:
1. Main topic
2. Key arguments
3. Conclusion"
```

### Pattern 2: Add Examples
```
Before: "Extract entities"
After: "Extract entities

Example:
Text: Apple released iPhone 15 yesterday
Entities: Apple (company), iPhone 15 (product), yesterday (date)"
```

### Pattern 3: Add Constraints
```
Before: "Summarize this"
After: "Summarize in exactly 3 bullet points, maximum 15 words each"
```

### Pattern 4: Add Verification
```
Before: "Calculate the result"
After: "Calculate the result, then verify your calculation is correct before responding"
```

### Pattern 5: Add Context
```
Before: "Answer the question"
After: "You are a {role} with {expertise}. Answer the question as if explaining to {audience}."
```

## Testing Strategy

### Start Simple
1. Begin with the simplest prompt that might work
2. Test it
3. Only add complexity if needed

### Test Progressively
1. Test on simple, clear cases
2. Test on edge cases
3. Test on ambiguous inputs
4. Test on difficult cases

### Iterate Based on Findings
- If failing on simple cases → Fix fundamental issues
- If failing on edge cases → Add edge case examples
- If inconsistent → Add more examples or clarify instructions
- If too verbose → Add length constraints
- If inaccurate → Add verification steps

## Quick Reference

### When to Optimize
- Inconsistent outputs across similar inputs
- Poor quality on specific input types
- Failure to follow format requirements
- Missing important information
- Too much or too little output

### Documentation Template

```
| Name | Goal | Result | Notes |
|------|------|--------|-------|
| prompt_v1 | One sentence | ✓ | Production ready |
```

**Key fields:** Name, Goal, Prompt, Sample Output, Result (✓/✗/~), Notes

### Optimization Checklist
- [ ] Instructions are clear and specific
- [ ] Examples demonstrate the desired output
- [ ] Format requirements are explicit
- [ ] Edge cases are addressed
- [ ] Verification is included for critical tasks
- [ ] Constraints are appropriate (not too loose/tight)
- [ ] Testing covers diverse input types
- [ ] Prompt is documented
- [ ] Works across agent boundaries (for AI-to-AI)

### Common Improvements
| Issue | Solution |
|-------|----------|
| Inconsistent format | Add format examples and constraints |
| Missing information | Add explicit completeness requirement |
| Wrong information | Add verification step |
| Too long | Add length constraint |
| Too short | Specify expected detail level |
| Off-topic | Clarify scope and boundaries |
| Not reproducible | Document prompt version |
| Fails across agents | Add context about intended audience |

