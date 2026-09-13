# Plan — A Tip Nobody Installs Is Not a Tip

**Standalone post.** This brief was written when these posts were planned as a
ten-part series. That is superseded: the draft carries no series note, no next-post
link and no cross-reference to another post in `blog-post/`. Where a section below
says to link to another post, explain the idea in a sentence or two inside this draft
instead, or leave it out. See [`../CRAFT.md`](../CRAFT.md).

**Source:** advanced workshop deck, slides 25–28, 30
**Status:** brief · not drafted

---

## 1. Positioning

### The angle
The closing post, and the one about compounding. Two ideas: recurring work should be a
committed file with an owner rather than a habit you have to remember, and — the harder
truth — a practice that only one person has installed is not a team practice. Distribution
is the actual work.

### The thesis
> Recurring work should be a committed file with an owner, not a habit you remember. And a
> tip nobody installs is not a tip — the distribution is the work, not the insight.

### Title options
1. **A Tip Nobody Installs Is Not a Tip** — best line, and the honest one.
2. **Automate the Boring Half: Scheduled Agents That Only Read** — most descriptive of the
   content.
3. **Your Team Doesn't Have Your Setup. That's the Whole Problem.** — good for a lead
   audience.

*Recommendation:* #1, subtitle "Scheduling recurring agent work, choosing the right
recurrence surface, and why distribution is harder than the insight."

---

## 2. Meta

- **Length:** 1,700–2,000 words (7–8 min).
- **Audience:** anyone who has built a good agent setup and watched nobody else adopt it.
  Leads and staff engineers especially.
- **Tags:** `AI`, `Automation`, `Software Engineering`, `Developer Tools`, `Productivity`

---

## 3. Structure

### Lede (~150 words)
Open on the recognisable disappointment: you build a genuinely good workflow, you demo it,
everyone nods, and three weeks later you are the only person using it. The insight was
never the bottleneck.

### Section 1 — Three recurrence surfaces, chosen by what they touch (~450 words)
The clearest decision rule in the source material. One subsection each:

- **Scheduled local tasks.** Need the local workspace or dev container: writing a cache to
  disk, running git commands, preparing review bundles. The default for anything local.
- **Cloud routines.** Hosted, connector-only, read-only. Ticket readiness summaries, stale
  work scans. No local file access — and they run with your laptop closed, which is the
  entire point.
- **In-session polling loops.** Temporary, scoped to an active session: watch a pipeline to
  green, poll a long job. Dies with the session.

Then the mistake worth naming: using an in-session loop for something that should be
scheduled, and then wondering why it stopped. It is session-scoped by design.

State the invariant that makes the whole thing safe: **the policy is identical in all three
modes.** External systems stay read-only; local writes are confined to one directory. If a
surface would require relaxing that, it is the wrong surface.

### Section 2 — A daily clock (~450 words)
The most copyable artifact in the post. Present four automations as a schedule, described
so a reader can rebuild them:

- **08:35, local** — cache the work assigned to you. Query the tracker for open items
  assigned to the current user, write an index plus one file per item, plus a readiness
  summary and a run log, under a single cache directory.
- **08:45, cloud or local** — a readiness check. Read the cache if it is fresh, otherwise
  the tracker read-only. Return four buckets — ready to implement, ready for architecture
  review, not ready with the missing sections named, blocked — plus today's top five
  actions. This is post 4's gate, running before you open your editor.
- **09:00, local** — review preparation. Run the bundle script across every repo, and
  report dirty worktrees and stale refs as first-class output. This is post 7's pipeline,
  pre-warmed.
- **Monday, cloud** — a stale-work scan. Active items assigned to or recently touched by
  you that are stale or missing acceptance criteria, a test plan, or architecture impact.

Then the verification checklist for any new schedule, which is the part that makes this
trustworthy rather than alarming — run it once manually, confirm the cache appeared,
confirm no tracker item changed, confirm nothing was posted anywhere, and confirm the output
separates tracker state from code and runtime evidence (post 7 again).

One paragraph on identity: each person authenticates their own approved account, and
discovery uses "the current user" rather than a hardcoded identifier — so nothing personal
ends up in committed configuration.

### Section 3 — Read-only connectors are the enabling constraint (~250 words)
Short but load-bearing. Scheduled runs are the least supervised thing an agent does — no
one is watching at 08:35. That is precisely why the connectors are read-only, and it is
what makes scheduling acceptable at all. The pattern from post 4 returns: the agent drafts,
the human publishes. A scheduled run may produce a summary; it may never post one.

### Section 4 — Distribution is the actual work (~400 words)
The section the title comes from. Progression:

- **A script.** An installer plus a verifier. Root instruction files, the dev container,
  the review command, the commit hook policy, per-repo instruction files. Check the host
  tooling; never auto-install a container runtime for someone.
- **Keeping it from drifting.** Three checks worth wiring into CI: that the scripts and
  their JSON parse, that an install actually landed, and that installed files still match
  the templates they came from. Land the line: **a drifted template is an unreviewed policy
  change.**
- **A plugin plus an internal source.** One install that bundles skills, subagents, hooks,
  commands and connectors, and an internal source teammates add once and update from —
  which removes the install script from onboarding entirely.

Be honest about the failure mode this fixes: not that people disagreed with the practice,
but that adopting it required six manual steps, and the sixth one failed silently on
someone's machine.

### Section 5 — Start Monday (~300 words)
The series close, as five moves in payback order. Keep them concrete:

1. **Install and verify** your setup, and reopen in the container (post 8).
2. **Turn on two read-only schedules** — the cache and the readiness check.
3. **Run one change through the review pipeline** and post the findings yourself (post 7).
4. **Write one reviewer subagent** for the repo you know best and commit it (post 5).
5. **Add one post-edit hook** that lints or formats the file just changed (post 8). It
   deletes a whole class of review comment for twenty lines of shell.

Then the paste-ready prompts, generically:

```
Check PROJ-1234 for feature readiness.
Prepare a local review for web-app against origin/main.
Read .ticket-cache/assigned/ and tell me what needs attention today.
Draft QA notes for PROJ-1234.
```

Close the series with the phasing and the improvements file: local pilot → team baseline →
operational hardening, write-capable automation needs explicit approval, and every finding
goes into a committed improvements file — because that file is how the practice actually
improves, and without it you are just maintaining documentation.

---

## 4. Genericizing notes

- Generic paths only: `.ticket-cache/assigned/`, `scripts/prepare-review.sh`,
  `scripts/install-setup.sh`. No internal script or document names.
- No real JQL. Describe the query in words: "open items assigned to the current user."
- Do not name the tracker, chat or wiki products in a way that maps to a specific company's
  stack — "your tracker", "your team chat" is enough.
- The daily clock is presented as "a schedule that works", not as one company's rollout.

---

## 5. Verify before publishing

- Terminology for the three recurrence surfaces, and whether cloud routines are generally
  available or plan-gated. This is the most product-dependent post in the series.
- Plugin and internal-source (marketplace) terminology and availability.
- Whether connector permissions can actually be constrained to read-only in the current
  product; if not, say what the operator must do instead. Do not assert a guarantee the
  tooling does not provide.

---

## 6. Hero image brief

Trust motif, closing the series: a 24-hour clock face with four marked slots (08:35, 08:45,
09:00, Mon), each with a small one-way arrow pointing *out* of the systems it reads —
visually signalling read-only. Large "10".

---

## 7. Traps

- Do not present unattended automation as harmless. The read-only constraint is what makes
  it acceptable and must be stated before the schedule, not after.
- Do not let the closing five moves become a summary of the whole series. Five actions, one
  line of context each.
- Do not promise that a scheduled run costs nothing — it consumes usage every morning
  whether or not you read the output.
