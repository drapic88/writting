> **STATUS — superseded draft, do not edit.**
>
> Written before `../../../../VOICE.md` and `../../CRAFT.md` were read. It conflicts with the voice
> spec on five points: invented composite scenarios instead of sourced evidence (§1), impersonal
> instead of first person singular (§2), almost no contractions (§3), pseudocode where real code was
> available (§5), and a nine-section shape rather than one worked example carried through (CRAFT §3).
> It also predates `premise.md` and has no agreed `brief.md`.
>
> It is kept because the arguments and the Musashi readings in it are sound and are the content plan
> for chapters 1 and 2, which it splits into. The prose is raw material. See
> `../../research/notes/EVIDENCE-NEEDED.md` for what chapters 1 and 2 are waiting on.

---

# The Ground Book

Musashi begins with ground because everything else needs somewhere to stand. His first book is not about
sword technique. It is about what the craft is for, how a master builder thinks, how to choose a tool,
and how to tell whether the thing you are doing is the thing that matters.

This one is about the same. What the work actually is. Not what it looks like from outside, not what it
is rewarded as, not what it is called in the job description. What it is.

The shortest answer available: software that works, for people who need it, that can still be changed
next year. Everything in this book is an attempt to say what follows from that.

---

## The nut and the flower

> If we look at the world we see arts for sale. Men use equipment to sell their own selves. As if with
> the nut and the flower, the nut has become less than the flower.
>
> — *The Ground Book*

The nut is the part that works. The flower is the display around it.

Musashi is not against the flower. Read the passage carefully and he never says the display is bad — he
says the ranking has inverted. The schools he is describing still teach, still have students, still have
names on the door. What has happened is that they now optimise for what can be shown, and the fighting
has quietly become the pretext.

Our version is so ordinary that it is difficult to see. A team chooses a distributed architecture for a
product with four hundred users. Nobody involved is stupid, and no one lies. Each person has a reason,
and the reasons are technical. But the design that would have worked — one service, one database, one
deploy — is not a design anyone can present, and the design that cannot be presented loses to the one
that can. The system that results is real, and so is the maintenance burden, and so is the conference
talk.

The flower has legitimate work to do. Communicating a design is part of building it. A diagram that
makes a system legible to the next person is not decoration; it is the joint that holds two people's
understanding together. Documentation is not vanity. Neither is care about how something looks to a
user — for most software, how it looks *is* how it works. The fault is never display. The fault is
specifically the inversion: choosing the worse thing because the better one is harder to narrate.

The inversion is easiest to spot in yourself by asking what you would do if nobody would ever know. Not
as a moral test — as a diagnostic. If the answer differs from what you are about to do, the difference
is the flower, and you can now decide about it deliberately instead of accidentally.

**Practice.** Take the design decision you are currently closest to. Write one sentence saying what you
would build if the decision would never be discussed, reviewed, or written up. If it differs from your
plan, you have found the ranking. Decide which way it should go, on purpose.

---

## The foreman still cuts wood

> The foreman carpenter must know the architectural theory of towers and temples, and the plans of
> palaces, and must employ men to raise up houses. The Way of the foreman carpenter is the same as the
> Way of the commander of a warrior house.
>
> The foreman should take into account the abilities and limitations of his men, circulating among them
> and asking nothing unreasonable.
>
> — *The Ground Book*

Musashi's model of leadership is a carpenter who got promoted.

This is a sharper idea than it looks, because it refuses a split our industry treats as natural: the
technical track and the management track, two ladders, two kinds of person. The foreman is not a
different kind of person from the carpenter. He is a carpenter who now also plans, allocates, and knows
his people. His authority comes from the craft, not from the title, and if the craft goes, the authority
goes with it and only the title is left.

Two words in that passage do most of the work.

*Circulating.* The foreman walks the site. He is not receiving reports about the site. There is a
recognisable failure where a lead's picture of a system is assembled entirely from status updates, and
the picture is always cleaner than the system — because every report is a summary, and summaries lose
exactly the ragged parts that predict failure. The lead who has not read the code in a year is not
leading a codebase; they are leading a description of one.

*Asking nothing unreasonable.* This is the whole of estimation and planning in three words, and it
contains an obligation: to know what is reasonable you must know the work, and you can only know the
work by having done it and by walking the site. A plan that is unreasonable is not a hard plan. It is a
plan made by someone who has stopped being a foreman.

The exception is real and needs stating plainly. A large enough organisation genuinely requires people
whose full-time work is coordination, funding, and hiring, and those people cannot also be in the code.
That is a different job, honourably done, and pretending otherwise produces the manager who blocks a
merge queue on a Friday to prove they are still technical. Musashi's foreman runs a house, not a
province. What he says about the foreman is true at the scale where one person can still see the whole
building.

**Practice.** If you lead: this week, read one pull request all the way through in an area you do not
own, and change nothing. If you do not lead: identify one thing your lead believes about your system that
is cleaner than the truth, and tell them the ragged version.

---

## Choosing the timber

> Straight un-knotted timber of good appearance is used for the revealed pillars, straight timber with
> small defects is used for the inner pillars. Timbers of the finest appearance, even if a little weak,
> is used for the thresholds, lintels, doors, and sliding doors. Good strong timber, though it be gnarled
> and knotted, can always be used discreetly in construction. Timber which is weak or knotted throughout
> should be used as scaffolding, and later for firewood.
>
> — *The Ground Book*

Not everything you build deserves the same standard. Our field states this badly when it states it at
all, usually as a grudging admission that some code is not worth caring about. Musashi states it as
craft: the carpenter's skill is precisely in matching material to load.

Four kinds of timber, and all four are used.

**Revealed pillars** carry the building and are seen. The public API. The data model. The permission
check. The migration that rewrites the table. These get everything — tests, review, documentation, a
second pair of eyes, a rollback plan. Not because they are interesting, but because everything else
rests on them and because they are hard to change once anything depends on them.

**Inner pillars** carry load and are not seen. The internal service that three teams call. Small defects
are acceptable here; structural weakness is not. These get correctness and tests, and can go without
polish.

**Thresholds and doors** are handled constantly and seen constantly and carry almost nothing. The admin
tool. The internal dashboard. The CLI your team uses forty times a day. Musashi's instruction is
striking: use the *finest appearance* here, even if a little weak. The thing people touch every day
should be pleasant, and it does not need to be robust, because when it breaks a person is standing right
there.

**Scaffolding** holds the building up while it is being built and is then taken down and burned. The
one-off backfill. The migration script that runs once. The throwaway analysis that answers one question.
Write it fast, make it correct for the single case it will face, and delete it. The failure here is not
carelessness — it is the opposite. An engineer who spends a day making a run-once backfill script
elegant has done a day of work that will be burned, and has also created the risk that it will *not* be
burned, because a nice script invites reuse and scaffolding reused as a pillar is how buildings fall
down.

```
# scaffolding — delete after 2026-03 backfill
# no retries, no batching, no config: it runs once, watched, on one table
for row in table.scan():
    row.tier = derive_tier(row)   # if this crashes, fix the row and re-run
    row.save()
```

The comment is the whole discipline. It says what this is, and when it stops existing.

The obvious misuse of this section is as a licence: *this part doesn't matter, so I can be sloppy.* That
is not what the passage says. Every one of the four grades is *used*, deliberately, for what it can
bear. The weak timber is not thrown away — it becomes scaffolding, and then firewood. What Musashi
condemns is not sloppiness and not perfectionism; it is the inability to judge load. Uniform care
everywhere is not rigour. It is a carpenter who cannot tell a pillar from a door.

There is a second reading of this passage, which is about sorting people the same way — *those of poor
ability lay the floor joists.* That one is a description of a frozen society and not an insight, and it
is left in the seventeenth century where it belongs. People are not timber. They grow, they rotate, and
the junior on the joists this quarter is the person who owns the pillar in two years.

**Practice.** Name the four grades in your current system. Say out loud which files are revealed
pillars. Then find one piece of scaffolding that was never burned, and either burn it or promote it
honestly.

---

## The joints, not the sections

> The attainment of the carpenter is that his work is not warped, that the joints are not misaligned, and
> that the work is truly planed so that it meets well and is not merely finished in sections.
>
> — *The Ground Book*

Quality belongs to the assembled thing, not to its parts. This is the most common way that good people
produce a bad system.

The composite is familiar. Three teams, three services, each well built. Each has tests, each has an
owner, each is something the team that wrote it is right to be proud of. And the system is unreliable,
because when the middle service times out, the caller retries, and the retry is not idempotent, and
nobody owns that sentence. Every section is finished. The joint is not.

*Warped* is the exact word. Sections finished separately drift. Not through negligence — through
ordinary local decisions, each correct in its own context. One team adds a retry because their
dependency is flaky. Another changes a field from required to optional because a customer needed it. A
third starts returning 200 with an error body because their client library handles it better. None of
these is wrong. Together they are a system where nobody can say what happens when a request fails.

The joints in software are specific and can be listed. The API contract, including what is *not* in the
schema — ordering, nullability in practice rather than in the type, what an empty list means. Retry and
timeout semantics on both sides. Who owns the failure case between two teams. What happens during the
minutes when both old and new versions are running. Every one of these is a place where two things must
meet, and every one of them is typically nobody's ticket.

The exception: a joint can only be planed if the two sides can see each other. In organisations where
teams genuinely cannot coordinate — different companies, different continents, an acquisition — the
answer is not better joints, it is fewer of them. Move the seam somewhere it can be defended, or
collapse it entirely. Musashi's carpenter has the advantage of building one house.

**Practice.** Pick one boundary your work crosses. Write down what happens when the other side is slow —
not down, slow. If you cannot answer in one sentence, you have found a warped joint, and you have found
it before it found you.

---

## Two timings

> There is timing in everything. Timing in strategy cannot be mastered without a great deal of practice.
>
> From among the large and small things and the fast and slow timings find the relevant timing, first
> seeing the distance timing and the background timing. It is especially important to know the background
> timing, otherwise your strategy will become uncertain.
>
> — *The Ground Book*

Musashi distinguishes two rhythms. The immediate one belongs to the exchange in front of you. The
background one is larger and slower: the tempo of a career, an institution, a market, the thing the
exchange is happening *inside*. He says the background one matters more, and that people who read only
the immediate one make correct moves that add up to nothing.

This names something that is otherwise hard to talk about, which is how an engineer can be right and
ineffective at the same time.

A composite: a service is genuinely badly built. The abstractions are wrong, the tests are slow, the
on-call burden is real and measured. An engineer proposes a rewrite. Technically the case is airtight —
they have the numbers, they have the design, and everything they say about the current system is true.
The rewrite is approved, begins, and is abandoned nine months later at sixty percent, because a funding
round closed badly and half the team was reallocated. The company now runs two systems instead of one
and the on-call burden has doubled.

Nothing in the immediate timing was wrong. The reading of the background timing was absent.

Background timing is answerable, and it is mostly three questions. *Where is this company in its life* —
searching for a product, scaling one that works, defending one that is mature, or winding one down; each
makes a different kind of work correct. *Where is this codebase in its life* — is it still finding its
shape, or has it settled into something worth hardening. *Where are you in yours* — an engineer with
three months of credit in an organisation should spend it differently from one with three years.

The uncomfortable consequence is that a technically correct proposal can be the wrong proposal, and that
"but I was right" is not a defence. It is also freeing, because it means an idea rejected this quarter is
not a dead idea. Fords open and close, which is the Fire Book's subject. Here it is enough to know that
there are two clocks and that most people only read one.

**Practice.** Before the next significant piece of work you propose, write one sentence about each of
the three questions. If you cannot answer where your company is in its life, that is the finding.

---

## No favourite weapon

> You should not have a favourite weapon. To become over-familiar with one weapon is as much a fault as
> not knowing it sufficiently well. You should not copy others, but use weapons which you can handle
> properly. It is bad for commanders and troopers to have likes and dislikes.
>
> — *The Ground Book*

Three claims here, and the middle one is nearly always dropped when this passage is quoted.

The first is the obvious one: attachment to a tool is a defect independent of the tool's quality, because
an attachment makes the tool choose the problem. "I am a Rust developer" is a smaller claim than "I build
systems," and it silently filters which problems you accept — not by argument, but by which ones look
interesting.

The second is that Musashi condemns shallow familiarity *in the same sentence*, at equal weight. To
become over-familiar is as much a fault as not knowing it sufficiently well. This is not a
recommendation of breadth. The engineer who has used nine databases badly is not ahead of the one who
knows one deeply — they are the other failure. Both are described here, and the passage is useless if
you only carry the half that flatters you.

The third is quiet and practical: *use weapons which you can handle properly.* Your team's actual
competence is a legitimate input into a technology decision. Not a compromise, not a sad concession to
reality — an input, on the same footing as throughput and cost. A team that knows one boring database
well will build a better system on it than on the correct-in-the-abstract choice they will be learning
in production during their first incident.

The exception, stated so it cannot be used as an excuse: this does not license permanent avoidance of
anything new. "We can't handle it properly" is true on the first day of every tool anyone has ever
learned, and Musashi has already covered this two pages earlier — *everything is difficult at first;
bows are difficult to draw.* The question is not whether the team can handle it today. It is whether the
team will be handling it, on purpose, with time allowed, before the thing is load-bearing.

**Practice.** Name the tool you would defend in an argument without checking anything. That is the
favourite. Next time it comes up, make the case *against* it out loud and see whether you can.

---

## Every tool has a range

> The bow is tactically strong at the commencement of battle, especially battles on a moor, as it is
> possible to shoot quickly from among the spearmen. However, it is unsatisfactory in sieges, or when
> the enemy is more than forty yards away.
>
> From inside fortifications, the gun has no equal among weapons. It is the supreme weapon on the field
> before the ranks clash, but once swords are crossed the gun becomes useless.
>
> — *The Ground Book*

This is the best statement of "no silver bullet" available, and it is better than the usual one because
it explains the mechanism rather than the conclusion. Musashi does not say all weapons are equal. He says
each one has a band of engagement in which it dominates and outside which it is dead weight. The gun has
*no equal* — at its range. Past that, it is a heavy stick.

Every technology in our field has this shape, and the arguments we have about them are almost always
arguments between people standing at different distances.

A message queue is a gun. Inside its range — decoupling producers from consumers, absorbing bursts,
surviving a consumer being down — it has no equal, and the alternatives are all worse. Put it inside a
tight synchronous path where the caller needs an answer before it can return, and it is not merely
suboptimal; it is dead weight that has also cost you the ability to reason about ordering.

A cache is a bow: fast, cheap, effective at the opening, useless in a siege. It buys time against read
load. It buys nothing against a write-heavy path and it actively costs you when correctness matters more
than latency, because it has added a second copy of the truth.

The failure is never picking the wrong tool in the abstract. Nobody chooses a database they believe is
bad. The failure is carrying a tool outside its range — usually because it worked last time, at a
different distance, and the distance was never made explicit.

So make it explicit. The question that ends most of these arguments is not "is X good" but "what is the
range of X, and are we inside it." Two people who have written down the range rarely disagree for long.

**Practice.** For the main piece of infrastructure your work depends on, write down the two boundaries:
the situation where it is unmatched, and the situation where it becomes a liability. If you cannot write
the second one, you do not yet know the tool — you have a favourite.

---

## The arrow you can see

> One of the virtues of the bow is that you can see the arrows in flight and correct your aim
> accordingly, whereas gunshot cannot be seen. You must appreciate the importance of this.
>
> — *The Ground Book*

A weaker instrument you can watch beats a stronger one you cannot.

Musashi has just finished saying the gun is supreme at its range. Then he adds this, and it complicates
his own ranking, which is why the sentence is worth keeping: the bow is worse in almost every respect,
and it has one advantage that sometimes outweighs the rest. You can see the arrow, so the second shot is
informed by the first.

Two things follow, and they are the argument for most of modern operational practice.

The first is observability, and it is the reason a slower system you can see into outperforms a faster
one that is opaque. Not because speed does not matter, but because the opaque system's performance is
fixed at whatever it was on the day it shipped, and the visible one improves every time someone looks at
it. A team that can answer "why was that request slow" in four minutes will, over a year, end up with a
faster system than a team that started faster and cannot answer the question at all.

The second is about the size of moves, and it is less often stated. Prefer a sequence of actions you can
watch to a single action you cannot. A deploy that goes to two percent of traffic and can be reversed in
thirty seconds is a bow. A quarterly release of everything at once is a gun: more powerful in one sense,
and you will never know which of the ninety changes caused the thing that happened on Thursday. Feature
flags, canaries, incremental migrations, small commits, short-lived branches — these are all the same
idea, which is that correction is worth more than power when you are aiming at something you do not fully
understand. And you are always aiming at something you do not fully understand.

The exception: watching costs something. Instrumentation has runtime cost, canaries have coordination
cost, and small increments have overhead that is real and is sometimes larger than the risk being
managed. Not every change deserves a canary. But the calculation should be made about the change in
front of you, not settled once as a habit, and the habit almost always errs toward the gun, because
firing once feels finished.

**Practice.** Take the last change you shipped that surprised you. Ask what instrument would have shown
you the surprise before your users did — and whether it was that you lacked the instrument, or had it and
did not look.

---

## The nine rules

Musashi ends his first book with a list. It is the compressed form of everything he believes, and what is
remarkable about it is what is absent: nothing about courage, honour, loyalty, glory, or sacrifice. It is
a list about honesty, breadth, practice, attention, and economy.

Here it is, with what each line asks of someone who builds software.

> **Do not think dishonestly.**

Start here, because the rest is unavailable without it. The dishonesty that matters is not lying to
others; it is the ordinary, comfortable kind you practise on yourself. The feature is not "done." The
test does not test that. You do not know why it started working. You have not read the code you are
reviewing. Nobody catches you, which is exactly why it is first.

> **The Way is in training.**

Skill comes from repeated contact with the real thing, not from reading about it. This applies to the
book you are holding.

> **Become acquainted with every art.**

The disciplines next to yours. If you write code, learn what the operator's night looks like, what the
designer is deciding, what the data person cannot get from your schema. Most systems fail at the seam
between two specialities, and seams are only visible from both sides.

> **Know the Ways of all professions.**

One step further out: understand the work of the people your software is *for*. Not their requirements —
their work. What they are trying to get done, what they do when your software is down, which of their
problems you are actually solving. A large amount of bad software is built by people who have never
watched anyone use it.

> **Distinguish between gain and loss in worldly matters.**

Weigh cost against benefit, honestly, including the costs that are inconvenient to your preference. Most
engineering argument skips this step entirely and argues about correctness instead, because correctness
is more comfortable to argue about than trade-offs.

> **Develop intuitive judgement and understanding for everything.**

Build the taste that lets you smell a bad design before you can prove it is bad. This is real and it is
earned; it is also the thing most often counterfeited, which the last book of this one is about.

> **Perceive those things which cannot be seen.**

The load that has not arrived. The coupling that has no line in the diagram. The dependency nobody has
upgraded. The failure that has not happened yet and will. Everything expensive in this work is invisible
at the moment it is created.

> **Pay attention even to trifles.**

The warning you have stopped reading. The test that fails one time in thirty. The log line that says
something odd and is followed by nothing. Systems announce their failures well in advance, in small type,
and the announcement is almost always in something a team has agreed to ignore.

> **Do nothing which is of no use.**

The hardest, and the most ignored. Delete it. Do not build it. Do not attend it. The abstraction for the
second case that has not arrived, the configuration option nobody sets, the meeting that produces a
document nobody reads, the dashboard nobody opens, the process step that exists because of an incident in
2019. Musashi puts this last, and it is the only line on the list that gives you back the time to do the
other eight.

**Practice.** Take the list and mark the one you break most often. Not the one you find most interesting
— the one you break. That is your ground, and the next four books stand on it.
