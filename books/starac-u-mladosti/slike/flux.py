#!/usr/bin/env python3
"""Naslikaj ilustracije lokalnim FLUX.2 [klein] 4B modelom (mflux) iz SVG kompozicija.

Za svaku sliku model dobiva gotovu SVG kompoziciju (verziju bez teksta, iz sastavi.py) i
uputu iz ../flux-upute.md: Početak, bilješku za tu sliku i Kraj, sa zamjenama iz tablice
„Zamjene“. Kad bilješka spominje „second image“, uz kompoziciju ide i karta dječaka. Svaka
slika dobiva nekoliko inačica s različitim seedom; na kraju se složi pregledni list
flux/pregled.png.

    python3 books/starac-u-mladosti/slike/flux.py --suho                   # samo ispiši upute
    python3 books/starac-u-mladosti/slike/flux.py                          # sve slike, 3 inačice
    python3 books/starac-u-mladosti/slike/flux.py 08-bob-do-neba --inacica 1
    python3 books/starac-u-mladosti/slike/flux.py --povecaj flux/08-bob-do-neba/seed102.png
    python3 books/starac-u-mladosti/slike/flux.py 06-bob-na-dar --lora flux/lora/trening/<adapter>.safetensors 0.8

Gotove inačice se preskaču, pa se prekinuto pokretanje samo nastavi. S LoRA-om (naučenom
u lora.py) inačice se zovu seedNNN-<adapter>.png, pa stoje uz obične. Treba mflux
(`uv tool install --python 3.12 mflux`) i najprije pokrenut sastavi.py.
"""
import os
import re
import shutil
import subprocess
import sys
import time
from pathlib import Path

OVDJE = Path(__file__).resolve().parent
UPUTE = OVDJE.parent / "flux-upute.md"
FLUX = OVDJE / "flux"
IZVOZ = OVDJE.parents[2] / "scripts" / "hero-export.sh"
OKOLINA = {**os.environ, "PATH": f"{Path.home() / '.local' / 'bin'}:{os.environ['PATH']}"}
MODEL = ["--model", "flux2-klein-4b", "--quantize", "4", "--low-ram", "--steps", "4"]

# ime slike i širina × visina; bilješka za sliku je u odlomku "### <ime>" u flux-upute.md
# (37-tvoj-crtez i zalist-vez su samo vez, a vez radi prijelom, ne model)
SLIKE = [
    ("01-rodenje", (1536, 768)),
    ("02-priprema", (1536, 768)),
    ("03-suma", (1536, 768)),
    ("04-strah-u-sumi", (1536, 768)),
    ("05-kuca-na-rubu-sume", (1536, 768)),
    ("06-bob-na-dar", (1536, 768)),
    ("07-noc-u-udolini", (1536, 768)),
    ("08-bob-do-neba", (1536, 768)),
    ("09-penjanje", (768, 1536)),
    ("10-kod-svetog-petra", (1536, 768)),
    ("11-nema-boba", (1536, 768)),
    ("12-uze-i-dlake", (1536, 768)),
    ("13-na-kraju-uzeta", (768, 1536)),
    ("14-skok-i-motika", (1536, 768)),
    ("15-doma", (1536, 768)),
    ("16-propusteno-krstenje", (1536, 768)),
    ("17-susjed", (1536, 768)),
    ("36-tvoja-istinita-laz", (1024, 1024)),
    ("predlist-karta", (1536, 768)),
    ("38-rjecnik", (1536, 768)),
    ("naslovnica", (1024, 1024)),
]

# bilješka koja spominje drugu sliku dobiva kartu dječaka kao drugu sliku
KARTA = "second image"
TOKENA = 480  # mflux čita najviše 512 tokena upute


def blok(tekst: str, iza: str) -> str:
    """Prvi ```text blok koji dolazi iza zadanog naslova."""
    pocetak = tekst.index(iza)
    nadeno = re.search(r"```text\n(.*?)\n```", tekst[pocetak:], re.S)
    return " ".join(nadeno.group(1).split())


def zamjene(tekst: str) -> dict:
    return dict(re.findall(r"^\| `(\[[A-Z_]+\])` \| ([^|]+?) \|", tekst, re.M))


def uputa(tekst: str, ime: str) -> str:
    sastavljena = " ".join([blok(tekst, "## Početak"), blok(tekst, f"### {ime}\n"),
                            blok(tekst, "## Kraj")])
    for oznaka, opis in zamjene(tekst).items():
        sastavljena = sastavljena.replace(oznaka, opis)
    if "[" in sastavljena:
        sys.exit(f"u uputi za {ime} je ostala nezamijenjena oznaka")
    return sastavljena


def tokena(tekst: str):
    """Broj tokena tokenizatorom samog modela, ako su mflux i model već na disku."""
    mapa = sorted(Path.home().glob(".cache/huggingface/hub/models--black-forest-labs--FLUX.2-klein-4B/snapshots/*/tokenizer"))
    python = Path.home() / ".local/share/uv/tools/mflux/bin/python"
    if not mapa or not python.exists():
        return None
    kod = ("import sys; from transformers import AutoTokenizer; "
           "print(len(AutoTokenizer.from_pretrained(sys.argv[1])(sys.stdin.read())['input_ids']))")
    rezultat = subprocess.run([str(python), "-c", kod, str(mapa[-1])], input=tekst,
                              capture_output=True, text=True)
    return int(rezultat.stdout.strip()) if rezultat.returncode == 0 else None


def kompozicija(ime: str, velicina: tuple) -> Path:
    izvor = OVDJE / f"{ime}-bez-teksta.png"
    if not izvor.exists():
        izvor = OVDJE / f"{ime}.png"
    if not izvor.exists():
        sys.exit(f"nema {izvor.name}; prvo pokreni sastavi.py")
    cilj = FLUX / ime / "kompozicija.png"
    cilj.parent.mkdir(parents=True, exist_ok=True)
    if not cilj.exists() or cilj.stat().st_mtime < izvor.stat().st_mtime:
        w, h = velicina
        subprocess.run(["sips", "-s", "format", "png", "-z", str(h), str(w), str(izvor),
                        "--out", str(cilj)], check=True, capture_output=True)
    return cilj


def karta() -> Path:
    cilj = FLUX / "karta-djecaka-ref.png"
    if not cilj.exists():
        subprocess.run(["sips", "-s", "format", "png", "-Z", "1024", str(OVDJE / "karta-djecaka.png"),
                        "--out", str(cilj)], check=True, capture_output=True)
    return cilj


def naslikaj(ime: str, velicina: tuple, seedovi: list, suho: bool, lora: list) -> None:
    """lora je prazan popis ili [put, mjera]; s LoRA-om se inačica zove seedNNN-<adapter>.png."""
    tekst = uputa(UPUTE.read_text(encoding="utf-8"), ime)
    broj = tokena(tekst) if suho else None
    if broj and broj > TOKENA:
        sys.exit(f"{ime}: uputa ima {broj} tokena, a model čita najviše 512; skrati je")
    slike = [kompozicija(ime, velicina)] + ([karta()] if KARTA in tekst else [])
    (FLUX / ime / "uputa.txt").write_text(tekst + "\n", encoding="utf-8")
    for seed in seedovi:
        izlaz = FLUX / ime / f"seed{seed}{'-' + Path(lora[0]).stem if lora else ''}.png"
        naredba = ["mflux-generate-flux2-edit", *MODEL, *(["--lora", *lora] if lora else []),
                   "--seed", str(seed),
                   "--width", str(velicina[0]), "--height", str(velicina[1]),
                   "--image-paths", *map(str, slike),
                   "--prompt-file", str(FLUX / ime / "uputa.txt"), "--output", str(izlaz)]
        if suho:
            print(f"{ime} seed {seed}: {broj or '?'} tokena u uputi, {len(slike)} slike")
            continue
        if izlaz.exists():
            print(f"{ime} seed {seed}: već postoji, preskačem")
            continue
        start = time.time()
        rezultat = subprocess.run(naredba, env=OKOLINA, capture_output=True, text=True)
        if rezultat.returncode != 0 or not izlaz.exists():
            print(rezultat.stdout[-1500:], rezultat.stderr[-1500:], sep="\n")
            sys.exit(f"{ime} seed {seed}: generiranje nije uspjelo")
        memorija = re.findall(r"Peak MLX memory: ([\d.]+ GB)", rezultat.stdout + rezultat.stderr)
        print(f"{ime} seed {seed}: {time.time() - start:.0f} s, "
              f"najviše {memorija[-1] if memorija else '?'} memorije")


def pregled() -> None:
    """Složi flux/pregled.png: po jedan red za svaku sliku, sve njene inačice."""
    redovi = []
    for ime, _ in SLIKE:
        inacice = sorted((FLUX / ime).glob("seed*.png")) if (FLUX / ime).exists() else []
        if inacice:
            redovi.append((ime, inacice))
    if not redovi:
        return
    v, razmak = 300, 20
    sirina = 40 + max(sum(v * 2 + razmak for _ in inacice) for _, inacice in redovi)
    visina = 20 + len(redovi) * (v + 60)
    dijelovi = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{sirina}" height="{visina}">',
                f'<rect width="{sirina}" height="{visina}" fill="#FAF6EC"/>']
    y = 50
    for ime, inacice in redovi:
        x = 20
        for put in inacice:
            dijelovi.append(f'<text x="{x}" y="{y - 10}" font-family="Georgia" font-size="20" '
                            f'fill="#3A2A20">{ime} · {put.stem}</text>')
            dijelovi.append(f'<image href="{put.as_uri()}" x="{x}" y="{y}" width="{v * 2}" '
                            f'height="{v}" preserveAspectRatio="xMidYMid meet"/>')
            x += v * 2 + razmak
        y += v + 60
    dijelovi.append("</svg>")
    svg = FLUX / "pregled.svg"
    svg.write_text("\n".join(dijelovi), encoding="utf-8")
    subprocess.run([str(IZVOZ), str(svg), "1"], check=True, capture_output=True)
    print(f"pregled: {(FLUX / 'pregled.png').relative_to(OVDJE.parents[2])}")


def povecaj(put: Path) -> None:
    izlaz = put.with_name(put.stem + "-x2.png")
    start = time.time()
    subprocess.run(["mflux-upscale-seedvr2", "--model", "seedvr2-3b", "--low-ram",
                    "--resolution", "2x", "--seed", "1", "--image-path", str(put),
                    "--output", str(izlaz)], env=OKOLINA, check=True, capture_output=True)
    print(f"{izlaz.relative_to(OVDJE.parents[2])}: {time.time() - start:.0f} s")


def main() -> None:
    argumenti = sys.argv[1:]
    if not shutil.which("mflux-generate-flux2-edit", path=OKOLINA["PATH"]):
        sys.exit("nema mfluxa; instaliraj ga: uv tool install --python 3.12 mflux")
    if "--povecaj" in argumenti:
        povecaj(Path(argumenti[argumenti.index("--povecaj") + 1]).resolve())
        return
    inacica = 3
    if "--inacica" in argumenti:
        i = argumenti.index("--inacica")
        inacica = int(argumenti[i + 1])
        del argumenti[i: i + 2]
    lora = []
    if "--lora" in argumenti:
        i = argumenti.index("--lora")
        lora = [str(Path(argumenti[i + 1]).resolve())]
        if i + 2 < len(argumenti) and re.fullmatch(r"[\d.]+", argumenti[i + 2]):
            lora.append(argumenti[i + 2])
        del argumenti[i: i + 1 + len(lora)]
        if not Path(lora[0]).exists():
            sys.exit(f"nema LoRA-e {lora[0]}")
    suho = "--suho" in argumenti
    imena = [a for a in argumenti if not a.startswith("--")]
    nepoznate = set(imena) - {ime for ime, _ in SLIKE}
    if nepoznate:
        sys.exit("nepoznate slike: " + ", ".join(sorted(nepoznate)))
    seedovi = [101 + n for n in range(inacica)]
    for ime, velicina in SLIKE:
        if not imena or ime in imena:
            naslikaj(ime, velicina, seedovi, suho, lora)
    if not suho:
        pregled()


if __name__ == "__main__":
    main()
