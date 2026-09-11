# Stories

Narrative non-fiction for Dragan Rapić's own site: true accounts from real work — incidents,
migrations, decisions that cost more than they looked like they would. AI and technology
subjects, told as what happened rather than argued as a thesis.

- **Craft spec:** [CRAFT.md](CRAFT.md) — what qualifies as a story, its anatomy, the scene
  discipline, the checklist.
- **Voice:** [`../VOICE.md`](../VOICE.md), shared with every other format here.
- **Anything from paid work:** [`../CONFIDENTIALITY.md`](../CONFIDENTIALITY.md), before
  drafting.
- **Croatian pieces:** [`../CROATIAN.md`](../CROATIAN.md). Originals, not translations.

## Layout

One story per folder, numbered in the order they were started:

```
stories/NN-slug/
├── plan.md      the brief — agreed before drafting
├── story.md     the draft (English)
├── story.hr.md  a Croatian original, when there is one
├── hero.svg
└── hero.png
```

`_template/` holds the starting `plan.md` and `story.md`.

## Index

| # | Folder | Working title | Type | Words | Status |
|---|--------|---------------|------|-------|--------|
| — | — | *nothing drafted yet* | — | — | — |

## Publishing

The site does not exist yet. Frontmatter (`title`, `description`, `date`, `tags`, `lang`,
`draft`, `hero`) is a sensible default to be reconciled with the site when it is built; the
body is plain Markdown with no site-specific components, so it survives that decision.

A story and a blog post can share a subject. They do not share text — the story is the
account, the post is the argument, and each links to the other.
