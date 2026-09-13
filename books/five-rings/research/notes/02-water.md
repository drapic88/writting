# Marks — The Water Book

Source: [`source/musashi/02-water.md`](../source/musashi/02-water.md)

The book of the individual practitioner. Musashi works from the inside out: spirit, then stance, then
gaze, then grip, then footwork, then technique. Roughly half of it is sword-specific mechanics that do
not transfer; the framing passages are among the best in the book.

---

## ★★★ Everyday stance is combat stance

> "In strategy your spiritual bearing must not be any different from normal. Both in fighting and in
> everyday life you should be determined though calm."

> "In all forms of strategy, it is necessary to maintain the combat stance in everyday life and to make
> your everyday stance your combat stance."

> "Learn what is written here; use this gaze in everyday life and do not vary it whatever happens."

**Reading** — Musashi repeats this three times in three different sections, which is his way of marking
something as essential. There is no special mode you enter when it matters. Whatever you will do under
pressure is whatever you have been doing all along, because pressure removes the ability to switch modes.

**Carries over** — This is the strongest idea in the Water Book for engineering and it has a precise
operational meaning: *the incident reveals your ordinary practice, it does not override it.* You will not
suddenly write careful commits during an outage. You will not suddenly have runbooks. You will not
suddenly start reading logs properly. Teams that behave differently in incidents than in ordinary weeks
are teams whose ordinary weeks are the problem. Practically: no "wartime" mode, no heroics as a
distinct gear, and the tools you rely on at 3 a.m. must be the tools you use on Tuesday afternoon.

---

## ★★★ Perception and sight

> "The gaze should be large and broad. This is the twofold gaze 'Perception and Sight'. Perception is
> strong and sight week."

> "In strategy it is important to see distant things as if they were close and to take a distanced view
> of close things."

**Reading** — Two distinct faculties. *Sight* registers what is physically in front of you. *Perception*
reads the situation — intent, structure, where this is going. Musashi ranks perception above sight and
tells you to invert the natural bias of attention, which pulls toward whatever is nearest and moving.

**Carries over** — Extremely well, and it is the best available description of what separates a senior
engineer from a fast one. Sight is the stack trace. Perception is knowing what class of bug this is
before you finish reading it. "Distant things as if close" is treating next year's scaling wall as
present. "A distanced view of close things" is refusing to be captured by the loudest current bug —
the exact failure of an on-call rotation that fights every page individually and never asks what keeps
generating pages.

The instruction to hold both is what makes it useful. Pure perception is architecture astronautics.
Pure sight is thrashing.

---

## ★★★ Fixedness is a dead hand

> "Grip the long sword with a rather floating feeling in your thumb and forefinger, with the middle
> finger neither tight nor slack, and with the last two fingers tight. It is bad to have play in your
> hands."

> "Generally, I dislike fixedness in both long swords and hands. Fixedness means a dead hand. Pliability
> is a living hand."

**Reading** — A grip must be simultaneously firm and adaptable, and the two are not a compromise between
each other — they are located in different fingers. Note that he condemns *both* failures: slack ("play
in your hands") and rigid ("fixedness"). This is a genuinely non-obvious piece of craft.

**Carries over** — Beautifully, and the finger-by-finger structure is the part worth stealing. A design
should be tight where it must not move — data model, invariants, contracts at the boundary — and loose
where the world will change: transport, presentation, vendors, policy. Engineers who fail do so at one
pole or the other. All-tight is the frozen system where every change is a migration. All-loose is the
configurable everything-engine that does nothing. "Pliability is a living hand" is the correct summary
of a codebase that is still changeable after five years.

---

## ★★★ Attitude—No Attitude

> "'Attitude No-Attitude' means that there is no need for what are know as long sword attitudes. Even so,
> attitudes exist as the five ways of holding the long sword."

> "Whatever attitude you are in, do not be conscious of making the attitude; think only of cutting."

> "Attitude in strategy on a larger scale is called 'Battle Array'... Fixed formation is bad."

**Reading** — The famous paradox, and it is not mysticism. The five stances are real and must be learned.
Once learned, they are not things you *adopt* — they are positions you pass through on the way to the
objective. Attention on the form is attention off the purpose. He is explicit that this comes *after*
mastery, not instead of it.

**Carries over** — This is the correct account of the relationship between patterns and engineering,
and it corrects the usual one in both directions. Design patterns, architectural styles, and
methodologies are worth learning properly — Musashi does not let you skip the five stances. But the
engineer who is *aware of doing MVC* is worse than one who has absorbed it and is thinking about the
user's problem. "Fixed formation is bad" is the argument against org-wide mandated architecture: the
shape should follow the engagement.

The practical test: if you can name the pattern you are applying while you apply it, you are still at
the stage of holding an attitude.

---

## ★★★ Cut and slash

> "To cut and to slash are two different things. Cutting, whatever form of cutting it is, is decisive,
> with a resolute spirit. Slashing is nothing more than touching the enemy. Even if you slash strongly,
> and even if the enemy dies instantly, it is slashing. When you cut, your spirit is resolved."

**Reading** — The distinction is not in the physical motion or even the outcome — Musashi says the enemy
may die either way — but in whether the action was committed. A slash that kills is still a slash. He is
describing intent as a property of the act itself.

**Carries over** — And this is where the real version of "resolute acceptance of death" lives, without
the death. Slashing is the fix that happens to work: the retry that made the symptom go away, the
timeout bumped until the error stopped, the null check added where the null came from. It may resolve
the ticket. It is still a slash, and the codebase accumulates them. Cutting is understanding the cause
and removing it.

The honest extension Musashi doesn't make: sometimes you slash on purpose, because the outage is now and
the cause is deep. The discipline is *knowing which one you just did* and writing it down.

---

## ★★ No design, no conception

> "In this method, when the enemy attacks and you also decide to attack, hit with your body, and hit with
> your spirit, and hit from the Void with your hands, accelerating strongly. This is the 'No Design, No
> Conception' cut. This is the most important method of hitting."

**Reading** — Action arriving without deliberation, from trained instinct rather than plan. Musashi calls
it the most important method, and it is only available after the long training described everywhere else.

**Carries over** — Partially, and it needs a guard. The real phenomenon is trained intuition: the
engineer who looks at a dashboard and says "it's the connection pool" before they can justify it, and is
right, because they have seen this shape three hundred times. That is worth naming and worth building.
The guard is that unearned intuition is just guessing with confidence, and software — unlike a duel —
usually gives you the option to check. Correct form: let the intuition choose where to look, then verify.

---

## ★★ Step by step walk the thousand-mile road

> "Deliberately, with a patient spirit, absorb the virtue of all this, from time to time raising your
> hand in combat. Step by step walk the thousand-mile road."

> "Today is victory over yourself of yesterday; tomorrow is your victory over lesser men."

**Reading** — The measure of progress is your former self. Musashi's second clause is competitive and
looks outward, but the first is the one he builds on, and it is placed first.

**Carries over** — Directly, and it is the answer to an industry that measures engineers against a
mythical peer. "Victory over yourself of yesterday" is a usable standard: is this codebase better than
last quarter, do I understand this system better than I did. The comparison to "lesser men" is the part
to drop — see the rejection at the end of [`01-ground.md`](01-ground.md).

---

## ★★ Do not just read

> "If you merely read this book you will not reach the Way of strategy. Absorb the things written in this
> book. Do not just read, memorise or imitate, but so that you realise the principle from within your own
> heart study hard to absord these things into your body."

> "Study this book; read a word then ponder on it. If you interpret the meaning loosely you will mistake
> the Way."

> Oral tradition: "Teach your body strategy."

**Reading** — Musashi distrusts his own medium. He says three times that the book is insufficient, and
what he wants is *bodily* knowledge — the kind that operates without retrieval.

**Carries over** — And it is a necessary warning for any derived book, including ours. Reading about
testing is not testing. Knowing the name of a code smell is not the ability to smell it. The engineering
equivalent of "teach your body strategy" is: the practice must become the thing you do when not thinking
about it — the reflex to write the failing test first, to read the error message rather than skim it, to
check the assumption rather than assume.

Any book in this tradition must state this about itself, or it is selling flowers.

---

## ★★ To become the rider — stab at the face

> "To stab at the face means, when you are in confrontation with the enemy, that your spirit is intent of
> stabbing at his face, following the line of the blades with the point of your long sword. If you are
> intent on stabbing at his face, his face and body will become rideale."

**Reading** — Sustained pressure at the point an opponent cannot ignore forces them into reaction, and a
reacting opponent has given up initiative. He is not describing a killing blow; he is describing how to
make one available.

**Carries over** — With reframing, since there is no opponent. The transferable core is: *apply constant
pressure at the thing that cannot be deferred.* In practice this is the forcing function — the
deprecation date, the failing build that blocks merge, the deleted fallback path. Systems and
organisations both drift indefinitely unless something is pointed at their face. Setting up a forcing
function is the legitimate engineering version.

---

## ★★ Many enemies

> "Observe their attacking order, and go to meet first those who attack first. Sweep your eyes around
> broadly, carefully examining the attacking order... Waiting is bad."

> "You must drive the enemy together, as if tying a line of fishes, and when they are seen to be piled
> up, cut them down strongly without giving them room to move."

**Reading** — Against many, the whole problem is order and geometry. Read who commits first, take them
in that sequence, and manoeuvre so the many become a line rather than a circle. Do not stand still, and
do not fight all sides at once.

**Carries over** — Very well, as the discipline of a bad week. Multiple simultaneous problems are handled
by sequencing, not by parallelism: sort by who *forces* action first, not by who is loudest. "Tying a
line of fishes" is arranging your work so problems arrive one at a time — batching interruptions,
serialising deploys, funnelling requests through one intake. "Waiting is bad" is the specific failure of
freezing when everything is on fire.

---

## ★ Chinese monkey's body / glue and lacquer

> "The Chinese Monkey's Body is the spirit of not stretching out your arms... the spirit is to go in with
> your whole body."

> "The spirit of 'Glue and Lacquer Emulsion Body' is to stick to the enemy and not separate from him...
> People tend to advance their head and legs quickly, but their body lags behind."

**Reading** — Two complementary faults of half-commitment: reaching with the arms while the body stays
back, and advancing the extremities while the trunk lags.

**Carries over** — As an image for partial migrations, which is where it earns its keep. The new system
is written (the arm extends), the old one still holds all the traffic (the body stays back), and the
organisation lives in the reach for two years. Musashi's diagnosis is exact: the failure is not speed,
it is that the mass didn't follow.

---

## ★ Mind the return stroke

> "When you have cut downwards with the longsword, lift it straight upwards; when you cut sideways,
> return the sword along a sideways path. Return the sword in a reasonable way."

**Reading** — Half of technique is recovery. The stroke is not finished when it lands; it is finished
when you are ready for the next one.

**Carries over** — Cleanly: the change is not done when it works. It is done when the system is ready
for the next change — cleanup merged, flag removed, dead branch deleted, docs corrected. Teams that
land features and never recover accumulate a codebase where every stroke starts from a worse position.

---

## ★ Yin-Yang foot

> "Yin-Yang foot means not moving only one foot. It means moving your feet left-right and right-left when
> cutting, withdrawing, or warding off a cut. You should not move on one foot preferentially."

**Reading** — Movement alternates; leading always with the same foot makes you predictable and unstable.

**Carries over** — Loosely but usefully, as the alternation between building and consolidating. The team
that only ships features hops on one foot; so does the team permanently refactoring. Musashi's point is
that these are the same motion, not a balance to be struck between rival goods.

---

## ★ Not fast

> "If you try to wield the long sword quickly you will mistake the Way. To wield the long sword well you
> must wield it calmly."

**Reading** — Speed pursued directly degrades technique. (Expanded at length in the Wind Book — see
"Speed in Other Schools" in [`04-wind.md`](04-wind.md), where it gets the fuller treatment.)

**Carries over** — Yes, but the good version is in the Wind Book. Recorded here for the cross-reference.

---

## ✗ Rejected — the five attitudes and five approaches

> "The five attitudes are: Upper, Middle, Lower, Right Side, and Left Side."
> "In the second approach with the long sword, from the Upper attitude cut the enemy just as he attacks..."

**Reading** — Concrete sword mechanics, several pages of them.

**Rejected** — as content, kept as *structure*. There is no engineering mapping for the Upper attitude,
and inventing one ("the Upper attitude is top-down design!") is the flowers Musashi warns about. What
does transfer is the observation that he insists on exactly five, refuses to enumerate more, and then
tells you to forget them. A derived book should have a small fixed vocabulary of concrete moves and
should resist the urge to grow it.

---

## ✗ Rejected — physical stance

> "Adopt a stance with the head erect... Do not roll your eyes nor allow them to blink, but slightly
> narrow them... Brace your abdomen so that you do not bend at the hips."

**Reading** — A precise physical description of how to stand.

**Rejected** — as literal content; there is no posture that makes you a better programmer, and ergonomic
advice dressed as philosophy is filler. What survives is only the sentence already marked above: make
your everyday stance your combat stance.
