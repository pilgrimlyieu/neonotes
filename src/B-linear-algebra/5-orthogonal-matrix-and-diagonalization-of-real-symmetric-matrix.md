---
layout: post
title: 正交矩阵及实对称矩阵的对角化
date: 2023-11-29 15:43:26
updated: 2023-12-08 11:08:09
description: 《线性代数》笔记
draft: false
comments: true
disableNunjucks: true
katex: true
---

### 矩阵可对角化

若 $n$ 阶方阵 $\bm{A}$ 相似于一个对角矩阵，即存在可逆矩阵 $\bm{P}$ 使

$$
\bm{P}^{-1}\bm{A}\bm{P} = \bm{\Lambda}
$$

则称 $\bm{A}$ **可对角化**。

!!! info ""
    $n$ 阶方阵 $\bm{A}$ 可对角化的充要条件是 $\bm{A}$ 有 $n$ 个线性无关的特征向量。

    ---

    证明：

    $\impliedby$：

    已知 $\bm{A}$ 有 $n$ 个线性无关的特征向量 $\bm{\eta}_1,\, \bm{\eta}_2,\, \cdots,\, \bm{\eta}_n$

    设

    $$
    \left\lbrace\begin{aligned}
    \bm{A}\bm{\eta}_1 &= \lambda_1\bm{\eta}_1 \\
    \bm{A}\bm{\eta}_2 &= \lambda_2\bm{\eta}_2 \\
    \vdots \\
    \bm{A}\bm{\eta}_n &= \lambda_n\bm{\eta}_n
    \end{aligned}\right.
    $$

    记 $\bm{P} = \begin{bmatrix} \bm{\eta}_1 & \bm{\eta}_2 & \cdots & \bm{\eta}_n \end{bmatrix}$，则 $\left\lvert P \right\rvert\ne 0$，即 $\bm{P}$ 可逆。

    $$
    \begin{aligned}
        \bm{A} \bm{P} &= \bm{A} \begin{bmatrix} \bm{\eta}_1 & \bm{\eta}_2 & \cdots & \bm{\eta}_n \end{bmatrix} \\
        &= \begin{bmatrix} \bm{A}\bm{\eta}_1 & \bm{A}\bm{\eta}_2 & \cdots & \bm{A}\bm{\eta}_n \end{bmatrix} \\
        &= \begin{bmatrix} \lambda_1\bm{\eta}_1 & \lambda_2\bm{\eta}_2 & \cdots & \lambda_n\bm{\eta}_n \end{bmatrix} \\
        &= \begin{bmatrix} \bm{\eta}_1 & \bm{\eta}_2 & \cdots & \bm{\eta}_n \end{bmatrix} \begin{bmatrix} \lambda_1 & & & \\ & \lambda_2 & & \\ & & \ddots & \\ & & & \lambda_n \end{bmatrix} \\
        &= \bm{P} \bm{\Lambda}
    \end{aligned}
    $$

    所以

    $$
    \bm{P}^{-1}\bm{A}\bm{P} = \bm{\Lambda}
    $$

    $\implies$：

    设 $\bm{\Lambda} = \begin{bmatrix} \lambda_1 & & & \\ & \lambda_2 & & \\ & & \ddots & \\ & & & \lambda_n \end{bmatrix}$

    则 $\exist_{\bm{P},\, |\bm{P}| \ne 0},\,\bm{P}^{-1}\bm{A}\bm{P} = \bm{\Lambda}$，则

    $$
    \bm{P} \bm{A} = \bm{P}\bm{\Lambda}
    $$

    记 $\bm{P} = \begin{bmatrix} \bm{\eta}_1 & \bm{\eta}_2 & \cdots & \bm{\eta}_n \end{bmatrix}$，则

    $$
    \begin{aligned}
        A \begin{bmatrix} \bm{\eta}_1 & \bm{\eta}_2 & \cdots & \bm{\eta}_n \end{bmatrix} &= \begin{bmatrix} \bm{\eta}_1 & \bm{\eta}_2 & \cdots & \bm{\eta}_n \end{bmatrix} \\
        &\kern{1em}\begin{bmatrix} \lambda_1 & & & \\ & \lambda_2 & & \\ & & \ddots & \\ & & & \lambda_n \end{bmatrix}\\
        \begin{bmatrix} \bm{A}\bm{\eta}_1 & \bm{A}\bm{\eta}_2 & \cdots & \bm{A}\bm{\eta}_n \end{bmatrix} &= \begin{bmatrix} \lambda_1\bm{\eta}_1 & \lambda_2\bm{\eta}_2 & \cdots & \lambda_n\bm{\eta}_n \end{bmatrix} \\
    \end{aligned}
    $$

    所以

    $$
    \left\lbrace\begin{aligned}
    \bm{A}\bm{\eta}_1 &= \lambda_1\bm{\eta}_1 \\
    \bm{A}\bm{\eta}_2 &= \lambda_2\bm{\eta}_2 \\
    \vdots \\
    \bm{A}\bm{\eta}_n &= \lambda_n\bm{\eta}_n
    \end{aligned}\right.
    $$

    而 $\bm{P}$ 可逆，所以 $\bm{\eta}_1,\, \bm{\eta}_2,\, \cdots,\, \bm{\eta}_n$ 线性无关。

    ---

    若 $\bm{A}$ 特征值没有重根（即恰有 $n$ 个不同的特征值），则 $\bm{A}$ 可对角化[^1]。

    [^1]: 之前已证过不同特征值对应的特征向量线性无关。

!!! note ""
    幂零矩阵不可对角化。

    ---

    证明：

    $\bm{O}$ 显然成立。

    假设 $\bm{A} \ne \bm{O}$ 可对角化，则存在可逆矩阵 $\bm{P}$ 使

    $$
    \bm{P}^{-1}\bm{A}\bm{P} = \begin{bmatrix}
    \lambda_1 & & & \\
    & \lambda_2 & & \\
    & & \ddots & \\
    & & & \lambda_n
    \end{bmatrix}
    $$

    又因为

    $$
    \bm{P}^{-1}\bm{A}^k\bm{P} = \bm{\Lambda}^k
    $$

    由于 $\bm{A}$ 幂零，故 $\bm{A}^k = \bm{O}$，即

    $$
    \bm{P}^{-1}\bm{A}^k\bm{P} = \bm{O}
    $$

    所以

    $$
    \lambda_1^k = \lambda_2^k = \cdots = \lambda_n^k = 0
    $$

    即 $\lambda_1 = \lambda_2 = \cdots = \lambda_n = 0$，那么

    $$
    \bm{A} = \bm{P}\bm{\Lambda}\bm{P}^{-1} = \bm{O}
    $$

    与 $\bm{A} \ne \bm{O}$ 矛盾，所以 $\bm{A}$ 不可对角化。

    ---

    除此以外，若 $\bm{J}$ 为幂零矩阵，则 $k \bm{E} + \bm{J}$（若尔当分解型）也不可对角化。

!!! note ""
    设 $\lambda_1,\, \lambda_1,\, \cdots,\, \lambda_m$ 为 $n$ 阶方阵 $\bm{A}$ 所有相异的特征值，对于每个 $i = 1,\, \cdots,\, m$，记 $\bm{\eta}_{i1},\, \bm{\eta}_{i2},\, \cdots,\, \bm{\eta}_{is_i}$ 为 $\bm{A}$ 关于 $\lambda_i$ 的所有线性无关的特征向量，其中 $s_i$ 为 $\lambda_i$ 的代数重数，则向量组

    $$
    \begin{aligned}
        &\bm{\eta}_{11},\, \bm{\eta}_{12},\, \cdots,\, \bm{\eta}_{1s_1},\,\\
        &\bm{\eta}_{21},\, \bm{\eta}_{22},\, \cdots,\, \bm{\eta}_{2s_2},\, \\
        &\cdots,\, \\
        &\bm{\eta}_{m1},\, \bm{\eta}_{m2},\, \cdots,\, \bm{\eta}_{ms_m}
    \end{aligned}
    $$

    也线性无关。

    ---

    证明：

    设 $\exist_{k_{11},\, k_{12},\, \cdots,\, k_{1s_1},\, k_{21},\, k_{22},\, \cdots,\, k_{2s_2},\, \cdots,\, k_{m1},\, k_{m2},\, \cdots,\, k_{ms_m}}$ 使

    $$
    \begin{aligned}
        &\overbrace{\left(k_{11}\bm{\eta}_{11} + k_{12}\bm{\eta}_{12} + \cdots + k_{1s_1}\bm{\eta}_{1s_1}\right)}^{\bm{\beta}_1} &+ \\
        &\overbrace{\left(k_{21}\bm{\eta}_{21} + k_{22}\bm{\eta}_{22} + \cdots + k_{2s_2}\bm{\eta}_{2s_2}\right)}^{\bm{\beta}_2} &+ \\
        &\cdots &+ \\
        &\overbrace{\left(k_{m1}\bm{\eta}_{m1} + k_{m2}\bm{\eta}_{m2} + \cdots + k_{ms_m}\bm{\eta}_{ms_m}\right)}^{\bm{\beta}_m} &= \bm{\theta}
    \end{aligned}
    $$

    即

    $$
    \bm{\beta}_1 + \bm{\beta}_2 + \cdots + \bm{\beta}_m = \bm{\theta}\tag{1}
    $$

    其中

    $$
    \left\lbrace\begin{aligned}
        \bm{A} \bm{\beta}_1 &= \lambda_1 \bm{\beta}_1 \\
        \bm{A} \bm{\beta}_2 &= \lambda_2 \bm{\beta}_2 \\
        \vdots \\
        \bm{A} \bm{\beta}_m &= \lambda_m \bm{\beta}_m \tag{2}
    \end{aligned}\right.
    $$

    不妨设 $\bm{\beta}_{j_1},\, \bm{\beta}_{j_2},\, \cdots,\, \bm{\beta}_{j_t}$ 为 $\bm{\beta}_1,\, \bm{\beta}_2,\, \cdots,\, \bm{\beta}_m$ 中不为 $\bm{\theta}$ 的向量，其中 $t \le m$，则由 $(1)$ 有

    $$
    \bm{\beta}_{j_1} + \bm{\beta}_{j_2} + \cdots + \bm{\beta}_{j_t} = \bm{\theta}\tag{3}
    $$

    由 $(2)$ 有 $\bm{\beta}_{j_1},\, \bm{\beta}_{j_2},\, \cdots,\, \bm{\beta}_{j_t}$ 为 $\bm{A}$ 关于 $\lambda_{j_1},\, \lambda_{j_2},\, \cdots,\, \lambda_{j_t}$ 的特征向量，且 $\lambda_{j_1},\, \lambda_{j_2},\, \cdots,\, \lambda_{j_t}$ 相异，所以 $\bm{\beta}_{j_1},\, \bm{\beta}_{j_2},\, \cdots,\, \bm{\beta}_{j_t}$ 线性无关，从而与 $(3)$ 矛盾（线性无关的向量组无法被线性表示为零向量）。

    所以 $\bm{\beta}_1,\, \bm{\beta}_2,\, \cdots,\, \bm{\beta}_m$ 中不为 $\bm{\theta}$ 的向量个数 $t = 0$，即 $\bm{\beta}_1,\, \bm{\beta}_2,\, \cdots,\, \bm{\beta}_m$ 全为 $\bm{\theta}$。

    而 $\forall_{i},\,\bm{\beta}_{i} = \bm{\theta}$，且有 $\bm{\eta}_{i1},\, \bm{\eta}_{i2},\, \cdots,\, \bm{\eta}_{is_i}$ 线性无关，所以 $k_{i1} = k_{i2} = \cdots = k_{is_i} = 0$，得证。

!!! info ""
    $n$ 阶方阵 $\bm{A}$ 特征多项式有因式分解

    $$
    \left\lvert \lambda \bm{E} - \bm{A} \right\rvert = (\lambda - \lambda_1)^{n_1}(\lambda - \lambda_2)^{n_2}\cdots(\lambda - \lambda_m)^{n_m}
    $$

    其中 $\lambda_1,\, \lambda_2,\, \cdots,\, \lambda_m$ 为 $\bm{A}$ 的所有相异的特征值，$n_1,\, n_2,\, \cdots,\, n_m$ 分别为 $\lambda_1,\, \lambda_2,\, \cdots,\, \lambda_m$ 的**代数重数**，$n_i \ge 1$ 且 $n_1 + n_2 + \cdots + n_m = n$。

    方程 $(\lambda_i \bm{E} - \bm{A}) \bm{x} = \bm{\theta}$ 的基础解系的个数，即 $ n - \rank(\lambda_i \bm{E} - \bm{A})$，称为 $\lambda_i$ 的**几何重数**。

!!! note ""
    几何重数 $\le$ 代数重数。

    设 $\lambda_0$ 是 $\bm{A}$ 的 $k$ 重特征值，则其几何重数 $\le k$，即 $\lambda_0$ 的线性无关的特征向量个数不超过 $k$ 个。

    ---

    证明：

    设 $(\lambda_0 \bm{E} - \bm{A})\bm{x} = \bm{\theta}$ 的基础解系为 $\bm{\eta}_1,\, \bm{\eta}_2,\, \cdots,\, \bm{\eta}_s \in \R^{n}$。

    则

    $$
    \left\lbrace\begin{aligned}
        \bm{A} \bm{\eta}_1 &= \lambda_0 \bm{\eta}_1 \\
        \bm{A} \bm{\eta}_2 &= \lambda_0 \bm{\eta}_2 \\
        \vdots \\
        \bm{A} \bm{\eta}_s &= \lambda_0 \bm{\eta}_s \\
    \end{aligned}\right.
    $$

    将 $\bm{\eta}_1,\, \bm{\eta}_2,\, \cdots,\, \bm{\eta}_s$ 扩充为 $\R^{n}$ 的一组线性无关的向量组 $\bm{\eta}_1,\, \bm{\eta}_2,\, \cdots,\, \bm{\eta}_s,\, \bm{\eta}_{s+1},\, \cdots,\, \bm{\eta}_{n}$[^2]。

    [^2]: 可扩充的证明：$\operatorname{span}\left\lbrace \bm{\eta}_1,\, \bm{\eta}_2,\, \cdots,\, \bm{\eta}_s \right\rbrace = \left\lbrace k_1\bm{\eta}_1 + k_2\bm{\eta}_2 + \cdots + k_s\bm{\eta}_s \mid \forall_{k_i},\,k_i \in \R \right\rbrace$，则 $\exist_{\bm{\eta}_{s+1}},\,\bm{\eta}_{s+1} \notin \operatorname{span}\left\lbrace \bm{\eta}_1,\, \bm{\eta}_2,\, \cdots,\, \bm{\eta}_s \right\rbrace$，则 $\bm{\eta}_1,\, \bm{\eta}_2,\, \cdots,\, \bm{\eta}_s,\, \bm{\eta}_{s+1}$ 线性无关，以此类推。

    则

    $$
    \begin{aligned}
        \bm{A} \bm{\eta}_{s+1} &= c_{1, s+1} \bm{\eta}_1 + \cdots + c_{s, s+1} \bm{\eta}_s + c_{s+1, s+1} \bm{\eta}_{s+1} + \cdots + c_{n, s+1} \bm{\eta}_{n} \\
        \vdots\\
        \bm{A} \bm{\eta}_{n} &= c_{1, n} \bm{\eta}_1 + \cdots + c_{s, n} \bm{\eta}_s + c_{s+1, n} \bm{\eta}_{s+1} + \cdots + c_{n, n} \bm{\eta}_{n}
    \end{aligned}
    $$

    即

    $$
    \begin{aligned}
        \begin{bmatrix}
            \bm{A} \bm{\eta}_1 & \cdots & \bm{A} \bm{\eta}_n
        \end{bmatrix} &= \begin{bmatrix}
            \bm{\eta}_1 & \cdots & \bm{\eta}_s & \bm{\eta}_{s+1} & \cdots & \bm{\eta}_{n}
        \end{bmatrix}\\
        &\kern{1em}\begin{bmatrix}
        \begin{array}{ccc:ccc}
            \lambda_0 & & & c_{1, s+1} & \cdots & c_{1, n} \\
            & \ddots & & \vdots & \ddots & \vdots \\
            & & \lambda_0 & c_{s, s+1} & \cdots & c_{s, n} \\
            \hdashline
            & & & c_{s+1, s+1} & \cdots & c_{s+1, n} \\
            & & & \vdots & \ddots & \vdots \\
            & & & c_{n, s+1} & \cdots & c_{n, n}
        \end{array}
        \end{bmatrix}\\
        &= \begin{bmatrix}
            \bm{\eta}_1 & \cdots & \bm{\eta}_s & \bm{\eta}_{s+1} & \cdots & \bm{\eta}_{n}
        \end{bmatrix} \begin{bmatrix}
            \lambda_0 \bm{E}_s & \bm{C}_1 \\
            \bm{O} & \bm{C}_2
        \end{bmatrix}
    \end{aligned}
    $$

    记 $\bm{P} = \begin{bmatrix} \bm{\eta}_1 & \cdots & \bm{\eta}_s & \bm{\eta}_{s+1} & \cdots & \bm{\eta}_{n} \end{bmatrix}$，则

    $$
    \begin{aligned}
        \bm{A} \bm{P} &= \bm{P} \begin{bmatrix}
            \lambda_0 \bm{E}_s & \bm{C}_1 \\
            \bm{O} & \bm{C}_2
        \end{bmatrix}\\
        \bm{P}^{-1} \bm{A} \bm{P} &= \begin{bmatrix}
            \lambda_0 \bm{E}_s & \bm{C}_1 \\
            \bm{O} & \bm{C}_2
        \end{bmatrix}\\
        &= \bm{B}
    \end{aligned}
    $$

    即 $\bm{A}$ 与 $\bm{B}$ 相似。

    又

    $$
    \begin{aligned}
        \left\lvert \lambda \bm{E} - \bm{B} \right\rvert &= \begin{vmatrix} (\lambda - \lambda_0)\bm{E}_s & -\bm{C}_1 \\ \bm{O} & \lambda \bm{E}_{n-s} - \bm{C}_2 \end{vmatrix}\\
        &= \left\lvert (\lambda - \lambda_0) \bm{E}_s\right\rvert \left\lvert \lambda \bm{E}_{n-s} - \bm{C}_2 \right\rvert\\
        &= (\lambda - \lambda_0)^s \left\lvert \lambda \bm{E}_{n-s} - \bm{C}_2 \right\rvert\\
        &= (\lambda - \lambda_0)^s f_{\bm{C}_2}(\lambda)
    \end{aligned}
    $$

    $\lambda_0$ 至少为 $\bm{B}$ 的 $s$ 重特征值。

    又 $\left\lvert \lambda \bm{E} - \bm{A} \right\rvert = (\lambda - \lambda_0)^{k}h(\lambda)$[^3]（$\lambda_0$ 不是 $h(\lambda)=0$ 的根，因为 $\lambda_0$ 只是 $\bm{A}$ 的 $k$ 重特征值），且 $\left\lvert \lambda \bm{E} - \bm{A} \right\rvert = \left\lvert \lambda \bm{E} - \bm{B} \right\rvert$，所以 $s \le k$。否则若 $s > k$，则 $\lambda_0$ 至少为 $\bm{A}$ 的 $s$ 重特征值，与 $\lambda_0$ 为 $\bm{A}$ 的 $k$ 重特征值矛盾。

    ---

    锚点有点问题，Admonition 里的锚点是单独放在 Admonition 里面的，然而锚点地址是一样的，导致这里的第一个锚点（以及后面的唯一锚点）都会跳转到上面的锚点。这个问题，以及 Admonition 内代码块渲染的问题都是因为 Admonition 里面的内容是单独渲染的，我也没暂时没有解决方案，只能说 Admonition 里的锚点尽量少用吧。

    [^3]: $h(\lambda)$ 与前面的 $f_{\bm{C}_2}(\lambda)$ 都是关于 $\lambda$ 的多项式。

<details>
<summary>大分块矩阵源码</summary>

```latex
\begin{bmatrix}
    \begin{array}{cccc:ccc}
        \lambda_0 & & & c_{1, s+1} & \cdots & c_{1, n} \\
        & \ddots & & \vdots & \ddots & \vdots \\
        & & \lambda_0 & c_{s, s+1} & \cdots & c_{s, n} \\
        \hdashline
        & & & c_{s+1, s+1} & \cdots & c_{s+1, n} \\
        & & & \vdots & \ddots & \vdots \\
        & & & c_{n, s+1} & \cdots & c_{n, n}
    \end{array}
\end{bmatrix}
```

</details>

### 正交矩阵

!!! info ""
    设 $\bm{\alpha},\, \bm{\beta}$ 为 $n$ 维向量，按列向量表示为

    $$
    \bm{\alpha} = \begin{pmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{pmatrix},\quad \bm{\beta} = \begin{pmatrix} b_1 \\ b_2 \\ \vdots \\ b_n \end{pmatrix}
    $$

    若 $\bm{\alpha},\, \bm{\beta}$ 为<u>实向量</u>，则称

    $$
    \sum_{i=1}^n a_i b_i
    $$

    为 $\bm{\alpha},\, \bm{\beta}$ 的**内积**，记为 $(\bm{\alpha}, \bm{\beta})$。

    即

    $$
    (\bm{\alpha}, \bm{\beta}) = \bm{\alpha}^\intercal \bm{\beta}
    $$

    若 $\bm{\alpha},\, \bm{\beta}$ 为<u>复向量</u>，则称

    $$
    \sum_{i=1}^n a_i \bar{b}_i
    $$

    为 $\bm{\alpha}, \bm{\beta}$ 的**内积**，记为 $(\bm{\alpha}, \bm{\beta})$[^1]。

    即

    $$
    (\bm{\alpha}, \bm{\beta}) = \bm{\alpha}^\intercal \bar{\bm{\beta}}
    $$

    [^1]: $\bar{b}_i$ 表示 $b_i$ 的<u>共轭复数</u>。使用共轭复数，可保证对复向量 $\bm{\alpha} = \left( a_1, a_2, \cdots, a_n \right)^\intercal$，有 $(\bm{\alpha}, \bm{\alpha}) = \displaystyle \sum_{i=1}^{n}\left\lvert a_i \right\rvert^2$。

!!! note ""
    后面讨论的大都是实向量。而实向量内积的性质，都比较容易，不再赘述。

    然而遗憾的是，一个比较基本的性质，即<u>可交换性</u>，对于复向量内积来说，却不再成立，也即

    $$
    (\bm{\alpha}, \bm{\beta}) \neq (\bm{\beta}, \bm{\alpha})
    $$

    这也难怪，看复向量内积的定义，看起来就不太对称的样子。而复向量内积那样定义，是为了保证模定义的有意义性。

!!! info ""
    并记

    $$
    \|\bm{\alpha}\| = \sqrt{(\bm{\alpha}, \bm{\alpha})}
    $$

    为 $\bm{\alpha}$ 的**模**。

!!! info ""
    若 $(\bm{\alpha}, \bm{\beta}) = 0$，则称 $\bm{\alpha},\, \bm{\beta}$ **正交**（**垂直**）。

    若 $\bm{\alpha},\, \bm{\beta}$ 不为零向量，则称

    $$
    \theta = \arccos \left(\frac{(\bm{\alpha}, \bm{\beta})}{\|\bm{\alpha}\| \boldsymbol{\cdot}  \|\bm{\beta}\|}\right),\quad 0 \le \theta \le \pi
    $$

    为 $\bm{\alpha},\, \bm{\beta}$ 的**夹角**。

!!! info ""
    若一个<u>不含零向量</u>的向量组 $\left\lbrace \bm{\alpha}_i \right\rbrace$ 中的任意两个向量都正交，则称 $\left\lbrace \bm{\alpha}_i \right\rbrace$ 为**正交向量组**。

    若一个<u>不含零向量</u>的向量组 $\{\bm{\alpha}_i\}$ 中的任意两个向量都正交，且 $\{\bm{\alpha}_i\}$ 中任意向量的模都为 $1$，则称 $\{\bm{\alpha}_i\}$ 为**标准正交向量组**，简称**法正交组**，还可表示为

    $$
    (\bm{\alpha}_i, \bm{\alpha}_j) = \begin{cases} 1, & i = j \\ 0, & i \neq j \end{cases}
    $$

!!! note ""
    若 $\left\lbrace \bm{\alpha}_i \right\rbrace_m$ 为正交向量组，则 $\left\lbrace \bm{\alpha}_i \right\rbrace_m$ 线性无关。

    设

    $$
    k_1 \bm{\alpha}_1 + k_2 \bm{\alpha}_2 + \cdots + k_m \bm{\alpha}_m = \bm{\theta} \tag{1}
    $$

    对式 $(1)$ 左乘 $\bm{\alpha}_i^\intercal$，得

    $$
    \begin{aligned}
        \sum_{j=1}^{n}(\bm{\alpha}_i, k_j \bm{\alpha}_j) &= 0 & \implies \\
        k_i (\bm{\alpha}_i, \bm{\alpha}_i) &= 0 & \implies \\
        k_i &= 0
    \end{aligned}
    $$

    从而 $\forall_{i = 1, 2, \cdots, m},\, k_i = 0$，即 $\left\lbrace \bm{\alpha}_i \right\rbrace_m$ 线性无关。

!!! note ""
    对 $\bm{\alpha} \in \R^n$ 与法正交组 $\left\lbrace \bm{e}_i \right\rbrace_n$，有

    $$
    \bm{\alpha} = \sum_{i=1}^{n}(\bm{\alpha}, \bm{e}_i) \bm{e}_i
    $$

### 施密特正交化

!!! info 施密特正交化
    设 $\left\lbrace \bm{\alpha}_i \right\rbrace_n$ 为线性无关的向量组，目标是构造出等价的正交向量组 $\left\lbrace \bm{\beta}_i \right\rbrace_n$。

    不妨取 $\bm{\beta}_1 = \bm{\alpha}_1 \ne \bm{\theta}$。

    而 $\bm{\alpha}_2$ 在 $\bm{\beta}_1$ 的投影向量为 $\dfrac{(\bm{\alpha}_2, \bm{\beta}_1)}{\| \bm{\beta}_1 \|} \dfrac{\bm{\beta}_1}{\| \bm{\beta}_1 \|}$（第一个分式是投影长度，第二个分式是投影方向的单位向量），于是取

    $$
    \bm{\beta}_2 = \bm{\alpha}_2 - \frac{(\bm{\alpha}_2, \bm{\beta}_1)}{\| \bm{\beta}_1 \|^2} \bm{\beta}_1
    $$

    则 $\bm{\beta}_2$ 与 $\bm{\beta}_1$ 正交，同时显然 $\bm{\beta}_2 \ne \bm{\theta}$，否则 $\bm{\alpha}_1,\, \bm{\alpha}_2$ 共线，与 $\left\lbrace \bm{\alpha}_i \right\rbrace_n$ 线性无关矛盾。

    同理设 $\bm{\beta}_3 = \bm{\alpha}_3 - c_1 \bm{\beta}_1 - c_2 \bm{\beta}_2$，其中 $c_1,\, c_2$ 为待定系数，使得 $\bm{\beta}_3$ 与 $\bm{\beta}_1,\, \bm{\beta}_2$ 都正交，即

    $$
    \begin{aligned}
        (\bm{\beta}_3, \bm{\beta}_1) = 0 &\implies (\bm{\alpha}_3 - c_1 \bm{\beta}_1 - c_2 \bm{\beta}_2, \bm{\beta}_1) = 0 \\
        &\implies (\bm{\alpha}_3, \bm{\beta}_1) - c_1 (\bm{\beta}_1, \bm{\beta}_1) - c_2 (\bm{\beta}_2, \bm{\beta}_1) = 0 \\
        &\implies (\bm{\alpha}_3, \bm{\beta}_1) - c_1 \| \bm{\beta}_1 \|^2 = 0 \\
        &\implies c_1 = \frac{(\bm{\alpha}_3, \bm{\beta}_1)}{\| \bm{\beta}_1 \|^2}
    \end{aligned}
    $$

    同理可得 $c_2 = \dfrac{(\bm{\alpha}_3, \bm{\beta}_2)}{\| \bm{\beta}_2 \|^2}$，于是取

    $$
    \bm{\beta}_3 = \bm{\alpha}_3 - \frac{(\bm{\alpha}_3, \bm{\beta}_1)}{\| \bm{\beta}_1 \|^2} \bm{\beta}_1 - \frac{(\bm{\alpha}_3, \bm{\beta}_2)}{\| \bm{\beta}_2 \|^2} \bm{\beta}_2
    $$

    显然 $\bm{\beta}_3$ 与 $\bm{\beta}_1,\, \bm{\beta}_2$ 都正交，同时 $\bm{\beta}_3 \ne \bm{\theta}$。

    以此类推，设 $\bm{\beta}_k = \bm{\alpha}_k - c_1 \bm{\beta}_1 - c_2 \bm{\beta}_2 - \cdots - c_{k-1} \bm{\beta}_{k-1}$ 与 $\bm{\beta}_1,\, \bm{\beta}_2, \cdots, \bm{\beta}_{k-1}$ 都正交，且 $\bm{\beta}_k \ne \bm{\theta}$，则

    $$
    \begin{aligned}
        (\bm{\beta}_k, \bm{\beta}_1) = 0 &\implies (\bm{\alpha}_k - c_1 \bm{\beta}_1 - c_2 \bm{\beta}_2 - \cdots - c_{k-1} \bm{\beta}_{k-1}, \bm{\beta}_1) = 0 \\
        &\implies (\bm{\alpha}_k, \bm{\beta}_1) - c_1 (\bm{\beta}_1, \bm{\beta}_1) - c_2 (\bm{\beta}_2, \bm{\beta}_1) - \cdots - c_{k-1} (\bm{\beta}_{k-1}, \bm{\beta}_1) = 0 \\
        &\implies (\bm{\alpha}_k, \bm{\beta}_1) - c_1 \| \bm{\beta}_1 \|^2 = 0 \\
        &\implies c_1 = \frac{(\bm{\alpha}_k, \bm{\beta}_1)}{\| \bm{\beta}_1 \|^2}
    \end{aligned}
    $$

    同理可得 $c_2 = \dfrac{(\bm{\alpha}_k, \bm{\beta}_2)}{\| \bm{\beta}_2 \|^2},\, \cdots,\, c_{k-1} = \dfrac{(\bm{\alpha}_k, \bm{\beta}_{k-1})}{\| \bm{\beta}_{k-1} \|^2}$，于是取

    $$
    \begin{aligned}
        \bm{\beta}_k &= \bm{\alpha}_k - \frac{(\bm{\alpha}_k, \bm{\beta}_1)}{\| \bm{\beta}_1 \|^2} \bm{\beta}_1 - \frac{(\bm{\alpha}_k, \bm{\beta}_2)}{\| \bm{\beta}_2 \|^2} \bm{\beta}_2 - \cdots - \frac{(\bm{\alpha}_k, \bm{\beta}_{k-1})}{\| \bm{\beta}_{k-1} \|^2} \bm{\beta}_{k-1}\\
        &= \boxed{\bm{\alpha}_{\textcolor{FF0099}{k}} - \sum_{\textcolor{82B1F5}{i}=1}^{\textcolor{FF0099}{k - 1}} \frac{(\bm{\alpha}_{\textcolor{FF0099}{k}}, \bm{\beta}_{\textcolor{82B1F5}{i}})}{\| \bm{\beta}_{\textcolor{82B1F5}{i}} \|^2} \bm{\beta}_{\textcolor{82B1F5}{i}}}
    \end{aligned}
    $$

    <details>
    <summary>碎碎念</summary>

    ~~最后的公式在 light 模式看不清，主要是因为我自己主要看 dark 模式，而且调一下 light 和 dark 都明显的颜色挺麻烦的，所以就算了。~~

    还是找了一下，根据[一个 StackExchange 的回答](https://graphicdesign.stackexchange.com/a/162285)分别用了 `#FF0099` 和 `#0099FF`，`#FF0099` 挺完美的，效果很理想，`#0099FF` 不太行，还稍微牺牲了一下 dark 模式的对比度，只不过 Ta 给的颜色里也没找到更好的了。

    我自己改了一下，把 `#0099FF` 改为了 `#82B1F5`，这样就不会牺牲 dark 模式的对比度了，而且 light 模式也不会太难看，唯一有个缺点就是不如 `#FF0099` 那么醒目，但是我觉得这个缺点可以接受。

    </details>

!!! info ""
    若实方阵 $\bm{A}$ 满足 $\bm{A}^\intercal \bm{A} = \bm{E}$，则称 $\bm{A}$ 为**正交矩阵**。

!!! note ""
    对方阵 $\bm{A}$，以下表述等价：
    1. $\bm{A}$ 为正交矩阵
    2. $\bm{A}^\intercal \bm{A} = \bm{E}$
    3. $\bm{A}^\intercal = \bm{A}^{-1}$
    4. $\bm{A}$ 的列向量构成法正交组
    5. $\bm{A}$ 的行向量构成法正交组

    ---

    证明：

    前三者等价性显然。

    (4) (5) $\implies$ (1)：（这里演示 (4) $\implies$ (1)，(5) $\implies$ (1) 同理）

    对于法正交组 $\left\lbrace \bm{\alpha}_i \right\rbrace_n$，设 $\bm{A} = \begin{bmatrix} \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n \end{bmatrix}$，则

    $$
    \bm{A}^\intercal = \begin{bmatrix} \bm{\alpha}_1^\intercal \\ \bm{\alpha}_2^\intercal \\ \vdots \\ \bm{\alpha}_n^\intercal \end{bmatrix}
    $$

    从而

    $$
    \begin{aligned}
        \bm{A}^\intercal \bm{A} &= \begin{bmatrix} \bm{\alpha}_1^\intercal \\ \bm{\alpha}_2^\intercal \\ \vdots \\ \bm{\alpha}_n^\intercal \end{bmatrix} \begin{bmatrix} \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n \end{bmatrix} \\
        &= \begin{bmatrix} \bm{\alpha}_1^\intercal \bm{\alpha}_1 & \bm{\alpha}_1^\intercal \bm{\alpha}_2 & \cdots & \bm{\alpha}_1^\intercal \bm{\alpha}_n \\ \bm{\alpha}_2^\intercal \bm{\alpha}_1 & \bm{\alpha}_2^\intercal \bm{\alpha}_2 & \cdots & \bm{\alpha}_2^\intercal \bm{\alpha}_n \\ \vdots & \vdots & \ddots & \vdots \\ \bm{\alpha}_n^\intercal \bm{\alpha}_1 & \bm{\alpha}_n^\intercal \bm{\alpha}_2 & \cdots & \bm{\alpha}_n^\intercal \bm{\alpha}_n \end{bmatrix} \\
        &= \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix} \\
        &= \bm{E}
    \end{aligned}
    $$

    从而 $\bm{A}$ 为正交矩阵。

    (1) $\implies$ (4)：（这里演示 (1) $\implies$ (4)，(1) $\implies$ (5) 同理）

    设 $\bm{A}$ 为正交矩阵，即 $\bm{A}^\intercal \bm{A} = \bm{E}$，设 $\bm{A} = \begin{bmatrix} \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n \end{bmatrix}$，则同理

    $$
    \begin{aligned}
        \bm{A}^\intercal \bm{A} &= \bm{E} &\implies \\
        \begin{bmatrix} \bm{\alpha}_1^{\intercal} \bm{\alpha}_1 & \bm{\alpha}_1^{\intercal} \bm{\alpha}_2 & \cdots & \bm{\alpha}_1^{\intercal} \bm{\alpha}_n \\ \bm{\alpha}_2^{\intercal} \bm{\alpha}_1 & \bm{\alpha}_2^{\intercal} \bm{\alpha}_2 & \cdots & \bm{\alpha}_2^{\intercal} \bm{\alpha}_n \\ \vdots & \vdots & \ddots & \vdots \\ \bm{\alpha}_n^{\intercal} \bm{\alpha}_1 & \bm{\alpha}_n^{\intercal} \bm{\alpha}_2 & \cdots & \bm{\alpha}_n^{\intercal} \bm{\alpha}_n \end{bmatrix} &= \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix} &\implies \\
        \bm{\alpha}_i^\intercal \bm{\alpha}_j &= \begin{cases} 1, & i = j \\ 0, & i \neq j \end{cases}
    \end{aligned}
    $$

    即 $\left\lbrace \bm{\alpha}_i \right\rbrace_n$ 为法正交组。

!!! note ""
    设二阶方阵

    $$
    \bm{A} = \begin{bmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{bmatrix}
    $$

    为正交矩阵，则由 $\bm{A}^\intercal = \bm{A}^{-1}$ 可得

    $$
    \begin{bmatrix} a_{11} & a_{21} \\ a_{12} & a_{22} \end{bmatrix} = \dfrac{1}{\left\lvert \bm{A} \right\rvert} \begin{bmatrix} a_{22} & -a_{12} \\ -a_{21} & a_{11} \end{bmatrix}
    $$

    Case 1: $\left\lvert \bm{A} \right\rvert = 1$

    从而

    $$
    \left\lbrace\begin{aligned}
        a_{11} &= a_{22} \\
        a_{21} &= -a_{12}
    \end{aligned}\right.
    $$

    而

    $$
    \begin{aligned}
        \left\lvert \bm{A} \right\rvert &= a_{11} a_{22} - a_{12} a_{21} \\
        &= a_{11}^2 + a_{21}^2 \\
        &= 1
    \end{aligned}
    $$

    从而存在 $\theta \in \left[ 0, 2\pi \right)$，使得

    $$
    \left\lbrace\begin{aligned}
        a_{11} &= \cos \theta \\
        a_{21} &= \sin \theta
    \end{aligned}\right.
    $$

    即

    $$
    \bm{A} = \begin{bmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix}
    $$

    即 $\bm{A}$ 代表的线性变换为<u>绕原点**逆时针**旋转 $\theta$</u>。

    Case 2: $\left\lvert \bm{A} \right\rvert = -1$

    从而

    $$
    \left\lbrace\begin{aligned}
        a_{11} &= -a_{22} \\
        a_{21} &= a_{12}
    \end{aligned}\right.
    $$

    而

    $$
    \begin{aligned}
        \left\lvert \bm{A} \right\rvert &= a_{11} a_{22} - a_{12} a_{21} \\
        &= -a_{11}^2 - a_{21}^2 \\
        &= -1
    \end{aligned}
    $$

    从而同样存在 $\theta \in \left[ 0, 2\pi \right)$，使得

    $$
    \left\lbrace\begin{aligned}
        a_{11} &= \cos \theta \\
        a_{21} &= \sin \theta
    \end{aligned}\right.
    $$

    即

    $$
    \bm{A} = \begin{bmatrix} \cos \theta & \sin \theta \\ \sin \theta & -\cos \theta \end{bmatrix}
    $$

    则

    $$
    \bm{A} = \begin{bmatrix}
        \cos \theta & - \sin \theta \\
        \sin \theta & \cos \theta
    \end{bmatrix} \begin{bmatrix}
        1 & 0 \\
        0 & -1
    \end{bmatrix}
    $$

    即 $\bm{A}$ 代表的线性变换为<u>先关于 $x$ 轴对称（反射），再绕原点**逆时针**旋转 $\theta$</u>。

!!! note ""
    旋转矩阵似乎会改变全部向量的方向，也就是说，似乎找不到特征向量。实际上其特征值为复数，特征向量为复向量。

    实际上有

    $$
    \left\lbrace\begin{aligned}
        \lambda_1 &= \e ^{\i \theta} \\
        \lambda_2 &= \e ^{-\i \theta}
    \end{aligned}\right.
    $$

!!! note ""
    设 $\bm{A}$ 为 $n$ 阶正交矩阵（正交矩阵要求为实矩阵），$\lambda$ 为 $\bm{A}$ 的特征值，$\bm{\alpha},\, \bm{\beta} \in \R^n$，则

    1. $\bm{A}^\intercal,\,  \bm{A}^k,\, \bm{A}^{-1},\, \bm{A}^{*}$ 也是正交矩阵
    2. $\left\lvert \bm{A} \right\rvert^2 = 1$（即 $\bm{A}$ 的行列式为 $\pm 1$）
    3. $(\bm{A} \bm{\alpha}, \bm{A} \bm{\beta}) = (\bm{\alpha}, \bm{\beta})$（即 $\bm{A}$ 保持内积不变，若取 $\bm{\alpha} = \bm{\beta}$，则 $\bm{A}$ 保持长度不变，即 $\| \bm{A} \bm{\alpha} \| = \| \bm{\alpha} \|$）
    4. $\left\lvert \lambda \right\rvert = 1$（即 $\lambda = \e ^{\i \theta}$，实特征值只能为 $\pm 1$）

    ---

    1. 证明：

    $\bm{A}^\intercal,\, \bm{A}^{-1},\, \bm{A}^{*}$ 显然。

    对于 $\bm{A}^k$，有

    $$
    \begin{aligned}
        (\bm{A}^k)^\intercal \bm{A}^k &= (\overbrace{\bm{A} \bm{A} \cdots \bm{A}}^{k})^\intercal \overbrace{\bm{A} \bm{A} \cdots \bm{A}}^{k} \\
        &= \rlap{$\overbrace{\phantom{\bm{A}^\intercal \bm{A}^\intercal \cdots (\bm{A}^\intercal}}^{k}$} \bm{A}^\intercal \bm{A}^\intercal \cdots \rlap{$\underbrace{(\bm{A}^\intercal \bm{A})}_{\bm{E}}$} \phantom{(\bm{A}^\intercal \bm{A})} \bm{A} \cdots \bm{A} \llap{$\overbrace{\phantom{\bm{A}) \bm{A} \cdots \bm{A}}}^{k}$}\\
        &\kern{0.5em}\vdots \\
        &= \bm{E}
    \end{aligned}
    $$

    2. 证明：

    $\bm{A}^\intercal \bm{A} = \bm{E}$ 得

    $$
    \left\lvert \bm{A} \right\rvert^2 = \lvert \bm{A}^\intercal \rvert \left\lvert \bm{A} \right\rvert = \left\lvert \bm{E} \right\rvert = 1
    $$

    3. 证明：

    $$
    \begin{aligned}
        (\bm{A} \bm{\alpha}, \bm{A} \bm{\beta}) &= (\bm{A} \bm{\alpha})^\intercal \bm{A} \bm{\beta} \\
        &= \bm{\alpha}^\intercal \bm{A}^\intercal \bm{A} \bm{\beta} \\
        &= \bm{\alpha}^\intercal \bm{E} \bm{\beta} \\
        &= \bm{\alpha}^\intercal \bm{\beta} \\
        &= (\bm{\alpha}, \bm{\beta})
    \end{aligned}
    $$

    那么同时还有

    $$
    \begin{aligned}
    \langle \bm{A} \bm{\alpha}, \bm{A} \bm{\beta} \rangle &= \arccos \dfrac{(\bm{A} \bm{\alpha}, \bm{A} \bm{\beta})}{\| \bm{A} \bm{\alpha} \| \| \bm{A} \bm{\beta} \|} \\
    &= \arccos \dfrac{(\bm{\alpha}, \bm{\beta})}{\| \bm{\alpha} \| \| \bm{\beta} \|} \\
    &= \langle \bm{\alpha}, \bm{\beta} \rangle
    \end{aligned}
    $$

    4. 证明：

    设 $\bm{A} \bm{\eta} = \lambda \bm{\eta}$，其中 $\bm{\eta} \in \C^n \backslash \left\lbrace \bm{\theta} \right\rbrace$，则

    $$
    \begin{aligned}
        \left( \bm{A} \bm{\eta}, \bm{A} \bm{\eta} \right)_{\C} &= \left( \bm{A} \bm{\eta} \right) ^\intercal \overline{\bm{A} \bm{\eta}} \\
        &= \bm{\eta}^\intercal \bm{A}^\intercal \overline{\bm{A} \bm{\eta}} \\
        &= \bm{\eta}^\intercal \bm{A}^\intercal \bm{A} \bar{\bm{\eta}} \\
        &= \bm{\eta}^\intercal \bar{\bm{\eta}} \\
        &= \| \bm{\eta} \| ^2
    \end{aligned}
    $$

    而

    $$
    \begin{aligned}
        \left( \lambda \bm{\eta}, \lambda \bm{\eta} \right)_{\C} &= (\lambda \bm{\eta})^\intercal \overline{\lambda \bm{\eta}} \\
        &= \lambda \bar{\lambda} \bm{\eta}^\intercal \bar{\bm{\eta}} \\
        &= \left\lvert \lambda \right\rvert^2 \| \bm{\eta} \| ^2
    \end{aligned}
    $$

    从而 $\left\lvert \lambda \right\rvert^2 = 1$。

!!! note ""
    考虑 $\R^n$ 空间中两个法正交组

    $$
    \bm{A}\colon \bm{\alpha}_1 ,\, \bm{\alpha}_2 ,\, \cdots ,\, \bm{\alpha}_n
    $$

    与

    $$
    \bm{B}\colon\bm{\beta}_1 ,\, \bm{\beta}_2 ,\, \cdots ,\, \bm{\beta}_n
    $$

    则存在矩阵 $\bm{C}$，使得

    $$
    \begin{aligned}
        \bm{B} &= \bm{A} \bm{C}\\
        \begin{bmatrix}
            \bm{\beta}_1 & \bm{\beta}_2 & \cdots & \bm{\beta}_n
        \end{bmatrix} &= \begin{bmatrix}
            \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n
        \end{bmatrix} \begin{bmatrix}
            c_{11} & c_{12} & \cdots & c_{1n} \\
            c_{21} & c_{22} & \cdots & c_{2n} \\
            \vdots & \vdots & \ddots & \vdots \\
            c_{n1} & c_{n2} & \cdots & c_{nn}
        \end{bmatrix}
    \end{aligned}
    $$

    那么

    $$
    \bm{C} = \bm{A}^{-1} \bm{B}
    $$

    则 $\bm{C}$ 也是正交矩阵。

### 实对称矩阵的对角化

!!! info ""
    若 $\bm{A}$ 为 $n$ 阶实方阵，且 $\bm{A}^\intercal = \bm{A}$，则称 $\bm{A}$ 为**实对称矩阵**。

!!! note ""
    实对称矩阵的特征值一定为**实数**。

    ---

    证明：

    对实对称矩阵 $\bm{A}$，设其一特征值为 $\lambda$，则存在特征向量 $\bm{\eta} \in \C^n\backslash \left\lbrace \bm{\theta} \right\rbrace$，即 $\bm{A} \bm{\eta} = \lambda \bm{\eta}$，等价于证明 $\bar{\lambda} = \lambda$。

    $$
    \left\lbrace\begin{aligned}
        \overline{\bm{A}\bm{\eta}} &= \overline{\lambda \bm{\eta}}\\
        (\bm{A} \bm{\eta})^\intercal &= (\lambda \bm{\eta})^\intercal
    \end{aligned}\right.
    \implies
    \left\lbrace\begin{aligned}
        \bm{A} \bar{\bm{\eta}} &= \bar{\lambda} \bar{\bm{\eta}}\\
        \bm{\eta}^\intercal \bm{A} &= \lambda \bm{\eta}^\intercal
    \end{aligned}\right.
    $$

    两式分别左乘 $\bm{\eta}^\intercal$ 和右乘 $\bar{\bm{\eta}}$，得

    $$
    \left\lbrace\begin{aligned}
        \bm{\eta}^\intercal \bm{A} \bar{\bm{\eta}} &= \bar{\lambda} \bm{\eta}^\intercal \bar{\bm{\eta}} &= \bar{\lambda} \| \bm{\eta} \|^2 \\
        \bm{\eta}^\intercal \bm{A} \bar{\bm{\eta}} &= \lambda \bm{\eta}^\intercal \bar{\bm{\eta}} &= \lambda \| \bm{\eta} \|^2
    \end{aligned}\right.
    $$

    从而

    $$
    \bar{\lambda} \| \bm{\eta} \|^2 = \lambda \| \bm{\eta} \|^2
    $$

    也即

    $$
    \bar{\lambda} = \lambda
    $$

!!! note ""
    对于 $n$ 阶实对称矩阵 $\bm{A}$ 与任意向量 $\bm{\alpha},\, \bm{\beta} \in \R^n$，有

    $$
    (\bm{A} \bm{\alpha}, \bm{\beta}) = (\bm{\alpha}, \bm{A} \bm{\beta})
    $$

    ---

    证明：

    $$
    \begin{aligned}
        (\bm{A} \bm{\alpha}, \bm{\beta}) &= (\bm{A} \bm{\alpha})^\intercal \bm{\beta} \\
        &= \bm{\alpha}^\intercal \bm{A}^\intercal \bm{\beta} \\
        &= \bm{\alpha}^\intercal \bm{A} \bm{\beta} \\
        &= (\bm{\alpha}, \bm{A} \bm{\beta})
    \end{aligned}
    $$

!!! note ""
    实对称矩阵属于不同特征值的特征向量必正交。

    即对实对称矩阵 $\bm{A}$，若 $\lambda_1,\, \lambda_2$ 为不同特征值，$\bm{\eta}_1,\, \bm{\eta}_2$ 为对应的特征向量，则 $(\bm{\eta}_1, \bm{\eta}_2) = 0$。

    ---

    由上面有 $(\bm{A} \bm{\eta}_1, \bm{\eta}_2) = (\bm{\eta}_1, \bm{A} \bm{\eta}_2)$，

    从而 $(\lambda_1 \bm{\eta}_1, \bm{\eta}_2) = (\bm{\eta}_1, \lambda_2 \bm{\eta}_2)$，即 $(\lambda_1 \bm{\eta}_1, \bm{\eta}_2) = (\lambda_2 \bm{\eta}_1, \bm{\eta}_2)$，从而 $(\lambda_1 - \lambda_2) (\bm{\eta}_1, \bm{\eta}_2) = 0$，

    而 $\lambda_1 \neq \lambda_2$，从而 $(\bm{\eta}_1, \bm{\eta}_2) = 0$。

!!! info ""
    实对称矩阵必可对角化。

    对于实对称矩阵 $\bm{A} \in M_n(\R)$，存在**正交矩阵** $\bm{P}$，使得 $\bm{P}^{-1} \bm{A} \bm{P} = \bm{\Lambda}$，其中 $\bm{\Lambda}$ 为对角矩阵。

    ---

    证明：

    $\bm{A}$ 有特征值 $\lambda_1,\, \lambda_2,\, \cdots,\, \lambda_n \in \R$。

    对 $\lambda_1$，存在单位向量 $\bm{\alpha}_1 \in \R^n\backslash\left\lbrace \bm{\theta} \right\rbrace$ 使得 $\bm{A} \bm{\alpha}_1 = \lambda_1 \bm{\alpha}_1,\, \|\bm{\alpha}_1\| = 1$。

    总能将其扩充为 $\R^n$ 的一组法正交组 $\bm{P}_1\colon\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_n$（总能先扩充为一个向量组⟦上面谈过证明。由于提及的锚点问题，不设置锚点跳转，因为设置也跳转不对⟧，再使用施密特正交化，并单位化）。

    则 $\bm{P}_1 = \begin{bmatrix} \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n \end{bmatrix}$ 为正交矩阵。

    从而有

    $$
    \begin{aligned}
        \bm{A} \bm{P}_1 &= \bm{A} \begin{bmatrix} \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n \end{bmatrix} \\
        &= \begin{bmatrix} \bm{A} \bm{\alpha}_1 & \bm{A} \bm{\alpha}_2 & \cdots & \bm{A} \bm{\alpha}_n \end{bmatrix} \\
        &= \begin{bmatrix} \lambda_1 \bm{\alpha}_1 & \bm{A} \bm{\alpha}_2 & \cdots & \bm{A} \bm{\alpha}_n \end{bmatrix} \\
        &= \begin{bmatrix}
            \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n
        \end{bmatrix} \begin{bmatrix}
            \lambda_1 & a_2 & \cdots & a_n \\
            0 & * & \cdots & * \\
            \vdots & \vdots & \ddots & \vdots \\
            0 & * & \cdots & *
        \end{bmatrix} \\
        &= \bm{P}_1 \begin{bmatrix}
            \lambda_1 & \begin{matrix}
                a_2 & \cdots & a_n
            \end{matrix}\\
            \begin{matrix}
                0 \\
                \vdots \\
                0
            \end{matrix} & \LARGE\bm{A}_1
            \end{bmatrix}\\
            &= \bm{P}_1 \bm{Q}_1
    \end{aligned}
    $$

    则

    $$
    \begin{aligned}
            \bm{Q}_1 &= \bm{P}_1^{-1} \bm{A} \bm{P}_1 \\
            &= \bm{P}_1^\intercal \bm{A} \bm{P}_1
    \end{aligned}
    $$

    而

    $$
    \begin{aligned}
        \bm{Q}_1^\intercal &= \left( \bm{P}_1^\intercal \bm{A} \bm{P}_1 \right)^\intercal \\
        &= \bm{P}_1^\intercal \bm{A}^\intercal \bm{P}_1 \\
        &= \bm{P}_1^\intercal \bm{A} \bm{P}_1 \\
        &= \bm{Q}_1
    \end{aligned}
    $$

    即 $\bm{Q}_1$ 也为实对称矩阵，从而 $a_2 = a_3 = \cdots = a_n = 0$，且 $\bm{A}_1$ 为 $n - 1$ 阶实对称矩阵，特征值为 $\lambda_2,\, \lambda_3,\, \cdots,\, \lambda_n$。

    以此类推，存在正交矩阵 $\bm{P}_1,\, \bm{P}_2,\, \cdots,\, \bm{P}_n$ 使

    $$
    \bm{P}_n^\intercal \cdots \bm{P}_2^\intercal \bm{P}_1^\intercal \bm{A} \bm{P}_1 \bm{P}_2 \cdots \bm{P}_n = \bm{\Lambda}
    $$

    记

    $$
    \bm{P} = \bm{P}_1 \bm{P}_2 \cdots \bm{P}_n
    $$

    显然 $\bm{P}$ 也是正交矩阵。则

    $$
    \bm{P}^\intercal \bm{A} \bm{P} = \bm{\Lambda}
    $$

    也即

    $$
    \bm{P}^{-1} \bm{A} \bm{P} = \bm{\Lambda}
    $$
