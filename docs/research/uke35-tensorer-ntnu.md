# Research: Pre-4C NTNU exam sources for TMA4432 "Uke 35 – Tensors and Tensor Decomposition"

> Provenans: utarbeidd 2026-10-26 av research-agenten som bakgrunn for spec-en om å fylle uke 35/36/38 (issue #1); lagd under docs/research/ av ticket 2 på greina `spec/fill-35-36-38`.

Date: 2026-10-26. Method note at bottom. All facts below cite a primary-source URL; quoted snippets were extracted from the cited PDFs/pages themselves.

## Question

Are there NTNU courses (past or present, any code) whose **published exam questions** plausibly contain problems on TMA4432 Matematikk 4C's Uke 35 content: tensor notation (order, modes, fibers/slices), outer products, mode-n products, rank-1 tensors, CP (CANDECOMP/PARAFAC) decomposition, Tucker decomposition, multilinear/k-mode products, tensor applications (compression), and — loosely — advanced SVD / Moore–Penrose material a 4C teacher would count as tensor-adjacent?

Context assumed: the corpus repo mines TMA4125/TMA4130 (4N), TMA4135 (4D), TMA4145 (to ~2022) and TMA4110; tensor content is absent there. TMA4432 itself has only the 2026 test exam.

## Findings

### 1. TMA4432 Matematikk 4C — the course itself (new autumn 2026)

- **Status.** Brand-new course, "New from the academic year 2026/2027", first run H2026 (lecturer Ronny Bergmann). Exam: 24.11.2026, Code D. Course content (authoritative): *"Innføring i metoder for matrise- og tensorfaktorisering. Singulærverdidekomposisjon (SVD), tensorer."* — https://www.ntnu.no/studier/emner/TMA4432/ (EN mirror: https://www.ntnu.edu/studies/courses/TMA4432/). The same page's "course reduction" table shows 4C replaces TMA4130, TMA4135, TMA4125 (and the other old TMA41xx math courses) from Høst 2026.
- **Exact week-35 content.** Lecture plan, "Week 35: Tensors and Tensor Decomposition", keywords: *"Tensor, definition, fibers, slices, and rank" / "Kronecker, Khatri-Rao, and Hadamard matrix products" / "matricization, multilinear transforms, k-mode product" / "Canonical Polyadic and Tucker decomposition"* — https://wiki.math.ntnu.no/tma4432/2026h/lecture_plan . Week 34 is SVD + *"truncated SVD"* + *"the Moore-Penrose inverse"*. Teaching material: `tensor-decompositions.pdf` and `hosvd.ipynb` (https://wiki.math.ntnu.no/_media/tma4432/2026h/tensor-decompositions.pdf), slides `02-tensors-web.pdf`. Text extracted from the notes confirms the terminology (frequency counts in extracted text: "canonical polyadic" ×3, "tucker" ×2, "hosvd" ×2, "khatri-rao" ×3, "slices" ×7).
- **References.** Official course literature is Hole (AH), Quarteroni/Sacco/Saleri *Numerical Mathematics* (QSS), Plonka et al. *Numerical Fourier Analysis* (PPST), Kreyszig — https://wiki.math.ntnu.no/tma4432/2026h/course_information . **None of these books covers tensor decomposition**, so the lecture notes PDF is effectively the pensum text for uke 35. I could NOT find "Kolda" or "Bader" as searchable text in `tensor-decompositions.pdf` or `02-tensors-web.pdf` (checked extracted text and raw PDF bytes) — the user's guess that the Kolda & Bader survey is the cited reference is **unconfirmed** (see Open uncertainties).
- **Transition from old courses.** Lecturer's own "transition" page: *"New topics in Math 4C: … SVD – it might be taught in math courses like TMA 4145 Linear Methods though not explicitly mentioned in the Learning outcomes. **Tensor decomposition**"* and *"Direct predecessors of 4C are TMA4125 Math 4N (Spring), TMA4130 Math 4N (Autumn), TMA4135 Math 4D."* — https://wiki.math.ntnu.no/tma4432/2026h/transition . I.e., official confirmation that no predecessor course taught tensor decomposition.
- **Its own exam pool.** The only 4C exam document that exists is the lecturer's **test exam with solution proposal**, which DOES contain a genuine tensor problem:
  > *"Problem … (Tensor decomposition, … points) Consider a 3-tensor X ∈ R^{I×J×K} … a) How are the Tucker decomposition and the canonical polyadic decomposition of X related? b) How do both decompositions relate to the singular value decomposition (SVD)?"* — followed by a full *"Solution"* deriving Tucker as X ≈ G ×₁ A ×₂ B ×₃ C and CPD as sum of rank-1 terms a_r ∘ b_r ∘ c_r, plus a separate Moore–Penrose problem (*"…the properties of the Moore-Penrose inverse… it suffices to check the two properties A A⁺ = A and (A A⁺)ᵀ = A A⁺"*).
  PDF: https://wiki.math.ntnu.no/_media/tma4432/2026h/test-exam-math4c_web.pdf (announced on https://wiki.math.ntnu.no/tma4432/2026h/exam : *"I prepared a test exam including a solution proposal"*). Problem number/point value were unreadable in text extraction (digit glyph encoding), hence "…".
- **Exercise pool (not exams, but official, public, solved).** Exercise sheets 1–9 with solution PDFs at https://wiki.math.ntnu.no/tma4432/2026h/exercises . Sheet 2 is the tensor one:
  > *"Problem 3. (Tensor matricisation and decomposition …) Consider the tensor X ∈ R^{4×3×2} given by the two frontal slices X::1 = … X::2 = …"* — https://wiki.math.ntnu.no/_media/tma4432/2026h/exercise-sheet2.pdf , solved in https://wiki.math.ntnu.no/_media/tma4432/2026h/exercise-sheet2-sol.pdf .

**Verdict:** the only authentic 4C-level tensor exam problem in the world is the 2026 test exam (plus exercise-sheet problems). Nothing pre-2026 exists for 4C itself.

### 2. TMA4431 Matematikk 4B — the other new tensor course (no exams yet)

Course content (new from 2026/2027, first run **V2027**): *"Videre behandles moderne metoder i maskinlæring, herunder metoder for **matrise- og tensorfaktorisering** og nevrale nettverk."* — https://www.ntnu.no/studier/emner/TMA4431 . **No exam can exist before spring 2027**; nothing to harvest. (4B is the other course in the new family that teaches tensor factorisation.)

### 3. TMA4145 Lineære metoder — the post-2022 gap the corpus missed; SVD-adjacent YES, tensors NO

- **Exam archive (this is the corpus gap: 2023–2025 are published, with solutions).** https://wiki.math.ntnu.no/tma4145/2026h/eksamensoppgaver lists ordinary + continuation exams **2023, 2024, 2025** each with "solution proposal":
  - 2023: https://wiki.math.ntnu.no/_media/tma4145/2023h/lineaere_metoder_h23.pdf + solutions; kont + solutions
  - 2024: https://wiki.math.ntnu.no/_media/tma4145/2024h/lineaere_metoder_h24.pdf + https://wiki.math.ntnu.no/_media/tma4145/2024h/lineaere_metoder_h24_solutions.pdf (+ kont pair)
  - 2025: https://wiki.math.ntnu.no/_media/tma4145/2025h/tma4145_h25.pdf + solutions; kontinuasjon 2026: https://wiki.math.ntnu.no/_media/tma4145/2025h/tma4145_k26.pdf + solutions
- **Tensor verdict: NO.** I downloaded and text-searched h23, h24, h24-solutions, h25, h25-solutions, k26, k26-solutions: **0 occurrences of "tensor"** in all of them. Course content is functional analysis + matrix theory: *"Spectral theorem, Jordan canonical form, and matrix decompositions"* — https://www.ntnu.edu/studies/courses/TMA4145/2025 . No tensor decomposition pensum.
- **SVD/Moore–Penrose adjacency: YES, real headliner problems every year.** Quoted from the PDFs:
  - 2023, Problem 3: *"a) Find the singular value decomposition of the matrix A. b) Find G ∈ R⁴ with AG = b such that ‖G‖₂ is minimal."* (https://wiki.math.ntnu.no/_media/tma4145/2023h/lineaere_metoder_h23.pdf)
  - 2024, Problem 3: *"a) Find the singular value decomposition of the matrix A. b) Find G ∈ R² such that ‖AG − b‖₂ is minimal…"* (https://wiki.math.ntnu.no/_media/tma4145/2024h/lineaere_metoder_h24.pdf)
  - 2025, Problem 1: *"Let A = [[14,23],[32,41]] and b = (1,−1,0,0). a) Find the singular value decomposition of the matrix A. b) Find x ∈ R² such that ‖Ax − b‖₂ is minimal."* (https://wiki.math.ntnu.no/_media/tma4145/2025h/tma4145_h25.pdf)
  These are exactly the truncated-SVD/least-squares/pseudoinverse skills the 4C week-34 material (and the CPD↔SVD link in week 35) leans on. Note the wiki labels the answers "solution proposal" ( løsningsforslag, not official facit).

### 4. 4N/4D exams 2023–2025 (the corpus stops ~2022): still no tensors, no SVD

- From 2023 the old 4D course was folded into the joint 4N/4D course run under **TMA4130** (root page https://wiki.math.ntnu.no/tma4135 cross-references `tma4130:2023h`–`tma4130:2026h`; the wiki page is titled "Math 4N 4D").
- Recent exams with solution proposals, downloaded and text-searched: **0 hits for "tensor" AND 0 hits for "singul|Penrose"** (extraction sanity-checked — the files read as normal exam text):
  - 2025 (4N/4D, "exam with a solution proposal"): https://wiki.math.ntnu.no/_media/tma4130/2025h/exam_math_4n_4d_tma4130_35-21.pdf (page: https://wiki.math.ntnu.no/tma4130/2025h/exam ; re-sit `re-sit_exam_tma41x_05-aug-2026-solutions.pdf` also linked there but not downloaded)
  - 2024: https://wiki.math.ntnu.no/_media/tma4130/2024h/exam_math_4n_4d_tma4130_35-15.pdf (page: https://wiki.math.ntnu.no/tma4130/2024h/exam)
  - 2023: https://wiki.math.ntnu.no/_media/tma4130/2023h/tma4130_2023h_exam-21.pdf (page: https://wiki.math.ntnu.no/tma4130/2023h/exam)
- Old course descriptions for TMA4135/TMA4130/TMA4125 (2025 versions): 0 "tensor" hits (https://www.ntnu.edu/studies/courses/TMA4135/2025 , …/TMA4130/2025 , …/TMA4125/2025). Confirms tensor material was never in 4N/4D pensum — consistent with the lecturer's transition page.

**Verdict:** extending the corpus to 2023–2025 for 4N/4D adds **zero** tensor or SVD problems. The harvest value of the post-2022 extension is negative for uke 35.

### 5. TK8117 Multivariat dataanalyse – videregående emner (kjemometri) — PARAFAC taught, but no written exam exists

- Course content explicitly lists: *"Independent Component Analysis — **PARAFAC**, multiblokk (sensor fusion) og IDLE modellering"* (PARAFAC = the CP decomposition's chemometrics name). https://www.ntnu.no/studier/emner/TK8117 ; EN: https://www.ntnu.edu/studies/courses/TK8117 . Department: Teknisk kybernetikk/kjemometri (ph.d.-level, Frank Westad).
- **Exam verdict: unusable as an exam-question source.** Assessment is *"Muntlig eksamen og arbeider"* (oral exam 70% + project work 30%, Bestått/Ikke bestått) — there is no written eksamensoppgave PDF, and I found no public past-exam archive (no wiki.math page: https://wiki.math.ntnu.no/tk8117 returns 404). Student-created material exists on GitHub (e.g. https://github.com/nicmig/MultiVaDA , presentations from the course), not official exams.

### 6. Negative keyword sweep across plausible NTNU courses

Searched NTNU course-description pages (english + where noted, norwegian pages) for "tensor"/"PARAFAC": **0 hits** on the descriptions of TMA4205 Numerisk lineær algebra (Numerical Linear Algebra — the real "numerical matrix computation" course; also 0 "tensor" hits on its wiki start and 2024h pages at https://wiki.math.ntnu.no/tma4205), TMA4215, TMA4230, TMA4265, TMA4269 Data science, TMA4268 Statistisk læring, TMA4285, TMA4300, TMA4162, TMA4150, TMA4320, TMA4216, TKP4154, TK8117 (desc has PARAFAC only in Norwegian content list above), and the teacher-education overlaps IMAA2012/IMAG2012/IMAT2012. URLs are of the form https://www.ntnu.edu/studies/courses/<CODE> .
Note the task's guessed codes are mis-mapped: at NTNU, TMA4265 = Stokastisk modellering, TMA4180 = Optimering 1, TMA4285 = Tidsrekker (per the department course list https://wiki.math.ntnu.no/emner ) — none tensor-related. A web sweep for "tensor decomposition"/"tensorfaktorisering"/"PARAFAC" + NTNU course pages returned only TMA4432, TMA4431, TK8117 (search over https://www.ntnu.no/studier/emner/ pages).
Tensor decomposition at NTNU otherwise lives in **research**, not exams: e.g. NTNU Open theses/papers using CP/tensor decomposition, https://ntnuopen.ntnu.no/ntnu-xmlui/handle/11250/3122464 (Heritage Science 2023, IDI/NTNU) — not exam sources.

## Conclusion

**Is there ANY genuine pre-4C NTNU exam source with tensor decomposition (CP/Tucker/mode-n/rank-1/fibers-slices)? NO — with high confidence, none.** The only NTNU courses whose pensum contains tensor decomposition are TMA4432 (first exam 24.11.2026) and TMA4431 (first exam spring 2027); TK8117 teaches PARAFAC but has only oral exams with no published questions; the 4N/4D lineage demonstrably never taught it (verified even for the post-2022 exams the corpus missed); TMA4145 has no tensor content in any of its 2023–2025 exams.

**Realistic harvest for uke 35:**
1. **TMA4432 test exam 2026** — 1 genuine Tucker-vs-CPD-and-SVD problem **with full solution** (plus Moore–Penrose and other SVD problems): https://wiki.math.ntnu.no/_media/tma4432/2026h/test-exam-math4c_web.pdf
2. **TMA4432 exercise sheets** (øving 1–9, public + solved) — at least one full tensor-matricisation/decomposition problem: https://wiki.math.ntnu.no/_media/tma4432/2026h/exercise-sheet2.pdf (+ `-sol.pdf`)
3. **SVD-adjacent tier (legitimate, not tensor):** TMA4145 ordinary exams 2023, 2024, 2025 (+ continuation 2025/2026), each with a real SVD + minimum-norm-least-squares problem and a solution proposal — the corpus's TMA4145 pool stops at 2022, so 2023–2025 is net-new for the corpus. Archive: https://wiki.math.ntnu.no/tma4145/2026h/eksamensoppgaver
Everything else is empty-handed.

## Open uncertainties / what I could NOT verify

- **Kolda & Bader citation:** not found as searchable text in the uke-35 notes or slides; the notes' bibliography text may be font-encoded or absent. Whether Bergmann's notes cite Kolda–Bader (SIAM Review 2009) remains unconfirmed.
- **Test exam problem numbering/points:** digits garble in my text extraction; snippet quoted verbatim otherwise. Problem number (~5th–6th of the exam) unverified.
- **NTNU's official central exam archive** (https://www.ntnu.edu/students/exams) is a JS app I could not text-search with the available tools; in principle it hosts published exams for courses without wiki pages. Given that no course description except 4B/4C/TK8117 mentions tensors, a hidden tensor exam there is unlikely but not ruled out.
- **TK8117 internals:** course material/inspera pages not publicly accessible; no wiki page (404 verified). Possible related intro course TKT4150 — I could not confirm such a course/page exists at NTNU.
- **Course-description sweep coverage:** I checked the live description pages (default/latest year) for ~20 candidate codes plus a keyword web sweep; I did not check every historical year of every NTNU course description (all ~6000). Discontinued courses at Gjøvik/Ålesund campuses were only spot-checked (IMAA2012/IMAG2012/IMAT2012). The 4C lecturer's transition page independently supports "tensor content never taught pre-4C".
- **2025 TMA4130 re-sit exam** (`re-sit_exam_tma41x_05-aug-2026-solutions.pdf`) linked but not downloaded/checked.
- **"Candide-Parrondo"** in the task prompt appears to be a corruption of **CANDECOMP/PARAFAC**; the 4C materials call it "canonical polyadic decomposition (CPD)".
- Extraction tooling: no `pdftotext` available; I wrote a FlateDecode/`Tj` text extractor. Readability of every quoted file was sanity-checked, but text with custom font encodings (digits in the test exam) can garble.

## Method & source policy

Primary sources only: NTNU course-description pages (ntnu.no/ntnu.edu, kansleren data), wiki.math.ntnu.no course pages and their PDF media, and PDF text extracted from the exam PDFs themselves. Tools: `curl` for fetch, Python (stdlib `zlib` + regex) PDF text extraction (`/tmp/opencode/pdftxt.py`), downloaded PDFs kept in `/tmp/opencode/pdfs/`. No files inside `/home/user/eksamensrelevant4c` were read-modified or written.
