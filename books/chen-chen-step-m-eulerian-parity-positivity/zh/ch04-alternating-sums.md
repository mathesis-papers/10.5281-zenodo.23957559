# 4. 奇数行为什么不抵消

偶数行可以按镜像成对抵消。奇数行有中间位置，同样的配对不能直接说明交错和是否为零。手稿寻找更强的算术障碍：奇整数不可能为零，模 3 余 1 的整数也不可能为零。生成函数把所有行装进一个形式级数，再通过比较系数找回原递推。

记 $A_q(m)=R_{m,2q+1}(-1)$，$A_0(m)=1$。A392665 与 A392666 的 COMMENTS 要求所有奇数行都不为零，而不只是已经列出的样例。

::: {.corollary #paper-cor-odd title="原文推论 6（cor:odd）" status="written-proof" proof="pf-paper-cor-odd" mathesis="collected:chen-chen-step-m-eulerian-parity-positivity:2:s6" doi="10.5281/zenodo.23957560" source="Corollary 6 (cor:odd)"}
对每个整数 $q\geq1$，

$$
A_q(-4)/8^q\ \hbox{是奇整数},\qquad
 A_q(-5)\equiv1\pmod3.
$$

更一般地，对每个被 $4$ 整除的正整数 $r$，第一条结论中可把 $-4,8$ 替换为 $-r,2r$；第二条结论对每个整数 $m\equiv1\pmod3$ 都成立。因此原文的两条非零性断言对所有奇数行成立。
:::

::: {.proof #pf-paper-cor-odd}
*书面证明来自 Ma 和 Zhang 冻结手稿第 2 版。*

将三角形递推乘以 $y^{k-1}$ 并求和得

<a id="eq-poly"></a>

**式 (5)。**

$$
R_{m,n+1}(y)=[1+(m(n-1)+1)y]R_{m,n}(y)
              +my(1-y)R'_{m,n}(y).
$$

当 $m\ne0$ 时，其指数生成函数为

<a id="eq-egf"></a>

**式 (6)。**

$$
H(t,y):=\sum_{j\geq0}R_{m,j+1}(y)\frac{t^j}{j!}
 =e^{(1-y)t}\left(\frac{1-y}{1-ye^{m(1-y)t}}\right)^{2/m}.
$$

直接求导验证 $(1-myt)H_t=(1+y)H+my(1-y)H_y$ 及 $H(0,y)=1$。比较系数得到式 (5)，再由唯一性证明公式。这里取 $y\ne1$ 时 $t=0$ 处的 Taylor 级数。令 $y=-1$，得到

$$
\sum_{q\geq0}A_q(-r)\frac{t^{2q}}{(2q)!}
       =\cosh(rt)^{2/r}.
$$

设 $C_j=(d/ds)^{2j}\log\cosh(s)|_{s=0}$。这些数是整数且 $C_1=1$，因为 $(\tanh s)'=1-\tanh^2s$，故 $\tanh s$ 的各阶导数都是 $\tanh s$ 的整系数多项式。上述生成函数的对数的偶阶导数是 $\kappa_{2j}=2r^{2j-1}C_j$，奇阶导数为零。

展开指数，把 $A_q(-r)$ 表示为对 $2q$ 个带标号元素的偶数大小分块划分求和，每个划分权重为 $\prod_B\kappa_{|B|}$。除以 $(2r)^q$ 后，一个大小为 $2j$ 的块贡献 $(r/2)^{j-1}C_j$。当 $4\mid r$ 时，只要某个块大于 2，整个划分就贡献偶整数；其余 $(2q-1)!!$ 个两两配对各贡献 1。因此商为奇整数。

若 $m\equiv1\pmod3$，递推模 3 化简给出 $R_{m,n}\equiv R_{1,n}\pmod3$。将 $(y\,d/dy)^n$ 作用于 $y/(1-y)$ 并与式 (5) 比较，可得 Eulerian 恒等式

$$
R_{1,n}(y)=(1-y)^{n+1}\sum_{j\geq0}(j+1)^n y^j.
$$

奇数 $n$ 满足 $(j+1)^n\equiv j+1\pmod3$，所以这个形式恒等式给出 $R_{m,n}(y)\equiv(1-y)^{n-1}\pmod3$。令 $y=-1$，结果是 $2^{n-1}\equiv1\pmod3$，即得所需结论。
:::
