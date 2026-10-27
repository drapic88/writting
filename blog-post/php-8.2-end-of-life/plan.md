# Plan — PHP 8.2 end of life

**Status:** published on Medium on 2026-10-27 (agreed and drafted 2026-10-26). Refresh before 31 December.
Public sources carry the argument; the BookStack probe supports two sections.

## Decisions (2026-10-26)

1. **Title:** keep *PHP 8.2 Stops Getting Security Fixes on 31 December*.
2. **Target:** the stance is "8.4, not the newest". 8.6 gets one sentence on why fresh
   releases wait on `"php"` caps, with no reference to any other post.
3. **Distro caveat:** shrunk to the limits paragraph. Debian 12 ships `php8.2`, and its LTS
   runs to June 2028. The Debian `php7.4` revision count is dropped because the advisory
   dates were never verified.
4. **Probe scope:** BookStack alone. Running the full playbook on it turned out to be
   cheap, so it was run end to end instead of adding a second project.

## What changed after re-checking (2026-10-26)

Data in `~/Projects/writting-experiments/exp-php82-eol/FINDINGS.md`, second half.

- **8.2.35 shipped on 21 Oct 2026** and is now the latest 8.2 release.
- Packagist September figures are unchanged. October to date: 8.2 10.1%, ≤ 8.2 18.6%.
- **Rector 2.8.0 and 2.8.1 shipped on 26 Oct.** Re-run on 2.8.1: same 110 files and the
  same rules. The only difference is one count
  (`ArrowFunctionDelegatingCallToFirstClassCallableRector` went from 4 to 6). No Rector
  rule covers `E_STRICT` or `E_USER_ERROR`.
- **New gotcha from the diff:** the `php84` set rewrites code into 8.4-only syntax
  (`new BookContents($page->book)->getTree()`, `array_any()`). So run it after production
  is on 8.4, not before. This sharpens section 5.
- **New finding from the playbook:** raising the floor to `^8.4` lets Composer move five
  Symfony components from 7.4 to **8.0** (`clock`, `event-dispatcher`, `filesystem`,
  `string`, `translation`), because 8.0 requires `php >=8.4`. That's 48 updates with the
  bump against 45 without. BookStack's suite stayed green (1,625 tests) on 8.2.35, on 8.4
  with the old lock, and on 8.4 with the bumped lock, with the same 162 deprecation lines
  and 6 distinct messages each time. That becomes its own section.
- **Timed costs:** `check-platform-reqs` took 1 s, the dry-run 4 s, the real update 20 s,
  the suite about 2 minutes on 8.4, and Rector 15 s to 2 minutes.
- The pre-RFC end date stays unquoted. Only the RFC's own wording is used.

---

## Positioning

The Medium audience reads PHP, and release-timed PHP posts earn the most on a member-only
account. This one is timed to a date rather than a release: **PHP 8.2 gets its last
security fix on 31 December 2026**. Publish in the first week of December, when the
deadline shows up in security scanners, hosting-panel banners and sprint planning, and
people search for "PHP 8.2 end of life".

**The premise checks out.** php.net/supported-versions (fetched 20 Oct 2026) lists 8.2 as
GA 8 Dec 2022, active support until 31 Dec 2024, security support until **31 Dec 2026**.
The date comes from the accepted Release cycle update RFC, which pushed security support
out by a year (31–0) and moved every end date to 31 December (33–0), applied to all
supported branches from 8.2 onwards. No corrected angle is needed.

It's an **upgrade-sizing** post, not a scare post. The numbers say one Composer install in
five still runs 8.2 or older. The probe says the language part of leaving 8.2 is small. The
point the post adds: Rector's PHP sets are mostly tools for *adopting* new syntax, not for
*surviving* the upgrade. The work that actually decides your date sits outside Rector's
reach — `composer.lock`, extensions, the container image, and runtime behaviour.

Stands alone. No reference to any other post in this folder. It explains the
dependency-cap problem in its own two paragraphs and names no other post.

## Title

**PHP 8.2 Stops Getting Security Fixes on 31 December**

Subtitle (`###`): *One Composer install in five still runs 8.2 or older. Leaving it is
mostly a config change. Rector won't do the part that's hard.*

Provenance line: *Support dates from php.net and Packagist statistics as of [drafting
date]; Rector 2.7.0 run against BookStack v26.09.1. PHP 8.6 shipped on 19 November, so its
package support is still settling.*

Alternatives:
- **Leaving PHP 8.2 Is a Config Change. Your Lock File Is the Upgrade.** (stronger claim,
  weaker search match)
- **Rector Won't Get You Off PHP 8.2** (provocative, but only half true, so the post has to
  earn it)
- **PHP 8.2 Has Ten Weeks Left. Here's How Big Your Upgrade Actually Is.** (only if
  publishing slips to late December, then adjust the count)

Recommendation: keep the working title. It's the search query, it's a dated claim, and it
has a verb.

## Thesis

The 31 December date is real, and a fifth of the ecosystem is still on 8.2 or older. But
for a codebase that already runs cleanly on 8.2, moving the floor is a `composer.json`
change. BookStack did it on 4 October 2026 without touching one line of application PHP.
**Your PHP 8.2 exit is a dependency upgrade, not a code rewrite, and Rector automates the
part you didn't need.** Spend the time on the lock file and the image. Don't spend it on a
110-file style diff.

## Evidence in hand

Saved under `~/Projects/writting-experiments/exp-php82-eol/` (`FINDINGS.md`, `raw/`,
`packagist_shares.py`, `run-rector.sh`, `summarize.py`).

**1. Support table** — php.net/supported-versions.php, fetched 20 Oct 2026
(`raw/sv.html`):

| Branch | GA | Active until | Security until |
|---|---|---|---|
| 8.2 | 8 Dec 2022 | 31 Dec 2024 | **31 Dec 2026** |
| 8.3 | 23 Nov 2023 | 31 Dec 2025 | 31 Dec 2027 |
| 8.4 | 21 Nov 2024 | **31 Dec 2026** | 31 Dec 2028 |
| 8.5 | 20 Nov 2025 | 31 Dec 2027 | 31 Dec 2029 |

- Latest 8.2 release: **8.2.34, 24 Sep 2026**, tagged `security` (php.net releases JSON:
  `curl -s 'https://www.php.net/releases/index.php?json&version=8.2'`).
- 8.1 went EOL on 31 Dec 2025 at 8.1.34 (php.net/eol.php).
- A detail worth one sentence: **8.4's active support also ends on 31 Dec 2026**. After
  New Year, 8.4 gets security fixes only. That matters when choosing a target.
- 8.6 is not in the table yet. It goes GA on 19 Nov 2026, and the table needs re-checking
  then.

**2. Release cycle RFC** — wiki.php.net/rfc/release_cycle_update (Zelenka, Rethans; status
Accepted). Vote results from the rendered page (`raw/rcr.html`):
- "Extend Security Support by One Year": **31–0**
- "Extend Releases Cycle to End of Year": **33–0**
- Scope, quoted: "The changes will apply immediately on the all currently supported
  branches from PHP 8.2." That's why 8.2 runs to the end of 2026 rather than its old date.

**3. Packagist install share** — packagist.org/php-statistics, monthly series embedded in
the page (`raw/packagist-php-statistics-2026-10-20.html`, parsed by
`packagist_shares.py`):

| Month | 8.5 | 8.4 | 8.3 | 8.2 | 8.1 | ≤ 8.2 |
|---|---|---|---|---|---|---|
| Oct 2024 | – | 0.2% | 30.0% | 31.1% | 21.2% | 69.8% |
| Oct 2025 | 0.5% | 23.4% | 32.6% | 20.9% | 10.6% | 43.6% |
| **Sep 2026** | 21.8% | 34.0% | 23.0% | **11.1%** | 4.0% | **21.1%** |

- Sep 2026 is the last full month: 5,809,870,614 installs. **10.0%** are already on an EOL
  branch (8.1 or older), and 8.2 joins them in ten weeks.
- The decline is steady, about 10 points of 8.2 share a year. At that rate, roughly one
  install in ten will still be on 8.2 on 1 January. That's a projection and the post
  labels it as one.
- Limit, stated in the post: these are Composer installs, which are dominated by CI.
  They are not a census of production servers.

**4. Rector probe** — BookStack v26.09.1 (`31d94dd`), whose `composer.json` requires
`"php": "^8.2.0"` with `config.platform.php` pinned to `8.2.0`. Laravel 12. Rector 2.7.0
(released 6 Oct 2026) on PHP 8.4.26, `--dry-run`, `withPhpSets(phpNN: true)` over `app/`
(522 files):

| Target set | Files changed | What's new versus the row above |
|---|---|---|
| `php82` | **110** | 17 rules, every one a pre-8.2 modernisation: `ClosureToArrowFunctionRector` 45, `ClassPropertyAssignToConstructorPromotionRector` 22, `RemoveUnusedVariableInCatchRector` 21, `IfToNullCoalescingAssignRector` 20 … |
| `php83` | 110 | nothing |
| `php84` | 110 | `NewMethodCallWithoutParenthesesRector` 21, `ForeachToArrayAnyRector` 2 |
| `php85` | 110 | nothing |
| `php86` | 110 | nothing |

Each run took 7–16 s. The reading: on a codebase that already runs on 8.2, moving the
Rector target from 8.2 to 8.6 adds **two rules, both optional 8.4 syntax**. The 110-file
diff is style the project never adopted. It isn't upgrade debt. Running on 8.4 doesn't
require any of it.

**5. What BookStack actually changed** — `ac89927af` (4 Oct 2026), "PHP: Updated min
version to 8.3": four CI workflow files, `composer.json` (+2 −2), `composer.lock`
(+139 −139), `dev/docker/Dockerfile`, `phpstan.neon.dist`. **No file under `app/`.** Then
`c4f30354e` (10 Oct 2026), "Framework: Updated to Laravel 13". Leaving 8.2 was a config
change, and the dependency work came next.

**6. Rector PHP sets that exist today** — rector-src at tag `2.7.0`:
- `config/set/php52.php` … `php86.php`, and `LevelSetList::UP_TO_PHP_53` …
  `UP_TO_PHP_86`.
- `php83` set: 6 rules. `php84`: 8, including `ExplicitNullableParamTypeRector` (the one
  8.4 deprecation it fixes for you) and `RoundingModeEnumRector`. `php85`: about 18,
  counting configured renames. `php86`: 2 (`ConstructorReadonlyAssignToDefaultRector`,
  `MinMaxToClampRector`).
- `RectorConfigBuilder::withPhpSets()` with no arguments reads the PHP version from
  `composer.json`. The per-version `withPhpNNSets()` methods are deprecated in favour of
  `withPhpLevel()`, and the source flags the per-version set files as deprecated. The post
  shows the no-argument form and says why: it follows your floor automatically.

**7. What Rector can't do** — from php-src `UPGRADING` on `PHP-8.3` and `PHP-8.4`
(`raw/up83.txt`, `raw/up84.txt`):
- 8.4 unbundles **IMAP, OCI8, PDO_OCI and pspell** to PECL (§8, lines 987–1000). That's an
  image and ops change. No source rewrite fixes a missing extension.
- 8.3 changes `range()` behaviour (§1) and deprecates `++`/`--` on non-numeric strings,
  which depends on runtime values that static analysis can't always see.
- 8.4 deprecates the `E_STRICT` constant and passing `E_USER_ERROR` to `trigger_error()`.
  The post checks at drafting whether a Rector rule covers either. If not, it says so.
- Plus everything outside your code: version caps in `vendor/`, the framework major, `ini`
  settings, the base image.

**8. Distros keep patching after php.net stops** — Debian 12 "bookworm" ships `php8.2`
(`8.2.32-1~deb12u1`, sources.debian.org), and Debian 12 LTS runs to **30 Jun 2028**
(endoflife.date). Bullseye's `php7.4` is at `7.4.33-1+deb11u5`, five Debian revisions on
top of upstream's final 7.4.33. This is the honest caveat: if you run distro PHP on an LTS
distro, 31 December isn't your cliff. It's your vendor's, and it moves.

## Structure (standard long-form, 1,600–1,900 words)

**Lede.** The trigger is concrete and dated: in December, the support table turns 8.2 red.
Show the four-row table, or the one-line `curl` of the releases JSON. Then the honest
answer up front: about one install in five is on 8.2 or older. For most of them, leaving
is a `composer.json` edit and a lock-file upgrade, not a rewrite. Thesis in bold, then a
roadmap sentence.

1. **`## 31 December is real, and it was already an extension`** — the table, the RFC's
   two votes, and why the date is now always 31 December. One paragraph on what EOL means
   in practice: no more `8.2.x` releases, so the next CVE stays open. Cite 8.2.34 as the
   latest security release.
2. **`## Who is still on 8.2`** — the Packagist table across three Octobers. 21.1% in
   September, 10.0% already on EOL branches. The CI-not-production caveat goes in the same
   paragraph as the number, not in a footnote.
3. **`## Pick 8.4, not the newest`** — target choice. 8.4 has security fixes to 2028 and
   holds the biggest Packagist share, so its dependency support is mature. 8.5 is the
   longer runway. 8.6 is a few weeks old in December, and the post explains in its own
   words why `"php"` upper bounds in packages lag a fresh release. Opinion, stated as one,
   with the case where it doesn't apply: a greenfield service with few dependencies can
   go straight to the newest.
4. **`## What BookStack changed to leave 8.2`** — the `ac89927af` file list. No `app/`
   file. The point: the floor is configuration, and the lock file is the work.
5. **`## What Rector automates, and what that's worth`** — the probe table, plus a
   before/after code pair from one real hit in the `php84` diff
   (`NewMethodCallWithoutParenthesesRector`). The finding: 110 files, none needed. Use
   Rector for `ExplicitNullableParamTypeRector`-class fixes, and treat the rest as an
   optional style PR you merge separately.
6. **`## What Rector can't see`** — the extension unbundling, `range()`, runtime-valued
   deprecations, `vendor/`, the image. Show `php -m` as the extensions check.
7. **`## Playbook: off 8.2 before the last patch`** — numbered, real commands:
   1. Find out which PHP you actually run: `php -v` in the production image, not on your
      laptop. If it says `deb12u`, read the distro caveat first.
   2. Set the target in `composer.json`: `"php": "^8.4"` and `config.platform.php`. Then
      run `composer update --dry-run` and read the conflicts.
   3. Check the image for the extensions 8.4 unbundled: `php -m | grep -iE
      'imap|oci8|pspell'` on the old image.
   4. Run the suite on the target with `error_reporting=-1` and count the deprecation
      lines.
   5. Run Rector with `withPhpSets()` (no arguments) and `--dry-run`. Apply the rules you
      need now, and put the style changes in a separate PR.

   Cost estimate: measured, not guessed. Time steps 2–5 on BookStack v26.09.1 (8.2 → 8.4)
   at drafting. The Rector step is 7–16 s, so the number will come from Composer and the
   test suite.
8. **`## The limits`** — one project in the probe. Packagist counts installs, not
   servers. Distro LTS changes the calculus. A codebase that doesn't run cleanly on 8.2
   today has a bigger job, and this post doesn't size it.
9. **`## Verdict`** — compressed thesis, then the action with a threshold: run
   `composer update --dry-run` with `"php": "^8.4"` this week. If it resolves, leaving 8.2
   is an afternoon and a deploy. If it doesn't, each conflict is a dependency you have to
   move first, and there are about four weeks left to do it in.

`### Sources` — php.net supported-versions and eol pages; the php.net releases JSON;
wiki.php.net/rfc/release_cycle_update; packagist.org/php-statistics; php-src `UPGRADING`
on `PHP-8.3` and `PHP-8.4`; rector-src at `2.7.0` (`config/set/`, `RectorConfigBuilder`);
BookStack `ac89927af` and `c4f30354e`; sources.debian.org `php8.2`; endoflife.date Debian.

## Facts verified vs still open

**Verified 20 Oct 2026** (primary source, saved under `raw/`):
- 8.2 security end 31 Dec 2026; 8.4 active end 31 Dec 2026; the rest of the table.
- RFC status Accepted; votes 31–0 and 33–0; the "from PHP 8.2" scope sentence.
- 8.2.34 on 24 Sep 2026; 8.1 EOL 31 Dec 2025 at 8.1.34.
- Packagist monthly shares for Oct 2024, Oct 2025 and Sep 2026.
- Rector 2.7.0 release date and set files `php52`–`php86`; the rule lists for `php83`,
  `php84` and `php86`; `withPhpSets()` reading `composer.json`.
- BookStack commits `ac89927af` and `c4f30354e`, with their file lists.
- 8.4's IMAP/OCI8/PDO_OCI/pspell unbundling (UPGRADING).
- Debian 12 ships `php8.2`; Debian 12 LTS end 30 Jun 2028.

**Open — re-check at drafting (early December):**
- Supported-versions table after 8.6 GA (19 Nov), and the latest 8.2.x release and date.
  If 8.2.35 ships in November or December, cite it.
- Packagist November 2026 full month. It replaces September as the headline number.
- 8.2's end date before the RFC. I derived "three years after GA, so 8 Dec 2025", but
  haven't seen it quoted. Find it in the php.net page history, or leave it out.
- Newest Rector release. Re-run the probe on it, and re-check the deprecation note on the
  per-version set files.
- Whether any Rector rule covers the `E_STRICT` or `E_USER_ERROR` deprecations.
- The end-to-end playbook time on BookStack 8.2 → 8.4. It hasn't been run, so no number
  goes in until it's timed.
- Debian LTS: confirm that DLAs for `php7.4` came after upstream EOL, with dates, before
  using the `+deb11u5` line. Check whether Debian LTS has said it will cover `php8.2`.
  RHEL/Ubuntu: no claim unless one is verified.
- Whether the claim about 8.6 package caps still holds in December. Describe the shape of
  the problem, and name a package only if the cap is still there.

## Out of scope

- The 8.3–8.6 feature tours. Only what the probe or UPGRADING forces in gets named.
- Upgrades from 7.x or 8.0/8.1. One sentence pointing at the 10.0% figure, nothing more.
- PHP 9.0, which has no release date. Don't imply one.
- Commercial extended support (paid 8.2 builds). If it's mentioned at all, it's one
  neutral sentence with no vendor named, unless a verified source exists.
- AI anything. Performance numbers.

## Medium meta

- Tags: `PHP`, `Programming`, `Software Engineering`, `Laravel`, `Security`.
- Publish: Tuesday 1 or Wednesday 2 December 2026, member-only. A short refresh around
  29 December, if the Packagist numbers move noticeably.
- Hero: the support table as a timeline. The 8.2 bar ends at a marked 31 Dec 2026, with
  the 8.4 bar shifting from active to security on the same line.

## Cost to produce

Re-check facts, re-run Rector, and time the playbook on BookStack: two hours. Draft: one
session. Hero and voice check: one session.

## Questions for Dragan

1. Title: keep **PHP 8.2 Stops Getting Security Fixes on 31 December**, or go with the
   stronger-claim alternative?
2. Recommended target: is "8.4, not the newest" the stance you want, given that 8.6
   launches two weeks earlier and your audience just read about it?
3. The distro caveat (Debian LTS patching past php.net) slightly undercuts the deadline.
   Keep it as an honest section, or shrink it to the limits paragraph?
4. Probe scope: is BookStack alone enough, or do you want a second public project still on
   `^8.2` (e.g. a library) for the Rector table?
