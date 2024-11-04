---
layout: post
title: 多元函数
date: 2023-11-30 15:44:16
updated: 2024-04-30 17:50:38
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 点集基本知识

$\R^n = \left\lbrace \left( x_1, x_2, \cdots, x_n \right) \mid x_1, x_2, \cdots, x_n \in \R \right\rbrace$

!!! info ""
    设 $P_1 \left( a_1, a_2, \cdots, a_n \right),\, P_2 \left( b_1, b_2, \cdots, b_n \right)$ 是 $n$ 维空间 $\R^{n}$ 中的两个点，$P_1$ 到 $P_2$ 的**距离**定义为

    $$
    \rho \left( P_1, P_2 \right) = \sqrt{\sum_{i=1}^{n} \left( a_i - b_i \right)^2}
    $$

!!! info ""
    设 $P_0 \in \R^{n},\, \delta > 0$，则点集

    $$
    N_{\delta} \left( P_0 \right) = \left\{ P \in \R^{n} \mid \rho \left( P, P_0 \right) < \delta \right\}
    $$

    称为点 $P_0$ 的 **$\delta$ 邻域**，简称**邻域**。点集

    $$
    \mathring{N}_{\delta} \left( P_0 \right) = N_{\delta} \left( P_0 \right) \backslash \left\{ P_0 \right\}
    $$

    称为点 $P_0$ 的 **$\delta$ 去心邻域**，简称**去心邻域**。

$$
B_{\delta}(\vec{a}) = \left\{ \vec{x} \in \R^n \mid \rho \left( \vec{x}, \vec{a} \right) \le  \delta \right\}
$$

$$
S_{\delta}(\vec{a}) = \pd B_{\delta}(\vec{a}) = \left\{ \vec{x} \in \R^n \mid \rho \left( \vec{x}, \vec{a} \right) =  \delta \right\}
$$

$$
N_{\delta}(\vec{a}) = B_{\delta}(\vec{a}) \backslash S_{\delta}(\vec{a}) = \left\{ \vec{x} \in \R^n \mid \rho \left( \vec{x}, \vec{a} \right) <  \delta \right\}
$$

!!! info ""
    设点集 $G \subseteq \R^{n}$：
    1. 若 $P_0 \in G$，且存在 $\delta > 0$，使得 $N_{\delta} \left( P_0 \right) \subseteq G$，则称 $P_0$ 为 $G$ 的**内点**。$G$ 的全体内点的集合称为 $G$ 的**内部**，记作 $G^{\circ}$。
    2. 若 $P_0 \in \R^n$，且对任意 $\delta > 0$，$N_{\delta}(P_0) \cap \complement_{\R^n}G \neq \varnothing,\, N_{\delta}(P_0) \cap  G \ne \varnothing$，则称 $P_0$ 为 $G$ 的**边界点**。$G$ 的全体边界点的集合称为 $G$ 的**边界**，记作 $\partial G$。
    3. 若 $P_0 \notin G$，且存在 $\delta > 0$，使得 $N_{\delta} \left( P_0 \right) \cap G = \varnothing$，则称 $P_0$ 为 $G$ 的**外点**。$G$ 的全体外点的集合称为 $G$ 的**外部**。
    4. 若 $P_0 \in \R^{n}$，且对任意 $\delta > 0$，$\mathring{N}_{\delta} \left( P_0 \right) \cap G \neq \varnothing$，则称 $P_0$ 为 $G$ 的**聚点**。$G$ 的全体聚点的集合称为 $G$ 的**导集**。
    5. 若 $P_0 \in G$，且存在 $\delta > 0$ 使得 $\mathring{N}_{\delta} \left( P_0 \right) \cap G = \varnothing$，则称 $P_0$ 为 $G$ 的**孤立点**。

!!! note ""
    值得注意的一些「点」：
    1. <u>点集的点未必是内点</u>。例如一个点集 $G = \left\{ \left( x, y \right) \mid x^2 + y^2 \le 1 \right\}$，其内部为 $G^{\circ} = \left\{ \left( x, y \right) \mid x^2 + y^2 < 1 \right\}$，即 $\forall_{P_0 \in \partial G \subseteq G} ,\, P_0 \notin G^{\circ}$。
    2. <u>边界点未必属于点集</u>。例如一个点集 $G = \left\{ \left( x, y \right) \mid x^2 + y^2 < 1 \right\}$，其边界为 $\partial G = \left\{ \left( x, y \right) \mid x^2 + y^2 = 1 \right\}$，而 $\forall_{P_0 \in \partial G} ,\, P_0 \notin G$。
    3. <u>聚点未必属于点集</u>。例如一个点集 $G = \left\{ \left( x, y \right) \mid x^2 + y^2 < 1 \right\}$，其聚点为 $\left\{ \left( x, y \right) \mid x^2 + y^2 \le 1 \right\}$。
    4. <u>边界点未必是聚点</u>。例如孤立点是边界点，而孤立点不是聚点。
    5. <u>边界点一定不是内点</u>。
    6. <u>孤立点一定是边界点</u>。
    7. <u>内点一定是聚点</u>。
    8. <u>外点一定不是聚点</u>。

!!! info ""
    设 $G \subseteq \R^{n}$：
    1. 若 $G$ 的每个点都是 $G$ 的内点，即 $G = G^{\circ}$，则称 $G$ 为**开集**。
    2. 若 $\R^n \backslash G$ 为开集，则称 $G$ 为**闭集**。
    3. 如果点集 $G$ 任意两点可以用曲线连接，且曲线上的点都属于 $G$，则称 $G$ 为**连通集**。[^connected]
    4. 若 $G$ 既是开集又是连通集，则称 $G$ 为**开区域**。
    5. 若存在非空开区域 $A$，使 $G = A \cup \pd A$，则称 $G$ 为**闭区域**。
    6. 开区域和闭区域统称为**区域**。
    7. 规定空集 $\empty$ 和全空间 $\R^n$ <u>既是开集又是闭集</u>。除此以外任何 $\R^n$ 的非空子集不可能既是开集又是闭集。

    [^connected]: 这个定义是「道路连通（弧连通）」的定义。连通的严格定义为：若点集无法写成两个非空开集的并，则称该点集为**连通集**。道路连通一定连通，反之不一定。例如[华沙正弦曲线](https://zh.wikipedia.org/wiki/%E6%8B%93%E6%89%91%E5%AD%A6%E5%AE%B6%E7%9A%84%E6%AD%A3%E5%BC%A6%E6%9B%B2%E7%BA%BF)是连通的，但不是道路连通的。

    ---

    对于第 2 个定义，我一开始想的是「不是开集的点集称为闭集」，这个观点是错误的，详细看下面的例子。

    对于第 5 个定义，我一开始想的是「既是闭集又是连通集的点集称为闭区域」，然而对于点集 $G = \left\{ \left( x, y \right) \mid x^2 + y^2 = 1 \right\}$，这是一个闭集，也是一个连通集，但不是闭区域（因为 $G$ 没有内点，而非空开区域一定有内点，形成的并集也一定有内点）。

!!! info ""
    设 $G \subseteq \R^{n}$，$P_0 \in \R^n$。若存在 $k \in \R,\, G \subseteq N_k(P_0)$，则称 $G$ 为**有界集**，称

    $$
    d \left( G \right) = \sup \left\{ \rho \left( P_1, P_2 \right) \mid P_1, P_2 \in G \right\}
    $$

    为 $G$ 的**直径**。否则称 $G$ 为**无界集**。

    注意，是 $\sup$（上确界）而非 $\max$，因为可能并不存在最大值，例如下面的例子。

    用的是直线距离，即「外蕴距离」。两点间**内蕴距离**定义为用点集中曲线连接两点的最小长度。

!!! example ""
    来看看一个点集 $G = \left\lbrace (x) \mathrel{\biggm|} x = \dfrac{1}{n}, n \in \N^{*}  \right\rbrace$：
    1. $G$ 的内部 $G^{\circ} = \varnothing$。这是显然的，毕竟 $G$ 中的点都是孤立点。
    2. $G$ 的边界 $\partial G = G \cup \left\lbrace (0) \right\rbrace$。孤立点一定是边界点，同时点集 $G$ 的点与 $(0)$ 的距离可以任意小（即对任意 $\delta > 0$，对任意 $n \ge \left\lceil \dfrac{1}{\delta} \right\rceil$，都有 $\rho \left( \left(\dfrac{1}{n}\right), (0) \right) < \delta$），因此 $(0)$ 也是边界点。
    3. $G$ 有唯一聚点 $(0)$。跟上面一样，$G$ 的点与 $(0)$ 的距离可以任意小。
    4. $G$ 不是开集，不是闭集，也不是连通集。$G$ 内部为 $\varnothing$，则 $G$ 不是开集；$(0)$ 不是 $\R^n\backslash G$ 的内点（因为 $(0)$ 的任意邻域都包含 $G$ 中的点），则 $G$ 不是闭集；$G$ 中的点都是孤立点，因此 $G$ 不是连通集。
    5. $G$ 是有界集，且 $d \left( G \right) = 1$。$G$ 的点都在 $N_1 \left( 0 \right)$ 中，因此 $G$ 是有界集；$G$ 中点距离的上界为 $1$，因此 $d \left( G \right) = 1$。

## 多元函数

### 概念

!!! info ""
    设 $D \subseteq \R^n$，称映射
    $$
    f \colon D \to \R
    $$

    为定义在 $D$ 上的 **$n$ 元函数**。常记为

    $$
    \begin{aligned}
        y &= f(P), &P \in D\\
        y &= f(x_1, x_2, \cdots, x_n),\quad &(x_1, x_2, \cdots, x_n) \in D
    \end{aligned}
    $$

    变量 $x_1, x_2, \cdots, x_n$ 称为**自变量**，$y$ 称为**因变量**，$D$ 称为函数 $f$ 的**定义域**，记为 $D(f)$。

    $$
    f(D) = \left\{ f(P) \mid P \in D \right\}
    $$

    称为函数 $f$ 的**值域**。

    $\left\lbrace \left( \vec{x}_n, f(\vec{x}_n) \right) \subset \R^{n + 1} \mid \vec{x}_n \in D \right\rbrace$ 称为函数 $f$ 的**图像**。

    二元函数及以上的函数称为**多元函数**。

    多元隐函数、多元复合函数、多元初等函数、多元有界函数等定义与一元函数类似，不再赘述。

    ---

    我们常将二元函数 $f\colon D \to \R\;(D \subseteq \R^2)$ 记为

    $$
    z = f(x, y),\quad (x, y) \in D
    $$

    三元函数 $f\colon D \to \R\;(D \subseteq \R^3)$ 记为

    $$
    w = f(x, y, z),\quad (x, y, z) \in D
    $$

    <details>
    <summary>变量群</summary>

    - $a,\, b,\, c,\, d$
    - $i,\, j,\, k$
    - $m,\, n,\, l$
    - $p,\, q,\, r,\, s,\, t$
    - $u,\, v,\, w$
    - $x,\, y,\, z,\, w$

    </details>

## 多元函数的极限

### $n$ 重极限

仿照一元函数的极限，以及多元函数距离的定义，我们可以定义多元函数的极限。

!!! info 二重极限
    设 $D \subseteq \R^2$，函数 $f(x, y)$ 在 $D$ 上有定义，$P_0(x_0, y_0)$ 是 $D$ 的聚点。若存在常数 $A$，对于任意给定的 $\varepsilon > 0$，存在 $\delta > 0$，使得当 $P(x, y) \in D$ 且 $0 < \rho(P, P_0) < \delta$ 时，有

    $$
    \left\lvert f(P) - A \right\rvert = \left\lvert f(x, y) - A \right\rvert < \varepsilon
    $$

    则称函数 $f(x, y)$ 在 $P \to P_0$ 时以 $A$ 为极限，记为

    $$
    \lim_{P \to P_0} f(P) = A\quad\text{或}\quad f(P) \to A\quad(P \to P_0)
    $$

    也记作

    $$
    \lim_{(x, y) \to (x_0, y_0)} f(x, y) = A\quad\text{或}\quad f(x, y) \to A\quad\Bigl((x, y) \to (x_0, y_0)\Bigr)
    $$

    或

    $$
    \lim_{\substack{x \to x_0\\y\to y_0}} f(x, y) = A\quad\text{或}\quad f(x, y) \to A\quad\left(x \to x_0, y \to y_0\right)
    $$

同理有

!!! info ""
    设 $D \subseteq \R^n$，函数 $f(x_1, x_2, \cdots, x_n)$ 在 $D$ 上有定义，$P_0(x_1^0, x_2^0, \cdots, x_n^0)$ 是 $D$ 的聚点。若存在常数 $A$，对于任意给定的 $\varepsilon > 0$，存在 $\delta > 0$，使得当 $P(x_1, x_2, \cdots, x_n) \in D$ 且 $0 < \rho(P, P_0) < \delta$ 时，有

    $$
    \left\lvert f(P) - A \right\rvert = \left\lvert f(x_1, x_2, \cdots, x_n) - A \right\rvert < \varepsilon
    $$

    则称函数 $f(x_1, x_2, \cdots, x_n)$ 在 $P \to P_0$ 时以 $A$ 为极限，记为

    $$
    \lim_{P \to P_0} f(P) = A\quad\text{或}\quad f(P) \to A\quad(P \to P_0)
    $$

    也记作

    $$
    \lim_{(x_1, x_2, \cdots, x_n) \to (x_1^0, x_2^0, \cdots, x_n^0)} f(x_1, x_2, \cdots, x_n) = A\quad\text{或}\quad f(x_1, x_2, \cdots, x_n) \to A\quad\Bigl((x_1, x_2, \cdots, x_n) \to (x_1^0, x_2^0, \cdots, x_n^0)\Bigr)
    $$

    或

    $$
    \lim_{\substack{x_1 \to x_1^0\\x_2 \to x_2^0\\\vdots\\x_n \to x_n^0}} f(x_1, x_2, \cdots, x_n) = A\quad\text{或}\quad f(x_1, x_2, \cdots, x_n) \to A\quad\left(x_1 \to x_1^0, x_2 \to x_2^0, \cdots, x_n \to x_n^0\right)
    $$

与一元函数的极限类似，一元函数极限可以通过任何方式趋于极限点，并取得相同的极限值。多元函数也是如此，要求趋于极限点的路径是任意的，只要通过两条路径趋于极限点的极限值不同，就可以断定多元函数在该点极限不存在。

但同时，多元函数比起一元函数只有左右两个方向，只需判定左右极限相等，有了更多的选择，因此也更加复杂。

### 累次极限

有时需要先对其中一个变量求极限，再对另一个变量求极限，这种极限称为**累次极限**。

!!! info ""
    对于二元函数 $f(x, y)$，先把 $y$ 看作常数，求 $x \to x_0$ 时的极限，得到一个关于 $y$ 的函数 $g(y)$，即

    $$
    \lim_{x \to x_0} f(x, y) = g(y)
    $$

    再对 $y$ 求极限，即

    $$
    \lim_{y \to y_0} g(y) = A
    $$

    若两个极限均存在，则称 $A$ 为函数 $f(x, y)$ 在点 $(x_0, y_0)$ 处**先对 $x$ 后对 $y$ 的累次极限**，记作

    $$
    \lim_{y \to y_0} \lim_{x \to x_0} f(x, y) = A
    $$

    同理可定义**先对 $y$ 后对 $x$ 的累次极限**，记作

    $$
    \lim_{x \to x_0} \lim_{y \to y_0} f(x, y) = A
    $$

## 多元函数的连续性

!!! info ""
    设 $G \subseteq \R^n$，函数 $f$ 在 $G$ 上有定义，$P_0$ 是 $G$ 的聚点 且 $P_0 \in G$。若

    $$
    \lim_{P \to P_0} f(P) = f(P_0)
    $$

    则称函数 $f$ 在点 $P_0$ 处**连续**。

    若 $G$ 中每一点都是聚点，且 $f$ 在 $G$ 中每一点都连续，则称 $f$ 在 $G$ 上**连续**。

    若 $f$ 在 $P_0$ 处不连续，则称 $f$ 在 $P_0$ 处**间断**，并称 $P_0$ 为 $f$ 的**间断点**。

对二元函数 $z = f(x, y)$，记

$$
\left\lbrace\begin{aligned}
    \Delta x &= x - x_0\\
    \Delta y &= y - y_0\\
    \Delta z &= f(x, y) - f(x_0, y_0)
\end{aligned}\right.
$$

称 $\Delta x,\, \Delta y$ 分别为自变量 $x,\, y$ 的增量，$\Delta z$ 为 $f(x, y)$ 在点 $(x_0, y_0)$ 处的**全增量**。

于是连续定义等价于

$$
\lim_{\substack{\Delta x \to 0\\\Delta y \to 0}} \Delta z = 0
$$

同时，类似一元函数，多元函数也有对应的*零点定理*、*介值定理*、*有界性定理*、*最值定理*等，在此不再赘述，只需注意定理中要求 $G \subseteq \R^n$ 为<u>有界闭区域</u>。
