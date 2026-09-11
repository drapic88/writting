# Working in this repository

This is Dragan Rapić's writing workspace: Medium blog posts, narrative non-fiction stories
for his site, and books. English and Croatian, both as originals.

## Before writing or editing any draft

1. **Read [VOICE.md](VOICE.md).** It is the voice specification for everything here —
   the evidence rule, stance, sentence mechanics, devices, anti-patterns. Do not draft from a
   generic idea of what technical writing sounds like.
2. **Read the craft spec for the format** — [`blog-post/CRAFT.md`](blog-post/CRAFT.md),
   [`stories/CRAFT.md`](stories/CRAFT.md), or [`books/CRAFT.md`](books/CRAFT.md). Anatomy,
   length, workflow and checklist live there.
3. **If the piece is in Croatian, read [CROATIAN.md](CROATIAN.md)** as well. Croatian pieces
   are written in Croatian from the first sentence, never translated from an English draft.
4. **If any of it comes from real client work, read
   [CONFIDENTIALITY.md](CONFIDENTIALITY.md)** before drafting, not before publishing.

The single rule everything serves: **every claim ends in a file path, a command, a number, a
vote count, or a quote.** If a paragraph cannot point at anything, cut it or go find the
evidence.

## Process

- **The brief comes first and gets agreed before the draft.** `plan.md` → `article.md` for
  posts, `plan.md` → `story.md` for stories, `premise.md` → `outline.md` → `brief.md` →
  `draft.md` for books. Do not jump to prose for a new piece.
- One piece per folder, with its `hero.svg` / `hero.png` alongside.
- Skills in `.claude/skills/` encode these procedures: `write-blog-post`, `write-story`,
  `write-book`, `hero-image`, `voice-check`.

## Facts

Verify every version number, model name, flag and command against current documentation
before it goes in a draft. Source material in this repo was written for July 2026 and some
specifics have already moved. When something might have been renamed, describe the shape of
the capability rather than quoting a flag.

Never invent evidence. No made-up benchmark, no plausible-sounding version number, no
dialogue that was not said. A thinner piece is the correct outcome when the evidence is not
there.

## Editing existing drafts

Match the surrounding voice rather than improving it toward a house style. Two blog drafts
are finished and set the standard: `blog-post/php-8.6-small-release/article.md` and
`blog-post/03-context-is-the-product/article.md`.

## Git

One repository for all four formats. Branch and commit conventions come from the global
rules: feature branches, no commits to `main`, and commits only when explicitly asked for.
