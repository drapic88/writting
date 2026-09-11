# Writing from real work without publishing your client

Most of what is worth writing here comes from paid work: a migration that went wrong, a
review process that took three iterations to get right, a production incident at 02:00.
That material is the reason the posts are credible. It is also not mine to give away.

The rule is a split, and it is not negotiable:

> **Every pattern carries over. Every identifier is replaced.**

The mechanism, the failure mode, the numbers, the sequence of events, the argument — all
publishable. The employer, the client, the repository names, the ticket IDs, the people,
the infrastructure layout — never, in any format.

Read this before drafting anything derived from real work: a blog post, a story, or a book
chapter. Stories are the sharpest case, because a narrative wants exactly the specifics
that identify people.

---

## 1. The substitution table

Use these consistently across everything, so a reader following several pieces sees one
coherent, fictional-but-stable stack rather than a new disguise each time.

| Internal | Public |
|----------|--------|
| employer / client name | "the team", "a company I work with" — never named |
| governance repo | `agent-guidelines` |
| Angular 20 + SSR app | `web-app` |
| Astro 5 static site | `marketing-site` |
| Java 17 / Spring Boot API | `rest-api` |
| Angular 17 admin panel | `admin-app` |
| Flutter app | `mobile-app` |
| Kubernetes manifests repo | `infra` |
| `RENO-1234` | `PROJ-1234` |
| internal script paths | `scripts/prepare-review.sh`, `scripts/install-setup.sh` |
| `.agentic-review/<ts>/` | `.review/<ts>/` |
| `.jira-cache/assigned/` | `.ticket-cache/assigned/` |
| specific JQL, Confluence reports, internal doc names | described, never quoted |

Extend the table rather than inventing a one-off alias in a draft. A name that appears in
two pieces must mean the same system in both.

## 2. People

A story needs a cast. The cast does not need names.

- **Default to role.** "the platform lead", "the engineer who owned the deploy", "our SEO
  partner". A role tells the reader what they need — authority, stake, blast radius.
- **A first name only when the person agreed**, and only a first name. Ask before drafting,
  not before publishing.
- **Invented first names are allowed for readability**, and must be disclosed once (§5).
  `VOICE.md` §4 endorses the named persona — "Let me tell you the story of John" — and that
  device stays available. John is not a real colleague with the serial numbers filed off;
  John is openly a device.
- **Never a composite presented as one real person.** If three incidents were merged into
  one narrative, say so, or don't merge them.
- **Nobody is the villain.** If the story needs someone to have been wrong, it is either me
  or "we". A published piece that makes a named role look incompetent is a piece that gets
  back to them.
- No email addresses, no Slack handles, no screenshots with a sidebar in them.

## 3. Time, numbers and evidence

The evidence rule from `VOICE.md` survives anonymisation. What changes is precision that
identifies rather than informs.

- **Keep durations, drop dates.** "Four hours of downtime" is the evidence. "On 14 March"
  is the fingerprint. Say "a Tuesday in spring", or shift the date by weeks and say you did.
- **Keep magnitudes, round the specifics.** "Roughly 40,000 orders" over the exact figure
  that can be matched against a public earnings report.
- **Keep log lines and stack traces, scrub the hostnames**, internal domains, bucket names,
  account IDs, IP ranges and tokens. Replace with the placeholder stack in §1.
- **Keep commit subjects, drop hashes and URLs** that resolve to a private repo.
- **Never publish anything that reads as a map of a production environment** — what is
  protected, what isn't, where the gap was, which vendor sits where. This is the one rule
  that outranks the evidence rule. When the two conflict, cut the evidence and say the post
  is thinner for it.
- **Security specifics get an extra gate.** A fixed vulnerability is publishable once fixed
  and once the affected party has said yes. An unfixed one is not publishable at all.

## 4. Policy material

Publish the *shape* of a policy, never the artefact.

Deny / ask / allow lists, review gates, branch protection rules and the like go out as "here
is how to think about the three tiers", with invented example rules. Not "here is our
config". A verbatim deny-list tells a reader exactly which command was worth denying, which
is the same as telling them what wasn't.

## 5. Disclosure

When details were changed, say so once, in the italic provenance line under the subtitle.
One sentence, no apology:

> *Names and identifying details are changed. The timeline, the numbers and the terminal
> output are as they happened.*

Or, where more was reshaped:

> *A composite of two migrations a year apart, told as one. Every failure described happened.*

This costs nothing and buys the reader's trust in everything that was *not* changed. A
piece with no disclosure line is asserting that everything in it is literal.

## 6. The check before publishing

Run this against any draft derived from real work.

- [ ] No employer, client, vendor or product name that wasn't already public.
- [ ] Every repo, service, path and ticket ID matches the table in §1.
- [ ] No real person identifiable by name, role-plus-company, or a detail only they have.
- [ ] Consent obtained where a real first name, a quote, or a photo is used.
- [ ] Dates shifted or vague; durations and magnitudes kept.
- [ ] Logs, traces and configs scrubbed of hosts, domains, IDs, keys and IP ranges.
- [ ] Nothing that maps a live environment's defences or gaps.
- [ ] No verbatim internal policy, deny-list, JQL, or document title.
- [ ] Disclosure line present if anything was changed.
- [ ] Would I be comfortable if the client's CTO read this and recognised the project?
      That is the real test, and it is the only one on this list that isn't mechanical.
