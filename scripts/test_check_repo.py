#!/usr/bin/env python3
"""Fixture-test for the repository validator scripts/check_repo.py.

Run: python3 scripts/test_check_repo.py   (from the repo root)

Seam under test: the validator CLI ONLY. We generate temp mini-repos, run
`check_repo.py check|index <repo>` as a subprocess and assert external
behaviour: exit code plus named violation classes in the report. Nothing
about internals. Fake PDFs are dummy bytes with known sha256 — no network.

Violation classes (from the spec): TAXONOMI, FILGRAMMATIKK, FOTSPOR,
DUPLIKAT, LOSNING_ULOST, ORPA, INDEX_UTDATERT, README_UTDATERT, SHA256.
"""
import hashlib
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
CHECK_REPO = HERE / "check_repo.py"

# The folder taxonomy is spec law (ticket 01 Implementation Decisions + the
# TMA4432 lecture plan), restated here independently of the implementation.
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

MANIFEST_HEADER = "course,year,term,set_type,filename,url,sha256,solved"
README_TEXT = """# testrepo

<!-- TELL-TABELL:START -->
| Uke | Emneknutepunkt | Oppgaver | Løsningsfiler |
|---|---|---|---|
<!-- TELL-TABELL:SLUTT -->
"""

PDF_TEST = b"fake-kildesett: official 4C test exam\n"
PDF_4D = b"fake-kildesett: 4D host 2019\n"
PDF_4D_VAR = b"fake-kildesett: 4D var 2019\n"
PDF_4D_KONT22 = b"fake-kildesett: 4D kont 2022 (aug-resit 4D-fil)\n"
PDF_4N_SOMMER22 = b"fake-kildesett: 4N sommer 2022 (aug-resit 4N-fil)\n"
PDF_M2_KONT23 = b"fake-kildesett: M2 kont 2023 (TMA4105 aug-resit)\n"
PDF_M2_HOST24 = b"fake-kildesett: M2 host 2024 (TMA4105 eksamen, unsolved)\n"


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def footer(course, term, year, problem, pdf, points=None):
    pts = f" points={points}" if points is not None else ""
    return (f"Kildesett: course={course} term={term} year={year} "
            f"problem={problem}{pts} file={pdf}\n")


def run_cli(mode, repo):
    return subprocess.run([sys.executable, str(CHECK_REPO), mode, str(repo)],
                          capture_output=True, text=True)


def make_repo(root: Path):
    """Generate a fully valid mini-repo (indexes/table not yet generated)."""
    for folder in TAXONOMY:
        (root / "oppgaver" / folder).mkdir(parents=True)
    sources = root / "sources"
    sources.mkdir()
    (sources / "testexam.pdf").write_bytes(PDF_TEST)
    (sources / "4d2019host.pdf").write_bytes(PDF_4D)
    (sources / "4d2019var.pdf").write_bytes(PDF_4D_VAR)
    (sources / "4d2022kont.pdf").write_bytes(PDF_4D_KONT22)
    (sources / "4n2022sommer.pdf").write_bytes(PDF_4N_SOMMER22)
    (sources / "m22023kont.pdf").write_bytes(PDF_M2_KONT23)
    (sources / "m22024host.pdf").write_bytes(PDF_M2_HOST24)
    (sources / "MANIFEST.csv").write_text(
        MANIFEST_HEADER + "\n"
        f"TMA4432,2026,test,test,testexam.pdf,https://example.test/testexam.pdf,{sha(PDF_TEST)},yes\n"
        f"TMA4135,2019,host,eksamen,4d2019host.pdf,https://example.test/4d2019host.pdf,{sha(PDF_4D)},no\n"
        f"TMA4135,2019,var,eksamen,4d2019var.pdf,https://example.test/4d2019var.pdf,{sha(PDF_4D_VAR)},no\n"
        f"TMA4135,2022,kont,kont,4d2022kont.pdf,https://example.test/4d2022kont.pdf,{sha(PDF_4D_KONT22)},yes\n"
        f"TMA4135,2022,sommer,kont,4n2022sommer.pdf,https://example.test/4n2022sommer.pdf,{sha(PDF_4N_SOMMER22)},yes\n"
        f"TMA4105,2023,kont,kont,m22023kont.pdf,https://example.test/m22023kont.pdf,{sha(PDF_M2_KONT23)},yes\n"
        f"TMA4105,2024,host,eksamen,m22024host.pdf,https://example.test/m22024host.pdf,{sha(PDF_M2_HOST24)},no\n",
        encoding="utf-8")
    readme = root / "README.md"
    readme.write_text(README_TEXT, encoding="utf-8")
    write_problem_files(root)


def write_problem_files(root: Path):
    p1 = root / "oppgaver" / "Uke 34 - SVD" / "2026-test-4C_problem1.md"
    p1.write_text("### **Problem 1** (Moore-Penrose inverse, 10 points)\n\nConsider the matrix ...\n\n"
                  + footer("TMA4432", "test", "2026", "1", "testexam.pdf", 10), encoding="utf-8")
    l1 = root / "oppgaver" / "Uke 34 - SVD" / "2026-test-4C-losning_problem1.md"
    l1.write_text("### **Solution to Problem 1**\n\na) We use the smaller matrix ...\n\n"
                  + footer("TMA4432", "test", "2026", "1", "testexam.pdf", 10), encoding="utf-8")
    p2 = root / "oppgaver" / "Uke 46 - Least Squares" / "2019-host-4D_oppgave5.md"
    p2.write_text("### **Oppgave 5** Minste kvadraters metode\n\n...\n\n"
                  + footer("TMA4135", "host", "2019", "5", "4d2019host.pdf"), encoding="utf-8")


class ValidatorTestCase(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self._tmp.cleanup)
        self.repo = Path(self._tmp.name) / "repo"
        make_repo(self.repo)
        idx = run_cli("index", self.repo)
        self.assertEqual(idx.returncode, 0, msg=idx.stdout + idx.stderr)

    def check(self):
        return run_cli("check", self.repo)

    def index(self):
        res = run_cli("index", self.repo)
        self.assertEqual(res.returncode, 0, msg=res.stdout + res.stderr)

    def assertViolates(self, cls):
        res = self.check()
        self.assertNotEqual(res.returncode, 0,
                            msg=f"expected nonzero exit, report:\n{res.stdout}")
        self.assertIn(cls, res.stdout,
                      msg=f"report must name {cls}, got:\n{res.stdout}")

    def assertOk(self):
        res = self.check()
        self.assertEqual(res.returncode, 0, msg=res.stdout + res.stderr)


class TestValidRepo(ValidatorTestCase):
    def test_valid_repo_exits_zero(self):
        self.assertOk()


class TestTaxonomy(ValidatorTestCase):
    def test_unknown_folder_names_taxonomy(self):
        stygt = self.repo / "oppgaver" / "Uke 47 - Repetition"
        stygt.mkdir()
        (stygt / "2026-test-4C_oppgave1.md").write_text(
            "x\n\n" + footer("TMA4432", "test", "2026", "1", "testexam.pdf"),
            encoding="utf-8")
        self.assertViolates("TAXONOMI")

    def test_missing_folder_names_taxonomy(self):
        import shutil
        shutil.rmtree(self.repo / "oppgaver" / "Uke 44 - PDE III")
        self.assertViolates("TAXONOMI")


class TestFilnavnGrammatikk(ValidatorTestCase):
    def test_bad_term_and_tag_names_filgrammatikk(self):
        stygt = self.repo / "oppgaver" / "Uke 39 - Fourier Series I"
        (stygt / "2019-vinter-4X_oppgave3.md").write_text(
            "x\n\n" + footer("TMA4135", "host", "2019", "3", "4d2019host.pdf"),
            encoding="utf-8")
        self.assertViolates("FILGRAMMATIKK")

    def test_underscore_before_number_names_filgrammatikk(self):
        # 3C ended up with drift like _oppgave_3; the grammar forbids it.
        (self.repo / "oppgaver" / "Uke 39 - Fourier Series I" / "2019-host-4D_oppgave_3.md").write_text(
            "x\n\n" + footer("TMA4135", "host", "2019", "3", "4d2019host.pdf"),
            encoding="utf-8")
        self.assertViolates("FILGRAMMATIKK")

    def test_set_letter_after_term_is_valid(self):
        # Two Kildesetter i same år+term (t.d. to sensensurar): den andre
        # får ein liten bokstav etter terminen.
        (self.repo / "oppgaver" / "Uke 39 - Fourier Series I" / "2022-kont-b-4D_oppgave7.md").write_text(
            "yy\n\n" + footer("TMA4135", "kont", "2022", "7", "4d2022kont.pdf"),
            encoding="utf-8")
        self.index()
        self.assertOk()

    def test_two_letter_set_names_filgrammatikk(self):
        (self.repo / "oppgaver" / "Uke 39 - Fourier Series I" / "2022-kont-bb-4D_oppgave7.md").write_text(
            "yy\n\n" + footer("TMA4135", "kont", "2022", "7", "4d2022kont.pdf"),
            encoding="utf-8")
        self.assertViolates("FILGRAMMATIKK")

    def test_M2_tag_is_valid(self):
        # Corpus extension (ADR 0004): the tag vocabulary gains M2 for the
        # TMA4105 Matematikk 2 Kildesetter.
        (self.repo / "oppgaver" / "Uke 36 - Parametrised Curves and Surfaces" /
         "2023-kont-M2_oppgave4.md").write_text(
            "x\n\n" + footer("TMA4105", "kont", "2023", "4", "m22023kont.pdf"),
            encoding="utf-8")
        self.index()
        self.assertOk()

    def test_unknown_tag_still_names_filgrammatikk(self):
        # M2 enters the tag vocabulary; nothing else does. An invented tag
        # must stay rejected.
        (self.repo / "oppgaver" / "Uke 36 - Parametrised Curves and Surfaces" /
         "2023-kont-XX_oppgave4.md").write_text(
            "x\n\n" + footer("TMA4105", "kont", "2023", "4", "m22023kont.pdf"),
            encoding="utf-8")
        self.assertViolates("FILGRAMMATIKK")


class TestProvensfot(ValidatorTestCase):
    def test_missing_footer_names_fotspor(self):
        (self.repo / "oppgaver" / "Uke 42 - PDE I" / "2019-host-4D_oppgave2.md").write_text(
            "### **Oppgave 2**\n\nuansynleg tekst utan fot\n", encoding="utf-8")
        self.assertViolates("FOTSPOR")

    def test_footer_to_unmanifested_pdf_names_fotspor(self):
        (self.repo / "oppgaver" / "Uke 42 - PDE I" / "2019-host-4D_oppgave2.md").write_text(
            "x\n\n" + footer("TMA4135", "host", "2019", "2", "spokelse.pdf"), encoding="utf-8")
        self.assertViolates("FOTSPOR")

    def test_footer_year_not_in_manifest_names_fotspor(self):
        # Same PDF name, but the row in the manifest is for another year.
        (self.repo / "oppgaver" / "Uke 42 - PDE I" / "2019-host-4D_oppgave2.md").write_text(
            "x\n\n" + footer("TMA4135", "host", "2018", "2", "4d2019host.pdf"), encoding="utf-8")
        self.assertViolates("FOTSPOR")


class TestSyntetisk(ValidatorTestCase):
    """ADR 0002: synthetic- first in the name => exempt from the manifest,
    but year/term/tag within the allowed value sets are still required."""

    def test_synthetic_without_footer_is_valid(self):
        (self.repo / "oppgaver" / "Uke 35 - Tensors and Tensor Decomposition" /
         "synthetic-2026-test-4C_oppgave1.md").write_text(
            "### **Oppgave 1** (CP-dekomposisjon)\n\n...\n", encoding="utf-8")
        # Production stems (ticket 27 rename): same exemption for the -host- stem.
        (self.repo / "oppgaver" / "Uke 35 - Tensors and Tensor Decomposition" /
         "synthetic-2026-host-4C_oppgave2.md").write_text(
            "### **Oppgave 2** (TUCKER)\n\n...\n", encoding="utf-8")
        self.index()
        self.assertOk()

    def test_synthetic_losning_without_manifest_is_valid(self):
        mappe = self.repo / "oppgaver" / "Uke 45 - Polynomial, Spline and Bézier Approximation"
        (mappe / "synthetic-2026-test-4C_oppgave1.md").write_text("x\n", encoding="utf-8")
        (mappe / "synthetic-2026-test-4C-losning_oppgave1.md").write_text("x\n", encoding="utf-8")
        self.index()
        self.assertOk()

    def test_malformed_synthetic_name_names_filgrammatikk(self):
        # Prefix present but no <year>-<term>-<tag> stem behind it.
        (self.repo / "oppgaver" / "Uke 35 - Tensors and Tensor Decomposition" /
         "synthetic-oppgave1.md").write_text("x\n", encoding="utf-8")
        self.assertViolates("FILGRAMMATIKK")


class TestDuplikat(ValidatorTestCase):
    """A Duplikat is the same problem placed in an additional Emneknutepunkt:
    the master (file without _dupN) sits in the lowest-numbered week, copies
    are numbered in ascending week order."""

    def master(self):
        return (self.repo / "oppgaver" / "Uke 39 - Fourier Series I" /
                "2019-host-4D_oppgave3.md")

    def dup(self, folder, n=1):
        suffix = f"_dup{n}" if n else ""
        return (self.repo / "oppgaver" / folder /
                f"2019-host-4D{suffix}_oppgave3.md")

    def test_valid_dup_pair_across_folders_is_valid(self):
        self.master().write_text("x\n\n" + footer("TMA4135", "host", "2019", "3", "4d2019host.pdf"),
                                 encoding="utf-8")
        self.dup("Uke 41 - DFT, FFT and Fourier Transform").write_text(
            "x\n\n" + footer("TMA4135", "host", "2019", "3", "4d2019host.pdf"), encoding="utf-8")
        self.index()
        self.assertOk()

    def test_dup_without_master_names_duplikat(self):
        self.dup("Uke 41 - DFT, FFT and Fourier Transform", n=2).write_text(
            "x\n\n" + footer("TMA4135", "host", "2019", "3", "4d2019host.pdf"), encoding="utf-8")
        self.assertViolates("DUPLIKAT")

    def test_dup_in_earlier_folder_than_master_names_duplikat(self):
        # Earliest occurrence is master: a copy may not precede its master.
        self.master().write_text("x\n\n" + footer("TMA4135", "host", "2019", "3", "4d2019host.pdf"),
                                 encoding="utf-8")
        self.dup("Uke 36 - Parametrised Curves and Surfaces").write_text(
            "x\n\n" + footer("TMA4135", "host", "2019", "3", "4d2019host.pdf"), encoding="utf-8")
        self.assertViolates("DUPLIKAT")


class TestDuplikatPaaTversAvSett(ValidatorTestCase):
    """RULES DUP-1: a later occurrence of an identical problem from ANOTHER
    Kildesett (e.g. a shared 4N/4D exam re-published under 4N) is a Duplikat
    on its OWN stem: the master is the non-dup file whose normalized full
    text (whitespace/case-insensitive, proven footer excluded) is identical,
    with (year, term-seq) not later than the dup's. The stems may differ
    entirely (cross-tag: 4D-tagged master, 4N-tagged dup)."""

    MAPPE = "Uke 40 - Fourier Series II"
    TEKST = ("### **Oppgave 8** Delte fellestonar\n\n"
             "Grensene for den felles eksamensfila er gjevne.\n")

    def fil(self, navn, tekst, problem="8", pdf="4d2019host.pdf"):
        (self.repo / "oppgaver" / self.MAPPE / navn).write_text(
            tekst + "\n" + footer("TMA4135", self.term_av(navn), self.year_av(navn),
                                  problem, pdf),
            encoding="utf-8")

    @staticmethod
    def term_av(navn):
        return navn.split("-")[1]

    @staticmethod
    def year_av(navn):
        return navn.split("-")[0]

    def test_kryss_tag_dup_mot_4d_mester_er_gyldig(self):
        # 4D master from the 2019 exam, 4N-tagged dup of the shared sitting.
        self.fil("2019-host-4D_oppgave8.md", self.TEKST)
        self.fil("2019-host-4N_dup1_oppgave8.md", self.TEKST)
        self.index()
        self.assertOk()

    def test_dup_tidlegare_enn_mester_names_duplikat(self):
        # The var sitting (term-seq earlier in 2019) cannot be a dup of the
        # later host exam: the earliest identical occurrence is the master.
        self.fil("2019-host-4D_oppgave8.md", self.TEKST)
        self.fil("2019-var-4N_dup1_oppgave8.md", self.TEKST, pdf="4d2019var.pdf")
        self.index()
        self.assertViolates("DUPLIKAT")

    def test_kont_mester_sommer_dup_er_gyldig(self):
        # RULES DUP-1 item 2 verbatim (the shared August-2022 resit case):
        # master `2022-kont-4D_problemN`, dup `2022-sommer-4D_dup1_problemN`.
        self.fil("2022-kont-4D_problem1.md", self.TEKST, problem="1", pdf="4d2022kont.pdf")
        self.fil("2022-sommer-4D_dup1_problem1.md", self.TEKST, problem="1",
                 pdf="4n2022sommer.pdf")
        self.index()
        self.assertOk()

    def test_kopiar_nummarast_etter_term_rekkje(self):
        # Two dups of the 2019 host master in 2022: kont (seq 2) comes before
        # sommer (seq 3), so kont must be _dup1 and sommer _dup2.
        self.fil("2019-host-4D_oppgave8.md", self.TEKST)
        (self.repo / "oppgaver" / self.MAPPE / "2022-kont-4N_dup2_oppgave8.md").write_text(
            self.TEKST + "\n" + footer("TMA4135", "kont", "2022", "8", "4d2022kont.pdf"),
            encoding="utf-8")
        (self.repo / "oppgaver" / self.MAPPE / "2022-sommer-4N_dup1_oppgave8.md").write_text(
            self.TEKST + "\n" + footer("TMA4135", "sommer", "2022", "8", "4n2022sommer.pdf"),
            encoding="utf-8")
        self.index()
        self.assertViolates("DUPLIKAT")

    def test_to_kopiar_av_same_mester_1_2_er_gyldig(self):
        # Same pair, correctly numbered: kont _dup1, sommer _dup2.
        self.fil("2019-host-4D_oppgave8.md", self.TEKST)
        (self.repo / "oppgaver" / self.MAPPE / "2022-kont-4N_dup1_oppgave8.md").write_text(
            self.TEKST + "\n" + footer("TMA4135", "kont", "2022", "8", "4d2022kont.pdf"),
            encoding="utf-8")
        (self.repo / "oppgaver" / self.MAPPE / "2022-sommer-4N_dup2_oppgave8.md").write_text(
            self.TEKST + "\n" + footer("TMA4135", "sommer", "2022", "8", "4n2022sommer.pdf"),
            encoding="utf-8")
        self.index()
        self.assertOk()

    def test_dup_utan_noka_mester_names_duplikat(self):
        # A _dupN whose normalized text matches no non-dup file at all has no
        # master to resolve to.
        self.fil("2022-sommer-4N_dup1_oppgave8.md",
                 "### **Oppgave 8** Heilt eineståande tekst\n\nInga anna fil har dette.\n",
                 pdf="4n2022sommer.pdf")
        self.index()
        self.assertViolates("DUPLIKAT")

    def test_dup_med_to_like_mestarar_names_duplikat(self):
        # "Exactly one master": two identical non-dup files make the master
        # ambiguous and must be named.
        self.fil("2022-kont-4D_problem1.md", self.TEKST, problem="1", pdf="4d2022kont.pdf")
        self.fil("2022-sommer-4D_problem1.md", self.TEKST, problem="1", pdf="4n2022sommer.pdf")
        self.fil("2022-sommer-4N_dup1_problem1.md", self.TEKST, problem="1",
                 pdf="4n2022sommer.pdf")
        self.index()
        res = self.check()
        self.assertNotEqual(res.returncode, 0, msg=res.stdout)
        self.assertIn("DUPLIKAT", res.stdout, msg=res.stdout)
        self.assertIn("fleire mogelege mestarar", res.stdout, msg=res.stdout)


class TestLosningPaaLosetSett(ValidatorTestCase):
    def test_losning_on_unsolved_set_names_losning_ulost(self):
        # The fixture's 4D-2019 row is solved=no; its Løsningsfil is therefore illegal.
        (self.repo / "oppgaver" / "Uke 46 - Least Squares" /
         "2019-host-4D-losning_oppgave5.md").write_text(
            "x\n\n" + footer("TMA4135", "host", "2019", "5", "4d2019host.pdf"), encoding="utf-8")
        self.assertViolates("LOSNING_ULOST")

    def test_M2_losning_on_unsolved_set_names_losning_ulost(self):
        # Grammar extension notwithstanding: the fixture's M2-2024 row is
        # solved=no, so an M2-tagged Løsningsfil under it stays illegal.
        (self.repo / "oppgaver" / "Uke 38 - Vector Functions II (Optimization)" /
         "2024-host-M2-losning_oppgave3.md").write_text(
            "x\n\n" + footer("TMA4105", "host", "2024", "3", "m22024host.pdf"), encoding="utf-8")
        self.assertViolates("LOSNING_ULOST")


class TestLosningKrevdOppgave(ValidatorTestCase):
    def test_losning_without_problem_sibling_names_orpa(self):
        # Every Løsningsfil must have its Oppgave-sibling in the same folder —
        # a lone solution PDF transcription is not a browsable problem entry.
        (self.repo / "oppgaver" / "Uke 44 - PDE III" /
         "2022-kont-4D-losning_problem7.md").write_text(
            "x\n\n" + footer("TMA4135", "kont", "2022", "7", "4d2022kont.pdf"), encoding="utf-8")
        self.index()
        self.assertViolates("ORPA")

    def test_losning_with_problem_sibling_is_valid(self):
        mappe = self.repo / "oppgaver" / "Uke 44 - PDE III"
        (mappe / "2022-kont-4D_problem7.md").write_text(
            "x\n\n" + footer("TMA4135", "kont", "2022", "7", "4d2022kont.pdf"), encoding="utf-8")
        (mappe / "2022-kont-4D-losning_problem7.md").write_text(
            "y\n\n" + footer("TMA4135", "kont", "2022", "7", "4d2022kont.pdf"), encoding="utf-8")
        self.index()
        self.assertOk()

    def test_synthetic_M2_losning_without_problem_sibling_names_orpa(self):
        # Unchanged by the grammar extension: also for M2-tagged synthetics a
        # lone Løsningsfil without its Oppgave is named (the pairing rule).
        (self.repo / "oppgaver" / "Uke 36 - Parametrised Curves and Surfaces" /
         "synthetic-2026-test-M2-losning_oppgave2.md").write_text("x\n", encoding="utf-8")
        self.index()
        self.assertViolates("ORPA")


class TestManifestHash(ValidatorTestCase):
    def test_changed_pdf_names_sha256(self):
        (self.repo / "sources" / "4d2019host.pdf").write_bytes(PDF_4D + b"page swapped!\n")
        self.assertViolates("SHA256")


class TestFreshness(ValidatorTestCase):
    def test_planted_file_names_index_utdatert_and_index_mode_repairs(self):
        (self.repo / "oppgaver" / "Uke 40 - Fourier Series II" /
         "2019-host-4D_oppgave2.md").write_text(
            "x\n\n" + footer("TMA4135", "host", "2019", "2", "4d2019host.pdf"), encoding="utf-8")
        self.assertViolates("INDEX_UTDATERT")
        self.index()
        self.assertOk()

    def test_missing_index_file_names_index_utdatert_and_index_mode_repairs(self):
        (self.repo / "oppgaver" / "Uke 43 - PDE II" / "INDEX.md").unlink()
        self.assertViolates("INDEX_UTDATERT")
        self.index()
        self.assertOk()

    def test_edited_readme_count_names_readme_utdatert_and_index_mode_repairs(self):
        readme = self.repo / "README.md"
        tekst = readme.read_text(encoding="utf-8")
        readme.write_text(tekst.replace("| 1 | 1 |", "| 9 | 9 |", 1), encoding="utf-8")
        self.assertViolates("README_UTDATERT")
        self.index()
        self.assertOk()


if __name__ == "__main__":
    unittest.main(verbosity=2)
