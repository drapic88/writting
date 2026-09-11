# Plan — post 2: Chat Answers. An Agent Acts.

**Series:** *From Assistant to Agent*, part 2 of 10 (Foundations)
**Source:** "AI basic" deck, slides 5–10
**Status:** brief · not drafted

---

## 1. Positioning

### The angle
Most engineers' mental model of AI tooling is autocomplete plus a chat box. An agent is a
different category of thing — it plans, calls tools, reads the result and decides again —
and the practices that work for chat actively fail for agents. This post draws the line
and then walks one real session end to end.

### The thesis
> Chat gives you an answer you evaluate. An agent gives you a *process* you supervise. The
> change is not that it types faster — it is that you stop reviewing keystrokes and start
> reviewing checkpoints.

### Title options
1. **Chat Answers. An Agent Acts.** — short, memorable, sets the whole frame.
2. **The Difference Between an Assistant and an Agent Is Who Takes the Next Step** — long
   but very clear.
3. **You Stopped Reviewing Keystrokes. Now Review Checkpoints.** — best for a senior
   audience.

*Recommendation:* #1, subtitle "What changes when your AI tool can read your repo, run
your tests, and decide what to do next."

---

## 2. Meta

- **Length:** 1,500–1,800 words (6–7 min).
- **Audience:** engineers who have used a chat assistant and are about to be handed an
  agentic tool, plus leads deciding whether to roll one out.
- **Tags:** `AI`, `Software Engineering`, `Developer Tools`, `Programming`, `Productivity`
- **Series slot:** publish 3rd, after the two flagships — it is the natural "start here"
  post to link back to.

---

## 3. Structure

### Lede (~130 words)
Two transcripts side by side, same request. In the first, you get a suggested patch and
apply it yourself. In the second, the tool reads three files, edits one, runs the suite,
sees a failure, fixes it, and hands you a diff. Same model underneath. Completely
different job for you.

### Section 1 — The two modes, honestly compared (~350 words)
Use the deck's contrast, but write it as prose with a compact table, not two bullet lists.

| | Chat | Agent |
|---|---|---|
| You provide | a question and context | a goal and boundaries |
| It produces | one reply | a sequence of tool calls |
| Reaches your files | no | yes, if you let it |
| Your role | evaluate an answer | approve at checkpoints |
| Fails by | being confidently wrong | being confidently wrong *and acting on it* |

That last row is the honest one and the reason the rest of the series exists. Say plainly
that chat is still the better tool for explaining, drafting and brainstorming — this is not
a "chat is obsolete" post.

### Section 2 — What an agent can reach for (~400 words)
Six capability categories, one short paragraph each, each with a concrete "you'd use this
when" line:
- **Tools** — read/write files, run shell commands, search the repo, execute tests.
- **Subagents** — separate sessions for isolated research or review (forward-reference
  post 5).
- **Skills** — packaged procedures loaded on demand (forward-reference post 6).
- **MCP connectors** — reach outside systems: issue trackers, chat, databases, internal
  APIs.
- **Hooks** — deterministic scripts that fire around the agent's actions
  (forward-reference post 8).
- **Git awareness** — branches, commits, PR descriptions.

Keep every forward-reference to a single clause. This section is a map, not the territory.

### Section 3 — One session, five phases (~400 words)
The deck's lifecycle, written as a narrative with a real fictional ticket
(`PROJ-1234`, "checkout submits twice on slow networks"):

1. **Understand** — reads the ticket, the relevant files, and the project's instruction
   file before touching anything.
2. **Plan** — for anything nontrivial, proposes the plan and waits. This is the cheapest
   place to redirect it (post 4).
3. **Implement** — edits, runs commands, iterates against real test output rather than its
   own guess about the output.
4. **Verify** — runs the suite and the linter, re-reads the diff, and reports what it ran.
   Name the standard here: evidence, not "done" (post 7).
5. **Hand off** — drafts the commit message and PR body. The merge stays human.

Include a short terminal-style block showing the loop, in the shape of the deck's example
but with the fictional stack.

### Section 4 — Choosing a model as a cost decision (~200 words)
Frame it as speed vs depth vs price, not as a leaderboard: a compact fast model for
high-volume mechanical work, a mid-tier agentic model for everyday coding and tool use, a
flagship for high-stakes reasoning, and a deep-reasoning model for long-horizon refactors.

**Do not list model names or version numbers from the deck** — see the verification list.
Describe the tiers; name the current line-up only if checked on the day of publishing.

### Section 5 — What does not change (~200 words)
Prompting practices that survive the jump, from the deck's slide 10, compressed hard
because this ground is saturated on Medium. Keep four:
- Specify the outcome, not the vibe: "the checkout button submits twice on slow networks —
  add a debounce and a regression test."
- Give context, not only instruction. It can search; it cannot know what you already know.
- Ask for a plan on anything multi-part.
- Show an example of the shape you want.

Then the guardrails from slide 11 in two sentences: no secrets or customer data in a
prompt, no unattended destructive commands, generated output is a draft.

### Close (~130 words)
The reframe: your job moved from producing every keystroke to designing the boundaries and
checking the evidence. Link forward to post 3.

---

## 4. Genericizing notes

- Use the shared fictional stack from the root `README.md`.
- The security do/don't list is generic industry advice — safe to publish as-is. Do **not**
  reproduce the internal wording about which specific systems are human-owned; that is
  post 8's material and needs the pattern framing.

---

## 5. Verify before publishing

- **Model names.** The deck is stale (Opus 4.8 / Fable 5). Current: the Claude 5 family —
  Fable 5.1, Opus 5, Sonnet 5 — plus Haiku 4.5. Either use current names or describe the
  tiers generically. Never copy from the deck.
- Check that the capability names (skills, subagents, MCP, hooks) still match current
  product vocabulary.

---

## 6. Hero image brief

Foundations motif, split composition: left half a single speech bubble with one arrow out;
right half the same bubble feeding a small loop of four nodes (read → act → check →
decide). Large "02".

---

## 7. Traps

- Do not write another "50 prompt engineering tips" section. Four practices, tightly
  written, then move on.
- Do not oversell autonomy. Every claim about what an agent does should be paired with the
  checkpoint where a human intervenes.
- Do not let the forward-references bloat — one clause each, or the post loses its shape.
