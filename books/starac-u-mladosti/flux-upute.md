# FLUX upute: Starac u mladosti

Ove upute čita [slike/flux.py](slike/flux.py). Lokalni model (FLUX.2 [klein] 4B preko
mfluxa) ne crta od nule. On preslikava gotovu SVG kompoziciju u naivnu sliku, pa uputa ne
prepričava priču. Kaže samo tko je tko na slici, što se mora zadržati i gdje ide tekst.
Upute za crtanje od nule, za vanjski alat, su u [ai-upute.md](ai-upute.md).

## Kako se slaže uputa

Svaka uputa ima tri dijela: **Početak**, bilješku za tu sliku i **Kraj**. Oznake u uglatim
zagradama zamjenjuju se tekstom iz tablice „Zamjene“. Ako bilješka spominje „second image“,
uz kompoziciju ide i [karta dječaka](slike/karta-djecaka.png) kao druga slika. Uputa smije
imati najviše 480 tokena, jer model čita najviše 512. To provjerava
`python3 books/starac-u-mladosti/slike/flux.py --suho`.

Pravila za bilješke, prema probama od 26. 10. 2026.:

- **Opisuj samo ono što je u kompoziciji.** Uputa koja je nabrajala sve likove iz knjige
  dodala je starce u dvostranicu 3, gdje ih nema.
- **Ne prepričavaj priču i ne opisuj raspoloženje bez mjesta.** Rečenica „pairs of eyes
  seem to glint in the dark leaves“ rasula je oči po svim deblima.
- **Dječaka uvijek veži uz kartu**, rečenicom „is the boy from the second image“. Bez karte
  mu se lice i nošnja mijenjaju od slike do slike.
- **Mjesto za tekst navedi kao „calm and empty“**, inače ga model popuni.

## Početak

```text
Repaint the first image as a finished children's picture book illustration in Croatian
naive art style: bright clear saturated colours, smooth glossy surfaces like oil painted on
glass, crisp outlines, trees with every leaf painted, decorative clouds, rich small details
of village life. Keep exactly the same composition, the same figures in the same places and
poses.
```

## Kraj

```text
No text, no letters, no signature.
```

## Zamjene

| Oznaka | Tekst |
|---|---|
| `[DJECAK]` | the boy from the second image: same red cap, white shirt, brown vest with red trim and gold buttons, dark trousers |
| `[OTRCAN]` | the boy from the second image, now ragged: same red cap, brown vest and dark trousers, but his vest is torn and his shirt sleeves and trouser legs are short and frayed |
| `[TORBA]` | the red woven bag with tassels |
| `[TIKVICA]` | the small decorated bottle gourd |
| `[ZENA]` | a white headscarf covering all her hair, a long dark dress and a red striped woven apron |
| `[STARICA]` | an OLD WOMAN with a wrinkled kind face, a white headscarf covering all her hair, a long dark blue dress and a red striped woven apron; she has no cap |
| `[STARAC]` | an old man with white hair and a white moustache, a red cap, a white shirt and a dark vest |
| `[KROVOVI]` | All house roofs are grey stone slabs, no red tiles. |

## Slike

### 01-rodenje

```text
Keep the same stone room with dark wooden beams, the shelf with pots, the wooden cross, the
small window, the open door with hens outside, the wooden cradle, the hearth fire with the
pot hanging on a chain and the sleeping grey cat. The taller boy in the middle, looking at
the baby in wonder, is [DJECAK]. The mother holding the newborn baby wears [ZENA]. The
grandfather sitting on the three-legged stool is [STARAC]. [TORBA] hangs on a peg on the
wall. Keep the upper right wall calm and empty.
```

### 02-priprema

```text
Evening in the same stone room, lit warmly by the hearth fire on the right. Keep the big
window showing a dusk landscape with a dotted path over the hills, the wooden chest, the
table with bread, two bottle gourds, a small bundle and [TORBA], the hearth with the hanging
pot and the cat. The boy in the middle, listening with his mouth open, is [DJECAK]. The
grandfather pointing up towards the window is [STARAC]. The two women wear [ZENA]. Keep the
upper right wall calm and empty.
```

### 03-suma

```text
Keep the same small stone village with the church and the villagers on the left, the well,
the dusty path, the dry-stone walls and the oak grove on the right. The frightened boy
standing on the path with stiff trembling arms and a worried face is [DJECAK], with [TORBA]
and [TIKVICA]. The sun rises behind the oak grove, the grove is dark in its own shade, and
long dark shadows shaped like fingers lie across the path at the boy's feet. Keep the white
wind curls in the treetops. The oak grove is a row of medium oak trees of equal height, as
small as in the first image, with open sky and the sun above them. [KROVOVI] Keep the upper
left sky calm and empty.
```

### 04-strah-u-sumi

```text
Keep the same row of oak trees with the path winding to the right, and the open sky above
the treetops with one small cloud. The forest on the left lies in soft blue shade that
lightens gradually towards the right, with no sharp edge. Inside three treetops on the left,
darker leaves form hidden patterns, exactly as in the first image. The boy on the left with
his hand on his chin, thinking, with small thought bubbles, is [DJECAK]. On the right, soft
sunbeams fall between the trees and a swirl of leaves with white wind curls passes through
the treetops. The same boy, smaller, walks calmly along the path on the right with [TORBA].
Keep the upper right sky calm and empty.
```

### 05-kuca-na-rubu-sume

```text
Night at the edge of an oak forest under a starry sky with a crescent moon. Keep the same
small stone house shown open like a doll's house, with its wooden door open. Inside, the
hearth fire with the pot hanging on a chain lights the room warmly; [STARAC] sits on a
three-legged stool, and on the other side sits [STARICA]; between them is a low round table
with bread, and a grey cat sleeps by the fire. The boy at the door raising his hand in
greeting is [DJECAK], with [TORBA]. [KROVOVI] Keep the upper left sky calm and empty.
```

### 06-bob-na-dar

```text
A bright morning in front of the old couple's small stone house at the edge of the oak
forest, with hens. The boy in the middle carrying an armful of firewood is [DJECAK], with
[TORBA]. The woman handing him a little pouch tied with red wool is [STARICA]. The man
pointing to the path that winds into the hills is [STARAC]. Keep the stack of logs, the far
fields with a small shepherd and his sheep, and the hills. [KROVOVI] Keep the upper right
sky calm and empty.
```

### 07-noc-u-udolini

```text
Dusk in a small hollow surrounded by oak forest, under the first stars in a violet sky. The
tired boy lying asleep in the grass with his head on [TORBA] is [DJECAK]; one bean falls
from his open hand. Keep [TIKVICA] by his head, the piece of bread, the owl in the tree on
the right, the small wind curl, the bushes and stones. Keep the upper left sky calm and
empty.
```

### 08-bob-do-neba

```text
Morning in a wide valley. Keep the gigantic broad bean stalk with white flowers rising from
the ground into the big cloud, the low sun, the small stone village with smoke and the
fields in the distance, the sheep and goats. The sitting boy rubbing his eyes is [DJECAK];
[TORBA] and [TIKVICA] lie next to him. The standing figure next to him is a shepherdess
holding a wooden crook: [STARICA]. The black and white goat on the left looks up at the
stalk. [KROVOVI] Keep the upper right sky calm and empty.
```

### 09-penjanje

```text
A tall view up into the sky. Keep the same gigantic bean stalk with big leaves and white
flowers winding up through the clouds like a ladder, the thick white clouds at the bottom
and the round green swelling near the top with a small arched wooden door in it, glowing
softly. The boy climbing the stalk, seen from behind with [TORBA] on his back, is [DJECAK].
Keep the small brown bird on a leaf looking at him in surprise, the small clouds and birds.
Keep the big clouds at the bottom soft, calm and simple.
```

### 10-kod-svetog-petra

```text
A bright golden corridor in heaven with a cream stone wall and a golden tiled floor. Keep
the same row of arched doors with blank plaques above them, the small saint symbols beside
them (a lily, a grate, a dragon, three golden balls) and the people in folk costume standing
in the doorways. At the right end, in a glowing niche behind a counter, only two hands are
seen offering a bowl of holy water, with a big bunch of keys hanging above. The boy in front
of the counter, half raising his hand to greet, is [DJECAK], with [TORBA]. The plaques stay
blank. Above the wall is only a golden sky with small cream clouds from edge to edge; there
are no trees or plants anywhere in heaven. Keep the upper left sky calm and empty.
```

### 11-nema-boba

```text
High in the sky. Keep the same glowing golden cloud on the left with the open arched
doorway and the wooden door. The boy standing on the threshold holding his head in both
hands in dismay is [DJECAK], with [TORBA] and [TIKVICA]. In front of him there is only
empty blue air with a few small clouds and birds. The ground is only a thin strip at the
very bottom, far below, with tiny trees, a tiny shepherdess, tiny sheep, goats chewing the
stump of the bean stalk and the black and white goat looking up. Keep the upper right sky
calm and empty.
```

### 12-uze-i-dlake

```text
Afternoon high in the sky. Keep the same golden cloud with the open arched doorway on the
left and the long golden cream cloud plateau to the right. The boy sitting with his back to
us is the boy from the second image, with short dark hair under his red cap; his white shirt
is rolled up to his shoulders, and his bare back is dotted with many tiny grey curls, which
he is plucking. Keep the unravelled bag with its loose red thread, the coiled rope striped
red, cream and blue, the rope running over the edge of the cloud and hanging down, ending
high above the ground, and [TIKVICA] on the cloud. The ground is only a thin strip at the
very bottom, far below, with tiny trees, a tiny goat and a sheep. Keep the upper right sky
calm and empty.
```

### 13-na-kraju-uzeta

```text
A tall view at sunset, violet at the top and orange near the ground. Keep the same golden
cloud at the top with the doorway ledge, and the long rope hanging from it, woven from red
wool in the upper part and from grey hairs in the lower part, with a red knot between them.
Hanging from the end of the rope with both hands is [OTRCAN], with [TIKVICA] around his
neck. Below him is a long empty drop of sky. The stony ground is only a thin strip at the
very bottom, far below, with the low setting sun on the left and a few tiny trees. Keep the
sky on both sides of the rope calm and simple.
```

### 14-skok-i-motika

```text
Dusk with a violet sky and the first stars. On the left, [OTRCAN] falls straight down from
the sky with arms and legs spread and a frightened face; above him hang the end of the grey
rope and white speed lines. On the right, the same boy sits on the ground with one foot
stuck in a gap between two grey stones. A dotted path leads from the stones to a small stone
house with smoke and back, and on it a tiny boy carries a hoe. Keep the bush with small
glowing eyes, the oak trees and the hills. [KROVOVI] Keep the upper right sky calm and
empty.
```

### 15-doma

```text
Dusk in the yard of the boy's home under a violet sky with a crescent moon. Keep the same
stone house with a lit window and smoke, the small shed with a hoe leaning by its door, the
stone bench, the dry-stone wall, the hens and the sleeping cat. In the middle, [OTRCAN]
happily hands [TIKVICA] to his mother, who holds the baby and wears [ZENA]. Keep the
grandfather sitting on the bench, the girl, the man with a hoe on his shoulder and the small
boy with the sheep. [KROVOVI] Keep the upper right sky calm and empty.
```

### 16-propusteno-krstenje

```text
A quiet morning in the empty stone room with dark wooden beams. [OTRCAN] stands alone at the
big window, seen from behind. Through the window, far away on a green hill, the family walks
along a path towards a small stone church with a bell; the mother carries the baby. Keep the
wooden cradle, the small table with [TIKVICA] and bread, the cold hearth and the sleeping
cat. [KROVOVI] Keep the left wall calm and empty.
```

### 17-susjed

```text
A warm sunny morning by a dry-stone wall with an open wooden yard gate. [OTRCAN] raises his
hand first and greets the neighbour with a smile. The neighbour, listening and smiling,
leaning on a walking stick, is [STARAC]. Keep the small brown bird on the wall, the stone
house and the shed with a hoe on the left, the hen and the cat, the far village with the
church, and the sun. [KROVOVI] Keep the upper left sky calm and empty.
```

### 36-tvoja-istinita-laz

```text
A quiet sunny picture with no people. Keep the same long stone bench in front of a
dry-stone wall in a meadow. On the bench lie a flat rectangular woollen bag woven in red,
cream and blue stripes with small red diamonds, its bottom edge unravelled into loose red
threads, and a small yellow dried bottle gourd with a red cord and tassel; beside them is an
empty place on the bench. Keep the small brown bird on the wall, the one small round oak
tree on the right and a few flowers. Keep the upper sky calm and empty.
```

### predlist-karta

```text
A map seen from above, painted as a naive picture on one single sheet of warm beige paper
with a thin border, with no fold, crease or seam down the middle. Keep
the same compass star in the upper left, the small village with the church on the left, the
red dotted path through the oak grove with the swirl of leaves, past the small stone house on
the hill, over the blue mountains and green hollows, to the hollow with sheep from which the
giant bean stalk rises to the golden cloud with a wooden door in the upper right. Keep the
cream paper plain between the pictures. [KROVOVI]
```

### 38-rjecnik

```text
Two pages of a picture glossary on plain cream paper, each with a thin rounded border.
Repaint every small object in its place and at its size as a small naive painting: a red
cap, a rocking cradle, a hoe, a hearth with a pot, leather opanci shoes, a meadow with a
sheep and a goat, balls of wool yarn, a woven apron, a swaddled baby, a low round table, a
small cloth bundle, a dry-stone wall, a wooden chest, a small stone shed, a bottle gourd, a
woven bag with tassels, a three-legged stool, a bell, the bean leaf and flowers at the top
and the embroidered band at the top left. At the bottom right [DJECAK] waves, next to a
black and white goat and a small bird on grass. Keep the cream paper plain around the
objects and add nothing.
```

### naslovnica

```text
A square book cover. Keep the same golden glowing cloud with a flat wooden ledge on top of
the gigantic bean stalk with big leaves and white flowers. Standing on the ledge in front of
the arched wooden door, happily waving at the reader, is [DJECAK], with [TORBA] and
[TIKVICA]. The ground is only a low green strip at the very bottom, far below, with two
tiny round trees at the edges, and there the black and white goat chews the stalk. Keep the
small clouds and the bird. Keep the upper sky calm and empty for the title.
```

## LoRA: model uči iz izabranih slika

Model se ne „usavršava“ u prazno, nego uči iz primjera. [slike/lora.py](slike/lora.py)
slaže skup za učenje iz parova koje već imamo: ulaz je SVG kompozicija
(`flux/<ime>/kompozicija.png`), cilj je izabrana inačica (`flux/<ime>/seedNNN.png`, popis
`IZBOR` u skripti), a uputa je ista koju je čitao flux.py. LoRA tako uči „iz ove kompozicije
napravi ovakvu sliku“ i usput zapamti dječaka, nošnju i boje.

Što o tome vrijedi znati, prema mfluxu 0.22:

- **Uređivački model uči se samo na nedestiliranom `flux2-klein-base-4b`.** Mflux to
  izričito provjerava. Naučena LoRA se onda koristi s običnim `flux2-klein-4b` u flux.py
  (`--lora <adapter>.safetensors [mjera]`), a inačice se zovu `seedNNN-<adapter>.png`.
- **Trener prima jednu ulaznu sliku po primjeru**, pa karte dječaka u učenju nema. Dječaka
  LoRA uči iz ciljnih slika.
- **Slike se za učenje smanjuju** na površinu `REZOLUCIJA²` (640 daje 896×448 za 2 : 1),
  istom formulom kao `max_resolution` u mfluxu. Zato povećavanje izabranih slika prije
  učenja ništa ne donosi: trener bi ih odmah smanjio.
- Mflux navodi da učenje uređivačkog modela s `gradient_checkpointing` „stane na strojeve
  s 32–36 GB“. Na 16 GB se zato prvo mjeri probom od dva primjera.

```bash
python3 books/starac-u-mladosti/slike/lora.py --skup
```

```bash
python3 books/starac-u-mladosti/slike/lora.py --proba
```

```bash
books/starac-u-mladosti/slike/lora-uci.sh 10
```

Posljednja naredba je puno učenje (10 epoha, 200 koraka) s držanjem Maca budnim i
bilježenjem memorije; sama skripta bi bila `lora.py --uci --epoha 10`. Naučeni adapter se
izvuče iz zadnje kontrolne točke (`unzip -j .../0000200_checkpoint.zip '*adapter*'`) i
daje flux.py-u kroz `--lora`.

### Što su pokazale probe 27. 10. 2026.

Sve na slici 06-bob-na-dar, 1024 × 512, seed 102, na Macu s M5 i 16 GB
(`slike/flux/proba-9b/usporedba.png`):

| Postavka | Vrijeme | Vršna memorija | Slika |
|---|---|---|---|
| klein-4b, 4 bita, 4 koraka (sadašnje) | 277 s | 9,44 GB | polazna |
| klein-4b, 8 bita, 4 koraka | 266 s | 9,50 GB | gotovo ista |
| klein-4b, 4 bita, 8 koraka | 425 s | 9,44 GB | gotovo ista |
| klein-9b | — | — | model je na Hugging Faceu zaključan iza licencije |

Parametri nisu poluga: sve tri inačice imaju isti veliki hrast u gornjem lijevom kutu i
ista lica. Za klein-9b treba prijava na Hugging Face i prihvaćanje licencije; prije toga
provjeri na stranici modela smije li se slika iz njega koristiti u knjizi za prodaju.

Proba učenja (dva primjera, jedna epoha, `flux/lora/proba/`) je prošla na 16 GB: oko 3
minute po koraku učenja na 1072 × 528 i 3,5 minute po probnoj slici. LoRA iz te probe
učitava se u klein-4b bez greške (mflux: „200/200 keys matched“).

**Puno učenje na 1072 × 528 srušilo je Mac.** Nakon 10 od 200 koraka (35 minuta, koraci
od 150 do 360 s, što je znak da je sustav već gurao memoriju u swap) kernel je pao s
„watchdog timeout“ i računalo se resetiralo; ostala je samo kontrolna točka s koraka 0
(`flux/lora/trening-1-768-stao-kod-10/`). Zato je rezolucija učenja spuštena na 640
(896 × 448), MLX-ov predmemorijski bazen na 1 GB, a kontrolna točka se sprema svakih 10
koraka. `slike/lora-mjeri.sh` uz učenje bilježi slobodnu, žičanu i komprimiranu memoriju i
swap svakih 15 sekundi, a `slike/lora-uci.sh` pokreće učenje, drži Mac budnim i mjeri.

Na 640 je razlika golema: proba od dva koraka trajala je 65 s po koraku umjesto 270, a
probna slika 1 minutu umjesto 3,5. U punom učenju korak traje oko 31 s, pa 200 koraka s 20
probnih slika traje oko 2 sata umjesto 10. Swap pritom nije prazan (oko 7 GB u uporabi uz
3 GB komprimirane memorije, `flux/lora/trening-memorija.log`), ali se vrijeme koraka ne
mijenja, što znači da model ne guta i ne bljuje stranice kao na 768.

### Rezultat učenja 28. 10. 2026.

Puno učenje na 896 × 448 prošlo je svih 200 koraka (10 epoha nad 20 slika) za 2 h 19 min,
bez pada; prosjek 41,8 s po koraku uključujući 20 probnih slika. Gubitak je padao polako i
stalno: prosjek 0,55 u prvih 20 koraka, 0,50 u zadnjih 20 (`flux/lora/trening/loss/`).
Probne slike trenera (`flux/lora/trening/preview/`) pokazuju što je naučio: na koraku 0
nedestilirani base model crta dvije kuće i mutne figure, na koraku 200 kompoziciju kakva je
u izabranim slikama.

Adapter je `flux/lora/trening/starac-200.safetensors` (96 MB, 200/200 ključeva stane u
klein-4b). Prvi test, 06-bob-na-dar sa seedom 101 uz skalu 1,0
(`flux/lora/usporedba-06.png`): kompozicija, likovi i boje su isti kao bez adaptera, jer je
LoRA učila iz slika koje je taj isti model nacrtao; razlika je u teksturi (slikarskija trava
i krošnje, čišći brk i prsluk, više kamena na kući). Hoće li pomoći na slikama gdje je
dječak mijenjao lice i hrast ulazio u kutove, vidi se tek na svih 20, po potrebi uz jaču
skalu (1,4).

Adapter i kontrolna točka nisu u gitu (`flux/` je u `.gitignore`, a GitHub bez LFS-a ne
prima 96 MB): ostaju na disku, a recept za ponovno učenje je `lora.py` + `lora-uci.sh`.
Međutočke 10–190 (19 × 267 MB) su obrisane, čuva se samo `0000200_checkpoint.zip` za
`--nastavi`.
