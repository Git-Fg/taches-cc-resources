# Workflow: Get Planning Guidance

## Purpose
Help decide the right planning approach based on project state and goals.

## Process

### Step: Understand Situation
Ask conversationally:
- What's the project/idea?
- How far along are you? (idea, started, mid-project, almost done)
- What feels unclear?

### Step: Recommend Approach
Based on situation:

**Just an idea:**
→ Start with Brief. Capture vision before diving in.

**Know what to build, unclear how:**
→ Create Roadmap. Break into phases first.

**Have phases, need specifics:**
→ Plan Phase. Get Claude-executable tasks.

**Mid-project, lost track:**
→ Audit current state. What exists? What's left?

**Project feels stuck:**
→ Identify the blocker. Is it planning or execution?

### Step: Offer Next Action
```
Recommendation: [approach]

Because: [one sentence why]

Start now?
1. Yes, proceed with [recommended workflow]
2. Different approach
3. More questions first
```

## Decision Tree
```
Is there a brief?
├─ No → Create Brief
└─ Yes → Is there a roadmap?
         ├─ No → Create Roadmap
         └─ Yes → Is current phase planned?
                  ├─ No → Plan Phase
                  └─ Yes → Plan Chunk or Generate Prompts
```

## Common Situations
**"I have an idea but don't know where to start"**
→ Brief first. 5 minutes to capture vision.

**"I know what to build but it feels overwhelming"**
→ Roadmap. Break it into 3-5 phases.

**"I have a phase but tasks are vague"**
→ Plan Phase with Claude-executable specificity.

**"I have a plan but Claude keeps going off track"**
→ Tasks aren't specific enough. Add Files/Action/Verification.

**"Context keeps running out mid-task"**
→ Tasks are too big. Break into smaller chunks + use handoff.

## Success Criteria
Guidance is complete when:
- [ ] User's situation understood
- [ ] Appropriate approach recommended
- [ ] User knows next step
