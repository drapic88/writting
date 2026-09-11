# Plan — post 1: What Actually Happens When You Prompt an LLM

**Series:** *From Assistant to Agent*, part 1 of 10 (Foundations)
**Source:** "AI basic" deck, slides 3–4
**Status:** brief · not drafted

---

## 1. Positioning

### The angle
Every engineer on the team already uses an LLM daily. Almost none of them can say what the
model is doing between hitting enter and the first token appearing — and that gap is
exactly where the frustration comes from. This post is the mechanical explanation, written
for someone who ships code, not for someone studying transformers.

### The thesis
> An LLM has no database of facts and no memory of you. It predicts the next token given
> everything in front of it. Once you believe that literally, most "the AI got dumber"
> complaints become diagnosable.

Everything in the post earns its place by making that sentence more actionable.

### Title options
1. **What Actually Happens When You Prompt an LLM** — plain, searchable, safe.
2. **Your LLM Has No Memory. It Has a Window.** — thesis-forward, best click-through.
3. **Tokens, Windows, and Why Your Model "Got Worse"** — concrete and a little contrarian.

*Recommendation:* title #2, subtitle "Tokens, context windows, and the one distinction
that explains most of your frustration." It sets up post 3, which is the flagship.

---

## 2. Meta

- **Length:** 1,200–1,500 words (5–6 min). This is an on-ramp, not a treatise.
- **Audience:** working engineers who use AI tools but have never read anything about how
  they work. Assume they know what a neural network is in the loosest sense; assume they
  do not know what a token is.
- **Tags:** `AI`, `LLM`, `Software Engineering`, `Programming`, `Developer Tools`
- **Series slot:** publish 7th. It exists to catch search traffic and funnel it to post 3.

---

## 3. Structure

### Lede (~120 words)
Open on a concrete, recognisable moment: you paste a stack trace, get a confident answer
naming a function that does not exist in your codebase, and lose twenty minutes. Not
because the model is broken — because it did exactly what it is built to do. Promise three
ideas that make it predictable.

Do **not** open with "AI is changing software development." Instant close.

### Section 1 — It is next-token prediction, all the way down (~350 words)
The deck's example is good, keep it. Show a probability distribution over one continuation:

```
"The build is …"
  → green    74%
  → failing  18%
  → ready     5%
```

Beats to hit:
- Trained on text, code and documents at enormous scale.
- Picks a high-probability continuation, one token at a time, then re-reads its own output
  and does it again.
- There is no lookup step. Nothing is retrieved from a table of facts.
- Therefore *fluency and correctness are unrelated properties.* This is the paragraph the
  whole post exists for. A wrong answer is not a malfunction; it is a high-probability
  continuation that happens to be false.

Land the practical consequence: verify anything that matters, and prefer questions whose
answer you can check cheaply.

### Section 2 — Tokens (~200 words)
Text is chunked at roughly four characters. The model reads and writes tokens, not words.
Two consequences engineers actually feel:
- Usage, limits and cost are all measured in tokens, so verbosity has a price.
- Code and JSON tokenize worse than prose — a 200-line diff is more expensive than a
  200-line essay.

Include a small illustration of one sentence split into tokens. Do not turn this into a
tokenizer tutorial.

### Section 3 — The context window (~300 words)
Everything the model can see in one turn: your messages, attached files, tool output, and
its own previous replies. Frame it as a desk, not a brain — finite surface, and *you*
decide what is on it.

Two misconceptions to kill explicitly:
- "It remembers our last conversation." It does not, unless something re-supplies that
  text.
- "A bigger window means I can stop thinking about what I paste." Signal-to-noise still
  degrades; forty irrelevant files make the relevant one harder to weight.

This is the hinge into post 3 — say so in one sentence and move on.

### Section 4 — Training vs inference (~200 words)
Training happened once, in the past, against a fixed data cutoff. Inference is the live
conversation. Nothing you say in a session is learned. Consequences:
- The model does not know your repo, your incident from last Tuesday, or a library
  released after its cutoff — you have to put those in front of it.
- Correcting it in-conversation fixes *this* window and nothing beyond it. Durable
  correction is a file you commit, which is post 3's subject.

### Close (~150 words)
Restate the three ideas as three habits: keep the window clean, pay attention to what you
paste, and re-supply context deliberately instead of hoping for memory. Then the series
link to post 3.

---

## 4. Genericizing notes

Nothing sensitive in this post — it is all general mechanics. The only rule: when
illustrating with a codebase, use the shared fictional stack from the root `README.md`
(`web-app`, `rest-api`, `PROJ-1234`) rather than inventing new names, so the series stays
consistent.

---

## 5. Verify before publishing

- Token ≈ 4 characters is a rule of thumb; state it as one.
- Do not quote a specific context-window size unless checked at publish time — sizes move
  and a stale number dates the post badly.
- Do not name a training cutoff date for any specific model.

---

## 6. Hero image brief

Foundations motif: a horizontal token stream, each token a rounded box, the last three
boxes ghosted with probability percentages beside them. Large "01" in the corner. Two
colours plus a neutral background, per the series system in the root `README.md`.

---

## 7. Traps

- Do not explain attention or transformer architecture. It does not change what the reader
  does on Monday.
- Do not moralise about hallucination. Explain the mechanism and let the reader conclude.
- Resist the urge to add prompting tips here — they belong in post 2.
