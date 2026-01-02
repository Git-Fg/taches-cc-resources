## Overview
Core principles guide skill authoring decisions. These principles ensure skills are efficient, effective, and maintainable across different models and use cases.

## Markdown Structure Principle
## Description
Skills use Markdown headings for structure to ensure readability and maintainability. XML is reserved only for highly structured elements like routing decisions in router pattern skills.

## Why Markdown Headings
## Consistency
Markdown headings provide consistent structure across all skills. Common section names appear consistently:
- `## Objective` or `# Objective` defines what the skill does
- `## Quick Start` provides immediate guidance
- `## Success Criteria` defines completion

This consistency makes skills predictable and easier to read and maintain.

## Readability
Markdown is human-readable and works well with all editors and tools. Claude can reliably:
- Identify section boundaries through heading levels
- Understand content purpose from semantic heading names
- Navigate structure efficiently
- Parse content programmatically when needed

## Accessibility
Markdown headings are:
- Easier to read directly in source files
- Supported by all editors and preview tools
- More familiar to developers
- Simpler to debug and modify

## Critical Rule
**Use Markdown headings (#, ##, ###) for structure.** Keep markdown formatting within content (bold, italic, lists, code blocks, links). Reserve XML only for router pattern skills with complex routing logic.

## Required Sections
Every skill MUST have:
- `## Objective` or `# Objective` - What the skill does and why it matters
- `## Quick Start` or similar - Immediate, actionable guidance
- `## Success Criteria` or `## When Successful` - How to know it worked

See [skill-structure.md](skill-structure.md) for conditional sections and structure guidance.

## Conciseness Principle
## Description
The context window is shared. Your skill shares it with the system prompt, conversation history, other skills' metadata, and the actual request.

## Guidance
Only add context Claude doesn't already have. Challenge each piece of information:
- "Does Claude really need this explanation?"
- "Can I assume Claude knows this?"
- "Does this paragraph justify its token cost?"

Assume Claude is smart. Don't explain obvious concepts.

## Concise Example
**Concise** (~50 tokens):
```markdown
## Quick Start

Extract PDF text with pdfplumber:

```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```
```

**Verbose** (~150 tokens):
```markdown
## Quick Start

PDF files are a common file format used for documents. To extract text from them, we'll use a Python library called pdfplumber. First, you'll need to import the library, then open the PDF file using the open method, and finally extract the text from each page. Here's how to do it:

```python
import pdfplumber

with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

This code opens the PDF and extracts text from the first page.
```

The concise version assumes Claude knows what PDFs are, understands Python imports, and can read code. All those assumptions are correct.

## When To Elaborate
Add explanation when:
- Concept is domain-specific (not general programming knowledge)
- Pattern is non-obvious or counterintuitive
- Context affects behavior in subtle ways
- Trade-offs require judgment

Don't add explanation for:
- Common programming concepts (loops, functions, imports)
- Standard library usage (reading files, making HTTP requests)
- Well-known tools (git, npm, pip)
- Obvious next steps

## Degrees Of Freedom Principle
## Description
Match the level of specificity to the task's fragility and variability. Give Claude more freedom for creative tasks, less freedom for fragile operations.

## High Freedom
## When
- Multiple approaches are valid
- Decisions depend on context
- Heuristics guide the approach
- Creative solutions welcome

## Example
```markdown
## Objective

Review code for quality, bugs, and maintainability.

## Process

1. Analyze the code structure and organization
2. Check for potential bugs or edge cases
3. Suggest improvements for readability and maintainability
4. Verify adherence to project conventions

## Success Criteria

- All major issues identified
- Suggestions are actionable and specific
- Review balances praise and criticism
```

Claude has freedom to adapt the review based on what the code needs.

## Medium Freedom
## When
- A preferred pattern exists
- Some variation is acceptable
- Configuration affects behavior
- Template can be adapted

## Example
```markdown
## Objective

Generate reports with customizable format and sections.

## Template

Use this template and customize as needed:

```python
def generate_report(data, format="markdown", include_charts=True):
    # Process data
    # Generate output in specified format
    # Optionally include visualizations
```

## Success Criteria

- Report includes all required sections
- Format matches user preference
- Data accurately represented
```

Claude can customize the template based on requirements.

## Low Freedom
## When
- Operations are fragile and error-prone
- Consistency is critical
- A specific sequence must be followed
- Deviation causes failures

## Example
```markdown
## Objective

Run database migration with exact sequence to prevent data loss.

## Process

Run exactly this script:

```bash
python scripts/migrate.py --verify --backup
```

**Do not modify the command or add additional flags.**

## Success Criteria

- Migration completes without errors
- Backup created before migration
- Verification confirms data integrity
```

Claude must follow the exact command with no variation.

## Matching Specificity
The key is matching specificity to fragility:

- **Fragile operations** (database migrations, payment processing, security): Low freedom, exact instructions
- **Standard operations** (API calls, file processing, data transformation): Medium freedom, preferred pattern with flexibility
- **Creative operations** (code review, content generation, analysis): High freedom, heuristics and principles

Mismatched specificity causes problems:
- Too much freedom on fragile tasks → errors and failures
- Too little freedom on creative tasks → rigid, suboptimal outputs

## Model Testing Principle
## Description
Skills act as additions to models, so effectiveness depends on the underlying model. What works for Opus might need more detail for Haiku.

## Testing Across Models
Test your skill with all models you plan to use:

## Haiku Testing
**Claude Haiku** (fast, economical)

Questions to ask:
- Does the skill provide enough guidance?
- Are examples clear and complete?
- Do implicit assumptions become explicit?
- Does Haiku need more structure?

Haiku benefits from:
- More explicit instructions
- Complete examples (no partial code)
- Clear success criteria
- Step-by-step workflows

## Sonnet Testing
**Claude Sonnet** (balanced)

Questions to ask:
- Is the skill clear and efficient?
- Does it avoid over-explanation?
- Are workflows well-structured?
- Does progressive disclosure work?

Sonnet benefits from:
- Balanced detail level
- Markdown structure for clarity
- Progressive disclosure
- Concise but complete guidance

## Opus Testing
**Claude Opus** (powerful reasoning)

Questions to ask:
- Does the skill avoid over-explaining?
- Can Opus infer obvious steps?
- Are constraints clear?
- Is context minimal but sufficient?

Opus benefits from:
- Concise instructions
- Principles over procedures
- High degrees of freedom
- Trust in reasoning capabilities

## Balancing Across Models
Aim for instructions that work well across all target models:

**Good balance**:
```markdown
## Quick Start

Use pdfplumber for text extraction:

```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

For scanned PDFs requiring OCR, use pdf2image with pytesseract instead.
```

This works for all models:
- Haiku gets complete working example
- Sonnet gets clear default with escape hatch
- Opus gets enough context without over-explanation

**Too minimal for Haiku**:
```markdown
## Quick Start

Use pdfplumber for text extraction.
```

**Too verbose for Opus**:
```markdown
## Quick Start

PDF files are documents that contain text. To extract that text, we use a library called pdfplumber. First, import the library at the top of your Python file. Then, open the PDF file using the pdfplumber.open() method. This returns a PDF object. Access the pages attribute to get a list of pages. Each page has an extract_text() method that returns the text content...
```

## Iterative Improvement
1. Start with medium detail level
2. Test with target models
3. Observe where models struggle or succeed
4. Adjust based on actual performance
5. Re-test and iterate

Don't optimize for one model. Find the balance that works across your target models.

## Progressive Disclosure Principle
## Description
SKILL.md serves as an overview. Reference files contain details. Claude loads reference files only when needed.

## Token Efficiency
Progressive disclosure keeps token usage proportional to task complexity:

- Simple task: Load SKILL.md only (~500 tokens)
- Medium task: Load SKILL.md + one reference (~1000 tokens)
- Complex task: Load SKILL.md + multiple references (~2000 tokens)

Without progressive disclosure, every task loads all content regardless of need.

## Implementation
- Keep SKILL.md under 500 lines
- Split detailed content into reference files
- Keep references one level deep from SKILL.md
- Link to references from relevant sections
- Use descriptive reference file names

See [skill-structure.md](skill-structure.md) for progressive disclosure patterns.

## Validation Principle
## Description
Validation scripts are force multipliers. They catch errors that Claude might miss and provide actionable feedback.

## Characteristics
Good validation scripts:
- Provide verbose, specific error messages
- Show available valid options when something is invalid
- Pinpoint exact location of problems
- Suggest actionable fixes
- Are deterministic and reliable

See [workflows-and-validation.md](workflows-and-validation.md) for validation patterns.

## Principle Summary
## Markdown Structure
Use Markdown headings for structure and readability. Required sections: Objective, Quick Start, Success Criteria. Reserve XML only for router pattern skills.

## Conciseness
Only add context Claude doesn't have. Assume Claude is smart. Challenge every piece of content.

## Degrees Of Freedom
Match specificity to fragility. High freedom for creative tasks, low freedom for fragile operations, medium for standard work.

## Model Testing
Test with all target models. Balance detail level to work across Haiku, Sonnet, and Opus.

## Progressive Disclosure
Keep SKILL.md concise. Split details into reference files. Load reference files only when needed.

## Validation
Make validation scripts verbose and specific. Catch errors early with actionable feedback.
