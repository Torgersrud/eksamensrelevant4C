# Research: TMA4105 Matematikk 2 (M2) exam archive — the harvest source for Uke 36/38

> Provenans: utarbeidd 2026-10-26 av research-agenten som bakgrunn for ADR 0004 og haustingstikkettane #7–#10 (issue #1); lagd under docs/research/ av ticket 2 på greina `spec/fill-35-36-38`.

Date: 2026-10-26. Every claim below cites a primary-source URL that was fetched on that date. All 110 exam/solution URLs were probed live (55 downloads + 55 HEAD requests); quoted text was extracted from the cited PDFs/pages themselves.

## Question

Does the NTNU TMA4105 Matematikk 2 exam archive at https://wiki.math.ntnu.no/tma4105/ really hold the Kildesett that the TMA4432 Matematikk 4C corpus is missing — real facited exam problems on parametrised curves/surfaces (Uke 36) and classical multivariable optimisation (Uke 38)? Per year 1998–2026: which sett are published (ordinary + continuation), at which exact URLs, in which language, does a facit/løysingsark exist, and how good is the PDF text layer for transcription?

## Short answer

**Yes.** The archive is one DokuWiki page, `tma4105:exam`, and it publishes **55 complete Kildesett: every year 2000–2025 has BOTH the ordinary spring exam and the August continuation exam, every single one with a published Løsningsforslag PDF** (plus Vår 1998 and Vår 1999, ordinary only, and Vår 2026, ordinary already published as of the probe date). All problem sets and all solution sheets returned HTTP 200 on 2026-10-26. All material is Norwegian (bokmål for most sett; seven published sett are nynorsk). Every file is digitally born LaTeX **except `tma4105_2023k.pdf`, which is a pure 3-page scan with no text layer**. Text-layer quality improves sharply toward the present — newest-first harvesting (as the spec decided) is the right order.

## 1. Where the archive lives and how it is organised

- **Course root** https://wiki.math.ntnu.no/tma4105 lists semester pages for **our-semester only** (2004v–2025v; pre-2008 semesters link to the old site `https://www.math.ntnu.no/emner/TMA4105/...`). Probing `tma4105/2024h` → HTTP 404: Matematikk 2 was not run as a fall course in the wiki era; the "second sett per year" in the archive table is the **August continuation ("Sommeren YYYY")**, not a fall semester.
- **The complete list** is the course-level page https://wiki.math.ntnu.no/tma4105/exam (raw: `?do=export_raw`), titled "Gamle eksamensoppgaver", embedded into each year via `{{page>:tma4105:exam}}` (e.g. https://wiki.math.ntnu.no/tma4105/2025v/eksamensoppgaver). One fetch yields the whole archive; no per-year crawling needed.
- **Download URL pattern** for every file (media namespace `:tma4105:eksamen:`):
  `https://wiki.math.ntnu.no/_media/tma4105/eksamen/<filename>.pdf`
  e.g. https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2026v.pdf and https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2026v.pdf
- **The wiki itself records four errata in the løsningsforslag** (footnotes on the exam page; verbatim, abridged):
  - Sommeren 2010 [1]: «I oppgave 5c er riktig svar 2π√3 og ikke 3π√3 slik det står i løsningsforslaget.»
  - Sommeren 2008 [2]: «I oppgave 6b er det feil fortegn i svaret.»
  - Sommeren 2006 [3]: «På side 4, linje 4 ovenfra skal grensene for x være −1 og 1, ikke 0 og 2. Feilen har ingen konsekvens for svaret.»
  - Sommeren 2012 [4]: «Det siste integralet som opptrer i løsningsforslaget for oppgave 4 har verdi 1/2, ikke 1 som der skrives.»
  These must become Kjeldevarsel errata attestations in the transcriptions (GLOSSARY use (1)).
- The page also hosts two PDFs from the predecessor course 75002/75012 Matematikk 1B (1993–1997): https://wiki.math.ntnu.no/_media/tma4105/eksamen/samling.pdf and https://wiki.math.ntnu.no/_media/tma4105/eksamen/samling2.pdf. **OUT for the corpus** — not M2, and pre-1998.
- A fourth table column links mediasite video walkthroughs for ~10 sett (e.g. 2012k 6a–6c). Not corpus material; ignore for harvest.

## 2. Per-year table (all 55 published Kildesett 1998–2026)

Every row: problem set + solution sheet both published (facit: **yes** for all 55). "ordinar" = Våren YYYY ordinary exam; "kont" = Sommeren YYYY continuation. Language = målform of the *published* problem PDF, determined from its extracted text (see §3). Text-layer classes per §4.

| # | År · sett | Oppgaver-fil | Løysingsark-fil | Målform | Tekstlag (oppgåvesett) |
|---|---|---|---|---|---|
| 1 | 2026 · ordinar | [`tma4105_2026v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2026v.pdf) | [`lf_tma4105_2026v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2026v.pdf) | bokmål | digital, clean |
| 2 | 2025 · ordinar | [`tma4105_2025v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2025v.pdf) | [`lf_tma4105_2025v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2025v.pdf) | bokmål | digital, clean |
| 3 | 2025 · kont | [`tma4105_2025k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2025k.pdf) | [`lf_tma4105_2025k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2025k.pdf) | bokmål | digital, clean |
| 4 | 2024 · ordinar | [`tma4105_2024v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2024v.pdf) | [`lf_tma4105_2024v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2024v.pdf) | bokmål | digital, clean |
| 5 | 2024 · kont | [`tma4105_2024k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2024k.pdf) | [`lf_tma4105_2024k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2024k.pdf) | bokmål | digital, clean |
| 6 | 2023 · ordinar | [`tma4105_2023v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2023v.pdf) | [`lf_tma4105_2023v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2023v.pdf) | bokmål | digital, clean |
| 7 | 2023 · kont | [`tma4105_2023k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2023k.pdf) | [`lf_tma4105_2023k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2023k.pdf) | bokmål | SCAN — no text layer — the only scan in the archive (3 raster pages) |
| 8 | 2022 · ordinar | [`tma4105_2022v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2022v.pdf) | [`lf_tma4105_2022v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2022v.pdf) | bokmål | digital, strong glyph splitting |
| 9 | 2022 · kont | [`tma4105_2022k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2022k.pdf) | [`lf_tma4105_2022k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2022k.pdf) | bokmål | digital, clean |
| 10 | 2021 · ordinar | [`tma4105_2021v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2021v.pdf) | [`lf_tma4105_2021v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2021v.pdf) | bokmål | digital, clean |
| 11 | 2021 · kont | [`tma4105_2021k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2021k.pdf) | [`lf_tma4105_2021k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2021k.pdf) | **nynorsk** | digital, clean |
| 12 | 2020 · ordinar | [`tma4105_2020v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2020v.pdf) | [`lf_tma4105_2020v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2020v.pdf) | bokmål | digital, strong glyph splitting — Inspera home exam, multiple-choice format, 5 pp, 5 JPEG figures |
| 13 | 2020 · kont | [`tma4105_2020k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2020k.pdf) | [`lf_tma4105_2020k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2020k.pdf) | bokmål | digital, strong glyph splitting — Inspera home exam, multiple-choice format, 4 pp, 5 JPEG figures |
| 14 | 2019 · ordinar | [`tma4105_2019v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2019v.pdf) | [`lf_tma4105_2019v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2019v.pdf) | **nynorsk** | digital, strong glyph splitting |
| 15 | 2019 · kont | [`tma4105_2019k_web.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2019k_web.pdf) | [`lf_tma4105_2019k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2019k.pdf) | bokmål | digital, clean — «_web» in filename |
| 16 | 2018 · ordinar | [`tma4105_2018v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2018v.pdf) | [`lf_tma4105_2018v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2018v.pdf) | bokmål | digital, clean |
| 17 | 2018 · kont | [`tma4105_2018k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2018k.pdf) | [`lf_tma4105_2018k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2018k.pdf) | bokmål | digital, clean |
| 18 | 2017 · ordinar | [`tma4105_2017v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2017v.pdf) | [`lf_tma4105_2017v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2017v.pdf) | bokmål | digital, clean |
| 19 | 2017 · kont | [`tma4105_2017k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2017k.pdf) | [`lf_tma4105_2017k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2017k.pdf) | bokmål | digital, clean |
| 20 | 2016 · ordinar | [`tma4105_2016v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2016v.pdf) | [`lf_tma4105_2016v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2016v.pdf) | bokmål | digital, clean |
| 21 | 2016 · kont | [`tma4105_2016k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2016k.pdf) | [`lf_tma4105_2016k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2016k.pdf) | bokmål | digital, clean |
| 22 | 2015 · ordinar | [`tma4105_15v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_15v.pdf) | [`tma4105_15v_lf.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_15v_lf.pdf) | bokmål | digital, clean — LF named tma4105_15v_lf.pdf (suffix, not lf_ prefix) |
| 23 | 2015 · kont | [`tma4105_2015_15k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_2015_15k.pdf) | [`lf_tma4105_2015_15k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_2015_15k.pdf) | bokmål | digital, clean — odd filename (kont 2015) |
| 24 | 2014 · ordinar | [`tma4105_14v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_14v.pdf) | [`lf_tma4105_14v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_14v.pdf) | bokmål | digital, clean |
| 25 | 2014 · kont | [`tma4105_14k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_14k.pdf) | [`lf_tma4105_14k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_14k.pdf) | bokmål | digital, clean — video walkthrough 6a on mediasite |
| 26 | 2013 · ordinar | [`tma4105_13v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_13v.pdf) | [`lf_tma4105_13v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_13v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 27 | 2013 · kont | [`tma4105_13k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_13k.pdf) | [`lf_tma4105_13k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_13k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 28 | 2012 · ordinar | [`tma4105_12v_ny.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_12v_ny.pdf) | [`lf_tma4105_12v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_12v.pdf) | **nynorsk** | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) — title prints «nynorsk» («_ny» in filename) |
| 29 | 2012 · kont | [`tma4105_12k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_12k.pdf) | [`lf_tma4105_12k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_12k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) — video walkthrough 6a–6c; LF erratum [4] |
| 30 | 2011 · ordinar | [`tma4105_11v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_11v.pdf) | [`lf_tma4105_11v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_11v.pdf) | **nynorsk** | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 31 | 2011 · kont | [`tma4105_11k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_11k.pdf) | [`lf_tma4105_11k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_11k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 32 | 2010 · ordinar | [`tma4105_10v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_10v.pdf) | [`lf_tma4105_10v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_10v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 33 | 2010 · kont | [`tma4105_10k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_10k.pdf) | [`lf_tma4105_10k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_10k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) — LF erratum [1] (5c svar 2π√3) |
| 34 | 2009 · ordinar | [`tma4105_09v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_09v.pdf) | [`lf_tma4105_09v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_09v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 35 | 2009 · kont | [`tma4105_09k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_09k.pdf) | [`lf_tma4105_09k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_09k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 36 | 2008 · ordinar | [`tma4105_08v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_08v.pdf) | [`lf_tma4105_08v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_08v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 37 | 2008 · kont | [`tma4105_08k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_08k.pdf) | [`lf_tma4105_08k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_08k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) — LF erratum [2] (fortegn 6b) |
| 38 | 2007 · ordinar | [`tma4105_07v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_07v.pdf) | [`lf_tma4105_07v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_07v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 39 | 2007 · kont | [`tma4105_07k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_07k.pdf) | [`lf_tma4105_07k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_07k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 40 | 2006 · ordinar | [`tma4105_06v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_06v.pdf) | [`lf_tma4105_06v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_06v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 41 | 2006 · kont | [`tma4105_06k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_06k.pdf) | [`lf_tma4105_06k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_06k.pdf) | **nynorsk** | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) — LF erratum [3] (grenser x: −1/1) |
| 42 | 2005 · ordinar | [`tma4105_05v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_05v.pdf) | [`lf_tma4105_05v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_05v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 43 | 2005 · kont | [`tma4105_05k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_05k.pdf) | [`lf_tma4105_05k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_05k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 44 | 2004 · ordinar | [`tma4105_04v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_04v.pdf) | [`lf_tma4105_04v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_04v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 45 | 2004 · kont | [`tma4105_04k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/tma4105_04k.pdf) | [`lf_tma4105_04k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_tma4105_04k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 46 | 2003 · ordinar | [`sif5005_03v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_03v.pdf) | [`lf_sif5005_03v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_sif5005_03v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 47 | 2003 · kont | [`sif5005_03k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_03k.pdf) | [`lf_sif5005_03k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_sif5005_03k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 48 | 2002 · ordinar | [`sif5005_02v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_02v.pdf) | [`lf_sif5005_02v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_sif5005_02v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 49 | 2002 · kont | [`sif5005_02k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_02k.pdf) | [`lf_sif5005_02k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_sif5005_02k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 50 | 2001 · ordinar | [`sif5005_01v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_01v.pdf) | [`lf_sif5005_01v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_sif5005_01v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 51 | 2001 · kont | [`sif5005_01k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_01k.pdf) | [`lf_sif5005_01k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_sif5005_01k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 52 | 2000 · ordinar | [`sif5005_00v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_00v.pdf) | [`lf_sif5005_00v.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_sif5005_00v.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 53 | 2000 · kont | [`sif5005_00k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_00k.pdf) | [`lf_sif5005_00k.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/lf_sif5005_00k.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 54 | 1999 · ordinar | [`sif5005_1999-05-14.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_1999-05-14.pdf) | [`sif5005_1999-05-14_lf.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_1999-05-14_lf.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |
| 55 | 1998 · ordinar | [`sif5005_1998-05-14.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_1998-05-14.pdf) | [`sif5005_1998-05-14_lf.pdf`](https://wiki.math.ntnu.no/_media/tma4105/eksamen/sif5005_1998-05-14_lf.pdf) | bokmål | digital, old Type1/OT1 (å/æ/ø garble in naïve extraction) |

## 3. Language

**No English M2 exam exists in this archive.** The 2020 exam page states the policy outright: «Eksamensoppgavene blir tilgjengelig på bokmål og på nynorsk. Ingen har bedt om oppgaver på engelsk.» — https://wiki.math.ntnu.no/tma4105/2020v/eksamen. So the spec's "norsk/engelsk" column resolves to norsk for all 55 sett.

Within norsk, seven published sett are **nynorsk** (verified from title glyphs and word forms, e.g. «Oppgåve», «La T vere området … avgrensa», «Dette er ein kombinasjon», «laurdag», «Bestem dei kritiske punkta»): Sommeren 2006, Våren 2011, Våren 2012 (the file is literally `tma4105_12v_ny.pdf`, its title prints «nynorsk»), Våren 2016, Våren 2017, Våren 2019, Sommeren 2021. The remaining 48 are bokmål. Since both variants were produced in some years (§4 of the 2020 page proves the practice), a parallel bokmål/nynorsk twin of a published sett may exist outside the wiki; the central censor archive was not searched (unverified, see Open uncertainties). Transcription law keeps each file on its own published målform.

Note that the classification is per *published sett*, judged on formative markers (the Oppgave/Oppgåve headings and the dominant word forms) — an individual M2 sett can mix målformar, because the teaching group compiles it from a shared problem bank: e.g. the 2024 ordinary («bokmål» by its headings) contains «Du trenger ikkje å vise dette» and «eit firma produserer … einingar» inside its problems. Transcriptions keep every problem verbatim on its own printed form, so this column is a harvest aid, not a transcription rule.

The recent headers already show exactly the uke-36/38 topics the corpus lacks, e.g.: 2018v «Finn en parametrisering av skjæringen …», 2022k «Finn punkta på hyperboloid …», 2026v «Bestem dei kritiske punkta …», 2016v «La C vere kurva gitt ved r(t) = …».

## 4. Text-layer quality

Structure probe of all 55 downloaded problem PDFs (stream-level inspection): every file is digital-native pdfTeX/LaTeX with a text layer — no CCITT/JBIG2 anywhere — **except `tma4105_2023k.pdf`, which is 3 rasterized full-page images with zero text operators (a scan; needs visual/OCR transcription and its exam date is not machine-readable)**. Quality tiers:

1. **1998–2013 (incl. all SIF5005 files)** — digital Type1/OT1 subset fonts. Text exists but naïve extraction garbles it: heavy inter-glyph splitting and å/æ/ø land on odd code points (extracted sample: «No r g es t ek ni s knatur v i tensk ap eli ge univ ersit et», «Oppg v e»). Recoverable with a proper extractor + encoding normalisation, but expect cleanup work. This matches the spec's "batch newest-first (better text layers)".
2. **2014–2018, 2021, 2023v, 2024, 2025, 2026** — clean word-level TJ arrays; extraction is near-verbatim (e.g. 2024k extracts «Oppgave 1 Finn en ligning for tangentpla…»).
3. **2019v, 2020v, 2020k, 2022v** — digital but glyph-level splitting from kerned CM fonts (extracts as «T M A 4 1 0 5 M a t e m a t i k k 2»); needs space-squeeze normalisation.
4. **2020v/2020k format caveat** — these are the Korona Inspera home exams (multiple choice, pairing, short-answer types; 5 and 4 pages; five embedded JPEG figures). The Relevansregel still judges each problem, but the problem style differs from the classic M2 sett.
5. **2023k** — the only scan (see above).

## 5. Filename quirks (for the manifest `filename` column)

- 1998/1999 use date-style names with the solution as a `_lf` suffix: `sif5005_1998-05-14.pdf` / `sif5005_1998-05-14_lf.pdf` (same pattern 1999), unlike the otherwise universal `lf_` prefix.
- Våren 2012 problem set is `tma4105_12v_ny.pdf` (nynorsk variant); its solution is `lf_tma4105_12v.pdf`.
- Våren 2015 pair: `tma4105_15v.pdf` + `tma4105_15v_lf.pdf` (suffix again); Sommeren 2015: `tma4105_2015_15k.pdf` + `lf_tma4105_2015_15k.pdf` (mixed 4/2-digit year).
- Sommeren 2019 is `tma4105_2019k_web.pdf` (suffix `_web`).
- From Vår 2020 down, the wiki itself switched to full `tma4105_YYYYv/k.pdf` names.

## 6. What this means for the harvest tickets (#7–#10)

- **55 candidate Kildesett, every one `solved` (solution PDF published)** — the manifest column solved gets `ja` throughout unless a transcription batch proves a specific LF unreadable.
- **Course codes:** ≥ 2004 → `TMA4105`; the ten SIF5005-coded sett 1998–2003 → manifest course `SIF5005` (the code the sheets actually print — the wiki re-branded them under TMA4105), all files tagged `M2` per ADR 0004 (ADR 0003 precedent).
- **Suggested batch split, newest-first** (one commit per sett regardless): #7: 2026v–2019k (14 sett), #8: 2019v–2012k (14), #9: 2012v–2005k (14), #10: 2005v–1998v incl. SIF5005 (13). Expect the Relevansregel to cut many sett down to 1–3 Oppgaver each (line/surface integrals, flux and multiple integrals stay UT), so batches will not be uniform. 2023k (scan) should be scheduled late and manually.
- **Politeness:** wiki.math.ntnu.no flood-blocks aggressive clients. All downloads in this survey ran a single-file queue with a custom User-Agent and a 4.5 s sleep between requests; no 403/429 occurred (script had a 30 s backoff-retry built in, unused). Keep that discipline in harvest.
- **Cached copies:** all 55 problem PDFs + the two 1B samling PDFs are on disk under `/tmp/opencode/pdfs/m2/` with sha256 recorded in the appendix; a harvester can hash-verify without re-downloading. The 55 solution PDFs were only HEAD-verified, not downloaded.

## Open uncertainties / what I could NOT verify

- The **content of the solution PDFs** was not read (HEAD-only verification); the only known LF defects are the four the wiki itself records.
- Per-problem **Relevansregel classification** is deliberately not done here — first page headers were sampled for topic evidence only; full classification belongs to the harvest tickets.
- Whether **parallel bokmål/nynorsk twins** of the seven nynorsk sett (and vice versa) exist beyond the wiki (central censor archive https://www.ntnu.edu/students/exams is a JS app, not machine-searchable here).
- **Sommeren 2026** will presumably appear on the page in August 2026; the survey reflects the page as fetched 2026-10-26 (which already lists Vår 2026 but no Sommeren 2026 — plausible if the 2026 kont sits later or was withheld).
- 2023k: exam **date and page count** are not machine-readable (scan); the table lists what the wiki's own row says (Sommeren 2023).

## Method & source policy

Primary sources only: the DokuWiki raw exports (`?do=export_raw`) of https://wiki.math.ntnu.no/tma4105, https://wiki.math.ntnu.no/tma4105/exam and selected semester pages, and the media PDFs themselves. Fetch policy: custom User-Agent `OpenCode-research-agent/1.0`, one request at a time, ≥ 4.5 s between wiki hits, 30 s backoff-retry on 403/429. PDF inspection without system pdftotext (none installed): Python-stdlib FlateDecode/Tj-TJ extraction (`/tmp/opencode/pdftxt.py` plus a throwaway word-assembly variant), plus a stream-level structure probe (filters, image XObjects, BT counts, ToUnicode). Language calls from word-form counts on space-squeezed extracted text (Oppgave/Oppgåve, ikke/ikkje, …). Working artifacts (URL list, per-file JSON probes, status log) under `/tmp/opencode/m2survey/`; PDFs under `/tmp/opencode/pdfs/m2/`. No PDF is committed anywhere; repo work happened only in the ticket worktree.

## Appendix — sha256 of the cached problem-set PDFs

Downloaded from the URLs in §2 on 2026-10-26; verify before reusing instead of re-downloading.

| fil | sha256 |
|---|---|
| `samling.pdf` | `880aab2314761233f58f3908cc588c1d30bf4e0a4b95b5429d8df9530bfa7ce6` |
| `samling2.pdf` | `1a3358ecf4a774afe4cd495ba00f5971f46f7481562dc03d5b4952b83c4ea695` |
| `sif5005_00k.pdf` | `086b07997a5631cc56cab55fc2b95d3a1e4ca5f4a196be062b91361ee3557a21` |
| `sif5005_00v.pdf` | `fac4b763dafdabe9fe6c6be55d5f05efa9178516e0d929aa2c75e99a6c1bd2ca` |
| `sif5005_01k.pdf` | `6c4d5245c8a095d4ad4a76dafd3eec9db438104ba8b416d2d71e0471ab0da61d` |
| `sif5005_01v.pdf` | `7ec3c57247a1465ee1c1a8a47967f3b7c3daf6d17b280246e10c740e46bff7fb` |
| `sif5005_02k.pdf` | `e6140120387c7d6189c4bb7bf562f698495bd137e29c6fcdabc9281e84237691` |
| `sif5005_02v.pdf` | `5f9676a8f2813b6e75a6a8da926555c624397aba5f230118caae2580695b381b` |
| `sif5005_03k.pdf` | `c18287c5ee574fc7165af29bc5accf47a23037f3a3de7b6e26eec11331e4a5a9` |
| `sif5005_03v.pdf` | `61d1f6920e9a8b4e105daa2d7f1d7ef68b008398324331665ad1fa424f7025aa` |
| `sif5005_1998-05-14.pdf` | `03309e9cc9fa099c338d057c61b5397324f08cbf96bb66022159d392d766b7e8` |
| `sif5005_1999-05-14.pdf` | `798cf6b3e0d6d4795b15ff8d941b97b7f25eb2ce0916934d9c48a14c8ba634bd` |
| `tma4105_04k.pdf` | `fe57813e19a87df6e081df46c52c276f4998febaec65995e0839b310afe43fe0` |
| `tma4105_04v.pdf` | `1c4672565abbcf85c30792573da95d8c57840bee4ce81a6495425e09394f9d9d` |
| `tma4105_05k.pdf` | `5f6bcc57da5e38f523088439e0ea979b92ecbd4bc9827c946ba92447382189bc` |
| `tma4105_05v.pdf` | `ce87983e6fa2d421bf45577dfb405c2598220017f097049d89bfc9c8a33964eb` |
| `tma4105_06k.pdf` | `816583444e02ae6d9e8e196c9523dcf3e4d23878f956055b56fcca16c3670908` |
| `tma4105_06v.pdf` | `25aca981a46e6cdcd9a79bc58fdfbd2f6856bc1d35359e674080b23c8ff6f45d` |
| `tma4105_07k.pdf` | `734a6dc9b27689d27071a42d8bf6d4719d39ab24c1f2b132ea54585e51200faf` |
| `tma4105_07v.pdf` | `5c448292283c7df8b4cde5582e38c9ff1db3e6311391fafb1c88ada55212a312` |
| `tma4105_08k.pdf` | `19cbc13e7ef66b24451f9c5838c48477f9b6a801771ce25dfe1a3152d3b3d8f8` |
| `tma4105_08v.pdf` | `020da6f2a22898deab42836b7da6a49708024cfeef7fef936a80e45330f862a3` |
| `tma4105_09k.pdf` | `514d147f9ca5f0048ce5cb2008bc7f4a17ac428213cd53557e2b27e47e11f8c2` |
| `tma4105_09v.pdf` | `5f9c990d45b463ea28f09059fb7d1e4501a240ad05c1e4c67002d34e7d8c53d6` |
| `tma4105_10k.pdf` | `11714f3e2e4da1eeac6300960e9eadfebdaef5ced58c0060a73a4042ffd8a510` |
| `tma4105_10v.pdf` | `bc6c5ad95115b9dc020632762ee8b5c3451fcf47d613e00550d75d81999086f0` |
| `tma4105_11k.pdf` | `931078ebabdc6f832caa2a99d1a08dd06cc0528258e9e6ee18f14416b3d029df` |
| `tma4105_11v.pdf` | `a59dd632b20874990a557b329ec8c0da5a0eb3f6a395824c9826fe6c1dc9606d` |
| `tma4105_12k.pdf` | `19ce3e7f9d412e8678662093322cd25d74b2dda1d19c894e5b22a47f30656719` |
| `tma4105_12v_ny.pdf` | `29010f46b92bc6ea90eb1d242598dccea90dbbde47eda52dbb7364b9ff20c767` |
| `tma4105_13k.pdf` | `5844ce53979c705000c5f7fd2c150aee960084f225a4b462e07acae1665c1f51` |
| `tma4105_13v.pdf` | `7e6ecb7d4f1963fc0a5ed89b431940461bb6a23d2d3e10fcf32a6eeef2e1b731` |
| `tma4105_14k.pdf` | `d19fa3c10fd69b43abe530d12d5409e12f1d9c5e52f5695ed8706fc21c2d633b` |
| `tma4105_14v.pdf` | `828591c99bc86efb583fc1fbdebed501106ffdef5bde53f157ba7b93472ce967` |
| `tma4105_15v.pdf` | `95fe40dd81bb77924c755d895ca69f8421c6af0a1796a661e5194e0855956e86` |
| `tma4105_2015_15k.pdf` | `456fffe91ef4cb71f6ec536043eb52ea2064aaf9fa75ca638ed21e188866c7de` |
| `tma4105_2016k.pdf` | `68bcbe4704f7cd47ac538304f5756593d3c2aedd81e782887d534838bce522df` |
| `tma4105_2016v.pdf` | `3157ad76704ef6320d938b23c2bf46536ed6ac6e394592a30d3f692022ef5519` |
| `tma4105_2017k.pdf` | `d06b15acdafc2b5818b5eba626c69598ee0e8dc237f07cbc754aef9872e748f7` |
| `tma4105_2017v.pdf` | `da083f1d66efa2ad8c12c776b7ae69b207c0679bf8691c39bc6302e5f0f4bdd7` |
| `tma4105_2018k.pdf` | `7f43ca485484464f00db8f35bbab4572b723c480ead5ddd501a2b752c6af224b` |
| `tma4105_2018v.pdf` | `cda3048544f792ca1e9bf7bcd0c6f7530e64f5a61374088236c9898b0f0d898a` |
| `tma4105_2019k_web.pdf` | `f39f5108232e371d7fa7be80f46b261d3b007d78d67d621acd5f1fcf7117ec1f` |
| `tma4105_2019v.pdf` | `1105a57ee6f1bf2513f84145a9b48dcf1032b6632188798ac5c9b383369ec8be` |
| `tma4105_2020k.pdf` | `127a89e8895d3499c0904f52e0f1e709b85592c3cc16a4e7274cef72dca34cc8` |
| `tma4105_2020v.pdf` | `6634be529c97d0695407336ca6e4ebeecf6c04d2a0d44416eb885243680fa560` |
| `tma4105_2021k.pdf` | `8fd81c636470be45a44453674ca9b564ea4d0b6984cd561a6cfd444c3d0fb4c9` |
| `tma4105_2021v.pdf` | `f4636f0b6a800ae2afa49179de28e69ec1b89bfbaef88638c09ea2cec87d5b11` |
| `tma4105_2022k.pdf` | `e8bc123011da3d081670cd3af5a1a91cccd7e9903f8a80f03a05ac7f47db9f97` |
| `tma4105_2022v.pdf` | `b40a7f722eb264d72d3b0376b7eabf0bf31ff023bef1d0c2c6d199f17628b7de` |
| `tma4105_2023k.pdf` | `a689c84aae2f631160e6673fb6a3eecd5f556fad02e571584a3292a8a8e42155` |
| `tma4105_2023v.pdf` | `8ee98bca3cb33888354770c85915a78743b211ffa602ffbd3b85170266ea7b06` |
| `tma4105_2024k.pdf` | `1c79fc7d82e39c1b58aa13d523f4f106d52f825f4ac52c8731544e2d93a6b493` |
| `tma4105_2024v.pdf` | `d4776e9331934191c825c1a980b5e418e659ecccc671b4a185f71187d4a4ecc4` |
| `tma4105_2025k.pdf` | `acee7d0bc67fed6b23a8d7142a74ed98ea80a1d0b03b1109588146ba9892847d` |
| `tma4105_2025v.pdf` | `9fc6d7fc172cf934fe5b3b3fe3c595cb974f7923a31041bfe4950ae45f8b1758` |
| `tma4105_2026v.pdf` | `b5468a59e888f94895e410e428a3b9688d955ec8c2c9b1305e6fd1c72327fdb4` |
