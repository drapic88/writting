#!/usr/bin/env python3
"""Nauči LoRA-u za FLUX.2 [klein] iz izabranih ilustracija ove knjige (mflux-train).

Skup za učenje su parovi kompozicija → izabrana slika: za svaku sliku iz IZBOR-a ulaz je SVG
kompozicija (flux/<ime>/kompozicija.png), cilj je izabrana inačica (flux/<ime>/seedNNN.png),
a uputa je ista koju je čitao flux.py (flux/<ime>/uputa.txt). Mflux uči uređivački model samo
na nedestiliranom flux2-klein-base-4b, a naučena LoRA se onda koristi s običnim flux2-klein-4b
u flux.py (--lora).

    python3 books/starac-u-mladosti/slike/lora.py --skup                 # složi flux/lora/skup/
    python3 books/starac-u-mladosti/slike/lora.py --proba                # 2 slike, 1 epoha: mjeri memoriju
    python3 books/starac-u-mladosti/slike/lora.py --uci                  # puno učenje
    python3 books/starac-u-mladosti/slike/lora.py --uci --nastavi flux/lora/trening/<checkpoint>.zip

Slike se za učenje smanjuju na površinu REZOLUCIJA² (isto pravilo kao max_resolution u
mfluxu), pa povećavanje izabranih slika prije učenja ništa ne donosi.
"""
import json
import math
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

OVDJE = Path(__file__).resolve().parent
FLUX = OVDJE / "flux"
LORA = FLUX / "lora"
OKOLINA = {**os.environ, "PATH": f"{Path.home() / '.local' / 'bin'}:{os.environ['PATH']}"}

# izabrane inačice (prijedlog iz pregleda 27. 10. 2026., flux/izbor.jpg); 38-rjecnik ostaje SVG
IZBOR = {
    "01-rodenje": 101, "02-priprema": 103, "03-suma": 101, "04-strah-u-sumi": 103,
    "05-kuca-na-rubu-sume": 102, "06-bob-na-dar": 102, "07-noc-u-udolini": 103,
    "08-bob-do-neba": 101, "09-penjanje": 101, "10-kod-svetog-petra": 102, "11-nema-boba": 101,
    "12-uze-i-dlake": 101, "13-na-kraju-uzeta": 102, "14-skok-i-motika": 102, "15-doma": 101,
    "16-propusteno-krstenje": 101, "17-susjed": 102, "36-tvoja-istinita-laz": 103,
    "predlist-karta": 103, "naslovnica": 102,
}
PREGLED = "06-bob-na-dar"  # slika na kojoj trener crta probne slike tijekom učenja
REZOLUCIJA = 640           # površina slike za učenje je REZOLUCIJA²; 640 daje 896×448 za 2:1 (768 je 27. 10. srušio Mac s 16 GB)
MODEL = "flux2-klein-base-4b"
DVOSTRUKIH, JEDNOSTRUKIH = 5, 20  # blokova u klein 4B transformeru
RANG = 16


def velicina(sirina: int, visina: int, rezolucija: int) -> tuple:
    """Ista formula kao TrainingUtil.resolve_dimensions: površina ≤ rezolucija², višekratnik 16."""
    if sirina * visina > rezolucija * rezolucija:
        s = math.sqrt(rezolucija * rezolucija / (sirina * visina))
        sirina, visina = int(sirina * s), int(visina * s)
    return 16 * (sirina // 16), 16 * (visina // 16)


def dimenzije(put: Path) -> tuple:
    izlaz = subprocess.run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(put)],
                           check=True, capture_output=True, text=True).stdout
    brojevi = [int(r.split()[-1]) for r in izlaz.splitlines() if "pixel" in r]
    return brojevi[0], brojevi[1]


def smanji(izvor: Path, cilj: Path, rezolucija: int) -> tuple:
    w, h = velicina(*dimenzije(izvor), rezolucija)
    subprocess.run(["sips", "-s", "format", "png", "-z", str(h), str(w), str(izvor),
                    "--out", str(cilj)], check=True, capture_output=True)
    return w, h


def skup(mapa: Path, imena: list, rezolucija: int) -> None:
    """Složi mapu s parovima <ime>_in.png, <ime>_out.png, <ime>_in.txt i probnom slikom."""
    if mapa.exists():
        shutil.rmtree(mapa)
    mapa.mkdir(parents=True)
    for ime in imena:
        izvor = FLUX / ime
        cilj = izvor / f"seed{IZBOR[ime]}.png"
        for put in (izvor / "kompozicija.png", cilj, izvor / "uputa.txt"):
            if not put.exists():
                sys.exit(f"nema {put}; prvo pokreni flux.py za {ime}")
        w, h = smanji(izvor / "kompozicija.png", mapa / f"{ime}_in.png", rezolucija)
        smanji(cilj, mapa / f"{ime}_out.png", rezolucija)
        shutil.copy(izvor / "uputa.txt", mapa / f"{ime}_in.txt")
        print(f"{ime}: {w}×{h}, cilj seed{IZBOR[ime]}")
    # probna slika: trener iz nje i upute crta sliku svakih nekoliko koraka
    w, h = smanji(FLUX / PREGLED / "kompozicija.png", mapa / "preview.png", rezolucija)
    shutil.copy(FLUX / PREGLED / "uputa.txt", mapa / "preview.txt")
    (mapa / "velicina.txt").write_text(f"{w} {h}\n")


def slojevi() -> list:
    """LoRA na svim linearnim slojevima pažnje i MLP-a u oba dijela transformera."""
    dvostruki = ["attn.to_q", "attn.to_k", "attn.to_v", "attn.to_out", "attn.add_q_proj",
                 "attn.add_k_proj", "attn.add_v_proj", "attn.to_add_out", "ff.linear_in",
                 "ff.linear_out", "ff_context.linear_in", "ff_context.linear_out"]
    jednostruki = ["attn.to_qkv_mlp_proj", "attn.to_out"]
    cilj = [{"module_path": f"transformer_blocks.{{block}}.{m}",
             "blocks": {"start": 0, "end": DVOSTRUKIH}, "rank": RANG} for m in dvostruki]
    cilj += [{"module_path": f"single_transformer_blocks.{{block}}.{m}",
              "blocks": {"start": 0, "end": JEDNOSTRUKIH}, "rank": RANG} for m in jednostruki]
    return cilj


def konfiguracija(mapa: Path, izlaz: Path, epoha: int, rezolucija: int, ucestalost: int) -> Path:
    w, h = map(int, (mapa / "velicina.txt").read_text().split())
    primjera = len(list(mapa.glob("*_out.png")))
    konf = {
        "model": MODEL,
        "data": str(mapa),
        "seed": 1,
        "steps": 20,
        "guidance": 1.0,
        "quantize": 4,
        "max_resolution": rezolucija,
        "low_ram": True,
        "gradient_checkpointing": True,
        "cache_limit_gb": 1,
        "training_loop": {"num_epochs": epoha, "batch_size": 1, "timestep_type": "sigmoid"},
        "optimizer": {"name": "AdamW", "learning_rate": 1e-4, "max_grad_norm": 1.0,
                      "lr_schedule": "cosine", "lr_warmup_steps": 10,
                      "lr_total_steps": epoha * primjera},
        "checkpoint": {"output_path": str(izlaz), "save_frequency": ucestalost},
        "monitoring": {"preview_width": w, "preview_height": h,
                       "plot_frequency": ucestalost, "generate_image_frequency": ucestalost},
        "lora_layers": {"targets": slojevi()},
    }
    put = izlaz.parent / f"{izlaz.name}.json"
    put.parent.mkdir(parents=True, exist_ok=True)
    put.write_text(json.dumps(konf, indent=2) + "\n", encoding="utf-8")
    return put


def uci(konf: Path, nastavi: Path | None, suho: bool) -> None:
    naredba = ["mflux-train", "--low-ram"]
    naredba += ["--resume", str(nastavi)] if nastavi else ["--config", str(konf)]
    if suho:
        naredba.append("--dry-run")
    dnevnik = konf.with_suffix(".log")
    print("pokrećem:", " ".join(naredba), f"(dnevnik {dnevnik.relative_to(OVDJE.parents[2])})")
    start = time.time()
    with dnevnik.open("a", encoding="utf-8") as d:
        rezultat = subprocess.run(naredba, env=OKOLINA, stdout=d, stderr=subprocess.STDOUT, text=True)
    tekst = dnevnik.read_text(encoding="utf-8", errors="replace")
    print(tekst[-2000:])
    print(f"gotovo za {time.time() - start:.0f} s, izlaz {rezultat.returncode}")
    if rezultat.returncode != 0:
        sys.exit("učenje nije uspjelo")


def main() -> None:
    argumenti = sys.argv[1:]
    if not shutil.which("mflux-train", path=OKOLINA["PATH"]):
        sys.exit("nema mfluxa; instaliraj ga: uv tool install --python 3.12 mflux")
    rezolucija = REZOLUCIJA
    if "--rezolucija" in argumenti:
        rezolucija = int(argumenti[argumenti.index("--rezolucija") + 1])
    epoha = 30
    if "--epoha" in argumenti:
        epoha = int(argumenti[argumenti.index("--epoha") + 1])
    nastavi = Path(argumenti[argumenti.index("--nastavi") + 1]).resolve() if "--nastavi" in argumenti else None
    suho = "--suho" in argumenti

    if "--proba" in argumenti:
        mapa, izlaz = LORA / "proba-skup", LORA / "proba"
        skup(mapa, [PREGLED, "13-na-kraju-uzeta"], rezolucija)
        uci(konfiguracija(mapa, izlaz, epoha=1, rezolucija=rezolucija, ucestalost=2), None, suho)
        return
    mapa, izlaz = LORA / "skup", LORA / "trening"
    if "--skup" in argumenti or not mapa.exists():
        skup(mapa, list(IZBOR), rezolucija)
    if "--uci" in argumenti:
        uci(konfiguracija(mapa, izlaz, epoha=epoha, rezolucija=rezolucija, ucestalost=10),
            nastavi, suho)


if __name__ == "__main__":
    main()
