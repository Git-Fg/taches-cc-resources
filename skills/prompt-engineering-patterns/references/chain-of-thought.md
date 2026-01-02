# Chain-of-Thought Prompting

Elicit step-by-step reasoning for complex tasks.

## Core Techniques

### Zero-Shot CoT

Add a simple trigger phrase:

**Template:**
```
{query}

Let's think step by step:
```

**Example:**
```
If a train travels 60 mph for 2.5 hours, how far does it go?

Let's think step by step:
1. Speed = 60 miles per hour
2. Time = 2.5 hours
3. Distance = Speed × Time
4. Distance = 60 × 2.5 = 150 miles

Answer: 150 miles
```

### Few-Shot CoT
Provide examples with explicit reasoning chains:

**Template:**
```
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 balls. How many tennis balls does he have now?
A: Let's think step by step:
1. Roger starts with 5 balls
2. He buys 2 cans, each with 3 balls
3. Balls from cans: 2 × 3 = 6 balls
4. Total: 5 + 6 = 11 balls
Answer: 11

Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, how many do they have?
A: Let's think step by step:
1. Started with 23 apples
2. Used 20 for lunch: 23 - 20 = 3 apples left
3. Bought 6 more: 3 + 6 = 9 apples
Answer: 9

Q: {user_query}
A: Let's think step by step:
```

### Self-Consistency
Generate multiple reasoning paths and take the most consistent answer:

**Approach:**
1. Generate the response multiple times with variations in reasoning
2. Compare the final answers from each attempt
3. Select the answer that appears most frequently

**When to use:**
- Complex math problems
- Multi-step logical reasoning
- When accuracy is critical

## Advanced Patterns

### Least-to-Most Prompting
Break complex problems into simpler subproblems:

**Stage 1 - Decomposition:**
```
Break down this complex problem into simpler subproblems:

Problem: {complex_query}

Subproblems:
```

**Stage 2 - Sequential Solving:**
For each subproblem:
```
Previous solutions: {solved_context}

Solve this subproblem:
{subproblem}

Solution:
```

**Stage 3 - Final Integration:**
```
Given these solutions to subproblems:
{all_solutions}

Provide the final answer to: {complex_query}

Final Answer:
```

**Example:**
```
Problem: A company has 500 employees. 60% are in sales, 25% in engineering, and the rest in operations. Sales team will grow by 20%, engineering by 10%, and operations will shrink by 5 employees. What's the final distribution?

Subproblems:
1. Calculate current department sizes
2. Calculate sales growth
3. Calculate engineering growth
4. Calculate operations change
5. Calculate final distribution

[Then solve each sequentially...]
```

### Tree-of-Thought
Explore multiple reasoning branches:

**Template:**
```
Problem: {problem}

Let's explore different approaches:

Approach 1: {first_approach}
{reasoning_path_1}
Result: {result_1}

Approach 2: {second_approach}
{reasoning_path_2}
Result: {result_2}

Approach 3: {third_approach}
{reasoning_path_3}
Result: {result_3}

Comparing the approaches, the best solution is:
```

**When to use:**
- Problems with multiple valid approaches
- Creative tasks requiring exploration
- Decision-making scenarios

### Verification Step
Add explicit verification to catch errors:

**Template:**
```
{problem}

Let's solve this step by step:
{reasoning_and_answer}

Now, verify this solution:
1. Check each step for logical errors
2. Verify all calculations
3. Ensure the final answer makes sense given the problem

Verification:
```

**Example:**
```
A store offers a 30% discount, then an additional 10% off the discounted price. What's the total discount from the original $100 price?

Step-by-step:
1. Original price: $100
2. After 30% discount: $100 - $30 = $70
3. Additional 10% off $70: $70 - $7 = $63
4. Total savings: $100 - $63 = $37
Answer: 37% total discount

Verification:
- 30% of $100 = $30 ✓
- 10% of $70 = $7 ✓
- Total discount: $30 + $7 = $37 ✓
- Final price: $100 - $37 = $63 ✓

The solution is correct.
```

## Domain-Specific CoT Templates

### Math Problems
```
Problem: {problem}

Solution:
Step 1: Identify what we know
- {known_values}

Step 2: Identify what we need to find
- {target_variable}

Step 3: Choose relevant approach
- {method_or_formula}

Step 4: Execute the calculation
- {calculation_steps}

Step 5: Verify the answer
- {verification}

Answer: {final_answer}
```

### Logical Reasoning
```
Premises:
{premises}

Question: {question}

Reasoning:
Step 1: List all given facts
{facts}

Step 2: Identify logical relationships
{relationships}

Step 3: Apply step-by-step deduction
{deductions}

Step 4: Draw conclusion
{conclusion}

Answer: {final_answer}
```

### Decision Making
```
Decision needed: {decision_context}

Let's think through this systematically:

Step 1: Define the objective
- {goal}

Step 2: Identify the options
- Option A: {option_a}
- Option B: {option_b}
- Option C: {option_c}

Step 3: Evaluate each option
- Option A: {pros_and_cons}
- Option B: {pros_and_cons}
- Option C: {pros_and_cons}

Step 4: Compare trade-offs
{comparison}

Step 5: Make recommendation
{recommendation}

Recommended action: {final_choice}
```

### Analysis Tasks
```
Task: {analysis_task}

Let's approach this systematically:

Step 1: Understand the scope
- What are we analyzing? {scope}
- What's the goal? {goal}

Step 2: Gather and organize information
- Key facts: {facts}
- Context: {context}

Step 3: Identify patterns and insights
- Pattern 1: {pattern_1}
- Pattern 2: {pattern_2}
- Pattern 3: {pattern_3}

Step 4: Draw conclusions
- Conclusion 1: {conclusion_1}
- Conclusion 2: {conclusion_2}

Step 5: Formulate recommendations
- Recommendation: {recommendation}

Summary: {summary}
```

## Best Practices

1. **Clear Step Markers**: Use numbered steps or clear delimiters
2. **Show All Work**: Don't skip steps, even obvious ones
3. **Verify Calculations**: Add explicit verification steps when accuracy matters
4. **State Assumptions**: Make implicit assumptions explicit
5. **Check Edge Cases**: Consider boundary conditions
6. **Use Examples First**: Show the reasoning pattern with examples before the actual task

## Common Pitfalls

- **Premature Conclusions**: Jumping to answer without full reasoning
- **Circular Logic**: Using the conclusion to justify the reasoning
- **Missing Steps**: Skipping intermediate calculations
- **Overcomplicated**: Adding unnecessary steps that confuse
- **Inconsistent Format**: Changing step structure mid-reasoning

## Technical Note: Reasoning Consistency

For agents implementing CoT in programmatic contexts, using consistent parameters helps ensure reproducible reasoning paths. In Web UI interactions, focus on clear reasoning structure rather than technical settings. The key is structuring prompts that elicit clear, step-by-step reasoning regardless of the underlying implementation.

## When to Use CoT

**Use CoT for:**
- Math and arithmetic problems
- Logical reasoning tasks
- Multi-step planning
- Complex decision making
- Analysis requiring synthesis
- Problem diagnosis

**Skip CoT for:**
- Simple factual queries
- Direct lookups
- Creative writing (unless structure helps)
- Tasks requiring extreme brevity
- When reasoning might slow down simple tasks

## Advanced Reasoning Patterns

### Comparative Reasoning
```
Let's compare {option_a} and {option_b}:

Aspect 1: {criterion_1}
- {option_a}: {analysis_a}
- {option_b}: {analysis_b}
- Comparison: {comparison_1}

Aspect 2: {criterion_2}
- {option_a}: {analysis_a}
- {option_b}: {analysis_b}
- Comparison: {comparison_2}

Conclusion: {overall_conclusion}
```

### Causal Chain Analysis
```
Event: {initial_event}

Let's trace the causal chain:

1. Initial cause: {cause}
2. Direct effect: {effect_1}
3. Secondary effect: {effect_2}
4. Tertiary effect: {effect_3}

Overall impact: {summary}
```

### Pros-Cons Evaluation
```
Topic: {topic}

Let's systematically evaluate:

Pros:
- Pro 1: {pro_1} - {impact}
- Pro 2: {pro_2} - {impact}
- Pro 3: {pro_3} - {impact}

Cons:
- Con 1: {con_1} - {impact}
- Con 2: {con_2} - {impact}
- Con 3: {con_3} - {impact}

Weighing the trade-offs:
{analysis}

Net assessment: {conclusion}
```

## Measuring CoT Effectiveness

Evaluate your chain-of-thought prompts by checking:

- **Correctness**: Does reasoning lead to correct answers?
- **Coherence**: Do steps follow logically from each other?
- **Completeness**: Are all necessary steps included?
- **Clarity**: Is the reasoning easy to follow?
- **Efficiency**: Are there unnecessary or redundant steps?

## Quick Templates

### Simple CoT
```
{question}

Let's think step by step:
```

### CoT with Examples
```
{example_with_reasoning}

{question}

Let's think step by step:
```

### CoT with Verification
```
{question}

Let's solve this step by step:
{reasoning}

Now verify: Is this answer correct?
```

### CoT for Multiple Choice
```
{question}
Options: A) {option_a} B) {option_b} C) {option_c} D) {option_d}

Let's analyze each option:
A) {analysis_a}
B) {analysis_b}
C) {analysis_c}
D) {analysis_d}

The correct answer is:
```

## Quick Reference Card

### When to Use Chain-of-Thought

- **Math problems** - Arithmetic, algebra, word problems
- **Logic reasoning** - Deduction, inference, puzzles
- **Multi-step planning** - Sequential decision making
- **Complex analysis** - Requiring synthesis of information
- **Problem diagnosis** - Systematic troubleshooting

### Key Templates

**Simple CoT:**
```
{question}

Let's think step by step:
```

**CoT with Verification:**
```
{question}

Let's solve this step by step:
{reasoning}

Now verify: Is this answer correct?
```

**Tree-of-Thought for Exploration:**
```
Problem: {problem}

Let's explore different approaches:

Approach 1: {first_approach}
{reasoning_path_1}
Result: {result_1}

Approach 2: {second_approach}
{reasoning_path_2}
Result: {result_2}

Comparing the approaches, the best solution is:
```

### Best Practices

1. **Put answer AFTER reasoning** - not embedded within it
2. **Use clear answer markers** like "Answer:" or "Result:"
3. **Show all work** - don't skip intermediate steps
4. **Add verification steps** when accuracy is critical
5. **Keep format consistent** throughout reasoning chain
6. **Structure reasoning clearly** for other agents to interpret

### Common Mistakes to Avoid

1. **Premature conclusions** - Jumping to answer without full reasoning
2. **Circular logic** - Using conclusion to justify reasoning
3. **Embedded answers** - Makes reasoning hard to follow
4. **Missing steps** - Skipping intermediate calculations
5. **Inconsistent structure** - Changing format mid-reasoning

