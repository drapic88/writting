# Plan — post 9: An Agent You Can Pipe Into `jq`

**Series:** *From Assistant to Agent*, part 9 of 10 (Trust)
**Source:** advanced workshop deck, slides 22–23
**Status:** brief · not drafted

---

## 1. Positioning

### The angle
Almost all writing about coding agents assumes an interactive session. The headless mode is
the underrated half: a prompt becomes a command, a command becomes a pipeline stage, and a
pipeline stage with a JSON schema becomes a gate you can fail a build on. That last step is
the one that turns an agent from "a paragraph a human reads" into a component.

### The thesis
> The moment an agent emits schema-conforming JSON, it stops being something you read and
> becomes something you can fail a build on.

### Title options
1. **An Agent You Can Pipe Into `jq`** — best hook for a unix-minded audience.
2. **Your AI Reviewer Should Fail the Build, Not Write a Paragraph** — strongest thesis
   framing.
3. **Headless Agents: The Half Nobody Writes About** — descriptive, weaker.

*Recommendation:* #1, subtitle "Headless runs, reproducible CI invocations, and JSON
schema output as a build gate."

---

## 2. Meta

- **Length:** 1,600–1,900 words (7–8 min).
- **Audience:** engineers who write CI, platform people, anyone who has thought "this
  should be a pipeline step." Narrower audience than the rest of the series but a much
  higher-intent one.
- **Tags:** `AI`, `DevOps`, `Software Engineering`, `Developer Tools`, `Automation`
- **Series slot:** publish 9th.

---

## 3. Structure

### Lede (~150 words)
Open on the reframe with a one-liner that reads like every other unix tool:

```bash
cat build-error.txt | claude -p 'explain the root cause'
```

That is the whole idea. Everything else in the post is about making that invocation
*reproducible* and its output *machine-readable*.

### Section 1 — Four patterns you can use today (~450 words)
Each with the code and one sentence of why:

```bash
# 1. A diff as a convention linter — no shell access needed
git diff origin/main | claude -p 'report violations as filename:line'

# 2. Pipe a build log in, get a root cause out
cat build-error.txt | claude -p 'explain the root cause'

# 3. Reproducible in CI: skip local config discovery entirely
claude --bare -p "$PROMPT" --allowedTools "Read,Grep"

# 4. Machine-readable output for a gate
claude -p "audit changed endpoints for authorization gaps" \
  --output-format json \
  --json-schema '{"type":"object",
    "properties":{"findings":{"type":"array"}},
    "required":["findings"]}' | jq .structured_output
```

Recommend starting with pattern 1: a convention linter where a false positive costs
nothing. Nobody should learn this on a security gate.

### Section 2 — Why reproducibility needs `--bare` (~350 words)
The subtle point that will save readers a confusing afternoon. Without it, a headless run
auto-discovers whatever is on the machine: hooks, skills, plugins, connectors, instruction
files. That is exactly right interactively and exactly wrong in CI, because a teammate's
local configuration can change the pipeline result and you will spend a day on a difference
that has nothing to do with the code.

With bare mode, only the flags you pass take effect. State the trade-off honestly: you lose
your instruction files too, so anything the run genuinely needs has to be passed explicitly.

### Section 3 — Schema output as a real gate (~400 words)
The most valuable section. Walk through the progression:

1. Free prose — a human reads it. Useful, ungateable.
2. Structured output — a schema the run must conform to.
3. A pipeline step that parses it and exits non-zero on a condition you chose.

Show the whole gate, end to end:

```bash
findings=$(claude --bare -p "$PROMPT" \
  --output-format json --json-schema "$SCHEMA" \
  | jq '.structured_output.findings | length')

if [ "$findings" -gt 0 ]; then
  echo "review found $findings issue(s)"
  exit 1
fi
```

Then the caveats that keep this honest, because an unqualified version of this advice is
dangerous:
- The schema constrains the *shape*, not the *judgement*. A conforming response can still
  be wrong.
- Start advisory. Emit an artifact and let humans read it for a few weeks before anything
  blocks a merge.
- A gate people learn to ignore is worse than no gate. If the false-positive rate is not
  low, it should not be blocking.

### Section 4 — Guardrails for scripted runs (~250 words)
Four rules, short:
- `--allowedTools` explicitly, never blanket approval. A CI run should have the narrowest
  tool set that can do the job.
- A locked-down permission mode for unattended runs, and never the bypass mode.
- Max turns plus a job timeout, so a confused run cannot become a cost incident.
- Capture the session identifier so a run can be resumed and inspected.

Tie back to post 8 in one clause: the same tiers apply, and CI is exactly where nobody is
watching.

### Section 5 — In your own CI runners (~300 words)
A minimal job, generically written for a GitLab-style pipeline with a note that the shape
is the same elsewhere:

```yaml
stages: [ai]

review:
  stage: ai
  image: node:24-alpine
  rules:
    - if: '$CI_PIPELINE_SOURCE == "merge_request_event"'
  before_script:
    - apk add --no-cache git curl bash
    - curl -fsSL https://claude.ai/install.sh | bash
  script:
    - claude --bare -p "$AI_FLOW_INPUT" --allowedTools "Read,Grep"
  # API key supplied as a masked CI variable
```

What it unlocks: mentioning the agent in an issue or PR thread to get a branch and a draft
change; automated first-pass review on every PR event; cloud-provider identity instead of
static keys.

Then the honest constraint paragraph, which is the most useful thing here: this is a
destination, not next sprint's change. The realistic first step is a **read-only review job
that writes an artifact, not a comment.** Agent-authored PRs get reviewed like any other
contributor's. And check the maturity status before depending on it.

### Close (~150 words)
The progression to leave readers with: interactive → scripted → piped → gated. Each step
only makes sense once the previous one is boring. Forward link to post 10.

---

## 4. Genericizing notes

- All prompts and schemas are generic examples. No internal prompt text.
- The CI job is a rewritten minimal example; no internal variable names or project
  configuration.
- Do not state a specific company's policy on agent-authored PRs. Present the boundary as a
  recommendation.

---

## 5. Verify before publishing

- **Every flag in this post is a verification item:** `-p`, `--bare`, `--allowedTools`,
  `--output-format`, `--json-schema`, permission-mode names, max-turns. Check current docs
  and, ideally, run each one before publishing. This is the post where a stale flag is most
  visible and most embarrassing.
- The JSON output field name (`structured_output`) — confirm before shipping the `jq`
  examples.
- The install URL and the current maturity of platform CI integrations.
- Confirm the pipeline snippet is valid YAML and the image tag exists.

---

## 6. Hero image brief

Trust motif: a horizontal pipeline of three boxes — `git diff` → agent glyph → `jq` —
followed by a gate symbol splitting into a tick and a cross. Monospace labels. Large "09".

---

## 7. Traps

- Do not present a blocking AI gate as a good default. The advisory-first advice is what
  makes the post trustworthy.
- Do not skip the `--bare` reasoning; it is the single most useful paragraph here.
- Keep the platform-CI section short and clearly marked as forward-looking, since its
  maturity will have moved by the time anyone reads this.
