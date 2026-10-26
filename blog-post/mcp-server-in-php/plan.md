# Plan — MCP server in PHP (working title: "Writing an MCP Server in PHP")

**Status:** agreed 2026-10-26. Drafted as `article.md` the same day.

**Decisions (Dragan, 2026-10-26):**
- Title #1: **MCP Went Stateless. PHP Was Ready.**
- Client-neutral: verify with MCP Inspector only. No Claude Code transcript, no API keys anywhere.
  The build-plan item about an AI client and the "AI client answering a question" check are dropped.
- symfony/demo as the app, with one Laravel paragraph.
- Don't wait for `mcp/sdk` 1.0; state the versions in the provenance line.
- Build the server and verify it end to end before writing about it.

**What moved between the brief and the draft (re-checked 2026-10-26):** `symfony/mcp-bundle` v0.15.0
(23 Oct) moved to `mcp/sdk` ^0.9, so the "bundle one SDK minor behind" papercut is gone; v1.0.0-BETA1
followed on 26 Oct with no significant changes. The `structuredContent` difference is explained (the
handshake era only allows an object; `2026-07-28` allows any JSON value, SEP-2106). The gotcha is
reproduced under PHP-FPM and through MCP Inspector 2.12.0 in `legacy` mode. `laravel/mcp` 1.x speaks
`2026-07-28` by default, and its download count is mostly `laravel/boost` installs. Details in
`~/Projects/writting-experiments/exp-mcp/FINDINGS.md`, section "Drafting run".

**Researched:** 2026-10-20. Feasibility probe run the same day, saved under
`~/Projects/writting-experiments/exp-mcp/` (`FINDINGS.md`, raw outputs next to it). No client
material; every piece of evidence is code built and run for this post.

---

## Positioning

The Medium audience comes for PHP, and AI+PHP posts did well in 2025. This one is AI material
with real PHP evidence in it: a Symfony app, a Composer install, a tool written as a PHP method,
and two failures you only hit in PHP. That's what keeps it from being a generic MCP explainer
with a PHP coat of paint.

The landscape changed this year and most of what search returns is out of date:

- **There is an official PHP SDK.** `modelcontextprotocol/php-sdk`, package `mcp/sdk`, described
  on GitHub as "Maintained in collaboration with The PHP Foundation". Its README calls it "a
  collaboration between the PHP Foundation and the Symfony project", and it started from
  `php-mcp/server` (Kyrian Obikwelu) plus the Symfony AI initiative. Composer authors:
  Christopher Hertel, Kyrian Obikwelu, Tobias Nyholm.
- **It's still pre-1.0.** v0.9.0 shipped 18 Oct 2026, the thirteenth release since v0.1.0
  (20 Nov 2025). The README says it's "experimental" until the first major. `docs/sdk-tier.md`
  puts it at **Tier 3** per the 19 Aug 2026 audit: server conformance 67/67, client 10/50 (almost
  all OAuth). v0.9.0's notes carry a long list of `[BC Break]` items.
- **MCP itself went stateless.** Spec revision `2026-07-28` (released 28 Jul 2026) drops the
  `initialize` handshake and `Mcp-Session-Id`. Every request now carries its protocol version and
  client capabilities in `params._meta` (SDK `docs/protocol-versions.md`). The SDK serves both eras
  from one endpoint.

That last point is the post's reason to exist. **Session-based MCP over HTTP is a bad fit for
PHP's request model, and the new revision removes exactly that part.** The probe shows it in four
`curl` calls.

**Stands alone.** No reference to other posts in this repo. A reader who has never seen MCP gets
two sentences on what a server, a tool and a client are, then code.

## Library choice — what the evidence supports

| Option | Version (20 Oct) | Built on | Fit for this post |
|---|---|---|---|
| `mcp/sdk` (official) | v0.9.0, PHP `^8.1` | itself | **Core of the post.** Framework-agnostic, official, the thing the reader will search for |
| `symfony/mcp-bundle` | v0.14.1 | `mcp/sdk` `^0.8.1` | **The demo app.** symfony/demo is Symfony 8.1, the bundle wires discovery, DI, a console command and a route |
| `laravel/mcp` | v1.0.2, PHP `^8.2` | its own implementation (no `mcp/sdk` in `composer.json`) | One paragraph: the Laravel route, already 1.x, most downloads (8.86M/month on Packagist vs 1.43M for `mcp/sdk`) |
| `php-mcp/server` | 3.3.0 (12 Jul 2025), last push 9 Aug 2025 | ReactPHP | One sentence: the SDK's ancestor, supports protocol `2025-03-26`, effectively superseded |

Decision: write against **`mcp/sdk` directly** for the hello-world and the session gotcha (so the
reader sees what the protocol does without a framework hiding it), then move the same idea into
symfony/demo with **`symfony/mcp-bundle`** for the real-app section. Not Laravel: the brief's app
is Symfony, and covering both would double the length. The Laravel paragraph says so.

## Thesis

PHP got an official MCP SDK this year, and the protocol changed under it in the same year — in
PHP's favour. **MCP's new stateless revision fits PHP's request model; the session-based one
quietly breaks it.** Build your server against the stateless revision and you get a plain PHP
endpoint. Build it the 2025 way and the SDK's default session store forgets every client after
the first request.

## Title options

1. **MCP Went Stateless. PHP Was Ready.** — recommended. A claim with a verb, and it puts PHP in
   the title for search. Risk: "was ready" undersells the two gotchas.
2. **Your PHP MCP Server Forgets Every Client After One Request** — sharpest, built on the
   probe's 404. Narrows the post to the gotcha section.
3. **Writing an MCP Server in PHP Is Easy. Running It Over HTTP Isn't.** — honest, closest to the
   working title and to what people type into search.

Subtitle (for #1): *The official PHP SDK is pre-1.0 and the protocol dropped sessions in July. I
put a Symfony app's blog posts behind MCP, and the hardest part was the one PHP never had:
remembering a client between requests.*

Provenance line: *Written against `mcp/sdk` v0.9.0, `symfony/mcp-bundle` v0.14.1 and MCP spec
revision `2026-07-28`, on PHP 8.4. The SDK is pre-1.0 and ships breaking changes in minor
releases; check the changelog before copying code.*

## Evidence in hand (probe, 2026-10-20)

All under `~/Projects/writting-experiments/exp-mcp/`.

1. **Hello world is one attribute.** `hello/src/Greeter.php`: one `#[McpTool]` method. Over stdio,
   `initialize` → `tools/list` → `tools/call` all answer (`hello/stdio-out.txt`). The docblock
   became the tool's `description`, the method signature became its `inputSchema`.
2. **The session gotcha.** `hello/http.php` behind `php -S`, the SDK's default
   `InMemorySessionStore`: `initialize` returns 200 and a `Mcp-Session-Id`; the next request
   gets **404** and `{"code":-32600,"message":"Session not found or has expired."}`
   (`hello/http-out.txt`, first block). With `FileSessionStore`: 202, then 200
   (`hello/http-filestore-out.txt`). The SDK documents this in `docs/run/sessions.md` ("PHP often
   serves each request in a different process"), but the default is still in-memory, and stdio
   hides the problem completely.
3. **The stateless revision needs no store at all.** The same `http.php`, same in-memory default:
   a `2026-07-28` `tools/call` with the `_meta` envelope and `Mcp-Method` / `Mcp-Name` headers, no
   `initialize`, no session — **200** (`hello/http-out.txt`).
4. **symfony/demo over MCP.** `demo/src/Mcp/BlogTools.php`: `search_posts(string $query, int
   $limit = 5)` over `PostRepository::findBySearchQuery()`, about 20 lines. Over stdio via
   `php bin/console mcp:server` it lists and calls (`demo-stdio-out.txt`). The bundle defaults to
   a file store (`var/cache/dev/mcp-sessions/default`), so the in-memory gotcha doesn't apply
   there.
5. **Two install papercuts on the Symfony path.** `symfony/mcp-bundle` v0.14.1 resolves
   **`mcp/sdk` v0.8.1**, one SDK minor behind, because its constraint is `^0.8.1` (bundle `main`
   already requires `^0.9`). No `mcp.yaml` recipe was created, and the HTTP route answered **500
   "No PSR-17 server request factory found"** until `composer require nyholm/psr7`
   (`demo-http-out.txt`).
6. **An unexplained difference.** Over HTTP on the bundle, the `2026-07-28` answer carries
   `structuredContent` (a JSON list) and the handshake-era answer doesn't. To check at drafting
   whether a list is even allowed there; v0.9.0 started validating `structuredContent` against
   `outputSchema`. Don't publish until it's understood.

**Not yet done:** an actual AI client using the server. The probe drove the protocol with raw
JSON-RPC (`printf | php`, `curl`). See the build plan.

## Structure (standard long-form, 1,700–2,000 words, 8 sections)

**Lede.** The dated trigger: an official PHP SDK exists, and in July the protocol dropped
sessions. The honest answer up front: writing the tool is one attribute on a method. Serving it
over HTTP the 2025 way fails on the second request with the SDK's own defaults. Thesis in bold.
Roadmap: the SDK, a tool on a real app, the HTTP trap, the stateless fix, a client using it.

1. **`## The official SDK: real, useful, pre-1.0`** — what `mcp/sdk` is, who maintains it, v0.9.0,
   Tier 3, 67/67 server conformance, the `[BC Break]` warning. Laravel and `php-mcp/server` in
   three sentences.
2. **`## A tool is a method with an attribute`** — `Greeter` in ~12 lines, then the stdio exchange
   (`tools/list` showing the generated schema). Two sentences on tools vs resources vs prompts.
3. **`## Putting a real app behind it`** — `BlogTools::search_posts()` on symfony/demo, the
   `mcp.yaml`, `bin/console mcp:server`. The two papercuts (SDK 0.8.1 via the bundle, missing
   PSR-17).
4. **`## The second request is where PHP breaks`** — the gotcha. The four-`curl` sequence with
   the 404, why it happens (in-memory store, a fresh PHP process per request), the fix with
   `FileSessionStore` or Redis via `Psr16SessionStore`, and why stdio tests never show it.
5. **`## The stateless revision: what PHP always assumed`** — what `2026-07-28` removed, the
   `_meta` envelope as a short JSON block, the same call answered 200 with no store. The point:
   the protocol now matches PHP's shared-nothing request model, and one endpoint still serves both
   eras.
6. **`## Playbook: from Composer to a client in an afternoon`** — numbered, real commands:
   1. `composer require mcp/sdk symfony/finder` (or `symfony/mcp-bundle nyholm/psr7`)
   2. Write one `#[McpTool]` method; keep the return type plain.
   3. Test over stdio with raw JSON-RPC, then with MCP Inspector.
   4. Before HTTP, pick a shared session store, or confirm your client speaks `2026-07-28`.
   5. Put the route behind your firewall like any other endpoint (bundle docs:
      `access_control` on `^/mcp`).
   6. Connect a real client.

   Cost estimate: measure at drafting. The probe took under an hour, but that included reading
   docs. No number goes in until it's timed from a clean start.
7. **`## The limits`** — pre-1.0 with BC breaks in minors; bundle one minor behind; OAuth client
   side unfinished (resource-server auth only on the server side, ADR 0002); which clients speak
   `2026-07-28` (open); a search tool that returns titles is a toy, and real exposure of app data
   is an authorization question first.
8. **`## Verdict`** — compressed thesis, then the action with a threshold: run the four `curl`
   calls against your own endpoint. A 404 on the second one means you're on the in-memory store
   and every HTTP client will fail after `initialize`; a 200 on the stateless call means you're
   ready for the revision clients are moving to.

`### Sources` — `modelcontextprotocol/php-sdk` (README, `docs/protocol-versions.md`,
`docs/run/sessions.md`, `docs/sdk-tier.md`, v0.9.0 release notes); MCP spec `2026-07-28`
changelog; `symfony/mcp-bundle` docs in `symfony/ai`; `laravel/mcp`; audit issue
modelcontextprotocol/modelcontextprotocol#3274.

## Build plan (at drafting)

Everything in `~/Projects/writting-experiments/exp-mcp/`, on the existing
`writting-experiments-php:8.4` image. The probe already did 1–3.

1. `hello/` — bare SDK, stdio and HTTP, both stores, both eras. **Done.**
2. `demo/` — local clone of symfony-demo @ `8d2e2ef`, bundle, `search_posts`. **Done** for stdio
   and HTTP.
3. Re-check the bundle's latest release: if one ships on `mcp/sdk` 0.9, re-run on it.
4. Add a second capability so the post shows more than one shape: a resource template
   `post://{slug}` returning the post body, or a `latest_posts` tool. Keep one; the post has
   room for two code blocks of app code, not four.
5. Resolve the `structuredContent` difference (evidence item 6): read the spec, add an
   `outputSchema` or return an object, re-run.
6. **Client test, the part the post promises.** MCP Inspector against stdio and HTTP for a
   screenshot of the protocol. Then one AI client calling `search_posts` from a natural-language
   question, with the transcript saved. Candidate: Claude Code (`claude mcp add` against the
   stdio command or the HTTP URL), using Dragan's own login, not an API key. Nothing that gets
   written down contains a key.
7. Time a clean run of the playbook for the cost estimate.

## Transport choice

- **stdio** for the first contact and the local-client demo: no session problem, no web server,
  and it's how desktop and CLI clients launch local servers.
- **Streamable HTTP** for the main argument, because that's how a PHP app is actually deployed
  and where the gotcha lives. Shown under `php -S` in the probe. At drafting, re-run once under
  PHP-FPM (or FrankenPHP if there's time) so "a new process per request" is shown, not inferred
  from the built-in server.
- No legacy HTTP+SSE: deprecated in the spec and not what the SDK centres.

## How the demo is verified

- Raw JSON-RPC over stdio and `curl` over HTTP, outputs saved as files (done).
- MCP Inspector listing and calling the tool (drafting).
- One AI client answering a question by calling `search_posts`, with the call visible in its
  transcript and the result matching what `findBySearchQuery()` returns for the same query in
  `bin/console` (drafting).
- `vendor/bin/phpunit` on the demo still passes 53 tests after the bundle goes in (drafting; not
  run in the probe).

## Facts: verified vs open

**Verified on 20 Oct 2026 (primary sources or the probe):**
- `mcp/sdk` repo, description, maintainers, Composer authors, PHP `^8.1`, v0.9.0 on 18 Oct,
  v0.1.0 on 20 Nov 2025, "experimental" until 1.0, Tier 3 with 67/67 server and 10/50 client.
- Spec revisions in `modelcontextprotocol/modelcontextprotocol/schema`: `2025-11-25` and
  `2026-07-28` (released 28 Jul 2026).
- `symfony/mcp-bundle` v0.14.1 (27 Sep) needs `mcp/sdk` `^0.8.1`; `laravel/mcp` v1.0.2 (12 Oct)
  has its own implementation; `php-mcp/server` 3.3.0, last push 9 Aug 2025.
- Packagist monthly downloads on 20 Oct: `laravel/mcp` 8.86M, `mcp/sdk` 1.43M,
  `symfony/mcp-bundle` 0.94M, `php-mcp/server` 0.09M.
- Every behaviour in "Evidence in hand", from the probe.

**Open, re-check at drafting:**
- The spec's own wording for what `2026-07-28` removed. The brief currently relies on the SDK's
  `docs/protocol-versions.md`; the article quotes the spec changelog.
- Which AI clients speak `2026-07-28` today, and whether they fall back to the handshake. This
  decides how hard the verdict can lean on "use the stateless revision".
- Whether `laravel/mcp`'s download count comes mostly from being a dependency of another Laravel
  package (it looks inflated next to its 853 stars). Don't print the comparison without that check.
- New `mcp/sdk` or bundle releases; any 1.0 date (none announced; don't imply one).
- The `structuredContent` list (evidence item 6).
- Whether the gotcha behaves the same under PHP-FPM as under `php -S` (it should; show it).

## Out of scope

- Writing an MCP **client** in PHP, and the Symfony AI agent components.
- OAuth and authorization beyond one paragraph in the limits section.
- Laravel walkthrough. Resources and prompts beyond the one extra capability.
- Comparing PHP with the TypeScript or Python SDKs.
- Performance, FrankenPHP worker mode, async.
- Any claim about what an AI model "understands" about the tool. Only what the transcript shows.

## Medium meta

- Tags: `PHP`, `Symfony`, `AI`, `Model Context Protocol` (check that the tag exists on Medium;
  fallback `LLM`), `Programming`.
- Publish: no release date to hit, so not ahead of a PHP 8.6 GA post. If `mcp/sdk` 1.0 or a
  bundle release on 0.9 is announced, publish in that week and say so in the provenance line.
- Hero: two lanes, same tool call. Top: `initialize` → 200 → `tools/call` → **404**. Bottom: one
  `tools/call` with the `_meta` envelope → 200. Mono-caps line: `MCP IN PHP`.

## Cost to produce

Finish the build plan (items 3–7): half a day, most of it the client test and resolving the
`structuredContent` question. Draft: one session. Hero and voice check: one session.

## Open questions for Dragan

1. **Title.** #1 (stateless angle, recommended), #2 (the gotcha), or #3 (closest to the working
   title)?
2. **AI client for the demo.** Is Claude Code under your own login OK for the client test and a
   transcript in the post? Or would you rather show MCP Inspector only and keep the post
   client-neutral?
3. **Laravel.** One paragraph, as planned, or does the PHP audience on Medium (Laravel-heavy)
   justify a Laravel-first variant instead of symfony/demo?
4. **Timing.** Hold for `mcp/sdk` 1.0 or the next bundle release, or publish as soon as it's
   drafted, after the PHP 8.6 GA posts?
