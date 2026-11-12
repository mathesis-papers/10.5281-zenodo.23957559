# Chen and Chen's parity-positivity conjectures

This note proves Conjecture 2 on page 1 of Chen and Chen's January 2026
executive summary and the conjectures in OEIS A392664–A392666, COMMENTS.
Every positive even row is strictly positive for real steps at most -3;
odd-row interiors are negative. For integer steps, even-row nonnegativity
holds exactly outside {-2,-1}.

It also proves the adjacent odd-row nonvanishing assertions at
steps -4 and -5. If A_q(m)=R_(m,2q+1)(-1), then A_q(-4)/8^q is an odd
integer and A_q(-5)=1 modulo 3. Stronger parameter congruences appear in
the section on odd-row alternating sums.

For the largest root modulus, the corrected asymptotic at step -3 is

    M_n(-3) ~ 5^(n/2) / sqrt(45).

Thus its growth exponent is log(5)/2, not log(2); scaling by 2^n has no
finite limit. The note proves the constants 1/6 and 1/10 when scaling
the steps -4 and -5 by 3^n and 4^n, respectively. More generally it proves
the root asymptotic for all real m > 0 and m <= -4. The remaining
real-parameter interval and all-row root reality at -4 and -5 are not
characterized here. Reflection, row and parity sums, the finite-row root
annulus, and degenerate-step factorizations have complete written proofs.

## Build

Keep `note.tex`, `companion-results.tex` and `coverage.tex` together.
With Tectonic 0.17.0:

```sh
tectonic --untrusted note.tex
```

Alternatively, use a standard TeX installation with `amsmath`, `amssymb`,
`amsthm`, `booktabs`, `array`, `longtable`, `geometry`, `hyperref`, `xurl`,
and Latin Modern:

```sh
pdflatex -no-shell-escape note.tex
pdflatex -no-shell-escape note.tex
```

The bibliography is contained in `note.tex`; no BibTeX database is needed.

## Exact finite checks

Python 3, standard library only:

```sh
python3 verify.py > finite-check.json
```

The output covers 14 integer steps through row 400, with exact row-stream
digests; the two degenerate integer steps through row 400; six rational
steps through row 60; alternating-sum congruences and polynomial identities;
the two column formulas; and 605 comparisons with the differential equation
for the hyperbolic-cosine generating function. Exact contour inequalities
give 5^200/7 < M_400(-3) < 5^200/6; a separate Vieta bound gives
M_100(-3) > 2^100. These finite computations are distinct from the
all-row proofs and root asymptotics in the note.

## Statement coverage

The pinned
[ChenChenParityPositivity.lean](https://github.com/the-omega-institute/trureturing/blob/66a0495cbdf1bb9b42d715c1b3cd3365862896fa/D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.lean)
has namespace `D5.S1.Recurrence.Algebraic.ChenChenParityPositivity`.
The declaration `even_rows_positive` states strict even-row positivity for
integer r >= 3 and every integer-valued function satisfying `Source (-r)`.
The declaration `result` states existence and universal even-row
nonnegativity for the three steps -3, -4 and -5. The real-parameter
extension, classification, identities, alternating-sum congruences and
root results are written proofs, not additional assertions of those
declarations. The note's coverage table maps the individual source items.

`source-guide.md` gives the public posing locators, recurrence
identifications, earlier related formulas and checked references.

## Authors and license

Haobo Ma — ChronoAI Pte Ltd, Singapore.

Wenlin Zhang — National University of Singapore;
ChronoAI Pte Ltd, Singapore.

CC BY 4.0 (`cc-by-4.0`).
