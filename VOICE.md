# Voice

How Dragan Rapić writes. This governs **everything in this repository** — Medium posts,
stories for the site, and books. Read it before drafting anything, and check the finished
draft against it.

Derived from six hand-written articles on Medium (2020–2023) and the long-form drafts in
`blog-post/`, which represent where the writing has landed. **When the two disagree, the
drafts win.** The Medium pieces contribute the instincts worth keeping — a real trigger
event, named parties, plain process lists, no marketing register. The drafts contribute the
structure, the length, and the evidence discipline.

This file holds what does not change between formats: the evidence rule, the stance, the
sentence mechanics, the devices, and the anti-patterns. What *does* change between formats
— anatomy, length, workflow, checklist — lives in the craft spec for that format:

| Format | Craft spec |
|--------|-----------|
| Medium blog posts | [`blog-post/CRAFT.md`](blog-post/CRAFT.md) |
| Stories for the site | [`stories/CRAFT.md`](stories/CRAFT.md) |
| Books | [`books/CRAFT.md`](books/CRAFT.md) |

Writing in Croatian additionally requires [`CROATIAN.md`](CROATIAN.md). Anything drawn from
real client work additionally requires [`CONFIDENTIALITY.md`](CONFIDENTIALITY.md).

---

## 1. The one rule

**Every claim ends in a file path, a command, a number, a vote count, or a quote.**

If a paragraph asserts something and cannot point at anything, cut it or go find the
evidence. This is the rule the rest of the guide serves. It is what separates these posts
from the enormous volume of confident, sourceless technical writing they compete with.

Corollaries:

- Prefer `error_reporting=E_ALL` over "enable strict error reporting."
- Prefer "passed 33 to 0" over "was widely supported."
- Prefer "half a day to a day for a well-tested Laravel app on 8.4+" over "the upgrade is
  straightforward."
- Prefer a five-line code block over a sentence describing what the code would look like.
- If a version, flag or command name might have moved, check it or describe the *shape* of
  the capability instead. Never quote a flag from a months-old deck.

---

## 2. Stance

Write as one engineer who did the work, to another engineer who is about to.

- **First person singular.** "I", "the model I use", "why I care about this release." Use
  "we" only for something a specific team genuinely did together, and say who the team is.
  Never the editorial "we" that means "you".
- **Second person for the reader's situation.** "Somebody on your team has said this in the
  last month." "That number tells you whether this upgrade is an afternoon or a sprint."
- **Opinions stated as opinions, and stated.** "That second block is why I care about this
  release." "This is a genuinely good language feature." A post with no position is a
  changelog.
- **Admit what cost you time.** "It took me embarrassingly long to arrive at." "It is a
  result of the many tries and fails." This buys more credibility than any amount of
  authority-signalling, and it is the strongest inherited habit from the earlier articles.
- **Name the limits before the reader finds them.** Every feature section gets its gotcha
  and its limits. Every recommendation gets the case where it does not apply.
- **No hedge stacking.** "Roughly thirty deprecations" is a real estimate. "It could
  potentially be argued that this may impact some users" is noise. One qualifier per
  claim, maximum.

---

## 3. Sentence and paragraph mechanics

- **Short declarative sentences.** Vary length, but the load-bearing sentence is always
  short. "Nothing changed about the model. What changed is what was in front of it."
- **Paragraphs of 1–4 sentences.** A one-sentence paragraph is a hammer; use it for the
  turn, not for every line. Do not write in LinkedIn staccato.
- **Contractions, always.** "isn't", "won't", "you'd rather know". Formal register reads as
  translated-from-marketing.
- **Bold carries the term, not the emphasis.** Bold the concept the reader should leave
  with (`**Instructions**`, `**Retrieved**`, `**Delegated**`) and the one number that
  matters. Three or four bolds per section, not fifteen.
- **Italics for provenance, book-titles and a single stressed word.** *clean*, *instead
  of*.
- **Em dashes for the aside that sharpens the point** — sparingly, one per paragraph at
  most.
- **Backticks for every identifier**: file paths, commands, flags, class names, branch
  names. `dev`, `staging`, `master`, `scripts/prepare-review.sh`, `Time\Duration`.
- **Second-person imperatives in playbooks.** "Bump the version. Make deprecations
  visible. Count the lines."
- **British/American:** be consistent within a post; the existing drafts lean British
  ("behaviour", "colour") in prose while keeping American spelling inside quoted code and
  API names. Match whatever the previous published post did.

---

## 4. Devices that work in this voice

Use these deliberately, not all at once.

- **The named persona.** "Let me tell you the story of John." A concrete engineer hitting
  the problem, given a name and two sentences of context. The single best device in the
  hand-written articles — keep it, but resolve the story later in the post rather than
  abandoning the character after the lede.
- **The overheard quote as blockquote.** `> "It was great last week. Now it keeps making
  things up."` Opens a post faster than any explanation.
- **The aphorism.** "Changes in the past always catch you in the future." Earn one per
  post, put it near the top or at the very end, never both.
- **Before/after code pairs.** Two blocks, same task, with the comment inside the code
  doing the pointing (`// PHP 8.5: the pipeline is drowning in arrow functions`). More
  persuasive than a paragraph of comparison.
- **The quiz.** "Quick quiz on the standard library. `sleep()` takes seconds. `usleep()`
  takes microseconds…" Makes the reader feel the problem before you name it.
- **The asymmetry triad.** Three bullets that compress a model and end on the one that
  matters: fully control / partly control / the only mechanism that removes volume.
- **The cost estimate.** "Half a day to a day, and most of that is waiting on dependency
  updates." Readers are deciding whether to spend time; tell them how much.
- **Cross-links in parentheses.** "(If the phrase 'context window' is doing a lot of
  unexplained work here, [post 1](#) covers the mechanics.)" Serves the skimmer without
  derailing the paragraph.
- **The self-implicating admission**, once per post, maximum.

---

## 5. Anti-patterns

Instant-close openers and register violations. None of these appear in a draft.

**Openers**

- "AI is transforming software development" and every variant of an industry abstraction.
- "In today's fast-paced world…"
- "In this article, we will explore…"
- A rhetorical question as the first line.
- Defining a term the reader already knows before saying why they should care.

**Register**

- game-changer, leverage, unlock, seamless, robust, cutting-edge, revolutionary,
  supercharge, delve, dive in, harness, empower, best-in-class.
- "It's important to note that…" — if it is important, note it.
- "Let's dive in." / "Without further ado."
- Emoji in headings. Emoji anywhere, in practice.
- Exclamation marks outside quoted speech.
- The fake "we" that means "you should".
- Praising the technology instead of assessing it.

**Structure**

- A listicle with no thesis.
- A conclusion that only summarises what was already said.
- Sections of one paragraph each, strung together with no argument.
- Pseudo-code where real code was available.
- A promise in the lede the post never delivers.
- Padding to hit a word count. A tight 1,400 words beats a padded 2,200.

**Grammar slips to watch for** — these are recurring in the hand-written articles and
should not survive an edit: "going throw code" (through), "Bests Practice" (Best),
"the many tries and fails" (trial and error, unless the rough phrasing is doing deliberate
work), missing articles before nouns, and `robot.txt` for `robots.txt`.

---
