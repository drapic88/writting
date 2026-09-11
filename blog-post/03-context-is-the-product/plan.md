# Plan — post 3: You Are Not Writing Prompts. You Are Curating a Window.

**Series:** *From Assistant to Agent*, part 3 of 10 (Craft) — **FLAGSHIP**
**Source:** advanced workshop deck, slides 3, 5, 12
**Status:** brief · not drafted

---

## 1. Positioning

### The angle
The single highest-leverage idea from the workshop, and the one that is genuinely
underwritten on Medium. Everyone is publishing prompt tips. Almost nobody is writing about
the fact that a prompt is a small fraction of what is in the window when the model decides
— and that the rest of it is yours to design.

### The thesis
> Context is the product. You are not writing prompts; you are curating what is in the
> window at the moment the model decides. Nearly every "the agent got worse" complaint is
> a context problem: a bloated session, a stale instruction file, or a subagent that read
> forty files it did not need.

### Title options
1. **You Are Not Writing Prompts. You Are Curating a Window.** — the thesis, verbatim.
2. **Your AI Didn't Get Worse. Your Context Did.** — highest click-through, slightly
   clickbait-adjacent but defensible.
3. **Context Is the Product** — cleanest, weakest on its own.

*Recommendation:* #2 as the title, #1 as the subtitle. That pairing gets the click and then
immediately states the real idea.

---

## 2. Meta

- **Length:** 2,000–2,400 words (9–10 min). The longest of the craft posts; it earns it.
- **Audience:** engineers already using an agent daily who have hit the wall where results
  degrade and they cannot say why. Assume they know what an instruction file is.
- **Tags:** `AI`, `Software Engineering`, `Developer Tools`, `Programming`, `Coding`
- **Series slot:** **publish first.** This is the post that earns subscribers.

---

## 3. Structure

### Lede (~180 words)
Open on the complaint, quoted the way people actually say it: "it was great last week, now
it keeps making things up." Then the reframe — nothing about the model changed; the window
changed. Name the three sources of context and promise the habits that follow.

### Section 1 — Three sources, one window (~450 words)
The core diagram of the post. Everything in the window at decision time comes from exactly
three places:

- **Instructions** — the files you commit: root and per-repo agent instruction files,
  scoped rule files, and whatever the tool accumulates as automatic memory. Loaded whether
  or not you thought about them today.
- **Retrieved** — files you or the agent read, command output, connector results. The
  volatile majority.
- **Delegated** — summaries handed back by subagents instead of raw search hits and log
  dumps. Context you deliberately did *not* let in.

Make the asymmetry explicit: you fully control the first, partly control the second, and
the third is the only one that *removes* volume while keeping the conclusion. That framing
is what makes delegation feel like a context technique rather than a performance trick.

### Section 2 — Layer your instructions, narrowest wins (~500 words)
Four levels, from the deck's slide 5, with the reasoning for each boundary:

1. **Workspace root** — operating boundary, evidence rules, commit format, repo map.
   Loaded every single turn, so length has a direct running cost.
2. **Per repo** — layer rules, test commands, framework conventions that travel with the
   code.
3. **Scoped rules** — loaded on demand. This is where anything conditional belongs, and
   it is how the always-on root file stays short.
4. **Automatic memory** — what the tool learned on its own. Review it; it is context you
   did not consciously write.

Give a real example of a root file that is actually short — five or six rules, in the
generic form:

```md
# Working agreement
- Start in plan mode for unclear tickets.
- No feature code before requirements, acceptance criteria, architecture impact,
  a test plan, risk and rollback exist.
- Identify the exact nested repo first — the workspace root is not a repo.
- Ask before commits, dependency updates, migrations and deploys.
- Issue-tracker, chat and wiki writes stay human-owned.
```

Two non-obvious points worth their own short paragraphs:
- **A long root file is a tax on every turn.** If it is conditional, it does not belong
  there.
- **Editing the instruction file mid-session may not take effect** because of prompt
  caching. Restart after editing. This is the kind of detail that makes readers trust the
  post.

### Section 3 — Four habits that follow (~400 words)
Each habit stated as an imperative, then the failure it prevents:

- **A fresh session per task.** Do not carry yesterday's window into today's ticket. The
  failure it prevents: the agent confidently applying a convention from an unrelated
  refactor.
- **Delegate anything read-heavy.** Only the conclusion should land in your window
  (forward-link post 5).
- **Compact deliberately, at a clean boundary — never mid-refactor.** Compaction is
  lossy; choosing *when* it happens is the whole skill.
- **Precision beats volume.** One exact file beats a repo-wide search. A hundred matches
  is not context, it is noise with line numbers.

### Section 4 — Stop guessing, inspect (~300 words)
The diagnostic move that turns "it feels worse" into a finding. Describe the class of
introspection commands and what each answers, generically enough to survive renames:

- what is currently loaded into context
- a full environment checkup
- what is burning your usage limits
- which hooks fired
- connector/server status

Then a short worked diagnosis: results degrade → check what is loaded → discover the
session is carrying a 3,000-line generated file read two tasks ago → start fresh, read the
one file that matters, problem gone. This narrative is the most persuasive thing in the
post; give it real detail.

### Section 5 — The hard case: a workspace that is not a repo (~350 words)
From slide 12. A folder holding six independent repositories, monorepo-shaped but not a
monorepo. Why agents trip on it constantly: they infer a single project, branch at the
wrong level, and read across boundaries that should be closed.

```
workspace/            # NOT a git repo
  agent-guidelines/
  web-app/            # own repo + instruction file
  rest-api/
  admin-app/
  mobile-app/
  marketing-site/
  infra/
```

Four rules that prevent the classic failures: branch inside the repo that will change;
check status first because these checkouts usually hold unrelated active work; keep a
per-repo instruction file so test commands travel with the code; switch repos with a fresh
session rather than dragging context across.

### Close (~150 words)
Restate: the model is not the variable you control day to day. The window is. Then the
forward link to post 4.

---

## 4. Genericizing notes

- Use `agent-guidelines`, `web-app`, `rest-api`, `admin-app`, `mobile-app`,
  `marketing-site`, `infra` from the root `README.md`. Never the real repo names.
- The root-file example above is a rewrite, not a quote. Keep it that way.
- Do not name the employer. "A workspace I work in every day" is enough.

---

## 5. Verify before publishing

- Introspection commands: check current names before quoting any of them. Prefer
  describing what each answers, with the command as an aside.
- The prompt-caching claim about mid-session instruction edits — verify it still holds and
  state it as behaviour you have observed if docs are silent.
- Automatic memory behaviour varies by tool and version; hedge accordingly.

---

## 6. Hero image brief

Craft motif, and the best visual in the series: a rectangle labelled "context window"
filled with three stacked bands (instructions / retrieved / delegated) in the two series
colours, the delegated band drawn much thinner than the raw material feeding it, with a
funnel narrowing into it. Large "03".

---

## 7. Traps

- Do not turn this into a list of commands. The mental model is the product; commands are
  citations.
- Do not repeat post 1's explanation of what a context window is — link back in one clause.
- Do not claim numbers ("40% fewer tokens") that were not measured.
- Resist adding subagent detail beyond one clause; post 5 owns it.
