#!/usr/bin/env python3
"""Sastavi slike za "Starac u mladosti" i izvezi ih u PNG.

Za svaku sliku u izvor/ skripta:
  1. umeće zajedničku knjižnicu likova (izvor/likovi.svg) na mjesto <!-- likovi -->,
  2. zamjenjuje <rect id="okvir-teksta" data-dvostranica="N" .../> okvirom s rubom od
     veza i tekstom te dvostranice iz ../prica.md, prelomljenim prema širinama slova
     fonta Georgia,
  3. piše NN-naziv.svg i NN-naziv-bez-teksta.svg (bez okvira i bez natpisa
     označenih s <text data-natpis ...>) i izvozi oba u PNG
     preko scripts/hero-export.sh.

    python3 books/starac-u-mladosti/slike/sastavi.py                 # sve slike, 2x
    python3 books/starac-u-mladosti/slike/sastavi.py 07-bob-do-neba  # jedna slika
    python3 books/starac-u-mladosti/slike/sastavi.py --skala 3       # za tisak
"""
import html
import re
import struct
import subprocess
import sys
from pathlib import Path

OVDJE = Path(__file__).resolve().parent
IZVOR = OVDJE / "izvor"
PRICA = OVDJE.parent / "prica.md"
REPO = OVDJE.parents[2]
IZVOZ = REPO / "scripts" / "hero-export.sh"
FONTOVI = Path("/System/Library/Fonts/Supplemental")
OZNAKA = "<!-- likovi -->"

RUB = 22          # širina ruba od veza
UNUTRA_X = 34     # razmak teksta od ruba, vodoravno
UNUTRA_Y = 26     # razmak teksta od ruba, okomito
VELICINE = [26, 25.5, 25, 24.5, 24, 23.5, 23, 22.5, 22, 21.5, 21]


# ---------- širine slova iz TTF-a (cmap + hmtx), bez vanjskih paketa ----------

class Font:
    def __init__(self, put: Path):
        p = put.read_bytes()
        broj = struct.unpack(">H", p[4:6])[0]
        tablice = {}
        for i in range(broj):
            oznaka, _, pomak, duljina = struct.unpack(">4sIII", p[12 + 16 * i: 28 + 16 * i])
            tablice[oznaka.decode("latin-1")] = (pomak, duljina)
        glava = tablice["head"][0]
        self.em = struct.unpack(">H", p[glava + 18: glava + 20])[0]
        hhea = tablice["hhea"][0]
        broj_mjera = struct.unpack(">H", p[hhea + 34: hhea + 36])[0]
        hmtx = tablice["hmtx"][0]
        self.sirine = [struct.unpack(">H", p[hmtx + 4 * i: hmtx + 4 * i + 2])[0]
                       for i in range(broj_mjera)]
        self.znakovi = self._cmap(p, tablice["cmap"][0])

    @staticmethod
    def _cmap(p: bytes, cmap: int) -> dict:
        broj = struct.unpack(">H", p[cmap + 2: cmap + 4])[0]
        for i in range(broj):
            platforma, kodiranje, pomak = struct.unpack(">HHI", p[cmap + 4 + 8 * i: cmap + 12 + 8 * i])
            if platforma == 3 and kodiranje == 1:
                t = cmap + pomak
                if struct.unpack(">H", p[t: t + 2])[0] != 4:
                    continue
                n = struct.unpack(">H", p[t + 6: t + 8])[0] // 2
                kraj = struct.unpack(f">{n}H", p[t + 14: t + 14 + 2 * n])
                poc = struct.unpack(f">{n}H", p[t + 16 + 2 * n: t + 16 + 4 * n])
                delta = struct.unpack(f">{n}h", p[t + 16 + 4 * n: t + 16 + 6 * n])
                rasp_pomak = t + 16 + 6 * n
                rasp = struct.unpack(f">{n}H", p[rasp_pomak: rasp_pomak + 2 * n])
                mapa = {}
                for s in range(n):
                    for kod in range(poc[s], kraj[s] + 1):
                        if kod == 0xFFFF:
                            continue
                        if rasp[s] == 0:
                            glif = (kod + delta[s]) & 0xFFFF
                        else:
                            adr = rasp_pomak + 2 * s + rasp[s] + 2 * (kod - poc[s])
                            glif = struct.unpack(">H", p[adr: adr + 2])[0]
                            if glif:
                                glif = (glif + delta[s]) & 0xFFFF
                        mapa[kod] = glif
                return mapa
        raise ValueError("font nema cmap formata 4")

    def sirina(self, tekst: str, velicina: float) -> float:
        zadnja = self.sirine[-1]
        ukupno = 0
        for z in tekst:
            g = self.znakovi.get(ord(z), 0)
            ukupno += self.sirine[g] if g < len(self.sirine) else zadnja
        return ukupno * velicina / self.em * 1.02  # mala rezerva za kerning


OBICNI = Font(FONTOVI / "Georgia.ttf")
KURZIV = Font(FONTOVI / "Georgia Italic.ttf")


# ---------- tekst iz prica.md ----------

def tekstovi() -> dict:
    sadrzaj = PRICA.read_text(encoding="utf-8")
    dijelovi = re.split(r"<!-- (.+?) -->", sadrzaj)
    po_broju = {}
    for i in range(1, len(dijelovi), 2):
        oznaka = dijelovi[i].strip()
        kljuc = "32" if oznaka == "zadnja stranica" else oznaka
        odlomci = [o.strip() for o in dijelovi[i + 1].strip().split("\n\n") if o.strip()]
        po_broju[kljuc] = odlomci
    return po_broju


def prelomi(odlomak: str, font: Font, velicina: float, sirina: float) -> list:
    redci, red = [], ""
    for rijec in odlomak.split():
        pokusaj = f"{red} {rijec}".strip()
        if red and font.sirina(pokusaj, velicina) > sirina:
            redci.append(red)
            red = rijec
        else:
            red = pokusaj
    if red:
        redci.append(red)
    return redci


def okvir(atributi: dict, odlomci: list, ime: str) -> str:
    x, y = float(atributi["x"]), float(atributi["y"])
    w, h = float(atributi["width"]), float(atributi["height"])
    sirina = w - 2 * RUB - 2 * UNUTRA_X
    visina = h - 2 * RUB - 2 * UNUTRA_Y
    najveca = float(atributi.get("data-najveca", VELICINE[0]))
    sredina = atributi.get("data-sredina") == "1"
    velicine = [najveca - 0.5 * i for i in range(int((najveca - VELICINE[-1]) * 2) + 1)]
    for velicina in velicine:
        razmak, praznina = velicina * 1.36, velicina * 0.55
        slozeno = []
        for odlomak in odlomci:
            kurziv = odlomak.startswith("*") and odlomak.endswith("*")
            cist = odlomak.strip("*")
            font = KURZIV if kurziv else OBICNI
            slozeno.append((kurziv, prelomi(cist, font, velicina, sirina)))
        redaka = sum(len(r) for _, r in slozeno)
        potrebno = velicina + (redaka - 1) * razmak + (len(slozeno) - 1) * praznina
        if potrebno <= visina:
            break
    else:
        sys.exit(f"{ime}: tekst ne stane u okvir {w:.0f}×{h:.0f}; povećaj okvir")

    vrh = y + RUB + UNUTRA_Y + (visina - potrebno) / 2 + velicina * 0.8
    lijevo = x + w / 2 if sredina else x + RUB + UNUTRA_X
    uzorak = f"vez-{ime}"
    dijelovi = [
        f'<g id="tekst">',
        f'<pattern id="{uzorak}" href="#vez" x="{x}" y="{y}"/>',
        f'<path d="M{x},{y} h{w} v{h} h{-w} Z M{x + RUB},{y + RUB} v{h - 2 * RUB} '
        f'h{w - 2 * RUB} v{-(h - 2 * RUB)} Z" fill="url(#{uzorak})" fill-rule="evenodd"/>',
        f'<rect x="{x + RUB}" y="{y + RUB}" width="{w - 2 * RUB}" height="{h - 2 * RUB}" '
        f'fill="#FBF6EA" opacity=".96"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="none" stroke="#7E2020" stroke-width="2.5"/>',
        f'<rect x="{x + RUB}" y="{y + RUB}" width="{w - 2 * RUB}" height="{h - 2 * RUB}" '
        f'fill="none" stroke="#7E2020" stroke-width="1.5"/>',
        f'<text font-family="Georgia, \'Times New Roman\', serif" font-size="{velicina}" fill="#2B2118"'
        + (' text-anchor="middle">' if sredina else '>'),
    ]
    yy = vrh
    for broj, (kurziv, redci) in enumerate(slozeno):
        if broj:
            yy += praznina
        stil = ' font-style="italic"' if kurziv else ""
        for red in redci:
            dijelovi.append(f'<tspan x="{lijevo:.1f}" y="{yy:.1f}"{stil}>{html.escape(red, quote=False)}</tspan>')
            yy += razmak
    dijelovi += ["</text>", "</g>"]
    return "\n".join(dijelovi)


# ---------- sastavljanje ----------

def knjiznica() -> str:
    tekst = (IZVOR / "likovi.svg").read_text(encoding="utf-8")
    nadeno = re.search(r'<defs id="likovi">.*?</defs>', tekst, re.S)
    if not nadeno:
        sys.exit('u izvor/likovi.svg nema <defs id="likovi">')
    return nadeno.group(0)


def izvezi(svg: Path, skala: str) -> None:
    rezultat = subprocess.run([str(IZVOZ), str(svg), skala], capture_output=True, text=True)
    if rezultat.returncode != 0:
        sys.exit(f"izvoz nije uspio za {svg.name}: {rezultat.stderr.strip()}")
    print(rezultat.stdout.strip().replace(str(OVDJE) + "/", ""))


def sastavi(ime: str, defs: str, svi_tekstovi: dict, skala: str) -> None:
    izvor = (IZVOR / f"{ime}.svg").read_text(encoding="utf-8")
    if OZNAKA not in izvor:
        sys.exit(f"{ime}.svg nema oznaku {OZNAKA}")
    izvor = izvor.replace(OZNAKA, defs, 1)

    s_tekstom, bez_teksta = izvor, izvor
    nadeno = re.search(r'<rect id="okvir-teksta"([^>]*)/>', izvor)
    if not nadeno and "data-natpis" in izvor:
        bez_teksta = re.sub(r'<text data-natpis[^>]*>.*?</text>', "", izvor, flags=re.S)
        (OVDJE / f"{ime}-bez-teksta.svg").write_text(bez_teksta, encoding="utf-8")
        izvezi(OVDJE / f"{ime}-bez-teksta.svg", skala)
    if nadeno:
        atributi = dict(re.findall(r'([\w-]+)="([^"]*)"', nadeno.group(1)))
        broj = atributi["data-dvostranica"]
        if broj not in svi_tekstovi:
            sys.exit(f"{ime}: u prica.md nema dvostranice {broj}")
        s_tekstom = izvor.replace(nadeno.group(0), okvir(atributi, svi_tekstovi[broj], ime))
        bez_teksta = re.sub(r'<text data-natpis[^>]*>.*?</text>', "", izvor.replace(nadeno.group(0), ""), flags=re.S)
        (OVDJE / f"{ime}-bez-teksta.svg").write_text(bez_teksta, encoding="utf-8")
        izvezi(OVDJE / f"{ime}-bez-teksta.svg", skala)

    (OVDJE / f"{ime}.svg").write_text(s_tekstom, encoding="utf-8")
    izvezi(OVDJE / f"{ime}.svg", skala)


def main() -> None:
    argumenti = sys.argv[1:]
    skala = "2"
    if "--skala" in argumenti:
        i = argumenti.index("--skala")
        skala = argumenti[i + 1]
        del argumenti[i: i + 2]
    defs = knjiznica()
    svi_tekstovi = tekstovi()
    imena = argumenti or sorted(p.stem for p in IZVOR.glob("*.svg") if p.stem != "likovi")
    for ime in imena:
        sastavi(ime, defs, svi_tekstovi, skala)


if __name__ == "__main__":
    main()
