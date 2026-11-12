# 1. 递推与猜想

读者可以把 $T_m(n,k)$ 理解为第 $n$ 行第 $k$ 个格子的值。计算一行只需前一行；我们不假定三角形外也有已经定义好的数。参数 $m=0$ 时，两个权重都为 1，得到熟悉的杨辉三角。参数变为负数后，两个负权重可能把正数变成负数，而再走一步又可能把负数变成正数。论文的关键是把这幅图景变成覆盖边界的严格归纳。

OEIS A392664–A392666 的 COMMENTS 猜测步长 $-3,-4,-5$ 的偶数行非负 [[3](references.md#bib-oeis3), [4](references.md#bib-oeis4), [5](references.md#bib-oeis5)]。Chen 和 Chen 的执行摘要把猜想推广到全部整数 $m\leq-3$，并报告上述三个参数已检查到第 400 行 [[6](references.md#bib-chen)，第 1 页猜想 2]。Ma 和 Zhang 的结论还包括所有实数 $m\leq-3$，并把非负加强为严格为正。有限检查与所有行的证明是两种不同的依据。

对实数参数 $m$，在整数指标 $1\leq k\leq n$ 上定义

<a id="eq-boundary"></a>

**式 (1)。**

$$
T_m(n,1)=T_m(n,n)=1 \qquad(n\geq1),
$$

<a id="eq-recurrence"></a>

**式 (2)。**

$$
T_m(n,k)=\bigl(m(n-k)+1\bigr)T_m(n-1,k-1)
          +\bigl(m(k-1)+1\bigr)T_m(n-1,k),
$$

其中式 (2) 只适用于 $1<k<n$。按行归纳即可得到三角形定义域上的存在性和唯一性；$m$ 为整数时所有项都是整数。递推不需要三角形外的值。

把一行作为多项式的系数，记 $R_{m,n}(y)=\sum_{k=1}^n T_m(n,k)y^{k-1}$。代入 $y=1$ 就是行和，代入 $y=-1$ 就是交错和；复根的位置则反映另一种性质，不能只凭系数正负判断其全部增长行为。

::: {.theorem #paper-thm-main title="原文定理 1（thm:main）" status="written-proof" proof="pf-paper-thm-main" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s1"}
对每个实数 $r\geq3$，步长 $m=-r$ 的三角形满足：

1. 对每个正偶数 $n$ 及 $1\leq k\leq n$，$T_{-r}(n,k)>0$；
2. 对每个奇数 $n\geq3$ 及 $1<k<n$，$T_{-r}(n,k)<0$。

特别地，三个 OEIS 猜想和 [[6](references.md#bib-chen)] 的猜想 2 在各自陈述的整数参数上成立。
:::

证明放在下一章：先解决紧靠边界的第二列，再进行两行一步的归纳。

先看一个有限例子：步长 $-3$ 的第 6 行全部为正。图中颜色只表示符号，圆大小不表示数值大小；这张图不是对所有行的证明。

::: {.viz src="step-triangle" preset="even" height="500"}
**第 6 行的内部也为正。** 当前步长为 $-3$，青色表示正项，琥珀色圈出当前项。例示对应 [@paper-thm-main]。
:::
