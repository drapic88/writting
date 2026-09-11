#!/usr/bin/env bash
# Rasterise a hero SVG to PNG at 2x, edge to edge.
#
#   scripts/hero-export.sh blog-post/03-context-is-the-product/hero.svg
#   scripts/hero-export.sh path/to/hero.svg 2   # explicit scale factor
#
# Writes hero.png next to the SVG. Reads width/height from the SVG's own
# width/height attributes, so the PNG is always the authored size x scale.
#
# No SVG rasteriser is installed on this machine; Chrome's headless renderer is
# the one thing available that gets fonts and gradients right. If Chrome moves,
# this is the only line to change.
set -euo pipefail

CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
SVG="${1:?usage: hero-export.sh <path/to/hero.svg> [scale]}"
SCALE="${2:-2}"

[ -f "$SVG" ] || { echo "no such file: $SVG" >&2; exit 1; }
[ -x "$CHROME" ] || { echo "Chrome not found at $CHROME" >&2; exit 1; }

W=$(sed -n 's/.*[^-]width="\([0-9.]*\)".*/\1/p' "$SVG" | head -1)
H=$(sed -n 's/.*[^-]height="\([0-9.]*\)".*/\1/p' "$SVG" | head -1)
[ -n "$W" ] && [ -n "$H" ] || { echo "could not read width/height from $SVG" >&2; exit 1; }

DIR=$(cd "$(dirname "$SVG")" && pwd)
OUT="$DIR/$(basename "${SVG%.svg}").png"
WRAP=$(mktemp -d)/wrap.html
cat > "$WRAP" <<HTML
<!doctype html><meta charset="utf-8">
<style>html,body{margin:0;padding:0;overflow:hidden}svg{display:block}</style>
$(cat "$SVG")
HTML

"$CHROME" --headless --disable-gpu --hide-scrollbars \
  --screenshot="$OUT" --window-size="$W,$H" --force-device-scale-factor="$SCALE" \
  "file://$WRAP" 2>/dev/null || true
rm -rf "$(dirname "$WRAP")"

[ -f "$OUT" ] || { echo "export failed" >&2; exit 1; }
echo "$OUT"
sips -g pixelWidth -g pixelHeight "$OUT" | tail -2
