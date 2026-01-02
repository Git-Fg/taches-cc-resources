# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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
