# ADR 0003: Eldre kurskoder — delte 4M/4N-eksamen under TMA4123

Status: accepted (2026-10-26)

## Sammenheng

ADR 0001 vedtok korpuset som fem kurskoder. Likevel bærer noen manifestrader
koden **TMA4123 (Matematikk 4M)**: i en årrekke ble 4M og 4N undervist og
eksaminert sammen, med felles overskrift på eksamensarket. Filene fra disse
fellessettingene er merket `4N` i filnavnet, siden det er 4N-siden av arket
som er relevant for TMA4432-pensumsplanen.

## Beslutning

De dokumenterte delte 4M/4N-settingene 2012–2015 hører til de fem kursene i
ADR 0001 — de regnes som TMA4125/TMA4130-førekomster under den eldre
med-koden TMA4123. Filene beholder `4N`-taggen; manifestraden beholder den
kurskoden PDF-en faktisk er publisert under. En **rein** TMA4123-eksamen
(4M uten 4N-medkjører) er derimot utenfor korpuset.

## Dokumentasjon — overskriftene som er render og lest (side 1)

| Manifestrad | PDF | Arkets overskrift (gjengitt) | Konklusjon |
|---|---|---|---|
| TMA4125,2012,var (`tma4123_25_v12.pdf`) | fellessett | «Eksamen i TMA4123/TMA4125 Matematikk 4M/N», mandag 21. mai 2012 | Delt — raden føres som TMA4125, filene som `4N` |
| TMA4123,2013,var (`eksamen2013v.pdf`) | fellessett | «Eksamen i TMA4123/TMA4125 Matematikk 4M/4N», torsdag 23. mai 2013 | Delt — beholdt med `4N`-tagg |
| TMA4123,2014,var (`v14-english.pdf`) | fellessett (LF-framside) | «Examination paper for **Solutions to Matematikk 4M and 4N**», eksamensdato 21. mai 2014 | Delt — beholdt med `4N`-tagg |
| TMA4123,2015,var (`eksamen-nb.pdf`) | fellessett | «Eksamensoppgave i TMA4123/TMA4125 Matematikk 4M/4N», 4. juni 2015 | Delt — beholdt med `4N`-tagg |
| TMA4123,2015,kont (`tma4123-4125-4130-2015k.pdf`) | felleskont | «Eksamensoppgave i TMA4123/TMA4125/TMA4130 Matematikk 4M/4N», fredag 14. aug. 2015 | Delt — beholdt med `4N`-tagg |
| ~~TMA4123,2007,var (`TMA4123_v07.pdf`)~~ | **rein 4M** | «EKSAMEN I TMA4123 MATEMATIKK 4M», lørdag 2. juni 2007 — ingen 4N/4125/4130-medkjører | Utenfor korpuset — rad og filer SLETTET |

## Konsekvenser

* ADR 0001s fem kurs inkluderer de dokumenterte delte forekomstene under
  eldre med-koder; TMA4123 er en slik med-kode, ikke et sjette kurs.
* Filnavnene endres ikke: `4N`-taggen uttrykker relevansen for TMA4432,
  provensfoten og manifestraden uttrykker hva arket faktisk trykker.
* 2007-var-førekomstene (`TMA4123_v07.pdf`, 10 filer) er slettet sammen med
  manifestraden — rein 4M, sammenliknbar med unntaket TMA4140 i ADR 0001.
* Framtidige funn av gamle med-koder (4M, «4B», «3N» osv.) vurderes mot
  denne ADR-en: delte eksamener med 4N-medkjører blir værende, rene
  4M-eksamener utelates.
