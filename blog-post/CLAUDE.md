# Working in blog-post/

Technical blog posts written for Medium under Dragan Rapić's byline.

## Before writing or editing any draft

**Read [`../VOICE.md`](../VOICE.md) then [CRAFT.md](CRAFT.md).** The first is the voice for
everything in this repository; the second is what a Medium post specifically requires —
anatomy, length, workflow, pre-publish checklist. Do not draft from a
generic idea of what a technical blog post sounds like.

The single rule it all serves: **every claim ends in a file path, a command, a number, a
vote count, or a quote.** If a paragraph cannot point at anything, cut it or go find the
evidence.

## Process

- One post per folder: `plan.md` (drafting brief) → `article.md` (the Medium draft) →
  `hero.svg` + `hero.png`.
- **Write and agree `plan.md` before drafting `article.md`.** Do not jump straight to prose
  for a new post.
- [README.md](README.md) holds the post index and the Medium tags and publication targets.
- **Every post is an independent article.** No series note, no "next post" link, no
  cross-reference to another post in this folder. A concept the post leans on gets a short
  self-contained explanation inside the post, or gets left out.
- Internal material is genericized per [`../CONFIDENTIALITY.md`](../CONFIDENTIALITY.md)
  before it reaches a draft.
- Verify every version number, model name, flag and command against current docs. Source
  decks in this repo were written for July 2026 and some specifics have already moved.

## Editing existing drafts

Match the surrounding voice rather than improving it toward a house style. Two drafts are
finished and set the standard: `php-8.6-small-release/article.md` and
`context-is-the-product/article.md`.
