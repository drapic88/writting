# Evidence needed

`VOICE.md` §1: every claim ends in a file path, a command, a number, a vote count, or a quote.
`CLAUDE.md`: never invent evidence.

The Musashi half of this book is sourced — 57 marked passages in `research/notes/`, every quotation
greppable against `research/source/`. The engineering half is not sourced at all. The first draft of
chapter 1 used invented composite scenarios, which is exactly what the one rule exists to exclude, and
it is being rewritten.

This file is the list of what has to come from Dragan before each chapter can be drafted. It is not a
questionnaire to be filled in neatly — two or three real answers with numbers attached are worth more
than ten sketched ones.

## The one that matters most

**A running example.** `books/CRAFT.md` §2 wants two or three examples that recur across the book.
One real system — something built, broken and changed over time — carried through Parts I to III
would do most of the work on its own, and would let several chapters below drop their individual asks.

Wanted: what it was, roughly how big, what it ran on, what went wrong with it, and what it looks like
now.

## Per chapter

| Ch | Working title | What is needed | Ideal shape of the answer |
|----|---------------|----------------|---------------------------|
| 1 | The nut and the flower | A decision where the option that was easier to explain won over the one that was better | The two options, who was in the room, what it cost afterwards |
| 2 | Choosing the timber | A real throwaway script, and ideally one that was not thrown away | The file, or what it did and how long it survived |
| 3 | Your ordinary week is your incident | An incident, preferably one that went badly | Timeline with clock times, what was missing that a normal Tuesday would have had |
| 4 | Cut and slash | A symptom fix shipped knowingly, and what happened later | The change, the reasoning at the time, whether it came back |
| 5 | Look at the ground first | Terrain numbers from a real system | Deploy duration, rollback time, suite runtime, review queue length — before and after if it improved |
| 6 | Holding the initiative | A change that only became fundable because something broke | What was asked for and refused, what broke, what then shipped |
| 7 | When you are stuck | A debugging session that went three wrong ways before the right one | The three hypotheses in order, what finally broke it open |
| 8 | Why study what you will never use | A tool or framework depended on past its range | What could not be done without it, and how that was discovered |
| 9 | Speed is not a quality | A metric optimised at the expense of the thing it measured | The metric, the number before and after, what got worse |
| 10 | The counterfeit | An "it depends" that turned out to be not-knowing | Honest answer only; `VOICE.md` §2 wants one self-implicating admission per piece and this is its slot |

## Confidentiality

Anything from paid work goes through [`../../../CONFIDENTIALITY.md`](../../../CONFIDENTIALITY.md)
before it is drafted, not before it is published, and every real party gets a row in `LEDGER.md`.
