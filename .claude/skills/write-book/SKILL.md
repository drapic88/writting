---
name: write-book
description: Work on a book in books/ — premise, outline, chapter brief, or chapter draft, plus the continuity ledger that keeps chapters agreeing with each other. Use for "start a book about X", "draft chapter 4", "outline the book", "does chapter 9 contradict chapter 2", or turning existing posts and stories into chapters. Enforces the stage gates and ledger discipline.
---

# Working on a book

What makes a book hard is not the word count. It is that chapter 9 has to agree with chapter
2 about what a term means, which example is running, and what was already promised.

## Read first, every time

1. [`VOICE.md`](../../../VOICE.md) — the voice.
2. [`books/CRAFT.md`](../../../books/CRAFT.md) — stage gates, the ledger, chapter anatomy,
   reuse rules, word budgets.
3. **The book's own `LEDGER.md`** — before writing a single sentence of any chapter. This is
   the step that gets skipped and it is the one that costs a month at the end.
4. [`CONFIDENTIALITY.md`](../../../CONFIDENTIALITY.md) — for anything from real work.
5. [`CROATIAN.md`](../../../CROATIAN.md) — for a Croatian book. A bilingual book is two
   books and two folders.

## The stage gates

Premise → outline → chapter brief → chapter draft. **Each is agreed before the next is
written.** Identify which stage the request is at and work at that stage only.

- Asked to "write chapter 4" with no `brief.md`? Write the brief and stop.
- Asked to "write the book" with no `premise.md`? Write the premise and stop.
- Starting a book: `cp -R books/_template books/<book-slug>` and fill `premise.md`.

## Workflow for a chapter

1. **Read `outline.md`** for this chapter's promise, and `LEDGER.md` for the terms, examples
   and forward promises already in play.
2. **`brief.md`** — thesis, the one worked example carried through the chapter, section
   structure with the evidence each rests on, limits, new terms, handoff. Get agreement.
3. **Add the new terms to `LEDGER.md` before drafting**, not after.
4. **Draft `draft.md`** against `books/CRAFT.md` §3. One worked example, a mandatory limits
   section, at least one runnable artefact, and a handoff paragraph.
5. **Update `LEDGER.md` in the same session** — terms, examples, numbers and sources,
   parties, promises made and promises resolved. Never defer this.
6. Report word count against the budget in `outline.md`.

## Reusing posts and stories

Material from `blog-post/` and `stories/` is a starting point and is **never pasted**. Record
the source in the brief, strip every trace of the original format (series notes, "in my last
post", Medium tags, standalone closes), re-verify every number, and expand what the post had
to compress. A chapter that is the post plus 200 words has no reason to exist.

## Rules that override convenience

- **No term in a draft that is not in the ledger.** No synonym drift.
- **No forward promise without a ledger row.** Unresolved rows block submission.
- **Never invent evidence**, and re-verify anything carried from a post written earlier.
- **`manuscript/` is generated.** Fixes go back into the chapter, never into the assembly.
- Nothing gets committed unless Dragan asks for a commit.
