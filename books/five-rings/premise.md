# Premise — Five Rings

## The claim

Miyamoto Musashi's *Go Rin No Sho* describes a craft practised under real consequences, and
stripped of its warrior imagery it is the most useful book on engineering judgement I have read.

## The reader

An engineer five or more years in, who has noticed that the hard parts of the job stopped being
technical a while ago — and who has already bounced off the "warrior mindset" genre, because
every book in it eventually asks them to treat a colleague as an enemy.

## What they can do at the end

Name the failure mode they are currently in, using a vocabulary that is small, concrete and
shared. Ten or so named moves — *holding down the pillow*, *choosing the timber*, *twice, never
three times*, *the nut and the flower* — that a team can say out loud in a design review and have
mean something specific rather than something admiring.

## Why me

> **GAP — this section is Dragan's to fill and the book does not go further without it.**
>
> `VOICE.md` §2 wants one engineer who did the work writing to one who is about to. `books/CRAFT.md`
> §1 says that if the honest answer here is thin, the book is a compilation and should be planned as
> one. What is needed: the incidents, migrations and decisions this book is actually drawn from.
> See `research/notes/EVIDENCE-NEEDED.md` for the specific asks, chapter by chapter.

## What it is not

- **Not a translation, and not an interpretation of Musashi.** It is a new book that took its
  structure from an old one and says so on the first page. Where Musashi is wrong for our purposes
  he is quoted and contradicted by name.
- **Not a book about war, battle, or enemies.** There is no enemy in software and this book does not
  invent one. Eight passages of the original were read, marked and deliberately dropped for this
  reason — see [`ADAPTATION.md`](ADAPTATION.md).
- **Not a management book.** The foreman carpenter appears, but the reader is the person holding the
  tools.

## The comparable shelf

| Book | What it does | What this one does differently |
|------|--------------|--------------------------------|
| *The Pragmatic Programmer* | A list of named practices, mostly technical, aimed at the individual | Takes the same "named practice" form but applies it to judgement and timing rather than technique, and admits where each practice is wrong |
| *A Philosophy of Software Design* | One coherent thesis — complexity — argued through code | Broader subject and no single thesis; closer to a set of tools than an argument |
| The "samurai/stoic wisdom for professionals" shelf | Borrows the atmosphere of an old text and asserts modern advice underneath it | States its adaptation rules up front, publishes what it rejected and why, and leaves one passage openly untranslated |

## A note on the craft spec

`books/CRAFT.md` is written for technical non-fiction, and this book strains two of its rules.
`VOICE.md` §1 — every claim ends in a file path, a command, a number or a quote — is satisfiable for
the engineering half of each chapter and for every Musashi quotation, but not for the philosophical
turn each chapter makes. The runnable-artefact rule in CRAFT §3 is satisfiable only as a practice the
reader performs, not as a script they execute.

Both are being treated as binding anyway, on the grounds that they are what stops this from becoming
the shelf it is trying to displace. Where a chapter cannot meet them, that is a signal the chapter has
no evidence and should be cut at outline stage.
