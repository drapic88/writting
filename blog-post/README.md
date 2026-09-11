# Blog posts

Each post lives in its own folder containing `plan.md` (drafting brief), `article.md`
(the Medium draft) and `hero.svg` / `hero.png` (the lead image).

---

## Series: *From Assistant to Agent*

A ten-part series on running coding agents inside a real, governed codebase — derived
from two internal talks: an introductory "Using AI" briefing and a 30-slide advanced
workshop on coding, QA, DevOps and daily automation.

The series arc: understand the machine → learn to work with it → make it trustworthy
enough to hand real work to.

### Reading and publishing order

Publish order is **not** numeric order. Post 3 is the strongest opener for subscribers;
posts 1–2 are broad-reach on-ramps that link *down* into the series.

| # | Folder | Working title | Arc | Words | Status |
|---|--------|---------------|-----|-------|--------|
| 1 | `01-how-llms-actually-work` | What Actually Happens When You Prompt an LLM | Foundations | 1,200–1,500 | plan |
| 2 | `02-chat-vs-agent` | Chat Answers. An Agent Acts. | Foundations | 1,500–1,800 | plan |
| 3 | `03-context-is-the-product` | Your AI Didn’t Get Worse. Your Context Did. | Craft ★ | 2,100 | **drafted** |
| 4 | `04-plan-before-you-let-it-code` | The Readiness Gate Is the Cheapest Bug Fix You Own | Craft | 1,700–2,000 | plan |
| 5 | `05-subagents-and-parallelism` | Subagents Buy Context Isolation, Not Speed | Craft | 1,900–2,200 | plan |
| 6 | `06-skills-beat-long-prompts` | Stop Retyping Procedures. Commit Them. | Craft | 1,600–1,900 | plan |
| 7 | `07-evidence-over-assertion` | "Done" Is Five Separate Claims | Trust ★ | 2,100–2,400 | plan |
| 8 | `08-design-the-blast-radius` | The Container Is the Security Model, Not the Prompt | Trust | 1,900–2,200 | plan |
| 9 | `09-the-agent-as-a-unix-tool` | An Agent You Can Pipe Into `jq` | Trust | 1,600–1,900 | plan |
| 10 | `10-automating-the-boring-half` | A Tip Nobody Installs Is Not a Tip | Trust | 1,700–2,000 | plan |

**Recommended publish order:** 3 → 7 → 2 → 8 → 5 → 4 → 1 → 6 → 9 → 10.
Lead with the two flagships while enthusiasm is high, then use the foundations posts to
catch search traffic and funnel it back.

★ = flagship. These two carry the series; give them the extra editing pass.

---

## Shared conventions

### Genericizing the source material

The talks were internal. Every **pattern** carries over to the public posts; every
**identifier** is replaced. The substitution table, the rules for people, dates and numbers,
and the pre-publish check live in [`../CONFIDENTIALITY.md`](../CONFIDENTIALITY.md) — they
apply to stories and book chapters too, so they are kept in one place. Use the aliases
consistently across all ten posts so a reader following the series sees one coherent stack.

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

Rule for the whole series, inherited from the workshop: **every claim ends in a file
path, a command, or a piece of evidence.** If a paragraph can't, cut it.

### Voice

See **[`../VOICE.md`](../VOICE.md)** for the voice and **[CRAFT.md](CRAFT.md)** for the
post format. In short: thesis in the title, honest framing in the lede, short declarative
sentences, real code over pseudo-code, opinions stated as opinions. No "AI is transforming
software development" openers — instant close.

### Medium meta

- **Tags** (5 per post): core set `AI`, `Software Engineering`, `Programming` plus two
  post-specific from `LLM`, `Developer Tools`, `DevOps`, `Testing`, `Software Testing`,
  `Security`, `Automation`, `Productivity`, `Coding`.
- **Series linking.** Every post opens with a one-line series note and closes with a
  "next in the series" link. Update the links as posts go live — a dangling promise to a
  post that doesn't exist yet costs more than it gains.
- **Publications.** Self-publish first, then submit to *Level Up Coding*, *ITNEXT* or
  *Better Programming*.
- **Canonical.** If any of these also go on a company blog, publish there first and use
  Medium's import so the SEO doesn't split.

### Hero images

One visual system across the series so the posts read as a set: same typeface, same
two-colour palette, the post number rendered large, and a single diagram motif per arc
(Foundations = token stream, Craft = layered window, Trust = evidence chain). Authored as
`hero.svg` on a 1400×650 viewBox and exported to `hero.png` at 2× (2800×1300), which is what
the finished heroes in this repo actually are. The `hero-image` skill has the palette, the
type stack and the export step.
