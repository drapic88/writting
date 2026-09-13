---
name: hero-image
description: Author and export the lead image for a post, story or book chapter — hero.svg in the established visual system, exported to hero.png at 2x. Use for "make the hero", "the lead image", "cover image", "export the SVG to PNG", or when a draft is finished and needs its image.
---

# Hero images

Authored as SVG in the piece's folder, exported to PNG. The SVG is the source; the PNG is
disposable and regenerated.

## The system

One visual system so pieces read as a set. Established by
`blog-post/context-is-the-product/hero.svg` — read that file before authoring a new one.

- **Canvas:** `viewBox="0 0 1400 650"` with matching `width`/`height`. Export at 2× →
  2800×1300.
- **Palette:** ink `#12203A`, muted `#6B7789`, accent `#E0662E`, ground `#FAF8F4`, with
  `#E4DED3` as the pale tint for rules and ghosted shapes. Two colours plus ink; no
  gradients.
- **Type stack, declared as CSS classes in `<defs>`:** Georgia/serif for the title (`.h`),
  `SF Mono`/monospace for labels and data (`.m`), system sans for the subtitle and body
  (`.s`). System fonts only — a webfont will not resolve during export.
- **Composition:** accent rule, then a kicker in spaced monospace caps naming this piece's
  own subject (`CONTEXT WINDOWS`, `TOKENS · WINDOWS`), then the title, then the subtitle.
  Diagram on the right or below.
- **No number and no series label.** Pieces are independent; the image carries the subject,
  never a position in a sequence. Nothing numbered goes on a hero.
- **`role="img"` and an `aria-label` that restates the thesis**, matching the alt text the
  draft uses.

The diagram carries the post's actual claim — the three context sources, the evidence chain,
the real numbers from the piece. Not decoration.

## Export

```bash
scripts/hero-export.sh blog-post/context-is-the-product/hero.svg
```

Writes `hero.png` next to the SVG at 2× and prints the resulting dimensions. Confirm they
are exactly double the SVG's `width`/`height` before considering it done.

The script renders through headless Chrome, because no SVG rasteriser (`rsvg-convert`,
`inkscape`, `resvg`, `magick`, `cairosvg`) is installed on this machine. `qlmanage` is not a
substitute — it pads to a square and crops. If Chrome moves, the path is one line at the top
of the script.

## Checks

- [ ] PNG dimensions are exactly 2× the SVG's declared size.
- [ ] Nothing clipped at the edges; the ground colour reaches all four sides.
- [ ] Text is legible at Medium's rendered width — nothing under 14px in SVG units.
- [ ] `aria-label` restates the thesis, and matches the draft's alt text.
- [ ] Only system fonts; no external references of any kind in the SVG.
- [ ] Open the exported PNG and look at it. Do not report an export you have not viewed.
