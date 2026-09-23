# Blog posts

Each post lives in its own folder containing `plan.md` (drafting brief), `article.md`
(the Medium draft) and `hero.svg` / `hero.png` (the lead image).

**Every post is an independent article.** No series, no numbering, no reading order. A
reader arrives at one post from search or a share, so a post never opens with a "part N"
note, never closes with a link to the next one, and never sends the reader elsewhere in this
folder to finish an idea. Where two posts touch the same concept, each explains the part it
needs, in its own words, as briefly as its own argument allows.

---

## The posts

Derived from two internal talks — an introductory "Using AI" briefing and a 30-slide
advanced workshop on coding, QA, DevOps and daily automation — plus standalone pieces on
whatever is worth writing about.

The table is ordered by **publishing order** — the sequence to ship them in, not a reading
order. Nothing in a post depends on an earlier one; a reader arriving at #9 from search gets
a complete argument. The order exists because publishing is sequential and the first posts
have to carry the ones behind them.

| # | Folder | Working title | Words | Status |
|---|--------|---------------|-------|--------|
| 1 | `context-is-the-product` | Your AI Didn’t Get Worse. Your Context Did. | 2,100 | **published** |
| 2 | `how-llms-actually-work` | Your LLM Has No Memory. It Has a Window. | 1,200–1,500 | **published** |
| 3 | `chat-vs-agent` | Chat Answers. An Agent Acts. | 1,500–1,800 | **published** |
| 4 | `php-8.6-small-release` | PHP 8.6 Is a Small Release With a Big Warning Label | 3,000 | **published** |
| 5 | `plan-before-you-let-it-code` | The Readiness Gate Is the Cheapest Bug Fix You Own | 1,700–2,000 | **drafted** |
| 6 | `subagents-and-parallelism` | Subagents Buy Context Isolation, Not Speed | 1,900–2,200 | **drafted** |
| 7 | `evidence-over-assertion` | "Done" Is Five Separate Claims | 2,100–2,400 | **drafted** |
| 8 | `design-the-blast-radius` | The Container Is the Security Model, Not the Prompt | 1,900–2,200 | plan |
| 9 | `skills-beat-long-prompts` | Stop Retyping Procedures. Commit Them. | 1,600–1,900 | plan |
| 10 | `the-agent-as-a-unix-tool` | An Agent You Can Pipe Into `jq` | 1,600–1,900 | plan |
| 11 | `automating-the-boring-half` | A Tip Nobody Installs Is Not a Tip | 1,700–2,000 | plan |

### Why this order

**1–4 are published and 5–7 are drafted.** The drafts ship as written; only 8–11 need
drafting time, so the order also keeps a publishable post in hand while the next brief is
still a brief.

- **#1 `context-is-the-product` opens** because it is the most differentiated post in the
  folder — Medium is saturated with prompt tips and near-empty on context design — and its
  title is the highest click-through of the eleven. The first post is the one that has to
  find readers with no audience behind it.
- **#2 `how-llms-actually-work` follows** as the explainer with the widest search surface.
  It is the shortest post here, it answers the question #1 raises for a reader who has never
  thought about the window, and it is the one most likely to keep earning traffic a year on.
- **#3 `chat-vs-agent`** draws the category line — answer you evaluate, process you
  supervise — which is the frame every practice post after it assumes.
- **#4 `php-8.6-small-release` is time-boxed and everything else is not.** PHP 8.6 GA is
  **19 November 2026**; the post is worth the most in the weeks either side of that date and
  loses value steadily after. It went out in the run-up; the beta-era specifics still need a
  refresh at GA. It also breaks the AI cadence and pulls a different audience, which is a second
  reason to place it here rather than at the end.
- **#5 `plan-before-you-let-it-code` and #6 `subagents-and-parallelism`** are the first two
  practice posts, in that order: the readiness gate is the cheaper, more universal
  intervention, and the subagents post is mildly contrarian — worth more to readers who have
  already tried the thing and seen the token bill.
- **#7 `evidence-over-assertion`** is the strongest post in the folder and the strongest
  title, so it closes the run of drafted posts before the briefs begin. It is deliberately not #1: "Done Is Five
  Separate Claims" lands hardest on a reader who is already running agents, which is the
  audience the first six build.
- **#8 `design-the-blast-radius`** reaches outside the usual readership — security reviewers
  and the people who have to answer them — so it is best published once there is something
  behind it to link to from a profile.
- **#9–#11 are the narrowing tail.** `skills-beat-long-prompts` needs the reader to already
  keep procedures somewhere; `the-agent-as-a-unix-tool` is for CI and platform people;
  `automating-the-boring-half` is about compounding and distribution, which is the idea that
  reads best last, to an audience that has adopted something.

Publishing order is an editorial decision and nothing in the drafts encodes it. Reorder it
freely — move a post up when its subject is suddenly live, or when a brief is ready earlier
than planned.

The briefs written before the standalone convention changed still contain instructions to
link forward and back between posts. Those instructions are superseded; the note at the top
of each brief says so.

---

## Shared conventions

### Genericizing the source material

The talks were internal. Every **pattern** carries over to the public posts; every
**identifier** is replaced. The substitution table, the rules for people, dates and numbers,
and the pre-publish check live in [`../CONFIDENTIALITY.md`](../CONFIDENTIALITY.md) — they
apply to stories and book chapters too, so they are kept in one place. Use the aliases
consistently, so a reader who happens to read two of these posts sees one coherent stack
rather than a new disguise each time.

### Facts to re-verify at drafting time

The source deck was written for July 2026 and some specifics have already moved:

- **Model line-up.** The deck lists Opus 4.8 / Fable 5 / Sonnet 5 / Haiku 4.5. Current is
  the Claude 5 family — Fable 5.1, Opus 5, Sonnet 5 — plus Haiku 4.5. Never copy model
  names from the deck.
- **Feature maturity.** Agent teams (experimental), GitLab CI/CD support (beta),
  `/ultraplan`, `/batch`, `/goal`, advisor and fast mode all need a docs check before a
  post asserts they exist and how. Prefer describing the *shape* of a capability over
  quoting a flag that may have been renamed.
- **Anything plan-gated.** Some session controls vary by plan. Say so rather than
  promising availability.

Rule for every post, inherited from the workshop: **every claim ends in a file path, a
command, or a piece of evidence.** If a paragraph can't, cut it.

### Voice

See **[`../VOICE.md`](../VOICE.md)** for the voice and **[CRAFT.md](CRAFT.md)** for the
post format. In short: thesis in the title, honest framing in the lede, short declarative
sentences, real code over pseudo-code, opinions stated as opinions. No "AI is transforming
software development" openers — instant close.

### Medium meta

- **Tags** (5 per post): core set `AI`, `Software Engineering`, `Programming` plus two
  post-specific from `LLM`, `Developer Tools`, `DevOps`, `Testing`, `Software Testing`,
  `Security`, `Automation`, `Productivity`, `Coding`.
- **Publications.** Self-publish first, then submit to *Level Up Coding*, *ITNEXT* or
  *Better Programming*.
- **Canonical.** If any of these also go on a company blog, publish there first and use
  Medium's import so the SEO doesn't split.

### Hero images

One visual system across the posts so they read as the same author's work: same typeface,
same two-colour palette, the same composition. **No post number and no series label** — the
mono-caps line above the title names the post's own subject. The diagram carries that post's
actual claim, not a decorative motif. Authored as `hero.svg` on a 1400×650 viewBox and
exported to `hero.png` at 2× (2800×1300), which is what the finished heroes in this repo
actually are. The `hero-image` skill has the palette, the type stack and the export step.
