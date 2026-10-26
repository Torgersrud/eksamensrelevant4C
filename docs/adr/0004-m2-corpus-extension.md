# ADR 0004: Korpusutviding — TMA4105 Matematikk 2 som sjette kurs

Status: accepted (2026-10-26)

## Sammenheng

ADR 0001 unntok TMA4105 (Matematikk 2) frå korpuset med premissa om at innhaldet deira
var «dekket av henholdsvis 4D- og M3-materialet». Premissa er motbevist. Ein full
gjennomgang av dei ~480 transkriberte Oppgaver viser at ingen av dei fem kursene nokon
gong har prøvd parametrisk kurve- og flateanalyse (uke 36) eller klassisk flervariabel
optimalisering med kritiske punkt, Hessian-test og Lagrange-multiplikatorar (uke 38) som
hovedfag — begge vekene stod med éi oppgåve kvar, båe frå 2026-testeksamen. Samstundes
viser granskinga av kurswikien (docs/research/m2-arkivsurvey.md) at TMA4105 har
publisert to retta eksamenssett årleg sidan 2000 — ordinairexamen om våren og
kontinuasjon («Sommeren») om sommaren, alt med løysingsark — til saman 55 Kildesett
1998–2026. Det er denne brønnen uke 36 og 38 treng.

## Beslutning

TMA4105 Matematikk 2 (fil-tagg `M2`) blir teken opp som det sjette kurset i korpuset.
Filnavnsgrammatikken får `M2`-taggen. Settingene med eldre kurskode frå før 2004 (SIF5005)
kjører inn i manifestet med den kurskoden arket faktisk trykkjer, men får `M2`-tagg i
filnamnet — etter same mønster som ADR 0003 brukte for dei delte 4M/4N-eksamenene.

Denne ADR-en opphevar **berre** unntaksklausulen for TMA4105 i ADR 0001, saman med
premissen om at M2-innholdet var dekt av 4D-/M3-materialet. Elles står ADR 0001 ved lag.
Dei andre kandidatkursa vart vurderte under granskinga og blir verande utanfor; denne
ADR-en fester grunngivingane, slik at den gamle unntaksteksten ikkje kan gjenopplivast:

| Kandidat | Konklusjon ved granskinga |
|---|---|
| TMA4120 (4K) | Eit Fourier/PDE-fag, ikkje vektoranalyse — innhaldet ligg på uke 39–44 og gjev inga etterfylling av uke 36/38 |
| TMA4106 | Vurdert under granskinga — utanfor |
| TMA4180 (Optimering 1) | Algoritmenivå — slår feil på Relevansregel |
| TMA4123 (4M) | Berre numerisk lineæralgebra å hente; reine 4M-eksamenar er allereie utelukka av ADR 0003 |
| TMA4285 | Emnet er Tidsrekkjer (Time Series) |

## Konsekvenser

* Uke 36 og 38 blir trenbare på ekte Kildesett. Haustinga tek alt Relevansregel slepp
  inn — ikkje berre uke 36/38: gradient-/Jacobian-nære M2-oppgåver kan lovleg hamne i
  uke 37. Linje-/flateintegral, fluks og multiple integral blir verande UT (ingen planuke).
* Haustinga følgjer vanleg arbeidsgang (README-kapittelet «Legg til nye Kildesett»):
  nedlasting → sha256 → manifestrad → transkripsjon → index → gate, éin commit per
  Kildesett, rekkjefølgje nyast først (best tekstlag). Nedlastingar frå wikien må gå
  pent for seg — NTNU-dokuwikien blokkerer aggressive klientar.
* Granskinga som dokumenterer arkivet sin faktiske dekning, nedlastingsURL-ar for kvart
  sett og tekstlagkvalitet, ligg som kontekstpeikar for haustingstikkettane i
  docs/research/m2-arkivsurvey.md.
