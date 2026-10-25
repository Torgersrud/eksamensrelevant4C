# ADR 0002: Gap-policy — hvorfor `synthetic-`-filer finnes

Status: accepted (2026-10-25)

## Sammenheng

Pensumsplanen til TMA4432 dekker emner som de fem gamle kursene nesten aldri har
prøvd: tensordekomposisjoner (uke 35) og Bézier-kurver (uke 45) har reelt ingen
ekte eksamensopphav i korpuset; DFT/FFT (uke 41) kan vise seg å bli tynn selv etter
4D-batchene. Tomme mapper gjør ukene usynlige for en student som trener på planen,
men å late som oppdiktede øvelser var ekte eksamensoppgaver ville vært det verste
sviket et øvingsarkiv kan by på.

## Beslutning

For de sanne gap-emnene forfatter vi Syntetiske oppgaver, alltid med prefikset
`synthetic-` helt på starten av filnavnet:

- Prefikset er obligatorisk for alt som ikke kan løses til en rad i `sources/MANIFEST.csv`.
- Syntetiske filer er unntatt fra manifestkravet og løsningsfil-regelen (det finnes ikke
  noe Kildesett), men følger ellers samme filnavnsgrammatikk — årstall og tag er frie å
  velge innenfor de tillatte verdier (`synthetic-2026-test-4C_oppgave1.md` er et lovlig
  syntetisk filnavn).
- De plasseres i de vanlige Emneknutepunkt-mappene og teller med i indekser og README-tabell,
  men blandes aldri med ekte eksamensfiler uten prefiks.
- DFT/FFT vurderes først etter at 4D-batchene er på plass — bare da, hvis det fortsatt er tynt.

## Konsekvenser

Tynne mapper gir likevel drill, og studenten er aldri i tvil om hva som er en ekte
eksamensoppgave: prefikset avgjør. Når rigtige Kildesett (f.eks. den virkelige 2026-eksamen)
legges til, erstatter ekte stoff etter hvert det syntetiske, og validatoren håndhever
skillet dag én.
