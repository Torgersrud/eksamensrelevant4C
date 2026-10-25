#!/usr/bin/env python3
"""check_repo.py — eksamensrelevant4C sin validator og indeks-generator.

Bruk:
    python3 scripts/check_repo.py check [REPO]   # sjekker alle invarianter (exit 0 = grønt)
    python3 scripts/check_repo.py index [REPO]   # regenererer INDEX.md-er + README-tabellen

REPO er repo-rota; standard er rota denne skripten ligger i.
Bare standardbibliotek. Test-sam: scripts/test_check_repo.py (CLI-en aleine).
"""
import csv
import hashlib
import re
import sys
from pathlib import Path

# Emneknutepunkten — vedtatt taxonomy (uke 34–46 i TMA4432-pensumsplanen).
TAXONOMY = [
    "Uke 34 - SVD",
    "Uke 35 - Tensors and Tensor Decomposition",
    "Uke 36 - Parametrised Curves and Surfaces",
    "Uke 37 - Vector Functions I",
    "Uke 38 - Vector Functions II (Optimization)",
    "Uke 39 - Fourier Series I",
    "Uke 40 - Fourier Series II",
    "Uke 41 - DFT, FFT and Fourier Transform",
    "Uke 42 - PDE I",
    "Uke 43 - PDE II",
    "Uke 44 - PDE III",
    "Uke 45 - Polynomial, Spline and Bézier Approximation",
    "Uke 46 - Least Squares",
]

TELL_START = "<!-- TELL-TABELL:START -->"
TELL_SLUTT = "<!-- TELL-TABELL:SLUTT -->"

NAME_RE = re.compile(
    r"(?P<year>\d{4})-(?P<term>host|var|kont|sommer|test)-(?P<tag>4N|4D|LM|M3|4C)"
    r"(?P<los>-losning)?(?:_dup(?P<dup>[1-9][0-9]*))?"
    r"_(?P<word>problem|oppgave)(?P<num>[1-9][0-9]*)\.md$"
)
SYN_PREFIX = "synthetic-"

MANIFEST_KOLONNER = ["course", "year", "term", "set_type", "filename",
                     "url", "sha256", "solved"]


def uke_av(mappenavn):
    return int(re.match(r"Uke (\d+)", mappenavn).group(1))


def md_filer(mappe):
    return sorted(p for p in mappe.glob("*.md") if p.name != "INDEX.md")


def les_manifest(repo):
    """{filename: rad} — trygt å kalle bare når fila finnes."""
    with open(repo / "sources" / "MANIFEST.csv", newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if reader.fieldnames != MANIFEST_KOLONNER:
            raise ValueError(f"MANIFEST.csv má hoduvekkene {MANIFEST_KOLONNER}, ikk {reader.fieldnames}")
        rader = {}
        for rad in reader:
            rader[rad["filename"]] = rad
        return rader


def fil_info(navn):
    """Parser filnamn -> dict, eller None. synthetic- merkes; resten follows NAME_RE."""
    synt = navn.startswith(SYN_PREFIX)
    m = NAME_RE.match(navn[len(SYN_PREFIX):] if synt else navn)
    if not m:
        return None
    return {"syntetisk": synt, "losning": m["los"] is not None,
            "dup": int(m["dup"]) if m["dup"] else None,
            "mester_navn": navn.replace(f"_dup{m['dup']}_", "_", 1) if m["dup"] else navn,
            "year": m["year"], "term": m["term"], "tag": m["tag"],
            "word": m["word"], "num": int(m["num"])}


# ---------- indeksering ----------

def indekstabel(mappe):
    rader = []
    for p in md_filer(mappe):
        info = fil_info(p.name)
        if info and not info["losning"]:
            sosa = losningsvenn(p.name)
            losning = f"[{sosa}]({sosa})" if sosa and (mappe / sosa).exists() else "–"
        elif info and info["losning"]:
            losning = "(løsningsfil)"
        else:
            losning = "–"
        rader.append(f"| [{p.name}]({p.name}) | {kildesett_celle(p)} | {oppgave_celle(p, info)} | {losning} |")
    header = ("# " + mappe.name + "\n\n"
              "Autogenerert av `python3 scripts/check_repo.py index` — ikkje rediger for hand.\n\n"
              "| Fil | Kildesett | Oppgave | Løsningsfil |\n|---|---|---|---|\n")
    kropp = "\n".join(rader) if rader else "*Tom for Oppgaver ena.*"
    return header + kropp + "\n"


def losningsvenn(navn):
    """Navnet losningsvenninna má ha, eller None for losningsfiler sjolve."""
    m = NAME_RE.match(navn[len(SYN_PREFIX):] if navn.startswith(SYN_PREFIX) else navn)
    if not m or m["los"]:
        return None
    v = navn.replace(f"-{m['tag']}", f"-{m['tag']}-losning", 1)
    return v


FOT_RE = re.compile(r"^Kildesett:((?:\s+[a-z_]+=\S+)+)\s*$")


def les_footer(p):
    """Siste ickje-tomme linje -> {key: value} eller None."""
    for linje in reversed(p.read_text(encoding="utf-8").splitlines()):
        if linje.strip():
            m = FOT_RE.match(linje.strip())
            if not m:
                return None
            return dict(tok.split("=", 1) for tok in m.group(1).split())
    return None


def kildesett_celle(p):
    f = les_footer(p)
    if not f:
        return "–"
    return f"{f.get('course', '?')} · {f.get('term', '?')} {f.get('year', '?')}"


def oppgave_celle(p, info):
    f = les_footer(p)
    word = info["word"] if info else "oppgave"
    num = info["num"] if info else "?"
    cell = f"{word} {num}"
    if f and f.get("points"):
        cell += f" ({f['points']} p)"
    return cell


def generer_index(repo):
    for mappenavn in TAXONOMY:
        mappe = repo / "oppgaver" / mappenavn
        if not mappe.is_dir():
            continue
        (mappe / "INDEX.md").write_text(indekstabel(mappe), encoding="utf-8")
    oppdater_tell_tabell(repo)


def tell_tabell(repo):
    linjer = ["| Uke | Emneknutepunkt | Oppgaver | Løsningsfiler |", "|---|---|---|---|"]
    tot_o = tot_l = 0
    for mappenavn in TAXONOMY:
        mappe = repo / "oppgaver" / mappenavn
        filer = md_filer(mappe) if mappe.is_dir() else []
        infoar = [fil_info(p.name) for p in filer]
        o = sum(1 for i in infoar if i and not i["losning"])
        l = sum(1 for i in infoar if i and i["losning"])
        tot_o += o
        tot_l += l
        uke = uke_av(mappenavn)
        emne = mappenavn.split(" - ", 1)[1]
        lenke = "oppgaver/" + mappenavn.replace(" ", "%20") + "/INDEX.md"
        linjer.append(f"| {uke} | [{emne}]({lenke}) | {o} | {l} |")
    linjer.append(f"| **Sum** | | {tot_o} | {tot_l} |")
    return "\n".join(linjer) + "\n"


def oppdater_tell_tabell(repo):
    readme = repo / "README.md"
    tekst = readme.read_text(encoding="utf-8")
    if TELL_START not in tekst or TELL_SLUTT not in tekst:
        raise SystemExit("README.md manglar TELL-TABELL-sentinelane — index-standen kan ikkje skrivast")
    forv, rest = tekst.split(TELL_START, 1)
    bak = TELL_SLUTT + rest.split(TELL_SLUTT, 1)[1]
    readme.write_text(forv + TELL_START + "\n" + tell_tabell(repo) + bak, encoding="utf-8")


# ---------- sjekk ----------

def sjekk(repo):
    """Returnerer lista av krenskel (klasse, fil, melding)."""
    krenske = []
    oppgaver = repo / "oppgaver"
    lovlege = set(TAXONOMY)
    if not oppgaver.is_dir():
        return [("TAXONOMI", "oppgaver/", "manglar heilt")]
    for mappe in sorted(oppgaver.iterdir()):
        if mappe.name in lovlege:
            continue
        if mappe.is_dir():
            krenske.append(("TAXONOMI", f"oppgaver/{mappe.name}/",
                            "ikkje ein av dei 13 vedtekne Emneknutepunkta"))
        else:
            krenske.append(("TAXONOMI", f"oppgaver/{mappe.name}",
                            "fil ligg laus i oppgaver/, skal vera i Emneknutepunkt-mappe"))
    for mappenavn in TAXONOMY:
        if not (oppgaver / mappenavn).is_dir():
            krenske.append(("TAXONOMI", f"oppgaver/{mappenavn}/", "vedteken mappe manglar"))
    for mappenavn in TAXONOMY:
        mappe = oppgaver / mappenavn
        if not mappe.is_dir():
            continue
        for p in md_filer(mappe):
            if fil_info(p.name) is None:
                krenske.append(("FILGRAMMATIKK", f"oppgaver/{mappenavn}/{p.name}",
                                "fylgjer ikkje <year>-<term>-<tag>[-losning][_dupN]_problem|oppgave<N>.md"
                                " (evt. med synthetic- framfor)"))
    krenske += sjekk_fotspor(repo)
    krenske += sjekk_duplikat(repo)
    krenske += sjekk_losning(repo)
    krenske += sjekk_sha256(repo)
    krenske += sjekk_indeksar(repo)
    krenske += sjekk_readme(repo)
    return krenske


def manifest_hvis_finst(repo):
    """{filename: rad}, eller None om sources/MANIFEST.csv manglar."""
    manifestfil = repo / "sources" / "MANIFEST.csv"
    if not manifestfil.is_file():
        return None
    return les_manifest(repo)


def sjekk_losning(repo):
    """-losning-filer far berre eksistere for Kildesetter manifestet seier er losde."""
    krenske = []
    manifest = manifest_hvis_finst(repo)
    if manifest is None:
        return []  # manifest-mangel allereie meldt av FOTSPOR
    for mappenavn in TAXONOMY:
        mappe = repo / "oppgaver" / mappenavn
        if not mappe.is_dir():
            continue
        for p in md_filer(mappe):
            info = fil_info(p.name)
            if info is None or info["syntetisk"] or not info["losning"]:
                continue
            fot = les_footer(p)
            if not fot or "file" not in fot:
                continue  # meldt av FOTSPOR
            rad = manifest.get(fot["file"])
            if rad is not None and rad["solved"].strip().lower() != "yes":
                krenske.append(("LOSNING_ULOST", f"oppgaver/{mappenavn}/{p.name}",
                                f"Kildesett {rad['filename']} er notert solved={rad['solved']!r} "
                                "i manifestet — losningsfil forboden"))
    return krenske


def sjekk_sha256(repo):
    """PDF-ar som finst pa disk muste matche manifest-radens sha256."""
    krenske = []
    manifest = manifest_hvis_finst(repo)
    if manifest is None:
        return []
    for filnamn, rad in sorted(manifest.items()):
        pdf = repo / "sources" / filnamn
        if not pdf.is_file():
            continue  # gitignored — mangel er ikkje eit brot
        hash_ = hashlib.sha256(pdf.read_bytes()).hexdigest()
        if hash_ != rad["sha256"].strip().lower():
            krenske.append(("SHA256", f"sources/{filnamn}",
                            "sha256 pa disk stemmer ikkje med manifest-rad"))
    return krenske


def sjekk_indeksar(repo):
    """INDEX.md i kvar mappe muste vera det index-laget skriv i dag, byte for byte."""
    krenske = []
    for mappenavn in TAXONOMY:
        mappe = repo / "oppgaver" / mappenavn
        index = mappe / "INDEX.md"
        if not mappe.is_dir():
            continue  # meldt av TAXONOMI
        merke = f"oppgaver/{mappenavn}/INDEX.md"
        if not index.is_file():
            krenske.append(("INDEX_UTDATERT", merke, "INDEX.md manglar — kor index-laget"))
        elif index.read_text(encoding="utf-8") != indekstabel(mappe):
            krenske.append(("INDEX_UTDATERT", merke, "INDEX.md er ikkje det index-laget genererer"))
    return krenske


def sjekk_readme(repo):
    """Tabellen mellom TELL-TABELL-sentinelane i README.md muste vera fersk."""
    readme = repo / "README.md"
    if not readme.is_file():
        return [("README_UTDATERT", "README.md", "manglar")]
    tekst = readme.read_text(encoding="utf-8")
    if TELL_START not in tekst or TELL_SLUTT not in tekst:
        return [("README_UTDATERT", "README.md", "TELL-TABELL-sentinelane manglar")]
    region = tekst.split(TELL_START, 1)[1].split(TELL_SLUTT, 1)[0]
    if region != "\n" + tell_tabell(repo):
        return [("README_UTDATERT", "README.md",
                 "uke-tabellen er ikkje det index-laget genererer — kor index-laget")]
    return []


# Rekkefølgje innanfor eitt år (RULES DUP-1): terminen sin plass i årssyklusen.
# `kont` tel tidleg (janar-kontinuasjon), `test` (testeksamen) sorterar først.
TERM_SEQ = {"test": 0, "var": 1, "kont": 2, "sommer": 3, "host": 4}


def tidspunkt(info):
    return (int(info["year"]), TERM_SEQ[info["term"]])


def normalisert_tekst(p):
    """Fulltekst for dup-samanlikning (RULES DUP-1): provensfoten utelaten,
    all kvitrydd samankastra, alt i liten bokstav."""
    linjer = p.read_text(encoding="utf-8").splitlines()
    for i in range(len(linjer) - 1, -1, -1):
        if linjer[i].strip():
            if FOT_RE.match(linjer[i].strip()):
                linjer = linjer[:i]
            break
    return re.sub(r"\s+", " ", " ".join(linjer)).casefold().strip()


def tekstmestarar(ikkje_dup, dupfil, dup_info):
    """DUP-1: dei ikkje-dup-filene med normalisert fulltekst identisk med
    dupfila og (year, term-seg) ikkje seinare enn dupet."""
    tekst = normalisert_tekst(dupfil)
    dup_tid = tidspunkt(dup_info)
    return [(p, info) for p, info in ikkje_dup
            if normalisert_tekst(p) == tekst and tidspunkt(info) <= dup_tid]


def sjekk_duplikat(repo):
    """Duplikatreglane, to variantar:
    (a) Same-stem kopiar (plassering i fleire Emneknutepunkt): same namn utan
        _dupN må liggja i mappe med lågare ukenummer enn kopiane, kopiane
        nummarast i stigande uke-rekkefølgje.
    (b) Krysssett-førekomstar (RULES DUP-1): kvar _dupN must løyse til nøyaktig
        éin mester — ei ikkje-dup-fil med normalisert fulltekst (kvitrydd og
        med liten bokstav, provensfoten utelaten) identisk med dupfila si og
        (year, term-seg) ikkje seinare enn dupet. Kopier per mester nummarast
        1..k samanhengande i stigande (year, term-seg)-rekkjefølgje."""
    krenske = []
    alle = []
    for mappenavn in TAXONOMY:
        mappe = repo / "oppgaver" / mappenavn
        if not mappe.is_dir():
            continue
        for p in md_filer(mappe):
            info = fil_info(p.name)
            if info is not None and not info["syntetisk"]:
                alle.append((p, info, uke_av(mappenavn), f"oppgaver/{mappenavn}/{p.name}"))
    ikkje_dup = [(p, info) for p, info, _, _ in alle if info["dup"] is None]
    grupper = {}
    kopiar_per_mester = {}
    for p, info, uke, merke in alle:
        grupper.setdefault(info["mester_navn"], []).append((uke, info["dup"], merke))
        if info["dup"] is None:
            continue
        mestrar = tekstmestarar(ikkje_dup, p, info)
        if len(mestrar) == 1:
            mester_p, mester_info = mestrar[0]
            kopiar_per_mester.setdefault(str(mester_p.resolve()), []).append(
                (tidspunkt(info), p.name, merke))
        elif not mestrar:
            tidlegare = [q for q, qi in ikkje_dup
                         if normalisert_tekst(q) == normalisert_tekst(p)]
            if tidlegare:
                krenske.append(("DUPLIKAT", merke,
                                f"{p.name}: _dup{info['dup']} er tidlegare enn alle like "
                                "mestarførekomstar — tidlegaste førekomst er mester"))
            else:
                krenske.append(("DUPLIKAT", merke,
                                f"{p.name}: _dup{info['dup']} har ingen mester (ingen "
                                "ikkje-dup-fil med same normaliserte fulltekst)"))
        else:
            krenske.append(("DUPLIKAT", merke,
                            f"{p.name}: _dup{info['dup']} har fleire mogelege mestarar "
                            f"({', '.join(sorted(q.name for q, _ in mestrar))}) — "
                            "normalisert fulltekst må vera unik"))
    for kopiar in sorted(kopiar_per_mester.values()):
        for forventa, (tid, navn, merke) in enumerate(sorted(kopiar), 1):
            tal = int(fil_info(navn)["dup"])
            if tal != forventa:
                krenske.append(("DUPLIKAT", merke,
                                f"{navn}: kopiar per mester nummarast 1..k etter "
                                f"(year, term-seg), forventa _dup{forventa}"))
    for navn, forekomstar in sorted(grupper.items()):
        if len({p for _, _, p in forekomstar}) < len(forekomstar):
            krenske.append(("DUPLIKAT", forekomstar[0][2],
                            "same filnamn i fleire mapper utan dup-merke"))
        kopiar = sorted([f for f in forekomstar if f[1] is not None])
        mestrar = [f for f in forekomstar if f[1] is None]
        if not kopiar or not mestrar:
            continue
        mester_uke = min(f[0] for f in mestrar)
        for uke, dup, merke in kopiar:
            if uke <= mester_uke:
                krenske.append(("DUPLIKAT", merke,
                                f"{navn}: tidlegaste førekomst er mester — kopi i uke {uke} "
                                f"føre mesteren i uke {mester_uke} er forboden"))
        for forventa, (uke, dup, merke) in enumerate(sorted(kopiar, key=lambda f: f[0]), 1):
            if dup != forventa:
                krenske.append(("DUPLIKAT", merke,
                                f"{navn}: kopier nummarast etter uke-rekkefølgje, forventa _dup{forventa}"))
    return krenske


FOT_KRAVT = ["course", "term", "year", "problem", "file"]
FOT_LOVLEG = set(FOT_KRAVT) | {"points"}


def sjekk_fotspor(repo):
    """Provensfoten má finst, kunna lesast og løyse til ei manifest-rad."""
    krenske = []
    manifestfil = repo / "sources" / "MANIFEST.csv"
    manifest = {}
    if manifestfil.is_file():
        manifest = les_manifest(repo)
    else:
        return [("FOTSPOR", "sources/MANIFEST.csv", "manifestet manglar")]
    for mappenavn in TAXONOMY:
        mappe = repo / "oppgaver" / mappenavn
        if not mappe.is_dir():
            continue
        for p in md_filer(mappe):
            info = fil_info(p.name)
            if info is None or info["syntetisk"]:
                continue  # syntetiske filer er unntatt manifestkravet
            merke = f"oppgaver/{mappenavn}/{p.name}"
            fot = les_footer(p)
            if fot is None:
                krenske.append(("FOTSPOR", merke,
                                "provensfot (siste linje) manglar eller er ikkje til å lesa"))
                continue
            ukjende = set(fot) - FOT_LOVLEG
            manglande = [k for k in FOT_KRAVT if k not in fot]
            if ukjende or manglande:
                krenske.append(("FOTSPOR", merke,
                                f"provensfot har nøklar {sorted(ukjende)} / manglar {sorted(manglande)}"))
                continue
            rad = manifest.get(fot["file"])
            if rad is None:
                krenske.append(("FOTSPOR", merke,
                                f"foten peikar på {fot['file']!r} som ikkje er noka Kildesett-rad i manifestet"))
                continue
            for felt in ("course", "term", "year"):
                if fot[felt] != rad[felt]:
                    krenske.append(("FOTSPOR", merke,
                                    f"fotens {felt}={fot[felt]!r} stemmer ikkje med manifest-rad {rad[felt]!r}"))
            if fot["year"] != info["year"] or fot["term"] != info["term"]:
                krenske.append(("FOTSPOR", merke,
                                "fotens year/term stemmer ikkje med filnamnet"))
            if fot["problem"] != str(info["num"]):
                krenske.append(("FOTSPOR", merke,
                                "fotens problem-nummer stemmer ikkje med filnamnet"))
    return krenske


def main(argv):
    args = argv[1:]
    if not args or args[0] not in ("check", "index") or len(args) > 2:
        print("bruk: python3 scripts/check_repo.py check [REPO]   # porten, exit 0 = grønt\n"
              "      python3 scripts/check_repo.py index [REPO]   # regenererer INDEX.md-er + README-tabellen",
              file=sys.stderr)
        return 2
    mode = args[0]
    repo = Path(args[1]).resolve() if len(args) == 2 else Path(__file__).resolve().parent.parent
    if mode == "index":
        generer_index(repo)
        print(f"index: {len(TAXONOMY)} mapper + README-tabell regenerert")
        return 0
    krenske = sjekk(repo)
    for klasse, fil, melding in sorted(krenske):
        print(f"{klasse}: {fil}: {melding}")
    if krenske:
        print(f"FEIL: {len(krenske)} krenskel")
        return 1
    print("OK: alle invarianter halde")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
