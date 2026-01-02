# Skill Structure

## Overview

Skills have three structural components: YAML frontmatter (metadata), Markdown body structure (content organization), and progressive disclosure (file organization). This reference defines requirements and best practices for each component.

## Markdown Structure Requirements

### Critical Rule

**Use Markdown headings (#, ##, ###) for structure.** Reserve XML only for highly structured elements like routing decisions in router pattern skills. Keep markdown formatting within content (bold, italic, lists, code blocks, links).

### Required Sections

Every skill MUST have these three sections:

- **`## Objective`** or **`# Objective`** - What the skill does and why it matters (1-3 paragraphs)
- **`## Quick Start`** or similar - Immediate, actionable guidance (minimal working example)
- **`## Success Criteria`** or **`## When Successful`** - How to know it worked

### Conditional Sections

Add based on skill complexity and domain requirements:

- **`## Context`** - Background/situational information
- **`## Process`** or **`## Workflow`** - Step-by-step procedures
- **`## Advanced Features`** - Deep-dive topics (progressive disclosure)
- **`## Verification`** or **`## Validation`** - How to verify outputs
- **`## Examples`** - Multi-shot learning demonstrations
- **`## Anti-Patterns`** - Common mistakes to avoid
- **`## Security Checklist`** - Non-negotiable security patterns
- **`## Testing`** - Testing workflows
- **`## Common Patterns`** - Code examples and recipes
- **`## Reference Guides`** - Links to reference files

### Section Selection Intelligence

**Simple skills** (single domain, straightforward):
- Required sections only
- Example: Text extraction, file format conversion

**Medium skills** (multiple patterns, some complexity):
- Required sections + workflow/examples as needed
- Example: Document processing with steps, API integration

**Complex skills** (multiple domains, security, APIs):
- Required sections + conditional sections as appropriate
- Example: Payment processing, authentication systems, multi-step workflows

### Heading Hierarchy

Use proper heading hierarchy for clarity:

```markdown
# Main Section (skill file title)

## Major Section
Content...

### Subsection
Content...

#### Detail (rarely needed)
Content...
```

Be consistent within your skill. Don't skip heading levels.

## YAML Requirements

### Required Fields

```yaml
---
name: skill-name-here
description: What it does and when to use it (third person, specific triggers)
---
```

### Name Field

**Validation rules**:
- Maximum 64 characters
- Lowercase letters, numbers, hyphens only
- No reserved words: "anthropic", "claude"
- Must match directory name exactly

**Examples**:
- ✅ `process-pdfs`
- ✅ `manage-facebook-ads`
- ✅ `setup-stripe-payments`
- ❌ `PDF_Processor` (uppercase)
- ❌ `helper` (vague)
- ❌ `claude-helper` (reserved word)

### Description Field

**Validation rules**:
- Non-empty, maximum 1024 characters
- Third person (never first or second person)
- Include what it does AND when to use it
- Use strong language patterns (MUST USE/PROACTIVELY USE/CONSULT)

**Critical rule**: Always write in third person with strong modal verbs.
- ✅ "Processes Excel files and generates reports. MUST USE when..."
- ✅ "Analyzes Excel spreadsheets and creates pivot tables. PROACTIVELY USE when..."
- ✅ "Provides expert guidance on API design. CONSULT when..."
- ❌ "I can help you process Excel files"
- ❌ "You can use this to process Excel files"

**Structure**: Include both capabilities and triggers with strong language.

**Language strength hierarchy**:
1. **MUST USE** - For creation/critical skills where usage is mandatory
2. **PROACTIVELY USE** - For skills that should be used proactively
3. **CONSULT** - For reference/expert guidance skills

**Effective examples**:

```yaml
# MUST USE pattern (creation/critical skills)
description: Expert guidance for creating AI agent skills. MUST USE when working with SKILL.md files, authoring new skills, or understanding best practices.
```

```yaml
# PROACTIVELY USE pattern (proactive usage skills)
description: Analyzes any project to understand structure, tech stack, patterns, and conventions. PROACTIVELY USE when starting work on a new codebase, onboarding, or asked "how does this project work?"
```

```yaml
# CONSULT pattern (reference/expert guidance skills)
description: Expert guidance for REST and GraphQL API design including endpoints, error handling, versioning, and documentation. CONSULT when designing APIs, creating endpoints, or asked about API patterns.
```

**Avoid**:
```yaml
description: Helps with documents
```

```yaml
description: Processes data
```

```yaml
description: Use when...  # Missing strong modal verb
```

## Naming Conventions

Use **verb-noun convention** for skill names:

### Create

Building/authoring tools

Examples: `create-agent-skills`, `create-hooks`, `create-landing-pages`

### Manage

Managing external services or resources

Examples: `manage-facebook-ads`, `manage-zoom`, `manage-stripe`, `manage-supabase`

### Setup

Configuration/integration tasks

Examples: `setup-stripe-payments`, `setup-meta-tracking`

### Generate

Generation tasks

Examples: `generate-ai-images`

### Avoid Patterns

- Vague: `helper`, `utils`, `tools`
- Generic: `documents`, `data`, `files`
- Reserved words: `anthropic-helper`, `claude-tools`
- Inconsistent: Directory `facebook-ads` but name `facebook-ads-manager`

## Progressive Disclosure

### Principle

SKILL.md serves as an overview that points to detailed materials as needed. This keeps context window usage efficient.

### Practical Guidance

- Keep SKILL.md body under 500 lines
- Split content into separate files when approaching this limit
- Keep references one level deep from SKILL.md
- Add table of contents to reference files over 100 lines

### High Level Guide Pattern

Quick start in SKILL.md, details in reference files:

```markdown
---
name: pdf-processing
description: Extracts text and tables from PDF files, fills forms, and merges documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.
---

## Objective

Extract text and tables from PDF files, fill forms, and merge documents using Python libraries.

## Quick Start

Extract text with pdfplumber:

```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

## Advanced Features

**Form filling**: See [forms.md](forms.md)
**API reference**: See [reference.md](reference.md)
```

Claude loads forms.md or reference.md only when needed.

### Domain Organization Pattern

For skills with multiple domains, organize by domain to avoid loading irrelevant context:

```
bigquery-skill/
├── SKILL.md (overview and navigation)
└── reference/
    ├── finance.md (revenue, billing metrics)
    ├── sales.md (opportunities, pipeline)
    ├── product.md (API usage, features)
    └── marketing.md (campaigns, attribution)
```

When user asks about revenue, Claude reads only finance.md. Other files stay on filesystem consuming zero tokens.

### Conditional Details Pattern

Show basic content in SKILL.md, link to advanced in reference files:

```markdown
## Objective

Process DOCX files with creation and editing capabilities.

## Quick Start

**Creating documents**: Use docx-js for new documents. See [docx-js.md](docx-js.md).

**Editing documents**: For simple edits, modify XML directly.

**For tracked changes**: See [redlining.md](redlining.md)
**For OOXML details**: See [ooxml.md](ooxml.md)
```

Claude reads redlining.md or ooxml.md only when the user needs those features.

### Critical Rules

**Keep references one level deep**: All reference files should link directly from SKILL.md. Avoid nested references (SKILL.md → advanced.md → details.md) as Claude may only partially read deeply nested files.

**Add table of contents to long files**: For reference files over 100 lines, include a table of contents at the top.

**Use Markdown in reference files**: Reference files should also use Markdown structure for readability.

## File Organization

### Filesystem Navigation

Claude navigates your skill directory using bash commands:

- Use forward slashes: `reference/guide.md` (not `reference\guide.md`)
- Name files descriptively: `form_validation_rules.md` (not `doc2.md`)
- Organize by domain: `reference/finance.md`, `reference/sales.md`

### Directory Structure

Typical skill structure:

```
skill-name/
├── SKILL.md (main entry point, Markdown structure)
├── references/ (optional, for progressive disclosure)
│   ├── guide-1.md (Markdown structure)
│   ├── guide-2.md (Markdown structure)
│   └── examples.md (Markdown structure)
└── scripts/ (optional, for utility scripts)
    ├── validate.py
    └── process.py
```

## Anti-Patterns

### Pure XML In Body

❌ Do NOT use pure XML in skill body:

```xml
<objective>
PDF processing with text extraction, form filling, and merging.
</objective>

<quick_start>
Extract text...
</quick_start>

<advanced_features>
Form filling...
</advanced_features>
```

✅ Use Markdown structure:

```markdown
## Objective

PDF processing with text extraction, form filling, and merging.

## Quick Start

Extract text...

## Advanced Features

Form filling...
```

### Vague Descriptions

- ❌ "Helps with documents"
- ✅ "Extract text and tables from PDF files, fill forms, merge documents. Use when working with PDF files or when the user mentions PDFs, forms, or document extraction."

### Inconsistent POV

- ❌ "I can help you process Excel files"
- ✅ "Processes Excel files and generates reports"

### Wrong Naming Convention

- ❌ Directory: `facebook-ads`, Name: `facebook-ads-manager`
- ✅ Directory: `manage-facebook-ads`, Name: `manage-facebook-ads`
- ❌ Directory: `stripe-integration`, Name: `stripe`
- ✅ Directory: `setup-stripe-payments`, Name: `setup-stripe-payments`

### Deeply Nested References

Keep references one level deep from SKILL.md. Claude may only partially read nested files (SKILL.md → advanced.md → details.md).

### Windows Paths

Always use forward slashes: `scripts/helper.py` (not `scripts\helper.py`)

### Missing Required Sections

Every skill must have: `## Objective`, `## Quick Start`, and `## Success Criteria` (or `## When Successful`).

## Validation Checklist

Before finalizing a skill, verify:

- ✅ YAML frontmatter valid (name matches directory, description in third person)
- ✅ Markdown headings used for structure (not pure XML)
- ✅ Required sections present: Objective, Quick Start, Success Criteria
- ✅ Conditional sections appropriate for complexity level
- ✅ Progressive disclosure applied (SKILL.md < 500 lines)
- ✅ Reference files use Markdown structure
- ✅ File paths use forward slashes
- ✅ Descriptive file names
