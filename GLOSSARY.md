# GLOSSARY

Prosjektet snakker ett språk. Disse sju begrepene er vedtatt — bruk dem, ikke synonymene.

## Oppgave

En selvstendig eksamensoppgave, transkribert ordrett fra et Kildesett på originalspråket, med
alle deloppgaver (a/b/c, …) i samme fil. Én fil per Oppgave, ingen kommentarer eller
vanskelighetsgrader. Total poengsum føres i provensfoten når Kildesettet oppgir den.

## Kildesett

Ett eksamenssett (PDF) som Oppgaver er hentet fra — en ekte eksamen (ordinær eller
kontinuasjon) eller den offisielle testeksamen for TMA4432. Hvert Kildesett har en rad i
`sources/MANIFEST.csv` med course, year, term, set_type, filename, url, sha256 og solved.
Selve PDF-en ligger i gitignored `sources/`; bare manifestet er committet.

## Emneknutepunkt

En av de 13 mappene under `oppgaver/`, navngitt etter TMA4432-pensumsplanens kalenderuke og
engelske emneord (f.eks. `Uke 39 - Fourier Series I`). Mapjeplassering er det *eneste*
uttrykket for relevans — ingen merkelapper eller kommentarer i filene. Uke 47 (repetisjon)
har ingen mappe.

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

En fulltekstkopi av en Oppgave som er plassert i ytterligere et Emneknutepunkt, markert med
`_dupN` i filnavnet (`_dup1` er den første kopien, `_dup2` den andre, …). Mesteren er den
tidligste forekomsten: mappen med lavest ukenummer har filen uten `_dupN`, og kopiene
nummereres i stigende uke­rekkefølge. Hver `_dupN` må ha mesteren sin i en mappe med
lavere ukenummer.

## Relevansregel

En Oppgave tas med hvis og bare hvis hovedfaget hennes forekommer på TMA4432s pensumsplan
(forelesningsplanen uke 34–46). Gamle fagnavn teller når planen dekker emnet — f.eks.
«minste kvadraters metode» → Uke 46, Jacobimatrise og flervariabel Newton → Uke 37.
