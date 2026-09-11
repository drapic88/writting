# Story craft — narrative non-fiction

**Read [`../VOICE.md`](../VOICE.md) first**, and
[`../CONFIDENTIALITY.md`](../CONFIDENTIALITY.md) before a word of a story that came out of
paid work. This file holds what is specific to stories: what qualifies as one, its shape,
the scene discipline that separates it from a blog post, and the checklist.

A blog post argues a thesis and proves it. **A story reports what happened and lets the
reader draw the conclusion one sentence before you state it.** Same evidence rule, different
delivery: the evidence arrives as events rather than as exhibits.

---

## 1. What counts as a story here

Four things have to be true. If one is missing, it is a blog post with an anecdote on top —
write it as a blog post.

1. **A trigger event.** Something happened, at a moment, to someone. A call from the SEO
   partner. A build that went green on a branch nobody had touched in six weeks. An alert at
   02:14.
2. **A belief that turned out to be wrong.** Mine, usually. The story is the distance
   between what we thought was true and what was true.
3. **A turn.** The moment the wrong belief breaks. This is the load-bearing scene and it
   gets rendered in full, not summarised.
4. **A cost, in a number.** Hours, euros, incidents, a sprint, a customer. Without a number
   the story is a war anecdote and the reader can't calibrate whether it applies to them.

Things that are stories here: incidents, migrations, a process that took three attempts to
get right, a tool adopted and abandoned, a decision that looked cheap and wasn't, a piece of
automation that quietly saved a month.

Things that are not: a tutorial with a framing device, a product review, a retrospective
with no wrong belief in it, an opinion piece wearing a timeline.

## 2. Anatomy

```markdown
---
title: ...
description: ...
date: 2026-09-11
tags: [...]
lang: en
draft: true
hero: ./hero.png
---

# Title as a claim, or as the sentence someone said

### The specifics in one line

*Provenance and disclosure.*

![Alt text restating what happened](./hero.png)

<the cold open: one scene, 80-150 words>

...
```

Then, in order:

1. **Cold open — one scene, present in the room.** A line of dialogue, a timestamp, a
   terminal output. No context, no setup. The reader is dropped in.
2. **The cast and the stakes**, in two or three sentences. Roles, not names (see
   `../CONFIDENTIALITY.md` §2). What was running, who was on the hook, what it cost per hour
   when it was down.
3. **What we believed.** Stated flatly, in the past tense, without hindsight in it. The
   reader must be able to believe it too — if the wrong belief reads as obviously stupid,
   you have flattened it and the story has no tension.
4. **The middle: what we tried, in sequence.** Each attempt gets its evidence and its
   result. This is where the piece earns its length; it is also where padding hides. Every
   attempt that did not change the outcome gets one sentence, not a section.
5. **The turn.** Full scene. Time-stamped. The thing that actually broke the belief —
   a log line, a sentence from a colleague, a diff. Never summarised, never explained before
   it is shown.
6. **The cost.** The number, plainly, in its own short paragraph.
7. **What changed.** One concrete practice that exists today because of this. A file that
   is in the repo now. A gate that is in CI now. If nothing changed, say that — it is a
   better ending than a fake one.
8. **What I would still get wrong.** The limit. The version of this that would catch me
   again. One paragraph, no false modesty.

The close follows `VOICE.md`: restate in one compressed line, say what it adds up to, and
end on something the reader can do this week with a threshold that tells them whether they
are in this situation.

## 3. Scene versus summary

This is the one craft skill a blog post does not need, and the reason stories are worth
writing separately.

- **At least two moments rendered in real time.** The cold open and the turn, at minimum.
  Real time means: a timestamp, what was on screen, what was said, in what order. Under 200
  words each — a scene is a close-up, not a transcript.
- **Everything else is summary.** Three days of investigation is two sentences. A story that
  renders everything is a log file; a story that renders nothing is a postmortem.
- **Dialogue is quoted only if it was said.** Blockquote for a line someone actually said,
  reconstructed from memory and marked as such if it matters. Inventing plausible dialogue
  to smooth a scene is the line between non-fiction and fiction, and this repository is on
  one side of it.
- **Show the artefact, not a description of it.** The log line, the diff, the alert text,
  the three-word Slack message — in a code block, verbatim, scrubbed per
  `../CONFIDENTIALITY.md` §3.
- **Keep the tense straight.** Past tense for events, present tense for what is true now
  ("that gate is still in CI"). Do not drift into the historical present for drama.

## 4. Evidence inside a narrative

The rule from `VOICE.md` §1 does not relax because there is a plot. It changes shape.

| In a blog post | In a story |
|----------------|-----------|
| a benchmark table | the duration between two timestamps |
| a documentation link | the log line that contradicted the documentation |
| a code sample | the diff that shipped, and the one that was reverted |
| "teams typically…" | what this team did, and what it cost them |

Anything checkable that is public still gets a link, in a `### Sources` section — vendor
changelogs, CVEs, docs that were wrong, an RFC. Anything internal gets anonymised, not
vaguened: `PROJ-1234`, not "a ticket".

## 5. Devices that carry over, and one that doesn't

From `VOICE.md` §4, these do the most work in a story: the overheard quote as the opener,
the named persona (openly a device, resolved later in the piece and not abandoned after the
lede), the cost estimate, and the self-implicating admission — once.

The one that does **not** transfer: the numbered playbook. A story that stops to become a
seven-step guide has changed genre mid-piece. If the lesson is procedural enough to need
steps, the story is the lede for a blog post — write both and link them.

## 6. Anti-patterns

On top of the `VOICE.md` §5 list:

- **The hero narrative.** The one where I spot it, fix it, and am thanked. Nobody believes
  it and nobody learns from it. If I was the one who got it right, the story is about what I
  got wrong first.
- **The moralising close.** "And so we learned to always write tests." The reader draws the
  conclusion; you name the practice that changed and stop.
- **The villain.** A named role that comes out of the piece looking incompetent. See
  `../CONFIDENTIALITY.md` §2.
- **Invented dialogue and undisclosed composites.**
- **Suspense as a substitute for structure.** Withholding the cause to keep the reader
  reading, when the honest version — stated in the lede, per `VOICE.md` §2 — is stronger.
- **The retrospective voice.** "Looking back, the signs were all there." They were not, or
  you would have seen them. Write what you could see at the time.
- **Dramatised technical detail.** The alert did not "scream". The server did not "die a
  quiet death". It returned 503.

## 7. Format and length

| Story type | Words | Scenes | Shape |
|------------|-------|--------|-------|
| Field note | 800–1,200 | 1 | one trigger, one turn, one lesson |
| Standard story | 1,500–2,200 | 2–3 | the full anatomy in §2 |
| Long / multi-thread | 2,500–3,500 | 3–4 | two threads that converge; earns its length or gets cut |

Frontmatter fields as in §2. **The site does not exist yet** — these field names are a
sensible default (`title`, `description`, `date`, `tags`, `lang`, `draft`, `hero`) and are
the one thing to revisit when the site is built. Body content below the frontmatter is
plain Markdown with no site-specific components, so it survives whatever the site turns out
to be.

## 8. Repository workflow

One story per folder, mirroring the blog:

```
stories/NN-slug/
├── plan.md      the brief — agreed before drafting
├── story.md     the draft (English)
├── story.hr.md  a Croatian original, when there is one
├── hero.svg
└── hero.png
```

Write and agree `plan.md` first. `_template/` holds the starting shapes for both files.
Croatian pieces are originals, not translations — see [`../CROATIAN.md`](../CROATIAN.md).

## 9. Pre-publish checklist

- [ ] All four qualifiers from §1 are present, and the cost is a real number.
- [ ] The wrong belief is stated so the reader could have held it too.
- [ ] Two scenes rendered in real time, each under 200 words.
- [ ] The turn is shown before it is explained.
- [ ] Every quoted line was actually said; nothing invented is presented as recorded.
- [ ] Artefacts are verbatim and scrubbed; no dramatised technical detail.
- [ ] Confidentiality checklist passed, disclosure line present if anything was changed.
- [ ] No hero narrative, no villain, no moralising close.
- [ ] "What I would still get wrong" is there and is honest.
- [ ] Close ends on something actionable with a threshold.
- [ ] Sources section for anything public and checkable.
- [ ] Zero words from the `VOICE.md` §5 list.
- [ ] Read aloud once. Anything you would not say to a colleague, cut.
