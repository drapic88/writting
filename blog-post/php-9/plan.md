# Plan — PHP 9 (working title: "The PHP 9 Upgrade Is Already in Your Error Log")

**Status:** brief, awaiting agreement. No `article.md` until this is agreed.
**Researched:** 2026-10-18, with PHP 8.6 at RC3 (RC4 due 22 October, GA 19 November 2026).

---

## Positioning

The PHP 8.6 post is the best performer on the Medium account by an order of magnitude, and
"when is PHP 9 coming, and what breaks?" is the obvious next question for that reader. The
search results for it are thin and partly wrong: posts claiming PHP 9.0 ships "later this
year", feature lists built from wishes, nobody pointing at the source tree.

The primary sources say something sharper and more useful:

- **PHP 9 is not the next release.** `master` was bumped to `8.7.0-dev` on 22 September 2026
  (php-src commit `7f8a74fb29`, "master is now for PHP 8.7.0-dev"), and `UPGRADING` on master
  is headed *PHP 8.7 UPGRADE NOTES*.
- **PHP 9 has no date.** The php-src "PHP 9" milestone has no due date and five items (three
  open, two closed). No RFC about 9.0's timing exists on the RFC index.
- **PHP 9's breaks are already decided.** The RFC index lists eleven accepted RFCs as
  *pending implementation* for 9.0, the oldest created in December 2020. Every one of them
  already does something observable on PHP 8.6 today.
- **Two of the biggest don't say "Deprecated".** I ran the 9.0-bound behaviours on the
  `php:8.6.0RC3-cli` image. Undefined variables and undefined properties — both voted to
  throw `Error` in 9.0 — still print a plain `Warning:` with no mention of 9.0, even though
  both RFCs said the next minor would change the message to warn about 9.0. That was in 2022;
  four minors later, it hasn't happened. Any scan that counts `Deprecated:` lines misses them.

That last point is the post's reason to exist. It's a gotcha nobody else has published, and
it's backed by a command anyone can rerun.

**Stands alone:** no reference to the 8.6 posts. A concept it needs (what an RFC vote is,
what `E_DEPRECATED` is) gets one sentence or is assumed knowledge for this audience.

## Thesis

PHP 9 has no release date, but its breaking changes are already voted, already running on
8.6, and already countable. **The PHP 9 upgrade is a list you can measure today — and the
two items most likely to break your app hide as warnings, not deprecations.**

## Title options

1. **The PHP 9 Upgrade Is Already in Your Error Log** — recommended. A claim, searchable,
   and the body delivers it literally.
2. **PHP 9 Isn't Next. Its Breaking Changes Are Already Here.** — leads with the surprising
   fact (8.7 is next); risks reading as a news item.
3. **PHP 9's Two Biggest Breaks Don't Say "Deprecated"** — sharpest, but narrows the post to
   one section.

Subtitle (for #1): *Master is 8.7-dev and PHP 9 has no date. Eleven accepted RFCs don't care —
and the two that will break the most code print warnings, not deprecations.*

Provenance line: *Checked against php-src `master` and the PHP RFC index on 18 October 2026,
and run on PHP 8.6.0 RC3. PHP 9.0 has no release date; if one is set, the list below may
grow but is unlikely to shrink.* (Re-check "unlikely to shrink" at drafting — no accepted
9.0 RFC has been reversed that I found, but say only what is verified.)

## Structure (standard long-form, 1,600–2,000 words, 6 sections)

### Lede (~200 words)
1. The question as people ask it — a search-box sentence, or the "PHP 9 is coming later
   this year" claim that circulates (quote the shape, not a named blog).
2. Honest answer up front: nobody can give you a date, because the next release is 8.7.
   Show the one-line evidence: `#define PHP_VERSION "8.7.0-dev"`.
3. Thesis in bold, once.
4. Roadmap: what "PHP 9" actually is today, the eleven decided breaks, the two that hide,
   the fixes, and how to count your own bill in ten minutes.

### 1. `PHP 9 is a list, not a date` (~250 words)
Evidence only: the version bump commit and its date, the milestone with no due date and its
five items (removal of long-deprecated mbstring INI settings, `proc_open()` resource →
object, `CONST_CS` removal…), the RFC index section. No speculation about when 9.0 ships —
say there is no RFC or announcement deciding it, and stop.

### 2. `The eleven decisions already made` (~350 words)
One table — the reader will screenshot it.

| 9.0 change | Warns since | Vote | What 8.6 prints today |
|---|---|---|---|
| Undefined variable throws `Error` | 8.0 (warning) | 33–8 | `Warning: Undefined variable $x` |
| Undefined property throws `Error` | 8.0 (warning) | 31–5 | `Warning: Undefined property: stdClass::$nope` |
| `${}` string interpolation removed | 8.2 | 31–1 | `Deprecated: Using ${var} in strings…` |
| Autovivification on `false` → `Error` | 8.1 | 34–2 | `Deprecated: Automatic conversion of false to array…` |
| Implicitly nullable params removed | 8.4 | 26–0 | `Deprecated: … Implicitly marking parameter $s as nullable…` |
| `Serializable` interface removed | 8.1 | 36–0 | `Deprecated: S implements the Serializable interface…` |
| Saner increment/decrement | 8.3 | *verify* | `Warning: Decrement on type null has no effect, this will change in the next major version` |
| GET/POST sessions removed | *verify* | *verify* | *run* |
| Overloaded-signature functions removed | *verify* | *verify* | *run* |
| Required param after optional → error | *verify* | *verify* | *run* |
| The 8.6 deprecations (filed under 9.0 on the index) | 8.6 | per sub-vote | *run a sample* |

The rows with real values are verified (RFC pages + RC3 run). The *verify*/*run* cells get
filled before drafting; any row I can't evidence gets dropped, not guessed.

### 3. `The two that don't say "Deprecated"` (~350 words) — the core section
- The RC3 output, verbatim, as a code block (from `exp-php9/rc3-output.txt`).
- The undefined-variable RFC's own text: the next minor version would change the warning to
  say it becomes an error in 9.0. Quote it (under 15 words). It hasn't happened through 8.6.
- Contrast: the increment/decrement warning *does* say "this will change in the next major
  version". So the engine knows how to warn about a major; these two just never got it.
- The gotcha, stated as an action: if your CI, your log alert or your upgrade script filters
  on `E_DEPRECATED` or greps `Deprecated:`, your PHP 9 count is missing its two largest rows.
- Limits: these are runtime-only. A static analyser catches many undefined variables, far
  fewer undefined properties on dynamic objects.
- **To verify before drafting:** how Laravel and Symfony treat `E_WARNING` by default (both
  are believed to turn warnings into exceptions in dev/test, which would surface these in a
  test suite but not in a production log). Do not claim either way until checked in the
  framework source.

### 4. `Before and after` (~300 words)
Three short code pairs, comments doing the pointing, each under ~10 lines:
- implicitly nullable → `?string $s = null`
- `${var}` → `{$var}`
- `Serializable` → `__serialize()` / `__unserialize()`
Name the Rector rule for each only if verified to exist under that name at drafting time;
otherwise say "Rector has a rule for this" and link the rule list.

### 5. `Playbook: count your PHP 9 bill today` (~400 words)
Numbered, with real commands, built from the probe run:
1. Run the suite on the newest 8.x with everything visible:
   `php -d error_reporting=E_ALL -d display_errors=1 vendor/bin/phpunit 2>&1 | tee php9.log`
2. Count both kinds — a grep that matches the exact strings from the RC3 output, including
   the two warnings.
3. Split own code from `vendor/` by path.
4. Static pass for what tests don't reach (PHPStan level and rule — verify names).
5. Fix the mechanical rows with Rector; the undefined-variable/property rows by hand.
No cost estimate of my own: no app was measured for this post. The playbook hands the
measuring to the reader — their count from steps 1–2 is their estimate, and the verdict's
threshold tells them how to read it.

### 6. `The limits` (~150 words)
Tests only see covered code; undefined properties are mostly a production discovery. The
list grows — every 8.x deprecations RFC adds rows (the 8.6 one is already filed under 9.0).
And this is the decided list, not the full 9.0: anything voted later lands on top.

### Verdict (~150 words)
Compressed thesis; what the evidence adds up to (9.0 is a backlog that has been accepted for
up to six years, not an event to wait for); one action with a threshold: run step 1–2 this
week and look at the two warning counts — zero means PHP 9 is a Rector run for you; any
non-zero undefined-property count means it's a production-logging project, start now.

### Sources
php-src `main/php_version.h` and commit `7f8a74fb29`; php-src milestone 6 ("PHP 9");
`UPGRADING` on master; the RFC index; each RFC linked from the table; php.net 8.6 RC
announcement.

---

## Evidence in hand

- `~/Projects/writting-experiments/exp-php9/p9.php` — probe script, one line per 9.0 change.
- `~/Projects/writting-experiments/exp-php9/rc3-output.txt` — its output on
  `php:8.6.0RC3-cli` (PHP `8.6.0RC3`).
- Vote counts and 9.0 behaviour, read from the RFC pages: undefined variable 33–8, undefined
  property 31–5, `${}` 31–1, autovivification 34–2, implicitly nullable 26–0,
  `Serializable` 36–0.

## Facts to verify at drafting time

- Re-run the probe on the newest RC (RC4 from 22 Oct) or GA; replace RC3 text if wording moved.
- The four *verify* rows in the table: RFC page, vote, and a probe line each.
- Milestone 6 contents and the RFC index section, same day as publishing.
- Laravel / Symfony default handling of `E_WARNING` (source, not blog posts).
- Rector rule names and PHPStan rule/level for undefined variables.
- The PHP license change: sources disagree on whether it's 8.6 or 9.0. Out of scope unless
  verified from the RFC, and even then probably one sentence at most.

## Out of scope

- Guessing a 9.0 release date, or what "might" be in it (generics, etc.). Only accepted RFCs.
- PHP 8.6 / 8.7 features.
- AI anything.
- Performance claims.

## Decided

- **This post owns PHP 9.** The `php-8.6-on-real-apps` brief keeps only two sentences on
  9.0-bound lines (decided 2026-10-18).
- **No local project run.** The post rests on primary sources (php-src, the RFC index, the
  RFC pages) and the ten-line probe script. A `symfony/demo` run on RC3 was tried and
  dropped: it showed zero 9.0-bound hits (a maintained showcase app is the best case), so it
  could not evidence the warnings-not-deprecations point.

- ~~Publish in 8.6 GA week (19 November 2026).~~ **Published on 2026-10-19**, a month early,
  against RC3.

## GA-week follow-up (the post is already live)

- Re-run `p9.php`, `p9b.php`, `p9c.php` from `exp-php9/` on the GA image and replace any
  message text in the article that moved; change the provenance line from RC3 to GA.
- Re-check the RFC index *Pending Implementation* section and milestone 6 on the day.
- Check whether an 8.7 deprecations RFC exists yet; the article says it hasn't been written.

## Medium meta

- Tags: `PHP`, `Programming`, `Software Engineering`, `Web Development`, `Backend`.
- Hero: the eleven rows as a strip, two of them highlighted as "Warning", the rest
  "Deprecated" — made after the table is final.

## Cost to produce

Filling the *verify* rows: one hour. Draft: one session. Hero and
voice check: one session.
