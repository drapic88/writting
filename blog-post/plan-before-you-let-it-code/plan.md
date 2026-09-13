# Plan — The Readiness Gate Is the Cheapest Bug Fix You Own

**Standalone post.** This brief was written when these posts were planned as a
ten-part series. That is superseded: the draft carries no series note, no next-post
link and no cross-reference to another post in `blog-post/`. Where a section below
says to link to another post, explain the idea in a sentence or two inside this draft
instead, or leave it out. See [`../CRAFT.md`](../CRAFT.md).

**Source:** advanced workshop deck, slide 6 (with a beat from slide 14)
**Status:** brief · not drafted

---

## 1. Positioning

### The angle
Agents are fast enough that the expensive mistake is no longer slow typing — it is
building the wrong thing quickly. A planning gate is the cheapest intervention available,
and the interesting claim is that the gate is not process bureaucracy: it is a *context
technique*, because an approved plan is the highest-value thing you can have in the window
while code is being written.

### The thesis
> An agent will happily implement an underspecified ticket. The readiness gate exists
> because redirecting a plan costs one paragraph and redirecting an implementation costs a
> day.

### Title options
1. **The Readiness Gate Is the Cheapest Bug Fix You Own** — thesis-forward.
2. **Never Let an Agent Start From an Underspecified Ticket** — direct, prescriptive.
3. **Ask for the Plan. Every Time.** — punchy but thin on its own.

*Recommendation:* #1, subtitle "Three planning surfaces, a ten-section readiness
checklist, and why agents make underspecified tickets more expensive, not less."

---

## 2. Meta

- **Length:** 1,700–2,000 words (7–8 min).
- **Audience:** engineers and tech leads who own an implementation decision. This one also
  reads well to an engineering manager, which is useful for reach.
- **Tags:** `AI`, `Software Engineering`, `Programming`, `Developer Tools`, `Productivity`

---

## 3. Structure

### Lede (~150 words)
Open on the failure: a two-line ticket, an agent that produced 400 lines in ten minutes,
and a review where the first comment is "this isn't what we needed." Nobody was lazy. The
ticket never contained enough to be implementable, and the agent's speed removed the
friction that used to expose that.

### Section 1 — Speed changes the economics of ambiguity (~300 words)
The argument, made carefully:
- With a human implementer, an underspecified ticket surfaces early — they ask a question
  before writing code, because writing code is expensive for them.
- An agent has no such incentive. Writing code is cheap, so it fills gaps with plausible
  assumptions and keeps going.
- So the cost of ambiguity did not go down; it moved from "asked on day one" to
  "discovered in review on day three."

Conclusion: the question a human implementer would have asked has to become an explicit
gate.

### Section 2 — Three planning surfaces, and when each fits (~450 words)
From the deck, generalised so the post survives feature renames. One short subsection each:

- **A read-only planning mode.** The agent investigates and proposes but cannot edit until
  you approve. Best for the everyday case: a ticket you mostly understand.
- **A dedicated planning subagent.** An architect role that returns a step-by-step plan
  and the list of critical files without touching code. Best when you want the plan
  produced in a separate window so your own stays clean (link post 3).
- **Cloud/long-horizon planning.** Draft the plan for a big task with more compute, then
  execute remotely or back in the terminal. Best for migrations and cross-repo work.

For each, give the decision rule in one italicised line, so the section is skimmable.

### Section 3 — The ten-section readiness checklist (~500 words)
The most reusable artifact in the post. Present it as a checklist a reader can paste into
their own tracker, then explain the four sections people always skip and why they are the
expensive ones.

1. Business goal
2. Requirements and non-goals
3. Acceptance criteria
4. Architecture impact
5. Data changes
6. API changes
7. Security review
8. Test plan
9. Rollback plan
10. Monitoring plan

Then the honest commentary. **Non-goals** is the one that stops scope creep, and it is the
one nobody writes. **Architecture impact** is where cross-repo consequences surface before
they become a rollout-order problem. **Rollback** and **monitoring** are skipped because
they feel like ops concerns, and they are exactly what you want written down *before* the
agent picks an implementation, because they constrain the design.

Add the one paragraph that makes this practical: none of this requires a new tool. It is a
template in your issue tracker plus one instruction in the agent's root file — "no feature
code before these ten sections exist."

### Section 4 — Make the gate mechanical (~350 words)
The upgrade: instead of remembering to check, commit a procedure that checks for you. A
read-only reviewer that reads the ticket, reports which of the ten sections are missing,
and drafts paste-ready text for the gaps — and *never writes to the tracker*.

State the pattern plainly, because it recurs through the whole series:

> The agent drafts. The human publishes.

Show the prompt shape rather than the internal skill:

```
Check PROJ-1234 for feature readiness. Report which sections are
missing and draft the text for each. Do not write to the tracker.
```

Then the second prompt shape, borrowed from slide 14, which pairs naturally with the gate:

```
Write the integration test matrix for PROJ-1234 first, list the
negative cases, then implement the narrowest change that passes it.
```

One clause forward-linking post 6 (skills) and one forward-linking post 7 (evidence).

### Close (~150 words)
The gate is not about distrusting the agent — it is what lets you hand it bigger work.
Forward link to post 5.

---

## 4. Genericizing notes

- The ten sections are a framework, not proprietary text — safe to publish. Describe it as
  "the readiness framework we settled on," never by its internal document name.
- No internal skill names, no script paths, no real ticket keys. `PROJ-1234` throughout.
- Do not reference the internal playbook file by name.

---

## 5. Verify before publishing

- Planning-mode keyboard shortcuts and command names change; describe the capability and
  keep any specific invocation in a parenthetical you can update.
- Check whether cloud planning is generally available or plan-gated before implying anyone
  can use it.

---

## 6. Hero image brief

Craft motif: a ten-cell checklist column on the left, four cells highlighted (non-goals,
architecture impact, rollback, monitoring), and a gate glyph between it and a code block on
the right. Large "04".

---

## 7. Traps

- Do not let this become a project-management post. Every section must end in something an
  engineer types or commits.
- Do not present the checklist as mandatory for every ticket — say explicitly that a
  one-line bug fix needs one sentence of intent, not ten sections. Losing that nuance
  makes the post easy to dismiss.
- No screenshots of a real tracker.
