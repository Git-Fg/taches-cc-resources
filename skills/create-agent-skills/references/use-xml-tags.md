## Overview
Skills use pure XML structure for consistent parsing, efficient token usage, and improved Claude performance. This reference defines the required and conditional XML tags for skill authoring, along with intelligence rules for tag selection.


## Critical Rule
**Remove ALL markdown headings (#, ##, ###) from skill body content.** Replace with semantic XML tags. Keep markdown formatting WITHIN content (bold, italic, lists, code blocks, links).


## Required Tags
Every skill MUST have these three tags:

### Objective Tag
**Purpose**: What the skill does and why it matters. Sets context and scope.

**Content**: 1-3 paragraphs explaining the skill's purpose, domain, and value proposition.

**Example**:
```xml
<objective>
Extract text and tables from PDF files, fill forms, and merge documents using Python libraries. This skill provides patterns for common PDF operations without requiring external services or APIs.
</objective>
```


### Quick Start Tag
**Purpose**: Immediate, actionable guidance. Gets Claude started quickly without reading advanced sections.

**Content**: Minimal working example, essential commands, or basic usage pattern.

**Example**:
```xml
<quick_start>
Extract text with pdfplumber:

```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
</quick_start>
```


### Success Criteria Tag
**Purpose**: How to know the task worked. Defines completion criteria.

**Alternative name**: `<when_successful>` (use whichever fits better)

**Content**: Clear criteria for successful execution, validation steps, or expected outputs.

**Example**:
```xml
<success_criteria>
A well-structured skill has:

- Valid YAML frontmatter with descriptive name and description
- Pure XML structure with no markdown headings in body
- Required tags: objective, quick_start, success_criteria
- Progressive disclosure (SKILL.md < 500 lines, details in reference files)
- Real-world testing and iteration based on observed behavior
</success_criteria>
```



## Conditional Tags
Add these tags based on skill complexity and domain requirements:

### Context Tag
**When to use**: Background or situational information that Claude needs before starting.

**Example**:
```xml
<context>
The Facebook Marketing API uses a hierarchy: Account → Campaign → Ad Set → Ad. Each level has different configuration options and requires specific permissions. Always verify API access before making changes.
</context>
```


### Workflow Tag
**When to use**: Step-by-step procedures, sequential operations, multi-step processes.

**Alternative name**: `<process>`

**Example**:
```xml
<workflow>
1. **Analyze the form**: Run analyze_form.py to extract field definitions
2. **Create field mapping**: Edit fields.json with values
3. **Validate mapping**: Run validate_fields.py
4. **Fill the form**: Run fill_form.py
5. **Verify output**: Check generated PDF
</workflow>
```


### Advanced Features Tag
**When to use**: Deep-dive topics that most users won't need (progressive disclosure).

**Example**:
```xml
<advanced_features>
**Custom styling**: See [styling.md](styling.md)
**Template inheritance**: See [templates.md](templates.md)
**API reference**: See [reference.md](reference.md)
</advanced_features>
```


### Validation Tag
**When to use**: Skills with verification steps, quality checks, or validation scripts.

**Example**:
```xml
<validation>
After making changes, validate immediately:

```bash
python scripts/validate.py output_dir/
```

Only proceed when validation passes. If errors occur, review and fix before continuing.
</validation>
```


### Examples Tag
**When to use**: Multi-shot learning, input/output pairs, demonstrating patterns.

**Example**:
```xml
<examples>
<example number="1">
<input>User clicked signup button</input>
<output>track('signup_initiated', { source: 'homepage' })</output>
</example>

<example number="2">
<input>Purchase completed</input>
<output>track('purchase', { value: 49.99, currency: 'USD' })</output>
</example>
</examples>
```


### Anti-Patterns Tag
**When to use**: Common mistakes that Claude should avoid.

**Example**:
```xml
<anti_patterns>
<pitfall name="vague_descriptions">
- ❌ "Helps with documents"
- ✅ "Extract text and tables from PDF files"
</pitfall>

<pitfall name="too_many_options">
- ❌ "You can use pypdf, or pdfplumber, or PyMuPDF..."
- ✅ "Use pdfplumber for text extraction. For OCR, use pytesseract instead."
</pitfall>
</anti_patterns>
```


### Security Checklist Tag
**When to use**: Skills with security implications (API keys, payments, authentication).

**Example**:
```xml
<security_checklist>
- Never log API keys or tokens
- Always use environment variables for credentials
- Validate all user input before API calls
- Use HTTPS for all external requests
- Check API response status before proceeding
</security_checklist>
```


### Testing Tag
**When to use**: Testing workflows, test patterns, or validation steps.

**Example**:
```xml
<testing>
Test with all target models (Haiku, Sonnet, Opus):

1. Run skill on representative tasks
2. Observe where Claude struggles or succeeds
3. Iterate based on actual behavior
4. Validate XML structure after changes
</testing>
```


### Common Patterns Tag
**When to use**: Code examples, recipes, or reusable patterns.

**Example**:
```xml
<common_patterns>
<pattern name="error_handling">
```python
try:
    result = process_file(path)
except FileNotFoundError:
    print(f"File not found: {path}")
except Exception as e:
    print(f"Error: {e}")
```
</pattern>
</common_patterns>
```


### Reference Guides Tag
**When to use**: Links to detailed reference files (progressive disclosure).

**Alternative name**: `<detailed_references>`

**Example**:
```xml
<reference_guides>
For deeper topics, see reference files:

**API operations**: [references/api-operations.md](references/api-operations.md)
**Security patterns**: [references/security.md](references/security.md)
**Troubleshooting**: [references/troubleshooting.md](references/troubleshooting.md)
</reference_guides>
```



## Intelligence Rules
### Decision Tree
**Simple skills** (single domain, straightforward):
- Required tags only: objective, quick_start, success_criteria
- Example: Text extraction, file format conversion, simple calculations

**Medium skills** (multiple patterns, some complexity):
- Required tags + workflow/examples as needed
- Example: Document processing with steps, API integration with configuration

**Complex skills** (multiple domains, security, APIs):
- Required tags + conditional tags as appropriate
- Example: Payment processing, authentication systems, multi-step workflows with validation


### Principle
Don't over-engineer simple skills. Don't under-specify complex skills. Match tag selection to actual complexity and user needs.


### When to Add Conditional Tags
Ask these questions:

- **Context needed?** → Add `<context>`
- **Multi-step process?** → Add `<workflow>` or `<process>`
- **Advanced topics to hide?** → Add `<advanced_features>` + reference files
- **Validation required?** → Add `<validation>`
- **Pattern demonstration?** → Add `<examples>`
- **Common mistakes?** → Add `<anti_patterns>`
- **Security concerns?** → Add `<security_checklist>`
- **Testing guidance?** → Add `<testing>`
- **Code recipes?** → Add `<common_patterns>`
- **Deep references?** → Add `<reference_guides>`



## XML vs Markdown Headings
### Token Efficiency
XML tags are more efficient than markdown headings:

**Markdown headings**:
```markdown
## Quick start
## Workflow
## Advanced features
## Success criteria
```
Total: ~20 tokens, no semantic meaning to Claude

**XML tags**:
```xml
<quick_start>
<workflow>
<advanced_features>
<success_criteria>
```
Total: ~15 tokens, semantic meaning built-in


### Parsing Accuracy
XML provides unambiguous boundaries and semantic meaning. Claude can reliably:
- Identify section boundaries
- Understand content purpose
- Skip irrelevant sections
- Parse programmatically

Markdown headings are just visual formatting. Claude must infer meaning from heading text.


### Consistency
XML enforces consistent structure across all skills. All skills use the same tag names for the same purposes. Makes it easier to:
- Validate skill structure programmatically
- Learn patterns across skills
- Maintain consistent quality



## Nesting Guidelines
### Proper Nesting
XML tags can nest for hierarchical content:

```xml
<examples>
<example number="1">
<input>User input here</input>
<output>Expected output here</output>
</example>

<example number="2">
<input>Another input</input>
<output>Another output</output>
</example>
</examples>
```


### Closing Tags
Always close tags properly:

✅ Good:
```xml
<objective>
Content here
</objective>
```

❌ Bad:
```xml
<objective>
Content here
```


### Tag Naming
Use descriptive, semantic names:
- `<workflow>` not `<steps>`
- `<success_criteria>` not `<done>`
- `<anti_patterns>` not `<dont_do>`

Be consistent within your skill. If you use `<workflow>`, don't also use `<process>` for the same purpose.



## Anti-Pattern
**DO NOT use markdown headings in skill body content.**

❌ Bad (hybrid approach):
```markdown
# PDF Processing

## Quick start

Extract text with pdfplumber...

## Advanced features

Form filling...
```

✅ Good (pure XML):
```markdown
<objective>
PDF processing with text extraction, form filling, and merging.
</objective>

<quick_start>
Extract text with pdfplumber...
</quick_start>

<advanced_features>
Form filling...
</advanced_features>
```


## Benefits
### Clarity
Clearly separate different sections with unambiguous boundaries


### Accuracy
Reduce parsing errors. Claude knows exactly where sections begin and end.


### Flexibility
Easily find, add, remove, or modify sections without rewriting


### Parseability
Programmatically extract specific sections for validation or analysis


### Efficiency
Lower token usage compared to markdown headings


### Consistency
Standardized structure across all skills in the ecosystem



## Combining with Other Techniques
XML tags work well with other prompting techniques:

**Multi-shot learning**:
```xml
<examples>
<example number="1">...</example>
<example number="2">...</example>
</examples>
```

**Chain of thought**:
```xml
<thinking>
Analyze the problem...
</thinking>

<answer>
Based on the analysis...
</answer>
```

**Template provision**:
```xml
<template>
```markdown
# Report Title

## Summary
...
```
</template>
```

**Reference material**:
```xml
<schema>
{
  "field": "type"
}
</schema>
```


## Tag Reference Pattern
When referencing content in tags, use the tag name:

"Using the schema in `<schema>` tags..."
"Follow the workflow in `<workflow>`..."
"See examples in `<examples>`..."

This makes the structure self-documenting.

