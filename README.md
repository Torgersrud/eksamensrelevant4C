# eksamensrelevant4C

Hei!

Dette er en samling av alle eksamensoppgaver som er relevante for TMA4432 Matematikk 4C,
hentet fra de gamle kursene 4N (TMA4125/TMA4130), 4D (TMA4135), Lineære metoder (TMA4145)
og Matematikk 3 (TMA4110) — pluss den offisielle testeksamen for 4C. Markdown-filene er lette
å lese for både oss og KI, så det er lett å be KI om å finne oppgaver til deg. Du må bare se
de igjennom en leser som formaterer LaTeX (Obsidian anbefales).

## Eksamen

- **Emne:** TMA4432 Matematikk 4C — Integraltransformer, funksjonsapproksimasjon og partiel
  differensialligninger
- **Eksamen:** 24. november 2026, kl. 15:00–19:00
- **Hjelpemidler:** Kode **D** — standard kalkulator uten kommunikasjonsmulighet, **ingen**
  håndskrevne support documents (1 side A4 for og mot er IKKE tillatt)
- **Formelark:** deleles av emnet ca. 9. november 2026 (én side, deles ut til eksamen)

## Relevansregel

En Oppgave tas med hvis og bare hvis hovedfaget hennes forekommer på
[pensumsplanen](https://wiki.math.ntnu.no/tma4432/2026h/lecture_plan) til TMA4432 (forelesnings
uke 34–46). Gamle fagnavn teller når planen dekker emnet — «minste kvadraters metode» → Uke 46,
Jacobimatrise og flervariabel Newton → Uke 37. Mapjeplassering er det *eneste* uttrykket for
relevans; ingen kommentarer eller vanskelighetsgrader i filene. Bare ekte eksamenssett
(ordinær + kontinuasjon) og den offisielle testeksamen transkriberes; øving/innlevering og
lærebokoppgaver er utenfor.

## Emneknutepunkt (mappestrukturen)

13 mapper under `oppgaver/`, nøyaktig etter pensumsplanens uker 34–46. Uke 47 (repetisjon)
har ingen mappe. Forfattede øvelser for gap-emner (tensordekomposisjoner, Bézier) får
prefikset `synthetic-` — se [ADR 0002](docs/adr/0002-gap-policy.md).

## Filnavn

    <year>-<term>[-<a-z>]-<tag>[-losning][_dupN]_problem|oppgave<N>.md

- `year`: eksamensåret, `term` ∈ `host`, `var`, `kont`, `sommer`, `test`
- liten bokstav etter terminen: skil fleire Kildesett i same år+term (t.d. to
  sensensur av same eksamen); det første Kildesettjen har vanleg namn, det
  andre får `-b`, det tredje `-c`, osv. — rekkefølgja følgjer Kildesettnummeret
- `tag` ∈ `4N`, `4D`, `LM`, `M3`, `4C` (4C er forbeholdt testeksamen, `2026-test-4C`)
- ordet er `problem` på engelske sett, `oppgave` på norske — uten understrek før nummeret
- `-losning`: løsningsfil, må bare eksistere hvis Kildesettet er løst ifølge manifestet
- `_dupN`: fulltekstkopi av ein Oppgave — anten ein kopi som òg ligg i ein
  annan ukes mappe (mesteren, fila utan `_dupN`, står i mappa med lågast
  ukenummer), eller ei førekomst som er gått på nytt i eit seinare Kildesett
  (mesteren er fila med identisk normalisert heilttekst og ikkje seinare
  år/term — dømes 4N-kopi av ein 4D-mester frå eit delt 4N/4D-examen); første
  kopi er `_dup1`, osv.
- `synthetic-` helt foran: forfattet øvelse, unntatt fra manifestet — prefikset er
  obligatorisk for alt som ikke står i `sources/MANIFEST.csv`

Hver fil har en provensfot på siste linje som løses tilbake til en rad i
`sources/MANIFEST.csv` (kurs, år, term, oppgavenummer, poeng, PDF-navn med sha256).
PDF-ene ligger i gitignored `sources/`; bare manifestet er committet.

## Uke → mappe → antall

Automatisk tabell — regeneration med `python3 scripts/check_repo.py index`.

<!-- TELL-TABELL:START -->
| Uke | Emneknutepunkt | Oppgaver | Løsningsfiler |
|---|---|---|---|
| 34 | [SVD](oppgaver/Uke%2034%20-%20SVD/INDEX.md) | 14 | 13 |
| 35 | [Tensors and Tensor Decomposition](oppgaver/Uke%2035%20-%20Tensors%20and%20Tensor%20Decomposition/INDEX.md) | 4 | 4 |
| 36 | [Parametrised Curves and Surfaces](oppgaver/Uke%2036%20-%20Parametrised%20Curves%20and%20Surfaces/INDEX.md) | 1 | 1 |
| 37 | [Vector Functions I](oppgaver/Uke%2037%20-%20Vector%20Functions%20I/INDEX.md) | 40 | 32 |
| 38 | [Vector Functions II (Optimization)](oppgaver/Uke%2038%20-%20Vector%20Functions%20II%20(Optimization)/INDEX.md) | 1 | 1 |
| 39 | [Fourier Series I](oppgaver/Uke%2039%20-%20Fourier%20Series%20I/INDEX.md) | 42 | 36 |
| 40 | [Fourier Series II](oppgaver/Uke%2040%20-%20Fourier%20Series%20II/INDEX.md) | 29 | 22 |
| 41 | [DFT, FFT and Fourier Transform](oppgaver/Uke%2041%20-%20DFT,%20FFT%20and%20Fourier%20Transform/INDEX.md) | 68 | 57 |
| 42 | [PDE I](oppgaver/Uke%2042%20-%20PDE%20I/INDEX.md) | 15 | 12 |
| 43 | [PDE II](oppgaver/Uke%2043%20-%20PDE%20II/INDEX.md) | 22 | 19 |
| 44 | [PDE III](oppgaver/Uke%2044%20-%20PDE%20III/INDEX.md) | 110 | 87 |
| 45 | [Polynomial, Spline and Bézier Approximation](oppgaver/Uke%2045%20-%20Polynomial,%20Spline%20and%20Bézier%20Approximation/INDEX.md) | 61 | 51 |
| 46 | [Least Squares](oppgaver/Uke%2046%20-%20Least%20Squares/INDEX.md) | 38 | 35 |
| **Sum** | | 445 | 370 |
<!-- TELL-TABELL:SLUTT -->

## Validering

Alt gate'es av én enkeltstående tool (ren standardbibliotek-Python):

    python3 scripts/check_repo.py check   # sjekker alle invarianter (exit 0 = alt i skikk)
    python3 scripts/check_repo.py index   # regenererer INDEX.md for alle mapper + tabellen over
    python3 scripts/test_check_repo.py    # fixture-testene til validatoren

Kjør `check` (gjerne sammen med testene) før hver commit.

## Mer

- [GLOSSARY.md](GLOSSARY.md) — de vedtatte begrepene: Oppgave, Kildesett, Emneknutepunkt,
  Løsningsfil, Syntetisk oppgave, Duplikat, Relevansregel
- [ADR 0001](docs/adr/0001-corpus-selection.md) — kvifor akkurat desse fem kursa
- [ADR 0002](docs/adr/0002-gap-policy.md) — kvifor `synthetic-`-filer finnes

Bruk og/eller misbruk etter egen vilje.

Lykke til med eksamen!
