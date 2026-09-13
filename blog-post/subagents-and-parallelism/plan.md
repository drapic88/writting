# Plan — Subagents Buy Context Isolation, Not Speed

**Standalone post.** This brief was written when these posts were planned as a
ten-part series. That is superseded: the draft carries no series note, no next-post
link and no cross-reference to another post in `blog-post/`. Where a section below
says to link to another post, explain the idea in a sentence or two inside this draft
instead, or leave it out. See [`../CRAFT.md`](../CRAFT.md).

**Source:** advanced workshop deck, slides 7, 8, 9, 11
**Status:** brief · not drafted

---

## 1. Positioning

### The angle
Everyone reaches for subagents because they sound like parallelism, then wonders why the
token bill tripled without much getting faster. The reframe: the primary product of a
subagent is a *clean window*, and speed is a side effect that only sometimes shows up.
Then the genuinely useful part — four distinct parallelism surfaces that are usually
discussed as one thing, and a rule for picking.

### The thesis
> A subagent burns its own window on the messy part and hands you back only the
> conclusion. That is what you are buying. If you are buying speed, you are usually just
> buying tokens.

### Title options
1. **Subagents Buy Context Isolation, Not Speed** — thesis-forward, mildly contrarian.
2. **A Reviewer With No Edit Tool Is Better Than One With It** — the best single idea in
   the post, and a great hook.
3. **Four Ways to Parallelise an Agent. Three of Them Are Wrong for Your Task.** — good
   click-through.

*Recommendation:* #1, subtitle "And why a code reviewer with no ability to edit is
strictly better than one that can fix things for you."

---

## 2. Meta

- **Length:** 1,900–2,200 words (8–9 min).
- **Audience:** daily agent users who have tried subagents and found them expensive or
  underwhelming.
- **Tags:** `AI`, `Software Engineering`, `Developer Tools`, `Programming`, `Coding`

---

## 3. Structure

### Lede (~150 words)
Open on the concrete win: you need to know which of six repositories call a deprecated
endpoint. Done in your own session, that answer arrives buried under 200 search hits that
stay in your window for the rest of the task. Delegated, you get four lines. Same answer,
completely different cost for everything you do next.

### Section 1 — What you are actually buying (~350 words)
Tie directly back to post 3's three sources: delegation is the only mechanism that reduces
volume while preserving the conclusion. Three cases where it is clearly right:
- The side task would flood your window with search hits or logs.
- You want a second, *uncontaminated* opinion on your own diff — one that has not read your
  reasoning and cannot be anchored by it.
- You need the same specialist judgement repeatedly, so it should be a committed file the
  whole team gets rather than a prompt you retype.

Be explicit about when it is wrong: a small task you already have the context for is
cheaper done inline. Every delegated worker pays a startup cost in tokens.

### Section 2 — Anatomy of a committed subagent (~400 words)
Show the file, generically:

```md
---
name: api-reviewer
description: Review rest-api changes for authorization gaps,
  DTO over-exposure, and caller impact.
tools: Read, Grep, Glob, Bash
model: inherit
---
Read the repo's instruction file, then the touched resources.
Report findings only. Do not edit.
```

Then the three controls that matter, each with the reasoning:

- **`tools:` — restrict capability.** The headline idea of the post. A reviewer with no
  edit tool cannot "helpfully" fix what it finds, which forces the finding to be *written
  down*. A silent patch is a finding you never learned from. Give this its own three or
  four sentences; it is the most quotable thing here.
- **`model:` — match cost to task.** Inherit for judgement work; pin something cheaper for
  mechanical sweeps.
- **`description:` — this is routing, not documentation.** It determines when the agent
  reaches for this specialist at all.

Mention built-in roles briefly: a fan-out search role, an architecture role, and forking to
inherit your current context when you want a second opinion *with* your reasoning rather
than without it.

### Section 3 — Route by repo, and commit the routing (~350 words)
From slide 8, fully genericized. The point is not the specific stack — it is that most
teams have already written down which specialist each part of the system needs, in a
playbook nobody has turned into agent files.

| Repo | Stack | What the reviewer must know |
|---|---|---|
| `web-app` | Angular + SSR | services own API calls, components render; guard and resolver changes need navigation and auth tests |
| `marketing-site` | Astro, static-first | CMS content resolved at build time, static i18n, SEO and accessibility validation |
| `rest-api` | Java + Spring Boot | thin resources, rules in the domain service layer, persistence isolated |
| `admin-app` | Angular admin | API access confined to the core layer and page facades |
| `mobile-app` | Flutter | features isolated per directory, shared routing and design in the app layer |
| `infra` | Kubernetes manifests | test-only, dry-run first, never live state without approval |

Then the cross-repo rule: one branch per repo, record the dependency in the PR
description, agree the rollout order before writing code.

Close the section with the actionable ask: take your existing routing notes and turn each
line into a committed reviewer file. That is an afternoon of work and the whole team gets
it.

### Section 4 — Four parallelism surfaces (~450 words)
The comparison table is the section's spine. Frame the axes first: *who coordinates*,
*whether the workers talk to each other*, and *whether they touch the same files*.

| Surface | What it gives you | Use it when |
|---|---|---|
| Subagents | delegation inside one session; you collect summaries | a side task would flood your window |
| Background sessions | one screen of independent sessions, each isolated | several unrelated tasks to hand off |
| Agent teams | a lead plus teammates with a shared task list and messaging | the agent should split and supervise a project |
| Scripted workflows | a rerunnable script driving many workers and cross-checking results | a codebase-wide audit or a large mechanical migration |

Then two paragraphs that matter more than the table:
- **Isolation.** Worktrees give each session its own checkout so parallel work cannot
  collide. In a multi-repo workspace they apply per repo, not at the root — a detail that
  bites people immediately.
- **Coordination is not free.** Agent teams do not necessarily isolate teammates, so
  partition files by owner explicitly. And every parallel worker multiplies token spend:
  parallelism is a wall-clock optimisation you pay for in cost.

### Section 5 — Session controls worth knowing (~250 words)
From slide 11, cut to the two that change daily life, because a long list of flags dates
badly:
- **Rewind / checkpointing.** Roll back the agent's edits, or restore files to an earlier
  state. This matters psychologically more than technically: it removes the fear that
  makes people over-review every edit.
- **A completion condition.** Set what "done" means and let it keep working until that
  holds, instead of declaring victory early.

Mention in one sentence each: plan-on-a-strong-model/execute-on-a-cheaper-one, an effort
dial, forking a conversation, and resuming a specific session. Note that availability
varies by plan and version.

### Close (~150 words)
The compression: delegate for a clean window, restrict capability so findings get written
down, parallelise deliberately and knowingly pay for it. Forward link to post 6.

---

## 4. Genericizing notes

- The routing table is fully rewritten to the shared fictional stack. Keep the *shape* of
  the architectural constraints (they are good, general advice) and drop anything
  identifying — no product names, no CMS vendor, no integration names.
- The subagent file above is a rewrite, not a copy.
- Do not name the internal playbook.

---

## 5. Verify before publishing

- Subagent frontmatter field names and the built-in role names — check current docs.
- Whether subagents run in the background by default, and whether agent teams are still
  experimental / off by default. State maturity honestly.
- Worktree and batch-split command names.
- Session-control names (rewind, goal, effort, fast mode, advisor) are the most
  rename-prone content in the series. Describe capability first, command second.

---

## 6. Hero image brief

Craft motif: one large window with three small satellite windows feeding thin arrows back
into it, each satellite visibly denser than the arrow it emits. One satellite drawn with a
crossed-out pencil icon (the reviewer with no edit tool). Large "05".

---

## 7. Traps

- Do not imply subagents make things faster by default. The post's credibility rests on
  being honest about token cost.
- Do not let the parallelism table sprawl into a feature comparison — three axes, four
  rows, then prose.
- Do not skip the "when delegation is wrong" paragraph; without it the post reads like
  advocacy.
