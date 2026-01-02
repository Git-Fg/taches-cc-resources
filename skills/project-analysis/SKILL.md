---
name: project-analysis
description: Analyzes any project to understand structure, tech stack, patterns, and conventions. PROACTIVELY USE when starting work on a new codebase, onboarding, or asked "how does this project work?" or "what's the architecture?"
---

# Objective

Analyzes any project to understand structure, tech stack, patterns, and conventions.

# Process

When analyzing a project, systematically gather and present information in this order:

## Step 1: Quick Overview

```bash
# Check for common project markers
ls -la
cat README.md 2>/dev/null | head -50
```

## Step 2: Tech Stack Detection

### Package Managers

- package.json to Node.js/JavaScript/TypeScript
- requirements.txt / pyproject.toml / setup.py to Python
- go.mod to Go
- Cargo.toml to Rust
- pom.xml / build.gradle to Java
- Gemfile to Ruby

### Frameworks

From dependencies, detect:
- React, Vue, Angular, Next.js, Nuxt
- Express, FastAPI, Django, Flask, Rails
- Spring Boot, Gin, Echo

### Infrastructure

- Dockerfile, docker-compose.yml to Containerized
- kubernetes/, k8s/ to Kubernetes
- terraform/, .tf files to IaC
- serverless.yml to Serverless Framework
- .github/workflows/ to GitHub Actions

## Step 3: Structure Analysis

Present as a tree with annotations:

```
project/
├── src/              # Source code
│   ├── components/   # UI components (React/Vue)
│   ├── services/     # Business logic
│   ├── models/       # Data models
│   └── utils/        # Shared utilities
├── tests/            # Test files
├── docs/             # Documentation
└── config/           # Configuration
```

## Step 4: Patterns

Look for and report:
- Architecture: Monolith, Microservices, Serverless, Monorepo
- API Style: REST, GraphQL, gRPC, tRPC
- State Management: Redux, Zustand, MobX, Context
- Database: SQL, NoSQL, ORM used
- Authentication: JWT, OAuth, Sessions
- Testing: Jest, Pytest, Go test, etc.

## Step 5: Workflow

Check for:
- .eslintrc, .prettierrc to Linting/Formatting
- .husky/ to Git hooks
- Makefile to Build commands
- scripts/ in package.json to NPM scripts

## Step 6: Output

```markdown
# Project: [Name]

## Overview
[1-2 sentence description]

## Tech Stack
| Category | Technology |
|----------|------------|
| Language | TypeScript |
| Framework | Next.js 14 |
| Database | PostgreSQL |
| ...      | ...        |

## Architecture
[Description with simple ASCII diagram if helpful]

## Key Directories
- `src/` - [purpose]
- `lib/` - [purpose]

## Entry Points
- Main: `src/index.ts`
- API: `src/api/`
- Tests: `npm test`

## Conventions
- [Naming conventions]
- [File organization patterns]
- [Code style preferences]

## Quick Commands
| Action | Command |
|--------|---------|
| Install | `npm install` |
| Dev | `npm run dev` |
| Test | `npm test` |
| Build | `npm run build` |
```
