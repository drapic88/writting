# Book craft

**Read [`../VOICE.md`](../VOICE.md) first.** This file holds what a book adds on top of it:
the stage gates, the continuity discipline, chapter anatomy, and the rules for reusing
material that already exists as posts or stories.

Written for **technical non-fiction**, which is the likely first book. §9 is a stub for
fiction, to be filled in if that turns out to be the project rather than guessed at now.

The thing that makes a book hard is not the word count. It is that chapter 9 has to agree
with chapter 2 about what a word means, which example is running, and what was already
promised to the reader. That is what `LEDGER.md` is for, and it is the only part of this
process that cannot be skipped.

---

## 1. Stage gates

Four artefacts, in order. **Each one is agreed before the next is written.** A chapter
drafted without an agreed brief is a chapter that gets rewritten.

| Stage | File | What it settles |
|-------|------|-----------------|
| 1. Premise | `premise.md` | the claim, the reader, what they can do afterwards, why me |
| 2. Outline | `outline.md` | the chapter list, each with a one-line promise and its evidence source |
| 3. Brief | `chapters/NN-slug/brief.md` | what this chapter proves, with what, in what order |
| 4. Draft | `chapters/NN-slug/draft.md` | the prose |

### `premise.md` — one page, and it stays one page

- **The claim.** One sentence, with a verb, that the whole book argues. If it fits in a
  blog post title, good; if it cannot be said in one sentence, the book has no spine yet.
- **The reader.** Named by situation, not by job title. "An engineer who has adopted a
  coding agent, has had it go wrong twice, and now has to decide what to let it touch."
- **What they can do at the end** that they could not do at the start. Concrete and
  testable — a thing they can run, a decision they can make, a gate they can install.
- **Why me.** The work this comes out of. If the honest answer is thin, the book is a
  compilation and should be planned as one.
- **What it is not.** Three bullets of scope exclusion, written early, because scope creep
  in a book costs months rather than paragraphs.
- **The comparable shelf.** Two or three existing books it sits next to, and the sentence
  that says what this one does differently.

### `outline.md` — the chapter table

One row per chapter: number, working title, the **one-line promise** to the reader, the
**evidence source** (which project, which post, which story, which measurement), and target
words. A chapter with no evidence source is a chapter that will pad, and it gets cut or
merged at outline stage where it costs nothing.

Also in `outline.md`: the arc in three or four sentences — how parts build, and where the
reader is allowed to stop reading and still have got their money's worth.

### `brief.md` — per chapter

Same discipline as the blog `plan.md`: the angle, the thesis, the section-by-section
structure with the evidence each section rests on, what it deliberately leaves to another
chapter, and the target length. Add two book-specific fields:

- **Depends on:** which earlier chapters the reader must have read.
- **Pays off:** which forward promise from `LEDGER.md` this chapter resolves.

## 2. `LEDGER.md` — the continuity file

One per book, updated **in the same session the chapter is drafted**, not at the end. Five
tables:

| Table | Columns | Why |
|-------|---------|-----|
| Terminology | term · definition as first given · chapter · notes | so chapter 9 does not redefine what chapter 2 defined, or use a synonym |
| Running examples | example · introduced in · reused in · current state | a book has two or three examples that recur; readers notice when one mutates |
| Numbers and sources | claim · number · source · date checked | every figure in the book is re-checkable years later |
| Parties | real party · public alias · where used | the `../CONFIDENTIALITY.md` table, applied per book |
| Promises | "covered in chapter N" · made in · resolved | the most common failure in technical books — a forward promise that is never paid |

The rule that makes it work: **no term enters a draft that is not in the ledger, and no
forward promise is written without a row.** Both are one line of typing at the time and a
week of reconciliation at the end.

## 3. Chapter anatomy

A chapter is a long-form post with a memory. It inherits the anatomy in
[`../blog-post/CRAFT.md`](../blog-post/CRAFT.md) §1 with four differences:

1. **Cold open, no series note.** Start on the reader's problem — a scene, a quote, a number
   — in under 150 words.
2. **The promise, stated once**, matching the row in `outline.md` verbatim in meaning. The
   reader should be able to tell from the first page whether to read this chapter now.
3. **One worked example carried the whole way through.** Not five illustrations; one thing
   built, broken, and fixed across the chapter. This is the main structural difference from
   a post.
4. **The limits section is mandatory**, and it names the cases where the chapter's advice is
   wrong, not just incomplete.
5. **The handoff.** One paragraph: what the next chapter does with this, phrased so the
   reader who stops here still has something finished.

Sections are sentence case, same as posts. Every chapter carries at least one runnable
artefact — a command, a file, a script — and ends with something the reader can do before
opening the next chapter.

## 4. Word budget

| Book shape | Chapters | Words/chapter | Total |
|------------|----------|---------------|-------|
| Short practical | 8–10 | 3,000–4,000 | 30,000–40,000 |
| Standard technical | 12–16 | 4,000–6,000 | 55,000–90,000 |
| Reference-heavy | 16–20 | 3,000–5,000 | 60,000–95,000 |

Budgets are set in `outline.md` and tracked per chapter. A chapter 40% over budget is a
chapter with two theses in it — split it rather than cutting evenly.

## 5. Reusing posts and stories

Material from `blog-post/` and `stories/` is a legitimate starting point, and is **never
pasted.**

- Record the source in the chapter's `brief.md` (`Derived from: blog-post/context-is-the-product`), so a
  reader who followed the blog is not sold the same text twice.
- Strip every artefact of the original format: series notes, "in my last post", Medium tags,
  next-post links, the call to clap, the pitch of a standalone lede.
- Re-verify every number and version against current sources. A post from last year is a
  draft of an argument, not a source.
- Expand what a post had to compress. If the chapter is the post plus 200 words, the chapter
  has no reason to exist.
- A story used as a chapter opener keeps its scene discipline
  ([`../stories/CRAFT.md`](../stories/CRAFT.md) §3) and loses its standalone close.

## 6. Repository workflow

```
books/<book-slug>/
├── premise.md
├── outline.md
├── LEDGER.md
├── chapters/
│   └── NN-slug/
│       ├── brief.md
│       └── draft.md
└── manuscript/        assembled output, generated — never edited by hand
```

`_template/` holds the empty shapes. Assembly concatenates `draft.md` files in outline
order; anything hand-edited in `manuscript/` is lost on the next assembly, so fixes go back
into the chapter.

Croatian books are originals, not translations — [`../CROATIAN.md`](../CROATIAN.md). A
bilingual book is two books and gets two folders.

## 7. Front and back matter

Planned at outline stage, drafted last: introduction (what the book claims and who it is
for — written after the chapters, when you know), how to read this book, acknowledgements,
a glossary generated from the ledger's terminology table, further reading, and an index
decision. The introduction is not the premise document with nicer sentences; it is written
to be read by someone standing in a bookshop.

## 8. Pre-submission checklist

- [ ] Every chapter's promise in `outline.md` is paid in that chapter.
- [ ] `LEDGER.md` promises table has no unresolved rows.
- [ ] No term used before its ledger definition; no synonym drift.
- [ ] Running examples are consistent across every chapter that touches them.
- [ ] Every number re-verified against a source dated after the first draft.
- [ ] Confidentiality checklist passed for the whole manuscript, not per chapter.
- [ ] Every chapter has a limits section and a runnable artefact.
- [ ] Reused post and story material is rewritten, sourced in the brief, and expanded.
- [ ] Word budget per chapter within 20% of `outline.md`.
- [ ] Front matter written after the chapters, not before.
- [ ] `VOICE.md` §5 anti-patterns: zero occurrences across the manuscript.

## 9. Fiction — stub

Not filled in, deliberately. If the first book turns out to be fiction, this section gets
the equivalents of the above before drafting starts: premise and the dramatic question,
character bible, beat sheet or outline method, point of view and tense decisions, scene-level
craft, a continuity ledger reshaped for character and timeline, and a revision pass order.
`VOICE.md` §1–§2 do not transfer to fiction unchanged; that would need its own spec.
