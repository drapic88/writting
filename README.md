# Writing

Dragan Rapić's writing workspace. Four formats, one voice.

| Format | Where | Craft spec | What it is |
|--------|-------|-----------|------------|
| Blog posts | [`blog-post/`](blog-post/) | [`blog-post/CRAFT.md`](blog-post/CRAFT.md) | technical posts for Medium, currently the ten-part *From Assistant to Agent* series |
| Stories | [`stories/`](stories/) | [`stories/CRAFT.md`](stories/CRAFT.md) | narrative non-fiction for the personal site — AI and technology accounts from real work |
| Books | [`books/`](books/) | [`books/CRAFT.md`](books/CRAFT.md) | long-form; scaffold in place, no book chosen yet |
| Croatian, any format | alongside the English piece | [`CROATIAN.md`](CROATIAN.md) | originals, never translations |

## The shared layer

- **[`VOICE.md`](VOICE.md)** — the voice. The evidence rule, the stance, sentence mechanics,
  the devices, the anti-patterns. Read before drafting anything.
- **[`CONFIDENTIALITY.md`](CONFIDENTIALITY.md)** — writing from real work without publishing
  a client. Every pattern carries over, every identifier is replaced.
- **[`CROATIAN.md`](CROATIAN.md)** — register, terminology and mechanics for Croatian pieces.
- **[`CLAUDE.md`](CLAUDE.md)** — how the agent works in this repository.

The one rule, inherited from the finished drafts and applying to all four formats:

> **Every claim ends in a file path, a command, a number, a vote count, or a quote.**

## Skills

`.claude/skills/` holds five, invocable by name:

| Skill | For |
|-------|-----|
| `write-blog-post` | a Medium post, brief through draft |
| `write-story` | a story for the site |
| `write-book` | premise, outline, chapter brief, chapter draft |
| `hero-image` | the lead image, authored as SVG and exported at 2× |
| `voice-check` | auditing a finished draft against the specs — reports, does not rewrite |

Each one loads `VOICE.md` plus the craft spec for its format, and adds `CROATIAN.md` when
the piece is in Croatian.

## Scripts

`scripts/hero-export.sh <path/to/hero.svg>` rasterises a hero SVG to PNG at 2×, reading the
size from the SVG itself. It renders through headless Chrome because no SVG rasteriser is
installed on this machine.

## Workflow

Every format works the same way: **brief first, agreed, then the draft.**
`plan.md` → `article.md` for posts, `plan.md` → `story.md` for stories, `brief.md` →
`draft.md` for chapters. The brief is where a piece gets cancelled cheaply.
