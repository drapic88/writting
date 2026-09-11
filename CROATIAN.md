# Writing in Croatian

Croatian pieces are **originals, not translations.** A Croatian post is written from its own
`plan.md`, in Croatian, from the first sentence. If the same subject is worth covering in
both languages, it is written twice — the argument is shared, the prose is not.

Everything in [`VOICE.md`](VOICE.md) still applies: the evidence rule, first person
singular, short load-bearing sentences, opinions stated as opinions, no marketing register.
This file covers what Croatian changes.

The reason for the rule: a translated English tech text is audible in Croatian from the
first paragraph. It has English word order, English sentence length, calqued idiom, and
vocabulary nobody says out loud. It reads as a press release, which is exactly the register
`VOICE.md` bans.

---

## 1. Address the reader as *ti*

Second person singular, informal, throughout — matching the English stance of one engineer
writing to another. Imperatives in playbooks are singular:

> Pokreni testove s `error_reporting=E_ALL` i prebroji linije s deprecation upozorenjima.
> Taj broj ti govori je li ovaj upgrade posao za popodne ili za cijeli sprint.

Never *Vi* — it puts a desk between you and the reader. Never the impersonal
*"korisnik bi trebao…"* when you mean *ti*.

## 2. Terminology: say what you would say out loud

The test is simple. **If you would say the English word to a colleague at the whiteboard,
write the English word.** Forcing a Croatian equivalent nobody uses is as damaging to the
voice as unnecessary anglicism.

| Keep the English word | Use the Croatian word |
|-----------------------|------------------------|
| `commit`, `pull request`, `merge`, `rebase`, `branch`, `deploy`, `build`, `staging`, `code review`, `token`, `prompt`, `agent`, `context window`, `framework`, `endpoint` | *greška* / *pogreška*, *ispravak*, *sigurnost*, *pouzdanost*, *održavanje*, *procjena*, *mjerenje*, *radni tok*, *poslužitelj*, *baza*, *sučelje*, *zahtjev*, *upozorenje* |

The line between the columns is not ideology, it is speech. Nobody says *zahtjev za
povlačenjem*; everybody says *pogreška*.

Rules for the English terms:

- **Decline them as Croatian nouns**, in Latin script, without italics or quotation marks:
  *u commitu*, *dva pull requesta*, *nakon deploya*, *na branchu*, *prompta*.
- **Do not respell them phonetically.** `commit`, not *komit*. `deploy`, not *deploj*.
- **Gloss a concept term once**, on first use, then pick one form and stay with it:
  *kontekstni prozor (context window)*, then *kontekstni prozor* everywhere after.
- **Identifiers stay in backticks and stay untouched** — file paths, flags, commands, class
  names. No declension inside backticks: *u datoteci `VOICE.md`*, not `` `VOICE.md`-u ``.

## 3. The register trap: nominalisation

The single most common way Croatian technical prose goes dead is turning verbs into nouns
and hanging them off an empty auxiliary. Croatian administrative style does this by default.
Reverse it every time.

| Ne | Da |
|----|-----|
| *izvršiti provjeru konfiguracije* | *provjeriti konfiguraciju* |
| *vrši se obrada podataka* | *sustav obrađuje podatke* |
| *u svrhu smanjenja broja grešaka* | *da bi bilo manje grešaka* |
| *prilikom izvođenja testova* | *kad pokreneš testove* |
| *došlo je do pada servisa* | *servis je pao* |
| *postoji mogućnost da* | *možda* |

Same principle as the English anti-pattern list: one qualifier per claim, and a verb doing
the work.

## 4. Sentence mechanics

- **Croatian tolerates longer clauses than English. The load-bearing sentence stays short
  anyway.** "Model se nije promijenio. Promijenilo se ono što je bilo pred njim."
- **Word order is your stress tool.** Croatian puts the new, important information at the
  end of the sentence. Use that instead of bolding more words.
- **Watch the enclitics.** *je, se, ga, mu, bi, će* go in second position. A sentence that
  starts *"Se događa…"* or *"Je li to bitno — je."* reads as broken, not casual.
- **Diacritics are mandatory** in prose: *č, ć, ž, š, đ*. A piece written without them reads
  as an SMS from 2005. They are of course absent inside code blocks and identifiers.
- **Standard forms:** *neću* (not *ne ću*), *ne znam* separate, *s* before most consonants
  and *sa* before *s, š, z, ž* and awkward clusters (*sa mnom*, *s timom*).
- **Numbers and dates Croatian-style:** decimal comma (*3,5 sata*), thousands separator a
  full stop (*1.400 × 650*), ordinals with a full stop (*14. ožujka 2026.*), and 24-hour
  time with a full stop (*14.30*).
- **Quotation marks:** „ovako" in prose. Straight quotes stay inside code.

## 5. Titles and headings

**English H1 is Title Case. Croatian H1 is sentence case.** Croatian capitalises only the
first word and proper nouns, and a Title Cased Croatian headline instantly reads as
machine-translated.

> *Tvoj AI nije postao gluplji. Tvoj kontekst jest.*
> *"Gotovo" su zapravo pet odvojenih tvrdnji.*

The title is still a claim with a verb in it, and the two-sentence false-belief-then-
correction form works at least as well in Croatian as in English.

## 6. Idioms that must not cross over

Calques that are invisible to a bilingual writer and glaring to a monolingual reader:

- *na kraju dana* (at the end of the day) → *u konačnici*, or cut it
- *u današnjem brzom svijetu* → banned in both languages, see `VOICE.md` §5
- *adresirati problem* → *riješiti*, *pozabaviti se*
- *implementirati rješenje* → *napraviti*, *uvesti*, *napisati*
- *podržava se* for "is supported" where *radi* is the honest word
- *pobrinuti se da* stacked three times per paragraph → vary or cut
- *dobar dan svima* / *pozdrav* as an opener → the lede starts with the problem, same as
  in English

## 7. Croatian anti-pattern list

The `VOICE.md` §5 list, in its local forms. None of these appear in a draft:

*revolucionarno*, *moćan alat*, *nezaobilazan*, *robustan*, *bešavan*, *iskoristi puni
potencijal*, *podigni na višu razinu*, *u današnje vrijeme*, *bez daljnjega*, *zaronimo*,
*u ovom članku ćemo objasniti*, *AI mijenja svijet razvoja softvera*.

And the structural ones carry over unchanged: no rhetorical question as a first line, no
listicle without a thesis, no closing paragraph that only summarises.

## 8. Check before publishing a Croatian piece

- [ ] Written from a Croatian `plan.md`, not translated from an English draft.
- [ ] *ti* throughout, imperatives singular.
- [ ] Every English term is one you would actually say out loud, declined as a Croatian noun.
- [ ] No nominalisation chains (§3); verbs are doing the work.
- [ ] Enclitics in second position; diacritics everywhere in prose.
- [ ] Title in sentence case, still a claim with a verb.
- [ ] Numbers, dates and quotation marks in Croatian conventions.
- [ ] Zero entries from §6 and §7.
- [ ] Read aloud once. If a sentence has an English shape, rewrite it, don't patch it.
