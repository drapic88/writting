---
name: write-blog-post
description: Draft or edit a technical blog post for Medium under Dragan Rapić's byline. Use for "write a post about X", "draft the plan for the sandboxing post", "edit this article", "is this article ready to publish", anything landing in blog-post/. Enforces brief-before-draft and the repository's voice.
---

# Writing a Medium blog post

## Read first, every time

1. [`VOICE.md`](../../../VOICE.md) — the voice. Non-negotiable.
2. [`blog-post/CRAFT.md`](../../../blog-post/CRAFT.md) — post anatomy, length, folder
   workflow, pre-publish checklist.
3. [`blog-post/README.md`](../../../blog-post/README.md) — the post index, the Medium tags
   and the publication targets.
4. [`CONFIDENTIALITY.md`](../../../CONFIDENTIALITY.md) — if any of it comes from real client
   work.
5. [`CROATIAN.md`](../../../CROATIAN.md) — if the post is in Croatian. Croatian posts are
   written in Croatian from the first sentence, never translated from an English draft.

Do not draft from memory of what these say. Read them.

## The gate

**`plan.md` is written and agreed before `article.md` exists.** If asked to "write a post"
and there is no agreed brief, write the brief and stop. Existing briefs in
`blog-post/*/plan.md` show the shape — positioning, meta, section-by-section structure,
evidence, out of scope.

If a `plan.md` is already in the folder, it is agreed. Draft from it and say which brief you
are working from. Briefs written before September 2026 carry instructions to link forward
and back between posts; those are superseded — see the note at the top of the brief.

## Workflow

1. **Locate or create the folder.** `blog-post/slug/` — a plain slug, never numbered.
2. **Brief.** Write `plan.md`. Name the thesis, the evidence that backs each section, and
   what the post deliberately leaves out. Stop here and get agreement.
3. **Gather evidence before prose.** Every section needs its file path, command, number,
   vote count or quote already in hand. A section you cannot evidence gets cut at brief
   stage, not padded at draft stage.
4. **Verify the facts.** Version numbers, model names, flags, command names — against
   current documentation, not against the source decks in this repo, which were written for
   July 2026. If a flag may have been renamed, describe the shape of the capability instead.
5. **Draft `article.md`** against the anatomy in `CRAFT.md` §1.
6. **Hero image.** Use the `hero-image` skill.
7. **Check.** Run the `voice-check` skill, or work the checklist in `CRAFT.md` §4 yourself.
   Report what fails; do not silently fix voice by flattening it.

## Rules that override convenience

- **Never invent evidence.** No plausible version number, no illustrative benchmark, no
  quote that was not said. Say the evidence is missing and let the post be thinner.
- **No pseudo-code where real code was available.** Go get the real thing.
- **Match the surrounding voice when editing**, rather than improving a draft toward a house
  style. `php-8.6-small-release/article.md` and `context-is-the-product/article.md` are
  the standard.
- **Every post stands alone.** No series note, no "next post" link, no "(post 1 covers the
  mechanics)". A concept the post leans on gets a short self-contained explanation inside
  the post, or gets left out. Links point outward, to documentation and sources.
- Nothing gets committed unless Dragan asks for a commit.
