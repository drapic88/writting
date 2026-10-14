# Upute za AI ilustracije: Starac u mladosti

Ovaj dokument služi za generiranje slika prema planu iz [ilustracije.md](ilustracije.md).
Upute su na engleskom jer većina alata za slike engleski razumije najbolje. Objašnjenja su
na hrvatskom. Upute ne ovise o alatu: opisuju što alat treba moći, a ne zastavice
pojedinog programa.

## Postupak

1. **Najprije reference.** U mapu `reference/` stavi fotografije torbe, tikvice, sinije,
   ognjišta, kuće, nošnje i šume iz kraja. Zatim popuni tablicu „Zamjene“ ispod. Bez toga
   AI izmišlja „starinu“ koja nije iz tvog kraja.
2. **Onda karte likova.** Za svaki lik prvo se napravi karta: isti lik sprijeda, sa
   strane, straga i s nekoliko izraza lica. Generira se više inačica i izabere jedna. Ta
   izabrana karta je od tada **jedini dječak**.
3. **Tek onda dvostranice.** Svaka uputa je spoj tri dijela: **STIL** i **ZABRANE** (uvijek
   isti, doslovno), opis scene, i karta lika priložena kao referentna slika, ako alat to
   podržava. Generiraj nekoliko inačica, izaberi jednu i ispravljaj je uređivanjem
   dijela slike, a ne novim generiranjem. Svako novo generiranje mijenja lice.
4. **Bilježi što je nastalo i kako.** Izabrane slike idu u `slike/` kao `NN-kratki-opis.png`.
   U `slike/LOG.md` upiši alat, datum i točnu uputu od koje je slika nastala.

**Omjeri:** dvostranice su 2 : 1, a dvostranice 8 i 11 su 1 : 2. Naslovnica je 1 : 1.
Ako alat ne nudi 2 : 1, generiraj najširi omjer koji nudi, pa sliku proširi uređivanjem.

**Pravna napomena:** slike koje u cijelosti izradi AI možda nisu zaštićene autorskim
pravom, a neki izdavači postavljaju svoje uvjete za takve slike. To provjeri prije
izdavanja. Ova napomena nije pravni savjet.

## STIL (ide u svaku uputu, doslovno)

```text
Croatian naive painting style: flat, frontal composition without linear perspective,
people, animals and houses shown as on a frieze or a map; bright, clear, saturated colours
with smooth glossy surfaces like oil painted on glass; crisp clean outlines; trees with
every leaf painted individually; decorative stylised skies and clouds; small scenes of
village life in the background; warm, gentle, humorous mood of a children's picture book.
Setting: the Dalmatian hinterland inland from Trogir, Croatia, early 20th century: grey
limestone karst, dry-stone walls enclosing small fields, small stone houses, sheep and
goats. [SUMA] where the story says forest.
```

## ZABRANE (ide u svaku uputu, doslovno)

```text
No text, no letters, no numbers, no signatures, no watermarks. No modern objects, no
electricity, no glass or plastic bottles. No photorealism, no 3D render look, no anime,
no comic-book style. Nothing important in the vertical centre line of the image.
```

Zadnja rečenica čuva hrbat: sredina dvostranice nestaje u uvezu.

## Zamjene

Uglate zagrade u uputama zamijene se ovim opisima. Opisi su moja polazna pretpostavka i
**svi čekaju tvoju potvrdu ili fotografiju**, osim crvenkape i tronošca, koji su potvrđeni
izvorima (vidi [ilustracije.md](ilustracije.md), „Kraj“).

| Oznaka | Polazni opis (engleski, ide u uputu) | Što treba potvrditi |
|---|---|---|
| `[TORBA]` | a woven woollen shoulder bag, red with geometric patterns, decorated with woollen tassels and fringes | boju, uzorak, raspored kita i resa |
| `[TIKVICA]` | a small dried bottle-gourd flask with a wooden stopper, wrapped with red woollen cord ending in a small tassel | kako je „okićena“ |
| `[VELIKA_TIKVICA]` | a larger plain dried bottle-gourd flask for drinking water | — |
| `[NOSNJA_DJECAK]` | white linen shirt, dark brown woollen vest, simple trousers, leather opanci sandals, a small red cap | nose li dječaci crvenkapu, kakve hlače |
| `[NOSNJA_MUSKARAC]` | white linen shirt, dark woollen vest and jacket, red cap, leather opanci | svakodnevna, ne svečana |
| `[NOSNJA_ZENA]` | white linen shirt, dark woollen dress, woven woollen apron, white headscarf | svakodnevna, ne svečana |
| `[KUCA]` | a small one-storey house of grey stone, roof of stone slabs | kamene ploče ili kupe |
| `[SINIJA]` | a low round wooden table, people sitting around it on low three-legged stools | oblik i visina sinije |
| `[OGNJISTE]` | an open hearth on the floor with a wood fire and a cauldron hanging on a chain above it | položaj u kući |
| `[SUMA]` | dense groves of oak trees | koje drveće |

## Karte likova

Za svaki lik radi se jedna karta. Na početak upute idu STIL i ZABRANE, a slijedi:

**Dječak**
```text
Character reference sheet on a plain light background: the same 10-year-old village boy
shown from the front, the side, the back and three-quarter view, plus five head close-ups
showing wonder, fear, relief, sadness and joy. Slim, dark hair, brown eyes, sun-browned
cheeks. Wearing [NOSNJA_DJECAK]. Carrying [TORBA] across his left shoulder and [TIKVICA]
hanging from the bag.
```

**Dječak, otrcan (za dvostranice 11 do 15)**
```text
Character reference sheet, the same boy as in the attached reference: his sleeves and
trouser legs are now short and frayed because the wool was unravelled, his hair is
patchy and plucked, the bag is half unravelled and empty. He is cheerful anyway.
[TIKVICA] tied around his neck.
```

**Koza**
```text
Character reference sheet: one black-and-white goat with a knowing, mischievous look,
shown from the front, the side, looking up, and chewing a large green leaf.
```

**Povjetarac**
```text
Design sheet for a gentle breeze shown as a character without a face: a soft spiral of
green and silver leaves with flowing lines of air, the same shape seen calm, pushing
forward, and catching something falling.
```

**Starac i starica**
```text
Character reference sheet: a kind old man and a kind old woman of the Dalmatian
hinterland, warm wrinkled faces, the man in [NOSNJA_MUSKARAC], the woman in [NOSNJA_ZENA],
front and side views, plus one view of each sitting.
```

**Pastirica, majka i susjed starac** rade se istom uputom kao starac i starica: pastirica s
pastirskim štapom, majka mlađa, a susjed sijed sa štapom za hodanje.

## Dvostranice

Svaka uputa ispod ide **nakon STIL-a i ZABRANA**. Uz nju se prilaže karta dječaka, a
gdje treba i karte drugih likova. Mirna površina za tekst navedena je u svakoj uputi.

**1 — Rođenje** (2 : 1)
```text
Inside [KUCA], daytime, warm light. A joyful family crowds around a mother holding a
newborn baby in swaddling clothes. The boy, the eldest child, leans in and looks at the
baby with wonder. An elderly man sits on a three-legged stool, siblings laugh. On a
wooden peg on the wall hangs [TORBA]. Keep a calm plain wall area in the upper right for
text.
```

**2 — Priprema** (2 : 1)
```text
Evening, lit by the hearth. Hands pack [TORBA] on a wooden table with bread and food
bundles, [VELIKA_TIKVICA], and [TIKVICA], which is being wrapped in a small cloth bundle.
Two elders point through a small window towards a distant forest and hills. The boy
listens closely. Keep a calm area in the lower left for text.
```

**3 — Šuma** (2 : 1)
```text
Dawn turning to day. A dusty village path crosses karst with dry-stone walls to the edge
of [SUMA]. The leaves swirl with visible stylised curls of wind. The boy stands before the
first tree with his right hand raised in greeting, and the breeze, a spiral of leaves,
gently pushes at his back. Keep a calm sky area in the upper left for text.
```

**4 — Kuća na rubu šume** (2 : 1)
```text
Night. A small stone house at the edge of the forest with its door open on a warm orange
interior: [OGNJISTE], and an old man and an old woman eating at [SINIJA]. The boy stands
on the threshold with his right hand raised in greeting. A cat sleeps by the fire. Deep
blue night outside with stars. Keep a calm night-sky area in the upper left for text.
```

**5 — Bob na dar** (2 : 1)
```text
Bright morning outside the old couple's house. The boy carries an armful of firewood. The
old woman hands him a small cloth pouch tied with the same red wool as his bag. The old
man points the way along a path into the hills. Keep a calm sky area in the upper right
for text.
```

**6 — Noć u udolini** (2 : 1)
```text
Dusk in violet tones. A small valley ringed by forest. The boy sleeps with his head on his
bag under the first stars. A single bean seed is falling from his open hand to the ground.
A faint spiral of leaves rests in a treetop. Keep a calm sky area in the upper left for
text.
```

**7 — Bob do neba** (2 : 1)
```text
Dawn mist in the valley. A gigantic bean stalk rises from where the boy slept and climbs
out of the top of the picture into the clouds. A shepherdess with sheep and goats passes
right beside the boy, who sits up rubbing his eyes with both hands. One black-and-white
goat stares up at the stalk with interest. Keep a calm misty area in the lower right for
text.
```

**8 — Penjanje** (1 : 2, uspravno)
```text
Vertical composition. A huge bean stalk climbs up through layers of decorative clouds
like a ladder. The boy, small, climbs it with his bag on his back. Near the top a wooden
door is set into the stalk. A small bird on a leaf looks at the boy in surprise. Keep a
calm cloud area in the lower third for text.
```

**9 — Kod svetog Petra** (2 : 1)
```text
A golden, shining corridor in heaven. Many doors line the walls, each with a blank plaque
above it. People of all ages calmly walk in and out through the doors. Beside some doors
stand small symbols of saints: a lily, a dragon, a gridiron. At the end, a counter window
where only two hands are visible, with a big bundle of keys hanging beside them; the hands
offer a bowl of holy water to the boy, whose right hand is only half raised in greeting.
Keep a calm plain gold area in the upper left for text.
```

Natpise na pločama nad vratima, uključujući „Sveti Petar“, dodaje prijelom.

**10 — Nema boba** (2 : 1)
```text
The boy stands on the threshold of the open door high in the sky, golden light behind
him, holding his head with both hands. In front of him, empty blue air with no bean stalk.
Far, far below, tiny goats chew the stump of the stalk; one black-and-white goat looks up
with a leaf in its mouth. Keep a calm sky area in the upper right for text.
```

**11 — Uže** (1 : 2, uspravno)
```text
Vertical composition at sunset in orange and red. The ragged boy hangs from the end of a
very long rope: the upper part is twisted from the red patterned wool of his bag, the lower
part is twisted grey hair. [TIKVICA] is tied tightly around his neck. Below him, a great
empty gap of air down to the stony ground. Keep a calm area of empty air in the middle
for text.
```

**12 — Skok i motika** (2 : 1)
```text
Left half, at dusk: the ragged boy falls through the sky and the breeze, a spiral of green
and silver leaves, catches him and slows him down. Right half: his foot is stuck in a hole
between two large stones, and a dotted path loops from the stones to his distant house
and back, with a tiny version of the boy walking along it carrying a hoe, while his foot
stays stuck in the stones the whole time. Keep a calm sky area in the upper left for text.
```

**13 — Doma** (2 : 1)
```text
Dusk in a farmyard by [KUCA]. Family members arrive from the fields with hoes and from the
pasture with sheep. In the middle, the ragged boy hands [TIKVICA] to his parents; the
mother holds the baby. A hoe leans by the shed door. Everyone is busy and nobody notices
the boy's frayed clothes or plucked hair. Keep a calm sky area at the top for text.
```

**14 — Propušteno krštenje** (2 : 1)
```text
A quiet morning, cooler colours. Inside the empty house, the boy stands alone at a small
window. Far away through the window his family walks towards a small stone church with a
bell tower. On the table lies [TIKVICA], empty. Keep a calm wall area on the left for text.
```

**15 — Susjed** (2 : 1)
```text
Warm morning at a wooden gate in a dry-stone wall. The boy raises his right hand in
greeting. An old neighbour with white hair leans on a walking stick, listens and smiles.
A small bird sits on the wall listening too. Keep a calm sky area in the upper left for
text.
```

**Stranica 32** (1 : 1)
```text
A simple, calm scene: an unravelled woollen bag and [TIKVICA] lie on a stone bench, with
empty space on the bench beside them, as if waiting for someone to sit down. Large calm
area for text.
```

**Predlist: karta puta** (2 : 1)
```text
A naive bird's-eye map of the journey: the boy's stone house, a dotted path through the
forest with a spiral of wind, the old couple's house at the forest edge, hills and
valleys, a valley with a bean stalk rising to the top edge where a door sits in the
clouds. No labels.
```

**Zalist: rječnik starih stvari** (2 : 1)
```text
A tidy grid of separate objects on a plain light background, each painted alone: [TORBA],
[TIKVICA], [SINIJA], [OGNJISTE], a hoe, a bean pod, a pair of opanci, a small cloth bundle.
Generous space under each object. No labels.
```

**Naslovnica** (1 : 1)
```text
The boy stands at the top of a gigantic bean stalk in front of a wooden door in the clouds,
[TIKVICA] around his neck, looking at the reader. Far below, a black-and-white goat chews
the bottom of the stalk. Keep a calm sky area across the top quarter for the title.
```

## Što ne radi AI nego prijelom

- Sav tekst priče, naslov, natpisi nad vratima i imena u rječniku.
- Okvir s rubom od narodnog veza. Napravi ga prema fotografiji pravog veza iz kraja, a ne
  generiranjem, jer AI ne crta pouzdano točan i simetričan vez.
