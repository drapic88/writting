# Books

Long-form projects. No book chosen yet — this is the scaffold, written for technical
non-fiction, with a fiction stub in [CRAFT.md](CRAFT.md) §9 to be filled in if that turns
out to be the project.

- **Craft spec:** [CRAFT.md](CRAFT.md) — stage gates, the continuity ledger, chapter
  anatomy, reuse rules, word budgets.
- **Voice:** [`../VOICE.md`](../VOICE.md).
- **Anything from paid work:** [`../CONFIDENTIALITY.md`](../CONFIDENTIALITY.md).
- **Croatian:** [`../CROATIAN.md`](../CROATIAN.md). A bilingual book is two books.

## Layout

```
books/<book-slug>/
├── premise.md     the claim, the reader, the payoff — one page
├── outline.md     chapter table: promise + evidence source + words
├── LEDGER.md      continuity: terms, examples, numbers, parties, promises
├── chapters/NN-slug/{brief.md, draft.md}
└── manuscript/    assembled output — generated, never hand-edited
```

`_template/` holds empty versions of all four. Copy it to start a book:

```bash
cp -R books/_template books/<book-slug>
```

## Stage gates

Premise → outline → chapter brief → chapter draft. Each agreed before the next is written.
A chapter drafted without an agreed brief is a chapter that gets rewritten.

## Projects

| Book | Stage | Chapters drafted | Words |
|------|-------|------------------|-------|
| — | *none started* | — | — |
