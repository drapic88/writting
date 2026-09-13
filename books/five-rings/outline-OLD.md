# Outline — *The Five Rings of Software* (working title)

A book on the daily work of a software engineer, structured on Musashi's five, following the rules in
[`../context/03-adaptation-rules.md`](../context/03-adaptation-rules.md) and the voice in
[`../context/02-voice.md`](../context/02-voice.md).

## Why the same five

Musashi's division is not decorative and it is not arbitrary. It runs from foundation, through the
individual, through conflict, through comparison, to what is left after method. That sequence is
independently correct for engineering, which is the reason to keep it rather than an excuse:

| Book | Musashi | This book | Subject |
|---|---|---|---|
| Ground | What strategy is; the carpenter | **Ground** | What the work actually is, and what it is for |
| Water | The individual swordsman | **Water** | The practitioner: attention, judgement, craft |
| Fire | The moment of combat | **Fire** | Engagement: incidents, migrations, tempo, being stuck |
| Wind | Rival schools | **Wind** | How methods decay, and why we adopt them anyway |
| Void | Beyond method | **Void** | What remains, and what cannot be written down |

---

## Front matter

**On borrowing.** One page. States openly that this is derivative, names the source and translation, and
states the rules it followed — especially that there is no enemy in this book, and why. Also states the
book's insufficiency (Rule 6): reading it does nothing.

---

## Book One — Ground

*What the work is. The shortest possible answer: software that works, for people who need it, that can
be changed tomorrow.*

| Section | From | Core |
|---|---|---|
| The nut and the flower | ★★★ Ground | The thing that works vs. the display around it; the inversion, not the display, is the fault |
| The foreman still cuts wood | ★★★ Ground | Leadership as promoted craft; the manager who has not read the code has stopped being a foreman |
| Choosing the timber | ★★★ Ground | Not all code deserves the same standard; revealed pillars, thresholds, scaffolding, firewood |
| The joints, not the sections | ★★ Ground | Quality is a property of the assembled whole; drift shows at the seams |
| Two timings | ★★★ Ground | Immediate vs. background timing; correct-but-wrong-this-quarter |
| No favourite weapon | ★★ Ground | Tool identity; and the second half — dilettante breadth condemned equally |
| Every tool has a range | ★★ Ground | The gun is supreme at its range and useless outside it |
| The arrow you can see | ★ Ground | A weaker instrument with feedback beats a stronger opaque one |
| The nine rules | ★★★ Ground | Musashi's list, given an engineering reading, one line each. Closes the book. |

**Exception work required:** Choosing the timber must guard hard against "some code doesn't need to be
good" as a licence. Rule 7 applies to the people reading of the same passage.

---

## Book Two — Water

*The practitioner. What you do when nobody is watching, because that is what you will do when everybody is.*

| Section | From | Core |
|---|---|---|
| Your ordinary week is your incident | ★★★ Water | No wartime mode; the incident reveals practice, it does not override it |
| Perception and sight | ★★★ Water | Two faculties; distant things as close, close things at distance; the on-call that fights every page |
| The living hand | ★★★ Water | Tight where it must not move, loose where the world changes; both failure poles |
| Attitude, no attitude | ★★★ Water | Learn the patterns properly, then stop performing them; if you can name it while doing it, you are still holding an attitude |
| Cut and slash | ★★★ Water | The fix that works vs. the fix that resolves; and the honest extension — slash on purpose, and write it down |
| Mind the return stroke | ★ Water | Done is when the system is ready for the next change: flag removed, branch deleted, doc corrected |
| The unearned instinct | ★★ Water | Trained intuition is real and must be verified; software, unlike a duel, lets you check |
| One foot then the other | ★ Water | Building and consolidating are one motion, not rival goods |
| Do not just read | ★★ Water | The book's own insufficiency, stated where the source states it. Closes the book. |

---

## Book Three — Fire

*Engagement. The longest book, as in the original.*

| Section | From | Core |
|---|---|---|
| Look at the ground first | ★★★ Fire | Terrain before technique: deploy speed, rollback, coverage, review queue. Highest leverage is often terrain, not skill |
| Check your retreat | ★★★ Fire | "Rear unobstructed" — never act without a checked rollback |
| Three ways to hold the initiative | ★★★ Fire | *Sen*: move first / take it inside their move / move as it moves. A team that only knows the first exhausts itself |
| Holding down the pillow | ★★★ Fire | "at…", "ju…", "cu…" — the cost curve; and the selective half: suppress useful actions, allow useless ones |
| Rhythm, not strength | ★★★ Fire | Things collapse when their rhythm derangess. Diagnostic: look for broken cadence before missing capacity |
| Twice, never three times | ★★★ Fire | The hard rule; then mountains against sea — change category, not instance |
| Renew | ★★★ Fire | Change the person, not the technique. Throwing away the tangled branch |
| Become the system | ★★★ Fire | Perspective-taking to correct a strength estimate; the intimidating codebase is a pheasant |
| Injure the corners | ★★ Fire | Migrations start at leaves; and failures live at boundaries, empty sets, midnight, first request after deploy |
| The zoom | ★★ Fire | Rat's head, ox's neck: deliberate scale switching as the way out of entanglement |
| Crossing at the ford | ★★ Fire | Windows close; route, ship, day — a real checklist |
| Probe to see | ★ Fire | Canary, dry run, floated RFC: cheap action to buy information |
| Calm is contagious | ★★ Fire | Transmission of state; the manipulation half explicitly dropped |
| Three shouts | ★ Fire | Declare, work quietly, announce the end — teams skip the third |
| When your own judgement goes | ★ Fire | The destabilisation catalogue, inverted to defence: danger, hardship, surprise, someone else's tempo |
| Not everything is a sword | ★ Fire | The ticket closed by a conversation; the feature deleted rather than fixed |

**Rule 1 pressure is highest in this book.** Every section names its non-person opposition explicitly.

---

## Book Four — Wind

*How methods decay. Patterns only, never named tools (Rule 4). Every criticism carries its exception (Rule 5).*

| Section | From | Core |
|---|---|---|
| Why study what you will never use | ★★★ Wind | Drift is invisible from inside; comparison is the only instrument |
| The school that relies on length | ★★★ Wind | Dependence, not the tool, is the fault. Test: can the team solve it without? |
| Speed is not a quality | ★★★ Wind | The distance runner; "never appear busy"; refusing someone else's tempo |
| The school that fixes its eyes | ★★★ Wind | Single-metric optimisation; the footballer doesn't watch the ball |
| The school of the strong hand | ★★ Wind | Effort as proxy for value; overcommitment carries your sword along |
| Process as garrison | ★★ Wind | Attitude is for holding ground, not engaging — with Musashi's own allowance for castles |
| The habit of responding | ★★ Wind | Each reaction correct, the habit fatal; connects back to *sen* |
| One gait for everything | ★★ Wind | Special deploy procedures, special review standards; the specialised gait fails outside its case |
| No interior, no surface | ★★★ Wind | Against gatekeeping and manufactured complexity; emerging at the gate. Closes the book. |

---

## Book Five — Void

*Very short. Three sections and an ending. Placed last and explicitly not readable first.*

| Section | From | Core |
|---|---|---|
| The counterfeit | ★★★ Void | Bewilderment relabelled as depth. "It depends" and "you develop a feel for it." The test: mastery can say where its knowledge ends |
| Clouded | ★★★ Void | The unclouded state as the condition of real debugging; the hour lost defending a hypothesis |
| What is not yours | ★★ Void | The code is not you; deleting your own work without pain |
| The passage I did not translate | Rule 8 | Quote Musashi's final turn, decline to convert it, say why. End the book here. |

---

## Open questions before drafting

1. **Audience level.** Written for a mid-level engineer growing into senior, or for anyone including
   leads and managers? Affects how much of the Ground Book's foreman material stays.
2. **Personal material.** Musashi's authority came from his own sixty duels. Should the book use
   first-person experience from your own work, or stay impersonal? Impersonal is safer and thinner.
3. **Code.** Zero code samples (Musashi has no diagrams), or a small number of concrete snippets?
4. **Title.** *The Five Rings of Software* is a placeholder.
