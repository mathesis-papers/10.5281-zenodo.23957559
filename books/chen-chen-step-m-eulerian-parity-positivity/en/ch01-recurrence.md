# 1. The conjectures and the recurrence

A triangular array can be built one row at a time: put 1 at each end, then combine two neighbours above each interior position. The parameter $m$ controls the two weights. When those weights become negative, ordinary one-step positivity induction stops working. The question is whether a predictable sign pattern nevertheless survives for all rows, rather than just the rows a computer can list. Here “positive even row” means an even row index $n>0$, not an extra assumption about its entries.

The polynomial $R_{m,n}$ simply packages a row as its coefficients. Evaluating it at 1 adds the entries; evaluating it at $-1$ alternates their signs. Its roots encode different information, so positive coefficients alone do not settle the growth of the largest root.

The COMMENTS sections of OEIS A392664–A392666 conjecture
even-row nonnegativity at steps $-3,-4,-5$ [[3](references.md#bib-oeis3), [4](references.md#bib-oeis4), [5](references.md#bib-oeis5)].
Their executive summary states the conjecture for every integer $m\leq-3$
[[6](references.md#bib-chen), p. 1, Conjecture 2] and reports verification through row 400
for the three listed steps. Ma and Zhang prove that stronger parameter-wide statement,
with strict positivity in place of nonnegativity.

For a real parameter $m$, define $T_m(n,k)$ for integers $1\leq k\leq n$ by

<a id="eq-boundary"></a>

**Equation (1).**

$$
T_m(n,1)=T_m(n,n)=1 \qquad(n\geq1),
$$

<a id="eq-recurrence"></a>

**Equation (2).**

$$
T_m(n,k)=\bigl(m(n-k)+1\bigr)T_m(n-1,k-1)
          +\bigl(m(k-1)+1\bigr)T_m(n-1,k),
$$

where the second equation applies only for $1<k<n$.
These equations give existence and uniqueness on the triangular domain
by induction on $n$. If $m$ is an integer, all entries are integers.
No values outside the triangle enter the equations.
Set $R_{m,n}(y)=\sum_{k=1}^n T_m(n,k)y^{k-1}$.

::: {.theorem #paper-thm-main status="written-proof" proof="pf-paper-thm-main" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s1" title="Paper Theorem 1 (thm:main)" doi="10.5281/zenodo.23957560" source="Theorem 1 (thm:main)"}
For every real $r\geq3$, the triangle of step $m=-r$ satisfies

1. $T_{-r}(n,k)>0$ for every positive even $n$ and $1\leq k\leq n$;
2. $T_{-r}(n,k)<0$ for every odd $n\geq3$ and $1<k<n$.

In particular, the three OEIS conjectures and Conjecture 2 of
[[6](references.md#bib-chen)] hold for their stated integer parameters.
:::

Start with a finite example: every entry of row 6 at step $-3$ is positive. Colour encodes sign, not magnitude; the picture illustrates [@paper-thm-main] and is not an all-row proof.

::: {.viz src="step-triangle" preset="even" height="500"}
**Row 6 has a positive interior too.** At step $-3$, cyan marks positive entries; amber rings the current cell.
:::
