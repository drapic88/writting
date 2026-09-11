---
name: voice-check
description: Audit a finished draft against the voice and craft specs and report what fails, with line numbers. Use for "check this draft", "is this ready to publish", "does this sound like me", "run the checklist", or before publishing any post, story or chapter. Reports; it does not rewrite unless asked.
---

# Checking a draft

An audit, not an edit. **Report the violations with line numbers and quote the offending
text. Do not rewrite unless Dragan asks for the fixes.** A draft silently "improved" toward a
house style is worse than one with a list of flagged lines.

## Load the right specs

Always [`VOICE.md`](../../../VOICE.md), plus:

| Draft lives in | Also read |
|----------------|-----------|
| `blog-post/` | [`blog-post/CRAFT.md`](../../../blog-post/CRAFT.md) §5 |
| `stories/` | [`stories/CRAFT.md`](../../../stories/CRAFT.md) §9 |
| `books/` | [`books/CRAFT.md`](../../../books/CRAFT.md) §8 |

Add [`CONFIDENTIALITY.md`](../../../CONFIDENTIALITY.md) §6 for anything from real work, and
[`CROATIAN.md`](../../../CROATIAN.md) §8 for a Croatian draft.

## Passes, in order

1. **The one rule.** Go paragraph by paragraph and ask what each claim points at. List every
   paragraph that asserts something and points at nothing. This is the pass that matters;
   the rest are hygiene.
2. **Anti-patterns.** Grep-level scan for the `VOICE.md` §5 register list, the banned
   openers, emoji, exclamation marks, and the fake "we". Quote each hit with its line.
3. **Structure.** Against the format's checklist: title is a claim with a verb, the honest
   answer is in the lede, the thesis is bold exactly once, a roadmap sentence exists, the
   close does its three moves and ends on an action with a threshold.
4. **Facts.** List every version number, model name, flag and command in the draft, and say
   which are verified, which are unverified, and which came from a source deck. Never mark
   something verified that you did not check.
5. **Format-specific.** Stories: the four qualifiers, two real-time scenes, no hero
   narrative, no moralising close. Books: ledger consistency, terms defined before use,
   promises resolved. Posts: series links resolve, tags present.
6. **Confidentiality**, where applicable. Names, aliases, dates, scrubbed artefacts,
   disclosure line.

## Report format

Group by severity, most serious first:

- **Blocking** — unevidenced claims, unverified facts stated as fact, confidentiality
  breaches, invented material.
- **Voice** — anti-pattern hits, register slips, hedge stacking, bold overuse.
- **Structure** — missing checklist items.
- **Nits** — grammar slips from `VOICE.md` §5, typos, inconsistent spelling convention.

Each entry: `file:line`, the quoted text, and one sentence on which rule it breaks. End with
a single sentence on whether the draft is publishable as it stands.

If nothing fails, say so plainly. A clean draft is a real outcome, not a prompt to find
something.
