# Upute za SVG ilustracije: Starac u mladosti

Prema ovim uputama Claude crta cijelu knjigu kao vektorske slike (SVG) i izvozi ih u PNG.
Plan je u [ilustracije.md](ilustracije.md), a tekst u [prica.md](prica.md). Upute za vanjski
alat za slike su u [ai-upute.md](ai-upute.md). Kad se taj alat spoji, SVG komplet služi kao
dogovorena kompozicija za svaku stranicu: gdje je tko, što radi i gdje stoji tekst.

## Datoteke

```
slike/
├── izvor/likovi.svg        knjižnica: svi likovi, poze, životinje, predmeti, stil
├── izvor/NN-naziv.svg      jedna datoteka po slici, koristi knjižnicu
├── sastavi.py              umeće knjižnicu i tekst, izvozi PNG
├── NN-naziv.svg            sastavljeno, samostalno (ne uređuje se ručno)
├── NN-naziv.png            slika s tekstom, pregled stranice
├── NN-naziv-bez-teksta.png slika bez teksta i natpisa, za prijelom
└── .gitignore              sve generirano ostaje izvan gita
```

Commitaju se samo `izvor/` i `sastavi.py`. Izvezene slike imaju oko 11 MB svaka (zrnata
tekstura se loše sažima), pa bi 40 slika bilo preko 350 MB. Izvoz svih slika traje oko
minutu i pol.

**Karte likova** su `izvor/pregled-likova.svg`, `izvor/pregled-predmeta.svg` i
`izvor/karta-djecaka.svg`. Izvoze se kao i ostale slike i služe za provjeru knjižnice.

Pokretanje, za sve slike ili samo za jednu:

```bash
python3 books/starac-u-mladosti/slike/sastavi.py
```

```bash
python3 books/starac-u-mladosti/slike/sastavi.py 07-bob-do-neba
```

**Pravilo:** lik se nikad ne crta u slici. Crta se jednom u `likovi.svg`, a slika ga samo
poziva s `<use href="#...">`. Promjena torbe, kape ili lica u knjižnici mijenja ih u cijeloj
knjizi odjednom. Ako slici treba nova poza, dodaje se u knjižnicu.

## Platna

| Što | Platno | Napomena |
|---|---|---|
| Dvostranice 1–7, 9, 10, 12–15, predlist, zalist | 2000 × 1000 | omjer 2 : 1, kvadratne stranice |
| Dvostranice 8 i 11 | 1000 × 2000 | knjiga se okreće uspravno |
| Naslovnica, stranica 32 | 1000 × 1000 | jedna stranica |

- **Hrbat** je pojas od 960 do 1040 po širini (kod uspravnih po visini). U njemu nema lica,
  ruku ni tikvice.
- **Rub:** ništa važno bliže od 40 jedinica rubu, jer se pri tisku obrezuje.
- **Izvoz:** za pregled 2×, za tisak 3×. Uz pretpostavku stranice 25 × 25 cm to je
  dvostranica 50 × 25 cm, pa izvoz 3× (6000 × 3000) daje oko 300 dpi. SVG je vektor, pa
  se može izvesti i veće.

## Stil: naiva u vektoru

1. **Obris** je tamnosmeđ (`#3A2A20`), debljine 2 do 2,5. Nikad crn.
2. **Plošna perspektiva.** Nema nedogleda. Daljnje stvari su više na slici i manje, kuće
   se gledaju sprijeda, a polja kao na karti.
3. **Puno sitnog života.** Svaka slika ima barem tri sitna prizora u pozadini, na primjer
   dim iz komina, magarac, žena na gustirni, ptice ili sušenje rublja. Ti prizori ne smiju
   proturječiti tekstu.
4. **Ukrasno nebo:** pretapanje boja i stilizirani oblaci. Noću zvijezde kao sitni
   četverokraki znakovi.
5. **Prvi plan:** cvijeće, trava i kamenje.
6. **Tekstura.** Preko cijele slike ide vrlo slab zrnati sloj (`#tekstura`), da površina
   ne bude plastična.
7. **Veličina likova.** Dječak u prvom planu dvostranice stoji visok oko 260 do 300
   jedinica. Lik ne smije biti sitan kad je on radnja.

**Paleta** (boje su u knjižnici kao CSS varijable i klase):

| Namjena | Boja |
|---|---|
| obris | `#3A2A20` |
| lan, bijela odjeća | `#FBF7EE` |
| vuna crvena (torba, pas, kapa) | `#A8292A`, `#C0312B` |
| tamnoplava vuna | `#2E3E6E`, `#2F3550` |
| smeđi prsluk | `#5A3B26` |
| okra (tikvica) | `#D9A441` |
| koža | `#F1C7A0`, starci `#EBBE98` |
| krš i kamen | `#B7B2A8`, `#97A58E` |
| zelenilo | `#3A6636`, `#86AE70`, `#A3AE72` |

## Likovi i poze u knjižnici

Boje odjeće mijenjaju se CSS varijablama, pa jedan lik može biti više ljudi. Primjer:
`<use href="#muskarac-stoji" style="--prsluk:#2E3E6E">`.

- **Dječak:** `djecak-tijelo-stoji`, `djecak-tijelo-sretan`, `djecak-tijelo-cudi` (bez
  torbe), `djecak-stoji`, `djecak-pozdrav`, `djecak-pozdrav-pola`, `djecak-hoda`, `djecak-slusa`,
  `djecak-sjedi-trlja`, `djecak-spava`, `djecak-nosi-drva`, `djecak-penje`,
  `djecak-drzi-glavu`, `djecak-pada`, `djecak-zaglavljen`, `djecak-predaje`,
  `djecak-prozor`, `djecak-motika`. Neke od ovih postoje samo u otrcanoj inačici. Otrcane poze (od dvostranice 11) imaju
  nastavak `-otrcan`: `djecak-visi-otrcan`, `djecak-pada-otrcan`,
  `djecak-zaglavljen-otrcan`, `djecak-motika-otrcan`, `djecak-predaje-otrcan`,
  `djecak-prozor-otrcan`, `djecak-pozdrav-otrcan`.
- **Odrasli:** `muskarac-stoji`, `muskarac-pokazuje`, `muskarac-pokazuje-gore`, `muskarac-sjedi`, `zena-stoji`,
  `zena-pruza`, `zena-sjedi`, `zena-dijete` (majka s bebom), `pastirica`, `starac-stap`
  (susjed). Starost se bira varijablama (`--kosa`, `--brci`).
- **Djeca:** `dijete-djevojcica`, `dijete-djecak`.
- **Životinje:** `ovca`, `ovca-zvonce`, `koza-ide` i `koza-pase` (boja preko `fill`),
  `koza-cb-gleda-gore`, `koza-cb-zvace`, `macka-spava`, `ptica`, `ptica-cudi`,
  `ptica-leti`, `sova`, `kokos`, `magarac`.
- **Povjetarac:** `povjetarac`, uvijek istog oblika: spirala zelenog i srebrnog lišća.
- **Predmeti:** `torba`, `torba-rasparana`, `tikvica`, `tikvica-oko-vrata`,
  `velika-tikvica`, `kruh`, `smotuljak`, `kesica`, `drva`, `motika`, `sinija`, `tronozac`,
  `ognjiste`, `stol`, `klupa`, `kolijevka`, `skrinja`, `bakrenjak`, `opanci`, `bunar`,
  `kuca`, `supa`, `crkva`, `dim`, `suhozid`, `vrata-raj`, `kljucevi-ruke`, znakovi svetaca
  (`znak-ljiljan`, `znak-resetka`, `znak-zmaj`, `znak-kugle`).
- **Priroda:** `hrast`, `grm`, `kamen`, `oblak`, `oblak-zlatni`, `zvijezda`, `mjesec`,
  `vjetar-kovrca`, cvijeće (`cvijet-bijeli`, `cvijet-zuti`, `cvijet-crveni`), `bob-list`,
  `bob-cvijet`, `bob-mahuna`, `zrno`.
- **Nebo i svjetlo:** `g-nebo-zora`, `g-nebo-dan`, `g-nebo-vecer`, `g-nebo-zalazak`,
  `g-nebo-noc`, `g-nebo-zlato`, `g-sjaj`, `g-sjaj-vatra`, filtri `magla` i `tekstura`.

## Tekst

Tekst se nikad ne upisuje ručno u sliku. Slika ima samo pravokutnik koji kaže gdje ide
okvir:

```xml
<rect id="okvir-teksta" data-dvostranica="7" x="1140" y="40" width="780" height="420"/>
```

`sastavi.py` uzima tekst te dvostranice iz `prica.md`, prelama ga prema stvarnim
širinama slova fonta Georgia, smanjuje slova ako treba (od 26 do 21) i crta okvir s rubom
od veza. Ako tekst ne stane, skripta javi grešku i slika se ne izvozi. Odlomci, replike i
refren „Što ću sad?“ ostaju u svojim recima, a formula *Čiča miča* ide kurzivom.

Okvir nikad ne prelazi hrbat. Kod uspravnih dvostranica tekst je i dalje vodoravan za
čitatelja koji je okrenuo knjigu.

Okvir prima i dva neobavezna atributa: `data-najveca="40"` podiže najveću veličinu slova,
a `data-sredina="1"` centrira tekst. Oba koristi stranica 32.

**Natpisi u slici** (natpisi nad vratima u dvostranici 9, naslov na naslovnici, imena u
rječniku) pišu se kao `<text data-natpis="1" ...>`. Ulaze u sliku s tekstom, a skripta ih
uklanja iz verzije bez teksta, jer ih u knjizi slaže prijelom.

## Kontinuitet (provjeriti na svakoj slici)

- **Tikvica** se vidi na svakoj dvostranici od 2 do 13.
- **Torba** je cijela do 10. U 11 postaje uže, a od 12 je `torba-rasparana`.
- **Dječak** je od 11 do 15 otrcan i počupan.
- **Pozdrav** je uvijek ista gesta, podignuta ruka okrenuta prema onome koga pozdravlja.
  Lik se smije zrcaliti (`scale(-1,1)`) da ruka gleda na pravu stranu. U dvostranici 7 ruke
  su na očima.
- **Povjetarac** je u 3 i 12 isti, a u 6 i 8 vidi se samo kriomice.
- **Crno-bijela koza** pojavljuje se u 7 i 10, a **ptica** u 8 i 15.
- **Nebo** ima samo jednu zlatnu dvostranicu, onu iz 9.

## Provjera prije nego je slika gotova

- [ ] `sastavi.py` prošao bez greške, a tekst je stao u okvir.
- [ ] PNG je otvoren i pogledan, i u cijelosti i uvećan na likove.
- [ ] U hrbatu nema lica, ruke ni tikvice.
- [ ] U slici nema slova osim okvira s tekstom i natpisa označenih s `data-natpis`.
- [ ] Sve stavke iz „Kontinuiteta“ koje se tiču te dvostranice su ispunjene.
- [ ] Nijedan detalj ne proturječi tekstu.

## Dvostranice

Sadržaj svake slike opisan je u [ilustracije.md](ilustracije.md), u tablici „Dvostranice“.
Ovdje su samo odluke koje trebaju za crtanje.

| # | Platno | Okvir teksta | Dječak |
|---|---|---|---|
| 1 | 2000×1000 | gore desno | `djecak-stoji`, nagnut prema bebi |
| 2 | 2000×1000 | dolje lijevo | `djecak-slusa` |
| 3 | 2000×1000 | gore lijevo | `djecak-pozdrav` |
| 4 | 2000×1000 | gore lijevo | `djecak-pozdrav` na pragu |
| 5 | 2000×1000 | gore desno | `djecak-nosi-drva` |
| 6 | 2000×1000 | gore lijevo | `djecak-spava` |
| 7 | 2000×1000 | gore desno | `djecak-sjedi-trlja` |
| 8 | 1000×2000 | dolje | `djecak-penje` |
| 9 | 2000×1000 | gore lijevo | `djecak-pozdrav` (ruka napola) |
| 10 | 2000×1000 | gore desno | `djecak-drzi-glavu` |
| 11 | 1000×2000 | sredina | `djecak-visi-otrcan` |
| 12 | 2000×1000 | gore desno | `djecak-pada-otrcan`, `djecak-zaglavljen-otrcan`, `djecak-motika` |
| 13 | 2000×1000 | gore | `djecak-predaje-otrcan` |
| 14 | 2000×1000 | lijevo | `djecak-prozor-otrcan` |
| 15 | 2000×1000 | gore lijevo | `djecak-pozdrav-otrcan` |
| 32 | 1000×1000 | gore | bez dječaka |
| predlist, zalist, naslovnica | — | bez teksta (naslov dodaje prijelom) | — |
