# ADR 0001: Korpusvalget — fem kildekurs, og kursnavn-rettingene

Status: accepted (2026-10-25)

## Sammenheng

TMA4432 Matematikk 4C går sin første periode høsten 2026 og har ingen egne tidligere
eksamener. Emnene har blitt prøvd på NTNU i over 20 år under gamle kurskoder, men
Kildesettene er spredt over flere kurswikier. Vi må velge hvilke kurs vi transkriberer fra:
for vidt valg gir urelevant støy, for snevert gir tynne mapper.

## Beslutning

Korpuset er disse fem kursene:

| Kurs | Reelt navn | Bidrag |
|---|---|---|
| TMA4125 + TMA4130 | Matematikk **4N** (vår / høst) | 4N-tvingene; felles eksamensarkiv |
| TMA4135 | Matematikk **4D** | tetttest match mot 4C-pensum |
| TMA4145 | **Lineære metoder** | den virkelige SVD/Moore-Penrose/minste-kvadrater-kilden |
| TMA4110 | Matematikk **3** | kurver, flater, flervariabel optimalisering |

Unntatt: TMA4140 Diskret matematikk (irrelevant for pensumsplanen) og TMA4120 (4K).
TMA4105 (M2) stod også på unntakslista med premissa om at «innholdet deres er dekket av
henholdsvis 4D- og M3-materialet» — premissen vart motbevist da uke 36/38 viste seg å
vere tomme for ekte stoff, og unntaket for M2 er oppheva av ADR 0004.

## Kursnavn-rettingene

Tidligere antakelser var feil og må ikke dukke opp igjen i filnavn eller dokumentasjon:

- TMA4135 er Matematikk **4D** (ikke «4B»)
- TMA4145 er **Lineære metoder** (ikke «4L»)
- TMA4130 er 4N (høst), TMA4125 er 4N (vår) (ikke «3N» eller «4L»)
- TMA4110 er Matematikk **3**
- TMA4120 er 4K

Taggene i filnavnene er derfor kun `4N`, `4D`, `LM`, `M3`, `4C`.

## Konsekvenser

Kildesettene ligger på fem kurswikier med ulik dekning: 4N ca. 1999–2025, 4D 2003–2024
(løsningsforslag nesten alltid), LM 2000–2022 (fasit nesten alle år), mens M3-sidens dekning
må sjekkes når det batchet starter. Endringer i korpuset krever et nytt ADR.
