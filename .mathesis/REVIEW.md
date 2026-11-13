# Statement comparison with the formal base

This condenses the existing statement review for catalog version 2. The eight
written statements and their proofs, including `companion-results.tex`, were
compared with frozen state at `2a8e85703420116c8f07e1eebebd34fa221c8d55`.
The inspected module was `D5/S1/Recurrence/Algebraic/ChenChenParityPositivity`.
This migration preserves that review; it performs no new mathematical review
or Lean compilation and does not change catalog verification status.

The public `even_rows_positive` statement covers integer parameters r ≥ 3 and
strict positivity in positive even rows. The public `result : claim` asserts
existence and even-row nonnegativity at -3, -4 and -5. The source's real-parameter,
odd-row, root and asymptotic claims have broader or different scope. All eight
book results retain written proofs and empty verification GID lists. A compared
declaration below is context for formalization, never verification of the full
written result.

| Result | Verdict | Compared declaration | Commit | Scope |
|---|---|---|---|---|
| `paper-thm-main` | special case | `D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.even_rows_positive` | `2a8e85703420116c8f07e1eebebd34fa221c8d55` | The manuscript quantifies over real r ≥ 3 and includes all odd-row interior signs. The public theorem supplies the integer even-row part only. The private next-interior helper is conditional on a positive preceding row and integer r. |
| `paper-lem-second` | special case | `D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.even_rows_positive` | `2a8e85703420116c8f07e1eebebd34fa221c8d55` | The surrounding manuscript parameter r is real. The public even-row theorem implies the second-column conclusion for integer r; the private second_even_positive helper also has integer r and is not a public target. Reindexing 2q+2 does not remove that domain gap. |
| `paper-cor-classification` | variant | `D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.even_rows_positive` | `2a8e85703420116c8f07e1eebebd34fa221c8d55` | The manuscript is an iff classification over all integer m, with the m ≥ 0 branch and exclusion of -1, -2. The public theorem is the m ≤ -3 branch only. |
| `paper-cor-sums` | none | — | `2a8e85703420116c8f07e1eebebd34fa221c8d55` | The manuscript asserts the all-real-m product, n=1 boundary, even-row cancellation and equal parity sums. Neither public statement states these identities; private integer reflection alone is insufficient. |
| `paper-cor-annulus` | none | — | `2a8e85703420116c8f07e1eebebd34fa221c8d55` | Requires all-real m ≤ -3, even n ≥ 2, all complex roots, both coefficient-ratio bounds and L U = 1. No root polynomial or annulus statement occurs in the inspected module. |
| `paper-cor-odd` | none | — | `2a8e85703420116c8f07e1eebebd34fa221c8d55` | Includes odd integrality, mod-3 congruence, both parameter generalizations and all-odd-row nonvanishing. No public or private statement in this module states alternating-sum arithmetic. |
| `paper-thm-growth` | none | — | `2a8e85703420116c8f07e1eebebd34fa221c8d55` | Includes real positive and negative parameter limits, exceptional -3 scale and exponent, constants at -4/-5 and failure of mirror growth. No root-modulus definition or asymptotic statement appears. |
| `paper-cor-boundaryroots` | none | — | `2a8e85703420116c8f07e1eebebd34fa221c8d55` | Includes all-q factorizations at -1/-2, unit moduli and zero exponents, m=0 formula, simple negative roots for every real m>0, and nonreal roots in row 6 at -3. Neither public theorem states any of this composite claim. |

The original digest search covered Eulerian and Chen/Chen terms,
Eneström/Kakeya, alternating row sums and root modulus at the inspected commit.
Its other hits concerned different objects and supplied no complete match;
keyword search does not exclude a differently named declaration. The inspected
module also retained the unresolved escape-audit annotation for issue #24785;
this review does not resolve it. The comparison record was not used as a
mathematical source for the exposition.
