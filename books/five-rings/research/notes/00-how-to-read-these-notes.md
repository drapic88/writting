# How to Read These Notes

## What these files are

`notes/` contains a close reading of Miyamoto Musashi's *Go Rin No Sho* (*The Book of Five Rings*, 1645),
in the translation shipped in the EPUB at the repository root. The plain-text source is in
[`source/musashi/`](../source/musashi/), one file per book.

There is one notes file per book of the original:

| Notes file | Source | Musashi's subject |
|---|---|---|
| [`01-ground.md`](01-ground.md) | [`01-ground.md`](../source/musashi/01-ground.md) | Foundations — what strategy *is*, and the carpenter analogy |
| [`02-water.md`](02-water.md) | [`02-water.md`](../source/musashi/02-water.md) | The individual practitioner — stance, grip, gaze, technique |
| [`03-fire.md`](03-fire.md) | [`03-fire.md`](../source/musashi/03-fire.md) | Conflict — initiative, tempo, position, breaking a deadlock |
| [`04-wind.md`](04-wind.md) | [`04-wind.md`](../source/musashi/04-wind.md) | Criticism of rival schools — how methods go wrong |
| [`05-void.md`](05-void.md) | [`05-void.md`](../source/musashi/05-void.md) | Mastery beyond method |

## The marking scheme

Each note is a marked passage. The format is:

> **Mark title** — a short name for the idea, used as a stable reference elsewhere in the project.
>
> A quotation from the source, verbatim.
>
> **Reading** — what Musashi is actually claiming, in plain modern language.
>
> **Carries over** — whether and how the idea survives translation into software engineering,
> including where it *doesn't*.

Marks are graded:

- ★★★ — load-bearing. The idea is the point of the book, and it transfers to engineering directly.
- ★★ — strong. Transfers with a small amount of reinterpretation.
- ★ — worth keeping. Interesting, narrow, or transfers only as an analogy.
- ✗ — recorded and rejected. The passage is famous or tempting but does not survive translation.
  These are marked deliberately, because a book of borrowed philosophy fails mostly by keeping what it should drop.

## An honest note on the source

Musashi wrote a manual for killing people with a sword, at sixty, having killed at least sixty men.
He is not writing metaphor. When he says "cut the enemy," he means it literally, and he is explicit
that everything decorative or theoretical in a fighting school is a lie people tell to sell lessons.

That literalism is the reason the book transfers well and the reason it must be handled carefully.
It transfers well because the pressure he writes under — real consequences, no partial credit, no
audience to impress — is the same pressure that separates working software from demos. It must be
handled carefully because software engineering has no enemy, and most of the damage done by
"warrior mindset" writing in our industry comes from inventing one. See [`../context/03-adaptation-rules.md`](../context/03-adaptation-rules.md)
for the rules this project uses to keep that line.
