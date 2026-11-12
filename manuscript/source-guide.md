# Scientific sources and statement coverage

## Primary posing statements

- Xin Chen and Yudian Chen, [OEIS A392664](https://oeis.org/A392664),
  COMMENTS, even-row conjecture; authored 18 January 2026; revision 35,
  5 February 2026; step -3.
- The same authors, [OEIS A392665](https://oeis.org/A392665), COMMENTS,
  even-row conjecture and odd-row alternating-sum nonvanishing;
  authored 18 January 2026; revision 20, 5 February 2026; step -4.
- The same authors, [OEIS A392666](https://oeis.org/A392666), COMMENTS,
  the corresponding two assertions at step -5; authored 1 February 2026;
  revision 17, 5 February 2026.
- Xin Chen and Yudian Chen, *The Step-m Eulerian Triangle: Mirror Symmetry
  and Universal Growth Rate — Executive Summary for OEIS*, January 2026,
  [version 1](https://doi.org/10.5281/zenodo.18446568), publication date
  31 January 2026, and [version 2](https://doi.org/10.5281/zenodo.18452218),
  1 February 2026. Page 1 contains Conjecture 2 and Theorem 1;
  pages 2–3 give the growth constants, root descriptions and figures.
  Both versions contain the same summary PDF.

## Cross-referenced triangles

The following identifications are equality of the displayed boundary-one
recurrences, not equality of every other enumerative interpretation.
Pascal's zero-based row n-1 corresponds to the note's positive row n.

| Step | OEIS entry | Defining locator | Consequences in the note |
|---|---|---|---|
| -2 | [A225372](https://oeis.org/A225372) | NAME and FORMULA | Factorization, unit-modulus roots, sign exception |
| -1 | [A144431](https://oeis.org/A144431) | NAME and FORMULA | Factorization, unit-modulus roots, sign exception |
| 0 | [A007318](https://oeis.org/A007318) | NAME, binomial coefficients | Binomial rows, root -1 |
| 1 | [A008292](https://oeis.org/A008292) | NAME and Eulerian recurrence | Positivity, simple negative roots, M_n/2^n -> 1 |
| 2 | [A060187](https://oeis.org/A060187) | NAME, boundary-one recurrence | Positivity, simple negative roots, M_n/3^n -> 1/3 |
| 3 | [A142458](https://oeis.org/A142458) | NAME and FORMULA | Positivity, simple negative roots, M_n/4^n -> 1/6 |

G. C. Greubel's 1 March 2022 FORMULA addition to A144431 already gives
the step -1 coefficients as a sum of two signed binomial coefficients.
The note credits that earlier formula and proves its polynomial
factorization. Peter Bala's 26 October 2008 FORMULA additions to A060187
give its exponential generating function and a real-zero assertion.
The note's m=2 specialization agrees with that generating function;
its positive-parameter root argument covers this example directly.
Other combinatorial and number-theoretic assertions linked by these
large entries are outside the listed recurrence and root statements.

## Root statements

The notation M_n(m) means the largest modulus of a zero of the exact
row polynomial defined in the summary. At step -3, the third column has
leading term (-5)^n/45, forcing a different exponential scale from the
second column. The root-growth theorem proves the exact scale and leading constant;
it also proves the source's constants at steps -4 and -5.
The source's broad complex-parameter law and its -1 degeneracy entry
therefore require the corrections stated in the coverage table.

The fixed-annulus correction concerns a positive inner radius containing
all scaled zeros. It does not make an assertion about the proportion
of zeros in a limiting distribution. Universal real-rootedness at steps
-4 and -5 is not established by the sign or asymptotic arguments.

## Classical tools

- S. Kakeya, *On the limits of the roots of an algebraic equation with
  positive coefficients*, Tôhoku Mathematical Journal 2 (1912), 140–142:
  [publisher record](https://www.jstage.jst.go.jp/article/tmj1911/2/0/2_0_140/_article).
  The positive-coefficient annulus is also proved in the note.
- [NIST DLMF §1.10(iv)](https://dlmf.nist.gov/1.10#iv), Rouché's theorem:
  the strict contour inequality preserves the number of zeros.
  It is applied on circles disjoint from zero with the uniform tail
  bound established in the root-growth proof.

## Declaration scope

The only pinned Lean file is
[ChenChenParityPositivity.lean](https://github.com/the-omega-institute/trureturing/blob/66a0495cbdf1bb9b42d715c1b3cd3365862896fa/D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.lean).
Its two principal declarations cover the integer even-row positivity
statements described in the note and README. The other conclusions
are supplied by the written proofs and the explicitly finite checks.

CC BY 4.0. Haobo Ma; Wenlin Zhang.
