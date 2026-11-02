# Plan — Composer audit blind spots (working title: "Composer Says Your Dependencies Are Fine. Here's What It Didn't Check.")

**Status:** published on Medium on 2026-11-02 (agreed and drafted 2026-10-26).

**Decisions (Dragan, 2026-10-26):**

- Lead with the audit / maintenance / majors angle. The PHP 8.6 caps get one section only,
  to limit overlap with the published lock-file post.
- Keep the working title.
- Use the app list below; drop Monica if its stale lock skews the comparison.
- Run the commands on the remaining apps first. The article reports only what was measured.

**Run note (2026-10-26):** all eight apps measured, results in
`~/Projects/writting-experiments/exp-composer-audit/FINDINGS.md` ("Full run"). Monica was
dropped: its lock dates from 9 Aug 2025, and its 61 advisories would have been most of the
total. The brief's premise didn't hold. Only BookStack passes `composer audit`; the other six
fail on advisories (9 of 22 published after the lock was committed) or on flagged abandoned
packages. The article says so in the lede and keeps the title, because the quiet-package
finding (55 unflagged against 37 flagged) is the part audit never covers.
**Researched:** 2026-10-20, against Composer 2.10.3 (27 August 2026, the latest release) and
PHP 8.6.0 RC3. One feasibility probe run, on BookStack; the other apps are not yet measured.

---

## Positioning

Medium readers on this account come for PHP, and the posts that earn are release-timed. This
one sits in the run-up to **PHP 8.6 GA on 19 November 2026**, when teams look at their
dependencies and the first command most of them run is `composer audit`. It answers a
question nobody has measured in public: what does a green `composer audit` actually certify,
and what does a real app's lock file carry past it?

It is a **tooling** post, not a release post. It has a release hook (PHP version caps that
block 8.6), but the argument still holds after GA, which gives it a longer tail than a
pure 8.6 post.

**A correction to the original idea, found during research.** The pitch assumed a clean
audit can still contain abandoned packages. By default it can't: since Composer **2.7.0**
(8 Feb 2024, #11643) `audit.abandoned` defaults to `fail`, so a package flagged abandoned on
Packagist makes `composer audit` exit non-zero. A "clean" audit therefore already means zero
*flagged* abandoned packages. The blind spot is narrower and better: audit only reads lists
that someone has to publish — an advisory, an abandoned flag, a malware entry. A package
whose maintainer walked away without flagging it, a package whose `"php"` constraint stops
at 8.5, a package two majors behind: none of those are on any list, so none of them can fail
an audit. The post has to state this correctly, because readers who know the default will
otherwise stop trusting it at paragraph three.

**Stands alone.** No reference to the PHP 8.6 posts already published, even though the caps
section overlaps with one of them (see open questions). Every concept it needs — what the
lock file records, what `require.php` is, what Packagist's abandoned flag is — gets one
sentence inside the post.

## Title

**Composer Says Your Dependencies Are Fine. Here's What It Didn't Check.** (working title,
kept: it's a claim with a verb, and the false-belief / correction shape works.)

Alternatives:

- **A Clean `composer audit` Is a Short List, Not a Clean Bill of Health**
- **`composer audit` Only Knows What Someone Reported**
- **Your Lock File Passed the Audit. It Still Can't Run PHP 8.6.** (strongest if the caps
  number holds across the apps; most release-timed)

Subtitle options (`###`):

- *I ran Composer's audit on the lock files of N popular PHP apps. All passed. Between them
  they still carried X packages capped below PHP 8.6, Y with no release in two years, and Z
  a major version behind.* (numbers from the run; no number goes in until it's measured)
- *Audit reads three lists: advisories, abandoned flags, malware. Here's what a real lock
  file carries that's on none of them.*

Provenance line: *Written against Composer 2.10.3 and PHP 8.6.0 RC3, with each app's lock
file as committed on [date]. Lock files and version caps change weekly; the commit hash for
each app is in the sources.*

## Thesis

`composer audit` checks your lock file against lists other people publish: security
advisories, Packagist's abandoned flag and, since 2.10, malware filter lists. A clean result
means nobody has *reported* a problem. **A green audit is a statement about the lists, not
about your dependencies** — and three questions every upgrade depends on (is this package
still maintained, will it install on the next PHP, how far behind am I) are on none of them.
Composer can answer two of the three already, with commands most teams never run, and one
of those commands hides most of its answer.

## Evidence in hand

Saved under `~/Projects/writting-experiments/exp-composer-audit/` (`FINDINGS.md`, `raw/`,
`tools/analyse.php`, `apps/bookstack/`).

**Composer behaviour, verified against the changelog and docs at tag 2.10.3**
(`raw/composer-CHANGELOG.md`, `raw/composer-2.10.3-doc-03-cli.md`,
`raw/composer-2.10.3-doc-06-config.md`):

1. `audit` arrived in **2.4.0-RC1** (21 Jul 2022, #10798), with an automatic audit after
   `update`.
2. `audit.abandoned` arrived in **2.6.3** (15 Sep 2023, #11639), defaulting to `report`; the
   default became **`fail` in 2.7.0** (8 Feb 2024, #11643). The `--abandoned=ignore|report|fail`
   flag came in **2.8.0** (#12091).
3. **2.9.0** added blocking at update time: `audit.block-insecure` (default `true`) and
   `audit.block-abandoned` (default `false`).
4. **2.10.0** (28 May 2026): malware filter lists, blocked at `install` by default; a new
   `config.policy` block that deprecates most of `config.audit`; and the audit exit code is
   now only 0 or 1 (#12881). Before 2.10 it was 1 / 2 / 3 for vulnerable / abandoned / both
   (#12203). A CI script that branches on exit code 2 silently changed meaning in May.
5. `composer outdated` has `--locked`, `--direct`, `--major-only`, `--sort-by-age` (`-A`) and
   JSON output with `release-date` and `latest-release-date` (added **2.7.8**, #12053).
   `composer show --locked --latest --format=json` gives the same fields plus `abandoned`
   for every package, without a `vendor/` directory.
6. **Not released:** the docs on Composer's `main` branch describe a `cooldown` policy and an
   `outdated --cooldown-period` option. Neither is in the 2.10.3 docs or the changelog. The
   post must not present them as available.

**The probe: BookStack** (`development` at `045c6a9`, lock last changed 10 Oct 2026), lock
file only, no `vendor/`. Output in `raw/bookstack-probe.txt` and
`raw/bookstack-analysis.json`.

| Measure | Result |
|---|---|
| Locked packages | 149 (113 prod, 36 dev) |
| `composer audit --locked` | "No security vulnerability advisories found.", exit 0 |
| Flagged abandoned | 0 |
| Latest release older than 2 years | 18 (12 older than 3) |
| …of which the GitHub repo saw no push in 2 years | 8, and 6 of those are PSR interface packages |
| GitHub source repo archived | 0 of 146 |
| A major version behind | 7, all production (`guzzlehttp/guzzle` 7→8, `phpseclib/phpseclib` 3→4, `intervention/image` 3→4, …) |
| Locked `require.php` excludes 8.6.0 | **4**, all production |
| Locked `require.php` excludes 8.7.0 | 5 |

The four packages that won't install on 8.6: `ezyang/htmlpurifier` (`~8.5.0` is its highest
range), `league/oauth2-client` (`>=8.0.0 <8.6.0`), `nette/schema` (`8.1 - 8.5`) and
`nette/utils` (`8.2 - 8.5`).

**The gotcha the probe turned up.** On `php:8.6-rc-cli` (8.6.0RC3),
`composer check-platform-reqs --lock --no-dev` prints **one** failing `php` line, naming
`ezyang/htmlpurifier`. The other three packages that exclude 8.6 aren't shown. That's by
design: Composer 2.10.3 `src/Composer/Command/CheckPlatformReqsCommand.php` (~lines
121–151) stops at the first failing link per platform package — the source comment reads
"show the first error from every failed candidate". Fix one cap, re-run, find the next. A
reader using it as an upgrade checklist sees a quarter of the list. (`raw/bookstack-platform-86.txt`)

**What the probe says about the metrics.** "No release in two years" is a noisy signal on
its own: most of BookStack's 18 are finished PSR interfaces (`psr/container`, `psr/log`,
`psr/http-message`) that have nothing left to release. The post needs the second filter (no
push to the source repo either) and an explicit "finished by design" exclusion, or it will
call `psr/log` dead. The 9.0 cap count (71) is meaningless — `^8.1` excludes 9.0 by
construction — and stays out of the post.

**Honest reading so far:** BookStack is a well-kept lock. Its dead weight is small (two
genuinely quiet packages: `dflydev/dot-access-data` and `ralouphie/getallheaders`). Its real
exposure is the four PHP caps, all transitive. If the other apps look the same, the post's
weight shifts toward caps and `check-platform-reqs`, and the "unmaintained" section shrinks.
That's an acceptable outcome; inflating it is not.

## App selection

Every candidate below has a committed `composer.lock` on its default branch (checked
20 Oct with `gh api repos/<repo>/contents/composer.lock`). Criteria: an application, not a
library (libraries don't commit locks); popular enough that readers know it; actively
maintained, so a finding isn't "an old project is old"; and a spread of frameworks.

| App | Framework | Stars | Lock last changed | Why |
|---|---|---|---|---|
| BookStack | Laravel 13 | 19.1K | 10 Oct 2026 | probed; well-kept baseline |
| Firefly III | Laravel | 24.9K | 11 Oct 2026 | large, active, finance |
| Akaunting | Laravel | 10.2K | 15 Sep 2026 | named in the pitch; accounting |
| Monica | Laravel | 25.5K | **9 Aug 2025** | named in the pitch; the stale-lock case |
| Kimai | Symfony | 5.1K | 19 Oct 2026 | Symfony counterweight |
| Wallabag | Symfony | 13.0K | 19 Oct 2026 | Symfony, long-lived codebase |
| `symfony/demo` | Symfony | 2.6K | 1 Sep 2026 | the reference app; small, a floor |
| Matomo | own | 22.0K | 28 Sep 2026 | not Laravel or Symfony |

Proposed: these eight. Monica is deliberately included as the outlier — a 25K-star app whose
lock hasn't moved in fourteen months. Its numbers get reported separately so one stale lock
doesn't drive the totals. Snipe-IT, Koel, Pixelfed, Invoice Ninja, Mautic and FreshRSS also
have locks and are reserves.

The post names the apps (they're public and the lock files are checkable) but never frames
a finding as the maintainers' failure. A cap is a maintainer listing the versions they've
tested; a quiet package is often finished. The target is the reader's assumption about what
audit covers.

## Exact commands

Pinned per app: record the default-branch commit, fetch `composer.json` and `composer.lock`
at that commit into `apps/<app>/`, run everything with `--locked` / `--lock`, never install.

```bash
# PHP 8.4.26 + Composer 2.10.3 (writting-experiments-php:8.4)
composer audit --locked                                  # the headline: what "clean" says
composer audit --locked --format=json > audit.json
composer outdated --locked --direct                      # what the reader would see
composer show --locked --latest --format=json > show-latest.json
composer check-platform-reqs --lock --no-dev             # on 8.4: baseline

# PHP 8.6.0 RC (php:8.6-rc-cli, Composer phar mounted)
php composer.phar check-platform-reqs --lock --no-dev    # count the php lines it prints

# all metrics, from the three files above
php tools/analyse.php apps/<app> <date>
```

Plus, per package with an old latest release: `gh api repos/<owner>/<repo>` for `archived`
and `pushed_at`. All of it is scripted already for BookStack; extending to eight apps is a
loop.

## Metrics (per app, then totals with Monica separate)

1. **Advisories** and **flagged abandoned** — expected 0 for most; this is the "audit is clean" row.
2. **Quiet**: latest release older than 2 years *and* no push to the source repo in 2 years,
   minus a published "finished by design" list (PSR interfaces, polyfills). Report the
   exclusion list in the post.
3. **Archived** source repos — the strongest "dead but unflagged" signal. 0 for BookStack.
4. **A major behind** (`latest-status` = `update-possible`), production only.
5. **PHP caps**: locked `require.php` that excludes 8.6.0, and separately 8.7.0. Evaluated
   with `composer/semver`'s `Semver::satisfies()`, the library Composer itself uses.
6. **Caps shown vs caps present**: `php` failure lines printed by `check-platform-reqs` on
   8.6 RC against metric 5. This is the gotcha in numbers.
7. **Time cost** of the whole check per app, timed, for the playbook's cost estimate.

## Structure (standard long-form, 1,600–2,000 words)

**Lede.** Audit prints "No security vulnerability advisories found." for all N apps. The
honest answer up front: that line is true and narrow, and the same lock files carry X caps
that refuse PHP 8.6 four weeks before GA. Thesis in bold. Roadmap: what audit actually
reads, what it can't see, the command that hides most of its answer, and a fifteen-minute
check.

1. **`## What a clean audit actually certifies`** — the three lists, the 2.7 default that
   makes abandoned packages fail, and the 2.10 exit-code change. Short; this section buys
   credibility with readers who know Composer.
2. **`## The table: N apps, all green`** — one table, every app, metrics 1–5. Monica in its
   own row with its lock date.
3. **`## Quiet is not the same as abandoned`** — the abandoned flag is opt-in, set by the
   maintainer. The two-filter method, the PSR exclusion, and the real quiet packages by name.
   The limit: a quiet package may simply be finished.
4. **`## The caps nobody's audit sees`** — `require.php` upper bounds, all transitive, with
   one `composer why` chain. Why maintainers cap (tested versions) and why audit never will
   check it.
5. **`## check-platform-reqs shows you one at a time`** — the gotcha. The four-vs-one
   output, the source lines, and the workaround (metric 5's script, or loop
   `composer why-not php 8.6.0`; verify that command's output shape at drafting).
6. **`## Playbook: read what audit didn't`** — numbered, real commands, ends on a timed
   cost estimate:
   1. `composer audit --locked` — keep it, know what it covers.
   2. `composer show --locked --latest --format=json` and sort by `latest-release-date`.
   3. Check `archived` / last push for anything older than two years.
   4. `composer outdated --locked --major-only` for production.
   5. Check every package's `require.php` against the next PHP version, not just the first
      failure `check-platform-reqs` prints.
7. **`## The limits`** — eight apps is not a survey; a lock is a snapshot; "two years" is a
   chosen threshold; caps get lifted near a release, so the 8.6 numbers are a dated reading.
8. **`## Verdict`** — compressed thesis, then the action with a threshold: run the cap check
   against 8.6 this week. Zero excluded packages means your audit was telling you most of
   the story. Any excluded package means your 8.6 date is that maintainer's next release.

`### Sources` — Composer CHANGELOG (2.4.0, 2.6.3, 2.7.0, 2.8.0, 2.9.0, 2.10.0), Composer docs
for `audit`, `outdated`, `check-platform-reqs` and `config.policy` at 2.10.3;
`CheckPlatformReqsCommand.php` at tag 2.10.3; Packagist pages for each capped package; each
app's repository at the commit tested; the php.net RC announcement.

## Facts verified vs open

**Verified (20 Oct 2026, primary sources saved in `raw/`):** Composer 2.10.3 is the latest
release (GitHub releases API). Every version/PR attribution in "Evidence in hand" items 1–6.
`audit` and `outdated` options at 2.10.3. `cooldown` is unreleased. The
`check-platform-reqs` one-failure-per-platform-package behaviour (source and observed
output). BookStack's numbers at `045c6a9`. Lock presence and last-change dates for the eight
apps.

**Open, to measure or re-check at drafting:**

- All numbers for the seven unprobed apps. Nothing in the subtitle or lede until measured.
- Whether the four BookStack caps are lifted in newer releases of those packages (a newer
  version may allow 8.6 while the lock still pins the capped one). That's a different and
  more useful number: "capped and fixable by `composer update`" vs "capped upstream". Add it
  to `analyse.php`.
- Composer 2.11: if it ships before publishing, re-check the `cooldown` policy and whether
  `check-platform-reqs` output changed.
- PHP 8.6 RC4 (due 22 Oct) and GA (19 Nov): re-run the 8.6 checks on the newest image.
- `composer why-not php 8.6.0` — whether it lists every blocking package in 2.10.3, which
  would be the simpler workaround for the gotcha.
- Whether Packagist's abandoned flag can be set only by the maintainer (describe the shape;
  check Packagist's docs before stating who can set it).

## Out of scope

- Security advisories themselves, CVE scoring, Roave/SecurityAdvisories. Audit's advisory
  check works; the post isn't about it.
- Malware lists beyond one sentence.
- Rector, Dependabot and Renovate beyond a mention.
- Running the apps or their test suites. This is lock-file analysis only.
- The features of PHP 8.6. AI anything.
- Grading or shaming the projects.

## Open questions for Dragan

1. **Overlap with the published PHP 8.6 lock-file post.** That post already names
   `nette/schema` and `ezyang/htmlpurifier` caps. This one stands alone, but a reader of both
   sees the same two packages. Options: lead with the audit/quiet/majors angle and keep caps
   to one section, or accept the overlap because it's the strongest number.
2. **Title**: keep the working title, or the more release-timed *Your Lock File Passed the
   Audit. It Still Can't Run PHP 8.6.*?
3. **App list**: the eight above, with Monica as the stale-lock outlier — or drop Monica and
   keep every app comparably maintained?
4. **Timing**: publish before GA (19 Nov) for the 8.6 hook, or after, leaning on the tooling
   angle?

## Medium meta

- Tags: `PHP`, `Composer`, `Software Engineering`, `Programming`, `DevOps`.
- Member-only. Publish in the run-up to 8.6 GA, after the RC4 re-check.
- Hero: a green "audit: clean" stamp on a lock file, with the lines it didn't read
  highlighted beside it: a cap, a quiet package, a major behind. The diagram carries the
  measured numbers, not placeholders.

## Cost to produce

Extend the probe to seven more apps and add the "fixable by update" metric: two to three
hours. Draft: one session. Hero and voice check: one session.
