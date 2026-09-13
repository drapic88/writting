# Plan — Stop Retyping Procedures. Commit Them.

**Standalone post.** This brief was written when these posts were planned as a
ten-part series. That is superseded: the draft carries no series note, no next-post
link and no cross-reference to another post in `blog-post/`. Where a section below
says to link to another post, explain the idea in a sentence or two inside this draft
instead, or leave it out. See [`../CRAFT.md`](../CRAFT.md).

**Source:** advanced workshop deck, slides 10 and 28
**Status:** brief · not drafted

---

## 1. Positioning

### The angle
Teams accumulate long, carefully tuned prompts in private notes files. That is an
unreviewed, unversioned, undiscoverable procedure — the exact opposite of how the same team
treats code. A skill is that procedure committed to the repo: loaded only when relevant,
improved through review, and structured so it does not cost context until it is needed.

### The thesis
> A prompt you retype is a procedure with no owner, no version history, and no review. Put
> it in a file, and it starts improving instead of decaying.

### Title options
1. **Stop Retyping Procedures. Commit Them.** — imperative, clear.
2. **Your Best Prompt Should Be a Reviewed File** — thesis in one line.
3. **Progressive Disclosure: How to Give an Agent 3,000 Words Without Paying for Them** —
   the most technically interesting angle, narrower audience.

*Recommendation:* #2, subtitle "Skills, progressive disclosure, and why the procedure
should live next to the code it describes."

---

## 2. Meta

- **Length:** 1,600–1,900 words (7–8 min).
- **Audience:** engineers who have a `prompts.md` in their home directory, and leads trying
  to make one person's good practice reach the team.
- **Tags:** `AI`, `Software Engineering`, `Developer Tools`, `Programming`, `Automation`

---

## 3. Structure

### Lede (~150 words)
Open on the artifact everyone recognises: a scratch file of prompts that took months to
tune, that nobody else on the team has, that has never been reviewed, and that quietly goes
stale as the codebase moves. Name it for what it is — a procedure with no owner.

### Section 1 — Why a file beats a prompt (~350 words)
Three arguments, each in its own short paragraph:
- **Conditional loading.** A description-matched file costs nothing until it is relevant. A
  prompt you paste costs the same every time, and a mega-prompt covering every case pays
  for all of them at once. Tie back to post 3: this is a context decision.
- **Review.** It changes in a pull request like anything else, which means it *improves*.
  Someone can disagree with step four and the disagreement gets resolved once, for
  everyone, in writing.
- **Distribution.** It arrives with the checkout. Nobody has to be told it exists.

### Section 2 — Progressive disclosure, with a real example (~500 words)
The section that carries the post. The structure: a short entry file that is always
considered, plus reference files loaded only when the situation warrants.

```
skills/
  content-port-review/
    SKILL.md                     # boundary, required context, when to escalate
    references/
      review-checklist.md        # loaded for every page or component port
      seo-baseline.md            # only when head/meta, canonicals or sitemaps change
      platform-gates.md          # what CI already enforces
```

Walk through what belongs at each level:
- `SKILL.md` — scope, the boundary of what this procedure may and may not do, what context
  it must gather first, and when to stop and escalate to a human. Short, on purpose.
- `references/` — the long material. Checklists, compliance baselines, domain rules.

Then the best concrete example the source material offers, generalised: an SEO compliance
baseline turned into per-change checkable rules with stable requirement IDs — *including
the known production defects, where matching production is itself a defect.* That last
clause is the whole argument for skills over prompts: no prompt carries that reliably,
because it is too long to retype and too specific to remember.

Add the paragraph about the third level of disclosure: a reference file that says what CI
already enforces, so the reviewer stops duplicating checks the pipeline runs. This is the
detail that makes readers realise skills are about *narrowing* work, not adding it.

### Section 3 — What makes a good skill boundary (~350 words)
Practical guidance, since most readers' first attempt will be too broad:
- One procedure per skill. "Review a content port" is a skill; "help with frontend" is not.
- The description is the trigger — write it as the situation, not the capability.
- Say what the skill must *not* do. Read-only boundaries belong in the file, not in the
  operator's memory.
- Escalation criteria beat exhaustive rules. A skill that knows when to stop is more
  valuable than one that tries to cover every case.

Give two or three real skill ideas readers can build this week: a readiness check for
tickets (post 4), a local review-bundle preparation step (post 7), and a per-repo
convention reviewer.

### Section 4 — Then package it (~300 words)
From slide 28, compressed. The progression: files in a repo → an installable plugin that
bundles skills, subagents, hooks, commands and connectors behind one install → an internal
source teammates add once and update from.

Then the two maintenance realities that nobody mentions:
- **Drift.** Installed files stop matching the templates they came from, and a drifted
  template is an unreviewed policy change. Check it in CI.
- **Tool-set size.** A large connector set floods the context window; the mechanisms that
  load tool definitions on demand exist for a reason.

One line on the honest framing: distribution is the actual work. A tip nobody installs is
not a tip — which is post 10's thesis, so keep it to a clause.

### Close (~150 words)
The test for whether something should be a skill: would you be annoyed if a teammate
solved this from scratch? Then commit it. Forward link to post 7.

---

## 4. Genericizing notes

- The three internal skills become generically named equivalents. Never use the internal
  names.
- The SEO baseline example is publishable as *a pattern* — describe the technique
  (requirements with stable IDs, known-defect exceptions) without quoting the internal
  compliance report or naming its source.
- No internal script or repo paths.

---

## 5. Verify before publishing

- Skill file layout, frontmatter fields and the loading mechanism — check current docs;
  this format has moved before.
- Plugin and marketplace terminology, and whether internal marketplaces are generally
  available.
- The name of the on-demand tool-loading mechanism.

---

## 6. Hero image brief

Craft motif: a small solid card labelled `SKILL.md` in front, three larger translucent
cards behind it, each with a dashed "loaded on demand" connector. Large "06".

---

## 7. Traps

- Do not write the post as documentation of a file format. The argument is
  organisational — reviewed procedures beat private ones — and the format is evidence.
- Do not claim skills reduce token use in general; they reduce *always-on* token use. Be
  precise, a reader who has measured will catch it.
- Keep the packaging section short. Post 10 owns distribution.
