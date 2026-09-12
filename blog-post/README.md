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
whatever is worth writing about. The table is an index, not a sequence.

| Folder | Working title | Words | Status |
|--------|---------------|-------|--------|
| `php-8.6-small-release` | PHP 8.6 Is a Small Release With a Big Warning Label | 3,000 | **drafted** |
| `context-is-the-product` | Your AI Didn’t Get Worse. Your Context Did. | 2,100 | **drafted** |
| `how-llms-actually-work` | Your LLM Has No Memory. It Has a Window. | 1,200–1,500 | **drafted** |
| `chat-vs-agent` | Chat Answers. An Agent Acts. | 1,500–1,800 | **drafted** |
| `plan-before-you-let-it-code` | The Readiness Gate Is the Cheapest Bug Fix You Own | 1,700–2,000 | **drafted** |
| `subagents-and-parallelism` | Subagents Buy Context Isolation, Not Speed | 1,900–2,200 | plan |
| `skills-beat-long-prompts` | Stop Retyping Procedures. Commit Them. | 1,600–1,900 | plan |
| `evidence-over-assertion` | "Done" Is Five Separate Claims | 2,100–2,400 | plan |
| `design-the-blast-radius` | The Container Is the Security Model, Not the Prompt | 1,900–2,200 | plan |
| `the-agent-as-a-unix-tool` | An Agent You Can Pipe Into `jq` | 1,600–1,900 | plan |
| `automating-the-boring-half` | A Tip Nobody Installs Is Not a Tip | 1,700–2,000 | plan |

The briefs written before this convention changed still contain instructions to link
forward and back between posts. Those instructions are superseded; the note at the top of
each brief says so.

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
