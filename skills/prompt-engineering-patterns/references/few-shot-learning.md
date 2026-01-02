# Example-Based Learning Guide

Zero-shot, one-shot, and few-shot learning strategies.

## Zero-Shot Prompting

Direct requests without examples.

### When to Use

- Simple, well-defined tasks (classification, extraction, transformation)
- Common formats (summarization, sentiment analysis, Q&A)
- Limited context space
- Familiar tasks (seen extensively during training)
- Quick prototyping

### Best Practices

- Be extremely specific about the task
- Use clear action verbs (Classify, Extract, Summarize, Transform)
- Specify output format explicitly
- Add constraints only when needed
- Use structured prompts with clear sections

### Example

```
Classify the following customer review as POSITIVE, NEGATIVE, or NEUTRAL.

Review: "The product broke after one day. Terrible quality! I want my money back."

Classification:
```

**Output:** NEGATIVE

Sentiment classification is a common task that AI models have seen millions of times during training.

### Zero-Shot with Constraints

```
Summarize the following article in exactly 3 bullet points.
Each bullet point should be maximum 15 words.

Article: [article text]

Summary:
```

## One-Shot Prompting

Single demonstration to show desired pattern.

### When to Use

- Task format is unclear without example
- Zero-shot produces inconsistent outputs
- One perfect example captures the pattern
- Non-standard format needs demonstration
- Limited context budget

### Best Practices

- Choose a representative example
- Make example comprehensive (show all aspects)
- Include edge cases if possible
- Use clear formatting
- Test the example yourself

### Example

```
Extract the price from product descriptions.

Example:
Description: "Premium wireless headphones, normally $299, now on sale for $199.99 with free shipping."
Price: $199.99

Description: "Luxury watch with Swiss movement, priced at £2,500, comes with 2-year warranty."
Price:
```

**Output:** £2,500

The example shows current/sale price extraction and handles different currencies.

### Decision Flow

```
Zero-shot → Works? → Done
            ↓ No
One-shot → Works? → Done
            ↓ No
Few-shot (3-8 examples)
```

## Example Selection Strategies

### 1. Semantic Similarity
Select examples most similar to the input query.

**Approach:** Choose examples that share similar keywords, concepts, or structure with the input.

**Best For:** Question answering, text classification, extraction tasks

**Example:**
```
Task: Classify customer feedback sentiment

Example 1:
Input: "The product broke after one day, terrible quality!"
Output: Negative

Example 2:
Input: "Great service, fast shipping, very happy!"
Output: Positive

Input: "I'm disappointed with the delayed delivery"
Output:
```

### 2. Diversity Sampling
Maximize coverage of different patterns and edge cases.

**Approach:** Select examples that represent different variations, styles, or categories of the task.

**Best For:** Demonstrating task variability, edge case handling

**Example:**
```
Task: Extract dates from text

Example 1 (Standard format):
Input: "The meeting is on January 15, 2024"
Output: 2024-01-15

Example 2 (Relative date):
Input: "The deadline is next Friday"
Output: {relative_date}

Example 3 (Informal format):
Input: "It happened last month on the 3rd"
Output: {relative_date}

Input: "The event is scheduled for March 23rd"
Output:
```

### 3. Difficulty-Based Selection
Gradually increase example complexity to scaffold learning.

**Approach:** Start with simple examples, progress to more complex ones.

**Best For:** Complex reasoning tasks, multi-step problems

**Example:**
```
Task: Solve word problems

Example 1 (Simple):
Input: "John has 3 apples. He buys 2 more. How many apples does John have?"
Output: 5

Example 2 (Moderate):
Input: "A store sells apples for $2 each. If you buy 5 apples, you get a 10% discount. How much do 5 apples cost?"
Output: $9.00

Example 3 (Complex):
Input: "A farmer has 100 apples. He sells 40% of them at $2 each and donates the remaining 30 apples to a school. The rest are used to make apple pie. Each pie requires 5 apples. How many pies can he make?"
Output: 6 pies

Input: "Sarah has twice as many books as Tom. Tom has 5 fewer books than Lisa, who has 20 books. How many books does Sarah have?"
Output:
```

### 4. Error-Based Selection
Include examples that address common failure modes.

**Approach:** Select examples demonstrating correct handling of common mistakes.

**Best For:** Tasks with known failure patterns, quality-critical applications

**Example:**
```
Task: Extract company names from text

Example 1 (Clear case):
Input: "Apple announced new products today"
Output: Apple

Example 2 (Ambiguous word):
Input: "I ate an apple for lunch"
Output: None

Example 3 (Multiple companies):
Input: "Microsoft and Google partnered on AI research"
Output: Microsoft, Google

Input: "Amazon's stock price increased"
Output:
```

### 5. Example Selection for AI-to-AI Prompting

When one AI agent provides examples to another agent, additional considerations apply:

**Use Agent-Understandable Patterns:**
- Examples should be in formats the receiving agent processes well
- Include metadata about example types for clarity
- Use formats that leverage shared training data

**Example with Metadata:**
```
Example 1 (Type: code_review, Complexity: low):
Input: "Add error handling to login function"
Output: "```javascript
function login(username, password) {
  try {
    // existing code
  } catch (error) {
    console.error('Login failed:', error);
    throw error;
  }
}
```"

Example 2 (Type: code_review, Complexity: high):
Input: "Refactor authentication for OAuth 2.0"
Output: "```javascript
// OAuth 2.0 authentication with token refresh
class AuthManager {
  // implementation
}
```"
```

**Contextualize Examples for Agents:**
```
Example type: {classification/extraction/transformation}
Domain: {domain}
Complexity: {simple/moderate/complex}
Expected output format: {format}

Input: {example_input}
Output: {example_output}
```

**Reference Shared Knowledge:**
- Use examples that leverage common understanding
- Reference well-known patterns in the domain
- Assume familiarity with standard formats

**Example for Shared Knowledge:**
```
Example: Extract SQL table relationships

Input: "Users table has id as primary key. Orders table references user_id"
Output: "Users (1) ──< (N) Orders"

Note: Uses standard ER diagram notation
```

**Best Practices for AI-to-AI Examples:**
1. **Explicit format requirements** - Specify output structure clearly
2. **Domain context** - Include the domain expertise level expected
3. **Processing instructions** - How the example should be interpreted
4. **Failure cases** - Show what to do when examples don't apply
5. **Modular examples** - Each example should be independently useful

**Example of AI-to-AI Example Block:**
```
These examples demonstrate code review patterns for a security-focused agent.

Example 1 (Pattern: input_validation):
Input: "function getUser(id) { return db.query('SELECT * FROM users WHERE id = ' + id) }"
Output: "VULNERABLE: SQL injection via string concatenation
Fix: Use parameterized queries:
function getUser(id) {
  return db.query('SELECT * FROM users WHERE id = ?', [id])
}"

Example 2 (Pattern: authentication):
Input: "if (password === storedPassword) login()"
Output: "VULNERABLE: Plaintext password comparison
Fix: Use proper hashing:
if (bcrypt.compare(password, storedHash)) login()"

Target agent should:
- Focus on security vulnerabilities
- Provide actionable remediation
- Reference OWASP guidelines where applicable
```

## Example Construction Best Practices

### Format Consistency
All examples should follow identical formatting:

**Good - Consistent format:**
```
Example 1:
Input: "What is the capital of France?"
Output: "Paris"

Example 2:
Input: "What is the capital of Germany?"
Output: "Berlin"
```

**Bad - Inconsistent format:**
```
Q: What is the capital of France? A: Paris
{"question": "What is the capital of Germany?", "answer": "Berlin"}
```

### Input-Output Alignment
Ensure examples demonstrate the exact task:

**Good - Clear relationship:**
```
Input: "Sentiment: The movie was terrible and boring."
Output: Negative
```

**Bad - Ambiguous relationship:**
```
Input: "The movie was terrible and boring."
Output: This review expresses negative sentiment toward the film, indicating strong dissatisfaction with both the storytelling and pacing.
```

### Complexity Balance
Include examples spanning the expected difficulty range:

```
Simple Example:
Input: "2 + 2"
Output: "4"

Moderate Example:
Input: "15 * 3 + 8"
Output: "53"

Complex Example:
Input: "(12 + 8) * 3 - 15 / 5"
Output: "57"
```

## Managing Example Quantity

### Token Budget Considerations
Balance example quantity with other prompt elements:

Typical distribution:
- System/Role Context: ~10-15%
- Examples: ~30-40%
- User Input: ~10-15%
- Expected Response: ~30-40%

### Optimal Example Count
- **1-2 examples**: Simple format transformations
- **3-5 examples**: Most tasks requiring pattern recognition
- **5-8 examples**: Complex tasks with many variations
- **More than 8**: Rarely needed; consider if examples add value

## Edge Case Handling

Include examples that demonstrate how to handle boundary conditions:

```
Example 1 (Empty input):
Input: ""
Output: "Please provide input text."

Example 2 (Ambiguous input):
Input: "bank"
Output: "Ambiguous: Could refer to financial institution or river bank. Please clarify."

Example 3 (Invalid input):
Input: "!@#$%"
Output: "Unable to process: Input contains invalid characters."

Example 4 (Multiple valid answers):
Input: "Name a primary color"
Output: "Valid answers include: red, blue, yellow"
```

## Prompt Templates for Example-Based Learning

### Classification Template
```
Classify the text into one of these categories: {categories}

{examples}

Text: {query}

Category:
```

### Extraction Template
```
Extract structured information from the text.

{examples}

Text: {query}

Extracted information:
```

### Transformation Template
```
Transform the input according to the pattern shown in examples.

{examples}

Input: {query}

Output:
```

## Evaluation and Improvement

### Example Quality Checklist
When evaluating your examples:

- **Clarity**: Is the input-output relationship clear?
- **Representativeness**: Does it match the target task?
- **Diversity**: Do examples cover different scenarios?
- **Consistency**: Are all examples formatted the same way?
- **Accuracy**: Are all outputs correct?

### A/B Testing Example Sets
Test different example sets to find optimal performance:

1. Create two versions of your prompt with different examples
2. Test on the same set of inputs
3. Compare quality and consistency of outputs
4. Select the example set that performs better

### Iterative Refinement
Improve examples based on failure analysis:

1. Identify where the AI produces incorrect outputs
2. Add examples addressing those specific cases
3. Remove examples that don't contribute value
4. Simplify examples if the prompt becomes too long
5. Test again and iterate

## Advanced Techniques

### Progressive Example Selection
Start with fewer examples, add more as needed:

```
Iteration 1: Use 2-3 core examples
Iteration 2: Add examples for edge cases discovered
Iteration 3: Add examples for remaining failure modes
```

### Example Chaining
Build complexity by chaining simple examples:

```
Step 1: Basic extraction
Input: "The price is $50"
Output: $50

Step 2: Extraction with currency conversion
Input: "The price is 50 euros"
Output: $54 (at 1.08 exchange rate)

Step 3: Extraction with comparison
Input: "The price dropped from $60 to $50"
Output: $50 (original: $60, change: -$10)
```

### Counter-Example Demonstration
Show what NOT to do:

```
Good Example:
Input: "Summarize: The article discusses the impact of climate change..."
Output: "Climate change affects ecosystems through rising temperatures and extreme weather."

Bad Example (avoid this):
Input: "Summarize: The article discusses the impact of climate change..."
Output: "The article is about climate change and talks about many things like temperature and weather and ecosystems and..."

Your task: Follow the Good Example pattern.
```

### Using Code as Examples

Code snippets can serve as powerful examples in prompts.

### When Code Examples Help

- **Demonstrating input/output formats** - Show expected structure clearly
- **Showing data transformation patterns** - Illustrate how to process data
- **API usage examples** - Demonstrate function calls and parameters
- **Template demonstration** - Show pattern to follow

### Code Example Template

```
{task_description}

Example:
{code_input}
{code_output}

{your_input}
{your_output}
```

### Code Example - Natural Language to SQL

```
Transform natural language requests into SQL queries.

Example:
Natural: "Show me all customers who signed up last month"
SQL:
```sql
SELECT * FROM customers
WHERE signup_date >= DATE_SUB(NOW(), INTERVAL 1 MONTH)
ORDER BY signup_date DESC
```

Natural: "Find the top 10 products by revenue this year"
SQL:
```

### Caution with Code Examples

**Important:** Ensure code examples are correct and follow best practices. The AI will copy patterns from examples, including mistakes!

**Risks:**
- Copying security vulnerabilities from examples
- Replicating deprecated APIs or patterns
- Perpetuating bad coding practices

**Best practices for code examples:**
- Verify code works before including
- Use modern, idiomatic code
- Include comments explaining the approach
- Show error handling if relevant
- Follow language-specific style guides

## Classification Task Best Practices

For classification tasks, how you organize your examples matters as much as the examples themselves.

### Mix Up the Classes

Don't group all examples of the same class together.

**Good - Mixed classes:**
```
Example 1: Review → Positive
Example 2: Review → Negative
Example 3: Review → Positive
Example 4: Review → Negative
Example 5: Review → Neutral
Example 6: Review → Positive
```

**Bad - Sequential classes:**
```
Example 1: Review → Positive
Example 2: Review → Positive
Example 3: Review → Positive
Example 4: Review → Negative
Example 5: Review → Negative
Example 6: Review → Neutral
```

**Why mixing matters:** When examples are grouped by class, the model may learn the pattern order ("3 positives, then negatives") rather than the actual classification criteria. Mixing forces the model to understand what makes each review positive or negative.

### Starting Point: 6 Examples

For classification tasks, start with approximately 6 examples:
- **Binary classification** (2 classes): ~3 examples per class
- **Multi-class** (3+ classes): ~2 examples per class

Test and adjust from there based on performance.

### Label Distribution

Match your example distribution to expected real-world distribution:

```
If in production:
- 70% of reviews are positive
- 20% are negative
- 10% are neutral

Then in examples, use approximately:
- 4 positive
- 1-2 negative
- 1 neutral
```

This prevents the model from being biased toward underrepresented classes.

### Per-Class Variation

Ensure examples for each class show variety:

**Positive examples should show:**
- Different reasons for positivity (quality, speed, price, service)
- Different lengths and styles
- Different intensities (mildly positive vs very positive)

**Negative examples should show:**
- Different complaint types (defective, late, rude, expensive)
- Different emotional intensities
- Different expressions of dissatisfaction

This helps the model understand the core concept of each class rather than surface patterns.

## Common Mistakes

1. **Too Many Examples**: More isn't always better; can dilute focus
2. **Irrelevant Examples**: Examples should match the target task closely
3. **Inconsistent Formatting**: Confuses the AI about output format
4. **Overly Specific Examples**: AI may copy too literally without generalizing
5. **Ignoring Length**: Too many examples leave insufficient room for input/output

## Quick Reference

### When to Use Example-Based Learning
- Format transformation tasks
- Style imitation
- Pattern recognition
- Complex instructions hard to articulate
- Reducing ambiguity

### When Examples May Not Help
- Simple factual queries
- Well-established standard formats
- When examples add confusion
- When context space is limited

### Optimal Example Characteristics
- Clear input-output relationship
- Consistent formatting across all examples
- Representative of target task
- Span complexity range
- Cover edge cases
- Concise and focused

## Quick Reference Card

### When to Use Each Technique

| Technique | Use When... |
|-----------|------------|
| **Zero-Shot** | Simple task, common format, limited space |
| **One-Shot** | Format unclear, zero-shot inconsistent, one good example exists |
| **Few-Shot** | Multiple patterns, edge cases, complex format |

### Example Selection Guidelines

- **Semantic similarity**: Match examples to input type
- **Diversity sampling**: Cover different patterns and edge cases
- **Difficulty progression**: Simple → Moderate → Complex
- **Error-based**: Include examples addressing common failures

### Classification Best Practices

- Mix up class order in examples (don't group by class)
- Start with 6 examples (2-3 per class)
- Match label distribution to real-world data
- Show variety within each class

### Common Mistakes to Avoid

1. Too many examples (dilutes focus)
2. Irrelevant examples (doesn't match task)
3. Inconsistent formatting (confuses the AI)
4. Sequential class ordering (causes pattern learning)
5. Uncopying bad code from examples (verify your examples!)

