# Research: Exercise harvest — Ballard & Kolda, *Tensor Decompositions for Data Science* → TMA4432 Uke 35 synthetic oppgaver

> Provenans: utarbeidd 2026-10-26 av research-agenten som bakgrunn for dei syntetiske tensorfilene i uke 35 (issue #1); lagd under docs/research/ av ticket 2 på greina `spec/fill-35-36-38`. PDF-ane rapporten refererer til, ligg ikkje i arkivet (lisens).

Date: 2026-10-26. Agent: research subagent (primary-source only).
Nothing was written inside the repo `/home/user/eksamensrelevant4c`. All artifacts live in `/tmp/opencode/tensor-research/`.

---

## 1. Source & verification

| Item | Value |
|---|---|
| Primary source | https://users.wfu.edu/ballard/pdfs/tensor_textbook.pdf |
| Local copy | `/tmp/opencode/tensor-research/tensor_textbook.pdf` |
| SHA-256 | `b327d14e90a68f9c437e52a45a3d811ac24c077b3a4fae057bdba55d33515486` |
| Size / pages | 18 197 089 bytes / 422 PDF pages |
| Version stamp | "Final Draft: March 25, 2025" (cover + running footer on every page) |
| Authors | Grey Ballard, Tamara G. Kolda — CUP, *Tensor Decompositions for Data Science* |
| Extraction method | pypdf 6.21.2 (pure-Python wheel unpacked to `/tmp/opencode/tensor-research/pylibs`), full text in `book_clean.txt`; per-exercise extractor `extract_ex.py` |

Cross-reference source (for the public-domain overlap check):

* **SAND2007-6702** (Kolda & Bader, *Tensor Decompositions and Applications*, Sandia Report, Nov 2007): the URL given in the task (`http://www.sandia.gov/~tgkolda/pubs/pubfiles/SAND2007-6702.pdf`) is **dead** (redirects to a generic HTML page). Obtained via the widely-mirrored copy `https://www.cs.cmu.edu/~christos/courses/826-resources/PAPERS+BOOK/Kolda-Bader-SAND2007-6702.pdf` → `/tmp/opencode/tensor-research/SAND2007-6702.pdf`, SHA-256 `896c8232…ab09c27`, 71 pp., cover says "SANDIA REPORT SAND2007-6702 Unlimited Release … Approved for public release". Verified by text search that it contains the matching standard machinery: mode-n matricization/unfolding, "mode-n vector multiplication" (= mode-n product terminology of that era), Khatri–Rao (8 hits), matricization (8 hits), Kronecker (9), Tucker model, rank-1/outer product, HOOI.
* SIAM Review 51(3):455–500 (2009) published version of the same survey also present (`kolda-bader.pdf`). Note: the *SIAM journal version* is SIAM-copyrighted; only the *SAND report version* carries the US-government "approved for public release" status. For attribution-safety purposes we lean on the SAND version only.

Structural finding important for the harvest: **the book has no end-of-chapter "Exercises" section.** Exercises are labelled `Exercise N.M` (chapter.index) and are placed *inline*, immediately after the section that teaches the skill. Each exercise therefore has an unambiguous home section, given below.

## 2. Front-matter license quote (exact)

Verbatim from the copyright page (PDF p. 2, after "Typeset on March 25, 2025.") and repeated as a footer on every page:

> "Notice: This material will be published by Cambridge University Press as Tensor Decompositions for Data Science by Grey Ballard and Tamara G. Kolda. This pre-publication version is free to view and download for personal use only. Not for re-distribution, re-sale, or use in derivative works. © Grey Ballard and Tamara G. Kolda, 2024."

Citation line on the same page:

> "Citation: Grey Ballard and Tamara G. Kolda, *Tensor Decompositions for Data Science*, Cambridge University Press, final draft, March 25, 2025."

**Consequences for our oppgaver:** the draft forbids redistribution *and derivative works*. A "synthetic" oppgave must therefore (i) use our own numbers/tensors, (ii) re-word the task stem in our own words (Norwegian is safest — a translation into a new language of a *re-formulated* skill task, with no copied sentences), and (iii) carry an attribution line for the *source of inspiration*, e.g.:

> "Oppgaven er modellert på øvingsoppgaver i Ballard & Kolda, *Tensor Decompositions for Data Science* (CUP, final draft mars 2025), kap. X.Y – Z.W, samt Kolda & Bader, SAND2007-6702 (public domain). Ingen tekst eller tall er gjenbru ket fra disse kildene."

Mathematical *facts and skills* (how many fibers, unfolding definitions, CP storage formula) are not copyrightable, and every one we use is independently documented in public-domain SAND2007-6702 — so our solution files can state them freely in our own words.

## 3. Chapter map

Book parts: I Tensor Basics (ch 1–3), II Tucker (ch 4–8), III CP (ch 9–16), IV Closing (ch 17), Appendices A (numerical linear algebra), B (optimization), C (probability/stats), Index. **No solutions/answers appendix** (see §5).

| Ch | Title | Exercises | In uke-35 bar? |
|---|---|---|---|
| 1 | Tensors and Their Subparts | 15 | **Core** |
| 2 | Indexing and Reshaping Tensors | 40 | Partial (unfolding/vec/permutation core; linear-index mechanics secondary) |
| 3 | Tensor Operations | 36 | Partial (outer products, TTM/mode-n core; sparse storage secondary; MTTKRP/contraction mostly out) |
| 4 | Tucker Decomposition | 6 | **Core** |
| 5 | Tucker Tensor Structure | 18 | **Core** (structure/storage/unfolding; cost-derivation items secondary) |
| 6 | Tucker Algorithms | 13 | Thin — mostly MATLAB/Miranda; one cost-comparison gem (6.12) |
| 7 | Tucker Approximation Error | 5 | Out (all five are research-style proofs) |
| 8 | Tensor Train Decomposition | 6 | Out of bar (TT not in uke 35) |
| 9 | Canonical Polyadic Decomposition | 16 | **Core for 9.1–9.6**; 9.7–9.16 are data/MATLAB |
| 10–17 | Kruskal structure, CP-ALS, gradient, NLS, incomplete data, GCP, rank/special topics, closing | 28+17+13+8+12+20+33+14 | Out of bar |
| App A/B/C | also carry numbered exercises (≥44 in A alone; e.g. A.27, A.39–A.44 seen) | — | Matrix-prereq only |

Total numbered exercises in ch 1–17: **300**. In-scope-bar chapters (1–6, 9): **134**.

## 4. Exercise catalogue (in-bar skill content)

Answer-key column: the book prints **no answers anywhere** (§5), so "answer printed in book" = **NO** in every row; the column is kept implicit from here on.
Verdicts: **VS** = VERBATIM-SAFE (pure math fact, also in public-domain SAND2007-6702; facts may be restated in our own words with minimal risk), **RW** = REWORD (in-bar, hand-computable; must be rewritten + new numbers), **AS** = ADAPT-SHAPE (good underlying skill, but as written needs code/data — reshape into hand computation), **RJ** = REJECT.

### Chapter 1 — Tensors and Their Subparts (15/15 in bar)

| § | Ex | Task (paraphrase) | Hand? | Verdict |
|---|---|---|---|---|
| 1.1 | 1.1 | Number of entries of a 100×80×60 tensor | yes | VS (pure count) |
| 1.1 | 1.2 | Memory in GB for 512³ doubles (GB = 2³⁰), and 512⁴ | yes (powers of 2) | VS (arithmetic fact) |
| 1.2 | 1.3 | Read off mode-1/mode-2 hyperslices X(1,:,:), X(:,2,:) of the 3×3×2 Example 1.2 tensor | yes | RW |
| 1.2 | 1.4 | List all horizontal/lateral/frontal slices of the 2×2×2 Example 1.1 tensor (entries 8,9,2,9,6,1,3,5) | yes | RW |
| 1.2 | 1.5 | How many frontal slices for m×n×p×q? for n₁×…×n_d? (hyperslice definition) | yes | VS |
| 1.2 | 1.6 | Mode-k hyperslices of the 4-way 3×4×3×2 Example 1.3 tensor: sizes + write them out | yes | RW |
| 1.3 | 1.7 | Count column/row/tube fibers of an m×n×p tensor | yes | VS |
| 1.3 | 1.8 | Read 5 specified fibers (X(2,:,2), X(1,4,:), …) from a printed 3×4×2 integer tensor | yes | RW |
| 1.3 | 1.9 | Same for the 4-way Example 1.3 tensor | yes | RW |
| 1.3 | 1.10 | Count mode-k fibers of an m×n×p×q tensor, k=1..4 | yes | VS |
| 1.3 | 1.11 | General formula: number of mode-k fibers of n₁×…×n_d tensor | yes | VS |
| 1.4 | 1.12 | Size of the mode-2 unfolding X₍₂₎ of a 10×8×6 tensor | yes | VS (one-line fact) |
| 1.5.1 | 1.13 | Which 2-D matrices (slice notation) are visualized in the Miranda figure | reading only | AS (application reading — make it about our own small synthetic "data" tensor) |
| 1.5.3 | 1.14 | Which fiber type (row/column/tube) = one neuron's reading in one BMI trial | reading only | AS (application reading) |
| 1.5.4 | 1.15 | Load Chicago crime tensor, recreate figures | no (MATLAB) | RJ |

### Chapter 2 — Indexing and Reshaping (in-bar subset; §2.1 linear-index drills listed compactly)

| § | Ex | Task | Hand? | Verdict |
|---|---|---|---|---|
| 2.1 | 2.1 | Strides s₁,s₂,s₃ for the six orderings of Fig. 2.1 (2×2×2) | yes | RW (secondary skill) |
| 2.1.1 | 2.2 | Natural-order linear ↔ tuple conversion, size 4×3×3, six items | yes | RW |
| 2.1.1 | 2.3 | Same on 100×80×60 (ugly numbers) | tedious | AS (keep skill, shrink numbers) |
| 2.1.1 | 2.4, 2.7 | Prove composition of linearization (3-way, d-way by induction) | proof | RJ (below-bar proof work) |
| 2.1.1 | 2.5 | Natural strides of a 5×4×3×4 tensor | yes | RW |
| 2.1.1 | 2.6, 2.14, 2.19 | Write lin2tup/tup2lin variants | no | RJ |
| 2.1.2 | 2.8 | Show reverse index L*(i,j,k;m,n,p) = L(k,j,i;p,n,m) | short proof | RW |
| 2.1.2 | 2.9–2.13, 2.15 | Kronecker / Khatri–Rao ↔ (reverse) linear indexing proofs; size of reverse Kronecker product | proofs, 2.13(b) hand | RW (2.13 size question VS) |
| 2.1.3 | 2.16 | Which permutation π is natural? reverse? | yes | VS |
| 2.1.3 | 2.17 | Linear-index formula for permuted ordering π=(2,1,3), forward + inverse | yes | RW |
| 2.1.3 | 2.18 | Number of mode orderings of a d-tuple (= d!) | yes | VS |
| 2.2.1 | 2.21 | d-way vectorization reduces to matrix vec when p=1 | short proof | VS |
| 2.2.1 | 2.22 | vec(X) of a given 2×2×2 tensor (entries 8,7,−3,9,−1,4,0,5) | yes | RW (gem) |
| 2.3.1 | 2.23 | Prove X₍₁₎ = reshape(X, m×np) | short proof | RW |
| 2.3.1 | 2.24 | Same 2×2×2 tensor: write X₍₁₎, X₍₂₎, X₍₃₎ | yes | RW (gem — THE matricisation drill) |
| 2.3.1 | 2.25 | Unfolding with reverse column ordering, on Example 1.2's 3×3×2 tensor | yes | RW |
| 2.3.2 | 2.26 | Prove vec X = vec X₍₁₎ | short proof | VS (fact also in SAND report) |
| 2.3.2 | 2.27 | Mode-1/3/4 unfoldings of the 3×4×3×2 Example 2.9 tensor | yes, tedious | AS (shrink to 2×2×2×2) |
| 2.3.2 | 2.28, 2.29 | Mode-k unfolding = general unfolding with R=(k), C=rest; vec = general unfolding special case | short proofs | VS/RW |
| 2.3.2 | 2.30 | General unfolding R=(1,4), C=(2,3) of Example 2.10's 4-way tensor | yes, tedious | AS |
| 2.3.2 | 2.31 | Prove Prop 2.20 (no-memory-move unfoldings) | proof | RJ |
| 2.3.3 | 2.32 | Show X̃₍d₎ = [vec of frontal slices] | short proof | VS |
| 2.3.3 | 2.33 | rank of slice-derivative tensor: rank Y₍k₎ = 1 if rank X₍k₎ = 1 (rank-1 slicing fact) | short proof | VS |
| 2.4 | 2.34 | Permute the 2×2×2 Example 1.1 tensor: P(X,(2,1,3)), P(X,(3,1,2)) | yes | RW |
| 2.4 | 2.35 | Permutations of a given 3×2×3×2 integer tensor | yes | RW |
| 2.4 | 2.36 | Permuted vectorizations vec₍₂,₁,₃₎(X), vec₍₃,₂,₁₎(X) of Example 2.5's tensor | yes | RW |
| 2.4.1 | 2.37 | Prove X₍₂₎ = Y₍₁₎ with Y = P(X,(2,1,3)) (unfold = permute + reshape) | short proof | VS (fact in SAND via matricization def) |
| 2.4.1 | 2.38 | Pseudocode for mode-3 unfolding | yes | AS |
| 2.4.2 | 2.39, 2.40 | Perfect-shuffle proofs / implement tps | proof / no | RJ |

### Chapter 3 — Tensor Operations (in-bar subset)

| § | Ex | Task | Hand? | Verdict |
|---|---|---|---|---|
| 3.1 | 3.1, 3.2 | ‖X‖ = ‖vec X‖; ⟨X,Y⟩ = xᵀy | short proofs | VS |
| 3.2.1 | 3.3 | Prove (a∘b∘c) vectorizes entrywise: yℓ = aᵢbⱼcₖ | short proof | VS |
| 3.2.1 | 3.4 | ‖a∘b∘c‖² = ‖a‖²‖b‖²‖c‖² | short proof | VS |
| 3.2.1 | 3.5 | Prove the outer-product unfolding identities X₍₁₎ = a(c⊗b)ᵀ etc. (Prop 3.7 c–e) | short proof | VS (core matricisation identity; Kronecker/unfolding machinery is in SAND) |
| 3.2.2 | 3.6 | Size and vec of X = c∘b∘a | yes | VS |
| 3.2.2 | 3.7, 3.8 | d-way vec of vector outer product; prove Prop 3.10 (incl. general unfolding = Kronecker outer products) | proof | VS/RW |
| 3.2.3 | 3.9 | (a∘b)∘c = a∘(b∘c) associativity | short proof | VS |
| 3.2.4 | 3.10, 3.11 | Tensor⊗tensor outer product; relation A∘B vs B⊗A vs A⊗B | short | RW (3.11 is a nice hand fact) |
| 3.3 | 3.12 | Y = X×ₖU ⟺ P(Y,π) = P(X,π)×_{πk}U | proof | RW |
| 3.3.1 | 3.13, 3.15 | Arithmetic cost of mode-2 (X×₂V) and mode-3 TTMs on m×n×p | yes | VS (counting) |
| 3.3.1 | 3.14 | Prove X₍₂₎ = B₁ᵀ … B_pᵀ slice-block structure | proof | RW |
| 3.3 | 3.16 | Code + time ttm on 500³ | no | RJ (AS if reduced to cost question — but 3.13/3.15 already cover) |
| 3.4 | 3.17 | TTMs in different modes commute | short proof | VS |
| 3.4 | 3.18, 3.22 | Prove multi-TTM vectorization/unfolding identities (Prop 3.20, 3.23) | proof | VS (vec(Y)=(W⊗V⊗U)vec X is *the* core identity) |
| 3.4 | 3.19 | Write the matrix SVD X=UΣVᵀ in TTM notation | yes, tiny | RW (gem: X = [[Σ; U,V]]-style) |
| 3.4.3 | 3.20 | Compare costs of 4 ways to compute X×₁U×₂V×₃W (n×n×n, n×r factors); best when r<n? r>n? | yes | VS/RW (excellent hand cost-drill) |
| 3.4.3 | 3.21 | Six TTM orders, cost each, optimal order under m>n>p>s>r>q | yes | RW (gem) |
| 3.5 | 3.23, 3.24 | MTTKRP implementation; structure defs M_k,P_k | no / proof | RJ / AS |
| 3.6 | 3.25–3.27 | Draw dimension trees for multi-TTM/MTTKRP sequences | yes-diagram | AS (nice "draw the tree" hand item, but peripheral to uke-35 bar) |
| 3.7 | 3.28 | Sparse 3×3×3: nnz and coordinate list (I,v) from printed slices | yes | RW |
| 3.7 | 3.29 | Permutation of a coordinate-format sparse tensor | yes | RW |
| 3.7 | 3.30 | Storage dense vs sparse; break-even density ρ | yes | VS (storage-count skill, matches bar) |
| 3.7 | 3.31, 3.32 | nnz(X+Y) bounds; sparse norm formula/cost | short | RW / VS |
| 3.7–3.8 | 3.33–3.36 | Sparse MTTKRP algo; contraction via reshape+GEMM; tensor-network diagrams | partly | AS (diagrams 3.35/3.36 are drawable by hand) — else RJ |

### Chapter 4 — Tucker Decomposition (6)

| § | Ex | Task | Hand? | Verdict |
|---|---|---|---|---|
| 4.1.1 | 4.1 | For the printed 3×3×3 Example 4.1 tensor with given core G and factors, verify X=[[G;U,V,W]] entrywise for x₁₁₁, x₃₂₂, x₂₁₃ | yes | RW (gem — best "Tucker by hand" item in the book) |
| 4.1.2 | 4.2 | Compression ratio for 384×384×256×7 tensor, core 83×81×23×6 | yes (calculator) | RW (formula is VS; numbers must change) |
| 4.3.1 | 4.3 | Complexity of HOSVD for rank-(r,r,r), n×n×n | yes | VS/RW |
| 4.3.2 | 4.4 | Complexity of ST-HOSVD, same | yes | VS/RW |
| 4.5 | 4.5, 4.6 | Load Miranda tensor; compress; errors | no | AS (reshape into "given a compression table, compute ratio/error" reading) else RJ |

### Chapter 5 — Tucker Tensor Structure (18)

| § | Ex | Task | Hand? | Verdict |
|---|---|---|---|---|
| 5.1.1 | 5.1 | Derive elementwise formula for G×₁U×₂V×₃W | proof | RW |
| 5.1.1 | 5.2 | Storage of 3-way Tucker tensor (core q×r×s, dims m,n,p): qrs+mq+nr+ps | yes | VS (core storage-count item of the bar) |
| 5.1 | 5.3 | Sum of two Tucker tensors = Tucker with concatenated/block core, sizes (q₁+q₂)… | yes | RW (nice construction) |
| 5.1.2 | (text) | d-way storage Σrₖnₖ+Πrₖ vs Πnₖ — fact used in bar | — | VS |
| 5.2 | 5.4, 5.5 | Prove vec(T)=(W⊗V⊗U)vec(G) and mode-k unfolding identity for Tucker tensors | proof | VS (central matricisation identity, also implied by SAND's mode-n machinery) |
| 5.2 | 5.6 | multirank(T)=multirank(G) with full-rank factors | proof | RW |
| 5.4/5.5 | 5.7 | Orthonormal factors ⇒ ‖T‖=‖G‖ | short proof | VS |
| 5.4 | 5.8 | Cost of orthonormalizing factors via per-mode QR | yes | RW |
| 5.5 | 5.9 | Illustrate full reconstruction in order (2,3,1) with dimension bookkeeping + cost | yes-diagram | RW (turn into dimension-tracking drill; or AS with tiny numbers) |
| 5.6 | 5.10 | Partial reconstruction of one frontal slice via selector matrix: which mode, sizes, operation order | yes | RW (very good hand item) |
| 5.6 | 5.11 | Implement partial reconstruction | no | RJ |
| 5.7.1 | 5.12, 5.13 | Inner product of two Tucker tensors, cost; d-way version | proof/yes | RW/VS |
| 5.7.2 | 5.14 | Prove TTM of Tucker tensor touches one factor only | short proof | VS |
| 5.7.3 | 5.15–5.18 | MTTKRP of Tucker tensors: proofs, mode-2/3 derivations, cost vs full | partly | RW/RJ |

### Chapter 6 — Tucker Algorithms (13) — thin for hand work

| § | Ex | Task | Hand? | Verdict |
|---|---|---|---|---|
| 6.1.2 | 6.1 | With orthonormal factors fixed, G = X×₁U₁ᵀ…×dU_dᵀ is the optimal core | proof | RW |
| 6.1.2 | 6.2 | Prove error identity ‖X−T‖² = ‖X‖²−‖G‖² | short proof | VS/RW |
| 6.1.3 | 6.3, 6.4 | Implement LLSV (SVD / Gram-eigen) | no | RJ |
| 6.1.3 | 6.5 | Equivalence of rank-selection formula Eq. 6.12 | short proof | RW |
| 6.2 | 6.6–6.9 | Miranda HOSVD/ST-HOSVD runs; (6.6a/6.9a complexity ratios are hand-doable) | part | AS (keep only the complexity-ratio arithmetic) else RJ |
| 6.2–6.4 | 6.7, 6.10 | Implement HOSVD / ST-HOSVD | no | RJ |
| 6.4 | 6.11, 6.13 | Miranda HOOI runs | no | RJ |
| 6.5 | 6.12 | Compare HOOI vs ST-HOSVD costs (n^d r etc.); how many HOOI iterations fit in one ST-HOSVD run? | yes | RW (gem: the only real hand-computable HOOI-related item) |

Note: **the book contains no numeric "run one HOOI iteration by hand" exercise.** If the uke-35 bar wants that, it must be self-designed from Algorithm 6.6 (no exercise to copy → zero redistribution risk).

### Chapter 9 — Canonical Polyadic Decomposition (16)

| § | Ex | Task | Hand? | Verdict |
|---|---|---|---|---|
| 9.1.1 | 9.1 | Validate X=[[A,B,C]] for Kruskal's 2×2×2 rank-3 tensor (slices [[1,0],[0,1]] and [[0,1],[−1,0]]) | yes | RW (gem; the underlying example is Kruskal 1983, a public fact — VS-level as a fact, but write our own factors) |
| 9.1.1 | 9.2 | Rewrite the same CP with explicit weights λ and unit-length factors | yes | RW (gem — scaling ambiguity by hand) |
| 9.1.2 | 9.3 | Storage of d-way rank-r CP factorization: r(n₁+…+n_d) | yes | VS |
| 9.2.1 | 9.4 | Two candidate factor sets — which one equals the Example 9.1 factorization? (permutation ambiguity of columns) | yes | RW (gem) |
| 9.2.3 | 9.5 | Show a perturbed factor set (Example 9.2) also represents the same tensor → non-uniqueness | yes | RW |
| 9.3.1 | 9.6 | CP-ALS step: show the A-subproblem is linear least squares; cost O(mnpr) | short proof | VS/RW |
| 9.5.2 | 9.7 | Missing-data trick: sparse Hadamard update X̃ = W∘X + (1−W)∘[[A,B,C]], storage/cost | yes | AS |
| 9.6–9.8 | 9.8–9.16 | EEM / monkey BMI / Chicago crime: run CP ranks 1–5, plot errors, interpret factors, cluster trials | no (MATLAB) | AS only for the *reading* skill: give students a printed small CP and ask "which rank looks right / what does a zero entry in a factor mean / match factors to ground truth up to permutation" — that is the uke-35 "simple application reading" item |

## 5. Solution-availability verdict

**The draft prints NO answers, hints, or worked solutions for ANY exercise.**
Evidence: (1) Contents lists only Appendices A (Numerical Linear Algebra), B (Optimization), C (Probability & Statistics) and Index — no "Solutions"/"Answers" appendix; (2) a full-text scan finds no section titled "Solutions"/"Answers"; (3) the Preface never mentions solutions, hints, or an instructor manual (it points only to `www.tensortoolbox.org`, `github.com/sandialabs/pyttb`, and the four gitlab tensor-data repositories); (4) no exercise carries an asterisk/hint convention.
→ All løsningsfiler must be **self-produced**. This also means there is no model answer to "accidentally" copy — good for us, bad for shortcut-hunting.

## 6. Top-3 synthetic-oppgave blueprints (≈8 points, 3–4 deloppgaver)

Attribution note to append to each: see §2. All tensors below are **our own**; do not reuse the book's printed entries.

### Blueprint 1 — "Tensorens anatomi" (order, entries, fibers/slices, unfoldings, storage) — 8p
Fuse: 1.1/1.2 (entries & memory) + 1.7/1.10/1.11 (fiber counting) + 1.4/1.5 (slices) + 2.22/2.24 (vec & unfoldings of a tiny given tensor) + 1.12/5.2 (unfolding & storage sizes).
Stem: print a **self-made** 3×2×4 tensor X with entries −3…5 (mirror the shape of the book's 2×2×2 drill but different numbers).
- a) (2p) Order, mode sizes, number of entries; bytes needed as float64. How many mode-1 fibers? mode-3 fibers? (answer: 2·4 and 3·2, general formula Σ per product-all-but-k).
- b) (2p) Write out X(1,:,:) (mode-1 hyperslice) and X(:,2,1) (mode-2 fiber); name the fiber type in the 3-way jargon.
- c) (2p) Compute vec(X), X₍₁₎, X₍₂₎, X₍₃₎ by hand; check dims n₁×(N/n₁) etc.
- d) (2p) A sensor net logs 100×80×60 values: unfolding sizes X₍₂₎; compare full storage with a rank-(20,20,20) Tucker format r³-style count qrs+mq+nr+ps — how many times smaller?
Verdict basis: mostly VS facts; item c follows the 2.24/2.22 *shape* → wording & numbers fully ours (RW).

### Blueprint 2 — "Rank-1 og CP av en liten tensor" (outer products, CP verification, ambiguity, CP-vs-Tucker storage) — 8p
Fuse: 3.3/3.5 + 3.6 (outer product & its unfoldings) + 9.1/9.2/9.4 (CP verification, weights, permutation ambiguity) + 9.3 (CP storage) + 2.33/5.6 (rank-1 unfolding fact).
Stem: give **our own** vectors, e.g. a=(1,2)ᵀ, b=(1,−1,1)ᵀ, c=(2,0,1)ᵀ, X=a∘b∘c; plus a second factor set (A,B,C) with two columns swapped and column 2 scaled by ½, third ×2.
- a) (2p) Write the frontal slices of X; show X₍₁₎ = a(c⊗b)ᵀ (verify numerically — the book's Prop 3.7 identity, a public-domain-style fact echoed in SAND2007-6702's mode-n section).
- b) (2p) Verify X=[[a,b,c]]; then verify the permuted/scaled factor set gives the same tensor → state which ambiguity (permutation + scaling) this demonstrates.
- c) (2p) Rewrite with unit-norm factors and weights λ; give λ and the new [[λ;A,B,C]] form.
- d) (2p) Storage: full 100×80×60 tensor vs rank-10 CP; rank-(20,20,20) Tucker; which is smaller and why can CP not hit an error target directly (one sentence)?
Verdict basis: a/c/d VS-level facts, b RW (Kruskal-example *shape* is public, factors ours).

### Blueprint 3 — "Tucker for hånd: rekonstruksjon, kompresjon, én HOOI-ide" — 8p
Fuse: 4.1 (entrywise Tucker verification) + 4.2/5.2 (compression ratio/storage) + 5.9/5.10 (reconstruction order & partial reconstruction with selector) + 3.19/3.20/3.21 (TTM-order costs) + 6.12 (cost-comparison reasoning) + Algorithm 6.6 idea (no numeric book exercise exists → fully self-made).
Stem: print a 2×2×2 core G (entries 1,2,−1,0,…) and 3×2 factors U,V,W (entries 0,±1, small fractions forming orthogonal columns) — all our own.
- a) (2p) Compute T=[[G;U,V,W]] entries t₂₁₃ and t₁₂₂ via the double-sum definition (mirrors Ex 4.1's skill exactly).
- b) (2p) Storage & compression ratio for a 120×160×80 tensor with core (8,6,5): formula + number; compare to rank-5 CP storage (links to Blueprint-2 fact).
- c) (2p) Only slice T(:,:,1) is needed: set up the selector row-vector e₁ᵀW, give the reduced computation (G×₁U×₂V with W contracted), compute that frontal slice by hand; argue the flop saving qualitatively.
- d) (2p) Reconstruction order: with U(3×2),V(4×2),W(5×2) and G(2×2×2), list intermediate dimensions and operation counts for orders (1,2,3) vs (3,2,1); which is cheaper? (Ex 3.21-style cost chase, tiny numbers.) Optional bonus: one HOOI-style power step: given current V,W, compress X in modes 2,3 and read off new U from a printed small Gram matrix.
Verdict basis: a/b/d RW over VS facts; c's *selector-matrix* framing follows 5.10 (RW); the HOOI-step bonus has **no** book exercise counterpart (self-designed).

## 7. Open uncertainties

1. **Uke 35's exact coverage of Ch 2 linear indexing.** The stated bar doesn't name strides/linear indices; the book interleaves them with vec/unfolding. If strides are out, drop Ex 2.1/2.2/2.5/2.8/2.16/2.17/2.18 from consideration (Blueprint 1 uses only the vec/unfolding parts anyway).
2. **"VERBATIM-SAFE" is a risk label, not a licence.** Even for VS items we should never copy a *sentence* from the draft (its footer bans derivative works); we restate facts in our own words, and our facts are backed by the public-release SAND2007-6702. The SIAM-journal copy of the survey is © SIAM and should NOT be the cited public-domain source — cite the SAND number.
3. **Glyph noise in extraction.** Math operators (∘, ×ₙ, ⟦⟧, script R) came out garbled in raw extraction; paraphrases above were verified by reading context on both sides of each label. Exercise *numbers*, counts and section homes are reliable; if a future step needs a verbatim quote of any exercise stem, re-read the PDF page image for that exercise.
4. **Kruskal 2×2×2 example (Ex 9.1) provenance.** The example is attributed "Kruskal, 1983" in the book; it is a published mathematical object, but to be extra clean Blueprint 2 uses different vectors.
5. **Mirror provenance of SAND2007-6702.** Downloaded from a CMU course mirror of the official Sandia PDF (official sandia.gov link dead). Cover page verified ("Approved for public release"). If the repo wants belt-and-braces, re-fetch from a Sandia/OSTI mirror when network allows.
6. **Appendix exercise counts (App A ≥ 44) were not fully enumerated** — out of bar anyway, so only relevant if TMA4432 later wants matrix-prerequisite drills.
7. The book may print per-exercise difficulty or solution status in a future CUP final version; everything above is pinned to the March 25, 2025 draft (hash in §1).
