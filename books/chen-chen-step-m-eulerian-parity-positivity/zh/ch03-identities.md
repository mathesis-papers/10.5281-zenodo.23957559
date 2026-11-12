# 3. 行和与根的范围

逐项求出一行可能很费力，但把递推相加就简单多了。上一行的一个数贡献到下一行两个位置；它的两个权重之和恰好与位置无关。于是二维三角形的计算化为一维乘积。对于偶数行，镜像位置一奇一偶，相同的数在交错和中恰好抵消。

以下结论回应三个 OEIS 条目中相邻的 COMMENTS。这里先讨论同一递推的有限行恒等式与根界，而不是根的渐近增长。

::: {.corollary #paper-cor-sums title="原文推论 4（cor:sums）" status="written-proof" proof="pf-paper-cor-sums" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s4"}
对每个实数 $m$，

$$
S_n(m):=\sum_{k=1}^n T_m(n,k)
 =\prod_{j=0}^{n-2}(mj+2),\qquad S_1(m)=1.
$$

当 $n$ 为偶数时，

$$
R_{m,n}(-1)=0,\qquad
 \sum_{\substack{1\leq k\leq n\\ k\text{ odd}}}T_m(n,k)
 =\sum_{\substack{1\leq k\leq n\\ k\text{ even}}}T_m(n,k)
 =\tfrac12 S_n(m).
$$
:::

::: {.proof #pf-paper-cor-sums}
*书面证明来自 Ma 和 Zhang 冻结手稿第 2 版。*

对 $n\geq3$，仅为求和把上一行在三角形外延拓为零。式 (2) 在 $k=1,n$ 时也给出边界值 1。上一行位置 $j$ 的项所获得的总系数是

$$
\bigl(m(n-j-1)+1\bigr)+\bigl(m(j-1)+1\bigr)=m(n-2)+2.
$$

因此 $S_n=(m(n-2)+2)S_{n-1}$。由 $S_2=2$ 得到乘积式。$n$ 为偶数时，反射把相同的项配到奇偶相反的位置 $k$ 和 $n+1-k$；它们对 $R_{m,n}(-1)$ 的贡献抵消，奇数位置与偶数位置的和相等。
:::

多项式的根可能是复数。“环域”只限制离原点的距离，不要求根为实数。下面的两个半径由同一行的相邻系数比值决定，可以随行号变化；不能把它理解为所有归一化根都落在一个固定环域中。

::: {.corollary #paper-cor-annulus title="原文推论 5（cor:annulus）" status="written-proof" proof="pf-paper-cor-annulus" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s5"}
对实数 $m\leq-3$ 及偶数 $n\geq2$，$R_{m,n}$ 的每个根 $z$ 满足

$$
L_n\leq |z|\leq U_n,\qquad
 L_n=\min_{1\leq k<n}\frac{T_m(n,k)}{T_m(n,k+1)},\quad
 U_n=\max_{1\leq k<n}\frac{T_m(n,k)}{T_m(n,k+1)}.
$$

这些比值都为正；对称性还给出 $L_nU_n=1$。
:::

::: {.proof #pf-paper-cor-annulus}
*这是 Eneström–Kakeya 界 [[7](references.md#bib-kakeya)]；以下为冻结手稿给出的、包含边界情形的书面论证。*

设 $P(z)=\sum_{j=0}^d a_jz^j$，$a_j>0$。令 $U=\max_{0\leq j<d}a_j/a_{j+1}$、$b_j=a_jU^j$，则 $b_0\leq\cdots\leq b_d$。若 $Q(w)=P(Uw)$ 有根满足 $|w|>1$，由恒等式

$$
(1-w)Q(w)=b_0+\sum_{j=1}^d(b_j-b_{j-1})w^j-b_dw^{d+1}
$$

可得

$$
b_d|w|^{d+1}
 \leq b_0+\sum_{j=1}^d(b_j-b_{j-1})|w|^j
 \leq b_d|w|^d,
$$

矛盾。对 $z^dP(1/z)$ 应用该上界，就得到下界。定理 1 保证这里系数为正。反射使连续系数比值的集合在取倒数下不变，所以 $L_n=1/U_n$。
:::
