# Plan — PHP 8.7 in progress (working title: "PHP 8.7 Is Being Decided Right Now")

**Status:** published on Medium on 2026-10-31 (agreed and drafted 2026-10-26).
**Researched:** 2026-10-20, with php-src `master` at `a17dcadd4c` (20 Oct 2026) and PHP 8.6 at
RC3 (RC4 due 22 October, GA 19 November 2026). **Re-checked 2026-10-26** at `219289d8e7`.

## Decided (2026-10-26)

1. **Title:** #1, *PHP 8.7 Has No Headline Feature Yet. Its Breaking Changes Already Landed.*
2. **Publish:** in the 19–26 Nov window, after 8.6 GA, with the open votes closed and their
   final tallies in.
3. **Playbook step 6 stays.** The check was quick: setup-php's README says `php-version: '8.7'`
   or `master` installs a nightly `8.7.0-dev` build from php-src `master` (setup-php v2,
   latest release 2.40.0, 8 Oct 2026).
4. **The opinion in section 2 stays an opinion,** stated in the first person.

## What moved between 20 and 26 Oct (the draft uses these numbers)

- `UPGRADING` on `master` now has **seven** BC entries. The two new ones are `Reflection*`
  `$name` / `$class` made readonly (`eef0f71aa7`, Kamil Tekiela, fixing GH-24147, no RFC) and
  `SoapClient` refusing cross-origin redirects (`7b3369c0c2`, Ilia Alshanetsky, GH-24315,
  security). Section 4 *Deprecated Functionality* is still empty.
- **IntlRelativeDateTimeFormatter passed 25–0–0** and merged as `c242f17cf4` (22 Oct). It
  ships with enums, so the constants-vs-enums objection from the first vote was resolved
  that way. It's the first entry under *Implemented → PHP 8.7* on the RFC index, which no
  longer reads `Placeholder`.
- **Number-base `Exception`:** 24–1–0, open until 2026-11-01 15:30 UTC.
- **`Filter\Filter` / `Filter\Flag` enums** went to vote: 2–10–0, open until
  2026-11-04 00:00 UTC.
- **PEAR:** 40–0–0 is final. The index lists it under *Accepted* and *Pending
  implementation*. No unbundling commit on `master` yet.
- **Deprecations for PHP 8.7:** still a draft, discussion thread "Not started yet".
- New on the index: *Context Managers, version 2* (draft, 23 Oct) and `array_partition()`
  (under discussion, 25 Oct). Neither is relevant to the argument.
- **Timed on BookStack** (`exp-php86/bookstack`): step 1 took 0.45 s and printed 42 lines;
  the step 2 grep took 2.3 s and found 0 lines in `app/` and 188 in `vendor/`, mostly
  `hexdec()` in UUID and image libraries. The 8.6 RC3 test logs of the same app
  (`exp-php86/raw/php86/`) contain no "Invalid characters passed" line. The suite took
  1:35.7 on RC3.
- `hexdec('1234-5678')` on `php:8.6.0RC4-cli` prints the deprecation and returns
  `int(305419896)` (`exp-php87/raw/hexdec-8.6.0RC4.txt`).

---

## Positioning

The PHP posts are where the account's reading time comes from, and the day after 8.6 GA the
reader's question is "what's next?". The search results for it will be what they always are:
wish lists of generics and "PHP 9 is coming", built from nobody's source tree.

The primary sources say something narrower and more useful:

- **Master has been 8.7 for four weeks.** Matteo Beccati's commit `7f8a74fb29`
  (22 Sep 2026, "master is now for PHP 8.7.0-dev") bumped `main/php_version.h`. His
  "PHP 8.6 forked" mail to internals (externals.io/message/132585) has the line "Feature
  freeze is on."
- **8.7 has no headline feature yet.** `UPGRADING` on `master` holds 21 entries. Five are
  backward-incompatible, ten are performance work, and section 4 *Deprecated Functionality*
  is empty. None of the 21 is a language change. The RFC index's *Implemented → PHP 8.7*
  heading says only `Placeholder`.
- **The breaking half of 8.7 doesn't wait for a vote.** Four of the five BC entries came in as
  ordinary commits (curl ×2, PDO, session). Since April 2026 the BC policy has explicitly
  exempted input type and value validation, so a new `TypeError` or `ValueError` in a minor
  release needs no RFC. That policy RFC passed 26–5–3. The fifth BC entry, the
  `php://filter` limit, is the second step of an 8.6 RFC (30–0–2): a deprecation in 8.6
  that becomes an error in 8.7.
- **The feature half needs two-thirds, and this summer the big syntax proposals didn't get
  it.** Bound-erased generics lost 7–19–10. The pipe assignment operator got more yes than
  no votes, 14–12–7, and still failed the 2/3 bar. Function autoloading lost 2–11–1, and
  `__exists()` 2–13–7. What passes is small and library-shaped. End PEAR endorsement passed
  40–0–0 on 19 Oct, IntlRelativeDateTimeFormatter stands at 22–0–0 and the number-base
  `Exception` at 17–0–0.

That split is the post's reason to exist. A reader who wants to know what 8.7 will break
should read section 1 of `UPGRADING` every month, not the RFC vote list. A reader who wants
to know what 8.7 will *add* can read the vote list, and it's a short one. Nobody else is
showing those two tracks side by side with the numbers.

**Stands alone.** No reference to the 8.6 or PHP 9 posts. Each concept it needs (what an
RFC vote is, the 2/3 rule, what `UPGRADING` is) gets one sentence inside the post.

## Thesis

PHP 8.7 is eleven months from GA and its shape is being set now, in two places that move at
different speeds. The breaking changes arrive as commits, weekly, under a policy that lets
type and value validation skip the vote. The features arrive by 2/3 vote, slowly, and this
summer every big syntax proposal lost. **What PHP 8.7 breaks is decided in commits; what it
adds is decided in votes, and the votes have mostly said no.**

## Title options

1. **PHP 8.7 Has No Headline Feature Yet. Its Breaking Changes Already Landed.** —
   recommended. A claim in two sentences (the expectation, then the correction), and the body
   proves both halves with `UPGRADING` and vote counts.
2. **PHP 8.7 Is Being Decided Right Now** — the working title. True and timely, but it names
   a topic rather than taking a position, and CRAFT wants a claim.
3. **PHP 8.7's Breaking Changes Don't Need a Vote** — the sharpest. It narrows the post to
   the policy half and could read as an accusation, which the post doesn't intend. The
   policy has a stated security rationale, and the post says so.

Subtitle (for #1): *Four weeks into the 8.7 cycle, master has five breaking changes, an empty
deprecations section, and no new syntax. This summer's language RFCs went 0 for 4. Here's
what's in, what's voting, and when the door closes.*

Provenance line: *Checked against php-src `master` at `<hash>` and the PHP RFC index on
<publish date>. Vote counts on open RFCs change daily. Every number below has the date it was
read.*

## Structure (standard long-form, 1,600–1,900 words, 7 sections)

### Lede (~200 words)
1. The dated trigger: 8.6 shipped on 19 November and the "what's in 8.7?" posts started the
   same week. Quote the shape of the claim ("8.7 brings generics…"), not a named blog.
2. The honest answer up front: as of <date>, 8.7 adds no new syntax, and the one generics
   RFC voted this year lost 7–19. One line of evidence: the RFC index's *PHP 8.7* section
   reads `Placeholder`.
3. Thesis in bold, once.
4. Roadmap: what is on master, how it got there without a vote, what is voting now, what
   lost, and the dates that close the door.

### 1. `What's on master: 21 lines and no new syntax` (~300 words)
A compact table of `UPGRADING` section 1 (the five BC entries), each with its php-src commit
and its route in:

| BC change in 8.7 | Commit | Route |
|---|---|---|
| `curl_multi_exec()` throws `TypeError` when `still_running` is not an int | `90a65ec8cb` (GH-24067) | commit, validation |
| Nested arrays in `CURLOPT_POSTFIELDS` throw `TypeError` instead of becoming `"Array"` | `2544d0b7d9` (GH-22740) | commit, shipped with the multi-file upload feature |
| `PDOStatement::bindColumn()` throws `ValueError` for an unknown column | `7f1e8cb37b` (GH-23835) | commit, validation |
| `session.cookie_path` / `cookie_domain` reject `;` CR LF etc. with a warning | `b9a0228bd8` (GH-22925) | commit, security |
| `php://filter` URL limited to 16 filters | `ee739e842b` | 8.6 RFC, step 2 (30–0–2) |

Then one paragraph on the rest: new features in curl, intl and streams, `IntlNumberFormatter`
(commit `a14b9f352f`), and ten performance entries such as `htmlspecialchars()` returning its
input uncopied (Nicolas Grekas, `5b765f4b68`). End on the empty section 4. That gap is a
timing fact, not a quiet cycle, and section 4 explains why.

### 2. `How a breaking change gets in without a vote` (~300 words)
- The policy RFC *Exempt input type and value validation from BC Break policy* (Gina Peter
  Banyard, accepted 2026-04-04, 26–5–3). Quote its reason in under 15 words: missing
  validation has caused security advisories, and it links three GHSAs.
- The release-process rule that extension features need no RFC unless a core developer
  objects within one month of the PR (php/policies `release-process.rst`).
  `IntlNumberFormatter` is the example. It was discussed on internals (132820), not voted.
- Position, stated as an opinion: I think this is the right policy. A `TypeError` today beats
  a silent behaviour change when a library adds a flag. The cost is that the 8.7 breaking
  list never appears on the RFC page people watch.
- The gotcha, as an action: a `catch (PDOException)` around `bindColumn()` won't catch a
  `ValueError`.

### 3. `What's voting now` (~300 words)
A table with the date each count was read. **Every number in it is re-checked on publish day.**

| RFC | Target | Vote (20 Oct) | Closes |
|---|---|---|---|
| End PEAR Project Endorsement (unbundle PEAR from php-src in 8.7) | 8.7 | 40–0–0, **accepted** | closed 2026-10-19 13:15 UTC |
| IntlRelativeDateTimeFormatter | 8.7 | 22–0–0 (open) | 2026-10-22 00:00 UTC |
| Exception for invalid characters in `bindec()`/`octdec()`/`hexdec()`/`base_convert()` | 8.7 | 17–0–0 (open) | 2026-11-01 15:30 UTC |

- The number-base RFC is the story inside this table. Base Convert Improvements deprecated
  invalid characters in **7.4** "with the intention of eventually turning it into an
  exception in PHP 8". That never happened, and 8.7 is the one that finally does it. It
  throws a plain `Exception`, not a `ValueError`. Version 0.3 of the RFC changed it on
  purpose, so `catch (\Error)` won't catch it. Show the before/after `hexdec('1234-5678')`.
- One paragraph on process texture. The IntlRelativeDateTimeFormatter vote first opened in
  September (due to close 2026-09-29), then was withdrawn and reopened (132504 → 132830) after Tim Düsterhus pointed out
  the RFC text had changed during the cooldown. PREG_THROW_ON_ERROR's vote (closing
  2026-09-18) was restarted after a late objection. These show that a 2/3 vote is not a
  formality.
- Under discussion with an explicit 8.7 target, in one line each, no tallies:
  PREG_THROW_ON_ERROR, `Io\Terminal`, `Time\Instant`/`Time\Clock`, Polling API additions,
  IO hooks, opt-in JSON comments and trailing commas, `ext/csv`, short array variable
  shorthand, `Filter\Filter` enums, case-insensitive `ini_get_all()`. The **Deprecations for
  PHP 8.7** RFC is a draft with three items (`is_a()` / `is_subclass_of()` with non-string
  non-object, the `b` string prefix) and no discussion thread yet.

### 4. `What lost, and by how much` (~250 words)
The four syntax proposals voted this summer, with counts and close dates: generics 7–19–10
(28 Jun), `__exists()` 2–13–7 (28 Jun), pipe assignment 14–12–7 (11 Aug), function autoloading
2–11–1 (13 Aug). The point is the 2/3 bar. Pipe assignment had a majority and lost. All four
targeted 8.6, so for 8.7 they're dead unless re-proposed. The post says that and does not
speculate on who will re-propose.
Also note, without making a story of it: primary constructors, literal scalar types and
pattern matching (`is`) are under discussion with no vote opened. Pattern matching's RFC was
created on 2020-11-11.

### 5. `The calendar: when the door closes` (~250 words)
- Verified: no `todo/php87` page exists on the wiki (20 Oct, "This topic does not exist
  yet"). No 8.7 release managers have been chosen. Policy starts that process "about four
  months prior" to alpha 1, in early March, with the vote in early April.
- Computed from php/policies `release-process.rst`, labelled as computed. Alpha 1 is tagged
  on the first Tuesday of July and released two days later, which in 2027 gives **8 Jul 2027**.
  Feature freeze (Beta 1) is `$rd + 42`, **19 Aug 2027**. GA is `$rd + 140`,
  **25 Nov 2027**. The 8.6 timetable matched this formula exactly (alpha 1 on 2 Jul 2026,
  freeze tag on 11 Aug, GA on 19 Nov), which is the evidence the formula is used.
- The pattern that matters for readers: 8.6's deprecations RFC opened discussion on
  22 Jun 2026 and closed its votes on 10 Aug 2026, three days before Beta 1. **The deprecation
  list is decided last.** Expect 8.7's in June–August 2027, not now.
- PHP 9 in two sentences. A major bump needs its own RFC, decided before the RMs are
  selected and "at least 6 months prior to the planned alpha release" (early January 2027
  for a July alpha). No such RFC is on the index, so the next release is 8.7 unless that
  changes in about eleven weeks.

### 6. `Playbook: track 8.7 in ten minutes a month` (~300 words)
Numbered, real commands:
1. Read the breaking section straight from master:
   `curl -s https://raw.githubusercontent.com/php/php-src/master/UPGRADING | sed -n '/^1\. Backward/,/^2\. New Features/p' | tail -n +3`
   (the `tail` skips the table of contents, which matches the same two headings)
2. Grep your code for the five entries: `php://filter`, `CURLOPT_POSTFIELDS`,
   `bindColumn(`, `session.cookie_path`/`cookie_domain`, `hexdec|octdec|bindec|base_convert`.
3. Run your suite on 8.6 with deprecations visible and look for "Invalid characters passed
   for attempted conversion". Every hit becomes an `Exception` in 8.7 if the vote holds.
4. Watch the votes. The wiki's *In voting phase* section, and externals.io's RFC feed
   (`/rss-rfc`).
5. If an RFC changes your code, the discussion phase is where comments land, before the vote.
6. Optional: run the suite against `master`. **How to get an 8.7-dev binary is open**: no
   official Docker tag was checked, and setup-php's nightly support is unverified. Either
   verify one route or drop the step.

Cost estimate: steps 1–3 timed on one real project at drafting. No number goes in untimed.

### 7. `The limits` (~150 words)
A four-week-old master is not 8.7. Anything can land until 19 Aug 2027 and, with RM
blessing, after it. Open votes can flip until they close. The calendar dates are computed
from policy, not announced. And `UPGRADING` is written by the people who commit, so an
omission is possible. Point at the commit log as the ground truth.

### Verdict (~150 words)
Compressed thesis. What the evidence adds up to: 8.7 so far is a cleanup release with real
breaking edges, and the features people expect from it lost their votes. The action, with a
threshold: run steps 1–3 this week. Zero hits means 8.7 is a non-event for you so far, so
check again in March, when the RM call goes out. Any hit on the number-base deprecation means
you have a change that is already voted (if the 1 Nov tally holds), so fix it on 8.6 now.

### Sources
php-src commit `7f8a74fb29`, `main/php_version.h` and `UPGRADING` on `master` at the publish
hash; each BC commit in the table; the RFC index; each RFC linked from sections 2–4;
php/policies `release-process.rst`; wiki `todo/php86`; internals threads 132495, 132585,
132789, 132504, 132830, 132426.

---

## Evidence in hand

Saved under `~/Projects/writting-experiments/exp-php87/`:

- `raw/UPGRADING-master-a17dcadd4c.txt` (161 lines) and `raw/UPGRADING-PHP-8.6.txt`.
- `raw/wiki/`: the RFC index and raw source of every RFC cited, plus `todo86.txt`.
- `raw/vote-tallies-2026-10-20.txt`: closed-poll tallies parsed from the rendered pages by
  `votes.py`. The two open polls were counted by hand from the same pages: reldate 22–0–0,
  number base 17–0–0.
- `raw/release-process.rst`: php/policies, read 2026-10-20.
- `raw/internals/`: the externals.io threads listed under Sources.

**Verified on 2026-10-20:** the bump commit and date; the 21 `UPGRADING` entries and their
sections; the commit behind each BC entry; every vote count and close date quoted above;
the RFC index *PHP 8.7* `Placeholder`; that no `todo/php87` page exists; the release-process
formulas and the 8.6 timetable's match to them; the BC-exemption policy text and vote; the
7.4 history in the number-base RFC; the 8.6 RMs (Beccati, Ferguson, Scherzer, per 132495).

## Re-check on publish day (the numbers that move)

- **Both open votes:** IntlRelativeDateTimeFormatter (closes 22 Oct) and number base
  (closes 1 Nov). Report the final tallies. If either fails, the section changes.
- **PEAR:** whether the RFC index has moved it to *Accepted*, and whether the php-src
  unbundling PR has merged on `master`. That would make a sixth `UPGRADING` line.
- **`UPGRADING` on `master`:** re-count entries and re-read section 1 and section 4. New BC
  lines go in the table, and the headline count changes.
- **Deprecations for PHP 8.7:** still a draft? Discussion started? Item list.
- **Under-discussion RFCs** with an 8.7 target: any that moved to voting get a row and a
  dated tally.
- **RFC index *PHP 8.7* section:** still `Placeholder`?
- **Any 9.0 version-bump RFC** on the index (none on 20 Oct).
- **`todo/php87`** page and any RM call (not expected before March 2027).
- Replace `<hash>` and `<publish date>` in the provenance line.
- **Draft-specific (2026-10-26):** the lede says "PHP 8.6 shipped on 19 November". Confirm
  GA happened on that date. "Two months into the 8.7 cycle" in the subtitle assumes a
  late-November publish. The step 1 "42 lines" and the "two RFCs" in *In voting phase* are
  26 Oct figures.
- **Hero (made 2026-10-26):** shows the seven BC entries and only closed votes. If `master`
  gains a BC entry before publishing, add its row to `hero.svg`, update "seven" in the alt
  text, and re-export.

## Open questions for Dragan

1. **Title:** #1 (recommended), the working title, or #3?
2. **Publish timing:** the 19–26 Nov window means the two open votes will have closed. Is that
   fine, or should the post go out earlier to catch the votes live?
3. **Step 6 of the playbook:** spend an hour verifying an 8.7-dev binary route (build from
   source in Docker, or setup-php nightly), or drop the step?
4. **The opinion in section 2:** I've written "this policy is right". Keep it, soften it,
   or cut it?

## Out of scope

- Speculation about what 8.7 "might" get. Only RFCs with a page, a target and a status.
- Re-litigating the declined RFCs or their authors. Counts and dates only.
- PHP 9 beyond the two sentences in section 5.
- 8.6 features and upgrade advice.
- AI anything. Performance claims beyond quoting `UPGRADING` section 14.

## Medium meta

- Tags: `PHP`, `Programming`, `Software Engineering`, `Web Development`, `Backend`.
- Member-only. Publish in 8.6 GA week (19–26 Nov 2026).
- Hero: two lanes, "commits" and "votes", each feeding a box marked `8.7`. The commit lane
  carries five BC items. The vote lane shows the summer's 0-for-4 tallies struck through and
  the three passing library RFCs. Made after the publish-day re-check fixes the numbers.

## Cost to produce

Publish-day re-check: one hour. Timing playbook steps 1–3 on a real project: thirty
minutes. Draft: one session. Hero and voice check: one session.
