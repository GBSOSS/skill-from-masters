---
name: skill-from-masters
description: Help users create high-quality skills by discovering and incorporating proven methodologies from domain experts. Use this skill BEFORE skill-creator when users want to create a new skill - it enhances skill-creator by first identifying expert frameworks and best practices to incorporate. Triggers on requests like "help me create a skill for X" or "I want to make a skill that does Y". This skill guides methodology selection, then hands off to skill-creator for the actual skill generation.
---

# Skill From Masters

Create skills that embody the wisdom of domain masters. This skill helps users discover and incorporate proven methodologies from recognized experts before generating a skill.

## Core Philosophy

Most professional domains have outstanding practitioners who have codified their methods through books, talks, interviews, and frameworks. A skill built on these proven methodologies is far more valuable than one created from scratch.

The goal is not just "good enough" — it's reaching the highest level of human expertise in that domain.

## Critical Requirements for Non-Technical Skills

**Technical skills have standard answers.** Writing code, debugging, or configuring systems — these have relatively objective quality bars.

**Non-technical skills vary dramatically in quality.** Skills involving decision-making, communication, persuasion, or judgment can range from mediocre to world-class. The difference comes from incorporating deep expertise.

For non-technical skills (writing, sales, hiring, product decisions, etc.), follow these requirements:

### 1. **Narrow, Specific Task Definition** ⚠️ CRITICAL
- The task must be **extremely specific and well-defined**
- ❌ BAD: "Write a sales email" (too broad)
- ✅ GOOD: "Write a B2B cold outreach email to enterprise CTOs"
- ✅ GOOD: "Write a project status report email to executive stakeholders"
- Different contexts require completely different skills
- If the user's request is too broad, help them narrow it down through questions

### 2. **Model Selection: Opus Required** 🎯 MANDATORY
- Non-technical skills MUST use **Claude Opus** (claude-opus-4-5)
- DO NOT use Sonnet, Haiku, or any other model
- Opus has the reasoning depth needed for nuanced, judgment-based tasks
- The quality difference is substantial for these domains

### 3. **Methodology Research: Clear & Reliable Conclusions** 🔍 ESSENTIAL
- Continue searching and communicating until you reach **very clear, reliable conclusions**
- Don't stop at surface-level research
- Sources to exhaust:
  - The model's own training knowledge
  - Web search for current best practices
  - Golden examples from top practitioners
  - Counter-examples and common mistakes
- Keep iterating until the methodology is crystal clear and well-validated

### 4. **Consider Plan Mode for Complex Tasks** 🎯 RECOMMENDED
- For complex or multi-faceted skills, prefer thinking through the approach first
- Better to think more before acting
- Use plan mode to structure the methodology research and synthesis

### 5. **Test Broadly, Then Iterate** ✅ REQUIRED
- Have the agent think through **extensive test scenarios**
- Test across diverse contexts, edge cases, and failure modes
- Review test results and optimize before finalizing
- Quality emerges from iteration, not first drafts

## Workflow

**Before Starting: Consider Plan Mode** 🎯

For complex or high-stakes skill creation (especially non-technical skills), consider using **plan mode**:
- Allows more upfront thinking before taking action
- Helps structure the methodology research systematically
- Reduces the risk of missing important considerations
- Better for skills involving judgment, persuasion, or complex decision-making

To use plan mode, the user can invoke it explicitly, or you can suggest: "This is a complex skill involving [decision-making/communication/etc]. Would you like me to use plan mode to think through the methodology research more carefully?"

### Step 1: Understand and Narrow the Skill Intent

**CRITICAL FOR NON-TECHNICAL SKILLS:** Ensure the task is narrow and specific enough.

Ask the user:
- What skill do they want to create?
- What specific tasks should it handle?
- What quality bar are they aiming for?

**If the request is too broad**, help narrow it down:

Example dialogue:
- User: "I want a skill for writing emails"
- You: "Let's narrow this down. Emails vary greatly by context. Some possibilities:
  - Cold outreach emails to potential customers?
  - Internal status update emails to executives?
  - Customer support response emails?
  - Negotiation emails with vendors?

  Which specific type of email writing would be most valuable to you?"

**Goal:** Define a task so specific that the methodology and quality criteria are unambiguous.

### Step 2: Identify Relevant Domains

Map the skill to one or more methodology domains. A single skill may span multiple domains.

Example mappings:
- "Sales email skill" → Sales, Writing, Persuasion
- "User interview skill" → User Research, Interviewing, Product Discovery
- "Presentation skill" → Storytelling, Visual Design, Persuasion
- "Code review skill" → Software Engineering, Feedback, Communication

### Step 3: Surface Expert Methodologies (Until Crystal Clear)

**GOAL:** Don't stop until you have **very clear, reliable conclusions** about the best methodology.

**Layer 1: Local Database**
Consult `references/methodology-database.md` for known frameworks.

**Layer 2: Web Search for Experts**
Search the web to discover additional experts and methodologies:
- Search: "[domain] best practices expert"
- Search: "[domain] framework methodology"
- Search: "[domain] master practitioner"

**Layer 3: Deep Dive on Selected Experts**
For promising experts, search for their original content:
- Search: "[expert name] methodology interview"
- Search: "[expert name] [domain] transcript"
- Search: "[expert name] framework explained"

Fetch and read primary sources when available (articles, talk transcripts, blog posts).

**Layer 4: Keep Iterating Until Clear** ⚠️ NEW
- Don't stop at the first search results
- If methodologies seem unclear or conflicting, dig deeper
- Look for:
  - Model's own knowledge (you have extensive training data)
  - Current web best practices
  - Golden examples from practitioners
  - Anti-patterns and common mistakes
- **Continue the research loop** until you can confidently say: "This is the proven way to do this"

For each relevant domain, present:
- Key experts and their core contributions
- Specific frameworks, principles, or processes
- Source materials (books, talks, interviews)
- **Confidence level** in the methodology (keep searching if low)

### Step 4: Find Golden Examples

Before finalizing methodology selection, search for exemplary outputs:
- Search: "best [output type] examples"
- Search: "[output type] template [top company]"
- Search: "award winning [output type]"

Understanding what excellence looks like helps define the quality bar.

### Step 5: Collaborative Selection

Present the methodologies to the user and discuss:
- Which frameworks resonate with their goals?
- Are there conflicts between methodologies to resolve?
- Should they combine multiple approaches?
- Any specific principles they want to emphasize or exclude?

Guide the user to select 1-3 primary methodologies that will form the skill's foundation.

### Step 6: Extract Actionable Principles

For each selected methodology, search for and distill:

**The Why (Core Principles)**
- Search: "[methodology] core principles"
- Search: "why [methodology] works"

**The How (Concrete Process)**
- Search: "[methodology] step by step"
- Search: "[methodology] implementation guide"

**The What (Quality Criteria)**
- Search: "[methodology] checklist"
- Search: "[methodology] evaluation criteria"

**The Pitfalls (Common Mistakes)**
- Search: "[domain] common mistakes"
- Search: "[methodology] pitfalls avoid"

Fetch primary sources to get exact wording and nuance, not just summaries.

### Step 7: Cross-Validate

Compare insights across multiple sources:
- What principles appear consistently? (high confidence)
- Where do experts disagree? (flag for user)
- What's unique to each approach? (differentiation)

Synthesize a coherent framework that takes the best from each source.

### Step 8: Design Test Scenarios (Before Generation)

**CRITICAL:** Before generating the skill, design comprehensive test scenarios.

Work with the user to identify:

**Diverse Test Cases:**
- Typical scenarios (the common case)
- Edge cases (unusual but valid situations)
- Boundary conditions (where the methodology might break down)
- Failure modes (what could go wrong)

**Context Variations:**
- Different user expertise levels
- Different organizational contexts (startup vs enterprise)
- Different constraints (time, resources, stakeholder complexity)
- Cultural or industry differences

**Quality Validation:**
- What does "excellent" output look like?
- What are the most common mistakes to avoid?
- How will we know if the skill is working?

Document these test scenarios — they'll be used after generation to validate and iterate.

### Step 9: Generate the Skill

With methodologies confirmed and test scenarios designed, use the **skill-creator** skill to generate the final skill.

**For non-technical skills, CRITICAL:**
- Invoke skill-creator with `model: "opus"` parameter
- This ensures the generation uses Claude Opus, not a weaker model

The generated skill should:

1. Credit the methodology sources in a comment (documenting provenance)
2. Translate expert wisdom into actionable instructions
3. Include concrete examples derived from golden examples found
4. Capture quality criteria as explicit checkpoints
5. Include "don't do this" anti-patterns from pitfall research
6. Match the quality bar of the best human practitioners
7. **Include the test scenarios** as part of the skill's self-validation

### Step 10: Test, Review, and Iterate

**Don't stop at first generation.** Quality emerges through iteration.

1. **Run Test Scenarios**: Apply the skill to each test case designed in Step 8
2. **Evaluate Results**: Compare outputs against quality criteria
3. **Identify Gaps**: Where did the skill fall short?
4. **Refine Methodology**: Do we need additional expert guidance?
5. **Regenerate**: Update the skill based on learnings
6. **Repeat**: Until the skill consistently produces excellent results

Involve the user in this evaluation — they know their domain and can spot nuances.

## Quality Checklist

Before finalizing, verify:

**Scope & Clarity:**
- [ ] Is the task definition narrow and specific enough? (Not too broad)
- [ ] Would someone reading the skill know exactly when to use it?

**Methodology Depth:**
- [ ] Did we search beyond the local database?
- [ ] Did we find primary sources, not just summaries?
- [ ] Did we reach **very clear, reliable conclusions** about the methodology?
- [ ] Did we find golden examples of the output?
- [ ] Did we identify common mistakes to avoid?
- [ ] Did we cross-validate across multiple experts?

**Generation Quality:**
- [ ] For non-technical skills: Did we use **Opus model** for generation?
- [ ] Does the skill encode specific, actionable steps (not vague principles)?
- [ ] Are test scenarios included in the skill?

**Testing & Iteration:**
- [ ] Did we design comprehensive test scenarios beforehand?
- [ ] Did we test the skill across diverse contexts and edge cases?
- [ ] Did we iterate based on test results?
- [ ] Does the skill consistently produce excellent outputs?

**Plan Mode (if applicable):**
- [ ] For complex skills: Did we consider using plan mode?
- [ ] Did we structure our thinking before acting?

## Example Interaction

**User**: I want to create a skill for writing product requirement documents.

**Assistant**: I can help with that. First, let me make sure we're scoped properly. PRDs can vary significantly by context:
- Are these for internal feature specs for engineers?
- Stakeholder alignment documents for executives?
- Product briefs for design teams?
- Technical requirements for external vendors?

Which specific type of PRD would be most valuable for you?

**User**: Internal feature specs for engineers at a B2B SaaS company.

**Assistant**: Perfect, that's specific enough. Since this is a non-technical skill involving communication and judgment, I'd recommend using **plan mode** to think through the methodology research carefully. Should I proceed in plan mode?

**User**: Yes, go ahead.

**Assistant**: [Enters plan mode and structures the research approach]

Let me search systematically for the best methodologies on engineering-focused PRD writing.

[Searches: "PRD best practices expert", "product requirements document methodology for engineers", "best PRD examples B2B SaaS"]

I found several strong frameworks:

**Product Management**:
- Marty Cagan (SVPG): Emphasizes problem-first PRDs, separating problem space from solution space
- Teresa Torres: Continuous discovery, outcome-focused requirements

**Business Writing**:
- Barbara Minto: Pyramid Principle - lead with conclusion, MECE structure
- Amazon: Working backwards from press release, 6-pager narrative format

**Golden Examples Found**:
- Intercom's public PRD template
- Linear's product spec format

**Common Mistakes** (from my search):
- Jumping to solutions before defining the problem
- Writing for engineers instead of for alignment
- Missing success metrics

Let me dig deeper into primary sources to get very clear conclusions...

[Continues searching until methodology is crystal clear]

Which of these approaches resonates? Or should I search deeper into any of them?

**User**: I like Amazon's approach combined with Cagan's problem-first thinking. Can you find more details on Amazon's method?

**Assistant**: [Searches: "Amazon 6-pager template", "Amazon working backwards methodology", "Amazon PR FAQ process"]

[Fetches relevant articles and synthesizes key principles]

Here's what I found from primary sources...

[After thorough methodology research]

**Assistant**: Before I generate the skill, let me design test scenarios. Let's think through diverse cases:

**Test Scenarios:**
1. Simple feature: Adding a filter to existing dashboard
2. Complex feature: New AI-powered recommendation engine
3. Edge case: Feature requiring significant backend architecture changes
4. Failure mode: Vague problem statement that needs refinement

Does this cover the range of PRDs you typically write? Any other scenarios we should test?

**User**: Also add: Feature that needs cross-team coordination.

**Assistant**: Great addition. Now I'll generate the skill using **Opus** to ensure high quality.

[Generates skill, then tests it]

I've generated the skill and tested it against our scenarios. Here's what I found...

[Reviews results, identifies gaps, iterates]

[Continues to Step 10: refinement based on test results]
