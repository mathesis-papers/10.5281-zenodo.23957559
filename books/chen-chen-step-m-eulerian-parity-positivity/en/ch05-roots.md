# 5. Root growth and the source's limiting constants

A root far from zero feels the leading coefficients most strongly. Reflection identifies those coefficients with the first columns of the triangle. Usually the second column supplies the largest exponential scale and the rescaled root equation becomes linear. At $m=-3$, the third column takes over: the correct limiting equation is quadratic. This change is why substituting $m=-3$ into a guessed universal growth law gives the wrong answer.

The proof below uses Rouché’s theorem, a complex-analysis tool: if a perturbation is smaller than a comparison polynomial on a closed contour, the two polynomials have the same number of zeros inside it. The argument must both produce roots near the predicted locations and exclude roots farther away; one direction alone would not establish the largest modulus.

For $n\geq2$, let $M_n(m)$ be the largest modulus among the roots
of $R_{m,n}$. The following corrects the $m=-3$ instance of
[[6](references.md#bib-chen), p. 1, Theorem 1; pp. 2–3, tables], and proves the
two other listed negative-step limiting constants.

::: {.theorem #paper-thm-growth status="written-proof" proof="pf-paper-thm-growth" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s7" title="Paper Theorem 7 (thm:growth)"}
For every real $m>0$ and every real $r\geq4$,

$$
\frac{M_n(m)}{(m+1)^n}\longrightarrow\frac{2}{m(m+1)},\qquad
 \frac{M_n(-r)}{(r-1)^n}\longrightarrow\frac{2}{r(r-1)}.
$$

At step $-3$, instead,

$$
\frac{M_n(-3)}{5^{n/2}}\longrightarrow\frac1{\sqrt{45}},\qquad
 \lim_{n\to\infty}\frac{\log M_n(-3)}n=\tfrac12\log5.
$$

In particular, $M_n(-4)/3^n\to1/6$ and
$M_n(-5)/4^n\to1/10$, whereas $M_n(-3)/2^n\to\infty$.
The proposed growth invariance between steps $1$ and $-3$ fails.
:::

::: {.proof #pf-paper-thm-growth}

*Written proof reproduced from Ma and Zhang, frozen manuscript version 2.*

Write $a_j(n)=T_m(n,j+1)$; reflection also makes it the
coefficient of $y^{n-1-j}$. Solving the second-column recurrence
gives, for $m\ne0$ and $n\geq2$,

<a id="eq-column2"></a>

**Equation (7).**

$$
a_1(n)=\frac{2(m+1)^{n-1}}m-n+1-\frac2m.
$$

Substitution and $a_1(2)=1$ verify it. At $m=-3$, the next column
satisfies $a_2(n+1)=(7-3n)a_1(n)-5a_2(n)$, with $a_2(3)=1$.
Consequently

<a id="eq-column3"></a>

**Equation (8).**

$$
a_2(n)=\frac{(-5)^n}{45}
       +\left(\frac59-\frac n3\right)(-2)^n
       +\frac{n^2}2-\frac{13n}6+\frac{20}9
       \quad(n\geq3),
$$

again verified by substitution and the initial value.

Here is a uniform bound for the remaining columns. Extend each row
by zeros outside its triangular domain. The same recurrence then
holds at its endpoints. A path from row 1 to position $j+1$ of
row $n$ has $j$ index-increasing steps and $n-1-j$ other steps.
There are $\binom{n-1}{j}$ such paths. Every increasing-step weight
has modulus at most $(|m|+1)n$. The other weights have modulus at
most $B_j=1+mj$ for $m>0$, or $B_j=rj-1$ for $m=-r$, $r\geq3$.
Therefore, for $1\leq j\leq n-1$,

<a id="eq-pathbound"></a>

**Equation (9).**

$$
|a_j(n)|\leq[(|m|+1)n^2]^j B_j^{\,n-1-j}.
$$

For $m>0$, $B_j^{1/j}\leq\sqrt{1+2m}$ for $j\geq2$:
$\log(1+mx)/x$ decreases for $x>0$, since
$\log(1+v)>v/(1+v)$ for $v>0$.
For $r\geq4$, $B_j^{1/j}\leq\sqrt{2r-1}$ for $j\geq2$;
here $\log(rx-1)/x$ decreases for $x\geq2$, since
$\log(rx-1)>rx/(rx-1)$ when $rx-1\geq7$.
For $r=3$ and $j\geq3$, $3j-1\leq2^j$ by induction.

In the first two cases put respectively $L_n=(m+1)^n$ and
$L_n=(r-1)^n$. Since
$\sqrt{1+2m}<m+1$ and $\sqrt{2r-1}<r-1$ for these parameters,
[(9)](ch05-roots.md#eq-pathbound) implies

<a id="eq-tail"></a>

**Equation (10).**

$$
|a_j(n)|/L_n^j\leq\epsilon_n^j\quad(j\geq2),
 \qquad \epsilon_n\longrightarrow0.
$$

One may take $\epsilon_n=(|m|+1)n^2(b/\lambda)^n$,
where $(b,\lambda)$ is the corresponding pair of bases above.
On every region $|z|\geq\delta>0$, the equation for a nonzero
root $y=L_nz$, divided by $L_n^{n-1}z^{n-2}$, is

$$
z+\frac{a_1(n)}{L_n}
    +\sum_{j=2}^{n-1}\frac{a_j(n)}{L_n^j}z^{1-j}=0.
$$

The last sum is bounded by
$\delta\sum_{j\geq2}(\epsilon_n/\delta)^j\to0$, uniformly on
that region. By [(7)](ch05-roots.md#eq-column2), the linear part tends to
$z+c$, with $c=2/[m(m+1)]$ for $m>0$, or to
$z+(-1)^nc$, with $c=2/[r(r-1)]$ for $m=-r$.
On a small circle about its nonzero limiting zero, the error is
smaller than the linear part for large $n$.
Rouché's theorem [[2](references.md#bib-dlmf), §1.10(iv)] gives a root there.
For $|z|\geq c+\eta$, the linear part has modulus at least
$\eta/2$ for large $n$, and the same estimate excludes roots.
Thus the largest scaled root modulus tends to $c$.

For $m=-3$ put $L_n=5^{n/2}$. The final column bound above gives
[(10)](ch05-roots.md#eq-tail) for $j\geq3$, with
$\epsilon_n=4n^2(2/\sqrt5)^n$.
Divide the root equation instead by $L_n^{n-1}z^{n-3}$.
The same geometric estimate makes its tail tend uniformly to zero
on $|z|\geq\delta$. Equations [(7)](ch05-roots.md#eq-column2)–[(8)](ch05-roots.md#eq-column3)
give the limiting quadratic

$$
z^2+(-1)^n/45.
$$

Its two simple zeros have modulus $1/\sqrt{45}$. Apply Rouché's
theorem on small circles about them, separately for even and odd
$n$. For $|z|\geq1/\sqrt{45}+\eta$, the full quadratic part
has modulus at least

$$
|z|^2-|a_1(n)/L_n|\,|z|-|a_2(n)/L_n^2|,
$$

which is bounded away from zero for large $n$.
The uniform tail estimate therefore excludes exterior roots.
This proves the remaining limit and its logarithmic consequence.
At $m=1$ the first limit gives exponent $\log2$, so the stated
mirror invariance is false for this pair.

:::

For a concrete finite bound, the accompanying exact checker gives

$$
5^{200}/7<M_{400}(-3)<5^{200}/6.
$$

On $|z|=1/7$ and $1/6$, the quadratic $z^2+1/45$ has modulus
at least $4/2205$ and $1/180$, respectively, whereas the preceding
error bound is less than $10^{-6}$. Comparing with
$z^{397}(z^2+1/45)$ gives 397 zeros inside the first circle and
all 399 inside the second. Exactly two lie between them.

The $m=-1$ coefficient formula already appears in Greubel's
1 March 2022 addition to OEIS A144431, FORMULA [[1](references.md#bib-oeislinked)].
Its factorization gives the following boundary-case root description.

::: {.corollary #paper-cor-boundaryroots status="written-proof" proof="pf-paper-cor-boundaryroots" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s8" title="Paper Corollary 8 (cor:boundaryroots)"}
For $q\geq1$, the two excluded integer steps satisfy

$$
R_{-1,2q}(y)=R_{-2,2q}(y)=(1-y)^{2q-2}(1+y),
$$

and

$$
R_{-1,2q+1}(y)=(1-y)^{2q-2}(1+y^2),\qquad
 R_{-2,2q+1}(y)=(1-y)^{2q}.
$$

Thus $M_n(-1)=M_n(-2)=1$ for $n\geq2$; both growth exponents
are zero. Also $R_{0,n}=(1+y)^{n-1}$. For $m>0$ and $n\geq2$,
every root of $R_{m,n}$ is simple and negative. At $m=-3$,
nonreal roots occur already in row 6.
:::

::: {.proof #pf-paper-cor-boundaryroots}

*Written proof reproduced from Ma and Zhang, frozen manuscript version 2.*

The factor formulas follow from [(5)](ch04-alternating-sums.md#eq-poly) in successive
even–odd pairs, starting with $R_{m,2}=1+y$ and
$R_{-1,3}=1+y^2$, $R_{-2,3}=(1-y)^2$.
At $m=0$, [(5)](ch04-alternating-sums.md#eq-poly) multiplies by $1+y$ at each step.
For $m>0$, at a negative simple zero $x$ of $R_{m,n}$,
[(5)](ch04-alternating-sums.md#eq-poly) has sign opposite to $R'_{m,n}(x)$.
The intermediate value theorem gives one zero between each pair
of consecutive negative zeros, one between the rightmost zero
and 0, and one to the left of the leftmost zero (the leading
coefficient is 1). These $n$ distinct zeros exhaust degree $n$;
induction starts at $R_{m,2}=1+y$.
Finally,

$$
R_{-3,6}(y)=(y+1)(y^4+16y^3+246y^2+16y+1).
$$

For real $y\ne0$, the quartic divided by $y^2$ is
$(y+y^{-1}+8)^2+180>0$, so its four roots are nonreal.

:::

The zero exponent at $m=-1$ corrects the summary's
page-2 entry $\beta=-\infty$. A monic polynomial with constant
term 1 has product of root moduli 1, hence $M_n\geq1$.
This also rules out the source's formula $\beta(m)=\log|m+1|$
when $0<|m+1|<1$. For $|m+1|>1$, the root $-1$ in every
even row scales to modulus $|m+1|^{-n}\to0$: an annulus with a
fixed positive inner radius cannot contain *all* scaled zeros.
The finite-row annulus of Corollary [5](ch03-identities.md#paper-cor-annulus) remains valid.
