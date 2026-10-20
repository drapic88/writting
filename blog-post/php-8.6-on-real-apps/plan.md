# Plan — PHP 8.6 on real apps

**Status:** published on Medium on 2026-10-20 (brief revised 2026-10-18 after the first experiment run).
Public sources carry the argument; the local test run supports one section.

---

## Positioning

The Medium audience reads PHP. The PHP 8.6 post (9 Sep 2026) is the best performer by an
order of magnitude: 5.2K presentations, 1.7K views, 916 reads, against single-digit reads
for the AI posts that followed. This post goes back to that reader, timed for the window
around **PHP 8.6 GA on 19 November 2026**, when teams decide whether to upgrade.

It is a **readiness** post, not a features post. The run turned up something more useful
than a deprecation count: on 8.6 RC3 the language is ready, but the things around it
are not — dependency version caps, a framework's previous major, even the official Docker
image. Nearly all of that can be checked from public sources (Packagist, `composer.json`
files, php-src, framework PRs), so the reader can verify every claim without running
anything. The BookStack test run is the one section that shows what happens when you
push past those gates anyway.

Stands alone: no reference to the 8.6 feature post. A future PHP 9 post owns the 9.0
material; here it gets two sentences.

## Title

**PHP 8.6 Is Ready. Your Lock File Isn't.**

Subtitle (`###`): *I tried three real PHP projects on the 8.6 release candidate. Composer
refused all three before a single test ran — and the worst breakage was a warning
documented as a deprecation.*

Provenance line: *Written against PHP 8.6.0 RC3 (13 October 2026) and the package versions
current on 18 October. Version caps get lifted quickly near a release; I'll re-check every
one at GA.*

Alternatives if the caps are lifted before publishing: **Your PHP 8.6 Upgrade Is Waiting
on Someone Else's Release** · **The PHP 8.6 Upgrade Starts With `composer
check-platform-reqs`**.

## Thesis

When a PHP minor release is late for your project, the cause is almost never the release.
It's a `"php"` upper bound three levels down your dependency tree, or a framework that only
fixed 8.6 in its next major. **Your upgrade date is set by your dependency tree, not by
php.net** — and you can read that date off public metadata in fifteen minutes, weeks
before GA.

## Evidence in hand

All saved under `~/Projects/writting-experiments/exp-php86/` (`FINDINGS.md`, `raw/`).

**Public, link-checkable:**

1. **Composer refuses all three projects on 8.6.0RC3.** `composer check-platform-reqs`
   fails, and a fresh resolve gives "Your requirements could not be resolved":
   - `nette/schema` v1.3.6 (16 Aug 2026) declares `"php": "8.1 - 8.5"`; its `master`
     branch says the same. The chain is `symfony/demo` → `league/commonmark` 2.10 →
     `league/config` 1.2 → `nette/schema`, which also blocks `league/commonmark` itself.
   - `ezyang/htmlpurifier` v4.19.1 (15 Sep 2026) lists every minor up to `~8.5.0`; `master`
     is the same. It blocks BookStack, and so does `xemlock/htmlpurifier-html5`.
   - Neither repository has an issue mentioning 8.6 (`gh search issues`, 18 Oct).
2. **A "deprecation" that is a warning.** `UPGRADING` on the `PHP-8.6` branch says a
   `SessionHandlerInterface` class without `create_sid()` / `validateId()` now emits a
   deprecation. php-src `ext/session/session.c` (PHP-8.6, ~line 2967) calls
   `zend_error(E_WARNING, …)`, and RC3 does exactly that: the repro script prints
   `level=2 E_WARNING` (`raw/repro-session.txt`). Frameworks that promote warnings to
   exceptions turn it into a 500.
3. **Laravel fixed 8.6 in 13.x, not in 12.x.** 12.x `ArraySessionHandler` has neither
   method, while 13.x has both (laravel/framework#61469, merged 7 Sep 2026). 12.x
   `Container::build()` calls `spl_object_hash()`, which is deprecated in 8.6; the 13.x
   branch has no calls. "Experimental support for PHP 8.6" (#61771) was still open on
   18 Oct.
4. **The official image changed under you.** `php:8.6.0RC3-cli` ships without `mbstring`,
   because docker-library dropped PEAR for 8.6 and `--enable-mbstring` was tied to it
   (commit 536691f70, #1654). It is also always built ZTS (2e430cd1a, #1686).
5. **Even Composer complains on 8.6.** It prints deprecations for return-in-`finally` in
   `symfony/flex` and for the `MB_ONIGURUMA_VERSION` constant.

**From the run.** Vendor was installed on 8.4 and run on 8.6, which is what
`--ignore-platform-req=php` gets you:

| Project | Tests | 8.4.26 | 8.6.0RC3 |
|---|---|---|---|
| `symfony/demo` @ `8d2e2ef` | 53 | OK | OK, no new deprecations |
| `league/commonmark` 2.10.4 | 4,409 | OK | OK; the only new deprecations are 8.5's `setAccessible()`, in test code |
| BookStack v26.09.1 (Laravel 12.69.3) | 1,625 | OK | **23 errors, 10 failures** |

- BookStack's deprecation log grows from **162 lines to 84,447**, which is only 11 distinct
  messages. 83,887 of those lines are one line of Laravel: `Container.php:1112`,
  `spl_object_hash()`. The next biggest are `mb_split()` in `Str.php` (381), `is_a()` with
  a string in `intervention/image` (16), and `guzzlehttp/promises` declaring a class
  named `Is` (1). BookStack's own code adds nothing new under 8.6.
- **30 of the 33 failures are deprecation text printed into responses.** With CLI
  `display_errors` on, the notice lands inside zip and image bodies. With
  `display_errors=0`, 3 failures remain. One is the session warning turned into a 500.
  Another, the APNG test, hits the same warning when run alone. The third,
  `test_upload_limit_restricts_attachment_uploads`, also fails alone on 8.4, so it is
  order-dependent and not caused by 8.6. The post says so.

## Structure (standard long-form, 1,600–2,000 words)

**Lede.** Swap the image tag to `8.6-rc`, run `composer install`, and watch it refuse, three
projects out of three. The honest answer up front: PHP 8.6 itself broke nothing in two of
the three, and what broke the third had already been fixed, one framework major
later. Thesis in bold. Roadmap.

1. **`## The first wall is composer, not PHP`** — the two caps, the dependency chain as a
   short `composer why` block, and why maintainers cap (they list versions they've tested).
   Also what `--ignore-platform-req=php+` does and why it is a test tool, not a fix.
2. **`## A deprecation that is really a warning`** — the `UPGRADING` text against the php-src
   line, the six-line repro, and the 403 that became a 500. This is the gotcha section.
3. **`## Fixed upstream, one major later`** — Laravel 12 vs 13, with both PRs. The general
   point: an 8.6 fix can arrive only on a framework branch you haven't moved to yet.
4. **`## What happens when you push past it anyway`** — the supporting run, with the table
   above. 162 → 84,447 lines, 11 distinct, one line of vendor code. 33 failures shrink to 3
   with `display_errors=0`, and only one of those is real. Short, and it has to show its
   limits.
5. **`## The image changed too`** — `mbstring` missing and ZTS on, with the docker-library
   commits. Two paragraphs.
6. **`## Playbook: read your upgrade date before GA`** — numbered, real commands:
   1. `docker run --rm -v "$PWD":/app -w /app php:8.6-rc-cli composer check-platform-reqs`
      (adding `mbstring` first if the project needs it)
   2. `composer why <package>` for every `failed` line; check the package's `master`
      `composer.json` and its open issues.
   3. Check which framework branch carries 8.6 fixes.
   4. Run the suite with `--ignore-platform-req=php+`, `error_reporting=-1` and
      `display_errors=0`.
   5. De-duplicate the deprecation log (the `sed | sort | uniq -c` one-liner) and attribute
      each line to `vendor/<package>` or your own code.

   Cost estimate from the run: the BookStack suite took 75 s on 8.4 and 84 s on 8.6;
   measure the end-to-end check time for the playbook at drafting. No number goes in until
   it has been timed.
7. **`## The limits`** — three projects is not a survey. RC3 is not GA. Caps may be lifted
   any day. A test suite only sees the code it covers. And PHP 9 in two sentences: the
   session message itself says "required in PHP 9.0", which is why the warning is worth
   fixing now. No RFC list.
8. **`## Verdict`** — compressed thesis, then the action with a threshold: run
   `check-platform-reqs` on the RC image this week. No `failed` lines means your upgrade is
   an afternoon. Any `failed` line means your date is that maintainer's next release, so
   open or upvote the issue now rather than in November.

`### Sources` — php.net RC3 announcement; `UPGRADING` and `ext/session/session.c` on
php-src `PHP-8.6`; Packagist and GitHub for `nette/schema` and `ezyang/htmlpurifier`;
laravel/framework #61469 and #61771; docker-library/php #1654 and #1686; each project at
the commit tested.

## Facts to re-verify at drafting time

- **Every cap**: `nette/schema`, `ezyang/htmlpurifier` and the `master` constraints of both.
  If either is lifted, the post says when, and the title may change.
- Newest RC (RC4 is scheduled for 22 Oct). Re-run the suites on it, and on GA if the post
  ships after 19 Nov.
- Whether `UPGRADING` still calls the session change a deprecation, and whether
  RC4 still emits `E_WARNING`.
- Laravel 12.x: whether a patch release has added `create_sid()` or dropped
  `spl_object_hash()`; status of #61771.
- docker-library: still no `mbstring` in the 8.6 image?
- PHP 9.0 has **no release date**. Don't imply one.

## Out of scope

- 8.6 features (partial application, `Time\Duration`, `clamp()`).
- The full 8.6 deprecation list. Only the ones the run actually hit get named.
- PHP 9.0 detail beyond two sentences.
- A compile-time lint pass and the PHP 9 mapping of the counted lines. The first run didn't
  do them, and this argument doesn't need them.
- AI anything. Performance. Rector beyond a mention.
- Blaming maintainers. Caps are a reasonable policy, and the post says why.

## Medium meta

- Tags: `PHP`, `Laravel`, `Symfony`, `Programming`, `Software Engineering`.
- Publish: in the run-up to GA, after the re-check. The post is worth most before 19 Nov.
- Hero: the dependency chain as a diagram, `symfony/demo → league/commonmark →
  league/config → nette/schema "php": "8.1 - 8.5"`, with the last box marked as the wall.

## Cost to produce

Re-check facts and re-run on the latest RC: one to two hours. Draft: one session. Hero and
voice check: one session.
