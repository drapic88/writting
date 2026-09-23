# Article plan — "PHP 8.6: What's New, What Breaks, and How to Migrate"

**Platform:** Medium · **Status:** published
**Researched:** 2026-09-08, when PHP 8.6 was at **beta 3** (feature freeze passed, so the
feature list below is effectively final — only bug fixes land between now and GA).
**PHP 8.6 GA:** **19 November 2026**

---

## 1. Positioning and meta

### The angle
PHP 8.6 is **not** a landmark release like 8.0 (JIT, union types) or 8.4 (property hooks).
It is a *quality-of-life and clean-up* release with one genuinely headline language feature —
**partial function application** — and an unusually long deprecation list that is really
**PHP 9.0 preparation in disguise**.

That tension is the article's spine, and it's what makes it worth reading rather than being
another changelog rewrite:

> Upgrading to 8.6 will take you an afternoon. Getting *clean* on 8.6 is how you avoid a
> painful PHP 9.0.

Every section should serve that thesis. Avoid the "10 cool new functions" format — it is
already saturated on Medium and adds nothing.

### Title options
1. **PHP 8.6: What's New, What Breaks, and How to Migrate** — clear, searchable, safe.
2. **PHP 8.6 Is a Small Release With a Big Warning Label** — thesis-forward, best CTR.
3. **PHP 8.6: One Great Feature and Thirty Deprecations** — concrete and honest.
4. **Partial Application Lands in PHP 8.6 — and PHP 9.0 Starts Here** — for a dev-heavy audience.

*Recommendation:* headline #2, subtitle "Partial function application, `Time\Duration`, and a
deprecation list that is really PHP 9.0 preparation." Medium rewards a thesis in the title and
the keywords in the subtitle.

### Practical meta
- **Target length:** 1,800–2,400 words (8–10 min read). Long enough for Medium's
  distribution, short enough to stay on-thesis.
- **Audience:** working PHP devs and tech leads on 8.2–8.5, Laravel/Symfony shops, people
  who own an upgrade decision. Assume they know what an RFC is; do not explain what an enum is.
- **Tags (5):** `PHP`, `Programming`, `Web Development`, `Software Engineering`, `Backend`
- **Publication:** pitch to *Level Up Coding* / *Better Programming* / *ITNEXT* after
  self-publishing, or submit directly if you want reach over speed.
- **Canonical:** if this also goes on the Analitix blog, publish there first and use Medium's
  import/canonical link so you don't split SEO.

---

## 2. Structure

Section-by-section outline with the beats to hit and the code to include.

### Lede (~120 words)
Open on the release date and the honest framing: PHP 8.6 ships 19 November 2026, the
diff is smaller than 8.5's, and the interesting part isn't the feature list. One sentence
that names the three things a reader will remember: partial application, `Time\Duration`,
and ~30 deprecations. Then promise the migration playbook so people scroll.

Do **not** open with "PHP has come a long way since PHP 5." Instant close.

### Section 1 — The headline feature: partial function application (~450 words)
This is the most quotable part of the release; give it the most space.

Two placeholders: `?` for exactly one argument, `...` for "all remaining parameters".

```php
// Bind some arguments now, leave the rest for later.
$makeSlug = str_replace(' ', '-', ?);
$makeSlug('Hello World');            // 'Hello-World'

// ? is positional; ... keeps the tail variadic
function stuff(int $i1, string $s2, float $f3, Point $p4, int $m5 = 0): string {}

$c = stuff(1, 'hi', ...);            // fn(float $f3, Point $p4, int $m5 = 0) => ...
$c = stuff(1, ?, 3.5, ...);          // fn(string $s2, Point $p4, int $m5 = 0) => ...

// Named placeholders reorder the resulting closure's signature
$c = stuff(s2: ?, i1: ?, p4: ?, f3: 3.5);
```

Beats to hit:
- **Why it matters now:** it is the natural partner to the **pipe operator** from PHP 8.5.
  Pipes without partial application force you to write `fn($x) => f($x, $extra)` wrappers
  everywhere. Show a before/after pipeline — this is the strongest single code sample in the
  article and probably the screenshot people share.
- **The gotcha worth the price of admission:** arguments are evaluated **immediately**,
  when the partial is created, not when it is called. Arrow functions defer. This is a real
  footgun and a great "you learned something" moment:

```php
$partial = speak(?, getArg());              // getArg() runs NOW
$arrow   = fn($who) => speak($who, getArg()); // getArg() runs on each call
```
- **Limits:** no `new` (use static factories), no `__get`/`__set`, no context-dependent
  functions (`compact()`, `extract()`, `func_get_arg()`, `get_defined_vars()`), and a
  positional `?` after a named argument is a fatal error.
- **vs. first-class callables (8.1):** `foo(...)` was a reference to the function as-is; PFA
  builds a *new* closure with arguments pre-bound. Note that only `#[\NoDiscard]` and
  `#[\SensitiveParameter]` carry over to the partial — FCC copied all attributes.
- Vote: **33 / 0 / 0**. Unanimous — worth saying, because it signals where the language is going.

### Section 2 — `Time\Duration`: the small class that fixes a recurring API mistake (~350 words)
The "is this timeout in seconds, milliseconds, or microseconds?" bug, solved by the type system.

```php
use Time\Duration;

$halfSecond = Duration::fromMilliseconds(500);
$combined   = Duration::fromSeconds(1)->add($halfSecond);
$backoff    = $baseDelay->multiplyBy(2 ** $attempt);   // exponential backoff, readably
```

`final readonly class Time\Duration`. Factories: `fromSeconds(int $s, int $ns = 0)`,
`fromNanoseconds`, `fromMicroseconds`, `fromMilliseconds`, `fromMinutes`, `fromHours`,
`fromIso8601DurationString`. Instance: `negate()`, `absolute()`, `add()`, `sub()`,
`multiplyBy(int)`, `divideBy(int)`, plus static `compare()`. Readonly props `$seconds`,
`$nanoseconds`, `$negative`. Vote: **35 / 1 / 2**.

Editorial note to make: it is deliberately a *stopwatch/egg-timer* duration, **not** a
calendar interval — no months, no DST, so it does not overlap with `DateInterval`. The first
consumer in core is `IO\Poll\Context::wait(?Time\Duration $timeout)`; the point of the RFC is
that future timeout-taking APIs have one obvious type to accept. Frame it as *infrastructure
for the next five years of PHP APIs*, which is more interesting than the method list.
**Verify at RC:** exactly which existing core functions (e.g. `sleep()`) accept a `Duration`
in the final build — this shifted during development and blog posts disagree.

### Section 3 — The async plumbing: the new Polling API (~250 words)
Low-level I/O multiplexing (`IO\Poll\Context`, `StreamPollHandle`, `Event::Read`) landed in core.

```php
$context = new IO\Poll\Context();
$context->add(new StreamPollHandle($stream), [Event::Read], ['type' => 'server']);
$watchers = $context->wait(Duration::fromSeconds(1));
```

Be honest about the audience: **almost no application code will call this.** It matters
because ReactPHP / Amp / Swoole / FrankenPHP-style runtimes currently each reimplement this
against `stream_select()` or an extension. A core primitive is how "async PHP" stops being a
per-framework dialect. Two-paragraph treatment, then move on — don't pad it.

### Section 4 — The rest of the good stuff (~300 words, tight list)
Keep this as a scannable list with one line each. Resist the urge to expand.

- **`clamp()`** — `clamp(101, min: 0, max: 100) // 100`; works on strings too: `clamp("a", "x", "z") // "x"`.
- **Readonly property defaults** — readonly properties can finally have default values;
  matters most with interface property hooks.
- **`#[\Override]` for class constants** — the 8.3 attribute extended again (8.5 gave it properties).
- **`enum SortDirection { Ascending; Descending; }`** — a built-in replacement for the
  `SORT_ASC`-style int constants everyone re-declares.
- **Debuggable enums** — enums may implement `__debugInfo()`.
- **Doc comments on parameters** — `function store(/** @param Book[] */ array $books): void {}`.
  Small syntax win, real static-analysis win.
- **Better error messages** — function arguments are now shown in errors, and `json_decode()`
  reports the *location* of a parse error. Both are pure debugging quality of life.
- **Object property writes on objects held in constants** — plugs a long-standing oddity.
- **Reflection** — `isReadable()` / `isWriteable()` for properties, scope-aware.
- **Closure optimizations** — free performance; note it, don't quantify it unless you
  benchmark it yourself (see §6).
- **`pack()`/`unpack()`** — `<` / `>` endianness modifiers for floats and signed ints.
  Niche, but if you do binary protocols it removes a pile of manual byte-swapping.
- Also: `grapheme_strrev()`, `mysqli_quote_string()`, `Locale::getDisplayKeyword()`,
  `IntlNumberRangeFormatter`, TLS session resumption + 0-RTT early data for streams,
  `Pdo\Pgsql::ATTR_CHUNK_SIZE` for lazy row fetching, `gmp_powm_sec()`, `gmp_prevprime()`,
  `finfo_file()` on remote streams, URI builder classes following up on 8.5's URI API.

### Section 5 — What didn't make it (~250 words)
High-engagement section; comment sections love this. It also shows you read the mailing list
rather than a changelog.

Declined for 8.6:
- **Pipe assignment operator** (`|>=`) — declined, one year after pipes were accepted.
- **`let` construct / block scoping** — declined, but `let` was *still* reserved (see below).
- **Bound-erased generic types** — declined. Generics remain PHP's forever-question.
- **`__exists()`** — a magic method to distinguish "missing" from "set to null". Declined.
- **`array_only_keys()` / `array_except_keys()`**, **`array_path_get()`/`array_path_exists()`**,
  **prefix/suffix functions** — all declined. Userland/framework territory.
- **Reassigning promoted readonly properties in the constructor** — declined.
- **Deprecating `list()`** — tied **23 / 23**, so it failed the 2/3 bar. `list()` survives.

Still under discussion and therefore missing the 8.6 train: **function autoloading (mark 5)**
and **`BackedEnum::values()`**. Note `ReflectionAttribute::getCurrent()` was in voting at
beta time — **verify its final status at RC**.

Good closing line for the section: the declines are a pattern, not noise — internals is
saying no to array helpers and yes to language plumbing.

### Section 6 — Migration: the actual work (~500 words, the payoff section)
Structure this as a numbered playbook, not prose. This is the part people bookmark.

**The good news first:** there is no 8.0-style wall here. No JIT rewrite, no engine break.
For most applications 8.6 is a version bump and a green test suite.

**Step 1 — Bump and run your suite with deprecations visible.**
```bash
php -d error_reporting=E_ALL -d display_errors=1 vendor/bin/phpunit
```
Deprecations are the whole story of this upgrade. If your CI hides `E_DEPRECATED`, you will
"pass" and inherit the problem in PHP 9.0.

**Step 2 — Fix the mechanical renames.** Pure find-and-replace, zero risk:
| Deprecated | Replacement |
|---|---|
| `is_double()` | `is_float()` |
| `is_integer()`, `is_long()` | `is_int()` |
| `doubleval()` | `floatval()` |
| `spl_object_hash()` | `spl_object_id()` |
| `strcoll()` | `Collator`-based comparison (intl) |
| `metaphone()` | `soundex()` or a userland phonetic lib |
| `spl_classes()` | reflection / an explicit map |
| `mysqli_stmt_init()`, `mysqli_get_charset()` | prepared statements directly / connection props |
| `define()`'s `$case_insensitive` | just define the constant once, correctly |

**Step 3 — Stop passing objects where arrays are expected.** This family of deprecations is
the most likely to actually appear in a real codebase: `array_walk()`,
`array_walk_recursive()`, `deflate_init()`/`inflate_init()`, zlib and bzip2 stream filter
params, `mb_convert_variables()`, and `http_build_query()`. The fix is usually
`get_object_vars($obj)` at the call site. Also: `is_a()` / `is_subclass_of()` with a string
first argument, and `ArrayIterator`'s inherited-but-meaningless methods, `SplFileObject`'s
CSV methods, and incomplete `session_set_save_handler()` implementations.

**Step 4 — Free your identifiers.** `readonly` as a function name, `is` and `let` as
identifiers, `namespace` as a class constant name, and `_` as a constant are all deprecated —
the engine is reserving vocabulary for future pattern matching. Rename now; these are cheap
and they *will* be hard errors later. (`in`/`out`/`inout` and `_()` as a gettext alias were
proposed and **rejected** — leave those alone.)

**Step 5 — `mb_ereg*` is on death row.** Oniguruma's upstream maintenance ended
2025-04-24, so **mbregex is deprecated in 8.6 and slated for removal in PHP 9.0**. If you
use `mb_ereg()`, `mb_eregi()`, `mb_regex_encoding()` and friends, this is your only real
porting project in this release: move to PCRE (`preg_*` with the `u` modifier). Budget for it
now — it is a semantic migration, not a rename, and Drupal has already opened an issue for it.

**Step 6 — Read the silent behaviour changes.** These break in production, not in tests:
- **Session INI defaults changed for security:** `session.use_strict_mode=1`,
  `session.cookie_httponly=1`, `session.cookie_samesite="Lax"`. If you relied on the old
  laxer defaults — cross-site POST flows, or JS reading the session cookie — you will find
  out on deploy day. Pin these explicitly in `php.ini` so the upgrade can't move them under you.
- Returning a value from `__construct()`/`__destruct()` is deprecated; returning from a
  `finally` block is deprecated (39 / 3 / 4 — the strongest vote in the whole deprecations RFC).
- `trim()`/`ltrim()`/`rtrim()`/`chop()` now strip **form feed (`\f`)** by default. Silent
  output change if you were parsing fixed-format text.
- Many functions that used to warn now throw `ValueError`/`TypeError`: `array_filter()`'s
  `$mode`, GMP shifts/powers, `pcntl_alarm()`/`pcntl_exec()`, `Phar::mungServer()`,
  curl's `CURLOPT_READFUNCTION` return values, non-stringable intl timezones, NUL bytes in
  `SimpleXMLElement`/session cookie settings.
- `preg_grep()` now returns `false` on error instead of a partial array — check your return handling.
- DOM read-only properties now use `public private(set)`; writing to them errors.
- `??`/`empty()` no longer trigger `__get()` after `__isset()` has materialised a property.
- `array_intersect()` converts values while scanning input (edge-case ordering change).

**Step 7 — Let the tools do it.** Rector (`PHP_86` set), PHPStan/Psalm at max level, and
`composer why` for any library still calling the deprecated APIs. Say plainly that most of
the above is a Rector run plus a careful read of the diff.

**Estimate to publish:** a well-tested Laravel/Symfony app on 8.4+ is realistically
**half a day to a day**, dominated by dependency updates rather than your own code. An
untested legacy codebase with `mb_ereg` is a different conversation.

### Verdict / close (~150 words)
Answer the question the title raised. Something like: PHP 8.6 is a *small* release and a
*loud* one. The language additions are modest — one excellent feature, a couple of
well-designed classes, better errors. The deprecation list is the real content, and it is a
readable roadmap: internals is reserving keywords for pattern matching, shedding an
unmaintained regex engine, closing the objects-as-arrays era, and turning warnings into
exceptions. Upgrade early, turn deprecations on, and treat the noise as a free PHP 9.0
migration plan. End with the one thing to do this week: run your suite on beta with
`E_ALL` and count the lines.

---

## 3. Fact sheet (verified 2026-09-08, beta 3)

Use this as the accuracy backstop while drafting — do not restate facts from memory.

**Implemented in 8.6:** partial function application (v2), readonly property defaults,
`#[\Override]` for class constants, deprecate returning values from `__construct()`/
`__destruct()`, closure optimizations, `clamp()` (v2), `enum SortDirection`, debuggable enums,
polling API, `Time\Duration`, form feed in trim functions, `grapheme_strrev()`,
`mysqli_quote_string()`, `Locale::getDisplayKeyword()`/`getDisplayKeywordValue()`,
`isReadable`/`isWritable` reflection methods, stream error handling improvements, filter-chain
limit, object property writes via constants, display function arguments in errors,
mbregex end-of-life deprecation, doc comments for parameters.

**Accepted (in or landing for 8.6):** deprecations for PHP 8.6, ext/uri follow-ups,
PFA optional-parameter handling, secure session configuration defaults, SNMP improvements,
`pack()`/`unpack()` endianness modifiers (floats + ints), "exempt input type/value validation
from the BC-break policy".

**Declined:** pipe assignment operator, `__exists()`, bound-erased generics,
`array_path_get()`/`array_path_exists()`, reassignment of promoted readonly properties,
`array_only_keys()`/`array_except_keys()`, prefix/suffix functions, `let` block scoping.

**Notable vote numbers** (nice for credibility, use two or three, not all):
PFA 33/0/0 · `Time\Duration` 35/1/2 · no returning from `finally` 39/3/4 ·
`readonly` as function name 39/1/2 · objects in `array_walk()` 41/3/0 ·
`list()` deprecation **failed** 23/23/1.

### Open items to re-verify at RC (before publishing)
- [ ] Which core functions accept `Time\Duration` in the shipped build (does `sleep()`?).
- [ ] Final status of `ReflectionAttribute::getCurrent()` (was in voting at beta).
- [ ] Whether every sub-vote in the deprecations RFC landed as described.
- [ ] Support timeline: active support and security-fix end dates for the 8.6 branch.
- [ ] Re-read the final `UPGRADING` file — the BC-break list grows during beta.
- [ ] Confirm Rector ships a `PHP_86` set by the time you publish.

---

## 4. Craft notes

- **Code samples:** 8–10 max, each under 12 lines, each making exactly one point. Use
  Medium's code blocks with `php` syntax highlighting; embed a Gist only for the pipe +
  partial-application before/after, which deserves to be shareable on its own.
- **Formatting:** Medium's engagement comes from scannability — subheads every ~200 words,
  one table (the rename table in Step 2), bold lead-ins on list items.
- **Voice:** first person, opinionated, specific. The differentiator against the twenty other
  "PHP 8.6 features" posts is *judgement* — say which features you will actually use, which
  you won't, and what the deprecations reveal about where the language is heading.
- **Honesty:** the article is written before GA. Say so once, in a line under the title
  ("written against 8.6 beta 3; I'll note any changes at RC"). It builds trust and gives you
  cover if something shifts.
- **Link out** to the RFCs inline — Medium readers click them and it signals primary-source work.
- **Images:** hero (`hero-php-8.6.png`, in this folder) at the top. Consider one more inline
  image: a simple two-column "before / after" of a pipeline with and without partial
  application. No stock photos of laptops.

---

## 5. Sources

- [PHP 8.6 RFC list — PHP.Watch](https://php.watch/versions/8.6/rfcs)
- [PHP 8.6 changes — PHP.Watch](https://php.watch/versions/8.6)
- [What's new in PHP 8.6 — stitcher.io](https://stitcher.io/blog/new-in-php-86)
- [PHP RFC index — wiki.php.net](https://wiki.php.net/rfc)
- [RFC: Partial Function Application v2](https://wiki.php.net/rfc/partial_function_application_v2)
- [RFC: Duration class](https://wiki.php.net/rfc/duration_class)
- [RFC: Deprecations for PHP 8.6](https://wiki.php.net/rfc/deprecations_php_8_6)
- [RFC: Oniguruma maintenance end / end of mbregex](https://wiki.php.net/rfc/eol-oniguruma)
- [php-src UPGRADING (master)](https://github.com/php/php-src/blob/master/UPGRADING)
- [Duration class discussion — PHP Foundation Discourse](https://discourse.thephp.foundation/t/php-dev-rfc-duration-class/5608)
- [PHP 8.6 Duration: a small class that fixes a recurring design mistake — SensioLabs](https://sensiolabs.com/blog/2026/php-duration-class)
- [Drupal issue: mb_regex_encoding()/mb_ereg() deprecated in 8.6](https://www.drupal.org/project/drupal/issues/3588024)
