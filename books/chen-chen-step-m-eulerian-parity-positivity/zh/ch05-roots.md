# 5. 最大根的增长与边界情形

离原点很远的根主要受多项式最高次的几个系数影响。反射把这些系数变成三角形最前面的几列。通常第二列决定指数尺度，缩放后的根方程趋于一次式；$m=-3$ 时却由第三列主导，极限方程变成二次式。这解释了为什么不能把一个猜测的通用公式直接代入 $m=-3$。

对 $n\geq2$，用 $M_n(m)$ 表示 $R_{m,n}$ 各根模的最大值。以下修正 [[6](references.md#bib-chen)，第 1 页定理 1 及第 2–3 页表格] 的 $m=-3$ 情形，并证明另外两个列出的负步长极限常数。

::: {.theorem #paper-thm-growth title="原文定理 7（thm:growth）" status="written-proof" proof="pf-paper-thm-growth" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s7" doi="10.5281/zenodo.23957560" source="Theorem 7 (thm:growth)" request="https://github.com/the-omega-institute/trureturing-requests/issues/8"}
对每个实数 $m>0$ 和每个实数 $r\geq4$，

$$
\frac{M_n(m)}{(m+1)^n}\longrightarrow\frac{2}{m(m+1)},\qquad
 \frac{M_n(-r)}{(r-1)^n}\longrightarrow\frac{2}{r(r-1)}.
$$

而在步长 $-3$，

$$
\frac{M_n(-3)}{5^{n/2}}\longrightarrow\frac1{\sqrt{45}},\qquad
 \lim_{n\to\infty}\frac{\log M_n(-3)}n=\tfrac12\log5.
$$

特别地，$M_n(-4)/3^n\to1/6$，$M_n(-5)/4^n\to1/10$，但 $M_n(-3)/2^n\to\infty$。步长 $1$ 与 $-3$ 之间所提出的增长不变性不成立。
:::

这里用到的 Rouché 定理说：如果在一条闭曲线上，扰动项的模严格小于比较函数的模，两者在曲线内部的零点数相同（计重数）。要证明“最大根模”的极限，既要找到靠近预测位置的根，也要排除更外面的根。只找到一个根还不够。

::: {.proof #pf-paper-thm-growth}
*以下保留 Ma 和 Zhang 冻结手稿第 2 版的书面论证与参数范围。*

记 $a_j(n)=T_m(n,j+1)$；由反射，它也是 $y^{n-1-j}$ 的系数。解第二列递推，对 $m\ne0$、$n\geq2$ 得

<a id="eq-column2"></a>

**式 (7)。**

$$
a_1(n)=\frac{2(m+1)^{n-1}}m-n+1-\frac2m.
$$

代入递推并检查 $a_1(2)=1$ 即可验证。在 $m=-3$ 时，下一列满足 $a_2(n+1)=(7-3n)a_1(n)-5a_2(n)$，$a_2(3)=1$。于是

<a id="eq-column3"></a>

**式 (8)。**

$$
a_2(n)=\frac{(-5)^n}{45}
       +\left(\frac59-\frac n3\right)(-2)^n
       +\frac{n^2}2-\frac{13n}6+\frac{20}9
       \quad(n\geq3).
$$

同样由代入和初值验证。

接下来统一控制其余各列。把每行在三角形外补零后，同一递推也适用于端点。从第 1 行走到第 $n$ 行位置 $j+1$ 的路径，包含 $j$ 次指标增加和 $n-1-j$ 次指标不变，共 $\binom{n-1}{j}$ 条。每个指标增加步骤的权重模至多为 $(|m|+1)n$。其余步骤权重模的上界在 $m>0$ 时为 $B_j=1+mj$，在 $m=-r$、$r\geq3$ 时为 $B_j=rj-1$。因此对 $1\leq j\leq n-1$，

<a id="eq-pathbound"></a>

**式 (9)。**

$$
|a_j(n)|\leq[(|m|+1)n^2]^j B_j^{\,n-1-j}.
$$

当 $m>0$，对 $j\geq2$ 有 $B_j^{1/j}\leq\sqrt{1+2m}$：由于 $v>0$ 时 $\log(1+v)>v/(1+v)$，函数 $\log(1+mx)/x$ 在 $x>0$ 上递减。对 $r\geq4$，$j\geq2$ 时有 $B_j^{1/j}\leq\sqrt{2r-1}$；这里 $rx-1\geq7$ 时 $\log(rx-1)>rx/(rx-1)$，故 $\log(rx-1)/x$ 在 $x\geq2$ 上递减。对 $r=3$、$j\geq3$，归纳得到 $3j-1\leq2^j$。

前两种情形分别取 $L_n=(m+1)^n$、$L_n=(r-1)^n$。因为 $\sqrt{1+2m}<m+1$，且这些参数下 $\sqrt{2r-1}<r-1$，式 (9) 给出

<a id="eq-tail"></a>

**式 (10)。**

$$
|a_j(n)|/L_n^j\leq\epsilon_n^j\quad(j\geq2),
 \qquad \epsilon_n\longrightarrow0.
$$

可取 $\epsilon_n=(|m|+1)n^2(b/\lambda)^n$，其中 $(b,\lambda)$ 为上述对应的底数。在任意 $|z|\geq\delta>0$ 上，令非零根 $y=L_nz$，将根方程除以 $L_n^{n-1}z^{n-2}$，得到

$$
z+\frac{a_1(n)}{L_n}
    +\sum_{j=2}^{n-1}\frac{a_j(n)}{L_n^j}z^{1-j}=0.
$$

最后一项在该区域上一致地由 $\delta\sum_{j\geq2}(\epsilon_n/\delta)^j\to0$ 控制。由式 (7)，一次部分在 $m>0$ 时趋于 $z+c$，$c=2/[m(m+1)]$；在 $m=-r$ 时趋于 $z+(-1)^nc$，$c=2/[r(r-1)]$。

在其非零极限零点周围的小圆上，当 $n$ 充分大时，误差小于一次部分。由 Rouché 定理 [[2](references.md#bib-dlmf)，§1.10(iv)]，圆内有根。对 $|z|\geq c+\eta$，当 $n$ 充分大，一次部分的模至少为 $\eta/2$，同样的误差估计排除外部根。因此最大缩放根模趋于 $c$。

对 $m=-3$，取 $L_n=5^{n/2}$。上述最后一种列界使式 (10) 在 $j\geq3$ 时成立，可取 $\epsilon_n=4n^2(2/\sqrt5)^n$。这次将根方程除以 $L_n^{n-1}z^{n-3}$。同一几何级数估计使尾项在 $|z|\geq\delta$ 上一致趋于零。式 (7)–(8) 给出极限二次式

$$
z^2+(-1)^n/45.
$$

其两个简单零点的模均为 $1/\sqrt{45}$。分别对偶数和奇数 $n$，在两个零点周围的小圆上应用 Rouché 定理。对 $|z|\geq1/\sqrt{45}+\eta$，完整二次部分的模至少为

$$
|z|^2-|a_1(n)/L_n|\,|z|-|a_2(n)/L_n^2|,
$$

当 $n$ 充分大时远离零。一致尾项估计因而排除外部根。这证明剩余极限及其对数结论。$m=1$ 时第一个极限给出指数 $\log2$，所以这对步长并不具有所述镜像增长不变性。
:::

手稿还给出具体有限界：随附精确检查器得到

$$
5^{200}/7<M_{400}(-3)<5^{200}/6.
$$

在 $|z|=1/7$ 和 $1/6$ 上，二次式 $z^2+1/45$ 的模分别至少为 $4/2205$ 和 $1/180$，上述误差界小于 $10^{-6}$。与 $z^{397}(z^2+1/45)$ 比较，第一条圆内有 397 个零点，第二条圆内包含全部 399 个零点，恰好两个在两圆之间。这是手稿的有限结论，不能以一个数值图取代相应误差界。

$m=-1$ 的系数公式已出现在 Greubel 于 2022 年 3 月 1 日补入 OEIS A144431 的 FORMULA 中 [[1](references.md#bib-oeislinked)]。其因式分解导出下列边界根描述。

::: {.corollary #paper-cor-boundaryroots title="原文推论 8（cor:boundaryroots）" status="written-proof" proof="pf-paper-cor-boundaryroots" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s8" doi="10.5281/zenodo.23957560" source="Corollary 8 (cor:boundaryroots)" request="https://github.com/the-omega-institute/trureturing-requests/issues/9"}
对 $q\geq1$，两个被排除的整数步长满足

$$
R_{-1,2q}(y)=R_{-2,2q}(y)=(1-y)^{2q-2}(1+y),
$$

且

$$
R_{-1,2q+1}(y)=(1-y)^{2q-2}(1+y^2),\qquad
 R_{-2,2q+1}(y)=(1-y)^{2q}.
$$

因此 $n\geq2$ 时 $M_n(-1)=M_n(-2)=1$，两者的增长指数均为零。此外 $R_{0,n}=(1+y)^{n-1}$。对 $m>0$、$n\geq2$，$R_{m,n}$ 的每个根都是简单负实根。在 $m=-3$ 时，第 6 行就已出现非实根。
:::

::: {.proof #pf-paper-cor-boundaryroots}
*书面证明来自 Ma 和 Zhang 冻结手稿第 2 版。*

从 $R_{m,2}=1+y$、$R_{-1,3}=1+y^2$、$R_{-2,3}=(1-y)^2$ 出发，在连续的偶数—奇数行对上应用式 (5)，得到各因式分解。$m=0$ 时，式 (5) 每一步都乘以 $1+y$。

当 $m>0$，在 $R_{m,n}$ 的负简单零点 $x$ 处，式 (5) 的符号与 $R'_{m,n}(x)$ 相反。介值定理在相邻负零点之间、最右零点与 0 之间、最左零点左侧各给出一个零点；最后一处使用首项系数为 1。这 $n$ 个互异零点穷尽次数 $n$，从 $R_{m,2}=1+y$ 开始归纳即可。

最后，

$$
R_{-3,6}(y)=(y+1)(y^4+16y^3+246y^2+16y+1).
$$

当实数 $y\ne0$ 时，四次式除以 $y^2$ 等于 $(y+y^{-1}+8)^2+180>0$，所以其四个根均非实数。
:::

$m=-1$ 的零指数修正了摘要第 2 页的 $\beta=-\infty$。常数项为 1 的首一多项式，其各根模之积为 1，所以 $M_n\geq1$；这也排除 $0<|m+1|<1$ 时的公式 $\beta(m)=\log|m+1|$。当 $|m+1|>1$，每个偶数行的根 $-1$ 缩放后模为 $|m+1|^{-n}\to0$，故内半径固定为正的环域不能容纳所有缩放根。推论 5 的有限行环域仍然有效。
