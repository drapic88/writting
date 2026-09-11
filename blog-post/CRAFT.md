# Blog post craft — Medium

**Read [`../VOICE.md`](../VOICE.md) first.** It holds the evidence rule, the stance, the
sentence mechanics, the devices and the anti-patterns that govern everything in this
repository. This file holds only what is specific to a Medium post: its anatomy, its
length, the series scaffolding, the folder workflow and the pre-publish checklist.

See [README.md](README.md) for the series table, publish order, and Medium tags and
publication targets. Anything drawn from real client work goes through
[`../CONFIDENTIALITY.md`](../CONFIDENTIALITY.md) first.

---

## 1. Anatomy of a post

Follow this skeleton. Deviations should be deliberate.

```markdown
# Thesis As A Claim With A Verb In It

### The specifics, or the reframe, in one line

*Provenance and caveat: what this was written against, and what might shift.*

![Alt text that restates the thesis for someone who only sees the image](./hero.png)

---

<lede: 3-5 short paragraphs>

---

## First real section

...
```

### Title (`#`)

A claim, not a topic. It must contain a verb and take a position.

- Good: *PHP 8.6 Is a Small Release With a Big Warning Label* — *Your AI Didn't Get Worse.
  Your Context Did.* — *"Done" Is Five Separate Claims* — *A Tip Nobody Installs Is Not a
  Tip*
- Weak (the earlier pattern, do not repeat): *Git Branch Naming Convention Bests
  Practice* — *How to create Continuous Integration/Continuous Deployment*. These describe
  the subject and promise nothing.

Title Case for the H1. Two short sentences are allowed and often the strongest form: the
false belief, then the correction.

### Subtitle (`###`)

Medium renders this as the kicker. It carries the specifics the title had to leave out, or
it states the reframe plainly. No hype, no colon-separated keyword salad.

### Provenance line (italic, optional but usual)

One italic sentence establishing what the post was written against and what could move —
a beta version, a series position, a warning that command names drift between releases.
This is a trust device: it tells the reader you know your own shelf life.

### Hero image

`hero.svg` authored in the folder, exported to `hero.png` at 1400×700. Alt text is a full
restatement of the thesis, not a caption.

### Lede

Four moves, in this order, in about 150–250 words:

1. **The reader's actual experience**, concretely. A sentence someone has said out loud,
   pulled into a blockquote if it is a direct quote. Or a dated trigger event: "A few days
   ago we got a call from our SEO partner…". Never an abstraction about the industry.
2. **The honest version, up front.** State the real answer immediately. "Upgrading to 8.6
   will take you an afternoon. Getting *clean* on 8.6 is how you avoid a painful PHP 9.0."
   No withholding the conclusion to keep people reading.
3. **The thesis in bold**, once. "**You are not writing prompts.**"
4. **A roadmap sentence** naming what the post covers, in order. "Three things are worth
   your attention…" / "Here is the model I use instead, the habits that fall out of it, and
   how to diagnose a bad session in ninety seconds."

Then a `---` rule.

### Sections (`##`)

Sentence case. A heading is an opinion, a warning, or a plain label — never a
content-marketing question.

- Opinion: `The headline: partial function application`
- Warning: `The gotcha that will bite someone on your team`
- Label with a stance: `` `Time\Duration`: fixing a twenty-year-old API smell ``
- Structural: `What didn't make it` · `The limits` · `Three sources, one window`
- Closing: `Verdict` or `The thing to keep`

The two-part `Subject: what I think of it` form with a colon is the workhorse. Use it.

Inherit `The problem` / `The solution` from the earlier articles when a post is genuinely
one problem and one solution — it is honest and it scans. Do not use it as a default
container for everything.

### Subsections (`###`)

Two uses only:

- Facets of one section: `Why this matters now`, `The gotcha…`, `The limits`.
- A numbered playbook: `### 1. Bump, and make deprecations visible` through
  `### 7. Let the tools do it`. Every long post earns its keep with one section like this —
  the part the reader will act on this week. Give each step the actual command, and end the
  playbook with a cost estimate.

### Close

Not a summary. Three moves:

1. Restate the thesis in one compressed line. "PHP 8.6 is a small release and a loud one."
2. Say what the evidence adds up to, with the position stated.
3. **One concrete action for this week, with a threshold that tells the reader which
   situation they are in.** "Run your suite against the beta with `error_reporting=E_ALL`
   and count the deprecation lines. That number tells you whether this upgrade is an
   afternoon or a sprint — and either way you'd rather know in September than next
   November."

Never end on the last item of a list. The earlier articles do this and it costs them the
whole ending.

### Sources (`###`)

Linked citations for anything checkable: RFCs, changelogs, vendor docs, issue threads.
Format `[Title](url) — publisher`. Non-negotiable for release and feature posts.

---

## 2. Format and length

| Post type | Words | Read time | Sections |
|-----------|-------|-----------|----------|
| Flagship / deep dive | 2,000–2,400 | 9–11 min | 6–9 `##`, one numbered playbook |
| Standard long-form | 1,500–2,000 | 7–9 min | 5–7 `##` |
| Field note / process | 900–1,300 | 4–6 min | 3–5 `##`, problem → solution |

Tables for comparisons and mappings, never for prose. Code blocks always carry a language
tag. Keep code under ~20 lines; if it needs more, the example is doing too much.

---

## 3. Series conventions

Every post in a series carries scaffolding at both ends — this is inherited directly from
"A Revendo Way" and it worked.

- **Open** with a one-line italic series note: `*Part 3 of* From Assistant to Agent — *a
  series on …*`.
- **Close** with the next post in the series, linked. Update links as posts go live; a
  dangling promise to a post that does not exist costs more than it gains.
- **Back-link list** at the top for the third post onward, as a plain bulleted list of the
  previous titles.

---

## 4. Repository workflow

Each post is a folder: `plan.md` (drafting brief) → `article.md` (the Medium draft) →
`hero.svg` + `hero.png`. Write `plan.md` first and get it agreed before drafting the
article. See [README.md](README.md) for the series table, publish order, and Medium tags
and publication targets. Internal material is genericized per
[`../CONFIDENTIALITY.md`](../CONFIDENTIALITY.md) before it reaches a draft.

---

## 5. Pre-publish checklist

Run this against the finished draft.

- [ ] Title is a claim with a verb, not a topic.
- [ ] The lede states the honest answer in the first three paragraphs.
- [ ] Thesis appears in bold exactly once.
- [ ] A roadmap sentence names what the post covers.
- [ ] Every section could survive the question "what is the evidence?"
- [ ] At least one real code block, command, or file path per major section.
- [ ] Every version number, flag and command verified against current docs, not a deck.
- [ ] Limits, gotchas and the case-where-this-fails are stated, not buried.
- [ ] One numbered playbook the reader can act on this week.
- [ ] A cost estimate somewhere.
- [ ] Close does the three moves and ends on a concrete action with a threshold.
- [ ] Sources section with real links.
- [ ] Series note at the top, next-post link at the bottom, both correct.
- [ ] Zero words from the anti-pattern list.
- [ ] Read the whole thing aloud once. Anything you would not say to a colleague, cut.
