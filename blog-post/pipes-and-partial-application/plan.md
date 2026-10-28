# Plan: pipes and partial application (working title: "Pipes Were Half a Feature Until Partial Application Arrived")

**Status:** published on Medium on 2026-10-28 (agreed 2026-10-26). Re-run on the GA image after 19 November.

**Decisions (2026-10-26):**
- Title stays: *Pipes Were Half a Feature Until Partial Application Arrived*.
- The published `php-8.6-small-release` article is not touched. Its unparenthesised 8.5 example stays as it is.
- No public gist. The post describes the counting method inline.
- The corpus stays at two frameworks (Laravel, Symfony).
- The overlap with the 8.6 release post is accepted.
- Snippets are re-run on the newest 8.6 RC image available on the drafting day, and the labels follow it.
**Researched:** 2026-10-20, against PHP 8.4.26, 8.5.11 and 8.6.0 RC3 (RC4 due 22 October, GA 19 November 2026).
Experiment code and raw output: `~/Projects/writting-experiments/exp-pipes-pfa/` (`FINDINGS.md`, `snippets/`,
`counter/`, `raw/`).

---

## Positioning

Medium readers come for PHP. This post goes back to them in the weeks around **PHP 8.6 GA (19 November 2026)**,
when "what's new in 8.6" searches peak, so it should go out member-only and at or before GA week.

Every 8.6 roundup will show partial function application (PFA) with a `str_replace(' ', '-', ?)` one-liner.
This post earns its slot by doing three things those roundups don't:

1. **The same pipeline three times**, in 8.4, 8.5 and 8.6 style, each one run on the official image with its
   output shown, plus the parse error each older version gives for the newer syntax.
2. **What the engine does with it.** The 8.5 pipeline compiles to 4 closures and 3 dynamic calls. The 8.6 one
   compiles to zero closures (opcache dump, below). That turns "it reads nicer" into "it reads nicer *and* the
   wrapper disappears."
3. **A count on real code.** I parsed Laravel and Symfony with `nikic/php-parser` and counted the callbacks
   partial application could replace. The answer is modest (**about 3% in Laravel `src/`**), and saying so is
   the post's credibility. Pipes were half a feature. PFA completes pipes. It doesn't replace your closures.

**Stands alone.** No reference to the 8.6 release post or any other post here. It explains the pipe operator
and PFA from zero, in its own words, as briefly as the argument allows.

**Overlap to be aware of.** The published `php-8.6-small-release` article already has an 8.5-vs-8.6 pipeline pair
and the eager-evaluation gotcha. This post has to go further, not repeat it. The 8.4 baseline, the
parenthesis fatal, the opcodes, the count and the extra-arguments trap are all new. (Also see open question 1:
that article's 8.5 example doesn't run.)

## Thesis

The 8.5 pipe operator was only half usable on its own: any step that takes more than one argument had to be
wrapped in a parenthesised arrow function. Partial application is the other half. **With PFA, a PHP pipeline
compiles down to plain function calls, but in real codebases PFA replaces only a few percent of closures, so
adopt it for pipelines and leave your callbacks alone.**

## Title options

1. **Pipes Were Half a Feature Until Partial Application Arrived.** The working title, and my
   recommendation. A claim with a verb, searchable on both feature names, and sections 1–3 deliver it.
2. **Partial Application Fixes PHP Pipes. It Won't Replace Your Closures.** Leads with the count. It's more
   honest about the second half of the post, but it undersells the pipeline half.
3. **PHP 8.6 Makes the Pipe Operator Worth Using.** Short and release-timed, but closer to a news headline.

Subtitle (for #1): *I wrote the same pipeline for PHP 8.4, 8.5 and 8.6 and read the opcodes. Then I counted the
closures partial application could replace in Laravel: 71 out of 2,289.*

Provenance line: *Run on the official `php:8.4-cli`, `php:8.5-cli` and `php:8.6.0RC3-cli` images on 20 October
2026; counts from laravel/framework v13.37.0 and symfony/symfony v8.1.9. RC syntax is frozen, but I'll re-run
everything on the GA image.*

## Structure (standard long-form, 1,600–2,000 words, 7 sections)

### Lede (~200 words)
1. A concrete moment: you try `|>` on 8.5, write `|> fn($s) => …` like the examples you've seen, and get
   `Fatal error: Arrow functions on the right hand side of |> must be parenthesized`. A real error line from
   `raw/probe-run-2.txt`, not a persona.
2. The honest answer up front: on 8.5, pipes only work cleanly for one-argument functions. 8.6's partial
   application fixes that. It also deletes the closures. And it won't touch 90% of the closures in your
   codebase.
3. Thesis in bold, once.
4. Roadmap: the same pipeline three ways, what the engine does with each, the three gotchas, and what a count
   of Laravel and Symfony says about where PFA actually belongs.

### 1. `## One pipeline, three PHP versions` (~350 words)
The core before/after, all three verified (output `string(19) "php, laravel, pipes"` on each version that
parses them). Code is in `snippets/tags-8{4,5,6}.php`:

```php
// PHP 8.4: read it inside-out
$tags = implode(', ', array_values(array_unique(array_filter(
    array_map(fn($t) => strtolower(trim($t)), explode(',', $input))
))));
```

```php
// PHP 8.5: top to bottom, but most steps are wrapped
$tags = $input
    |> (fn($s) => explode(',', $s))
    |> (fn($a) => array_map(fn($t) => strtolower(trim($t)), $a))
    |> array_filter(...)
    |> array_unique(...)
    |> array_values(...)
    |> (fn($a) => implode(', ', $a));
```

```php
// PHP 8.6: partial application fills the gaps
$tags = $input
    |> explode(',', ?)
    |> array_map(trim(...), ?)
    |> array_map(strtolower(...), ?)
    |> array_filter(...)
    |> array_unique(...)
    |> array_values(...)
    |> implode(', ', ?);
```

Explain the two placeholders in two sentences: `?` is exactly one argument, `...` is the rest (RFC). Say which
version rejects what: 8.4 gives `syntax error, unexpected token ">"` and 8.5 gives `unexpected token "?"`. Pipes
are left-associative and bind looser than arithmetic but tighter than comparison and `??`. That's one sentence
with the RFC's `'beep' |> strlen(...) == 4` example.

### 2. `## What the engine sees: the closures disappear` (~250 words)
`php -d opcache.enable_cli=1 -d opcache.opt_debug_level=0x20000` on 8.6RC3:
- 8.5 version: **4 `DECLARE_LAMBDA_FUNCTION`, 3 `INIT_DYNAMIC_CALL`** in the pipeline.
- 8.6 version: **zero closures**. Every step is `INIT_FCALL` / `DO_ICALL` or `FRAMELESS_ICALL_2(implode)`, and
  both `array_map` calls are inlined.
Tie it to the PFA RFC's "Pipe operator" section: `foo(?)`, `foo(1, ?)`, `foo(1, a: ?)` and `foo(1, ...)` on the
right of a pipe are compiled to direct calls. php-src covers this in
`Zend/tests/partial_application/pipe_optimization_001.phpt` through `_015.phpt`. Show about 6 lines of each dump.
No timing benchmark (see Out of scope). The claim is "no closure is created", which the dump proves, not
"N% faster".

### 3. `## The three gotchas` (~400 words)
Each one has a runnable snippet and its real output:
1. **Arrow functions in a pipe need parentheses.** The fatal above. It came from errata added after the vote
   (RFC errata 2025-08-28, php-src PR #19533). Without the parentheses the arrow function would swallow the
   rest of the chain. Many pre-release examples on the web still show the unparenthesised form.
2. **Arguments in a partial are evaluated once, when it is created.** `label(?, nextId())` prints `a#1 b#1`,
   and the arrow version prints `c#2 d#3` (`snippets/eval-order.php`). Bind eagerly on purpose.
3. **`foo(...)` passes extra arguments through; `foo(?)` drops them.** A callback called with `(value, key)`,
   as Laravel's `Arr::map` does when it calls `array_map($callback, $array, $keys)`
   (`src/Illuminate/Collections/Arr.php:868`). `trim(...)` then receives the key as `$characters` and returns
   `" 10 "`. `trim(?)` returns `"10"` (`snippets/extra-args.php`). The RFC warns about this with `intval`. This
   is the most useful paragraph in the post for Laravel readers.
Plus one line on by-ref: `$a |> sort(...)` throws `sort(): Argument #1 ($array) could not be passed by
reference`, and pipes forbid by-ref callables by design.

### 4. `## I counted: where partial application actually fits` (~350 words)
Method in one paragraph and the table. The script is short enough to describe, but don't paste it (≤20-line
rule). It goes on a public gist if Dragan agrees (open question 4).

| Codebase (non-test code) | Closures + arrow fns | `foo(...)` already works (since 8.1) | Needs PFA | PFA, but changes eval timing | Neither |
|---|---|---|---|---|---|
| laravel/framework v13.37.0 `src/` | 2,289 | 130 (5.7%) | **71 (3.1%)** | 26 (1.1%) | 2,062 (90.1%) |
| symfony/symfony v8.1.9 `src/` (non-test) | 1,361 | 19 (1.4%) | **71 (5.2%)** | 4 (0.3%) | 1,267 (93.1%) |

("Needs PFA" = `pfa_clean` + `pfa_reorder`. Laravel's 71 includes 7 that need named placeholders because the
closure passes params out of order, e.g. `fn ($value, $key) => $this->hasHeader($key, $value)`.)

Real examples from each bucket, quoted with file:line, e.g.
`array_map(fn ($group) => static::collapse($group, $min, $max), $groups)`
(`Console/Scheduling/CronExpressionTimezoneConverter.php:283`) → `static::collapse(?, $min, $max)`, and
`->map(fn ($property) => sprintf('<fg=gray>%s</>', $property))` (`Database/Console/ShowModelCommand.php:114`).

The reading: Laravel has 130 arrow functions that could have been first-class callables since 8.1 and weren't.
Some of those may be deliberate, because of gotcha 3. For those, `foo(?)` is the safe spelling 8.6 adds. The
other ~90% are multi-statement bodies, nested calls or params used twice, and PFA isn't for them.

### 5. `## Playbook: adopting pipes and PFA this week` (~250 words)
1. Run your pipeline-shaped code on `php:8.6-rc-cli` (or GA). Note the image has no `mbstring`, so install it or
   avoid `mb_*` in the probe.
2. Rewrite one nested-call chain as a pipe, and use `?` for every multi-argument step.
3. Grep for unparenthesised arrow functions after `|>` if you adopted pipes on 8.5 from early examples.
4. Prefer `foo(?)` over `foo(...)` for callbacks that may receive extra arguments.
5. Only bind values that are safe to evaluate once.
6. Run the counter on your own `src/` to see whether PFA is a style change worth a Rector rule or a handful of
   hand edits.
Cost estimate: **to be timed at drafting**. The counter took seconds per corpus, but no number goes in until the
whole playbook has been timed end to end.

### 6. `## The limits` (~150 words)
RC3 isn't GA. The counter is a syntactic heuristic: it doesn't know function signatures, so it can't see arity
traps (gotcha 3) or the closure's own parameter types, which PFA replaces with the target function's. "Stable"
arguments are judged conservatively (captured variables count as stable, any call or property fetch counts
as eager). Two frameworks are not a survey, and both still support 8.3/8.4 (`"php": "^8.3"` and
`">=8.4.1"`), so neither can use pipes or PFA yet. No `new` (constructors) and no `compact()`/`extract()`
family, per the RFC.

### 7. `## Verdict` (~120 words)
Compressed thesis. The position: use pipes plus PFA for data-transformation chains from 8.6. Don't run a mass
"convert closures to partials" refactor, because the numbers say it buys about 3%. The action with a
threshold: take your longest nested-call chain and rewrite it as a pipe on the RC image. If every step becomes
`foo(?)` or `foo(...)`, adopt the style. If you still need a wrapped arrow function in every other step, your
code isn't pipe-shaped and you lose nothing by waiting.

### `### Sources`
- [RFC: Pipe operator v3](https://wiki.php.net/rfc/pipe-operator-v3) — PHP wiki (vote 33–7, errata 2025-08-28)
- [RFC: Partial Function Application v2](https://wiki.php.net/rfc/partial_function_application_v2) — PHP wiki
  (vote 33–0–0)
- php-src PR #19533 (arrow function parentheses); commits 1c09c0c8 (pipe), 5472cac8 and b5fba859 (PFA)
- php-src `PHP-8.6`: `Zend/tests/pipe_operator/`, `Zend/tests/partial_application/pipe_optimization_*.phpt`
- PHP 8.6.0 RC3 announcement — php.net; `nikic/php-parser` v5.9.0 — Packagist
- laravel/framework v13.37.0 and symfony/symfony v8.1.9 at the commits counted

## Evidence status

**Verified (20 Oct 2026, raw output saved):**
- Pipe RFC: Implemented in 8.5, vote **33–7**. Arrow functions must be parenthesised (errata, PR #19533). By-ref
  callables are disallowed. Precedence examples are in the RFC.
- PFA RFC: Implemented in 8.6, vote **33–0–0**. `?` and `...` semantics, eager evaluation, the extra-args
  caution, the pipe compile-time optimisation list, and no constructors or scope functions.
- All three `tags-8x.php` snippets print the same output. Each older version's parse error is captured.
- The parenthesis fatal on 8.5.11 and 8.6RC3. The `sort(...)` by-ref error. The eval-order and extra-args
  outputs. The `ArgumentCountError` text for `str_replace(?)`.
- Opcode counts: 4 lambdas + 3 dynamic calls (8.5 style) vs 0 (8.6 style), on 8.6RC3 with opcache.
- `php:8.6.0RC3-cli` lacks `mbstring`.
- php-src `PHP-8.6` has 32 pipe tests and 151 PFA test files, including `pipe_optimization_001–015`.
- The counts above, and Laravel's `Arr::map` passing keys (`Arr.php:868`).

**Open (check at drafting):**
- Re-run every snippet and the opcode dump on RC4 (22 Oct) and on GA (19 Nov).
- The one parse error per corpus in the counter: identify the file, and confirm it doesn't change a count by
  more than noise.
- Hand-check a larger sample of each bucket (I spot-checked 6 per bucket in Laravel `src/` and they looked
  right) and report the false-positive rate. One known conservative case: `substr($r, strlen($relationName) + 1)`
  is counted as eager although it is stable.
- A reason breakdown for the 90% "neither" bucket (multi-statement vs nested vs reused param), if it fits.
- Does Laravel's `Collection::map` go through `Arr::map` with keys in v13.37.0? Quote the exact line used.
- Whether the php.net 8.6 docs page for PFA exists yet. Link to it if so.
- Timing for the playbook's cost estimate.

## Out of scope

- A runtime benchmark. The opcode dump makes the "no closure" claim; a microbenchmark invites argument and adds
  nothing.
- The function composition operator (`+`/`∘` RFC, future scope) and the declined `|>=`. One sentence at most.
- The full PFA grammar (variadic renumbering, LSB errata, reflection). Link to the RFC.
- Rector rules. Mention only if one exists at drafting (unchecked).
- Other 8.6 features and the deprecation list.

## Medium meta

- Tags: `PHP`, `Laravel`, `Programming`, `Software Engineering`, `Functional Programming`.
- Member-only. Publish in the run-up to GA or in GA week, after the RC4/GA re-run.
- Hero: the three-version pipeline as three stacked blocks, with the 8.5 block's closures marked and the 8.6
  block's caption "0 closures". It carries the claim, not a motif.

## Open questions for Dragan

1. **The published `php-8.6-small-release` article's 8.5 example doesn't run.** It writes `|> fn($s) => trim($s)`
   without parentheses, which is a fatal error on 8.5.11 and 8.6RC3. Fix it at the GA refresh? (Not touched by
   this brief.)
2. Title: keep the working title (#1) or lead with the count (#2)?
3. Is the overlap with the 8.6 release post acceptable, given this one adds the 8.4 baseline, opcodes, the count
   and two new gotchas?
4. Publish `counter/count.php` as a public gist so readers can run it on their own code?
5. Add a third corpus (e.g. a large application rather than a framework), or keep it to two frameworks?

## Cost to produce

RC4/GA re-run and the open checks: one to two hours. Draft: one session. Hero and voice check: one session.
