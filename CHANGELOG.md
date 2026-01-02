# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2026-01-02

### AI Context Awareness for Hooks

This release adds AI context awareness to PostToolUse hooks, allowing Claude to understand what happened during formatting and type-checking operations.

### Added

**AI Context via JSON Output**

- `format-on-edit.py` - Now outputs JSON with `additionalContext` informing Claude about:
  - Which formatter was run (ruff, prettier, markdownlint, etc.)
  - Whether formatting was successful
  - Any formatter output/errors
- `type-check-on-edit.py` - Now outputs JSON with `additionalContext` informing Claude about:
  - Type check results (passed/failed)
  - Number of issues found
  - Summary of first few errors when issues exist
  - Type checker timeouts or errors

### Changed

**Hook Output Behavior**

- Hooks now output BOTH:
  - stderr messages for user visibility (shown in verbose mode with ctrl+o)
  - JSON with `hookSpecificOutput.additionalContext` for AI awareness
- Claude agents now automatically know when:
  - A file was formatted successfully
  - Type checking found issues
  - A formatter timed out or wasn't available

### Benefits

**Better AI Awareness:** Claude now knows the results of formatting and type-checking without manual checking

**Automatic Feedback Loop:** When type-checking fails, Claude sees the error summary and can fix issues immediately

**Transparent to Users:** stderr output still provides visibility in verbose mode

### Technical Details

Hooks use the `hookSpecificOutput.additionalContext` field from the [PostToolUse JSON output schema](https://code.claude.com/docs/hooks#posttooluse-decision-control). This context is added to Claude's conversation context, allowing the AI to respond to hook results autonomously.

## [1.1.0] - 2026-01-02

### Security & Code Quality Improvements

This release focuses on security hardening and code quality improvements for all automation hooks, following official Claude Code documentation best practices.

### Fixed

**Critical Bug: Mutable Default Argument**

- Removed `optimize-prompt.py` script (dataclass with `metadata: Dict = None` causing TypeError)
- This script was unused and contained a critical runtime bug

**Security: Path Traversal Protection**

- Added `contains_path_traversal()` function to all hooks
- Detects `..` in path components and URL-encoded variants (`%2e%2e`, `%2E%2E`)
- Logs detection and skips silently (permissive mode maintained)

**Code Quality**

- Fixed redundant string splitting in `type-check-on-edit.py` (was splitting 3 times)
- Standardized type annotations to modern `list[str]` syntax (removed `from typing import List`)
- Added proper error logging with `logging.getLogger(__name__)` and `logger.debug()`
- All exception handlers now log with `exc_info=True` for debugging

### Changed

**All Hooks (4 files updated)**

- `protect-files.py` - Added security checks, improved input validation
- `security-check.py` - Added security checks, improved input validation
- `format-on-edit.py` - Added security checks, modern type annotations
- `type-check-on-edit.py` - Added security checks, fixed string splitting bug

**Build Artifacts**

- Updated `.gitignore` to exclude Python cache files (`__pycache__/`, `*.pyc`, `*.pyo`, `*.pyd`)

### Benefits

**Enhanced Security:** Path traversal detection prevents malicious file access attempts

**Better Debugging:** All errors now logged with full tracebacks (via `--debug` flag)

**Modern Code:** Uses Python 3.9+ built-in generic types instead of `typing` module

**Documentation Compliance:** All hooks now follow [official Claude Code hooks documentation](https://code.claude.com/docs/hooks) best practices

### Migration Notes

No breaking changes. Hooks remain in permissive mode (warn, don't block). Security checks silently skip suspicious paths and log for debugging.

## [1.0.8] - 2026-01-02

### AI Agent Discoverability Improvements

This release implements the A+D Hybrid methodology for writing descriptions that AI agents can autonomously discover and invoke. All commands, skills, and subagents now use strong calling conditions (MUST/ALWAYS/PROACTIVELY USE) with concrete trigger conditions.

### Changed

**Command Descriptions** (16 commands updated)

All commands now follow the pattern: `[CALLING_CONDITION] when [primary_condition]. Secondary: [edge_cases]`

- `/debug` - "MUST USE when investigating bugs, errors, or unexpected behavior requiring systematic root cause analysis. Secondary: recurring issues, intermittent failures, production outages."
- `/review` - "ALWAYS USE after completing code changes to review quality, identify issues, and ensure standards compliance. Secondary: before merging PRs, when refactoring, after implementing features."
- `/brainstorm` - "PROACTIVELY USE for complex problems requiring structured thinking frameworks, multi-perspective analysis, or strategic insight. Secondary: ambiguous challenges, decisions with trade-offs, situations requiring creative solutions."
- `/create-plan` - "MUST USE when planning projects, phases, or tasks that an AI agent will execute."
- `/create-prompt` - "MUST USE when creating prompts that will be executed by Claude or other AI agents."
- `/create-meta-prompt` - "MUST USE when building prompts that produce outputs for other prompts to consume."
- `/create-slash-command` - "MUST USE when creating custom slash commands, standardizing workflows."
- `/create-subagent` - "MUST USE when creating specialized AI agents, setting up delegation tools."
- `/create-agent-skill` - "MUST USE when working with SKILL.md files, authoring new skills."
- `/create-hook` - "MUST USE when working with hooks, setting up event listeners."
- `/run-plan` - "MUST USE when executing PLAN.md files created by the planning system."
- `/run-prompt` - "MUST USE when executing prompts from .prompts/prompts/ as delegated sub-tasks."
- `/whats-next` - "MUST USE when pausing work and needing to resume later in a fresh context."
- `/audit-skill` - "MUST USE when auditing skills for best practices compliance."
- `/audit-subagent` - "MUST USE when auditing subagents for best practices compliance."
- `/audit-slash-command` - "MUST USE when auditing slash commands for YAML compliance."

**Skill Descriptions** (6 skills updated)

- `api-design` - "MUST USE when designing APIs, creating endpoints, defining error handling."
- `architecture-patterns` - "MUST USE when designing systems, choosing patterns, structuring projects."
- `prompt-engineering-patterns` - "MUST USE when creating prompts for AI agents, structuring constraints."
- `create-meta-prompts` - "MUST USE when building prompts that produce outputs for other prompts."
- `create-plans` - "MUST USE when planning projects, phases, or tasks that an AI agent will execute."
- `create-slash-commands` - "MUST USE when creating custom slash commands, standardizing workflows."

**Subagent Descriptions** (1 updated)

- `plan-executor` - "MUST USE when executing PLAN.md files created by the planning system."

### Added

**Documentation**

- `.claude/description-guidelines.md` - Comprehensive guidelines for writing agent-discoverable descriptions including:
  - A+D hybrid methodology explanation
  - Decision tree for writing descriptions
  - Validation checklist
  - Before/after examples
  - Anti-patterns to avoid

### Benefits

**Improved Autonomous Invocation**: AI agents can now autonomously discover and invoke tools with confidence due to unambiguous activation signals.

**Reduced Hesitation**: Strong calling conditions (MUST/ALWAYS/PROACTIVELY USE) override agent hesitation in borderline cases.

**Better Differentiation**: Each tool has mutually exclusive conditions where appropriate, preventing confusion between similar tools.

**Consistency**: All commands, skills, and subagents follow the same description pattern, making the plugin more predictable.

## [1.0.7] - 2026-01-02

### Architecture Refactoring - "Refine & Relay" Pattern

This release implements a systematic architectural improvement across all slash commands and agent interactions. The "Refine & Relay" pattern optimizes the relationship between main model (cheaper, faster) and specialist agents (more capable, expensive).

### Changed

**Slash Commands - Pre-Flight Controller Pattern**

Commands now act as "Pre-Flight Controllers" that gather context, synthesize it into high-fidelity prompts, then delegate to specialist agents. This prevents agents from wasting their first turn asking basic questions.

- `/brainstorm` - Categorizes requests (Technical/Strategic/Analytical) and adds thinking direction before delegating to brainstormer
- `/debug` - Analyzes git status to identify suspect files, creates targeted investigation directive for debugger
- `/review` - Synthesizes diff stats with user focus to create precise briefing for code-reviewer
- `/audit-subagent` - Validates search results and synthesizes directive for subagent-auditor
- `/audit-skill` - Validates pre-flight checks and synthesizes directive for skill-auditor
- `/create-*` commands - Standardized to "dumb relay" pattern for skill delegation

**Agent Input Handling**

All specialist agents now include explicit "Input Handling" or "Initialization" sections to process synthesized context from commands:

- `debugger.md` - Added Input Handling section to process context injection and adapt to detected language
- `code-reviewer.md` - Added Input Processing section to handle specific paths vs vague requests
- `subagent-auditor.md` - Added Initialization section to read files or ask for clarification
- `skill-auditor.md` - Added Initialization section to validate paths and check SKILL.md existence

### Benefits

**Token Efficiency**: Agents receive targeted context in their first prompt (no "what file?" questions)

**Cost Optimization**: Cheaper main model (Haiku/Sonnet) does synthesis, expensive agent (Opus) executes

**Human Alignment**: Main model translates "vague human" to "precise agent directive"

**Speed**: Bash commands (`!`) execute instantly before model thinking, providing immediate context

### Technical Details

The "Refine & Relay" pattern represents the "Middle Way" between:

- **Dumb Relay**: Main model passes raw input without processing
- **Smart Agent**: Agent does all context gathering and synthesis

Instead: Main model gathers context via bash commands, synthesizes into sharp prompt, delegates to agent.

## [1.0.2] - 2025-01-01

### Bug Fixes - Incomplete Migration

This release completes the XML to Markdown migration that was incomplete in v1.0.1. Approximately 158 additional files have been converted from XML to proper Markdown headings.

### Fixed

**Phase 1: Router Skills** (4 files)

- Preserved `<intake>` and `<routing>` XML sections only (complex routing logic)
- Converted all other XML to Markdown headings
- Files: create-plans, create-agent-skills, create-subagents, create-hooks

**Phase 2: Expertise Skills** (Complete)

- Converted all XML tags to Markdown in expertise skills
- Files: macos-apps, iphone-apps (SKILL.md and all workflow files)

**Phase 3: Framework Skills** (Complete)

- Converted all XML framework definitions to Markdown
- Files: All frameworks in strategic-thinking/, prioritization/, problem-analysis/

**Phase 4: Reference Files** (Complete)

- Converted XML reference documentation to Markdown
- Files: All reference files with remaining XML tags

### Changed

**YAML Frontmatter Standardization**

- Standardized frontmatter across all agents (added permissionMode where missing)
- Standardized frontmatter across all commands (consistent structure)
- Verified all skills have proper name and description fields

**Cleanup**

- Removed .DS_Store files from all directories

### Migration Notes

If upgrading from v1.0.1, note that:

- XML structure has been fully converted to Markdown (except `<intake>` and `<routing>` in router skills)
- All functionality remains backwards-compatible
- No breaking changes

## [1.0.1] - 2025-01-01

### Major Feature Release - claude-workflow Integration & Strategic Thinking

This release integrates comprehensive workflow capabilities including operational agents, knowledge domain skills, strategic thinking frameworks, and automation hooks.

### Added

#### Operational Agents (7 new)

- **orchestrator** - Master coordinator for complex multi-step tasks (uses Opus model)
- **code-reviewer** - Expert code review specialist for quality, security, and performance
- **debugger** - Systematic bug investigation and fixing with 6-phase protocol
- **docs-writer** - Technical documentation specialist
- **security-auditor** - Security vulnerability detection specialist
- **refactorer** - Code structure improvements and technical debt reduction
- **test-architect** - Comprehensive test strategy design

#### Knowledge Domain Skills (6 new)

- **project-analysis** - Understand codebase structure and patterns
- **architecture-patterns** - System design guidance (Clean Architecture, Hexagonal, Event-Driven, CQRS)
- **testing-strategy** - Test approaches (unit, integration, E2E)
- **performance-optimization** - Speed optimization and bottleneck identification
- **git-workflow** - Version control best practices and conventional commits
- **api-design** - REST/GraphQL API patterns and best practices

#### Strategic Thinking Skills (3 new)

- **strategic-thinking** - Long-term perspective and big-picture analysis
  - Frameworks: first-principles, inversion, second-order, swot, 10-10-10
  - Use when making strategic decisions, business planning, or major life choices
- **prioritization** - Focus resources on high-impact activities
  - Frameworks: pareto, one-thing, eisenhower-matrix
  - Use when overwhelmed with tasks, need clarity on what to do first
- **problem-analysis** - Deep understanding and root causes
  - Frameworks: 5-whys, opportunity-cost, occams-razor, via-negativa
  - Use when analyzing problems, making constrained choices, or simplifying complexity

#### Brainstormer Agent & Command (1 new)

- **brainstormer agent** - Strategic thinking and decision specialist (opus model)
  - Auto-selects appropriate frameworks based on context
  - Combines multiple frameworks when beneficial
- **/brainstorm command** - Unified entry point for all thinking frameworks
  - Auto-detect mode: Agent analyzes context and suggests frameworks
  - Specific framework mode: Apply named framework directly
  - Skill mode: Apply frameworks from strategic-thinking, prioritization, or problem-analysis

#### Output Mode Commands (4 new)

- **/architect** - System design mode focusing on architecture before code
- **/rapid** - Fast development mode for shipping quickly and iterating
- **/mentor** - Learning mode that explains the "why"
- **/review** - Code review mode with strict quality standards

#### Automation Hooks (3 new)

- **protect-files.py** - Blocks edits to sensitive files (lock files, .env, .git)
- **security-check.py** - Scans for potential secrets before writes
- **format-on-edit.py** - Auto-formats files on edit
  - Python files use `ruff` (instead of black)
  - JS/TS/JSON/CSS/MD use prettier
  - Go uses gofmt
  - Rust uses rustfmt

### Changed

**Agent Refinements**

- **test-architect** - Added "Use PROACTIVELY when..." pattern for proper activation
- **docs-writer** - Added "Use PROACTIVELY when..." pattern and project-analysis skill
- **refactorer** - Added "Use PROACTIVELY when..." pattern
- **debugger** - Added debug-like-expert skill for systematic debugging methodology

**Creation Commands Guidance**

- Added guidance notes to all creation commands explaining when to use each:
  - `/create-plan` - For building projects (hierarchical planning)
  - `/create-meta-prompt` - For Claude→Claude pipelines (staged workflows)
  - `/create-prompt` - For single prompts (simple, one-off)
  - `/create-agent-skill` - For creating new skills
  - `/create-subagent` - For creating specialized agents
  - `/create-slash-command` - For creating commands
  - `/create-hook` - For automation

**Plugin Configuration**

- Updated plugin.json description to reflect expanded capabilities
- Added keywords: orchestration, code-review, security, testing, architecture, debugging
- Updated README with new strategic thinking section

### Removed

**12 consider:* commands** - Consolidated into unified brainstormer:

- Old: `/consider:pareto`, `/consider:first-principles`, etc.
- New: `/brainstorm` with framework-specific or auto-detect modes

### Migration Guide

**Thinking Frameworks:**

- Before: `/consider:pareto` or `/consider:first-principles`
- After:
  - `/brainstorm` - Auto-detect best framework
  - `/brainstorm pareto` - Apply specific framework
  - `/brainstorm strategic` - Use strategic-thinking skill frameworks

### Total Counts

- **Agents**: 3 → 11 (+8 operational)
- **Skills**: 9 → 16 (+7 knowledge and strategic thinking)
- **Commands**: 27 → 20 (-12 consider consolidated, +1 brainstorm, +4 output modes)
- **Hooks**: 0 → 3 (automation system added)

## [1.0.0] - Initial Release

### Features

- Meta-prompting system with staged prompts
- Todo management with context preservation
- 12 thinking model commands (consider/)
- Creation commands for skills, commands, subagents, hooks, meta-prompts, plans
- Quality assurance auditors for skills, commands, and subagents
- Debug-like-expert skill for systematic debugging
- Prompt engineering patterns skill
- Platform expertise (iPhone apps, macOS apps)
