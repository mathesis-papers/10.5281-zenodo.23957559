# 2. Two-row sign propagation

The proof works two rows at a time. A positive even row feeds a negative odd interior, and two negative factors then feed a positive next even interior. The delicate positions sit next to the boundary: one predecessor there is the fixed value 1. Lemma 2 handles exactly that obstacle instead of pretending the same sign argument works everywhere. Reflection means the left-hand calculation also handles the right-hand edge.

First observe that for every real $m$,

<a id="eq-symmetry"></a>

**Equation (3).**

$$
T_m(n,k)=T_m(n,n+1-k).
$$

Indeed, reflection interchanges the boundary entries. For an interior
entry, the two predecessor indices $k-1,k$ are reflected in row $n-1$
to $n+1-k,n-k$, respectively. The two coefficients in
[(2)](ch01-recurrence.md#eq-recurrence) are interchanged as well. Induction on $n$
therefore proves [(3)](ch02-signs.md#eq-symmetry).

::: {.lemma #paper-lem-second status="written-proof" proof="pf-paper-lem-second" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s2" title="Paper Lemma 2 (lem:second)"}
For $r\geq3$, $T_{-r}(n,2)>0$ whenever $n\geq2$ is even.
:::

::: {.proof #pf-paper-lem-second}

*Written proof reproduced from Ma and Zhang, frozen manuscript version 2.*

Write $a_n=T_{-r}(n,2)$ for $n\geq2$. The boundary gives $a_2=1$;
substitution at $k=2$ gives, for $n\geq2$,

$$
a_{n+1}=1-r(n-1)+(1-r)a_n.
$$

Substituting this identity once more and collecting terms yields

<a id="eq-twostep"></a>

**Equation (4).**

$$
a_{n+2}=(r-1)^2a_n+r(r-2)n+2-r^2.
$$

The first step must be treated separately:

$$
a_4=(r-1)^2+2r(r-2)+2-r^2
     =2r(r-3)+3\geq3.
$$

For $n\geq4$, the remaining term in [(4)](ch02-signs.md#eq-twostep) satisfies

$$
r(r-2)n+2-r^2
 \geq3r^2-8r+2
 =3(r-3)^2+10(r-3)+5>0.
$$

Thus [(4)](ch02-signs.md#eq-twostep), starting at $a_4>0$, proves positivity for
all later even $n$. Together with $a_2=1$, this proves the lemma.

:::

::: {.proof #pf-paper-thm-main}

*Written proof reproduced from Ma and Zhang, frozen manuscript version 2.*

The even row $n=2$ is $(1,1)$. Suppose an even row $n\geq2$
is strictly positive. For $1<k<n+1$, both coefficients defining
$T_{-r}(n+1,k)$ are strictly negative: their positive integer factors
$n+1-k$ and $k-1$ are at least one, so each coefficient is at most
$1-r<0$. Both predecessor entries lie in row $n$ and are positive.
Every interior entry of row $n+1$ is therefore negative.

In row $n+2$, the boundary entries are 1. The entries at $k=2$
and $k=n+1$ are positive by Lemma [2](ch02-signs.md#paper-lem-second) and symmetry.
For $3\leq k\leq n$, both predecessor indices $k-1,k$ are
strictly interior to row $n+1$, so both predecessor entries are
negative. Both recurrence coefficients are again negative. Their
products, and hence their sum, are positive. This last index range
is empty when $n=2$, in which case the boundary and second-column
arguments cover the entire row. Induction proves positivity of
all even rows, and the intervening argument proves negativity of
all odd-row interior entries.

:::

::: {.corollary #paper-cor-classification status="written-proof" proof="pf-paper-cor-classification" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s3" title="Paper Corollary 3 (cor:classification)"}
For integer $m$, every positive even row is entrywise nonnegative
if and only if $m\leq-3$ or $m\geq0$. For exactly these parameters,
every positive even row is in fact strictly positive.
:::

::: {.proof #pf-paper-cor-classification}

*Written proof reproduced from Ma and Zhang, frozen manuscript version 2.*

Theorem [1](ch01-recurrence.md#paper-thm-main) covers $m\leq-3$. If $m\geq0$, both
coefficients in [(2)](ch01-recurrence.md#eq-recurrence) are at least one, so induction
gives strict positivity of every row. The two remaining integer
parameters fail already at

$$
T_m(4,2)=T_m(4,3)=2m^2+6m+3=-1
 \qquad(m=-1,-2).
$$

:::

Odd-row boundary entries remain 1; the theorem asserts negativity only in the interior. This card makes that restriction visible.

::: {.viz src="step-triangle" preset="odd" height="500"}
**Row 5 is negative only in its interior.** At step $-3$, magenta appears between two positive boundary entries, illustrating [@paper-thm-main].
:::

The excluded parameters need a counterexample, not merely a failed proof method. Row 4 supplies one.

::: {.viz src="step-triangle" preset="excluded" height="500"}
**The two middle entries of row 4 at step $-1$ are $-1$.** Magenta marks the failure in [@paper-cor-classification]; this is a finite illustration.
:::

Compare the familiar case where both weights are 1. This comparison follows the recurrence rather than extrapolating a negative-step picture.

::: {.viz src="step-triangle" preset="pascal" height="500"}
**Step $0$ gives Pascal’s triangle.** Row 6 and the other displayed rows are cyan; the page illustrates finitely many computed rows.
:::

The full lab lets you vary the step and row or click cells for values, within the first 10 rows.

::: {.viz src="step-triangle" height="620"}
**Vary the parameter and inspect the finite sign pattern.** The experiment helps explain the induction mechanism; it does not replace the written argument.
:::
