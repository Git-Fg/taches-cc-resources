## Overview
Prompt patterns for gathering information that will be consumed by planning or implementation prompts.

Includes quality controls, verification mechanisms, and streaming writes to prevent research gaps and token limit failures.

## Prompt Template
```xml
### Session Initialization
Before beginning research, verify today's date:
!`date +%Y-%m-%d`

Use this date when searching for "current" or "latest" information.
Example: If today is 2025-11-22, search for "2025" not "2024".

### Research Objective
Research {topic} to inform {subsequent use}.

Purpose: {What decision/implementation this enables}
Scope: {Boundaries of the research}
Output: {topic}-research.md with structured findings

### Research Scope
#### Include
{What to investigate}
{Specific questions to answer}

#### Exclude
{What's out of scope}
{What to defer to later research}

#### Sources
{Priority sources with exact URLs for WebFetch}
Official documentation:
- https://example.com/official-docs
- https://example.com/api-reference

Search queries for WebSearch:
- "{topic} best practices {current_year}"
- "{topic} latest version"

{Time constraints: prefer current sources - check today's date first}

### Verification Checklist
{If researching configuration/architecture with known components:}
□ Verify ALL known configuration/implementation options (enumerate below):
  □ Option/Scope 1: {description}
  □ Option/Scope 2: {description}
  □ Option/Scope 3: {description}
□ Document exact file locations/URLs for each option
□ Verify precedence/hierarchy rules if applicable
□ Confirm syntax and examples from official sources
□ Check for recent updates or changes to documentation

{For all research:}
□ Verify negative claims ("X is not possible") with official docs
□ Confirm all primary claims have authoritative sources
□ Check both current docs AND recent updates/changelogs
□ Test multiple search queries to avoid missing information
□ Check for environment/tool-specific variations

### Research Quality Assurance
Before completing research, perform these checks:

#### Completeness Check
- [ ] All enumerated options/components documented with evidence
- [ ] Each access method/approach evaluated against ALL requirements
- [ ] Official documentation cited for critical claims
- [ ] Contradictory information resolved or flagged

#### Source Verification
- [ ] Primary claims backed by official/authoritative sources
- [ ] Version numbers and dates included where relevant
- [ ] Actual URLs provided (not just "search for X")
- [ ] Distinguish verified facts from assumptions

#### Blind Spots Review
Ask yourself: "What might I have missed?"
- [ ] Are there configuration/implementation options I didn't investigate?
- [ ] Did I check for multiple environments/contexts (e.g., Desktop vs Code)?
- [ ] Did I verify claims that seem definitive ("cannot", "only", "must")?
- [ ] Did I look for recent changes or updates to documentation?

#### Critical Claims Audit
For any statement like "X is not possible" or "Y is the only way":
- [ ] Is this verified by official documentation?
- [ ] Have I checked for recent updates that might change this?
- [ ] Are there alternative approaches I haven't considered?

### Output Structure
Save to: `.prompts/{num}-{topic}-research/{topic}-research.md`

Structure findings using this XML format:

```xml
#### Research
  ##### Summary
    {2-3 paragraph executive summary of key findings}

  ##### Findings
    <finding category="{category}">
      <title>{Finding title}</title>
      <detail>{Detailed explanation}</detail>
      <source>{Where this came from}</source>
      <relevance>{Why this matters for the goal}</relevance>
    <!-- Additional findings -->

  ##### Recommendations
    <recommendation priority="high">
      <action>{What to do}</action>
      <rationale>{Why}</rationale>
    <!-- Additional recommendations -->

  ##### Code Examples
    {Relevant code patterns, snippets, configurations}

  ##### Metadata
    <confidence level="{high|medium|low}">
      {Why this confidence level}
    ###### Dependencies
      {What's needed to act on this research}
    ###### Open Questions
      {What couldn't be determined}
    ###### Assumptions
      {What was assumed}

    <!-- ENHANCED: Research Quality Report -->
    ###### Quality Report
      ####### Sources Consulted
        {List URLs of official documentation and primary sources}
      ####### Claims Verified
        {Key findings verified with official sources}
      ####### Claims Assumed
        {Findings based on inference or incomplete information}
      ####### Contradictions Encountered
        {Any conflicting information found and how resolved}
      ####### Confidence By Finding
        {For critical findings, individual confidence levels}
        - Finding 1: High (official docs + multiple sources)
        - Finding 2: Medium (single source, unclear if current)
        - Finding 3: Low (inferred, requires hands-on verification)
```

### Pre Submission Checklist
Before submitting your research report, confirm:

**Scope Coverage**
- [ ] All enumerated options/approaches investigated
- [ ] Each component from verification checklist documented or marked "not found"
- [ ] Official documentation cited for all critical claims

**Claim Verification**
- [ ] Each "not possible" or "only way" claim verified with official docs
- [ ] URLs to official documentation included for key findings
- [ ] Version numbers and dates specified where relevant

**Quality Controls**
- [ ] Blind spots review completed ("What did I miss?")
- [ ] Quality report section filled out honestly
- [ ] Confidence levels assigned with justification
- [ ] Assumptions clearly distinguished from verified facts

**Output Completeness**
- [ ] All required XML sections present
- [ ] SUMMARY.md created with substantive one-liner
- [ ] Sources consulted listed with URLs
- [ ] Next steps clearly identified
```

### Incremental Output
**CRITICAL: Write findings incrementally to prevent token limit failures**

Instead of generating the full research in memory and writing at the end:
1. Create the output file with initial structure
2. Write each finding as you discover it
3. Append code examples as you find them
4. Update metadata at the end

This ensures:
- Zero lost work if token limit is hit
- File contains all findings up to that point
- No estimation heuristics needed
- Works for any research size

#### Workflow
Step 1 - Initialize structure:
```bash
# Create file with skeleton
Write: .prompts/{num}-{topic}-research/{topic}-research.md
Content: Basic XML structure with empty sections
```

Step 2 - Append findings incrementally:
```bash
# After researching authentication libraries
Edit: Append <finding> to <findings> section

# After discovering rate limits
Edit: Append another <finding> to <findings> section
```

Step 3 - Add code examples as discovered:
```bash
# Found jose example
Edit: Append to <code_examples> section
```

Step 4 - Finalize metadata:
```bash
# After completing research
Edit: Update <metadata> section with confidence, dependencies, etc.
```

#### Example Prompt Instruction
```xml
##### Output Requirements
Write findings incrementally to {topic}-research.md as you discover them:

1. Create the file with this initial structure:
   ```xml
   ###### Research
     <summary>[Will complete at end]</summary>
     <findings></findings>
     <recommendations></recommendations>
     <code_examples></code_examples>
     <metadata></metadata>
   ```

2. As you research each aspect, immediately append findings:
   - Research JWT libraries → Write finding
   - Discover security pattern → Write finding
   - Find code example → Append to code_examples

3. After all research complete:
   - Write summary (synthesize all findings)
   - Write recommendations (based on findings)
   - Write metadata (confidence, dependencies, etc.)

This incremental approach ensures all work is saved even if execution
hits token limits. Never generate the full output in memory first.
```

#### Benefits
**vs. Pre-execution estimation:**
- No estimation errors (you don't predict, you just write)
- No artificial modularization (agent decides natural breakpoints)
- No lost work (everything written is saved)

**vs. Single end-of-execution write:**
- Survives token limit failures (partial progress saved)
- Lower memory usage (write as you go)
- Natural checkpoint recovery (can continue from last finding)

### Summary Requirements
Create `.prompts/{num}-{topic}-research/SUMMARY.md`

Load template: [summary-template.md](summary-template.md)

For research, emphasize key recommendation and decision readiness. Next step typically: Create plan.

### Success Criteria
- All scope questions answered
- All verification checklist items completed
- Sources are current and authoritative
- Findings are actionable
- Metadata captures gaps honestly
- Quality report distinguishes verified from assumed
- SUMMARY.md created with substantive one-liner
- Ready for planning/implementation to consume
```

## Key Principles

### Structure For Consumption
The next Claude needs to quickly extract relevant information:
```xml
<finding category="authentication">
  <title>JWT vs Session Tokens</title>
  #### Detail
    JWTs are preferred for stateless APIs. Sessions better for
    traditional web apps with server-side rendering.
  <source>OWASP Authentication Cheatsheet 2024</source>
  #### Relevance
    Our API-first architecture points to JWT approach.
```

### Include Code Examples
The implementation prompt needs patterns to follow:
```xml
#### Code Examples
<example name="jwt-verification">
```typescript
import { jwtVerify } from 'jose';

const { payload } = await jwtVerify(
  token,
  new TextEncoder().encode(secret),
  { algorithms: ['HS256'] }
);
```
Source: jose library documentation
```

### Explicit Confidence
Help the next Claude know what to trust:
```xml
#### Metadata
  <confidence level="medium">
    API documentation is comprehensive but lacks real-world
    performance benchmarks. Rate limits are documented but
    actual behavior may differ under load.

  ##### Quality Report
    ###### Confidence By Finding
      - JWT library comparison: High (npm stats + security audits + active maintenance verified)
      - Performance benchmarks: Low (no official data, community reports vary)
      - Rate limits: Medium (documented but not tested)
```

### Enumerate Known Possibilities
When researching systems with known components, enumerate them explicitly:
```xml
#### Verification Checklist
**CRITICAL**: Verify ALL configuration scopes:
□ User scope - Global configuration
□ Project scope - Project-level configuration files
□ Local scope - Project-specific user overrides
□ Environment scope - Environment variable based
```

This forces systematic coverage and prevents omissions.


## Research Types

### Technology Research
For understanding tools, libraries, APIs:

```xml
#### Research Objective
Research JWT authentication libraries for Node.js.

Purpose: Select library for auth implementation
Scope: Security, performance, maintenance status
Output: jwt-research.md

#### Research Scope
##### Include
- Available libraries (jose, jsonwebtoken, etc.)
- Security track record
- Bundle size and performance
- TypeScript support
- Active maintenance
- Community adoption

##### Exclude
- Implementation details (for planning phase)
- Specific code architecture (for implementation)

##### Sources
Official documentation (use WebFetch):
- https://github.com/panva/jose
- https://github.com/auth0/node-jsonwebtoken

Additional sources (use WebSearch):
- "JWT library comparison {current_year}"
- "jose vs jsonwebtoken security {current_year}"
- npm download stats
- GitHub issues/security advisories

#### Verification Checklist
□ Verify all major JWT libraries (jose, jsonwebtoken, passport-jwt)
□ Check npm download trends for adoption metrics
□ Review GitHub security advisories for each library
□ Confirm TypeScript support with examples
□ Document bundle sizes from bundlephobia or similar
```

### Best Practices Research
For understanding patterns and standards:

```xml
#### Research Objective
Research authentication security best practices.

Purpose: Inform secure auth implementation
Scope: Current standards, common vulnerabilities, mitigations
Output: auth-security-research.md

#### Research Scope
##### Include
- OWASP authentication guidelines
- Token storage best practices
- Common vulnerabilities (XSS, CSRF)
- Secure cookie configuration
- Password hashing standards

##### Sources
Official sources (use WebFetch):
- https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html
- https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html

Search sources (use WebSearch):
- "OWASP authentication {current_year}"
- "secure token storage best practices {current_year}"

#### Verification Checklist
□ Verify OWASP top 10 authentication vulnerabilities
□ Check latest OWASP cheatsheet publication date
□ Confirm recommended hash algorithms (bcrypt, scrypt, Argon2)
□ Document secure cookie flags (httpOnly, secure, sameSite)
```

### Api Service Research
For understanding external services:

```xml
#### Research Objective
Research Stripe API for payment integration.

Purpose: Plan payment implementation
Scope: Endpoints, authentication, webhooks, testing
Output: stripe-research.md

#### Research Scope
##### Include
- API structure and versioning
- Authentication methods
- Key endpoints for our use case
- Webhook events and handling
- Testing and sandbox environment
- Error handling patterns
- SDK availability

##### Exclude
- Pricing details
- Account setup process

##### Sources
Official sources (use WebFetch):
- https://stripe.com/docs/api
- https://stripe.com/docs/webhooks
- https://stripe.com/docs/testing

Context7 MCP:
- Use mcp__context7__resolve-library-id for Stripe
- Use mcp__context7__get-library-docs for current patterns

#### Verification Checklist
□ Verify current API version and deprecation timeline
□ Check webhook event types for our use case
□ Confirm sandbox environment capabilities
□ Document rate limits from official docs
□ Verify SDK availability for our stack
```

### Comparison Research
For evaluating options:

```xml
#### Research Objective
Research database options for multi-tenant SaaS.

Purpose: Inform database selection decision
Scope: PostgreSQL, MongoDB, DynamoDB for our use case
Output: database-research.md

#### Research Scope
##### Include
For each option:
- Multi-tenancy support patterns
- Scaling characteristics
- Cost model
- Operational complexity
- Team expertise requirements

##### Evaluation Criteria
- Data isolation requirements
- Expected query patterns
- Scale projections
- Team familiarity

#### Verification Checklist
□ Verify all candidate databases (PostgreSQL, MongoDB, DynamoDB)
□ Document multi-tenancy patterns for each with official sources
□ Compare scaling characteristics with authoritative benchmarks
□ Check pricing calculators for cost model verification
□ Assess team expertise honestly (survey if needed)
```


## Metadata Guidelines
Load: [metadata-guidelines.md](metadata-guidelines.md)

**Enhanced guidance**:
- Use <quality_report> to distinguish verified facts from assumptions
- Assign confidence levels to individual findings when they vary
- List all sources consulted with URLs for verification
- Document contradictions encountered and how resolved
- Be honest about limitations and gaps in research

## Tool Usage

### Context7 Mcp
For library documentation:
```
Use mcp__context7__resolve-library-id to find library
Then mcp__context7__get-library-docs for current patterns
```

### Web Search
For recent articles and updates:
```
Search: "{topic} best practices {current_year}"
Search: "{library} security vulnerabilities {current_year}"
Search: "{topic} vs {alternative} comparison {current_year}"
```

### Web Fetch
For specific documentation pages:
```
Fetch official docs, API references, changelogs with exact URLs
Prefer WebFetch over WebSearch for authoritative sources
```

Include tool usage hints in research prompts when specific sources are needed.

## Pitfalls Reference
Before completing research, review common pitfalls:
Load: [research-pitfalls.md](research-pitfalls.md)

Key patterns to avoid:
- Configuration scope assumptions - enumerate all scopes
- "Search for X" vagueness - provide exact URLs
- Deprecated vs current confusion - check changelogs
- Tool-specific variations - check each environment
