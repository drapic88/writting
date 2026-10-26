# Plan — FrankenPHP worker mode (working title: "Worker Mode Is Fast Until Request Two Sees Request One's Data")

**Status:** agreed 2026-10-26.
**Researched:** 2026-10-20, against FrankenPHP v1.13.1, Laravel Octane v2.22.0 and Symfony
8.1.9. Re-checked 2026-10-26: FrankenPHP is now v1.13.3.

## Decisions (agreed 2026-10-26)

- **No benchmark.** The FPM vs FrankenPHP speed measurement is dropped entirely. The post
  quotes no speed-up number unless it comes from a cited primary source. It's about the
  state leaks and the resets. Everything below about the benchmark (the three-config
  table, the load tool, section 2 "The speed-up, measured") is superseded.
- **App:** `symfony/demo` for every reproduction. Laravel/Octane appears in the reset
  section only, from its source and docs.
- **Title:** the working title stays: *Worker Mode Is Fast Until Request Two Sees Request
  One's Data*.
- **Lede:** no real incident. The planted `curl` transcript carries it.
- **Scenarios:** every leak scenario is reproduced before it's written about. Any that
  can't be reproduced is cut.
- **Run 2026-10-26:** all six application scenarios (static user, memoized service, captured
  request, tenant + exception, `$_ENV`, timezone) reproduced on `symfony/demo` with FrankenPHP
  1.13.3; the libxml leak reproduced on 1.13.1 and is fixed in 1.13.3. Results, raw output
  and code: `~/Projects/writting-experiments/exp-frankenphp/FINDINGS.md`.

---

## Positioning

The Medium audience reads PHP, and PHP posts are where the Partner Program earnings are.
This one isn't tied to a php.net date, so it doesn't compete with the 8.6 GA window
(19 November 2026). It's a **performance-and-correctness** post, which the folder doesn't
have yet, and the subject is live:

- **FrankenPHP is now a PHP project, not a side project.** The PHP Foundation announced
  official support on 15 May 2025, and the repository now lives at `php/frankenphp`
  (11,405 stars, last push 18 Oct 2026). Releases are frequent: v1.13.0 on 4 Oct, v1.13.1
  on 16 Oct.
- **Symfony and Laravel both ship a worker-mode path.** Symfony's own `symfony/runtime` has
  had a `FrankenPhpWorkerRunner` since 7.4, and 8.1.0 added `FRANKENPHP_RESET_KERNEL`.
  Laravel goes through Octane (`php artisan octane:install --server=frankenphp`).

The search results for "FrankenPHP worker mode" are mostly benchmark screenshots of
hello-world routes. Almost nobody shows the other half: the failure that the speed buys
you. That's the reason for this post to exist, and the probe already reproduced it in five
`curl` calls.

**The angle nobody has published:** the Octane docs file static arrays under **"Managing
Memory Leaks"** (`octane.md`, line 570). A static that holds a user ID isn't a memory
problem. It's a data-exposure problem, and the docs' framing hides that.

**Stands alone:** no reference to other posts in this repo. What FPM's
share-nothing model is gets three sentences, because the whole argument rests on it.

## Title

**Worker Mode Is Fast Until Request Two Sees Request One's Data** (working title, keep)

Alternatives:
- **PHP-FPM Forgot Everything for You. Worker Mode Doesn't.**
- **FrankenPHP Doesn't Leak Your Data. Your Static Properties Do.**
- **Your PHP App Was Stateless Because It Died After Every Request**

Subtitle (`###`), pick at drafting once the numbers exist:
- *I moved a Symfony app from PHP-FPM to FrankenPHP's worker mode and measured [N]× the
  throughput. Then I made one request serve another user's data, with eight lines of code.*
- *The framework resets what it owns. Nobody resets what you own.*

Provenance line: *Written against FrankenPHP 1.13.1 (PHP 8.5.11), Symfony 8.1 and Laravel
Octane 2.22, in October 2026. Benchmark numbers are from Docker Desktop on a laptop; the
ratios are the claim, not the absolute numbers.*

## Thesis

Worker mode is fast for exactly the reason it's dangerous: the PHP process no longer dies
at the end of the request. Under FPM, every `static`, every singleton and every memoized
array was wiped for free; in worker mode it survives into the next request, possibly for a
different user. Frameworks reset the state they own (Octane registers 40 reset listeners
by default; Symfony resets every service tagged with `ResetInterface`), but neither can see
yours. **You get worker mode's speed from one line of config. You get its safety only from
an audit of your own state.**

## Evidence in hand

Everything below is saved under `~/Projects/writting-experiments/exp-frankenphp/`
(`PROBE.md`, `probe/`, and copies of the cited files in `sources/`).

**Public, link-checkable:**

1. **Stewardship.** PHP Foundation blog, 15 May 2025: "FrankenPHP Is Now Officially
   Supported by The PHP Foundation". The repo is `github.com/php/frankenphp`; the existing
   maintainers keep control of releases. Latest release v1.13.1 (16 Oct 2026), which
   embeds Caddy 2.11.7. v1.13.0 notes say "Compatibility with PHP 8.6" (#2600).
2. **Config syntax, from `docs/config.md` at v1.13.1.** A `worker` block inside the global
   `frankenphp` option, with `file`, `num`, `env`, `watch`, `name` and
   `max_consecutive_failures`; or the one-line form `worker <file> <num>`; or `worker
   index.php <num>` inside `php_server`. Default `num` is 2× the CPU count. `max_requests`
   exists at the `frankenphp` level and is marked **experimental**. The Docker shortcut
   is `FRANKENPHP_CONFIG="worker ./public/index.php"`.
3. **FrankenPHP's own list of what survives (`docs/worker.md`, "State persistence").**
   Static variables, class static properties, globals, in-memory caches, and runtime
   settings changed with `ini_set()`, `date_default_timezone_set()`, `chdir()`,
   `set_error_handler()` and others. Also: "**`$_ENV` is currently not reset between
   requests**."
4. **The server itself leaked once.** The v1.13.0 security notes: "`putenv()` no longer
   writes to the process-wide OS environment, which leaked values across requests and
   threads" (GHSA-996f-w38m-f574). A real, published cross-request leak, fixed 4 Oct 2026.
5. **Laravel Octane's reset list.** `src/Concerns/ProvidesDefaultConfigurationOptions.php`
   on `2.x`: **8** listeners in `prepareApplicationForNextRequest()` (locale, cookies,
   session, auth, request instance, paginator…) and **32** in
   `prepareApplicationForNextOperation()` (config sandbox, URL generator, fresh app
   instance handed to the router, cache, DB, mail, queue managers…). `config/octane.php`
   wires both into `RequestReceived`. Default `--max-requests` is 500.
6. **What Octane says it won't do.** Octane docs (`laravel/docs`, `octane.md`, "Dependency
   Injection and Octane"): Octane "does not always know how to reset the global state
   created by your application", and injecting the container or the request into a
   singleton's constructor leaves "a stale version" on later requests. Laravel's container
   has `scoped()` bindings, flushed per request (`Container.php`, `13.x`, line 528).
7. **How Symfony resets.** `HttpKernel/Kernel.php` (8.1): on every `boot()` after the
   first request, if the request stack is empty, it calls `services_resetter->reset()`,
   which resets services implementing `ResetInterface`. `SymfonyRuntime` picks
   `FrankenPhpWorkerRunner` when `FRANKENPHP_WORKER` is truthy; `worker_loop_max` /
   `FRANKENPHP_LOOP_MAX` defaults to **500**. `FRANKENPHP_RESET_KERNEL` (commit
   `95d19f507d`, 27 Apr 2026; present in v8.1.0, absent from v7.4.21) clones the kernel
   after each request "to mitigate cross-request state leaks".
8. **A linter exists.** FrankenPHP's `symfony.md` recommends Igor PHP
   (`igor-php/igor-php`, created April 2026, 128 stars), which flags services missing
   `ResetInterface`, mutable statics and superglobal writes. Not yet tried.

**From the probe (20 Oct 2026, `dunglas/frankenphp:1.13.1-php8.5`, one worker thread):**

- A class with `public static ?string $name`, set only when `?user=` is present. Five
  requests to the worker script — `?user=alice`, none, none, `?user=bob`, none — answer
  `alice, alice, alice, bob, bob`. The same file without the loop answers `alice`, then
  `(anonymous)`. That's the post's central demo, and it's eight lines.
- **`getmypid()` returned `1` for every request.** Workers are threads inside one process,
  so a PID can't tell you which worker served a request. The repro scripts need a random
  ID generated at worker boot. Small, but it's the kind of thing a reader will try first,
  and it's worth one sentence.
- A hello-world `ab` run showed worker mode **no faster** than classic mode (2,781 vs
  3,329 req/s, `-n 2000 -c 20`). That's expected: there is no framework bootstrap to skip,
  and Docker Desktop port-forwarding dominates. It shapes the benchmark design below.
- The image has `pdo_sqlite` and OPcache but **not `intl` or `zip`**, which `symfony/demo`
  needs. The experiment image adds them with `install-php-extensions`.

## Experiment design

### App

**Primary: `symfony/demo`**, already cloned at `~/Projects/writting-experiments/symfony-demo`
(commit `8d2e2ef`, Symfony `^8`, `symfony/runtime ^8`, SQLite). Symfony 8 supports FrankenPHP
worker mode natively, so no extra package is needed. It has a real kernel, Doctrine, Twig and
security. A new worktree `exp-frankenphp/` with its own `vendor/`, like the others.

**Secondary: a fresh Laravel 13 skeleton with Octane 2.22** for the Laravel leak scenarios
only. No benchmark on it, to keep the post to one set of numbers. (Open question 1.)

### Benchmark: three configurations, same PHP

| Config | Image | Notes |
|---|---|---|
| A. PHP-FPM | `php:8.5-fpm` + `nginx` | `pm = static`, children = worker threads in C |
| B. FrankenPHP classic | `dunglas/frankenphp:1.13.1-php8.5` | `php_server`, no `worker` |
| C. FrankenPHP worker | same image | `worker ./public/index.php`, `FRANKENPHP_WORKER=1` |

- Same PHP patch version in all three (check the `php:8.5-fpm` tag matches 8.5.11), same
  extensions, OPcache on with identical settings, `APP_ENV=prod`, `APP_DEBUG=0`, warmed
  cache. Each container capped with `--cpus=4`.
- **Load tool runs inside the same Docker network**, not from macOS, because the probe
  showed host port-forwarding swamping the difference. Candidate: `grafana/k6` or an
  `oha` image (verify which official image exists before choosing). `ab` stays as the
  fallback since it's on the host.
- Routes: `/en/blog/` (Doctrine + Twig), one post page, and `/en/login` (a cheap route,
  where bootstrap dominates and worker mode should win the most).
- Concurrency 1, 10 and 50; 60 s each after a 10 s warm-up; three runs, median reported.
  Record req/s, p50/p95/p99, and RSS of the server container after 10,000 requests.
- **No number goes in the post until it has been measured.** If worker mode's gain on the
  DB route is small, that's the finding and the post says so.

### Leak scenarios, each a minimal repro plus a test

Each scenario is a two-request test against **one worker thread** (`num 1`): request A with
user/tenant 1, request B without, assert B doesn't see A. Every one runs under FPM too, to
show it passing there.

1. **Static property** (done in the probe). The baseline demo.
2. **Memoized service.** A singleton with `private array $cache` keyed by product ID but
   computing a user-specific price. Symfony: a plain service; fixed by implementing
   `ResetInterface`. Laravel: `$this->app->singleton()`; fixed with `scoped()`.
3. **Request captured in a singleton constructor.** The case Octane's docs warn about:
   inject `Request` into a singleton, read a header on request B, get request A's value.
   Show what Octane does and doesn't catch.
4. **Tenant ID set by middleware, not unset on exception.** Request A throws after setting
   it; request B inherits. Shows why `try/finally` or a reset hook beats "remember to clear
   it at the end".
5. **`$_ENV` write.** Documented as not reset. One line.
6. **Runtime setting.** `date_default_timezone_set()` from a user preference: request B
   renders dates in request A's timezone. The quietest leak in the list, and the one an
   audit is least likely to catch.
7. **Symfony `FRANKENPHP_RESET_KERNEL=1`.** Re-run scenarios 1–6 with it on: which ones it
   fixes (container services) and which it can't (statics, `$_ENV`, ini settings), and what
   it costs in req/s on config C.
8. **Igor PHP** on the demo app with scenarios 1–6 planted: which does it flag?

## Structure (standard long-form, 1,800–2,100 words)

**Lede.** The benchmark number first, as a dated trigger: the same Symfony app, FPM vs
worker mode, [N]× req/s on the cheap route. Then the five-line `curl` transcript where Bob
sees Alice. The honest answer up front: worker mode is worth it for most apps, and the
config is one line, but the process stops forgetting, and FPM's forgetting was a safety
feature you never had to write. Thesis in bold. Roadmap: what got faster and why, the six
leaks, what Symfony and Laravel reset for you, and the audit.

1. **`## What FPM was doing for you`** — share-nothing in three sentences, then
   `frankenphp_handle_request()` and the loop. The `getCounter()` example from FrankenPHP's
   own docs.
2. **`## The speed-up, measured`** — the three-config table. Why the cheap route gains most
   and the DB route least: worker mode removes bootstrap, not queries. The hello-world
   non-result in one sentence as the honest limit.
3. **`## Six ways request two sees request one`** — the scenarios, each with a ≤15-line
   repro and the observed output. The longest section. Ends on the server's own `putenv()`
   advisory: even FrankenPHP shipped a leak.
4. **`## What the frameworks reset, and what they can't`** — Octane's 40 listeners
   and its docs' admission; Symfony's `services_resetter` and `FRANKENPHP_RESET_KERNEL`;
   the table of which scenario each fixes. The "memory leak" framing point goes here.
5. **`## The gotcha: max_requests is not a fix`** — Octane and Symfony both restart a
   worker after 500 requests. That bounds a memory leak; it doesn't stop request 2 of 500
   seeing request 1. Plus the PID gotcha.
6. **`## Playbook: audit before you flip the switch`** — numbered, real commands:
   1. Find your statics: a `grep -rnE 'static (\?|array|int|string|\$)'` over `src/` /
      `app/` (exact pattern tested at drafting), and every `self::$` / `static::$` write.
   2. List your singletons (`debug:container`, or `singleton(` in service providers) and
      ask of each: does it hold anything a user sent?
   3. Symfony: implement `ResetInterface` on stateful services; try
      `FRANKENPHP_RESET_KERNEL=1` and measure its cost. Laravel: move per-request state to
      `scoped()` bindings or an Octane `RequestReceived` listener.
   4. Write the two-request test with `num 1` for every piece of user-dependent state.
   5. Run Igor PHP on Symfony (if scenario 8 shows it's useful).
   6. Then turn worker mode on, with `max_requests` as a memory guard only.

   Cost estimate: measured on the demo at drafting. No figure until timed.
7. **`## The limits`** — one app, one laptop, Docker Desktop. Worker mode doesn't speed up
   your database. Long-running processes also leak memory and connections, which this post
   only touches.
8. **`## Verdict`** — compressed thesis; then the action with a threshold: grep your
   statics and singletons this week. Zero hits that hold request data means you can turn
   worker mode on today. Any hit is a bug that FPM was hiding, and you'd rather find it
   with a test than in a support ticket.

`### Sources` — PHP Foundation announcement; FrankenPHP `docs/worker.md`, `config.md`,
`symfony.md`, `laravel.md` at v1.13.1; v1.13.0 release notes and GHSA-996f-w38m-f574;
Laravel Octane docs and `ProvidesDefaultConfigurationOptions.php`; Symfony
`FrankenPhpWorkerRunner.php`, `SymfonyRuntime.php`, `Kernel.php` on 8.1, commit
`95d19f507d`; `ResetInterface`; Igor PHP.

## Facts verified vs open

**Verified (20 Oct 2026, primary sources):** Foundation support and the `php/frankenphp`
move; v1.13.1 as latest, with Caddy 2.11.7 and PHP 8.5.11 in the `1.13.1-php8.5` image;
the worker config syntax and defaults; the documented list of what persists, including
`$_ENV`; the `putenv()` advisory; Octane v2.22.0 and its 8 + 32 default listeners; Octane's
500-request default and its DI warnings; `scoped()` in Laravel 13's container; Symfony's
`services_resetter` path, `FRANKENPHP_WORKER`, the 500-loop default, and
`FRANKENPHP_RESET_KERNEL` being in 8.1.0 but not 7.4.21; the static-property leak (probe).

**Open, to settle in the experiment or at drafting:**
- Every benchmark number. Every leak scenario except #1.
- Whether an official FrankenPHP image exists for PHP 8.6 RC (only `php8.5` and older
  tags were checked). The post runs on 8.5 either way.
- Which in-network load tool to use, and that its image is official.
- Whether `FRANKENPHP_RESET_KERNEL` makes scenario #2 pass without `ResetInterface`, and
  its req/s cost.
- Whether Igor PHP catches the planted scenarios. If it doesn't, it gets one line or
  nothing.
- The exact grep pattern for the playbook, tested on the demo.
- Re-check FrankenPHP, Octane and Symfony versions on publishing day; all three release
  often.

## Out of scope

- FrankenPHP's other features (early hints, Mercure, static binaries, hot reload).
- RoadRunner and Swoole comparisons. One sentence at most: the reset problem is the same
  on any long-running runtime.
- Memory-leak hunting, connection pooling and DB reconnects beyond one line in The limits.
- Production tuning (`num_threads`, `max_threads`, autoscaling).
- A Laravel benchmark.

## Open questions for Dragan

1. **One framework or two?** I'd benchmark `symfony/demo` only and show Laravel in the
   leak and reset sections. Alternative: a Laravel-first post, since Octane has the bigger
   audience, at the cost of building a Laravel app with real routes.
2. **Title.** The working title or *PHP-FPM Forgot Everything for You. Worker Mode
   Doesn't.*
3. **Slot.** It isn't release-timed, so it could go out before 8.6 GA, or right after the
   GA refreshes as the first non-release PHP post.
4. **Has worker mode run anywhere real for you?** A real incident would make a stronger
   lede than the planted one, but only if it can go through `CONFIDENTIALITY.md`. If not,
   the planted `curl` transcript carries the lede.

## Medium meta

- Tags: `PHP`, `Symfony`, `Laravel`, `Security`, `Software Engineering`. (`Performance` dropped with the benchmark.)
- Hero: two requests on one worker thread. Request 1 sets `user=alice`; request 2 arrives
  without a user, and the response box reads `alice`. The arrow between them is labelled
  with the `static` keyword.

## Cost to produce

Experiment (images, benchmark, eight scenarios): one to two sessions. Draft: one session.
Hero and voice check: one session.
