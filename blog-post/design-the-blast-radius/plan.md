# Plan — The Container Is the Security Model, Not the Prompt

**Standalone post.** This brief was written when these posts were planned as a
ten-part series. That is superseded: the draft carries no series note, no next-post
link and no cross-reference to another post in `blog-post/`. Where a section below
says to link to another post, explain the idea in a sentence or two inside this draft
instead, or leave it out. See [`../CRAFT.md`](../CRAFT.md).

**Source:** advanced workshop deck, slides 18–21, 24, 29
**Status:** brief · not drafted

---

## 1. Positioning

### The angle
Most teams' agent safety story is a sentence in an instruction file asking the agent not to
do dangerous things. That is a request to a probabilistic system. This post argues the
containment has to be structural — the container, the deny list, and the hook are the parts
that do not depend on anyone paying attention.

### The thesis
> You cannot ask a probabilistic system to be reliably careful. Design the blast radius
> first: what it can reach, what it must ask about, and what is refused without a prompt.

### Title options
1. **The Container Is the Security Model, Not the Prompt** — thesis-forward, strong.
2. **Design the Blast Radius Before You Give an Agent Shell Access** — most direct.
3. **Deny Is Policy. Ask Is Judgement. Allow Is Speed.** — the best line in the post, and a
   great subtitle.

*Recommendation:* #1, with #3 as the subtitle.

---

## 2. Meta

- **Length:** 1,900–2,200 words (8–9 min).
- **Audience:** engineers and leads about to give an agent real capability, plus anyone who
  has to answer a security review about it. Also the post most likely to reach a
  platform/DevOps audience.
- **Tags:** `AI`, `DevOps`, `Security`, `Software Engineering`, `Developer Tools`

---

## 3. Structure

### Lede (~170 words)
Open on the asymmetry: an agent that writes a wrong line of code costs a review comment. An
agent that runs a wrong command against a live cluster costs an incident. The instruction
file is where you express intent; it is not where you enforce it. Promise four layers, from
outermost in.

### Section 1 — Pick isolation to match the blast radius (~350 words)
Four options, weakest to strongest, each with what it does and does not contain:

- **A sandboxed single command** — filesystem and network isolation for one invocation.
  Good for an untrusted script; does nothing about the session as a whole.
- **A dev container** — the sensible default. Consistent, reviewable, identical for the
  whole team.
- **A worktree** — and the important correction: *this isolates changes, not capabilities.*
  A worktree does not stop a command from reaching your SSH keys. People conflate these two
  constantly; make the distinction explicit.
- **A VM or a cloud session** — for anything you would not run on your laptop.

### Section 2 — What the container does not mount (~400 words)
The concrete, publishable part. Present a dev container configuration generically:

```json
{
  "remoteUser": "node",
  "workspaceFolder": "/workspaces/project",
  "mounts": ["source=agent-config,target=/home/node/.config,type=volume"],
  "containerEnv": { "DISABLE_AUTOUPDATER": "1", "DO_NOT_TRACK": "1" },
  "postStartCommand": "sh .devcontainer/post-start.sh"
}
```

Then the list that carries the section — never mounted:
- the host home directory
- SSH keys, kubeconfigs, cloud credentials
- browser profiles and password-manager files
- the downloads folder

Explain *why* each one, briefly. The browser-profile and password-manager entries are the
ones readers have not thought about, and they are the ones that matter most, because an
agent that can read a browser profile can read live sessions. Frame the whole list as: the
question is not "would it do that" but "could it."

One paragraph on the boring but real part: a post-start script that keeps the runtime tidy —
one managed install, stale binaries removed — and documenting the expected warnings so
people stop filing them as bugs.

### Section 3 — Three permission tiers (~450 words)
The best-structured idea in the source material. Lead with the line:

> Deny is policy. Ask is judgement. Allow is speed.

Present it as a pattern with example rules, explicitly framed as "here is how to think
about the tiers," not as anyone's config:

**Deny — no prompt, ever.** Pushes. Cluster mutations. Context switches to anything
production-shaped. Infrastructure apply and destroy. Secret-manager reads. Reading private
keys and environment files. Editing environment files.

**Ask — a human decides each time.** Commits. Dependency installs and updates. Builds and
device commands. And the deliberate asymmetry worth its own paragraph: *reading* production
state — get, describe, logs — sits in ask, not allow. Reading production is still a
decision.

**Allow — no friction.** Status, diff, log. Search. Tests. Lint. Build. Analyze. Version
checks.

Then the two structural points:
- **Turn off the local escape hatch.** If an individual can opt out of the permission
  model, the permission model is a suggestion. This is one setting and it is the difference
  between policy and etiquette.
- **Deny is the only layer that does not depend on attention.** Ask-tier rules degrade under
  fatigue: the tenth prompt of the afternoon gets approved without reading. Anything you
  would regret approving at 5pm on a Friday belongs in deny.

Mention permission modes briefly (plan → default → accept-edits → don't-ask) and that
classifier-driven automatic modes still lose to hard deny rules.

### Section 4 — Hooks: the deterministic layer (~400 words)
Define it in one line: a hook is a shell command, HTTP call or tool invocation that fires
on a lifecycle event — the deterministic layer wrapped around a probabilistic agent.

Events worth wiring, each with the use case in a clause:
- **before a tool runs** — block a call outright
- **after a file edit** — format, lint or type-check the file just changed
- **after a failed command** — react instead of retrying blindly
- **at session start** — inject today's branch, ticket, or cache freshness as context
- **at stop / subagent stop** — refuse to finish while tests are red
- **on file or directory change** — react to an environment file or a repo switch

Then the exit-code contract, which is the whole API and takes three lines:
- `0` — success; stdout can add context for some events
- `2` — blocking error; stderr goes back to the agent to act on
- JSON on stdout — a structured decision with a reason

Give one worked example: a commit-message hook enforcing conventional commits plus a ticket
key, with the rule that if no key can be inferred, the agent must ask before committing.

```
feat(checkout): PROJ-1234 add attachment size validation
```

Close the section with the recommendation from the deck, which is genuinely the best
cost-to-value item in the whole series: **one post-edit hook per repo that runs that repo's
formatter and linter on the file just changed.** Twenty lines of shell, and it deletes an
entire category of review comment.

### Section 5 — The line you do not cross (~350 words)
The boundary slide, generalised into three columns:

- **Allowed** — approved local reads, read-only connectors, local workspace writes, drafts
  for humans to publish, test-environment checks when approved.
- **Human-owned** — tracker, chat, wiki and PR writes; commits, pushes and merges; deploys
  and production data writes; production cluster state; acceptance and go/no-go.
- **Never mounted** — the list from section 2.

Then runtime evidence, tying back to post 7: a runtime claim must name the environment
explicitly, the deployed image or tag, the pod or job state, the endpoint result, and a log
or monitoring signal.

Finish with the operational failure modes an agent will not think of, because this is
genuinely useful and rarely written about: overlapping scheduled jobs that are not
idempotent; caches that go stale after a deploy (application cache, rendered pages, service
workers, sitemaps); public query endpoints that amplify under crawlers; and
under-provisioned pods that pend or throttle.

### Close (~150 words)
State it plainly, as the deck does: the boundary is not distrust of the tool — it is what
lets you give the tool more work. Every exception has a written form: request, business
reason, systems and data touched, duration, rollback path, approver. Forward link to post 9.

---

## 4. Genericizing notes

**The most sensitive post in the series. Handle with care.**

- The deny/ask/allow lists are published as a **pattern with example rules**, framed in the
  second person ("here is how to think about the tiers"), never as "our configuration."
- Remove anything that maps a specific environment: no real cluster context names, no named
  integrations or third-party jobs, no internal document names, no monitoring vendor names —
  say "your error tracker" and "your metrics dashboard."
- The dev container JSON is a rewritten generic example.
- The commit example uses `PROJ-1234`.
- Do not state which specific systems are read-only *at a named company*. Describe the
  policy shape.

---

## 5. Verify before publishing

- Hook event names and the exit-code contract — check current docs; event naming has moved.
- Permission-mode names and the setting that disables the bypass mode.
- Whether classifier-driven automatic permission modes still behave as described.
- Dev container key names in the sample JSON must be valid.

---

## 6. Hero image brief

Trust motif: three concentric rounded rectangles labelled deny / ask / allow from outside
in, with a small agent glyph at the centre and four crossed-out key/credential icons outside
the outermost ring. Large "08".

---

## 7. Traps

- Do not present this as a security-theatre checklist. Every rule needs the failure it
  prevents.
- Do not publish anything that reads as a map of what is and is not protected in a real
  production environment.
- Do not overstate what a container prevents — it is a boundary, not immunity, and saying so
  buys credibility for everything else.
