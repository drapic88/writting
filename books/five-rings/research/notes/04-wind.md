# Marks — The Wind Book

Source: [`source/musashi/04-wind.md`](../source/musashi/04-wind.md)

Nine criticisms of rival schools. It is the most immediately useful book for engineers, because it is a
catalogue of *failure modes of method* — how a discipline decays while its practitioners believe they are
improving. Musashi refuses to name the schools he attacks, which is a deliberate choice worth copying.

---

## ★★★ Why you must study other schools

> "Without knowledge of the Ways of other schools, it is difficult to understand the essence of my Ichi
> school."

> "It is difficult to know yourself if you do not know others. To all Ways there are side-tracks. If you
> study a Way daily, and your spirit diverges, you may think you are obeying a good Way but objectively
> it is not the true Way. If you are following the true way and diverge a little, this will later become
> a large divergence." *(stated in the Ground Book, previewing this one)*

**Reading** — The purpose of studying rivals is calibration, not refutation. A practice drifts, drift is
invisible from inside, and small early divergence becomes large later divergence. Comparison is the only
available instrument.

**Carries over** — Completely, and it is the argument for learning languages and paradigms you will never
ship. You cannot see your stack's assumptions from inside it; Haskell shows you what your type system
isn't doing, Erlang shows you what your error handling assumed, a different company shows you which of
your practices were universal and which were local habit. Musashi's drift model is exact for teams: no
single sprint's compromise is visible, and four years later the codebase is somewhere nobody chose.

---

## ★★★ Speed is not part of the Way

> "Speed is not part of the true Way of strategy. Speed implies that things seem fast or slow, according
> to whether or not they are in rhythm. Whatever the Way, the master of strategy does not appear fast."

> "Some people can walk as fast as a hundred or a hundred and twenty miles in a day, but this does not
> mean that they run continuously from morning till night. Unpractised runners may seem to have been
> running all day, but their performance is poor."

> "Really skilful people never get out of time, and are always deliberate, and never appear busy."

> "When your opponent is hurrying recklessly, you must act contrarily and keep calm. You must not be
> influenced by the opponent."

**Reading** — The best passage in the Wind Book. Speed is not a quality of action; it is an artefact of
being in or out of rhythm. Musashi's distance-runner argument is empirical, not moral: the person who
covers a hundred miles is not the person running hardest. And the marker of skill is *not appearing
busy*.

**Carries over** — With almost no adjustment, and it indicts something our industry does constantly.
Visible busyness is treated as throughput. The engineer typing furiously, the team with the packed
sprint, the company shipping constantly — Musashi's claim is that these are the unpractised runners, and
the evidence is on his side: the highest-output engineers usually look unhurried, because most of their
output came from not doing things.

"You must not be influenced by the opponent" is the specific discipline. Panic in an incident, or an
adjacent team's urgency, or a competitor's launch, will set your tempo unless you refuse it. Deranged
rhythm is how systems collapse — see "To know collapse" in [`03-fire.md`](03-fire.md).

---

## ★★★ There is no interior and no surface

> "There is no 'interior' nor 'surface' in strategy. The artistic accomplishments usually claim inner
> meaning and secret tradition... but in combat there is no such thing as fighting on the surface, or
> cutting with the interior."

> "When I teach my Way, I first teach by training in techniques which are easy for the pupil to
> understand... I gradually endeavour to explain the deep principle... according to the pupil's progress."

> "Accordingly I dislike passing on my Way through written pledges and regulations."

> "If you go into the mountains, and decide to go deeper and yet deeper, instead you will emerge at the
> gate."

**Reading** — Musashi rejects the entire structure of esoteric transmission: no secret inner teaching, no
initiation, no certificate. There is one body of knowledge, taught in the order a person can absorb it.
The mountain image is the sharpest thing in the book — pursue depth far enough and you come out at the
entrance, because the deepest teaching turns out to be the first one.

**Carries over** — This is the case against gatekeeping and against artificial complexity, made by
someone who was unambiguously an expert. Applied: no secret senior knowledge, only knowledge not yet
transferred. Distrust any explanation that cannot eventually be made simple. Distrust the architect whose
value depends on being the only one who understands the diagram. And distrust the elaborate solution —
"emerging at the gate" is what happens when a long investigation ends at "just add an index," and that
ending is a sign of depth, not shallowness.

"I dislike passing on my Way through written pledges and regulations" is a direct hit on process
maturity models, certification, and every attempt to make competence into a document.

---

## ★★★ Relying on the length of the sword

> "Some other schools have a liking for extra-long swords... relying on the virtue of its length, they
> think to defeat the enemy from a distance."

> "It shows the inferior strategy of a weak spirit that men should be dependent on the length of their
> sword, fighting from a distance without the benefit of strategy."

> "In my doctrine, I dislike preconceived, narrow spirit."

**Reading** — Note carefully what Musashi objects to. He says explicitly, "do not unconditionally dislike
extra-long swords... What I dislike is the inclination towards the long sword." The fault is dependence,
not the tool.

**Carries over** — The heavyweight framework, the enormous platform, the elaborate abstraction that must
be adopted whole. The tell is dependence: can this team solve the problem if the tool is unavailable? A
team that cannot write an HTTP handler without their framework has an inclination, not a capability. And
"fighting from a distance" is the specific failure of building layers of indirection so you never have
to touch the actual problem.

---

## ★★★ Fixing the eyes

> "Some schools maintain that the eyes shouls be fixed on the enemy's long sword. Some schools fix the
> eyes on the hands. Some fix the eyes on the face, and some fix the eyes on the feet... If you fix the
> eyes on these places your spirit can become confused and your strategy thwarted."

> "Footballers do not fix their eyes on the ball, but by good play on the field they can perform well.
> When you become accustomed to something, you are not limited to the use of your eyes."

> "In strategy, fixing the eyes means gazing at the man's heart."

**Reading** — Rival schools each prescribe a single fixation point, and every one of them is wrong,
because a fixed point is a blind spot everywhere else. The football analogy is Musashi's own and is
startlingly modern — expert attention is diffuse and predictive, not focused and reactive.

**Carries over** — Directly to metrics and monitoring, which is a field built almost entirely out of
fixing the eyes on one place. Every team that optimises a single number gets exactly that number and
nothing else: test coverage, velocity, p99, uptime, lines reviewed. Musashi's answer is not "use more
metrics" — it is that a trained practitioner reads the *situation*, and instruments serve that reading
rather than replacing it. "Gazing at the man's heart" translates as: watch for user impact and system
intent, not the nearest available number.

---

## ★★ Do not think of cutting strongly

> "You should not speak of strong and weak long swords. If you just wield the long sword in a strong
> spirit your cutting will be coarse, and if you use the sword coarsely you will have difficulty in
> winning."

> "Whenever you cross swords with an enemy you must not think of cutting him either strongly or weakly;
> just think of cutting."

> "If you rely on strength, when you hit the enemy's sword you will inevitably hit too hard. If you do
> this, your own sword will be carried along as a result. Thus the saying, 'The strongest hand wins', has
> no meaning."

**Reading** — Force is the wrong axis entirely. Thinking about *how hard* displaces thinking about
*whether it works*, and overcommitted force carries you out of position — the effort itself becomes the
vulnerability.

**Carries over** — Effort as a proxy for value, which is endemic. Hours worked, the heroic weekend, the
brute-force solution that "shows commitment." Musashi's mechanical point is the good one: excess force
carries your sword along, meaning the overcommitment leaves you worse positioned than before. The
all-nighter that ships the feature and leaves the team unable to work the following week is exactly
being carried along by your own stroke.

---

## ★★ Attitude is the spirit of awaiting an attack

> "What is known in the world as 'attitude' applies when there is no enemy."

> "Attitudes are for situations in which you are not to be moved. That is, for garrisoning castles, battle
> array... In the Way of duelling, however, you must always be intent upon taking the lead."

> "When you attack the enemy, your spirit must go to the extent of pulling the stakes out of a wall and
> using them as spears and halberds."

**Reading** — Formal position is for holding ground, not for engaging. Musashi allows it explicitly for
static situations, then denies it for live ones. The stakes-from-the-wall image is about converting
defensive structure into active means.

**Carries over** — As a critique of process that exists to be defensible rather than to work. Much
engineering ceremony is attitude: it looks correct, it is auditable, and it addresses no live problem.
Musashi's allowance matters — a castle *does* need a garrison, and regulated environments genuinely need
formal process. The failure is applying garrison posture to live work.

---

## ★★ Countering, evading, retreating as habit

> "By their study of strategy, people of the world get used to countering, evading and retreating as the
> normal thing. They become set in this habit, so can easily be paraded around by the enemy."

> "To aim for the enemy's unguarded moment is completely defensive, and undesirable."

**Reading** — The subtle claim: it is not that defence is wrong in a given exchange, but that repeated
defence becomes a *habit*, and a habitual defender has handed over the tempo permanently.

**Carries over** — Teams that only respond. Every quarter is incidents, escalations, and requests;
nobody chose any of it; each individual decision to respond was correct. Musashi's diagnosis is that the
habit is the problem, and the cure is not working harder at responding. It connects directly to the
three initiatives in [`03-fire.md`](03-fire.md) — such a team knows only reaction and has never learned
Tai no Sen, which is a form of *taking* the initiative inside an incoming attack.

---

## ★★ Footwork does not change

> "There are various methods of using the feet: floating foot, jumping foot, springing foot, treading
> foot, crow's foot... From the point of view of my strategy, these are all unsatisfactory."

> "In my strategy, the footwork does not change. I always walk as I usually do in the street."

> "I dislike floating foot because the feet always tend to float during the fight. The Way must be trod
> firmly."

**Reading** — Every specialised movement style is a habit that will appear when it is not wanted.
Musashi's alternative is deliberately unremarkable: walk normally. Note that he condemns "treading foot"
as a *waiting* method, so this is not a preference for slowness.

**Carries over** — The pair to "everyday stance is combat stance" from [`02-water.md`](02-water.md), and
it is the argument against special-case practices. The special deploy procedure used only for big
releases, the review standard applied only to important changes, the documentation written only for
audits. Each is a specialised gait; each fails when the situation is not the one it was designed for.
One ordinary process, used for everything, executed well.

---

## ★★ On not naming the schools

> "I could now continue by giving a specific account of these schools one by one... but I have
> intentionally not named the schools or their main points. The reason for this is that different branches
> of schools give different interpretations of the doctrines. In as much as men's opinions differ, so
> there must be differing ideas on the same matter."

**Reading** — A structural decision, not politeness. Named criticism becomes a dispute about the naming
and dates instantly; the failure mode outlives any particular school.

**Carries over** — And it is a direct instruction to any derived book. Criticise the *pattern*, never the
framework by name. "Some schools rely on the length of the sword" ages well; a chapter attacking a
specific 2020s framework is unreadable in five years and reads as partisanship immediately. It also
avoids Musashi's own worst trait — the passages where he stops describing and starts winning an argument.

---

## ★ Great and small go together

> "From olden times it has been said: 'Great and small go together.' So do not unconditionally dislike
> extra-long swords."

**Reading** — The self-correction inside the long-sword criticism. Musashi checks his own polemic.

**Carries over** — As a rule for the derived book itself: every criticism of a practice must carry the
conditions under which the practice is right. The microservice criticism must admit where microservices
are correct. Otherwise the book becomes another school selling flowers.
