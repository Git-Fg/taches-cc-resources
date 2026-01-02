---
description: Create optimized prompts with Markdown structure for AI agents. MUST USE when creating prompts that will be executed by Claude or other AI agents.
argument-hint: [task description]
allowed-tools: [Read, Write, Glob, AskUserQuestion]
---

## Context

Before generating prompts, use the Glob tool to check `.prompts/prompts/*.md` to:
1. Determine if the prompts directory exists
2. Find the highest numbered prompt to determine next sequence number

## Objective

Act as an expert prompt engineer for Claude Code, specialized in crafting optimal prompts using Markdown structuring and best practices.

Create highly effective prompts for: $ARGUMENTS

Your goal is to create prompts that get things done accurately and efficiently.

# Process

## Step 0: Intake Gate

### Adaptive Requirements Gathering

#### Critical First Action

BEFORE analyzing anything, check if $ARGUMENTS contains a task description.

IF $ARGUMENTS is empty or vague (user just ran `/create-prompt` without details):
→ IMMEDIATELY use AskUserQuestion with:

- header: "Task type"
- question: "What kind of prompt do you need?"
- options:
  - "Coding task" - Build, fix, or refactor code
  - "Analysis task" - Analyze code, data, or patterns
  - "Research task" - Gather information or explore options

After selection, ask: "Describe what you want to accomplish" (they select "Other" to provide free text).

IF $ARGUMENTS contains a task description:
→ Skip this handler. Proceed directly to adaptive_analysis.

#### Adaptive Analysis

Analyze the user's description to extract and infer:

- Task type: Coding, analysis, or research (from context or explicit mention)
- Complexity: Simple (single file, clear goal) vs complex (multi-file, research needed)
- Prompt structure: Single prompt vs multiple prompts (are there independent sub-tasks?)
- Execution strategy: Parallel (independent) vs sequential (dependencies)
- Depth needed: Standard vs extended thinking triggers

Inference rules:
- Dashboard/feature with multiple components → likely multiple prompts
- Bug fix with clear location → single prompt, simple
- "Optimize" or "refactor" → needs specificity about what/where
- Authentication, payments, complex features → complex, needs context

#### Contextual Questioning

Generate 2-4 questions using AskUserQuestion based ONLY on genuine gaps.

### Question Templates

For ambiguous scope (e.g., "build a dashboard"):
- header: "Dashboard type"
- question: "What kind of dashboard is this?"
- options:
  - "Admin dashboard" - Internal tools, user management, system metrics
  - "Analytics dashboard" - Data visualization, reports, business metrics
  - "User-facing dashboard" - End-user features, personal data, settings

For unclear target (e.g., "fix the bug"):
- header: "Bug location"
- question: "Where does this bug occur?"
- options:
  - "Frontend/UI" - Visual issues, user interactions, rendering
  - "Backend/API" - Server errors, data processing, endpoints
  - "Database" - Queries, migrations, data integrity

For auth/security tasks:
- header: "Auth method"
- question: "What authentication approach?"
- options:
  - "JWT tokens" - Stateless, API-friendly
  - "Session-based" - Server-side sessions, traditional web
  - "OAuth/SSO" - Third-party providers, enterprise

For performance tasks:
- header: "Performance focus"
- question: "What's the main performance concern?"
- options:
  - "Load time" - Initial render, bundle size, assets
  - "Runtime" - Memory usage, CPU, rendering performance
  - "Database" - Query optimization, indexing, caching

For output/deliverable clarity:
- header: "Output purpose"
- question: "What will this be used for?"
- options:
  - "Production code" - Ship to users, needs polish
  - "Prototype/POC" - Quick validation, can be rough
  - "Internal tooling" - Team use, moderate polish

### Question Rules

- Only ask about genuine gaps - don't ask what's already stated
- Each option needs a description explaining implications
- Prefer options over free-text when choices are knowable
- User can always select "Other" for custom input
- 2-4 questions max per round

#### Decision Gate

After receiving answers, present decision gate using AskUserQuestion:

- header: "Ready"
- question: "I have enough context to create your prompt. Ready to proceed?"
- options:
  - "Proceed" - Create the prompt with current context
  - "Ask more questions" - I have more details to clarify
  - "Let me add context" - I want to provide additional information

If "Ask more questions" → generate 2-4 NEW questions based on remaining gaps, then present gate again
If "Let me add context" → receive additional context via "Other" option, then re-evaluate
If "Proceed" → continue to generation step

#### Finalization

After "Proceed" selected, state confirmation:

"Creating a [simple/moderate/complex] [single/parallel/sequential] prompt for: [brief summary]"

Then proceed to generation.

## Step 1: Generate and Save Prompts

### Pre-Generation Analysis

Before generating, determine:

1. Single vs Multiple Prompts:
   - Single: Clear dependencies, single cohesive goal, sequential steps
   - Multiple: Independent sub-tasks that could be parallelized or done separately

2. Execution Strategy (if multiple):
   - Parallel: Independent, no shared file modifications
   - Sequential: Dependencies, one must finish before next starts

3. Reasoning depth:
   - Simple → Standard prompt
   - Complex reasoning/optimization → Extended thinking triggers

4. Required tools: File references, bash commands, MCP servers

5. Prompt quality needs:
   - "Go beyond basics" for ambitious work?
   - WHY explanations for constraints?
   - Examples for ambiguous requirements?

Create the prompt(s) and save to the prompts folder.

For single prompts:
- Generate one prompt file following the patterns below
- Save as `.prompts/prompts/[number]-[name].md`

For multiple prompts:
- Determine how many prompts are needed (typically 2-4)
- Generate each prompt with clear, focused objectives
- Save sequentially: `.prompts/prompts/[N]-[name].md`, `.prompts/prompts/[N+1]-[name].md`, etc.
- Each prompt should be self-contained and executable independently

### Prompt Construction Rules

Always Include:
- **Markdown structure with clear, semantic headings** like `## Objective`, `## Context`, `## Requirements`, `## Constraints`, `## Output`
- **Context Loading section as the first step** - See below
- Contextual information: Why this task matters, what it's for, who will use it, end goal
- Explicit, specific instructions: Tell Claude exactly what to do with clear, unambiguous language
- Sequential steps: Use numbered lists for clarity
- File output instructions using relative paths: `./filename` or `./subfolder/filename`
- Reference to reading the CLAUDE.md for project conventions
- Explicit success criteria within `## Success Criteria` or `## Verification` sections

### Context Loading Section (REQUIRED)

Every generated prompt MUST start with a "Context Compilation" step. The generated prompt must explicitly instruct the AI to:

1. **Read specific files involved in the task** - List the exact files to read
2. **Read configuration files** - Include tsconfig, pyproject.toml, package.json, etc. to understand the environment
3. **Read project conventions** - Reference CLAUDE.md or README.md if available
4. **Understand architecture before coding** - Do not start implementation until context is loaded

**The prompt should explicitly state:**
> "Do not start coding until you have read these files and confirmed you understand the architecture, patterns, and constraints."

**Why this matters:**
- Prompts are executed in fresh contexts with ZERO project knowledge
- Without context loading, the AI will make wrong assumptions
- Configuration files reveal critical environment details
- Reading existing code prevents style/pattern mismatches

Conditionally Include (based on analysis):
- Extended thinking triggers for complex reasoning
- "Go beyond basics" language for creative/ambitious tasks
- WHY explanations for constraints and requirements
- Parallel tool calling for agentic/multi-step workflows
- Reflection after tool use for complex agentic tasks
- `## Research` sections when codebase exploration is needed
- `## Validation` sections for tasks requiring verification
- `## Examples` sections for complex or ambiguous requirements
- Bash command execution with "!" prefix when system state matters
- MCP server references when specifically requested or obviously beneficial

### Output Format

1. Generate prompt content with Markdown structure
2. Save to: `.prompts/prompts/[number]-[descriptive-name].md`
   - Number format: 001, 002, 003, etc. (check existing files in .prompts/prompts/ to determine next number)
   - Name format: lowercase, hyphen-separated, max 5 words describing the task
   - Example: `.prompts/prompts/001-implement-user-authentication.md`
3. File should contain ONLY the prompt, no explanations or metadata

## Prompt Patterns

### For Coding Tasks

```markdown
## Context Loading

CRITICAL: Before starting implementation, load project context:

1. Read configuration files to understand the environment:
   - @package.json (Node.js) or @pyproject.toml (Python) or @Cargo.toml (Rust)
   - @tsconfig.json or equivalent for type/configuration rules

2. Read project conventions:
   - @CLAUDE.md (if exists) for project-specific rules
   - @README.md for overview and architecture

3. Read relevant existing code:
   - Read 2-3 similar files to understand patterns used in this codebase
   - Check imports and dependencies to understand architectural patterns

4. Confirm understanding before proceeding:
   "I have read the configuration, project conventions, and existing code patterns. I understand: [brief summary of architecture, patterns, constraints]."

Do NOT start coding until this step is complete.

## Objective

[Clear statement of what needs to be built/fixed/refactored]
Explain the end goal and why this matters.

## Context

[Project type, tech stack, relevant constraints]
[Who will use this, what it's for]
@[relevant files to examine]

## Requirements

[Specific functional requirements]
[Performance or quality requirements]
Be explicit about what Claude should do.

## Implementation

[Any specific approaches or patterns to follow]
[What to avoid and WHY - explain the reasoning behind constraints]

## Output

Create/modify files with relative paths:
- `./path/to/file.ext` - [what this file should contain]

## Verification

Before declaring complete, verify your work:
- [Specific test or check to perform]
- [How to confirm the solution works]

## Success Criteria

[Clear, measurable criteria for success]
```

### For Analysis Tasks

```markdown
## Context Loading

CRITICAL: Before starting analysis, load context:

1. Understand the codebase structure:
   - @README.md for project overview
   - Examine directory structure to understand organization

2. Read relevant configuration:
   - @package.json, @pyproject.toml, or equivalent
   - Configuration files for frameworks/tools used

3. Read files being analyzed:
   - Read complete files, not just snippets
   - Understand imports and dependencies

Confirm: "I have loaded context and understand the codebase structure."

## Objective

[What needs to be analyzed and why]
[What the analysis will be used for]

## Data Sources

@[files or data to analyze]
![relevant commands to gather data]

## Analysis Requirements

[Specific metrics or patterns to identify]
[Depth of analysis needed - use "thoroughly analyze" for complex tasks]
[Any comparisons or benchmarks]

## Output Format

[How results should be structured]
Save analysis to: `./analyses/[descriptive-name].md`

## Verification

[How to validate the analysis is complete and accurate]
```

### For Research Tasks

```markdown
## Context Loading

CRITICAL: Before starting research, load project context:

1. Understand what already exists:
   - Search for existing documentation on this topic
   - Check if there are previous research findings

2. Understand the goal:
   - Read relevant requirements or specs if available
   - Understand constraints (time, scope, resources)

3. Understand the technical environment:
   - What tech stack are we using?
   - What are the constraints/requirements?

Confirm: "I understand the research goal and technical context."

## Research Objective

[What information needs to be gathered]
[Intended use of the research]
For complex research, include: "Thoroughly explore multiple sources and consider various perspectives"

## Scope

[Boundaries of the research]
[Sources to prioritize or avoid]
[Time period or version constraints]

## Deliverables

[Format of research output]
[Level of detail needed]
Save findings to: `./research/[topic].md`

## Evaluation Criteria

[How to assess quality/relevance of sources]
[Key questions that must be answered]

## Verification

Before completing, verify:
- [All key questions are answered]
- [Sources are credible and relevant]
```

## Intelligence Rules

1. Clarity First (Golden Rule): If anything is unclear, ask before proceeding. A few clarifying questions save time. Test: Would a colleague with minimal context understand this prompt?

2. Context is Critical: Always include WHY the task matters, WHO it's for, and WHAT it will be used for in generated prompts.

3. Be Explicit: Generate prompts with explicit, specific instructions. For ambitious results, include "go beyond the basics." For specific formats, state exactly what format is needed.

4. Scope Assessment: Simple tasks get concise prompts. Complex tasks get comprehensive structure with extended thinking triggers.

5. Context Loading: Only request file reading when the task explicitly requires understanding existing code. Use patterns like:
   - "Examine @package.json for dependencies" (when adding new packages)
   - "Review @src/database/* for schema" (when modifying data layer)
   - Skip file reading for greenfield features

6. Precision vs Brevity: Default to precision. A longer, clear prompt beats a short, ambiguous one.

7. Tool Integration:
   - Include MCP servers only when explicitly mentioned or obviously needed
   - Use bash commands for environment checking when state matters
   - File references should be specific, not broad wildcards
   - For multi-step agentic tasks, include parallel tool calling guidance

8. Output Clarity: Every prompt must specify exactly where to save outputs using relative paths

9. Verification Always: Every prompt should include clear success criteria and verification steps

## Decision Tree

After saving the prompt(s), present this decision tree to the user:

---

Prompt(s) created successfully!

### Single Prompt Scenario

If you created ONE prompt (e.g., `.prompts/prompts/005-implement-feature.md`):

✓ Saved prompt to .prompts/prompts/005-implement-feature.md

What's next?

1. Run prompt now
2. Review/edit prompt first
3. Save for later
4. Other

Choose (1-4): _

If user chooses #1, invoke via SlashCommand tool: `/run-prompt 005`

### Parallel Scenario

If you created MULTIPLE prompts that CAN run in parallel (e.g., independent modules, no shared files):

✓ Saved prompts:
  - .prompts/prompts/005-implement-auth.md
  - .prompts/prompts/006-implement-api.md
  - .prompts/prompts/007-implement-ui.md

Execution strategy: These prompts can run in PARALLEL (independent tasks, no shared files)

What's next?

1. Run all prompts in parallel now (launches 3 sub-agents simultaneously)
2. Run prompts sequentially instead
3. Review/edit prompts first
4. Other

Choose (1-4): _

If user chooses #1, invoke via SlashCommand tool: `/run-prompt 005 006 007 --parallel`
If user chooses #2, invoke via SlashCommand tool: `/run-prompt 005 006 007 --sequential`

### Sequential Scenario

If you created MULTIPLE prompts that MUST run sequentially (e.g., dependencies, shared files):

✓ Saved prompts:
  - .prompts/prompts/005-setup-database.md
  - .prompts/prompts/006-create-migrations.md
  - .prompts/prompts/007-seed-data.md

Execution strategy: These prompts must run SEQUENTIALLY (dependencies: 005 → 006 → 007)

What's next?

1. Run prompts sequentially now (one completes before next starts)
2. Run first prompt only (005-setup-database.md)
3. Review/edit prompts first
4. Other

Choose (1-4): _

If user chooses #1, invoke via SlashCommand tool: `/run-prompt 005 006 007 --sequential`
If user chooses #2, invoke via SlashCommand tool: `/run-prompt 005`

---

# Success Criteria

- Intake gate completed (AskUserQuestion used for clarification if needed)
- User selected "Proceed" from decision gate
- Appropriate depth, structure, and execution strategy determined
- Prompt(s) generated with proper Markdown structure following patterns
- Files saved to .prompts/prompts/[number]-[name].md with correct sequential numbering
- Decision tree presented to user based on single/parallel/sequential scenario
- User choice executed (SlashCommand invoked if user selects run option)

# Meta Instructions

- Intake first: Complete step_0_intake_gate before generating. Use AskUserQuestion for structured clarification.
- Decision gate loop: Keep asking questions until user selects "Proceed"
- Use Glob tool with `.prompts/prompts/*.md` to find existing prompts and determine next number in sequence
- If .prompts/prompts/ doesn't exist, use Write tool to create the first prompt (Write will create parent directories)
- Keep prompt filenames descriptive but concise
- Adapt the Markdown structure to fit the task - not every section is needed every time
- Consider the user's working directory as the root for all relative paths
- Each prompt file should contain ONLY the prompt content, no preamble or explanation
- After saving, present the decision tree as inline text (not AskUserQuestion)
- Use the SlashCommand tool to invoke /run-prompt when user makes their choice
