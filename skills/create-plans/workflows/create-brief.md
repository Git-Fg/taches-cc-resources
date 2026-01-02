# Workflow: Create Brief

## Required Reading
**Read these files NOW:**
1. templates/brief.md

## Purpose
Create a project vision document that captures what we're building and why.
This is the ONLY human-focused document - everything else is for Claude.

## Process

### Step: Gather Vision
Ask the user (conversationally, not AskUserQuestion):

1. **What are we building?** (one sentence)
2. **Why does this need to exist?** (the problem it solves)
3. **What does success look like?** (how we know it worked)
4. **Any constraints?** (tech stack, timeline, budget, etc.)

Keep it conversational. Don't ask all at once - let it flow naturally.

### Step: Decision Gate
After gathering context:

Use AskUserQuestion:
- header: "Ready"
- question: "Ready to create the brief, or would you like me to ask more questions?"
- options:
  - "Create brief" - I have enough context
  - "Ask more questions" - There are details to clarify
  - "Let me add context" - I want to provide more information

Loop until "Create brief" selected.

### Step: Create Structure
Create the planning directory:

```bash
mkdir -p .planning
```

### Step: Write Brief
Use the template from `templates/brief.md`.

Write to `.prompts/planning/BRIEF.md` with:
- Project name
- One-line description
- Problem statement (why this exists)
- Success criteria (measurable outcomes)
- Constraints (if any)
- Out of scope (what we're NOT building)

**Keep it SHORT.** Under 50 lines. This is a reference, not a novel.

### Step: Offer Next
After creating brief, present options:

```
Brief created: .prompts/planning/BRIEF.md

NOTE: Brief is NOT committed yet. It will be committed with the roadmap as project initialization.

What's next?
1. Create roadmap now (recommended - commits brief + roadmap together)
2. Review/edit brief
3. Done for now (brief will remain uncommitted)
```

## Anti Patterns
- Don't write a business plan
- Don't include market analysis
- Don't add stakeholder sections
- Don't create executive summaries
- Don't add timelines (that's roadmap's job)

Keep it focused: What, Why, Success, Constraints.

## Success Criteria
Brief is complete when:
- [ ] `.prompts/planning/BRIEF.md` exists
- [ ] Contains: name, description, problem, success criteria
- [ ] Under 50 lines
- [ ] User knows what's next
