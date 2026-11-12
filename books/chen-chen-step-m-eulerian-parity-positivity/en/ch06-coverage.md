# 6. Coverage and verification

Read the following table as the manuscript’s coverage of the cited source claims. “Proved” here means a written argument in this manuscript. In this Mathesis reading, all eight registered results have WRITTEN PROOF status and none has an exact frozen Lean citation. The public comparison candidates at the current [book pin](trureturing:commit) establish narrower integer statements, as detailed after the table. The imported Mathesis nodes remain in their recorded preparing state.

| Source item | Coverage |
|---|---|
| A392664–A392666, COMMENTS: even-row conjectures; [[6](references.md#bib-chen), p. 1, Conjecture 2] | Proved: Theorem [1](ch01-recurrence.md#paper-thm-main), including all real $m\leq-3$. |
| Same entries: reflection, row sums, even-row alternating sums | Proved: [(3)](ch02-signs.md#eq-symmetry) and Corollary [4](ch03-identities.md#paper-cor-sums). |
| Same entries: coefficient-ratio root annulus | Proved: classical bound cited and proved in Corollary [5](ch03-identities.md#paper-cor-annulus). |
| Cross-referenced steps $m=-2,-1,0,1,2,3$ | Proved: Corollaries [3](ch02-signs.md#paper-cor-classification), [8](ch05-roots.md#paper-cor-boundaryroots) and Theorem [7](ch05-roots.md#paper-thm-growth); recurrence identifications appear in the source guide. |
| A392665, A392666, COMMENTS: odd-row nonvanishing | Proved: Corollary [6](ch04-alternating-sums.md#paper-cor-odd), with stronger congruences. |
| A392664, COMMENTS: $R_{-3,5}(-1)=0$ | Proved by [(6)](ch04-alternating-sums.md#eq-egf) or row 5; displayed odd-row values are also exact finite checks. |
| [[6](references.md#bib-chen), pp. 2–3]: constants $1/6,1/10$ at $m=-4,-5$ | Proved: Theorem [7](ch05-roots.md#paper-thm-growth) covers every real $r\geq4$. |
| [[6](references.md#bib-chen), p. 1, Theorem 1; pp. 2–3]: step $-3$ growth, constant $1/3$, and growth invariance with $m=1$ | Refuted-and-corrected: Theorem [7](ch05-roots.md#paper-thm-growth) gives exponent $\tfrac12\log5$ and scale $5^{n/2}/\sqrt{45}$. |
| [[6](references.md#bib-chen), p. 1, Theorem 1; p. 2]: unrestricted complex growth law and $m=-1$ degeneracy | Refuted-and-corrected: $M_n\geq1$; the exponent at $m=-1$ is 0. Remaining complex-parameter asymptotics are not covered. |
| [[6](references.md#bib-chen), pp. 2–3]: nonreal roots at $m=-3$; all roots real at $m=-4,-5$ | Proved at $m=-3$ by row 6; all-row reality at $m=-4,-5$ is not covered. |
| [[6](references.md#bib-chen), p. 2]: fixed annulus for scaled zeros | Refuted-and-corrected as a uniform positive inner radius for all zeros; the finite-row bound above applies. |
| OEIS mirror map $m\mapsto-m-2$ and equality of $\lvert m+1\rvert$ | Proved by substitution; it does not imply equal growth exponents, as steps $1,-3$ show. |
| [[6](references.md#bib-chen), pp. 2–3]: finite plots and EK tightness percentages; page-3 reference to a full preprint | Not covered as numerical accuracy claims or as unprovided additional theorems; no conclusion depends on them. |

The pinned
[`ChenChenParityPositivity.lean`](https://github.com/the-omega-institute/trureturing/blob/66a0495cbdf1bb9b42d715c1b3cd3365862896fa/D5/S1/Recurrence/Algebraic/ChenChenParityPositivity.lean)
at its 2 November 2026 revision contains the declarations
`even_rows_positive` and `result`, in namespace
`D5.S1.Recurrence.Algebraic.ChenChenParityPositivity`.
The first formalizes strict positivity for integer $r\geq3$ and
every function satisfying the boundary and recurrence. The second
formalizes existence together with universal even-row nonnegativity
for steps $-3,-4,-5$. The real-parameter extension, integer-step
classification, identities, alternating-sum congruences and root-growth
results have written proofs above; they are not additional assertions
of either pinned declaration.
The accompanying `verify.py` checks exact integer rows through
$n=400$ for $m=-12,\ldots,-3,0,1,2,3$: symmetry, the row-sum
product, even-row positivity and parity sums, and negative-step
odd-row interior signs. It also checks the displayed initial values
and the two excluded integer parameters. Further exact checks cover
the alternating-sum congruences, column formulas and degenerate-step
factorizations. These finite computations are separate from the all-row proofs.

::: {.slides src="seminar"}
**English seminar slides.** A 4:3 academic Beamer deck with speaker notes, planned for about 25 minutes; result citations use the book model.
:::
