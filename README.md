# TÂCHES Prompts

Slash commands and prompt systems for Claude Code.

## Quick Start

```bash
# Clone the repo
git clone https://github.com/glittercowboy/taches-cc-prompts.git
cd taches-cc-prompts

# Install meta-prompting
cp meta-prompting/*.md ~/.claude/commands/

# Install todo management
cp todo-management/*.md ~/.claude/commands/

# Install context handoff
cp context-handoff/*.md ~/.claude/commands/
```

All commands work globally. Project-specific data (prompts, todos) lives in each project's working directory.

## Available Prompts

### [Meta-Prompting](./meta-prompting/)

A systematic approach to building complex software by delegating prompt engineering to Claude itself. Instead of telling Claude what to do, you tell Claude what you want, and it figures out how to ask itself to do it.

Perfect for complex refactoring, new features, and multi-step tasks where you want rigorous specifications without manually crafting detailed prompts.

### [Todo Management](./todo-management/)

Capture ideas mid-conversation without losing focus. When you spot a bug, think of a feature, or notice something to refactor - but don't want to derail your current work - `/add-to-todos` captures it with full context. Later, `/check-todos` resumes exactly where you left off.

Perfect for staying focused while building a backlog of improvements, features, and research tasks that won't be forgotten.

### [Context Handoff](./context-handoff/)

Continue work in a fresh context without losing progress. `/whats-next` analyzes the current conversation and creates a structured handoff document with what was completed, what remains, and critical context. Reference it in your next chat to resume seamlessly.

Perfect for when your context is getting full, you need a clean slate, or you're switching between tasks and want to preserve exactly where you left off.

---

More prompts coming soon.

---

**Community Ports:** [OpenCode](https://github.com/stephenschoettler/taches-oc-prompts)

—TÂCHES
