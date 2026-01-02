# Prompt Template Patterns

Reusable template patterns for effective prompts.

## Template Structure

Basic components:

```
[Role/Context] - Who the AI should be
[Task/Instruction] - What the AI should do
[Examples] - How to approach the task (optional)
[Input Data] - The specific content to process
[Output Format] - Expected structure
```

**Example Template:**
```
You are an expert {role} specializing in {domain}.

Task: {task_description}

{optional_examples}

Input: {user_input}

{output_format_specification}
```

## Template Types

### 1. Classification Template

Classify input into predefined categories:

```
Classify the {content_type} into one of these categories: {categories}

{if_examples: Here are some examples:
{examples}
}

{content_type}: {user_input}

Category:
```

**Usage Example:**
```
Classify the email into one of these categories: Urgent, Important, Normal, Low Priority

Examples:
Email: "Server is down, production affected!"
Category: Urgent

Email: "Meeting reminder for tomorrow"
Category: Normal

Email: {user_email}

Category:
```

### 2. Extraction Template

Extract structured information from text:

```
Extract {information_type} from the {content_type}.

Required fields:
{field_list}

{if_examples: Example extractions:
{examples}
}

{content_type}: {user_input}

Extracted information:
```

**Usage Example:**
```
Extract event details from the text.

Required fields:
- Event name
- Date
- Time
- Location
- Organizer

Example:
Text: "Join us for the Annual Tech Summit on March 15th at 9 AM in the Grand Hall, hosted by TechCorp."
Extracted:
- Event name: Annual Tech Summit
- Date: March 15th
- Time: 9 AM
- Location: Grand Hall
- Organizer: TechCorp

Text: {user_text}

Extracted:
```

### 3. Transformation Template

Transform input from one format to another:

```
Transform the {source_format} to {target_format}.

Transformation rules:
{rules}

{if_examples: Example transformations:
{examples}
}

Input {source_format}:
{user_input}

Output {target_format}:
```

**Usage Example:**
```
Transform casual text to professional email.

Transformation rules:
- Use formal greetings and closings
- Complete abbreviations
- Remove emojis
- Use proper grammar and punctuation

Example:
Input: "hey, can u send me the files asap? thx!"
Output: "Dear [Name], Could you please send me the files at your earliest convenience? Thank you."

Input: {user_input}

Output:
```

### 4. Generation Template

Generate new content based on specifications:

```
Generate {output_type} based on the {input_type}.

Requirements:
{requirements}

{if_style: Style: {style}}
{if_constraints: Constraints:
{constraints}}
{if_examples: Examples:
{examples}}

{input_type}: {user_input}

{output_type}:
```

**Usage Example:**
```
Generate a social media post based on the product description.

Requirements:
- Length: 100-150 characters
- Tone: Enthusiastic and professional
- Include relevant hashtags
- Highlight key benefit

Style: Concise and engaging

Product description: {user_product}

Social media post:
```

### 5. Question Answering Template

Answer questions based on provided context:

```
Answer the question based on the context below.

Context:
{context}

{if_examples: Examples:
Q: {example_question}
A: {example_answer}
}

Question: {user_question}

Answer:
```

**Usage Example:**
```
Answer the question based on the company policy below.

Context:
"Vacation Policy: Full-time employees accrue 2.5 vacation days per month. Requests must be submitted 2 weeks in advance. Maximum 2 consecutive weeks during peak season."

Q: How many vacation days do I get per year?
A: Full-time employees accrue 30 vacation days per year (2.5 days × 12 months).

Question: {user_question}

Answer:
```

## Conditional Components

### Optional Sections

Include sections only when relevant:

```
You are a {role}.

{if_context: Context: {context}}

Task: {task}

{if_examples: Reference examples:
{examples}}

{if_constraints: Constraints:
{constraints}}

Input: {user_input}

Output:
```

### Adaptive Complexity

Add complexity based on task difficulty:

```
Task: {task}

{if_complex: For this complex task:
- Break it into steps
- Show your reasoning
- Verify your answer}

{if_simple: Provide a direct answer}

Input: {user_input}
```

## Modular Template Design

### Component-Based Structure

Create reusable prompt components:

```
[COMPONENT: Role]
You are an expert {role} with {experience_level} experience.
You specialize in {specialization}.

[COMPONENT: Task Analysis]
Task: {task}
Goal: {goal}
Audience: {audience}

[COMPONENT: Guidelines]
- {guideline_1}
- {guideline_2}
- {guideline_3}

[COMPONENT: Output Format]
Format: {format}
Structure: {structure}
```

### Composing Templates

Combine components for different use cases:

**Simple Prompt:**
```
[Role]

[Task Analysis - simplified]

Input: {input}
```

**Detailed Prompt:**
```
[Role]
[Task Analysis - full]
[Guidelines]
[Output Format]
[Examples]
Input: {input}
```

## Multi-Turn Templates

### Conversation Template

For back-and-forth interactions:

```
System: You are a helpful {role} specializing in {domain}.

Conversation so far:
{conversation_history}

User: {current_message}

{agent_name}:
```

### Progressive Workflow

For multi-step processes:

```
Stage {current_stage} of {total_stages}: {stage_name}

Previous stages completed:
{completed_stages}

Current task:
{current_task}

{if_next: Next stages:
{upcoming_stages}}

Output for this stage:
```

**Usage Example:**
```
Stage 1 of 3: Information Gathering

Previous stages completed: None

Current task:
Identify the key stakeholders for this project.

Output for this stage:
List the stakeholders with their roles and influence level.
```

## AI-to-AI Prompt Templates

Templates for when one AI agent creates prompts for another AI agent.

### Task Delegation Template

```
As the {receiving_agent_type}, please {task}.

Context:
- Delegating from: {sending_agent_type}
- Task purpose: {why_this_task}
- Dependencies: {what_this_depends_on}
- Output will be used by: {next_agent_or_purpose}

{task_details}
```

**Usage Example:**
```
As the code reviewer agent, please review these recent changes.

Context:
- Delegating from: Orchestrator agent
- Task purpose: Ensure code quality before merging
- Dependencies: Changes are in src/auth/* directory
- Output will be used by: Documentation agent to update API docs

Files changed:
- src/auth/login.js
- src/auth/oauth.js

Focus on security vulnerabilities and code quality issues.
```

### Inter-Agent Workflow Template

```
This prompt initiates a multi-agent workflow.

Step 1 of {total_steps}: {step_description}

Your role: {agent_role}
Your task: {specific_task}

When complete, provide output in this format:
{structured_output_format}

The next agent will use your output to: {next_step_description}
```

**Usage Example:**
```
This prompt initiates a multi-agent workflow.

Step 1 of 3: Code Analysis

Your role: Code analyzer agent
Your task: Identify the main components and dependencies in this codebase.

When complete, provide output in this format:
{
  "components": [{"name": "...", "file": "..."}],
  "dependencies": [{"from": "...", "to": "..."}]
}

The next agent will use your output to generate architecture diagrams.
```

### Meta-Prompt Template

```
Generate a prompt that will {target_task}.

The generated prompt should be for: {target_agent_type}

Required elements in the generated prompt:
- {element_1}
- {element_2}

Context: {context_information}

Generate the prompt:
```

**Usage Example:**
```
Generate a prompt that will extract product features from user reviews.

The generated prompt should be for: A data extraction agent

Required elements in the generated prompt:
- Clear task definition
- Output format specification (JSON)
- Example of desired extraction

Context: We have 10,000 customer reviews to process. Features can be positive or negative mentions.

Generate the prompt:
```

### Skill Creation Template

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

**Usage Example:**
```
Create a skill for database-query-review.

Skill purpose: Analyze SQL queries for performance and security issues

The skill should include:
- Clear role definition
- Core capabilities (3-5 items)
- When to use the skill
- Example prompts

Output format: SKILL.md structure
```

### Context Propagation Template

```
{main_task}

Context from previous agent:
{previous_context}

Continuing from:
{previous_stage_summary}

Your task:
{specific_task}

Ensure output maintains:
{consistency_requirements}
```

**Usage Example:**
```
Review this code for security issues.

Context from previous agent:
The analyzer agent identified this file as handling authentication.
It uses OAuth 2.0 and stores sessions in Redis.

Continuing from:
Analysis complete - authentication flow uses industry-standard OAuth.

Your task:
Review for security vulnerabilities including:
- Token handling
- Session management
- Input validation

Ensure output maintains:
Focus on OAuth-specific vulnerabilities
```

### Agent Handoff Template

```
{task_description}

You are agent {N} of {total_agents}.

Your responsibility: {specific_responsibility}

Input from previous agent:
{previous_agent_output}

Your output should:
{output_requirements}

Next agent will:
{next_agent_role}
```

**Usage Example:**
```
Analyze this bug report.

You are agent 2 of 4.

Your responsibility: Categorize the bug severity and type.

Input from previous agent:
Bug reported in checkout flow. Users unable to complete payment after adding items to cart.

Your output should:
- Provide severity rating (Critical/High/Medium/Low)
- Categorize bug type (Functional/UI/Performance/Security)
- Include reasoning

Next agent will:
Investigate root cause by examining checkout code.
```

## Best Practices

1. **Keep It DRY**: Use templates to avoid repetition
2. **Validate Early**: Ensure all variables have appropriate values
3. **Version Templates**: Track changes like any other content
4. **Test Variations**: Ensure templates work with diverse inputs
5. **Document Variables**: Clearly specify required/optional variables
6. **Provide Defaults**: Set sensible default values where appropriate
7. **Use Clear Placeholders**: Make variable names self-explanatory
8. **Group Related Elements**: Keep related information together

## Template Library

### Analysis Templates

**SWOT Analysis:**
```
Perform a SWOT analysis for {subject}.

Strengths:
- Identify internal advantages
- List key capabilities

Weaknesses:
- Identify internal limitations
- List areas for improvement

Opportunities:
- Identify external possibilities
- List potential growth areas

Threats:
- Identify external risks
- List potential challenges

Subject: {input}
```

**Cost-Benefit Analysis:**
```
Analyze the costs and benefits of {proposal}.

Costs:
- Direct costs: {consider_direct_costs}
- Indirect costs: {consider_indirect_costs}
- Opportunity costs: {consider_opportunity_costs}

Benefits:
- Tangible benefits: {consider_tangible_benefits}
- Intangible benefits: {consider_intangible_benefits}
- Long-term value: {consider_long_term_value}

Conclusion:
Provide recommendation based on the analysis.
```

### Content Creation Templates

**Blog Post:**
```
Write a blog post about {topic}.

Requirements:
- Length: {word_count} words
- Target audience: {audience}
- Tone: {tone}
- Key points to cover: {key_points}

Structure:
1. Engaging title
2. Introduction (hook + thesis)
3. Main body (3-5 sections)
4. Conclusion with call-to-action

Topic: {topic}

Blog post:
```

**Product Description:**
```
Write a compelling product description for {product}.

Product details:
- Features: {features}
- Benefits: {benefits}
- Target audience: {audience}
- Price point: {price}

Requirements:
- Highlight unique value proposition
- Address customer pain points
- Include social proof if available
- End with clear call-to-action

Product: {product}

Description:
```

### Problem-Solving Templates

**Troubleshooting:**
```
Help troubleshoot: {problem_description}

System information:
{system_info}

Error messages:
{error_messages}

Recent changes:
{recent_changes}

Provide:
1. Most likely cause
2. Diagnostic steps
3. Solution options
4. Prevention recommendations
```

**Decision Framework:**
```
Help make a decision about {decision}.

Options:
{options}

Criteria for evaluation:
{criteria}

Provide:
1. Comparison of options against criteria
2. Pros and cons of each option
3. Risk assessment
4. Recommendation with rationale
```

## Code Prompting Templates

### Code Generation

Generate new code based on specifications:

```
Generate {code_type} code to {task_description}.

Requirements:
- Language: {programming_language}
- Style: {style_guide}
- Error handling: {yes/no}
- Comments: {comment_level}
- Testing: {test_requirements}

{if_examples: Reference implementation:
```{language}
{code_example}
```
}}

Generate code:
```

**Usage example:**
```
Generate backend API code to handle user authentication.

Requirements:
- Language: Python
- Style: PEP-8 compliant
- Error handling: Yes (handle all exceptions)
- Comments: Docstrings for all functions
- Testing: Include pytest test cases

Reference implementation:
```python
def hash_password(password: str) -> str:
    """Hash a password using bcrypt."""
    import bcrypt
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
```

Generate code:
```

### Code Explanation

Explain what existing code does:

```
Explain what this {code_type} code does:

```{language}
{code_to_explain}
```

Focus on:
- Overall purpose
- Key functions/methods
- Data flow
- Notable patterns or anti-patterns
- {specific_focus}

Explanation:
```

**Usage example:**
```
Explain what this Python code does:

```python
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)
```

Focus on:
- Overall purpose
- How reduce() is used
- Lambda function behavior
- Edge cases

Explanation:
```

### Code Translation

Translate code from one language to another:

```
Translate this {source_language} code to {target_language}:

```{source_language}
{source_code}
```

Preserve:
- Functionality
- Variable naming conventions
- Comments
- Error handling

Translated code:
```

**Usage example:**
```
Translate this JavaScript code to Python:

```javascript
function formatDate(date) {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return date.toLocaleDateString('en-US', options);
}
```

Preserve:
- Functionality
- Parameter names
- Documentation

Translated code:
```

### Code Debugging

Debug and fix broken code:

```
This code has an error:
{error_message}

```{language}
{code_with_error}
```

Debug what's wrong and provide:
1. Root cause explanation
2. Fixed code
3. How to prevent similar issues

Debug:
```

**Usage example:**
```
This code has an error:
IndexError: list index out of range

```python
def get_middle(items):
    return items[len(items) // 2]

items = [1, 2, 3, 4]
print(get_middle(items))  # Works

items = [1, 2]
print(get_middle(items))  # Fails
```

Debug what's wrong and provide:
1. Root cause explanation
2. Fixed code
3. How to prevent similar issues

Debug:
```

## JSON Schema Templates

### Input Schema

Define expected JSON input structure:

```
I need you to process {data_type} with this structure:

Schema:
```json
{
    "type": "object",
    "properties": {
        "field1": {"type": "string", "description": "..."},
        "field2": {"type": "number", "description": "..."},
        "field3": {
            "type": "array",
            "items": {"type": "string"},
            "description": "..."
        }
    },
    "required": ["field1", "field2"]
}
```

Input data conforming to schema:
{user_input}

Process the data:
```

**Usage example:**
```
I need you to analyze sales data with this structure:

Schema:
```json
{
    "type": "object",
    "properties": {
        "period": {"type": "string", "description": "Time period (e.g., 'Q1 2024')"},
        "revenue": {"type": "number", "description": "Total revenue"},
        "region": {"type": "string", "description": "Sales region"}
    },
    "required": ["period", "revenue", "region"]
}
```

Input data:
```json
{"period": "Q1 2024", "revenue": 150000, "region": "North America"}
```

Analyze the data:
```

### Output with Schema

Request JSON output with specific structure:

```
Extract {information_type} from the text.

Return JSON following this schema:
```json
{
    "field1": "description",
    "field2": "description",
    "field3": ["array", "of", "items"]
}
```

Text: {user_input}

JSON Output:
```

**Usage example:**
```
Extract event details from the text.

Return JSON following this schema:
```json
{
    "event_name": "Name of the event",
    "date": "ISO format date (YYYY-MM-DD)",
    "time": "Time in HH:MM format",
    "location": "Venue name",
    "attendees": ["List", "of", "attendees"]
}
```

Text: "The annual Tech Summit will be held on March 15th, 2024 at 9 AM in the Grand Hall. Confirmed attendees include Alice Johnson and Bob Smith from TechCorp."

JSON Output:
```

### JSON Repair

Fix malformed JSON:

```
This JSON is invalid:
{invalid_json}

Fix the JSON and return a valid version:
```

**Best practices for JSON outputs:**
- Always specify "Return JSON only, no additional text"
- Provide example of expected structure
- Use specific field names and types
- Specify if fields are required or optional
- Handle edge cases (empty arrays, null values)

## Variables in Prompts

Use variable placeholders for dynamic, reusable prompts:

### Simple Variables

```
Analyze the sentiment of customer reviews for {product_name}.

Review: {review_text}

Sentiment analysis:
```

**Usage:**
- Replace `{product_name}` with "Acme Widgets"
- Replace `{review_text}` with the actual review

### Multiple Variables

```
VARIABLES:
{city} = "Amsterdam"
{category} = "museums"
{count} = 3

PROMPT:
As a travel guide for {city}, recommend {count} {category}.
Include:
- Name of each location
- Brief description
- Why it's worth visiting

Recommendations:
```

### Variable Groups

Group related variables:

```
## Customer Context
{customer_name}
{customer_tier}
{purchase_history}

## Product Context
{product_name}
{product_category}
{product_price}

## Request
Draft a personalized email for {customer_name} about {product_name}.
```

### Optional Variables

```
Summarize the {document_type}.

{if_context: Context: {context}}

{if_requirements: Requirements:
- {requirements}}

{if_length_constraint: Length constraint: {length_constraint}}

Document: {document_text}

Summary:
```

### Benefits of Variables

1. **Reusability:** Use same template with different inputs
2. **Maintainability:** Easy to update template structure
3. **Clarity:** Clear what needs to be filled in
4. **Automation:** Can be dynamically replaced in applications
5. **Documentation:** Variables self-document the template

### Best Practices

1. **Use descriptive names:** `{customer_email}` not `{email}` or `{e}`
2. **Provide defaults:** `{language = "English"}`
3. **Document required vs optional:** Mark which variables must be filled
4. **Group related variables:** Organize by context or category
5. **Use consistent format:** Stick to `{variable_name}` style
6. **Validate inputs:** Check that variables contain valid values

## Quick Reference

### Template Variables
Use clear, descriptive placeholders:
- `{role}` - Who the AI should be
- `{task}` - What to do
- `{input}` - User-provided content
- `{format}` - Expected output structure
- `{constraints}` - Limitations and requirements
- `{examples}` - Demonstration examples

### Code Prompt Templates

| Task | Template Pattern |
|------|------------------|
| **Generate** | "Generate {language} code to {task}. Requirements: ..." |
| **Explain** | "Explain what this {language} code does. Focus on: ..." |
| **Translate** | "Translate this {source} code to {target}. Preserve: ..." |
| **Debug** | "This code has error: {message}. Debug and provide: 1) Root cause 2) Fixed code 3) Prevention" |

### JSON Schema Templates

| Purpose | Pattern |
|---------|---------|
| **Input schema** | "Process data with this structure: ```json {...}```" |
| **Output schema** | "Return JSON following this schema: ```json {...}```" |
| **JSON repair** | "This JSON is invalid: {...}. Fix and return valid version." |

**Best practice:** Always specify "Return JSON only, no additional text"

### Variable Best Practices

1. **Descriptive names:** `{customer_email}` not `{e}`
2. **Group related variables:** Organize by context/category
3. **Document defaults:** `{language = "English"}`
4. **Mark required:** Indicate which variables must be filled
5. **Consistent format:** Use `{variable_name}` style

### Common Structures

**Simple:**
```
[Role] + [Task] + [Input] + [Output]
```

**With Examples:**
```
[Role] + [Task] + [Examples] + [Input] + [Output]
```

**Comprehensive:**
```
[Role] + [Context] + [Task] + [Guidelines] + [Examples] + [Input] + [Format] + [Constraints]
```

### When to Use Templates
- Repetitive tasks with consistent structure
- Multi-step processes
- Standardized outputs
- Team collaboration (shared prompts)
- A/B testing variations
- Dynamic variable replacement
- Code generation and analysis
- Structured data extraction

