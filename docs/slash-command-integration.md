# Slash Command Integration Guide & Best Practices

## Overview

This guide provides comprehensive best practices for integrating slash commands with AI agents (Claude Code and compatible systems). It covers when to use commands vs skills vs agents, proper permission configuration, and integration patterns for optimal workflows.

## Table of Contents

1. [Understanding Commands vs Skills vs Agents](#understanding-commands-vs-skills-vs-agents)
2. [Command Structure Best Practices](#command-structure-best-practices)
3. [Agent-Command Integration Patterns](#agent-command-integration-patterns)
4. [Permission Management](#permission-management)
5. [Common Patterns and Anti-Patterns](#common-patterns-and-anti-patterns)
6. [Agent → Command Mapping](#agent--command-mapping)
7. [Security Considerations](#security-considerations)
8. [Testing and Validation](#testing-and-validation)

---

## Understanding Commands vs Skills vs Agents

### Slash Commands

**Use for:** Quick, frequently used prompts that fit in a single file

**Characteristics:**
- Single `.md` file
- Explicit invocation (`/command-name`)
- No automatic discovery
- Minimal overhead
- Project or user scope

**When to create a slash command:**
- You find yourself typing the same prompt repeatedly
- The prompt fits in a single file
- You want explicit control over when it runs
- Quick reminders or templates

**Example:**
```markdown
---
description: Review code for security vulnerabilities. PROACTIVELY USE when handling sensitive data or authentication.
argument-hint: [file-path]
---

Review @/$ARGUMENTS for:
1. SQL injection vulnerabilities
2. XSS vulnerabilities
3. Hardcoded secrets or credentials
4. Insecure authentication/authorization
```

### Skills

**Use for:** Comprehensive capabilities with multiple files and workflows

**Characteristics:**
- Directory with `SKILL.md` + resources
- Automatic discovery based on context
- Complex workflows with validation
- Progressive disclosure (references/, workflows/, scripts/)
- Team sharing via git

**When to create a skill:**
- Multiple workflows or decision paths
- Requires scripts or utilities
- Knowledge organized across multiple files
- Claude should discover automatically
- Team needs standardized guidance

**Example structure:**
```
skills/security-review/
├── SKILL.md (overview and routing)
├── workflows/
│   ├── vulnerability-scan.md
│   └── compliance-check.md
├── references/
│   ├── owasp-top-10.md
│   └── security-patterns.md
└── scripts/
    └── run-security-scan.sh
```

### Agents

**Use for:** Specialized autonomous execution with focused roles and limited tools

**Characteristics:**
- Defined in `agents/` directory
- Invoked via `Task` tool (not by users directly)
- Runs in isolated context
- Focused expertise with specific tools
- Used by other agents or orchestrator

**When to create an agent:**
- Need autonomous execution without user interaction
- Task requires specific tool restrictions
- Complex coordination between multiple specialists
- Want to delegate and forget

---

## Command Structure Best Practices

### Required Frontmatter Fields

Every command should have:

```yaml
---
description: Clear description with strong language (MUST USE/PROACTIVELY USE/CONSULT)
argument-hint: [argument format hint]  # Include if command accepts arguments
allowed-tools: [Tool1, Tool2, Tool3]  # Include to restrict tools
---
```

### Description Guidelines

**Strong Language Hierarchy:**

| Strength | Pattern | Use For |
|----------|---------|---------|
| **MUST USE** | Creation/critical skills, mandatory actions | `/create-plan`, `/commit` |
| **PROACTIVELY USE** | Skills that should be used proactively | `/project-analysis`, `/test-architect` |
| **CONSULT** | Reference/expert guidance | `/api-design`, `/architecture-patterns` |

**Good descriptions:**
```yaml
# MUST USE - For creation/critical
description: Expert guidance for creating AI agent skills. MUST USE when working with SKILL.md files.

# PROACTIVELY USE - For proactive usage
description: Analyzes any project to understand structure, tech stack, and patterns. PROACTIVELY USE when starting work on a new codebase.

# CONSULT - For reference/expert guidance
description: Expert guidance for REST and GraphQL API design including endpoints, error handling, and versioning. CONSULT when designing APIs.
```

**Avoid:**
```yaml
# ❌ Vague
description: Helps with code review
description: Processes data
description: Use when debugging
```

### Argument Hints

Provide clear argument hints for discoverability:

```yaml
---
# Single required argument
argument-hint: [file-path]

# Multiple arguments
argument-hint: [pr-number] [priority] [assignee]

# Optional arguments
argument-hint: [task description, optional]

# No arguments
# (omit argument-hint field entirely)
---
```

### Allowed-Tools

Always restrict tools to minimum required:

```yaml
---
# Security-sensitive: Restrict specific bash commands
allowed-tools: [Bash(git add:*), Bash(git status:*), Bash(git commit:*)]

# Read-only operations
allowed-tools: [Read, Grep, Glob]

# Full access for trusted operations
allowed-tools: [Read, Write, Edit, Bash]

# Skill invocation only
allowed-tools: [Skill(create-agent-skills)]
---
```

**Security guidelines:**
- **Git operations**: Use specific patterns like `Bash(git add:*)` not `Bash(git:*)`
- **File operations**: Restrict to specific patterns when possible
- **Network operations**: Avoid unless explicitly needed
- **Destructive operations**: Use specific command restrictions

---

## Agent-Command Integration Patterns

### Pattern 1: Agent References Commands in Instructions

Agents should reference commands they should use in their workflow or process sections.

**Example - Orchestrator Agent:**
```xml
<orchestration_workflow>
1. Analyze the task requirements

2. If task requires planning:
   - MUST USE /create-plan to generate executable plan
   - MUST USE /run-plan to execute the generated plan

3. If task requires prompt creation:
   - MUST USE /create-prompt for single prompts
   - MUST USE /create-meta-prompt for multi-stage workflows

4. Delegate to specialist agents using Task tool
5. Verify outputs and integrate results
</orchestration_workflow>
```

### Pattern 2: Agent Has Permission to Use SlashCommand Tool

Agents that should invoke commands need `SlashCommand` in their allowed-tools:

```yaml
---
name: orchestrator
description: Master coordinator for complex multi-step tasks. MUST BE USED for open-ended requests like "improve", "refactor", or when implementing features.
tools: Read, Write, Task, SlashCommand
skills: project-analysis, architecture-patterns
---
```

**Important:** Only add `SlashCommand` if the agent actually needs to invoke commands programmatically.

### Pattern 3: Direct Command Invocation in Agent Process

```xml
<process>
1. Read and analyze the current state

2. For code review tasks:
   - Invoke /review command via SlashCommand tool
   - Wait for review completion
   - Process review findings

3. For planning tasks:
   - Invoke /create-plan with task description
   - Execute generated plan using /run-plan

4. Verify and integrate results
</process>
```

### Pattern 4: Conditional Command Usage

```xml
<conditional_workflow>
<when_task_is_complex>
IF task involves multiple modules OR requires architectural planning:
1. MUST USE /create-plan for structured planning
2. MUST USE /run-plan for execution with subagent delegation
ELSE:
3. Execute directly using available specialist agents
</when_task_is_complex>
</conditional_workflow>
```

---

## Permission Management

### Agent Permissions Checklist

When creating or reviewing agents, verify:

#### ✅ Tool Permissions
- [ ] Has `Read` for reading files
- [ ] Has `Write` if creating/modifying files
- [ ] Has `Edit` if making targeted edits
- [ ] Has `Bash` if running commands (consider restrictions)
- [ ] Has `Grep` and `Glob` for codebase analysis
- [ ] Has `Task` for delegating to subagents
- [ ] Has `SlashCommand` if invoking commands
- [ ] Has `AskUserQuestion` if gathering input

#### ✅ Tool Restrictions (Security)
- [ ] Git operations restricted to specific commands
- [ ] File operations scoped to necessary paths
- [ ] No unrestricted `Bash(*)` in production commands
- [ ] No unrestricted `Task` without purpose

#### ✅ Skill References
- [ ] Skills listed are actually used in agent logic
- [ ] Skill names match installed skill files
- [ ] Skill dependencies are documented

### Command Permissions Checklist

#### ✅ Frontmatter Completeness
- [ ] Has `description` with strong language
- [ ] Has `argument-hint` if accepts arguments
- [ ] Has `allowed-tools` if tool restrictions needed
- [ ] No `name` field in frontmatter (only `description`)

#### ✅ Tool Appropriateness
- [ ] Git commands use specific patterns (`Bash(git add:*)`)
- [ ] Read-only commands use `Read, Grep, Glob` only
- [ ] File write commands include `Write`
- [ ] Dangerous operations have explicit restrictions

#### ✅ Security Review
- [ ] No hardcoded credentials
- [ ] Input validation where needed
- [ ] No unrestricted bash with user input
- [ ] Sensitive operations require user confirmation

---

## Common Patterns and Anti-Patterns

### ✅ Good Pattern: Delegation Command

```markdown
---
description: Orchestrates multi-step task by delegating to specialist agents. MUST USE for complex tasks requiring multiple specialists.
argument-hint: [task description]
allowed-tools: [Task, Read, Write]
---

1. Analyze the task: $ARGUMENTS
2. Identify required specialists
3. Delegate to appropriate agents
4. Integrate results
5. Report completion
```

### ❌ Anti-Pattern: Command Without Purpose

```markdown
---
description: Helper command
---

Help with things.
```

**Problems:**
- Vague description ("helper", "things")
- No strong language (MUST USE/PROACTIVELY USE/CONSULT)
- No clear purpose or trigger
- No workflow structure

### ✅ Good Pattern: State-Dependent Command with Context

```markdown
---
description: Debug errors systematically. MUST USE when encountering errors, test failures, or unexpected behavior.
argument-hint: [error description]
allowed-tools: [Read, Edit, Bash, Grep, Glob, Write]
---

<context>
Recent errors: !`grep -r "ERROR\|Error" . --include="*.log" --include="*.txt" 2>/dev/null | head -5 || echo "No recent errors"`
Git status: !`git status --short`
</context>

1. Reproduce the error
2. Identify root cause
3. Fix the issue
4. Verify the fix
5. Document findings
```

### ❌ Anti-Pattern: Over-Permissioned Command

```markdown
---
allowed-tools: [Bash(*)]
---

Execute deployment: $ARGUMENTS
```

**Problems:**
- Unrestricted bash access is dangerous
- Could delete files, stop services, expose data
- No tool restrictions for deployment operations

### ✅ Good Pattern: Restricted Command

```markdown
---
allowed-tools: [Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:origin main:*)]
---

Commit and push changes: $ARGUMENTS
```

---

## Agent → Command Mapping

### Agents and Their Related Commands

| Agent | Commands | Integration Pattern |
|-------|----------|---------------------|
| **orchestrator** | `/create-plan`, `/run-plan`, `/create-prompt`, `/create-meta-prompt` | Agent invokes commands via SlashCommand tool for planning and prompt creation |
| **code-reviewer** | `/review` | Agent's workflow should reference /review for structured review output |
| **debugger** | `/debug` | Agent should use debug skill, command can reference debug workflows |
| **security-auditor** | (none directly, but could use `/security-review`) | Could be enhanced to invoke security review command |
| **test-architect** | (none directly) | Could be enhanced with test planning commands |
| **docs-writer** | (none directly) | Could be enhanced with documentation template commands |

### Documentation Commands

| Command | Purpose | Agent Usage |
|---------|---------|-------------|
| `/create-plan` | Generate hierarchical project plans | Orchestrator MUST USE this for planning |
| `/run-plan` | Execute generated plans | Orchestrator MUST USE this for plan execution |
| `/create-prompt` | Create optimized prompts | Orchestrator uses for single prompts |
| `/create-meta-prompt` | Create meta-prompts for AI→AI pipelines | Orchestrator uses for staged workflows |
| `/create-agent-skill` | Create new skills | Used when skill creation needed |
| `/create-subagent` | Create specialized agents | Orchestrator uses for complex tasks |
| `/create-slash-command` | Create new commands | Used when command creation needed |
| `/audit-skill` | Audit skill for best practices | Independent auditor, could be invoked by quality processes |
| `/audit-subagent` | Audit subagent for best practices | Independent auditor, could be invoked by quality processes |
| `/audit-slash-command` | Audit command for best practices | Independent auditor, could be invoked by quality processes |

### Output Mode Commands

| Command | Purpose | When to Use |
|---------|---------|-------------|
| `/architect` | System design and architecture planning | Before implementation, for design docs, trade-offs |
| `/review` | Strict code review mode | When reviewing code, PRs, or changes |
| `/mentor` | Educational mode explaining concepts | When learning new codebases or technologies |
| `/rapid` | Fast-paced development mode | For prototypes, MVPs, time-sensitive tasks |

---

## Security Considerations

### Command Security Checklist

- [ ] **Input Validation**: Commands that accept user input validate or sanitize it
- [ ] **Tool Restrictions**: Commands have minimal required tool permissions
- [ ] **Git Safety**: Git commands restrict to specific operations (add, status, commit)
- [ ] **File Safety**: File operations scoped to necessary paths
- [ ] **Network Safety**: No unrestricted network operations
- [ ] **Credential Safety**: No hardcoded credentials or API keys
- [ ] **Injection Safety**: User input is properly escaped in command contexts

### Agent Security Checklist

- [ ] **Principle of Least Privilege**: Agents have minimum tools needed
- [ ] **No Unrestricted Delegation**: Task tool not used without specific subagent
- [ ] **File Modification Boundaries**: Write/Edit permissions scoped appropriately
- [ ] **Command Invocation Control**: SlashCommand tool only when needed
- [ ] **User Interaction**: AskUserQuestion only for genuine user input
- [ ] **Bash Restrictions**: Bash commands use specific patterns
- [ ] **Secret Protection**: No secrets in agent descriptions or prompts

### Examples of Secure Configurations

#### Secure Git Command
```yaml
---
allowed-tools: [Bash(git add:*), Bash(git status:*), Bash(git commit:*, Bash(git log:*)]
description: Create git commit safely. MUST USE when committing changes.
---
```

#### Secure File Reading Command
```yaml
---
allowed-tools: [Read, Grep, Glob]
description: Analyze code for security issues. MUST USE when security auditing.
---
```

#### Insecure Command (Do NOT use)
```yaml
---
allowed-tools: [Bash(*)]
description: Execute deployment
---
```

---

## Testing and Validation

### Command Testing Checklist

Test each command to verify:

- [ ] **Frontmatter Valid**: YAML parses correctly
- [ ] **Description Accurate**: Description matches command behavior
- [ ] **Arguments Work**: Arguments are properly integrated
- [ ] **Tool Restrictions Work**: Restricted tools function as intended
- [ ] **No Errors**: Command completes without errors
- [ ] **Output Useful**: Command produces expected results

### Testing Procedure

```bash
# 1. Install command
cp /path/to/command.md ~/.claude/commands/

# 2. Test with Claude Code
claude
# /command-name [arguments]

# 3. Verify behavior
# - Did it do what you expected?
# - Were tools restricted correctly?
# - Was output format correct?

# 4. Test edge cases
# - No arguments when required
# - Invalid arguments
# - Missing referenced files
```

### Agent Testing Checklist

Test each agent to verify:

- [ ] **Permissions Correct**: Agent has required tools
- [ ] **No Extra Tools**: Agent doesn't have unnecessary tools
- [ ] **Skills Available**: Referenced skills exist
- [ ] **Workflow Clear**: Process steps are unambiguous
- [ ] **Constraints Enforced**: Agent respects defined boundaries
- [ ] **Output Quality**: Agent produces expected results

### Integration Testing

Test agent-command integration:

```bash
# 1. Create test command
cat > ~/.claude/commands/test-integration.md << 'EOF'
---
description: Test integration command. MUST USE for testing agent-command integration.
allowed-tools: [Task]
---

Test agent-command integration:
1. Invoke orchestrator agent
2. Verify it can use /create-plan
3. Verify it can use /run-plan
EOF

# 2. Create test agent
cat > ~/.claude/agents/test-orchestrator.md << 'EOF'
---
name: test-orchestrator
description: Test orchestrator for integration testing. MUST USE for testing agent-command integration.
tools: Read, Task, SlashCommand
skills: project-analysis
---

<test_integration>
MUST USE /create-plan when planning
MUST USE /run-plan when executing plans
</test_integration>
EOF

# 3. Test integration
claude
# Invoke test-orchestrator agent via Task tool
# Verify it can access test-integration command
```

---

## Quick Reference

### Command Template

```markdown
---
description: [What it does]. [MUST USE/PROACTIVELY USE/CONSULT] when [trigger condition].
argument-hint: [argument format]
allowed-tools: [Tool1, Tool2, Tool3]
---

<objective>
[Clear statement of purpose]
</objective>

<context>
[Optional: Dynamic context loading with !`command` syntax]
</context>

<process>
1. [Step 1]
2. [Step 2]
3. [Step 3]
</process>

<success_criteria>
- [Success criterion 1]
- [Success criterion 2]
- [Success criterion 3]
</success_criteria>
```

### Agent Template

```yaml
---
name: agent-name
description: [What it does]. MUST BE USED / PROACTIVELY USE when [trigger condition].
tools: [Tool1, Tool2, Tool3]
skills: [skill-name]
---

<role>
You are a [specific role] specializing in [domain].
</role>

<constraints>
- MUST [requirement 1]
- NEVER [restriction 1]
- ALWAYS [requirement 2]
</constraints>

<workflow>
1. [Step 1]
2. [Step 2]
3. [Step 3]
</workflow>

<output_format>
[Expected output structure]
</output_format>

<success_criteria>
- [Criterion 1]
- [Criterion 2]
</success_criteria>
```

### Integration Patterns

| Pattern | Description | Example |
|---------|-------------|---------|
| **Direct Reference** | Agent mentions command in workflow | Orchestrator mentions /create-plan |
| **Tool Invocation** | Agent uses SlashCommand tool | Agent invokes /review via SlashCommand |
| **Conditional Usage** | Agent uses command based on condition | IF complex THEN /create-plan |
| **Delegation Chain** | Agent → Command → Agent → Command | Orchestrator → /run-plan → Subagents |

---

## Conclusion

Following these best practices ensures:

1. **Security**: Proper tool restrictions prevent accidents and vulnerabilities
2. **Clarity**: Strong language and clear descriptions make commands predictable
3. **Maintainability**: Consistent structure makes codebase easier to understand
4. **Integration**: Agents and commands work together seamlessly
5. **Quality**: Testing validates that everything works as intended

For more information, see:
- [Claude Code Official Documentation](https://code.claude.com/docs/slash-commands)
- [Agent Creation Guide](../skills/create-subagents/SKILL.md)
- [Slash Command Creation Guide](../skills/create-slash-commands/SKILL.md)
- [Auditor Best Practices](../agents/slash-command-auditor.md)
