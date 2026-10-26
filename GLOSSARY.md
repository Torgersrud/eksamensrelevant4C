# GLOSSARY

Prosjektet snakker ett språk. Disse sju begrepene er vedtatt — bruk dem, ikke synonymene.

## Oppgave

En selvstendig eksamensoppgave, transkribert ordrett fra et Kildesett på originalspråket, med
alle deloppgaver (a/b/c, …) i samme fil. Én fil per Oppgave, ingen kommentarer eller
vanskelighetsgrader. Total poengsum føres i provensfoten når Kildesettet oppgir den.

Unntaket er *Kjeldevarsel*: ei henvisningslinje merkt «Kjeldevarsel» (vanlegvis heilt
kursiv, siste linje før provensfoten) som er den eneste tillatte annotasjonsklassen i
filene. Den er et
provenansnotat og brukes til tre ting: (1) errata-/trykkfeil-attestasjon —
at en feil i kilden er bevart ordrett, med det rette svaret oppgitt, (2)
LF-som-provenans-markering — når løsningsarket er den eneste publiserte kilden til
oppgaveteksten, (3) beskrivelse av en figur eller et plot som kilde-PDF-en inneholder.
En Kjeldevarsel er *ikke* innholds- eller vanskelighetskommentar — forbudet mot
vanskelighetsgrader og faglige kommentarer står ved lag.

## Kildesett

Ett eksamenssett (PDF) som Oppgaver er hentet fra — en ekte eksamen (ordinær eller
kontinuasjon) eller den offisielle testeksamen for TMA4432. Hvert Kildesett har en rad i
`sources/MANIFEST.csv` med course, year, term, set_type, filename, url, sha256 og solved.
Selve PDF-en ligger i gitignored `sources/`; bare manifestet er committet.

## Emneknutepunkt

En av de 13 mappene under `oppgaver/`, navngitt etter TMA4432-pensumsplanens kalenderuke og
engelske emneord (f.eks. `Uke 39 - Fourier Series I`). Mapjeplassering er det *eneste*
uttrykket for relevans — ingen merkelapper eller kommentarer i filene, bortsett fra
*Kjeldevarsel*-annotasjonen definert under Oppgave (provenans, aldri relevans eller
vanskelighetsgrad). Uke 47 (repetisjon) har ingen mappe.

## Løsningsfil

Vennindefilen til en Oppgave, med `-losning` inn i filnavnet etter taggen
(f.eks. `2026-test-4C-losning_problem1.md`). Inneholder løsningsforslaget fra Kildesettet.
En Løsningsfil må bare eksistere hvis Kildesettets manifestrad er markert `solved=yes`.

## Syntetisk oppgave

En forfattet exercise for et ekte gap-emne (tensordekomposisjoner, Bézier-kurver, evt.
DFT/FFT), med prefikset `synthetic-` først i filnavnet. Syntetiske filer er unntatt fra
manifestkravet (det finnes ikke noe Kildesett), men følger ellers samme filnavnsgrammatikk.
De blandes aldri med ekte eksamensnavn — prefikset er obligatorisk for alt som ikke står i
manifestet.

## Duplikat

Ein fulltekstkopi av ein Oppgave, markert med `_dupN` i filnavnet (`_dup1` er
den første kopien, `_dup2` den andre, …). Duplikat finst i to variantar: same
Oppgave plassert i ytterligare eit Emneknutepunkt (kopi med same stamn), og
same Oppgave som er gått på ny i eit seinare Kildesett — delte 4N/4D-examen
og gjenbrukte kontinuasjonssett gjer ei førekome med eigen stamn (eige år og
term) til kopi av ein tidlegare mester. Mesteren er alltid den tidlegaste
førekomsten: for fleirfold-mapper kopier står fila utan `_dupN` i mappa med
lågast ukenummer, og for kryss-sett-kopier er mesteren den fila med normalisert
fulltekst (kvitrydd og i liten bokstav, provensfoten utelaten) identisk med
kopiens og (year, term) ikkje seinare enn kopien sin. Kopiar av same mester
nummerast 1..k samanhengande: på tvers av mapper i uke-rekkefølgje, på tvers
av sett i (year, term)-rekkefølgje (var < kont < sommer < host, test først).

## Relevansregel

En Oppgave tas med hvis og bare hvis hovedfaget hennes forekommer på TMA4432s pensumsplan
(forelesningsplanen uke 34–46). Gamle fagnavn teller når planen dekker emnet — f.eks.
«minste kvadraters metode» → Uke 46, Jacobimatrise og flervariabel Newton → Uke 37.
