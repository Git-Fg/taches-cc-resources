# Advanced Prompting Techniques

Meta-prompting, constraint structuring, and skill creation patterns.

## Step-Back Prompting

### When to Use

Step-back prompting is effective for:
- Complex problems requiring principle-based reasoning
- Tasks where diving into specifics too early leads to suboptimal solutions
- Problems that benefit from establishing context before solving
- Creative tasks where understanding the "big picture" first helps

### How It Works

Instead of immediately solving the specific problem, first prompt the AI to consider broader principles, concepts, or categories related to the task. Then use those principles to inform the specific solution.

### Template

```
First, let's consider the broader context:

What are {number} key principles/concepts/categories for {domain}?

[AI provides principles]

Now, applying these principles, solve the specific problem:
{specific_problem}
```

### Example - Story Creation

**Direct approach (less effective):**
```
Write a storyline for a first-person shooter video game level that is challenging and engaging.
```

**Step-back approach:**
```
First, what are 5 key settings that contribute to a challenging and engaging FPS level storyline?

[AI responds with: Abandoned Military Base, Cyberpunk City, Alien Spaceship, Zombie-Infested Town, Underwater Research Facility]

Now, take one of these themes (Underwater Research Facility) and write a one paragraph storyline for a new FPS level that is challenging and engaging.
```

**Why it works:** The step-back prompt activates relevant background knowledge and patterns before tackling the specific problem, leading to more coherent and contextually appropriate outputs.

### Example - Technical Design

```
First: What are 5 key principles for designing a scalable REST API?

[AI provides principles about statelessness, resource identification, caching, etc.]

Now, applying these principles, design an API endpoint for bulk user creation that handles 10,000 requests per minute.
```

## Meta-Prompting for AI Agents

### What is Meta-Prompting?

Meta-prompting is creating prompts that generate other prompts. This is essential for AI agents that need to delegate tasks or create specialized prompts for different contexts.

### Meta-Prompt Template

```
Generate a prompt that will {task_description}.

The generated prompt should:
- {requirement_1}
- {requirement_2}
- {requirement_3}

Context: {context}

Generate the prompt:
```

### Example: Generating Analysis Prompts

```
Generate a prompt that will help an AI assistant analyze business documents.

The generated prompt should:
- Ask for key findings extraction
- Request specific output format (3-5 bullet points)
- Include verification step
- Work for various document types

Context: The assistant will be processing quarterly reports, market analysis, and competitor research.

Generate the prompt:
```

**Output:**
```
Analyze this business document and extract the key findings.

Provide your analysis in 3-5 bullet points.
Each bullet point should be concise (maximum 15 words).

After extracting findings, verify:
- All key points are covered
- Information is accurate based on the document
- No important insights were missed

Document: {document}

Key Findings:
```

### When to Use Meta-Prompting

- **Task delegation**: Agent creates prompts for other agents
- **Context adaptation**: Generate prompts for different scenarios
- **Prompt optimization**: Create variations to test
- **Skill building**: Build reusable prompt patterns

### Meta-Prompt for Skill Creation

```
Create a skill for {skill_name}.

Skill purpose: {what_skill_does}

The skill should include:
- Clear role definition
- Core capabilities (3-5 items)
- When to use the skill
- Example prompts

Output format: SKILL.md structure
```

## Structuring Constraints, Goals, and Objectives

### Clear Constraint Definition

Constraints define what the AI should NOT do or limits it should work within.

**Constraint Template:**
```
Task: {task_description}

Constraints:
- Must NOT: {prohibited_actions}
- Must: {required_actions}
- Limit: {specific_limits}
- Format: {output_format}

{task_input}
```

**Example:**
```
Summarize this technical article.

Constraints:
- Must NOT: Use jargon without explanation
- Must: Preserve all key technical details
- Limit: Maximum 200 words
- Format: 3-5 bullet points

Article: {article}
```

### Goal Formulation

Goals define what success looks like.

**Goal Template:**
```
Goal: {measurable_outcome}

To achieve this goal:
- Step 1: {first_action}
- Step 2: {second_action}
- Step 3: {third_action}

Input: {task_input}
```

**Example:**
```
Goal: Extract all dates from the text and convert to ISO format (YYYY-MM-DD).

To achieve this goal:
- Step 1: Identify all date expressions
- Step 2: Parse each date to determine its value
- Step 3: Format each date as ISO 8601

Text: {input_text}
```

### Objective Structuring

Objectives are specific, measurable targets within the broader goal.

**Objective Template:**
```
Primary Objective: {main_target}

Secondary Objectives:
- Objective 1: {secondary_target_1}
- Objective 2: {secondary_target_2}
- Objective 3: {secondary_target_3}

Task: {task_description}
```

### Combined Framework

**Complete Structure:**
```
You are a {role} assistant.

Your objective is to: {primary_objective}

Goals:
- {goal_1}
- {goal_2}

Constraints:
- Must: {required}
- Must not: {prohibited}

Output format: {format}

Task: {task}
```

### Example: Complete Framework in Action

```
You are a data analysis assistant specializing in business intelligence.

Your objective is to: Extract actionable insights from sales data.

Goals:
- Identify key performance trends
- Highlight anomalies or opportunities
- Provide data-driven recommendations

Constraints:
- Must: Base all insights on provided data only
- Must not: Make assumptions beyond the data
- Limit: Maximum 5 insights

Output format: Numbered list with brief explanations for each insight

Sales data: {data}

Insights:
```

## Automatic Prompt Engineering

### When to Use

Consider automatic (AI-assisted) prompt engineering when:
- You need to generate many prompt variations
- Exploring different ways to frame a problem
- Want to discover optimal prompt patterns
- Creating training data for prompt tuning
- Stuck on manual prompt refinement

### Meta-Prompting for Variation

Use AI to generate and improve prompts:

**Template:**
```
Generate {number} different prompts for {task}.

Each prompt should:
- {requirement_1}
- {requirement_2}
- {requirement_3}

Task description: {original_task_description}

Generate the prompts:
```

**Example:**
```
Generate 10 different prompt variations for customer sentiment classification.

Each prompt should:
- Be clear and specific
- Request POSITIVE, NEGATIVE, or NEUTRAL classification
- Handle edge cases (sarcastic reviews, mixed sentiment)
- Be under 50 words

Original task: Classify customer reviews as positive, negative, or neutral.

Generate the prompts:
```

### Prompt Evaluation and Selection

After generating variations, evaluate them:

```
For each generated prompt, evaluate based on:
- Clarity: Is the instruction unambiguous?
- Completeness: Does it cover edge cases?
- Conciseness: Is it efficient with words?
- Specificity: Does it set clear expectations?

Select the best 3 prompts and explain why they work best.
```

### Iterative Refinement with AI

Use AI to improve prompts iteratively:

```
Original prompt: "{original_prompt}"

This prompt sometimes produces {failure_description}.

Suggest 3 improvements to fix this issue, maintaining the prompt's core intent while addressing the failure mode.
```

### When Manual is Better

Automatic prompt engineering isn't always the answer:

**Use manual refinement when:**
- You deeply understand the specific domain
- The task is straightforward
- You need precise control over output format
- Working with sensitive content
- Time constraints (automatic takes longer)

**Use automatic when:**
- Exploring unfamiliar domains
- Need many variations quickly
- Want to discover unexpected approaches
- Building training datasets
- Stuck on manual attempts

## Zero-Shot vs One-Shot vs Few-Shot Decision Guide

### Decision Tree

```
Start: What type of task?

├─ Simple, common format (summarize, classify)
│  └─> Try ZERO-SHOT first
│     ├─ Works well? → Done
│     └─ Inconsistent? → Try ONE-SHOT
│
├─ Complex or unusual format
│  └─> Start with ONE-SHOT
│     ├─ Works well? → Done
│     └─ Needs more guidance? → Try FEW-SHOT (3-5 examples)
│
└─ Many edge cases or patterns
   └─> Use FEW-SHOT (5-8 examples)
      ├─ Still inconsistent? → Add more examples
      └─ Context limit reached? → Improve prompt clarity instead
```

### When to Use Each

**Zero-Shot**
- Simple, well-defined tasks
- Common formats (summarize, extract, classify)
- AI has seen similar tasks extensively during training
- Quick prototyping

**One-Shot**
- Task format is unclear
- Want to show desired structure
- Zero-shot produces variable results
- One representative example exists

**Few-Shot**
- Complex tasks with patterns to follow
- Multiple edge cases to demonstrate
- Output format is non-standard
- Want robust performance

### Progression Strategy

Start simple and add complexity only when needed:

```
Iteration 1: Zero-shot
"Summarize this article"

Iteration 2: Zero-shot with constraints
"Summarize this article in 3 bullet points"

Iteration 3: One-shot with example
"Summarize this article in 3 bullet points.

Example article: [example]
Example summary: [summary]

Current article: [article]
Summary:"

Iteration 4: Few-shot with multiple examples
[Add 2-3 more diverse examples]
```

## Quick Reference Card

### Step-Back Prompting

**When to use:** Complex tasks needing principle-based reasoning

**Template:** "What are {N} key principles for {domain}? Now apply these to {specific problem}."

**Common mistake:** Jumping straight to solution without establishing context

---

### Meta-Prompting

**When to use:** Task delegation, prompt optimization, skill building

**Template:** "Generate a prompt that will {task}. The generated prompt should: {requirements}"

**Common mistake:** Using auto-generated prompts without testing

---

### Constraint Structuring

**When to use:** Tasks requiring clear boundaries and success criteria

**Template:** "Constraints: Must NOT {prohibited}, Must {required}, Limit {bounds}"

**Common mistake:** Too many constraints make prompts rigid

---

### Choosing Example Count

| Task Complexity | Start With | Add If... |
|-----------------|------------|----------|
| Simple, common | Zero-shot | Inconsistent |
| Format unclear | One-shot | Still inconsistent |
| Multiple patterns | 3-5 examples | Missing edge cases |
| Very complex | 5-8 examples | Still failing |
