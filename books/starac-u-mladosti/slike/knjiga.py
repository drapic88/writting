#!/usr/bin/env python3
"""Složi izvezene ilustracije u knjiga.pdf, redom kojim idu u knjizi.

Svaka dvostranica je jedna stranica PDF-a (50 × 25 cm), uspravne dvostranice 8 i 11 su
uspravne stranice (25 × 50 cm), a naslovnica i stranica 32 su kvadrati (25 × 25 cm).
Najprije pokreni sastavi.py, jer ova skripta koristi njegove PNG-ove (verzije s tekstom).

    python3 books/starac-u-mladosti/slike/knjiga.py
"""
import subprocess
import sys
import tempfile
from pathlib import Path

OVDJE = Path(__file__).resolve().parent
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# (slika, oblik stranice)
REDOSLIJED = [
    ("naslovnica", "kvadrat"),
    ("predlist-karta", "siroka"),
    ("01-rodenje", "siroka"),
    ("02-priprema", "siroka"),
    ("03-suma", "siroka"),
    ("04-kuca-na-rubu-sume", "siroka"),
    ("05-bob-na-dar", "siroka"),
    ("06-noc-u-udolini", "siroka"),
    ("07-bob-do-neba", "siroka"),
    ("08-penjanje", "uspravna"),
    ("09-kod-svetog-petra", "siroka"),
    ("10-nema-boba", "siroka"),
    ("11-uze", "uspravna"),
    ("12-skok-i-motika", "siroka"),
    ("13-doma", "siroka"),
    ("14-propusteno-krstenje", "siroka"),
    ("15-susjed", "siroka"),
    ("32-tvoja-istinita-laz", "kvadrat"),
    ("zalist-rjecnik", "siroka"),
]
VELICINE = {"siroka": ("50cm", "25cm"), "uspravna": ("25cm", "50cm"), "kvadrat": ("25cm", "25cm")}


def main() -> None:
    nedostaje = [ime for ime, _ in REDOSLIJED if not (OVDJE / f"{ime}.png").exists()]
    if nedostaje:
        sys.exit("nema izvezenih slika, prvo pokreni sastavi.py: " + ", ".join(nedostaje))

    with tempfile.TemporaryDirectory() as privremeno:
        tmp = Path(privremeno)
        stranice = []
        for broj, (ime, oblik) in enumerate(REDOSLIJED):
            jpg = tmp / f"{broj:02d}-{ime}.jpg"
            subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "85",
                            "-Z", "3000", str(OVDJE / f"{ime}.png"), "--out", str(jpg)],
                           check=True, capture_output=True)
            stranice.append(f'<div class="{oblik}"><img src="{jpg.name}"></div>')

        css = "".join(
            f"@page {oblik} {{ size: {w} {h}; margin: 0 }} .{oblik} {{ page: {oblik}; width: {w}; height: {h} }}"
            for oblik, (w, h) in VELICINE.items()
        )
        html = tmp / "knjiga.html"
        html.write_text(
            "<!doctype html><meta charset='utf-8'><style>"
            "html,body{margin:0;padding:0} div{break-after:page;overflow:hidden}"
            "img{width:100%;height:100%;object-fit:contain;display:block}"
            f"{css}</style>" + "".join(stranice),
            encoding="utf-8",
        )
        pdf = OVDJE / "knjiga.pdf"
        subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                        f"--print-to-pdf={pdf}", html.as_uri()],
                       check=True, capture_output=True)
    print(f"{pdf.relative_to(OVDJE.parents[2])}: {len(REDOSLIJED)} stranica, "
          f"{pdf.stat().st_size / 1e6:.1f} MB")


if __name__ == "__main__":
    main()
