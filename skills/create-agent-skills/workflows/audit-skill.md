# Workflow: Audit a Skill

## Required Reading
**Read these reference files NOW:**
1. references/skill-structure.md
2. references/core-principles.md

## Process
## Step 1: List Available Skills

**DO NOT use AskUserQuestion** - there may be many skills.

Enumerate skills in chat as numbered list:
```bash
ls ~/.claude/skills/
```

Present as:
```
Available skills:
1. create-agent-skills
2. build-macos-apps
3. manage-stripe
...
```

Ask: "Which skill would you like to audit? (enter number or name)"

## Step 2: Read the Skill

After user selects, read the full skill structure:
```bash
# Read main file
cat ~/.claude/skills/{skill-name}/SKILL.md

# Check for workflows and references
ls ~/.claude/skills/{skill-name}/
ls ~/.claude/skills/{skill-name}/workflows/ 2>/dev/null
ls ~/.claude/skills/{skill-name}/references/ 2>/dev/null
```

## Step 3: Run Audit Checklist

Evaluate against each criterion:

### YAML Frontmatter
- [ ] Has `name:` field (lowercase-with-hyphens)
- [ ] Name matches directory name
- [ ] Has `description:` field
- [ ] Description says what it does AND when to use it
- [ ] Description is third person with strong language (MUST USE/PROACTIVELY USE/CONSULT)

### Structure
- [ ] SKILL.md under 500 lines
- [ ] Pure XML structure (no markdown headings # in body)
- [ ] All XML tags properly closed
- [ ] Has required tags: objective OR essential_principles
- [ ] Has success_criteria

### Router Pattern (if complex skill)
- [ ] Essential principles inline in SKILL.md (not in separate file)
- [ ] Has intake question
- [ ] Has routing table
- [ ] All referenced workflow files exist
- [ ] All referenced reference files exist

### Workflows (if present)
- [ ] Each has required_reading section
- [ ] Each has process section
- [ ] Each has success_criteria section
- [ ] Required reading references exist

### Content Quality
- [ ] Principles are actionable (not vague platitudes)
- [ ] Steps are specific (not "do the thing")
- [ ] Success criteria are verifiable
- [ ] No redundant content across files

## Step 4: Generate Report

Present findings as:

```
## Audit Report: {skill-name}

### ✅ Passing
- [list passing items]

### ⚠️ Issues Found
1. **[Issue name]**: [Description]
   → Fix: [Specific action]

2. **[Issue name]**: [Description]
   → Fix: [Specific action]

### 📊 Score: X/Y criteria passing
```

## Step 5: Offer Fixes

If issues found, ask:
"Would you like me to fix these issues?"

Options:
1. **Fix all** - Apply all recommended fixes
2. **Fix one by one** - Review each fix before applying
3. **Just the report** - No changes needed

If fixing:
- Make each change
- Verify file validity after each change
- Report what was fixed

## Audit Anti Patterns
## Common Anti-Patterns to Flag

**Skippable principles**: Essential principles in separate file instead of inline
**Monolithic skill**: Single file over 500 lines
**Mixed concerns**: Procedures and knowledge in same file
**Vague steps**: "Handle the error appropriately"
**Untestable criteria**: "User is satisfied"
**Markdown headings in body**: Using # instead of XML tags
**Missing routing**: Complex skill without intake/routing
**Broken references**: Files mentioned but don't exist
**Redundant content**: Same information in multiple places

## Success Criteria
Audit is complete when:
- [ ] Skill fully read and analyzed
- [ ] All checklist items evaluated
- [ ] Report presented to user
- [ ] Fixes applied (if requested)
- [ ] User has clear picture of skill health
