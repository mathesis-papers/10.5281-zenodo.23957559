# 4. Odd-row alternating sums

An even row cancels at $y=-1$ by reflection. Odd rows have a middle position, so the same pairing argument leaves something over and does not prove nonvanishing. The manuscript uses stronger arithmetic obstructions: an odd integer cannot be zero, and an integer congruent to 1 modulo 3 cannot be zero. A generating function is a way to keep the whole family of rows in a single formal series; extracting its coefficients recovers the original recurrence.

Put $A_q(m)=R_{m,2q+1}(-1)$, with $A_0(m)=1$.
The COMMENTS of A392665 and A392666 assert nonvanishing for
every odd row, not just the displayed examples.

::: {.corollary #paper-cor-odd status="written-proof" proof="pf-paper-cor-odd" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s6" title="Paper Corollary 6 (cor:odd)"}
For every integer $q\geq1$,

$$
A_q(-4)/8^q\ \hbox{is an odd integer},\qquad
 A_q(-5)\equiv1\pmod3.
$$

More generally, the first conclusion holds with $-4,8$ replaced by
$-r,2r$ for every positive integer $r$ divisible by $4$; the second
holds for every integer $m\equiv1\pmod3$. In particular, both
source nonvanishing assertions hold for all odd rows.
:::

::: {.proof #pf-paper-cor-odd}

*Written proof reproduced from Ma and Zhang, frozen manuscript version 2.*

Multiplication of the triangle recurrence by $y^{k-1}$ and summation gives

<a id="eq-poly"></a>

**Equation (5).**

$$
R_{m,n+1}(y)=[1+(m(n-1)+1)y]R_{m,n}(y)
              +my(1-y)R'_{m,n}(y).
$$

For $m\ne0$ the exponential generating function is

<a id="eq-egf"></a>

**Equation (6).**

$$
H(t,y):=\sum_{j\geq0}R_{m,j+1}(y)\frac{t^j}{j!}
 =e^{(1-y)t}\left(\frac{1-y}{1-ye^{m(1-y)t}}\right)^{2/m}.
$$

Indeed, differentiation verifies
$(1-myt)H_t=(1+y)H+my(1-y)H_y$ and $H(0,y)=1$.
Coefficient comparison gives [(5)](ch04-alternating-sums.md#eq-poly), so uniqueness proves
the formula. It is a Taylor series at $t=0$ for $y\ne1$.
At $y=-1$ it gives

$$
\sum_{q\geq0}A_q(-r)\frac{t^{2q}}{(2q)!}
       =\cosh(rt)^{2/r}.
$$

Set $C_j=(d/ds)^{2j}\log\cosh(s)|_{s=0}$.
These are integers and $C_1=1$: successive derivatives of
$\tanh s$ are integer polynomials in $\tanh s$, by
$(\tanh s)'=1-\tanh^2s$.
The logarithm of the last generating function has even derivatives
$\kappa_{2j}=2r^{2j-1}C_j$ and odd derivatives zero.
Expanding its exponential expresses $A_q(-r)$ as the sum over
partitions of $2q$ labelled elements into even blocks, with weight
$\prod_B\kappa_{|B|}$. After division by $(2r)^q$, a block of
size $2j$ contributes $(r/2)^{j-1}C_j$.
When $4\mid r$, every partition with a block larger than two
therefore contributes an even integer. The remaining
$(2q-1)!!$ pair partitions each contribute 1. This proves the
first assertion.

If $m\equiv1\pmod3$, reduction of the recurrence gives
$R_{m,n}\equiv R_{1,n}\pmod3$. The Eulerian identity

$$
R_{1,n}(y)=(1-y)^{n+1}\sum_{j\geq0}(j+1)^n y^j
$$

follows by applying $(y\,d/dy)^n$ to $y/(1-y)$ and comparing
[(5)](ch04-alternating-sums.md#eq-poly). For odd $n$, $(j+1)^n\equiv j+1\pmod3$,
so this formal identity gives
$R_{m,n}(y)\equiv(1-y)^{n-1}\pmod3$.
At $y=-1$ the value is $2^{n-1}\equiv1\pmod3$, as required.

:::
