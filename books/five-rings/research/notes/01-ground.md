# Marks — The Ground Book

Source: [`source/musashi/01-ground.md`](../source/musashi/01-ground.md)

Musashi's foundations book. He defines strategy as something wider than sword-fencing, attacks the
commercialisation of martial schools, compares the strategist to a carpenter, previews the five books,
and closes with a nine-line rule of life.

---

## ★★★ The nut and the flower

> "If we look at the world we see arts for sale. Men use equipment to sell their own selves. As if with
> the nut and the flower, the nut has become less than th flower. In this kind of Way of strategy, both
> those teaching and those learning the way are concerned with colouring and showing off their technique,
> trying to hasten the bloom of the flower. They speak of 'This Dojo' and 'That Dojo'. They are looking
> for profit."

**Reading** — The nut is the thing that works; the flower is the display around it. Schools optimise for
the flower because the flower is what sells, and once that inversion happens the school keeps its name
and loses its function. Note that Musashi does not say display is bad. He says the ranking is wrong.

**Carries over** — Directly, and it is the single most useful passage in the book for our industry. The
nut is software that works in production for the people who depend on it. The flower is conference
talks, architecture diagrams, framework partisanship, follower counts, the internal design doc that
impresses the promotion committee. Every one of those has real uses. The failure is specifically the
inversion: choosing the technically worse option because the better one is harder to narrate. "This Dojo
and That Dojo" is the framework war, verbatim, four hundred years early.

---

## ★★★ The nine rules

> "Do not think dishonestly. The Way is in training. Become acquainted with every art. Know the Ways of
> all professions. Distinguish between gain and loss in worldly matters. Develop intuitive judgement and
> understanding for everything. Perceive those things which cannot be seen. Pay attention even to trifles.
> Do nothing which is of no use."

**Reading** — Musashi's whole ethic, compressed. Worth noting what is *absent*: nothing about courage,
honour, loyalty, or glory. It is a list about honesty, breadth, practice, attention, and economy.

**Carries over** — Almost line by line, and it is the natural spine for a derived book:

| Musashi | Engineering reading |
|---|---|
| Do not think dishonestly | Do not lie to yourself about what the code does or how done it is |
| The Way is in training | Skill comes from repetition under real conditions, not from reading |
| Become acquainted with every art | Learn adjacent disciplines — ops, design, data, the business |
| Know the Ways of all professions | Understand the work of the people your software is for |
| Distinguish between gain and loss | Actually weigh cost against benefit; most engineering argument skips this |
| Develop intuitive judgement | Build the taste that lets you smell a bad design before you can prove it |
| Perceive what cannot be seen | Latency, coupling, load, the failure that hasn't happened yet |
| Pay attention even to trifles | The warning, the flaky test, the log line nobody reads |
| Do nothing which is of no use | Delete it. Don't build it. Don't attend it. |

"Do nothing which is of no use" is the strongest and least followed. It condemns speculative
generality, premature abstraction, and most process.

---

## ★★★ The foreman carpenter

> "The foreman carpenter must know the architectural theory of towers and temples, and the plans of
> palaces, and must employ men to raise up houses."

> "The foreman should take into account the abilities and limitations of his men, circulating among
> them and asking nothing unreasonable. He should know their morale and spirit, and encourage them when
> necessary."

**Reading** — Musashi's model of leadership is a working craftsman who has been promoted, not a class
apart. The foreman still knows how to cut wood. His new skills are planning, allocation, and knowing
his people. "Asking nothing unreasonable" is the load-bearing phrase.

**Carries over** — This is the tech lead and the engineering manager, and it is a sharper model than
most of what our industry writes about them, because it refuses the split between "technical track" and
"management track." The foreman's authority comes from craft. Note the demand that he *circulate*: he
walks the site. The manager who has not read the code in a year has stopped being a foreman.

---

## ★★★ Choosing the timber

> "Straight un-knotted timber of good appearance is used for the revealed pillars, straight timber with
> small defects is used for the inner pillars. Timbers of the finest appearance, even if a little weak,
> is used for the thresholds, lintels, doors... Good strong timber, though it be gnarled and knotted, can
> always be used discreetly in construction. Timber which is weak or knotted throughout should be used as
> scaffolding, and later for firewood."

> "The foreman carpenter allots his men work according to their ability."

**Reading** — Two readings sit on top of each other, and Musashi means both. Materials are matched to
load: appearance where appearance is seen, strength where strength is needed, and the flawed stock is
used honestly rather than hidden in a pillar. And people are matched to work the same way.

**Carries over** — The material reading is the better one for us, and it is a genuinely good engineering
principle that our field states badly. Not all code deserves the same standard. The public API, the
payment path, and the migration script are revealed pillars. The internal admin tool is a threshold.
The one-off backfill is scaffolding — write it fast, use it, burn it. Insisting on uniform craft
everywhere is not rigour; it is an inability to judge load.

The people reading needs care. "Those of poor ability lay the floor joists" is a fixed hierarchy of
worth; a software team is not that, because people grow and rotate. Keep "match work to demonstrated
strength," drop "sort people into permanent grades." See [`../context/03-adaptation-rules.md`](../context/03-adaptation-rules.md).

---

## ★★ The joints, not the sections

> "The attainment of the carpenter is that his work is not warped, that the joints are not misaligned,
> and that the work is truly planed so that it meets well and is not merely finished in sections."

**Reading** — Quality is a property of the assembled whole. Perfect components that don't meet are a
failed building.

**Carries over** — This is integration, and it is the most common way good engineers produce bad systems.
Every service well-written, every team's section finished, and the joints — the API contracts, the
retry semantics, the ownership of the failure case between two teams — misaligned. Musashi's word
"warped" is exact: sections finished separately drift, and drift shows at the seams.

---

## ★★★ Timing and background timing

> "There is timing in everything... There is timing in the whole life of the warrior, in his thriving
> and declining, in his harmony and discord. Similarly, there is timing in the Way of the merchant, in
> the rise and fall of capital."

> "From among the large and small things and the fast and slow timings find the relevant timing, first
> seeing the distance timing and the background timing... It is especially important to know the
> background timing, otherwise your strategy will become uncertain."

**Reading** — Musashi distinguishes the tempo of the immediate exchange from the *background* tempo: the
larger rhythm of a career, an institution, a market, in which the exchange sits. He says the background
one matters more, and that ignoring it makes correct local moves add up to nothing.

**Carries over** — Very strongly, and it names something engineers routinely get wrong. A refactor can
be right in itself and wrong this quarter. A rewrite can be technically justified and land during a
funding crunch that kills it half-finished. Reading only the immediate timing produces engineers who are
always correct and never effective. Background timing is: where is this company in its life, where is
this codebase in its life, where am I in mine.

---

## ★★ Do not have a favourite weapon

> "You should not have a favourite weapon. To become over-familiar with one weapon is as much a fault as
> not knowing it sufficiently well. You should not copy others, but use weapons which you can handle
> properly. It is bad for commanders and troopers to have likes and dislikes."

**Reading** — Attachment to a tool is a defect regardless of the tool's quality, because it makes the
tool choose the situation. Note the balance: he equally condemns *not knowing it well enough*. He is not
recommending shallow breadth.

**Carries over** — Language and framework identity. "I'm a Rust developer" is a smaller claim than "I
build systems," and it silently filters which problems you accept. The second half is the part usually
dropped: dilettante breadth is condemned in the same sentence. And "use weapons which you can handle
properly" licenses the boring choice — the team's actual competence is a legitimate input to technology
selection, not a compromise.

---

## ★★ Weapons hardy rather than decorative

> "Weapons should be hardy rather than decorative."

> "The bow is tactically strong at the commencement of battle... However, it is unsatisfactory in sieges,
> or when the enemy is more than forty yards away."

> "From inside fortifications, the gun has no equal among weapons. It is the supreme weapon on the field
> before the ranks clash, but once swords are crossed the gun becomes useless."

**Reading** — Tools have ranges. The entire section is Musashi refusing to rank weapons absolutely and
insisting on ranking them per situation and distance.

**Carries over** — The clearest possible statement of "no silver bullet," but more useful than the usual
version because it is specific about *why*: each tool has a band of engagement where it dominates and
outside which it is dead weight. A message queue is a gun. It has no equal at its range. It is useless
once you are in a tight synchronous loop. The mistake is never picking the wrong tool in the abstract;
it is carrying it outside its range.

---

## ★ Seeing the arrow in flight

> "One of the virtues of the bow is that you can see the arrows in flight and correct your aim
> accordingly, whereas gunshot cannot be seen. You must appreciate the importance of this."

**Reading** — A weaker instrument with feedback beats a stronger one without it.

**Carries over** — Observability, and this is a small gem. A slower system you can watch and correct
outperforms a faster one that is opaque. It also argues for short feedback loops over powerful
one-shot moves: a deploy you can watch and roll back beats a bigger deploy you cannot.

---

## ★★ Immature strategy is the cause of grief

> "Someone once said 'Immature strategy is the cause of grief'. That was a true saying."

**Reading** — Half-learned method is worse than none, because it produces confidence without competence.

**Carries over** — The engineer who has read about microservices, DDD, or event sourcing and applies the
vocabulary without the conditions. Partial understanding is actively dangerous in a way that ignorance
is not, because ignorance does not build.

---

## ★★ From one thing, know ten thousand things

> "The strategist makes small things into big things, like building a great Buddha from a one foot
> model." / "The principle of strategy is having one thing, to know ten thousand things."

> "The Way of battles is the same for man to man fights and for ten thousand a side battles."

**Reading** — Musashi's core structural claim: the same principles operate at every scale, so mastery of
the small case is mastery of the large. It is why he can teach army command by teaching duelling.

**Carries over** — Genuinely, and it justifies the whole enterprise of a book like this: what you learn
debugging one function applies to debugging one organisation. But it deserves a flag. Musashi is wrong
in one specific direction — some things are *only* emergent at scale, and distributed systems are the
standing counterexample. A function that works does not imply a fleet that works. Keep the claim as
"principles generalise"; reject it as "behaviour generalises."

---

## ★ Everything is difficult at first

> "It will seem difficult at first, but everything is difficult at first. Bows are difficult to draw,
> halberds are difficult to weild; as you become accustomed to the bow so your pull will become stronger."

**Reading** — Initial difficulty carries no information about eventual fit.

**Carries over** — Plainly, as an argument against judging a tool, language, or practice by the first
week. Ordinary, but the ordinariness is the point: he states it without drama.

---

## ✗ Rejected — the four estates

> "There are four Ways in which men pass through life: as gentlemen, farmers, artisans and merchants."

**Reading** — The Tokugawa caste order, taken as natural law.

**Rejected** — A description of a specific frozen society, not a transferable insight. Any derived book
that reproduces it — as "founders, engineers, designers, salespeople know their place" — imports a caste
system while sounding traditional. The carpenter material is what to keep from this passage's neighbourhood.

---

## ✗ Rejected — resolute acceptance of death

> "Generally speaking, the Way of the warrior is resolute acceptance of death."

**Reading** — Literal. It is what makes a soldier useful and it is what Musashi is training for.

**Rejected** — This is the single most-quoted line of the samurai tradition and it does not survive.
Software has no death to accept, and the metaphorical versions — sacrifice, the death march, the
crunch — are exactly the harm this genre does. There is a real neighbouring idea (act without hedging
once committed; see "Cut and Slash" in [`02-water.md`](02-water.md)) and it should be taken from the
passage that actually says that, not smuggled in through the word "death."

---

## ✗ Rejected — "strategy is based on overcoming men"

> "The warrior is different in that studying the Way of strategy is based on overcoming men. By victory
> gained in crossing swords with individuals... we can attain power and fame for ourselves or our lord."

**Reading** — Musashi's stated purpose. Defeat of other people, for power and reputation.

**Rejected** — The frame does not transfer, and pretending otherwise produces the worst version of this
genre: colleagues as enemies, code review as a duel, other teams as opposing armies. The derived book
must find its own answer to "what is the opposition" and it will not be people. See
[`../context/03-adaptation-rules.md`](../context/03-adaptation-rules.md), Rule 1.
