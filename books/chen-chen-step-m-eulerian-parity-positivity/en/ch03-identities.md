# 3. Companion identities and root bounds

Summing the recurrence is easier than computing each entry. A value in the old row contributes to two positions in the new one, and its two weights add to the same number regardless of its position. That turns a triangular computation into a one-variable product. For even rows, mirror positions have opposite parity, so their alternating contributions cancel in pairs.

The root annulus asks a different question: where can a polynomial with positive coefficients vanish? Consecutive coefficient ratios give two radii. This is a finite-row bound, with radii that can change with $n$; it is not a uniform annulus for every rescaled root in every row.

These consequences address the adjacent COMMENTS statements in the three
OEIS entries. They concern the same recurrence, rather than a different
root-asymptotic assertion.

::: {.corollary #paper-cor-sums status="written-proof" proof="pf-paper-cor-sums" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s4" title="Paper Corollary 4 (cor:sums)"}
For every real $m$,

$$
S_n(m):=\sum_{k=1}^n T_m(n,k)
 =\prod_{j=0}^{n-2}(mj+2),\qquad S_1(m)=1.
$$

For even $n$,

$$
R_{m,n}(-1)=0,\qquad
 \sum_{\substack{1\leq k\leq n\\ k\text{ odd}}}T_m(n,k)
 =\sum_{\substack{1\leq k\leq n\\ k\text{ even}}}T_m(n,k)
 =\tfrac12 S_n(m).
$$
:::

::: {.proof #pf-paper-cor-sums}

*Written proof reproduced from Ma and Zhang, frozen manuscript version 2.*

For $n\geq3$, extend the preceding row by zeros just for summing
[(2)](ch01-recurrence.md#eq-recurrence). At $k=1,n$, the same formula then gives
the boundary value 1. A preceding-row entry at position $j$
has total coefficient

$$
\bigl(m(n-j-1)+1\bigr)+\bigl(m(j-1)+1\bigr)=m(n-2)+2.
$$

Consequently $S_n=(m(n-2)+2)S_{n-1}$. Since $S_2=2$,
the product follows. For even $n$, reflection pairs equal entries
at positions $k$ and $n+1-k$ of opposite parity. Their contributions
to $R_{m,n}(-1)$ cancel, and their parity sums agree.

:::

::: {.corollary #paper-cor-annulus status="written-proof" proof="pf-paper-cor-annulus" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s5" title="Paper Corollary 5 (cor:annulus)"}
For real $m\leq-3$ and even $n\geq2$, every root $z$ of
$R_{m,n}$ satisfies

$$
L_n\leq |z|\leq U_n,\qquad
 L_n=\min_{1\leq k<n}\frac{T_m(n,k)}{T_m(n,k+1)},\quad
 U_n=\max_{1\leq k<n}\frac{T_m(n,k)}{T_m(n,k+1)}.
$$

All these ratios are positive; symmetry also gives $L_nU_n=1$.
:::

::: {.proof #pf-paper-cor-annulus}

*Written proof reproduced from Ma and Zhang, frozen manuscript version 2.*

This is the Eneström–Kakeya bound [[7](references.md#bib-kakeya)]; the following
argument includes the boundary cases. For a polynomial
$P(z)=\sum_{j=0}^d a_jz^j$ with $a_j>0$, put
$U=\max_{0\leq j<d}a_j/a_{j+1}$ and $b_j=a_jU^j$.
Then $b_0\leq\cdots\leq b_d$. If
$Q(w)=P(Uw)$ had a root with $|w|>1$, the identity

$$
(1-w)Q(w)=b_0+\sum_{j=1}^d(b_j-b_{j-1})w^j-b_dw^{d+1}
$$

would imply

$$
b_d|w|^{d+1}
 \leq b_0+\sum_{j=1}^d(b_j-b_{j-1})|w|^j
 \leq b_d|w|^d,
$$

a contradiction. Applying this upper bound to $z^dP(1/z)$
gives the lower bound. Theorem [1](ch01-recurrence.md#paper-thm-main) supplies positive
coefficients here. Reflection makes the set of consecutive ratios
invariant under reciprocation, so $L_n=1/U_n$.

:::
