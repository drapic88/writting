# Marks — The Fire Book

Source: [`source/musashi/03-fire.md`](../source/musashi/03-fire.md)

The longest and most tactical book: twenty-odd named techniques for the moment of engagement. Musashi's
subject here is initiative, tempo, position, and what to do when neither side can win. It is the book
whose *frame* transfers worst — there is no enemy in software — and whose *mechanisms* transfer best,
because most of them are really about rhythm, deadlock, and attention.

Read the whole book with [`../context/03-adaptation-rules.md`](../context/03-adaptation-rules.md) Rule 1
in hand: where Musashi says "the enemy," the derived reading must supply something that is not a colleague.

---

## ★★★ Depending on the place

> "Examine your environment. Stand in the sun; that is, take up an attitude with the sun behind you...
> Make sure that your rear is unobstructed, and that there is free space on your left."

> "Always chase the enemy into bad footholds, obstacles at the side, and so on, using the virtues of the
> place to establish predominant positions from which to fight."

**Reading** — Musashi opens his book on fighting not with a technique but with terrain. Before anything
else: know where you are standing, what is behind you, what constrains movement. Position is chosen
before the exchange, and it decides much of the exchange.

**Carries over** — Strongly, and it argues for putting environment first in any derived book. The
engineering terrain is: what can you deploy, how fast can you roll back, what does the test suite
actually cover, who has context, what does the org reward, how long is the review queue. Every one of
those is decided before the work starts and constrains it more than skill does. An engineer with good
terrain and average skill outperforms the reverse consistently, which is why the highest-leverage work
is often improving the terrain — fixing the deploy pipeline, not the feature.

"Make sure that your rear is unobstructed" is the rollback path. Never take an action whose retreat you
have not checked.

---

## ★★★ The three initiatives — Sen

> "The first is to forestall him by attacking. This is called Ken No Sen (to set him up). Another method
> is to forestall him as he attacks. This is called Tai No Sen (to wait for the initiative). The other
> method is when you and the enemy attack together. This is called Tai Tai No Sen."

> "This does not mean that you always attack first; but if the enemy attacks first you can lead him
> around. In strategy, you have effectively won when you forestall the enemy."

**Reading** — The most systematic passage in the book. Initiative is not the same as moving first: there
are three ways to hold it, including one where you let the other side commit and take the initiative
inside their commitment. Musashi is explicit that "always attack first" is a misreading.

**Carries over** — As three postures toward change, and it is a better framework than the usual
proactive/reactive binary:

- **Ken no Sen** — move first. Migrate before the version is dropped; refactor before the feature needs
  it; write the postmortem before the incident repeats.
- **Tai no Sen** — let it come, and take the initiative inside it. The classic engineering form: an
  incident, an audit, an outage arrives, and you use its authority to fix the thing you have been unable
  to get funded for a year. Not opportunism — the moment is genuinely when the change is cheapest.
- **Tai Tai no Sen** — move into it as it moves. The rewrite that happens *during* the feature that
  needs it, rather than as a separate project nobody funds.

The insight worth keeping is Musashi's: **initiative is a thing you can hold while not moving first**,
and a team that only knows Ken no Sen exhausts itself.

---

## ★★★ To hold down a pillow

> "'To Hold Down a Pillow' means not allowing the enemy's head to rise... The spirit is too check his
> attack at the syllable 'at...', when he jumps check his jump at the syllable 'ju...', and check his cut
> at 'cu...'."

> "The important thing in strategy is to suppress the enemy's useful actions but allow his useless
> actions. However, doing this alone is defensive."

**Reading** — Intervene at the first syllable, before the motion is committed, because a suppressed
intention costs nothing and a committed one costs everything. The second paragraph is the sophisticated
part and is usually dropped from quotations: suppress *selectively*, and understand that even perfect
suppression is only defence.

**Carries over** — This is the entire argument for early feedback, stated better than our field states it.
The cost curve of defects is Musashi's "at...", "ju...", "cu...". Type checker at the syllable, test at
the word, code review at the sentence, production at the paragraph. Every shift-left practice is holding
down the pillow.

The selective part is the good bit: *suppress the useful actions, allow the useless ones*. Do not gate
everything. A team that blocks every change equally has made the pillow into a pillow fort, and Musashi
already tells you that pure suppression wins nothing.

---

## ★★★ To know collapse

> "Everything can collapse. Houses, bodies, and enemies collapse when their rhythm becomes deranged."

> "If you fail to take advantage of your enemies' collapse, they may recover... Fix your eye on the
> enemy's collapse, and chase him, attacking so that you do not let him recover."

**Reading** — Collapse is a *rhythm* phenomenon, not a strength phenomenon — things fail when their
timing derangess, not when they get weak. And collapse is a window: unexploited, it closes.

**Carries over** — The diagnostic half is excellent and underrated. Systems and teams do fail by
derangement of rhythm rather than by lack of capacity: the deploy cadence breaks, the review queue
lengthens, the retry storm desynchronises, the on-call handoff drifts. When you are looking for what is
wrong with a team or a service, look for the broken rhythm before the missing resource.

The exploitation half needs Rule 1 applied. Against a system: yes, when a bug becomes reproducible, drop
everything and pin it — reproducibility is exactly a collapse window and it does close. Against a
person: no. "Don't let him recover" aimed at a colleague is how this genre poisons a team.

---

## ★★★ To become the enemy

> "'To become the enemy' means to think yourself in the enemy's position. In the world people tend to
> think of a robber trabbed in a house as a fortified enemy. However, if we think of 'becoming the
> enemy', we feel that the whole world is against us and that there is no escape."

> "People are always under the impression that the enemy is strong, and so tend to become cautious."

**Reading** — Occupy the other position and your estimate changes, usually downward. The cornered robber
looks formidable from outside and is terrified from inside. Musashi is describing a systematic
overestimation bias and a cure for it.

**Carries over** — Well, and in several directions at once. The legacy system that seems to be held
together by unknowable genius was written by people under deadline making the same compromises you make.
The other team blocking your migration has its own quarter and its own on-call. The user doing the
"stupid" thing has a reason. And most usefully: the intimidating codebase is a pheasant, not a hawk —
from inside it is just decisions, most of them ordinary.

This is the passage that best survives the removal of enmity, because the mechanism — deliberate
perspective-taking to correct a strength estimate — is neutral.

---

## ★★★ The mountain-sea change

> "It is bad to repeat the same thing several times when fighting the enemy. There may be no help but to
> do something twice, but do not try it a third time. If you once make an attack and fail, ther is little
> chance of success if you use the same approach again."

> "If the enemy thinks of the mountains, attack like the sea; and if he thinks of the sea, attack like
> the mountains."

**Reading** — A hard numeric rule, which is rare for Musashi: twice if forced, never three times. Then a
positive instruction — change to the opposite category, not to a variation.

**Carries over** — As the sharpest debugging rule in the book. Two attempts at a fix from the same
hypothesis is the limit; a third is a signal that the hypothesis, not the attempt, is wrong. Every
engineer has spent an afternoon making the same wrong assumption in six increasingly elaborate ways.

"Mountains against sea" is the crucial second half, because "try something different" is useless advice
without direction. It means change *category*: if you have been reading code, run it. If you have been
running it, read it. If you've been adding logging, take things away instead — bisect. If you have been
working alone, describe it to someone. The switch must be to the opposite kind of investigation, not a
new instance of the same kind.

---

## ★★★ To renew

> "'To renew' applies when we are fighting with the enemy, and an entangled spirit arises where there is
> no possible resolution. We must abandon our efforts, think of the situation in a fresh spirit then win
> in the new rhythm... without changing our circumstance we change our spirit."

**Reading** — Companion to Mountain-Sea, but distinct: that one changes the technique, this one changes
*you*. The circumstance is unchanged. What resets is the approach you bring to it.

**Carries over** — This is the walk, the sleep, the rubber duck, the "start the branch over from main."
Both the psychological version (stop, come back tomorrow, the bug is obvious in nine minutes) and the
literal one (throw away the tangled branch and redo the change cleanly now that you understand it —
almost always faster than untangling, and almost never done).

The pairing with Mountain-Sea is worth preserving in any derived book: change the technique, or change
the person holding it.

---

## ★★ Crossing at a ford

> "It means setting sail even though your friends stay in harbour, knowing the route, knowing the
> soundness of your ship and the favour of the day. When all the conditiongs are meet, and there is
> perhaps a favourable wind, then set sail."

> "I believe this 'crossing at a ford' occurs often in man's lifetime... To cross at a ford means to
> attack the enemy's weak point, and to put yourself in an advantageous position."

**Reading** — Committed passage at the right moment and the right place, with preparation done in advance
and the willingness to go when others don't. Note the ordering: knowledge of route, soundness of ship,
favour of the day — *then* sail. And note he says it happens often in a life, meaning career decisions,
not just battles.

**Carries over** — Directly, to both migrations and careers. The ford is the narrow window where a hard
crossing is cheap: the quarter before the traffic doubles, the moment after the team learns the new
system but before the deadline, the version before the breaking change lands. Fords close. Musashi's
preconditions are a real checklist — do you know the route (have you done a spike), is the ship sound
(does the test suite hold), is the day favourable (is the org's attention available).

---

## ★★ Rat's head, ox's neck

> "When we are fighting with the enemy and both he and we have become occupied with small points in an
> entangled spirit, we must always think of the Way of strategy as being both a rat's head and an ox's
> neck. Whenever we have become preoccupied with small detail, we must suddenly change into a large
> spirit, interchanging large with small."

> "It is necessary that the warrior think in this spirit in everyday life."

**Reading** — Deliberate, sudden switching of scale as a way out of entanglement. Not balance —
oscillation, applied when stuck.

**Carries over** — The zoom, and it is the practical companion to Perception and Sight from
[`02-water.md`](02-water.md). Three hours deep in a null pointer, ask what this service is for. Three
weeks into architecture discussion, go read the actual query that is slow. The entangled state Musashi
describes — both parties fixated on small points — is a design review arguing about naming while the
data model is wrong.

---

## ★★ To injure the corners

> "It is difficult to move strong things by pushing directly, so you should 'injure the corners'. In
> large-scale strategy, it is beneficial to strike at the corners of the enemy's force. If the corners
> are overthrown, the spirit of the whole body will be overthrown."

**Reading** — Structures fail at edges. Direct force against the strong centre is wasted; the corner is
load-bearing and reachable.

**Carries over** — Two good readings. For migrations: never start with the core. Take the leaf services,
the edge cases, the newest module — and the monolith's centre becomes movable once its dependencies have
gone. For failure analysis, it is even better: systems break at their corners — boundaries between
services, empty collections, midnight, the maximum value, the first request after deploy. When looking
for where something will fail, look at the corners, not at the load-bearing middle everyone has tested.

---

## ★★ To pass on

> "Sleepiness can be passed on, and yawning can be passed on. Time can be passed on also... when the
> enemy is agitated and shows an inclination to rush, do not mind in the least. Make a show of complete
> calmness, and the enemy will be taken by this and will become relaxed."

**Reading** — States are contagious across people, and Musashi treats this as a mechanism you can operate
deliberately.

**Carries over** — Observationally, minus the manipulation. Panic is transmissible and so is calm, and in
an incident the highest-value contribution of a senior engineer is often the transmission of the second
one. Rushing spreads through a team and produces exactly the errors that extend the outage. The
weaponised form — deliberately infecting people with boredom or carelessness, as Musashi describes —
does not transfer and should not.

---

## ★★ The commander knows the troops

> "Using the wisdom of strategy, think of the enemy as your own troops. When you think in this way you
> can move him at will."

**Reading** — Reframe an opposing force as something you direct, and options appear that were invisible
while it was a threat.

**Carries over** — Cleanly once "the enemy" is a system rather than a person. The production system, the
legacy codebase, the flaky test suite are not adversaries with intent; they are things with inputs and
responses that can be commanded once understood. The engineer who says "the deploy failed *at* me" is
not the commander. The one who says "it fails when the cache is cold, so warm the cache" is.

---

## ★★ The body of a rock

> "When you have mastered the Way of strategy you can suddenly make your body like a rock, and ten
> thousand things cannot touch you. This is the body of a rock. You will not be moved. Oral tradition."

**Reading** — Musashi's last and shortest technique, and he refuses to explain it — "oral tradition"
means the writing stops here. Immovability that is a consequence of mastery, not a technique of it.

**Carries over** — As the thing to aim at rather than a thing to do, which is how he presents it. The
engineer twelve years in who is not moved by the outage, the reorg, the framework of the year, or the
loud opinion in review — not because they are disengaged but because they have seen the shape before. It
is worth noting that Musashi puts this last and declines to teach it. Any derived book should be
similarly honest that its final chapter cannot be transmitted in writing.

---

## ★ To move the shade / to hold down a shadow

> "'To move the shade' is used when you cannot see the enemy's spirit... indicate that you are about to
> attack strongly, to discover his resources."

> "'Holding down a shadow' is use when you can see the enemy's attacking spirit."

**Reading** — A matched pair for two states of information: probe when you cannot read the situation,
pre-empt when you can.

**Carries over** — "Move the shade" is the deliberate probe, and it is genuinely useful: the canary
deploy, the load test, the migration dry-run, the RFC floated to see who objects. Cheap action taken to
generate information rather than to achieve the outcome. Engineers under-use it because it looks like
wasted work; it is the cheapest information available.

---

## ★ The three shouts

> "The voice is a thing of life... In large-scale strategy, at the start of battle we shout as loudly as
> possible. During the fight, the voice is low-pitched, shouting out as we attack. After the contest, we
> shout in the wake of our victory."

**Reading** — Three distinct registers of communication, matched to phase: loud to commit and align,
low and functional during, loud again to close.

**Carries over** — As incident communication, surprisingly exactly. Announce loudly at the start
(declare the incident, page, tell everyone). Speak in short functional statements during. Announce
loudly at the end — and the third shout is the one teams skip. Musashi says it is "to announce victory,"
and its absence is why organisations don't know their engineers fixed anything.

---

## ★ To cause loss of balance / to frighten / to throw into confusion

> "Many things can cause a loss of balance. One cause is danger, another is hardship, and another is
> surprise."

> "In large-scale strategy you can frighten the enemy not just by what you present to their eyes, but by
> shouting, making a small force seem large."

> "Victory is certain when the enemy is caught up in a rhythm which confuses his spirit."

**Reading** — Three techniques for degrading an opponent's decision-making.

**Carries over** — Inverted only. As offence against people these are workplace manipulation and are
rejected outright. As a *defensive* catalogue they are worth keeping: this is a list of the conditions
under which your own judgement fails — danger, hardship, surprise, a rhythm you did not set, an
apparent force larger than it is. Recognising that you are currently being destabilised is the useful
half, and the honest way to carry this material across.

---

## ★ To let go the hilt

> "There is the spirit of winning without a sword. There is also the spirit of holding the long sword but
> not winning."

**Reading** — Two sentences, then he stops. The tool is not the capability.

**Carries over** — As the smallest possible statement of a real thing: the best solution is often not
software. The ticket closed by a conversation, the feature deleted rather than fixed, the automation
replaced by not doing the task. "Holding the long sword but not winning" is the team with excellent
tooling shipping nothing.

---

## ✗ Rejected — to crush

> "This means to crush the enemy regarding him as being weak... we knock the hat over his eyes, crushing
> him utterly. If we crush lightly, he may recover... without allowing him space for breath."

**Reading** — Total destruction of a weaker opponent, denying recovery.

**Rejected** — There is a legitimate neighbour ("when you have a reproducible bug, finish it") and it is
already covered by "To know collapse." Keeping this passage under its own name imports a disposition
toward weaker parties that has no place in engineering. It is exactly the material that produces the bad
version of this genre, and it should be visibly dropped rather than quietly softened.

---

## ✗ Rejected — to penetrate the depths

> "We can destroy the enemy's spirit in its depths, demoralising him by quickly changing our spirit."

**Reading** — Defeating morale rather than the body, on the grounds that a superficially beaten opponent
recovers.

**Rejected** — Demoralisation as a goal does not transfer. There is a faint technical shadow — a fix that
addresses symptoms leaves the cause alive to recur — but that idea is already carried, and better, by
"Cut and Slash" in [`02-water.md`](02-water.md).
