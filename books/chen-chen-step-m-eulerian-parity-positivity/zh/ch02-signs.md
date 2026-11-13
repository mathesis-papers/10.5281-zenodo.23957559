# 2. 为什么要一次看两行

从正的偶数行出发，两个负权重让下一奇数行的内部变负。再向下一行时，两个“负乘负”给出正数。不过第二列有一个前驱是边界的 1，不能直接使用内部的负性。引理 2 正是为这个缺口准备的。反射对称性使左边的计算同时处理右边。

先注意，对每个实数 $m$，

<a id="eq-symmetry"></a>

**式 (3)。**

$$
T_m(n,k)=T_m(n,n+1-k).
$$

反射交换两个边界。内部项的两个前驱 $k-1,k$ 在上一行分别反射为 $n+1-k,n-k$，式 (2) 的两个系数也互换。因此按 $n$ 归纳得到式 (3)。

::: {.lemma #paper-lem-second title="原文引理 2（lem:second）" status="written-proof" proof="pf-paper-lem-second" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s2" doi="10.5281/zenodo.23957560" source="Lemma 2 (lem:second)" request="https://github.com/the-omega-institute/trureturing-requests/issues/3"}
对 $r\geq3$，只要 $n\geq2$ 为偶数，就有 $T_{-r}(n,2)>0$。
:::

::: {.proof #pf-paper-lem-second}
*以下为 Ma 和 Zhang 冻结手稿第 2 版的书面证明。参数 $r$ 仍在实数范围内。*

记 $a_n=T_{-r}(n,2)$（$n\geq2$）。边界给出 $a_2=1$；在递推中令 $k=2$，得到对 $n\geq2$，

$$
a_{n+1}=1-r(n-1)+(1-r)a_n.
$$

再代入一次并合并同类项，得到

<a id="eq-twostep"></a>

**式 (4)。**

$$
a_{n+2}=(r-1)^2a_n+r(r-2)n+2-r^2.
$$

第一步要单独检查：

$$
a_4=(r-1)^2+2r(r-2)+2-r^2
     =2r(r-3)+3\geq3.
$$

对 $n\geq4$，式 (4) 的剩余项满足

$$
r(r-2)n+2-r^2
 \geq3r^2-8r+2
 =3(r-3)^2+10(r-3)+5>0.
$$

于是从 $a_4>0$ 出发，式 (4) 逐次证明后面所有偶数指标的正性。再加上 $a_2=1$，引理得证。
:::

::: {.proof #pf-paper-thm-main}
*原文定理 1 的书面证明，来自 Ma 和 Zhang 冻结手稿第 2 版。*

第 $2$ 行为 $(1,1)$。设偶数行 $n\geq2$ 严格为正。当 $1<k<n+1$ 时，定义 $T_{-r}(n+1,k)$ 的两个系数都严格为负：其中的正整数因子 $n+1-k$ 与 $k-1$ 至少为 1，所以每个系数至多为 $1-r<0$。两个前驱均在正的第 $n$ 行。因此第 $n+1$ 行的每个内部项都为负。

第 $n+2$ 行的两端是 1。位置 $k=2$ 与 $k=n+1$ 由引理 2 及对称性为正。对 $3\leq k\leq n$，两个前驱 $k-1,k$ 都严格位于第 $n+1$ 行内部，因而为负；两个递推系数也为负，所以两个乘积及其和都为正。$n=2$ 时最后这个指标区间为空，边界与第二列已经覆盖整行。归纳得到所有偶数行严格为正，中间的论证同时给出奇数行内部严格为负。
:::

该结论限制在 $m\leq-3$。若只讨论整数参数，剩下的值可以完整分类；下一条并没有声称对所有实数给出分类。

::: {.corollary #paper-cor-classification title="原文推论 3（cor:classification）" status="written-proof" proof="pf-paper-cor-classification" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s3" doi="10.5281/zenodo.23957560" source="Corollary 3 (cor:classification)" request="https://github.com/the-omega-institute/trureturing-requests/issues/4"}
对整数 $m$，每个正偶数行逐项非负，当且仅当 $m\leq-3$ 或 $m\geq0$。恰好在这些参数上，每个正偶数行实际上都严格为正。
:::

::: {.proof #pf-paper-cor-classification}
*书面证明来自 Ma 和 Zhang 冻结手稿第 2 版。*

定理 1 处理 $m\leq-3$。若 $m\geq0$，式 (2) 的两个系数都至少为 1，归纳得到每行都严格为正。剩下两个整数参数在下列位置已经失败：

$$
T_m(4,2)=T_m(4,3)=2m^2+6m+3=-1
 \qquad(m=-1,-2).
$$
:::

奇数行的两端始终是 1，定理只断言内部为负。下一张卡把这个限定直接画出来。

::: {.viz src="step-triangle" preset="odd" height="500"}
**第 5 行内部为负，两端为正。** 步长为 $-3$；品红只在内部出现。这是 [@paper-thm-main] 的有限例示。
:::

被排除的参数需要实际反例，而不只是无法套用证明；下面的第 4 行给出反例。

::: {.viz src="step-triangle" preset="excluded" height="500"}
**步长 $-1$ 的第 4 行中间两项都是 $-1$。** 品红两项说明偶数行正性失败，见 [@paper-cor-classification]；图示不是额外证明。
:::

最后回到权重都为 1 的熟悉情形，比较递推本身，而不是由负步长图像外推结论。

::: {.viz src="step-triangle" preset="pascal" height="500"}
**步长 $0$ 给出杨辉三角。** 当前第 6 行及图中其他行均为青色；这是递推的有限例示。
:::

完整实验室允许改变步长与行号、点击格子查看数值；它的范围限制在前 10 行。

::: {.viz src="step-triangle" height="620"}
**改变参数，观察有限三角形的符号。** 实验可帮助理解归纳机制，不能替代书面论证。
:::
