## Overview
Prompt patterns for execution tasks that produce artifacts (code, documents, designs, etc.).

## Prompt Template
```xml
### Objective
{Clear statement of what to build/create/fix}

Purpose: {Why this matters, what it enables}
Output: {What artifact(s) will be produced}

### Context
{Referenced research/plan files if chained}
@{topic}-research.md
@{topic}-plan.md

{Project context}
@relevant-files

### Requirements
{Specific functional requirements}
{Quality requirements}
{Constraints and boundaries}

### Implementation
{Specific approaches or patterns to follow}
{What to avoid and WHY}
{Integration points}

### Output
Create/modify files:
- `./path/to/file.ext` - {description}

{For complex outputs, specify structure}

### Verification
Before declaring complete:
- {Specific test or check}
- {How to confirm it works}
- {Edge cases to verify}

### Summary Requirements
Create `.prompts/{num}-{topic}-{purpose}/SUMMARY.md`

Load template: [summary-template.md](summary-template.md)

For Do prompts, include Files Created section with paths and descriptions. Emphasize what was implemented and test status. Next step typically: Run tests or execute next phase.

### Success Criteria
{Clear, measurable criteria}
- {Criterion 1}
- {Criterion 2}
- SUMMARY.md created with files list and next step
```

## Key Principles

### Reference Chain Artifacts
If research or plan exists, always reference them:
```xml
#### Context
Research findings: @.prompts/001-auth-research/auth-research.md
Implementation plan: @.prompts/002-auth-plan/auth-plan.md
```

### Explicit Output Location
Every artifact needs a clear path:
```xml
#### Output
Create files in ./src/auth/:
- `./src/auth/middleware.ts` - JWT validation middleware
- `./src/auth/types.ts` - Auth type definitions
- `./src/auth/utils.ts` - Helper functions
```

### Verification Matching
Include verification that matches the task:
- Code: run tests, type check, lint
- Documents: check structure, validate links
- Designs: review against requirements


## Complexity Variations

### Simple Do
Single artifact example:
```xml
#### Objective
Create a utility function that validates email addresses.

#### Requirements
- Support standard email format
- Return boolean
- Handle edge cases (empty, null)

#### Output
Create: `./src/utils/validate-email.ts`

#### Verification
Test with: valid emails, invalid formats, edge cases
```

### Complex Do
Multiple artifacts with dependencies:
```xml
#### Objective
Implement user authentication system with JWT tokens.

Purpose: Enable secure user sessions for the application
Output: Auth middleware, routes, types, and tests

#### Context
Research: @.prompts/001-auth-research/auth-research.md
Plan: @.prompts/002-auth-plan/auth-plan.md
Existing user model: @src/models/user.ts

#### Requirements
- JWT access tokens (15min expiry)
- Refresh token rotation
- Secure httpOnly cookies
- Rate limiting on auth endpoints

#### Implementation
Follow patterns from auth-research.md:
- Use jose library for JWT (not jsonwebtoken - see research)
- Implement refresh rotation per OWASP guidelines
- Store refresh tokens hashed in database

Avoid:
- Storing tokens in localStorage (XSS vulnerable)
- Long-lived access tokens (security risk)

#### Output
Create in ./src/auth/:
- `middleware.ts` - JWT validation, refresh logic
- `routes.ts` - Login, logout, refresh endpoints
- `types.ts` - Token payloads, auth types
- `utils.ts` - Token generation, hashing

Create in ./src/auth/__tests__/:
- `auth.test.ts` - Unit tests for all auth functions

#### Verification
1. Run test suite: `npm test src/auth`
2. Type check: `npx tsc --noEmit`
3. Manual test: login flow, token refresh, logout
4. Security check: verify httpOnly cookies, token expiry

#### Success Criteria
- All tests passing
- No type errors
- Login/logout/refresh flow works
- Tokens properly secured
- Follows patterns from research
```


## Non Code Examples

### Document Creation
```xml
#### Objective
Create API documentation for the authentication endpoints.

Purpose: Enable frontend team to integrate auth
Output: OpenAPI spec + markdown guide

#### Context
Implementation: @src/auth/routes.ts
Types: @src/auth/types.ts

#### Requirements
- OpenAPI 3.0 spec
- Request/response examples
- Error codes and handling
- Authentication flow diagram

#### Output
- `./docs/api/auth.yaml` - OpenAPI spec
- `./docs/guides/authentication.md` - Integration guide

#### Verification
- Validate OpenAPI spec: `npx @redocly/cli lint docs/api/auth.yaml`
- Check all endpoints documented
- Verify examples match actual implementation
```

### Design Architecture
```xml
#### Objective
Design database schema for multi-tenant SaaS application.

Purpose: Support customer isolation and scaling
Output: Schema diagram + migration files

#### Context
Research: @.prompts/001-multitenancy-research/multitenancy-research.md
Current schema: @prisma/schema.prisma

#### Requirements
- Row-level security per tenant
- Shared infrastructure model
- Support for tenant-specific customization
- Audit logging

#### Output
- `./docs/architecture/tenant-schema.md` - Schema design doc
- `./prisma/migrations/add-tenancy/` - Migration files

#### Verification
- Migration runs without errors
- RLS policies correctly isolate data
- Performance acceptable with 1000 tenants
```

