#!/usr/bin/env python3
"""Naslikaj ilustracije lokalnim FLUX.2 [klein] 4B modelom (mflux) iz SVG kompozicija.

Za svaku sliku model dobiva gotovu SVG kompoziciju (verziju bez teksta, iz sastavi.py) i
uputu složenu iz ../ai-upute.md: STIL, opis scene sa zamjenama iz tablice „Zamjene“ i
ZABRANE, plus popravke iz proba (jedna neprekinuta slika bez crte uveza, prirodna trava,
krovovi od kamenih ploča, izričit opis likova). Svaka slika dobiva nekoliko inačica s
različitim seedom; na kraju se složi pregledni list flux/pregled.png.

    python3 books/starac-u-mladosti/slike/flux.py --suho                   # samo ispiši upute
    python3 books/starac-u-mladosti/slike/flux.py                          # sve slike, 3 inačice
    python3 books/starac-u-mladosti/slike/flux.py 07-bob-do-neba --inacica 1
    python3 books/starac-u-mladosti/slike/flux.py --karta                  # uz kartu dječaka
    python3 books/starac-u-mladosti/slike/flux.py --povecaj flux/07-bob-do-neba/seed102.png

Gotove inačice se preskaču, pa se prekinuto pokretanje samo nastavi. Treba mflux
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
UPUTE = OVDJE.parent / "ai-upute.md"
FLUX = OVDJE / "flux"
IZVOZ = OVDJE.parents[2] / "scripts" / "hero-export.sh"
OKOLINA = {**os.environ, "PATH": f"{Path.home() / '.local' / 'bin'}:{os.environ['PATH']}"}
MODEL = ["--model", "flux2-klein-4b", "--quantize", "4", "--low-ram", "--steps", "4"]

# ime slike, naslov odlomka u ai-upute.md, širina × visina
SLIKE = [
    ("01-rodenje", "**1 —", (1536, 768)),
    ("02-priprema", "**2 —", (1536, 768)),
    ("03-suma", "**3 —", (1536, 768)),
    ("04-kuca-na-rubu-sume", "**4 —", (1536, 768)),
    ("05-bob-na-dar", "**5 —", (1536, 768)),
    ("06-noc-u-udolini", "**6 —", (1536, 768)),
    ("07-bob-do-neba", "**7 —", (1536, 768)),
    ("08-penjanje", "**8 —", (768, 1536)),
    ("09-kod-svetog-petra", "**9 —", (1536, 768)),
    ("10-nema-boba", "**10 —", (1536, 768)),
    ("11-uze", "**11 —", (768, 1536)),
    ("12-skok-i-motika", "**12 —", (1536, 768)),
    ("13-doma", "**13 —", (1536, 768)),
    ("14-propusteno-krstenje", "**14 —", (1536, 768)),
    ("15-susjed", "**15 —", (1536, 768)),
    ("32-tvoja-istinita-laz", "**Stranica 32**", (1024, 1024)),
    ("predlist-karta", "**Predlist", (1536, 768)),
    ("zalist-rjecnik", "**Zalist", (1536, 768)),
    ("naslovnica", "**Naslovnica**", (1024, 1024)),
]

UVOD = (
    "Repaint the first image as one finished, continuous painting for a children's book. "
    "Keep exactly the same composition, figures, poses, objects and landscape; keep the calm "
    "empty areas calm and empty."
)
LIKOVI = (
    "Characters: the boy (about 10) has a small red cap, white shirt, brown vest with red trim, "
    "dark trousers and leather opanci. Women wear white headscarves covering their hair, long "
    "dark dresses and red striped aprons; old women are wrinkled and wear no caps. Men wear red "
    "caps, white shirts and dark vests; old men have white hair and white moustaches."
)
OTRCAN = "The boy's sleeves and trouser legs are short and frayed and his hair is patchy."
POPRAVCI = (
    "One continuous painting with no fold or seam down the middle. Natural painted grass. "
    "Grey stone-slab roofs, no red tiles."
)
ZABRANE = "No text, no letters, no signature, no watermark. No modern objects. No photorealism, no 3D look."
# otrcan je od dvostranice 11 do 15
OTRCANE = {"11-uze", "12-skok-i-motika", "13-doma", "14-propusteno-krstenje", "15-susjed"}
# rečenice o mjestu teksta iz ai-upute.md: raspored tu određuje kompozicija
O_TEKSTU = re.compile(r"\s*(Keep a calm[^.]*\.|Large calm area for text\.)")
TOKENA = 480  # mflux čita najviše 512 tokena upute


def blok(tekst: str, iza: str) -> str:
    """Prvi ```text blok koji dolazi iza zadanog naslova."""
    pocetak = tekst.index(iza)
    nadeno = re.search(r"```text\n(.*?)\n```", tekst[pocetak:], re.S)
    return " ".join(nadeno.group(1).split())


def zamjene(tekst: str) -> dict:
    return dict(re.findall(r"^\| `(\[[A-Z_]+\])` \| ([^|]+?) \|", tekst, re.M))


def uputa(tekst: str, naslov: str, ime: str) -> str:
    stil = blok(tekst, "## STIL")
    scena = O_TEKSTU.sub("", blok(tekst, naslov))
    for oznaka, opis in zamjene(tekst).items():
        stil, scena = stil.replace(oznaka, opis), scena.replace(oznaka, opis)
    if "[" in scena or "[" in stil:
        sys.exit(f"u uputi za {naslov} je ostala nezamijenjena oznaka")
    likovi = LIKOVI + (" " + OTRCAN if ime in OTRCANE else "")
    return " ".join([UVOD, "Scene: " + scena, likovi, POPRAVCI, stil, ZABRANE])


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


def naslikaj(ime: str, naslov: str, velicina: tuple, seedovi: list, s_kartom: bool, suho: bool) -> None:
    tekst = uputa(UPUTE.read_text(encoding="utf-8"), naslov, ime)
    broj = tokena(tekst) if suho else None
    if broj and broj > TOKENA:
        sys.exit(f"{ime}: uputa ima {broj} tokena, a model čita najviše 512; skrati je")
    slike = [kompozicija(ime, velicina)] + ([karta()] if s_kartom else [])
    (FLUX / ime / "uputa.txt").write_text(tekst + "\n", encoding="utf-8")
    for seed in seedovi:
        izlaz = FLUX / ime / f"seed{seed}.png"
        naredba = ["mflux-generate-flux2-edit", *MODEL, "--seed", str(seed),
                   "--width", str(velicina[0]), "--height", str(velicina[1]),
                   "--image-paths", *map(str, slike),
                   "--prompt-file", str(FLUX / ime / "uputa.txt"), "--output", str(izlaz)]
        if suho:
            print(f"{ime} seed {seed}: {broj or '?'} tokena u uputi")
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
    for ime, _, _ in SLIKE:
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
    suho = "--suho" in argumenti
    s_kartom = "--karta" in argumenti
    imena = [a for a in argumenti if not a.startswith("--")]
    nepoznate = set(imena) - {ime for ime, _, _ in SLIKE}
    if nepoznate:
        sys.exit("nepoznate slike: " + ", ".join(sorted(nepoznate)))
    seedovi = [101 + n for n in range(inacica)]
    for ime, naslov, velicina in SLIKE:
        if not imena or ime in imena:
            naslikaj(ime, naslov, velicina, seedovi, s_kartom, suho)
    if not suho:
        pregled()


if __name__ == "__main__":
    main()
