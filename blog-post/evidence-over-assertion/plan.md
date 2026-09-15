# Plan — "Done" Is Five Separate Claims

**Standalone post.** This brief was written when these posts were planned as a
ten-part series. That is superseded: the draft carries no series note, no next-post
link and no cross-reference to another post in `blog-post/`. Where a section below
says to link to another post, explain the idea in a sentence or two inside this draft
instead, or leave it out. See [`../CRAFT.md`](../CRAFT.md).

**Source:** advanced workshop deck, slides 13–17
**Status:** brief · drafted

---

## 1. Positioning

### The angle
The most differentiated post in the series. Everyone writes about making agents
*productive*; almost nobody writes about making them *trustworthy*, which is the actual
bottleneck on adoption. The core insight is that an agent infers delivery from code it can
see, so the fix is structural: never let five independent signals collapse into one word.

### The thesis
> An agent is fast at producing confident prose. QA is where you make it produce verifiable
> evidence instead. "Done" is not a status — it is five separate claims, and each one has
> its own proof.

### Title options
1. **"Done" Is Five Separate Claims** — best title in the series. Concrete, surprising,
   quotable.
2. **Your Agent Said It Shipped. Nothing Was Deployed.** — story-first, high click-through.
3. **Evidence Over Assertion: Making an AI Agent Trustworthy** — descriptive, safest,
   weakest.

*Recommendation:* #1, subtitle "The failure mode where an agent reads feature code and
reports 'shipped' — and the evidence standard that makes it impossible to say by accident."

---

## 2. Meta

- **Length:** 2,100–2,400 words (9–10 min).
- **Audience:** engineers, QA, and leads who have to decide whether agent output can be
  believed. This is the post to send to a sceptical staff engineer.
- **Tags:** `AI`, `Software Engineering`, `Software Testing`, `Programming`, `Developer Tools`

---

## 3. Structure

### Lede (~200 words)
Lead with the failure in full, because it is the most persuasive 150 words available. The
agent reads a branch that looks merged. It sees the feature code. It reports "shipped." The
ticket is still In Progress, nothing is deployed, and a stakeholder acts on the summary.

Nobody lied. The agent inferred delivery from code it could see, which is a reasonable
inference and completely wrong. Then the thesis: the fix is not a better prompt, it is
refusing to let five signals become one word.

### Section 1 — The five signals (~450 words)
The heart of the post. Each signal gets a short paragraph naming what it proves and, more
importantly, what it *does not*:

| Signal | Proves | Does not prove |
|---|---|---|
| Ticket status | what a human recorded | that any code exists |
| Branch | where the work lives | that it is reviewed or merged |
| PR / commit | the actual diff and its target | that it passes anything |
| Tests | commands run and their exact results | that it is deployed |
| Runtime | image or tag, pod or job state, endpoint result, logs | that it is accepted |

Then the three rules that follow:
- **Never collapse them.** Report them separately, always, even when all five are green.
- **Low-confidence items stay out of business summaries** until manually confirmed.
- **On failure, name the failing layer, keep the partial evidence, and return a useful
  partial result.** "It didn't work" is a worse output than "tests pass, deploy blocked on
  a missing config value, here is the log line."

That last rule is the one experienced readers will appreciate most — give it real space.

### Section 2 — Tests are the contract (~450 words)
Reframe: ask for the test matrix *before* the implementation. Four layers from slide 14,
each with what belongs there and when it is required:

1. **Unit** — pure logic, validators, mappers, guards, controllers, form configuration.
   Generated alongside the change, never after.
2. **Integration** — authorization on endpoints (401/403/cross-account), repositories,
   scheduled job and CLI behaviour, adapters against fakes. Required for any endpoint or
   data change, no exceptions.
3. **Regression** — one narrow test per bug you have already paid for once. Name the
   category: handoffs between systems, lifecycle state, subscription/entitlement state,
   accidental public exposure, platform parity.
4. **End-to-end and manual** — full workflows across UI, API, auth and external services.
   Name the manual-only gaps explicitly rather than pretending coverage.

The important paragraph: **the negative cases matter more than the happy path.** The two
risks that only appear in tests you deliberately ask for are cross-account authorization
and public endpoints exposing more data than intended. An agent asked for "tests" writes
the happy path; asked for "the negative cases," it writes the ones that find bugs.

Give the prompt shape:

```
Write the integration test matrix for PROJ-1234 first. List the negative
cases — unauthorized, cross-account, missing field, oversized payload.
Then implement the narrowest change that passes it.
```

Then the standard for when tests cannot run: state exactly why, and supply manual QA
steps. "Should work" is not an accepted output.

### Section 3 — A review pipeline with three tiers (~400 words)
- **In-session review of your working diff** — a fast first pass before you open the PR.
- **A deeper multi-agent review** — several reviewers whose findings are then verified
  before you believe them. Note the two-stage shape: find, then adversarially verify.
- **A committed reviewer subagent** — the specialist from post 5, with read and search
  tools and no edit tool.

Then the local prep pattern, which is the practical part: a script that assembles a review
bundle before any reviewing happens.

```
scripts/prepare-review.sh --repo web-app --target origin/main
# writes .review/<timestamp>/web-app/
#   metadata.txt  status.txt  diffstat.txt
#   changed-files.txt  branch-commits.txt
#   diff.patch  review-prompt.md
```

Findings, in priority order: bugs and behavioural regressions; security and trust-boundary
changes; missing or weak tests; QA risks and manual gaps; traceability (a missing ticket
key).

Two traps worth naming explicitly, because both produce confidently wrong reviews:
- **Stacked PRs reviewed against the wrong base**, which attributes prerequisite changes to
  this change.
- **Treating the PR description or the task document as evidence** rather than as a claim
  to verify. Read the status file first, and do not mistake your own dirty worktree for the
  change under review.

### Section 4 — A security finding needs a shape (~400 words)
"This looks risky" is unactionable. Seven required fields:

1. Attack path
2. Preconditions
3. Severity
4. Confidence
5. Files and lines
6. Suggested fix
7. Validation test

Then the paragraph that makes the section: **confidence is the field everyone skips and the
one reviewers need most.** A high-severity, low-confidence finding is worth writing down
and must not go into a business summary. Without the field, those two states are
indistinguishable and you either panic or ignore.

Follow with the high-risk-by-default list — public endpoints, auth flows, payments and
subscriptions, uploads and downloads, admin actions, integrations, and anything rendering
CMS content or third-party browser code — and a closing note on prompt-injection and
supply-chain risk wherever code fetches remote scripts or proxies AI services.

Mention tooling generically in two sentences: a review command scoped to pending changes,
and plugins that let the agent review its own diff as it writes.

### Close (~150 words)
The reframe: this is not distrust. An evidence standard is what lets you *give the agent
more work*, because a claim you can check is a claim you do not have to re-do. Forward
link to post 8.

---

## 4. Genericizing notes

- The audit-artifact list stays, with generic paths: `.ticket-cache/assigned/`,
  `.review/<timestamp>/`, PR description, QA note, runtime check output. Keep the "do not
  commit generated caches or review bundles" line.
- The script name becomes `scripts/prepare-review.sh`. No internal script paths.
- The regression categories are rewritten to remove named third-party systems.
- `PROJ-####` for ticket keys. No real project prefix.
- Do not reproduce the internal wording of the review-prompt file.

---

## 5. Verify before publishing

- Review and security command names and whether the deep multi-agent review is generally
  available or plan-gated.
- Plugin names for security review — check before naming any.
- If quoting the two-stage find-then-verify review shape, confirm it still describes how
  the tooling works.

---

## 6. Hero image brief

Trust motif and the series' strongest visual: five chain links labelled ticket / branch /
diff / tests / runtime, four solid and the fifth drawn open, with the word "done" struck
through above. Large "07".

---

## 7. Traps

- Do not soften the opening failure story. Its specificity is what makes the post land.
- Do not turn the test-layer section into a general testing-pyramid post — every layer must
  connect to what an agent gets wrong without it.
- Do not present the seven-field finding format as bureaucracy; each field exists because
  its absence produced a bad decision. Say which.
- No real findings, severities, or incident details.
