# Frozen-statement comparison

Inspected commit: `2a8e85703420116c8f07e1eebebd34fa221c8d55`, a member of the
locally available trureturing `dev` history. The book pin was set with `tbook pin`.
The source and frozen JSON were read with `git show`, not from the working tree.
Exact inspection bytes are retained in `evidence/compared-source.txt` and
`evidence/frozen-state.json`. No Lean compilation was run in this conversion.

Module: `D5/S1/Recurrence/Algebraic/ChenChenParityPositivity`.
The frozen JSON lists 12 theorem entries: 2 public and 10 private/generated.
The public GID used below as comparison context is
`D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.even_rows_positive`.
Its source declaration starts at line 175, counted from the inspected bytes.
`result` starts at line 191. Neither is a book verification citation.

`Source (m : ℤ) (T : ℕ → ℕ → ℤ)` requires the triangular boundary and the
interior recurrence; outside values and row zero are unconstrained.
`ParityPositivity m` expands to existence of a source and universal even-row
nonnegativity for every source. `claim` is the conjunction at -3, -4, -5.
`even_rows_positive` quantifies over integer `r ≥ 3`, any integer-valued source,
positive even `n` and all `1 ≤ k ≤ n`, concluding strict positivity.
`result : claim` gives the three existence/nonnegativity assertions only.

| Node | Book id | Status | Verdict | Complete-statement comparison |
|---|---|---|---|---|
| s1 | paper-thm-main | written-proof | special case | The manuscript quantifies over real r ≥ 3 and includes all odd-row interior signs. The public theorem supplies the integer even-row part only. The private next-interior helper is conditional on a positive preceding row and integer r. |
| s2 | paper-lem-second | written-proof | special case | The surrounding manuscript parameter r is real. The public even-row theorem implies the second-column conclusion for integer r; the private second_even_positive helper also has integer r and is not a public target. Reindexing 2q+2 does not remove that domain gap. |
| s3 | paper-cor-classification | written-proof | variant | The manuscript is an iff classification over all integer m, with the m ≥ 0 branch and exclusion of -1, -2. The public theorem is the m ≤ -3 branch only. |
| s4 | paper-cor-sums | written-proof | none | The manuscript asserts the all-real-m product, n=1 boundary, even-row cancellation and equal parity sums. Neither public statement states these identities; private integer reflection alone is insufficient. |
| s5 | paper-cor-annulus | written-proof | none | Requires all-real m ≤ -3, even n ≥ 2, all complex roots, both coefficient-ratio bounds and L U = 1. No root polynomial or annulus statement occurs in the inspected module. |
| s6 | paper-cor-odd | written-proof | none | Includes odd integrality, mod-3 congruence, both parameter generalizations and all-odd-row nonvanishing. No public or private statement in this module states alternating-sum arithmetic. |
| s7 | paper-thm-growth | written-proof | none | Includes real positive and negative parameter limits, exceptional -3 scale and exponent, constants at -4/-5 and failure of mirror growth. No root-modulus definition or asymptotic statement appears. |
| s8 | paper-cor-boundaryroots | written-proof | none | Includes all-q factorizations at -1/-2, unit moduli and zero exponents, m=0 formula, simple negative roots for every real m>0, and nonreal roots in row 6 at -3. Neither public theorem states any of this composite claim. |

All eight manuscript statements and their proofs were checked against the frozen
TeX, including companion-results.tex. Their exact English statements remain in
the book; Chinese translations preserve quantifiers, parameter domains and
boundary cases. No result was narrowed to obtain a Lean badge. Every row has an
empty `gids` list. The first three comparison candidates are recorded separately;
`none` uses null. All comparisons record the full inspected commit.

A digest search at that commit for Eulerian, Chen/Chen, Eneström/Kakeya,
row alternating sums and root modulus found no other complete match. Other hits
concern shifted Eulerian polynomials from coprime width descents, rook-Eulerian
counterexamples, fixed rows of the ordinary Eulerian matrix square, and unrelated
Stirling/partition or degree-root objects. These do not state the paper's
parameterized recurrence claims. The retained search transcript records scope;
a keyword search is not a proof that no differently named theorem exists.

The module's header explicitly records an unresolved escape-audit annotation
for issue #24785. This work records membership and statement scope; it does not
resolve that annotation or promote a catalog receipt/status. This internal
comparison record was not used as mathematical source material for exposition.
