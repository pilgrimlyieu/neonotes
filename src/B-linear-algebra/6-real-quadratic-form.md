---
layout: post
title: 实二次型
date: 2023-12-08 11:03:08
updated: 2023-12-17 15:47:57
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 实二次型

### 定义

!!! info ""
    含有 $n$ 个实变量 $x_1,\, x_2,\, \cdots,\, x_n$ 的在某个数域上的二次齐次多项式

    $$
    f(x_1,\, x_2,\, \cdots,\, x_n) = \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j \qquad (a_{ij} = a_{ji})
    $$

    称为**二次型**，若全部 $a_{ij} \in \mathbb{R}$，则称为**实二次型**，若全部 $a_{ij} \in \mathbb{C}$，则称为**复二次型**。

    $$
    \begin{aligned}
    f(x_1,\, x_2,\, \cdots,\, x_n) &= \sum_{i=1}^n \sum_{j=1}^n a_{ij} x_i x_j \\
    &= \sum_{i=1}^n a_{ii} x_i^2 + \sum_{i < j}(a_{ij} + a_{ji}) x_i x_j \\
    &= \sum_{i=1}^n a_{ii} \underbrace{x_i^2}_{\text{平方项}} + 2 \sum_{i < j} a_{ij} \underbrace{x_i x_j}_{\text{交叉项}}
    \end{aligned}
    $$

    **二次型 $f$ 的矩阵表示形式**

    $$
    \begin{aligned}
        f(x_1, x_2, \cdots, x_n) &= \begin{bmatrix}
            x_1 & x_2 & \cdots & x_n
        \end{bmatrix}
        \begin{bmatrix}
            a_{11} & a_{12} & \cdots & a_{1n} \\
            a_{21} & a_{22} & \cdots & a_{2n} \\
            \vdots & \vdots & \ddots & \vdots \\
            a_{n1} & a_{n2} & \cdots & a_{nn}
        \end{bmatrix}
        \begin{bmatrix}
            x_1 \\
            x_2 \\
            \vdots \\
            x_n
        \end{bmatrix}\\
        &= \bm{x}^\intercal \bm{A} \bm{x}
    \end{aligned}
    $$

    其中 $\bm{A}$ 为对称矩阵，称为<u>二次型 $f$ 的矩阵</u>。$\bm{A}$ 的秩称为<u>二次型 $f$ 的秩</u>，即 $\rank(f) \coloneqq \rank(\bm{A})$ 。

### 实二次型的标准形

!!! info ""
    为化简二次型矩阵（仅保留平方项，消去交叉项），要进行变量代换。

    $$
    \left\lbrace\begin{aligned}
        x_1 &= c_{11} y_1 + c_{12} y_2 + \cdots + c_{1n} y_n \\
        x_2 &= c_{21} y_1 + c_{22} y_2 + \cdots + c_{2n} y_n \\
        &\kern{0.25em}\vdots \\
        x_n &= c_{n1} y_1 + c_{n2} y_2 + \cdots + c_{nn} y_n
    \end{aligned}\right.
    $$


    设 $\bm{P} = [c_{ij}]_n$ 为 $n$ 阶可逆矩阵，考虑*非退化线性变换*（又称非奇异线性变换，即 $\bm{P}$ 可逆，由此可得 $\bm{y} = \bm{P}^{-1} \bm{x}$）

    $$
    \bm{x} = \bm{P} \bm{y}
    $$

    其中 $\bm{y} = \begin{bmatrix} y_1 & y_2 & \cdots & y_n \end{bmatrix}^\intercal$ 为新变量，从而

    $$
    \begin{aligned}
        f(\bm{x}) = \bm{x}^\intercal \bm{A} \bm{x} &\xlongequal{\bm{x} = \bm{P} \bm{y}} (\bm{P} \bm{y})^\intercal \bm{A} (\bm{P} \bm{y}) \\
        &= \bm{y}^\intercal (\bm{P}^\intercal \bm{A} \bm{P}) \bm{y} \\
        &= \bm{y}^\intercal \bm{B} \bm{y}
    \end{aligned}
    $$

    设 $\bm{A},\, \bm{B}$ 为同阶方阵，若存在可逆矩阵 $\bm{P}$ 使得

    $$
    \bm{B} = \bm{P}^\intercal \bm{A} \bm{P}
    $$

    则称 $\bm{A}$ 与 $\bm{B}$ **合同**（或 $\bm{A}$ 合同于 $\bm{B}$），$\bm{B}$ 称为 $\bm{A}$ 的*合同矩阵*，$\bm{P}$ 为 $\bm{A}$ 到 $\bm{B}$ 的*合同变换矩阵*。显然 $\bm{B}$ 也合同于 $\bm{A}$，因为有

    $$
    \bm{A} = \left(\bm{P}^{-1}\right)^\intercal \bm{B} \bm{P}^{-1}
    $$

    <details>
    <summary>至此已学习的矩阵关系</summary>

    1. **等价矩阵**：$\bm{B} = \bm{P} \bm{A} \bm{Q}$（$\bm{A},\, \bm{B}$ 为 $m \times n$ 矩阵，$\bm{P},\, \bm{Q}$ 分别为 $m$ 阶和 $n$ 阶可逆矩阵）
    2. **相似矩阵**：$\bm{B} = \bm{P}^{-1} \bm{A} \bm{P}$（$\bm{A},\, \bm{B}$ 为 $n$ 阶方阵，$\bm{P}$ 为 $n$ 阶可逆矩阵）
    3. **合同矩阵**：$\bm{B} = \bm{P}^\intercal \bm{A} \bm{P}$（$\bm{A},\, \bm{B}$ 为 $n$ 阶方阵，$\bm{P}$ 为 $n$ 阶可逆矩阵）

    </details>

!!! info ""
    只包含平方项的二次型称为**标准形**，即

    $$
    f(x_1,\, x_2,\, \cdots,\, x_n) = \sum_{i=1}^n d_{ii} x_i^2
    $$

    设实二次型 $f(x_1,\, x_2,\, \cdots,\, x_n) = \bm{x}^\intercal \bm{A} \bm{x}$，则存在非退化线性变换 $\bm{x} = \bm{P} \bm{y}$，使得 $f$ 化为标准形。

    等价于证明<u>存在可逆矩阵将实对称矩阵合同变换为实对角矩阵</u>。

    因为 $\bm{A}$ 为实对称矩阵，所以存在正交矩阵 $\bm{P}$，使得

    $$
    \begin{aligned}
        \bm{P}^\intercal \bm{A} \bm{P} &= \bm{P}^{-1} \bm{A} \bm{P} \\
        &= \begin{bmatrix}
            \lambda_1 & & & \\
            & \lambda_2 & & \\
            & & \ddots & \\
            & & & \lambda_n
        \end{bmatrix}
    \end{aligned}
    $$

    从而令正交变换 $\bm{x} = \bm{P} \bm{y}$，则有

    $$
    \begin{aligned}
        f(\bm{x}) &= \bm{x}^\intercal \bm{A} \bm{x} \\
        &= (\bm{P} \bm{y})^\intercal \bm{A} (\bm{P} \bm{y}) \\
        &= \bm{y}^\intercal (\bm{P}^\intercal \bm{A} \bm{P}) \bm{y} \\
        &= \bm{y}^\intercal \begin{bmatrix}
            \lambda_1 & & & \\
            & \lambda_2 & & \\
            & & \ddots & \\
            & & & \lambda_n
        \end{bmatrix} \bm{y} \\
        &= \lambda_1 y_1^2 + \lambda_2 y_2^2 + \cdots + \lambda_n y_n^2
    \end{aligned}
    $$

    显然标准型是不唯一的。

### 化标准形方法

!!! note 正交变换法（特征值法）
    1. 求出实二次型的矩阵 $\bm{A}$ 的特征值 $\lambda_1,\, \lambda_2,\, \cdots,\, \lambda_n$ 及相应的特征向量 $\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_n$。（若同一特征值特征向量不正交，则使用施密特正交化进行正交。显然经过线性变换后仍然是特征向量。而不同特征值的特征向量，已经在笔记 5 证明是正交的了）[^1]
    2. 取正交矩阵 $\bm{P} = \begin{bmatrix} \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n \end{bmatrix}$，则

        $$
        \bm{P}^\intercal \bm{A} \bm{P} = \begin{bmatrix}
            \lambda_1 & & & \\
            & \lambda_2 & & \\
            & & \ddots & \\
            & & & \lambda_n
        \end{bmatrix}
        $$

    3. 取正交变换 $\bm{x} = \bm{P} \bm{y}$

    [^1]: 实际做题中，对三维方阵可能会出现两个特征值，在算完重特征值的特征向量后，可运用向量叉乘，直接得出第三个正交向量，而不用再去回去慢慢算矩阵。这运用了「实对称矩阵不同特征值对应特征向量正交」的性质。

!!! note 配方法
    1. 若二次型含有平方项，如 $a_{11} x_1^2$，则把所有含 $x_1$ 的项集中进行配方，即令

    $$
    \left\lbrace\begin{aligned}
        y_1 &= x_1 + \dfrac{a_{12}}{a_{11}} x_2 + \cdots + \dfrac{a_{1n}}{a_{11}} x_n \\
        y_2 &= x_2 \\
        &\kern{0.25em}\vdots \\
        y_n &= x_n
    \end{aligned}\right.
    $$

    从而

    $$
    f = a_{11} y_1^2 + f_1(y_2,\, y_3,\, \cdots,\, y_n)
    $$

    2. 若二次型不含平方项，取非零交叉项，如 $2a_{12} x_1 x_2$，则令

    $$
    \left\lbrace\begin{aligned}
        x_1 &= y_1 + y_2\\
        x_2 &= y_1 - y_2 \\
        x_3 &= y_3 \\
        &\kern{0.25em}\vdots \\
        x_n &= y_n
    \end{aligned}\right.
    $$

    从而

    $$
    f = 2a_{12} y_1^2 - 2a_{12} y_2^2 + F(y_1, y_2, y_3,\, y_4,\, \cdots,\, y_n)
    $$

    3. 重复上述过程，直至化为标准形。

!!! note 合同变换法
    没时间了，下节课再写。

    1. 利用二次型矩阵 $\bm{A}$，构造 $2n \times n$ 矩阵 $\bm{B} = \begin{bmatrix} \bm{A} \\ \bm{E} \end{bmatrix}$。
    2. 对 $\bm{B}$ 做一次*初等列变换*，然后再做一次同类型的*初等行变换*，即 $\begin{bmatrix} \bm{P}_1^\intercal &   \\ & \bm{E} \end{bmatrix} \begin{bmatrix} \bm{A} \\ \bm{E} \end{bmatrix} \bm{P}_1 = \begin{bmatrix} \bm{P}_1^\intercal \bm{A} \bm{P}_1 \\ \bm{P}_1 \end{bmatrix}$。操作若干次化为 $\begin{bmatrix} \bm{\Lambda} \\ \bm{P} \end{bmatrix}$ 的形式，其中 $\bm{\Lambda}$ 为对角矩阵。（原理即为 $\bm{P}^\intercal \bm{A} \bm{P} = \bm{\Lambda}$，且 $\bm{P} = \bm{P}_1 \bm{P}_2 \cdots \bm{P}_{k}$）
    3. 令线性变换 $\bm{x} = \bm{P} \bm{y}$，则原二次型变为标准型 $\bm{y}^\intercal \bm{\Lambda} \bm{y}$。

### 二次型的规范形

!!! info ""
    实二次型 $f(x_1, x_2, \cdots, x_n)$ 经过非退化的实线性变换得到如下形式的二次型

    $$
    z_1^2 + \cdots + z_p^2 - z_{p+1}^2 - \cdots - z_r^2\qquad(r \le n)
    $$

    称为实二次型 $f(x_1, x_2, \cdots, x_n)$ 的**实规范形**，$r$ 称为实二次型 $f(x_1, x_2, \cdots, x_n)$ 的**秩**，$p$ 称为实二次型 $f(x_1, x_2, \cdots, x_n)$ 的**正惯性指数**，$r - p$ 称为实二次型 $f(x_1, x_2, \cdots, x_n)$ 的**负惯性指数**。

    复二次型 $f(x_1, x_2, \cdots, x_n)$ 经过非退化的复线性变换得到如下形式的二次型

    $$
    z_1^2 + \cdots + z_r^2\qquad(r \le n)
    $$

    称为复二次型 $f(x_1, x_2, \cdots, x_n)$ 的**复规范形**，$r$ 称为复二次型 $f(x_1, x_2, \cdots, x_n)$ 的**秩**。

!!! note 惯性定理
    任意实二次型 $f(x_1, x_2, \cdots, x_n) = \bm{x}^\intercal \bm{A} \bm{x}$，都可用适当的非退化<u>实</u>线性变换，化成实规范形

    $$
    z_1^2 + \cdots + z_p^2 - z_{p+1}^2 - \cdots - z_r^2\qquad(r \le n)
    $$

    其中 $r = \rank(\bm{A})$，且实规范形唯一。

    ---

    证明：

    存在性：存在可逆矩阵 $\bm{P}$ 使得 $\bm{P}^\intercal \bm{A} \bm{P} = \begin{bmatrix} d_1 &   &   &   \\   & d_2 &  & \\   &   & \ddots &   \\   &   &  & d_n \end{bmatrix}$，其中 $d_i \in \R$。

    设 $d_1 > 0,\, \cdots,\, d_p > 0;\; d_{p + 1} < 0,\, \cdots,\, d_r < 0;\; d_{r + 1} = 0,\, \cdots,\, d_n = 0$。

    则

    $$
    \begin{aligned}
        f \xlongequal{\bm{x} = \bm{P}\bm{y}} &\left( d_1 y_1^2 + \cdots + d_p y_p^2 \right) +\\
        &\left( d_{p+1} y_{p+1}^2 + \cdots + d_r y_r^2 \right) +\\
        &\left( d_{r+1} y_{r+1}^2 + \cdots + d_n y_n^2 \right)
    \end{aligned}
    $$

    取线性变换 $\bm{y} = \bm{Q} \bm{z}$ 使得

    $$
    \left\lbrace\begin{aligned}
        z_1 &= \sqrt{d_1} y_1\\
        &\kern{0.25em}\vdots\\
        z_p &= \sqrt{d_p} y_p\\
        z_{p+1} &= \sqrt{-d_{p+1}} y_{p+1}\\
        &\kern{0.25em}\vdots\\
        z_r &= \sqrt{-d_r} y_r\\
        z_{r+1} &= y_{r+1}\\
        &\kern{0.25em}\vdots\\
        z_n &= y_n
    \end{aligned}\right.
    $$

    从而有

    $$
    f \xlongequal{\bm{x} = \bm{P} \bm{y},\, \bm{y} = \bm{Q} \bm{z}} z_1^2 + \cdots + z_p^2 - z_{p+1}^2 - \cdots - z_r^2
    $$

    唯一性：即证 $p$ 唯一确定。

    假设存在两个非退化线性变换，使得 $\bm{x} = \bm{P}_1 \bm{z},\, \bm{x} = \bm{P}_2 \bm{w}$，即

    $$
    \begin{aligned}
        f &\xlongequal{\bm{x} = \bm{P}_1 \bm{z}} z_1^2 + \cdots + z_p^2 - z_{p+1}^2 - \cdots - z_r^2\\
        f &\xlongequal{\bm{x} = \bm{P}_2 \bm{w}} w_1^2 + \cdots + w_q^2 - w_{q+1}^2 - \cdots - w_r^2
    \end{aligned}
    $$

    即要证明 $p = q$。反证法，假设 $p > q$。

    因为 $\bm{x} = \bm{P}_1 \bm{z} = \bm{P}_2 \bm{w}$，则 $ \bm{w} = \bm{P}_2^{-1} \bm{P}_1 \bm{z}$，从而对 $\bm{w} = (\bm{P}_2^{-1}\bm{P}_1)\bm{z}$，有

    $$
    \begin{aligned}
        & z_1^2 + \cdots + z_p^2 - z_{p+1}^2 - \cdots - z_r^2 = \\
        & w_1^2 + \cdots + w_q^2 - w_{q+1}^2 - \cdots - w_r^2 \tag{1}
    \end{aligned}
    $$

    设 $\bm{C} = \bm{P}_2^{-1} \bm{P}_1$，即 $\bm{w} = \bm{C} \bm{z}$，则

    $$
    \begin{bmatrix}
        w_1 \\
        w_2 \\
        \vdots \\
        w_n
    \end{bmatrix} =
    \begin{bmatrix}
        c_{11} & c_{12} & \cdots & c_{1n} \\
        c_{21} & c_{22} & \cdots & c_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        c_{n1} & c_{n2} & \cdots & c_{nn}
    \end{bmatrix}
    \begin{bmatrix}
        z_1 \\
        z_2 \\
        \vdots \\
        z_n
    \end{bmatrix}
    $$

    令

    $$
    \bm{C} =
    \begin{bmatrix}
        \bm{C}_1^{q \times p} & \bm{C}_2^{q \times (n - p)} \\
        \bm{C}_3^{(n - q) \times p} & \bm{C}_4^{(n - q) \times (n - p)}
    \end{bmatrix},\quad \bm{z} =
    \begin{bmatrix}
        \bm{z}_1^{p} \\
        \bm{z}_2^{n - p}
    \end{bmatrix}
    $$

    构造齐次方程组

    $$
    \left\lbrace\begin{aligned}
        c_{11} z_1 + c_{12} z_2 + \cdots + c_{1p} z_p &= 0\\
        c_{21} z_1 + c_{22} z_2 + \cdots + c_{2p} z_p &= 0\\
        &\kern{0.25em}\vdots\\
        c_{q1} z_1 + c_{n2} z_2 + \cdots + c_{qp} z_p &= 0
    \end{aligned}\right.
    $$

    即 $\bm{C}_1 \bm{z}_1 = \bm{\theta}$。

    由于 $q < p$，方程个数小于未知元个数，则存在非零解 $(z_1, z_2, \cdots, z_p) = (t_1, t_2, \cdots, t_p)$。

    取 $\bm{z} = (t_1, t_2, \cdots, t_p, 0, \cdots, 0)$，则

    $$
    \begin{aligned}
        \bm{w} &= \bm{C}\bm{z}\\
        &= \begin{bmatrix}
            \bm{C}_1 & \bm{C}_2 \\
            \bm{C}_3 & \bm{C}_4
        \end{bmatrix}
        \begin{bmatrix}
            \bm{z}_1^{p}\\
            \bm{\theta}^{n - p}
        \end{bmatrix}\\
        &= \begin{bmatrix}
            \bm{C}_1 \bm{z}_1\\
            \bm{C}_3 \bm{z}_1
        \end{bmatrix}\\
        &= \begin{bmatrix}
            \bm{\theta}^{q}\\
            \bm{C}_3 \bm{z}_1
        \end{bmatrix}\\
        &= (\overbrace{0, \cdots, 0}^{q}, s_{q+1}, \cdots, s_n)
    \end{aligned}
    $$

    代入 $(1)$ 式，得

    $$
    t_1^2 + \cdots + t_p^2 = - s_{q+1}^2 - \cdots - s_n^2
    $$

    左边 $t_1^2 + \cdots + t_p^2 > 0$，右边 $- s_{q+1}^2 - \cdots - s_n^2 \le 0$，矛盾。

    故 $p \le q$，同理可证 $q \le p$，从而 $p = q$。

!!! note ""
    若实对称矩阵 $\bm{A},\, \bm{B}$ 合同，则二次型 $\bm{x}^\intercal\bm{A}\bm{x}$ 与 $\bm{x}^\intercal\bm{B}\bm{x}$ 有相同的秩、正惯性指数和负惯性指数。

    ---

    证明：

    存在可逆矩阵 $\bm{P}$ 使得

    $$
    \bm{P}^\intercal \bm{A} \bm{P} =
    \begin{bmatrix}
    1 & & & & & & & & \\
    & \ddots & & & & & & & \\
    & & 1 & & & & & & \\
    & & & -1 & & & & & \\
    & & & & \ddots & & & & \\
    & & & & & -1 & & & \\
    & & & & & & 0 & & \\
    & & & & & & & \ddots & \\
    & & & & & & & & 0
    \end{bmatrix}
    $$

    而又存在可逆矩阵 $\bm{Q}$ 使得 $\bm{B} = \bm{Q}^\intercal \bm{A} \bm{Q}$，即 $\bm{A} = (\bm{Q}^{-1})^\intercal \bm{B} \bm{Q}^{-1}$，从而

    $$
    \begin{aligned}
        \bm{P}^\intercal \bm{A} \bm{P} &= \bm{P}^\intercal (\bm{Q}^{-1})^\intercal \bm{B} \bm{Q}^{-1} \bm{P}\\
        &= (\bm{Q}^{-1} \bm{P})^\intercal \bm{B} (\bm{Q}^{-1} \bm{P})\\
        &=
        \begin{bmatrix}
        1 & & & & & & & & \\
        & \ddots & & & & & & & \\
        & & 1 & & & & & & \\
        & & & -1 & & & & & \\
        & & & & \ddots & & & & \\
        & & & & & -1 & & & \\
        & & & & & & 0 & & \\
        & & & & & & & \ddots & \\
        & & & & & & & & 0
        \end{bmatrix}
    \end{aligned}
    $$

    令 $\bm{R} = \bm{Q}^{-1} \bm{P}$，则 $\bm{R}$ 可逆，且

    $$
    \bm{R}^\intercal \bm{B} \bm{R} =
    \begin{bmatrix}
        1 & & & & & & & & \\
        & \ddots & & & & & & & \\
        & & 1 & & & & & & \\
        & & & -1 & & & & & \\
        & & & & \ddots & & & & \\
        & & & & & -1 & & & \\
        & & & & & & 0 & & \\
        & & & & & & & \ddots & \\
        & & & & & & & & 0
    \end{bmatrix}
    $$

    从而 $\bm{x}^\intercal \bm{A} \bm{x}$ 与 $\bm{x}^\intercal \bm{B} \bm{x}$ 有相同的秩、正惯性指数和负惯性指数。

### 正定二次型

!!! info ""
    设 $f(x_1, x_2, \cdots, x_n) = \bm{x}^\intercal \bm{A} \bm{x}$ 为实二次型，若对任意实向量 $\bm{x} \ne \bm{\theta}$，都有

    $$
    f(\bm{x}) = \bm{x}^\intercal \bm{A} \bm{x} > 0
    $$

    则称 $f(\bm{x})$ 为**正定二次型**，$\bm{A}$ 为**正定矩阵**。

    同理可定义**负定二次型**和**半正定二次型**。

    正定矩阵一定是<u>实对称矩阵</u>。

!!! example ""
    如 $f(x_1, x_2, x_3) = x_1^2 + x_2^2$ 就不是正定二次型，因为 $f(0, 0, a) = 0$ 对任意 $a \in \R\backslash\left\lbrace 0 \right\rbrace$ 成立，而 $(0, 0, a) \ne \bm{\theta}$。

    该二次型称为**半正定二次型**，二次型矩阵称为**半正定矩阵**，因为对任意实向量 $\bm{x} \ne  \bm{\theta}$，都有

    $$
    f(\bm{x}) = \bm{x}^\intercal \bm{A} \bm{x} \ge 0
    $$

    同理有**半负定二次型**和**半负定矩阵**。

!!! note ""
    设 $\bm{A}$ 为 $n$ 阶正定矩阵，$\bm{P}$ 为 $n$ 阶可逆矩阵，则 $\bm{P}^\intercal \bm{A} \bm{P}$ 也是正定矩阵。

    即合同变换不改变正定性。

    ---

    证明：

    因为 $\bm{A}$ 为正定矩阵，故对任意 $\bm{x} \ne \bm{\theta}$，都有

    $$
    \bm{x}^\intercal \bm{A} \bm{x} > 0
    $$

    即证对任意 $\bm{y} \ne \bm{\theta}$，都有

    $$
    \bm{y}^\intercal (\bm{P}^\intercal \bm{A} \bm{P}) \bm{y} > 0
    $$

    令 $\bm{x} = \bm{P} \bm{y}$，则 $\bm{x} \ne \bm{\theta}$，从而

    $$
    \begin{aligned}
        \bm{y}^\intercal (\bm{P}^\intercal \bm{A} \bm{P}) \bm{y} &= (\bm{P} \bm{y})^\intercal \bm{A} (\bm{P} \bm{y})\\
        &= \bm{x}^\intercal \bm{A} \bm{x}\\
        &> 0
    \end{aligned}
    $$

!!! info 顺序主子式
    设矩阵 $\bm{A} = \left[ a_{ij} \right]_{n \times n}$，称如下行列式

    $$
    \begin{vmatrix}
        a_{11} & a_{12} & \cdots & a_{1k} \\
        a_{21} & a_{22} &   & a_{2k} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{k1} & a_{k 2} & \cdots & a_{kk}
    \end{vmatrix}
    $$

    为 $\bm{A}$ 的 **$k$ 阶顺序主子式**。显然 $\bm{A} \in M_{n}(\R)$ 的顺序主子式有 $n$ 个。

!!! note ""
    设 $\bm{A}$ 为 $n$ 阶实对称矩阵，则以下结论等价：
    1. $\bm{A}$ 为正定矩阵
    2. $\bm{A}$ 的特征值全为正
    3. $\bm{A}$ 的正惯性指数为 $n$
    4. $\bm{A}$ 的各阶顺序主子式全为正
    5. $\bm{A}$ 合同于单位矩阵 $\bm{E}$（存在可逆矩阵 $\bm{P}$，使得 $\bm{A} = \bm{P}^\intercal \bm{P}$）

    ---

    证明：（只证明部分）

    1. $\implies $ 4.：

    由 $\bm{A}$ 正定，取 $\bm{x} = (x_1, \cdots, x_{k}, 0, \cdots, 0)$，其中 $x_i$ 不全为零，则有 $\bm{x} \ne  \bm{\theta}$，则 $\bm{x}^\intercal \bm{A} \bm{x} > 0$，即

    $$
    \begin{aligned}
        \begin{bmatrix}
            x_1 & \cdots & x_k
        \end{bmatrix}
        \begin{bmatrix}
            a_{11} & \cdots & a_{1k} \\
            \vdots & \ddots & \vdots \\
            a_{k1} & \cdots & a_{kk}
        \end{bmatrix}
        \begin{bmatrix}
            x_1 \\ \vdots \\ x_k
        \end{bmatrix} &> 0\\
        \begin{bmatrix}
            x_1 & \cdots & x_k
        \end{bmatrix}
        \bm{A}_k
        \begin{bmatrix}
            x_1 \\ \vdots \\ x_k
        \end{bmatrix} &> 0
    \end{aligned}
    $$

    则 $\bm{A}_{k} \in M_{k}(\R)$ 为对称、正定矩阵，从而 $|\bm{A}_{k}| > 0$，即 $\bm{A}_{k}$ 的顺序主子式全为正。

    4. $\implies $ 1.：

    设实对称矩阵 $\bm{A} \in M_n(\R)$。

    数学归纳法，$n = 1$ 时显然成立。

    假设 $n = m - 1$ 时成立，当 $n = m$ 时，有

    $$
    \bm{A} = \begin{bmatrix}
        \bm{B} & \bm{\beta}\\
        \bm{\beta}^\intercal & a_{mm}
    \end{bmatrix}\\
    $$

    其中 $\bm{B} \in M_{m-1}(\R)$ 为对称正定矩阵，$\bm{\beta} = \begin{bmatrix} a_{1m} \\ \vdots \\ a_{m-1, m} \end{bmatrix} \in \R^{m-1}$，$a_{mm} \in \R$。

    构造 $\bm{P} = \begin{bmatrix} \bm{E} & -\bm{B}^{-1} \bm{\beta} \\ \bm{\theta}^\intercal & 1 \end{bmatrix}$，则有

    $$
    \begin{aligned}
        \bm{P}^\intercal \bm{A} \bm{P} &= \begin{bmatrix} \bm{E} & (\bm{\theta}^\intercal)^\intercal \\ \left(-\bm{B}^{-1} \bm{\beta}\right)^\intercal & 1 \end{bmatrix} \begin{bmatrix}
            \bm{B} & \bm{\beta}\\
            \bm{\beta}^\intercal & a_{mm}
        \end{bmatrix} \begin{bmatrix} \bm{E} & -\bm{B}^{-1} \bm{\beta} \\ \bm{\theta}^\intercal & 1 \end{bmatrix}\\
        &= \begin{bmatrix} \bm{E} & \bm{\theta} \\ - \bm{\beta}^\intercal \bm{B}^{-1} & 1 \end{bmatrix} \begin{bmatrix}
            \bm{B} & \bm{\beta}\\
            \bm{\beta}^\intercal & a_{mm}
        \end{bmatrix} \begin{bmatrix} \bm{E} & -\bm{B}^{-1} \bm{\beta}^\intercal \\ \bm{\theta}^\intercal & 1 \end{bmatrix}\\
        &=
        \begin{bmatrix}
            \bm{B} & \bm{\beta}\\
            \bm{\theta}^\intercal & a_{mm} - \bm{\beta}^\intercal \bm{B}^{-1} \bm{\beta}
        \end{bmatrix}
        \begin{bmatrix} \bm{E} & -\bm{B}^{-1} \bm{\beta} \\ \bm{\theta}^\intercal & 1 \end{bmatrix}\\
        &=
        \begin{bmatrix}
            \bm{B} & \bm{\theta}\\
            \bm{\theta}^\intercal & a_{mm} - \bm{\beta}^\intercal \bm{B}^{-1} \bm{\beta}
        \end{bmatrix}\\
    \end{aligned}
    $$

    因为 $\left\lvert \bm{A} \right\rvert > 0$，则

    $$
    \begin{aligned}
        \left\lvert \bm{P}^\intercal \bm{A} \bm{P} \right\rvert &= \left\lvert \bm{P}^\intercal \right\rvert \left\lvert \bm{A} \right\rvert \left\lvert \bm{P} \right\rvert\\
        &= \left\lvert \bm{P} \right\rvert^2 \left\lvert \bm{A} \right\rvert\\
        &> 0
    \end{aligned}
    $$

    即 $\left\lvert \bm{B} \right\rvert\left(a_{mm} - \bm{\beta}^\intercal \bm{B}^{-1} \bm{\beta}\right) > 0$，而 $\left\lvert \bm{B} \right\rvert > 0$，则有 $a_{mm} - \bm{\beta}^\intercal \bm{B}^{-1} \bm{\beta} > 0$。

    由 $\bm{B}$ 为正定矩阵，存在可逆矩阵 $\bm{Q} \in M_{m - 1}(\R)$ 使得 $\bm{Q}^\intercal \bm{B} \bm{Q} = \bm{E}_{m - 1}$，令

    $$
    \bm{C} = \begin{bmatrix}
        \bm{Q} & \bm{\theta}\\
        \bm{\theta}^\intercal & 1
    \end{bmatrix}
    $$

    则有

    $$
    \begin{aligned}
        \bm{C}^\intercal \left( \bm{P}^\intercal \bm{A} \bm{P} \right) \bm{C} &=
        \begin{bmatrix}
            \bm{Q}^\intercal & \bm{\theta}\\
            \bm{\theta}^\intercal & 1
        \end{bmatrix}
        \begin{bmatrix}
            \bm{B} & \bm{\theta}\\
            \bm{\theta}^\intercal & a_{mm} - \bm{\beta}^\intercal \bm{B}^{-1} \bm{\beta}
        \end{bmatrix}
        \begin{bmatrix}
            \bm{Q} & \bm{\theta}\\
            \bm{\theta}^\intercal & 1
        \end{bmatrix}\\
        &=
        \begin{bmatrix}
            \bm{Q}^\intercal \bm{B} \bm{Q} & \bm{\theta} \\
            \bm{\theta}^\intercal & a_{mm} - \bm{\beta}^\intercal \bm{B}^{-1} \bm{\beta}
        \end{bmatrix}\\
        &=
        \begin{bmatrix}
            \bm{E}_{m - 1} & \bm{\theta} \\
            \bm{\theta}^\intercal & a_{mm} - \bm{\beta}^\intercal \bm{B}^{-1} \bm{\beta}
        \end{bmatrix}\\
        &= \left( \bm{P} \bm{C} \right) ^\intercal \bm{A} \left( \bm{P} \bm{C} \right)\\
    \end{aligned}
    $$

    令 $\bm{D} = \bm{P} \bm{C}$，则有 $\bm{D}^\intercal \bm{A} \bm{D} = \begin{bmatrix} \bm{E}_{m - 1} & \bm{\theta} \\ \bm{\theta}^\intercal & a_{mm} - \bm{\beta}^\intercal \bm{B}^{-1} \bm{\beta} \end{bmatrix}$，由 $a_{mm} - \bm{\beta}^\intercal \bm{B}^{-1} \bm{\beta} > 0$，故 $\bm{A}$ 为正定矩阵。

    1. $\implies $ 5.：

    $f \xlongequal{\bm{x} = \bm{P} \bm{y}} \lambda_1 y_1^2 + \cdots + \lambda_n y_n^2$，其中 $\lambda_i > 0$ 为 $\bm{A}$ 的特征值。

    则有正交矩阵 $\bm{Q}$ 使

    $$ \begin{aligned}
        \bm{A} &= \bm{Q} \begin{bmatrix} \lambda_1 &   &   \\   & \ddots &   \\   &   & \lambda_n \end{bmatrix} \bm{Q}^\intercal\\
        &= \bm{Q} \begin{bmatrix} \sqrt{\lambda_1} &   &   \\   & \ddots &   \\   &   & \sqrt{\lambda_n} \end{bmatrix} \begin{bmatrix} \sqrt{\lambda_1} &   &   \\   & \ddots &   \\   &   & \sqrt{\lambda_n} \end{bmatrix} \bm{Q}^\intercal \\
        &= \left(  \bm{Q} \begin{bmatrix} \sqrt{\lambda_1} &   &   \\   & \ddots &   \\   &   & \sqrt{\lambda_n} \end{bmatrix} \right) \left( \bm{Q} \begin{bmatrix} \sqrt{\lambda_1} &   &   \\   & \ddots &   \\   &   & \sqrt{\lambda_n} \end{bmatrix} \right)^\intercal \\
        &= \bm{P}^\intercal \bm{P}
    \end{aligned} $$

    其中 $\bm{P} = \left( \bm{Q} \begin{bmatrix} \sqrt{\lambda_1} &   &   \\   & \ddots &   \\   &   & \sqrt{\lambda_n} \end{bmatrix} \right)^\intercal$。


!!! note 推论
    正定矩阵行列式大于零。

!!! note ""
    正定矩阵 $\bm{A}$ 主对角线元素 $a_{ii} > 0$。

    ---

    证明：

    存在可逆矩阵 $\bm{P}$，使

    $$
    \begin{aligned}
        \bm{A} &= \bm{P}^\intercal \bm{P}\\
        &= \begin{bmatrix} \bm{\alpha}_1^\intercal \\ \vdots \\ \bm{\alpha}_n^\intercal \end{bmatrix} \begin{bmatrix} \bm{\alpha}_1 & \cdots & \bm{\alpha}_n \end{bmatrix}\\
        &= \begin{bmatrix} \bm{\alpha}_1^\intercal \bm{\alpha}_1 & \cdots & \bm{\alpha}_1^\intercal \bm{\alpha}_n \\ \vdots & \ddots & \vdots \\ \bm{\alpha}_n^\intercal \bm{\alpha}_1 & \cdots & \bm{\alpha}_n^\intercal \bm{\alpha}_n \end{bmatrix}
    \end{aligned}
    $$

    从而有 $a_{ii} = \bm{\alpha}_i^\intercal \bm{\alpha}_i = \| \bm{\alpha}_i \|^2 > 0$。（可逆矩阵，不可能为零向量）

!!! info 主子式
    设矩阵 $\bm{A} = \left[ a_{ij} \right]_{n \times n}$，取 $i_1 < i_2 < \cdots < i_{k}$，则如下行列式

    $$
    \begin{vmatrix}
        a_{i_1 i_1} & a_{i_1 i_2} & \cdots & a_{i_1 i_k} \\
        a_{i_2 i_1} & a_{i_2 i_2} & \cdots & a_{i_2 i_k} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{i_k i_1} & a_{i_k i_2} & \cdots & a_{i_k i_k}
    \end{vmatrix}
    $$

    称为 $\bm{A}$ 的一个 **$k$ 阶主子式**。

!!! note ""
    正定矩阵 $\bm{A}$ 的 $k$ 阶主子式全为正。

    ---

    证明：

    由 $\bm{A}$ 正定，取 $\bm{x} = (x_1, x_2, \cdots, x_n)^\intercal$，其中 $x_{i_1},\, x_{i_2},\, \cdots,\, x_{i_k}$ 不全为零，其余 $n - k$ 个分量为零，则有 $\bm{x} \ne \bm{\theta}$，则 $\bm{x}^\intercal \bm{A} \bm{x} > 0$，即

    $$
    \begin{aligned}
        \begin{bmatrix}
            x_{i_1} & \cdots & x_{i_k}
        \end{bmatrix}
        \begin{bmatrix}
            a_{i_1 i_1} & \cdots & a_{i_1 i_k} \\
            \vdots & \ddots & \vdots \\
            a_{i_k i_1} & \cdots & a_{i_k i_k}
        \end{bmatrix}
        \begin{bmatrix}
            x_{i_1} \\ \vdots \\ x_{i_k}
        \end{bmatrix} &> 0\\
        \begin{bmatrix}
            x_{i_1} & \cdots & x_{i_k}
        \end{bmatrix}
        \bm{B}
        \begin{bmatrix}
            x_{i_1} \\ \vdots \\ x_{i_k}
        \end{bmatrix} &> 0
    \end{aligned}
    $$
    
    $\bm{B} \in M_k(\R)$ 为对称、正定矩阵，从而 $|\bm{B}| > 0$，即 $\bm{B}$ 的顺序主子式全为正。

    由 $i_1,\, i_2,\, \cdots,\, i_k$ 的任意性，可知 $\bm{A}$ 的 $k$ 阶主子式全为正。

!!! note ""
    上面写正定矩阵合同于单位矩阵，即存在可逆矩阵 $\bm{P}$，使得 $\bm{A} = \bm{P}^\intercal \bm{P}$。

    实际上有更强的结论，存在正定矩阵 $\bm{B}$，使得 $\bm{A} = \bm{B}^\intercal \bm{B}$，从而 $\bm{A} = \bm{B}^2$ 

    ---

    证明：

    $\impliedby$：

    $\bm{A} = \bm{B}^2 \implies \bm{A} = \bm{B}^\intercal \bm{B}$，其中 $\bm{B}$ 为正定矩阵。从而 $\bm{A}$ 正定。

    > $\bm{x}^\intercal \bm{A} \bm{x} = \bm{x}^\intercal \bm{B}^\intercal \bm{B} \bm{x} = \left( \bm{B} \bm{x} \right)^\intercal \bm{B} \bm{x} = \| \bm{B} \bm{x} \|^2 > 0$，从而 $\bm{A}$ 正定。

    $\implies$：

    设 $\bm{A}$ 为正定矩阵，存在正交矩阵 $\bm{P}$（$\bm{P} \bm{P}^\intercal = \bm{E}$）使得

    $$
    \begin{aligned}
        \bm{A} &= \bm{P}^\intercal
        \begin{bmatrix}
            \lambda_1 &   &   \\   & \ddots &   \\   &   & \lambda_n
        \end{bmatrix} \bm{P}\\
        &= \bm{P}^\intercal \begin{bmatrix}
            \sqrt{\lambda_1} &   &   \\   & \ddots &   \\   &   & \sqrt{\lambda_n}
        \end{bmatrix} \begin{bmatrix}
            \sqrt{\lambda_1} &   &   \\   & \ddots &   \\   &   & \sqrt{\lambda_n}
        \end{bmatrix} \bm{P}\\
        &= \bm{P}^\intercal \bm{\Lambda} \bm{\Lambda} \bm{P}\\
        &= \bm{P}^\intercal \bm{\Lambda} \bm{P} \bm{P}^\intercal \bm{\Lambda} \bm{P}\\
        &= \left( \bm{P}^\intercal \bm{\Lambda} \bm{P} \right)^\intercal \left( \bm{P}^\intercal \bm{\Lambda} \bm{P} \right)\\
    \end{aligned}
    $$
    
    取 $\bm{B} = \bm{P}^\intercal \bm{\Lambda} \bm{P}$，则有 $\bm{A} = \bm{B}^\intercal \bm{B} = \bm{B}^2$。

!!! note ""
    设 $\bm{A}$ 为实对称矩阵，则当实数 $t$ 充分大时，$\bm{A} + t \bm{E}$ 为正定矩阵。

    ---

    证明：

    由于 $\bm{A}$ 为实对称矩阵，存在正交矩阵 $\bm{P}$ 使得

    $$
    \bm{A} = \bm{P}^\intercal
    \begin{bmatrix}
        \lambda_1 &   &   \\   & \ddots &   \\   &   & \lambda_n
    \end{bmatrix} \bm{P}
    $$
    
    则

    $$
    \begin{aligned}
        \bm{A} + t \bm{E} &= \bm{P}^\intercal \begin{bmatrix}
            \lambda_1  &   &   \\   & \ddots &   \\   &   & \lambda_n 
        \end{bmatrix} \bm{P} + t \bm{P}^\intercal \bm{P}\\
        &= \bm{P}^\intercal\bm{\Lambda}\bm{P} + \bm{P}^\intercal (t \bm{E}) \bm{P}\\
        &= \bm{P}^\intercal \left( \bm{\Lambda} + t \bm{E} \right) \bm{P}\\
        &= \bm{P}^\intercal
        \begin{bmatrix}
            \lambda_1 + t &   &   \\   & \ddots &   \\   &   & \lambda_n + t
        \end{bmatrix} \bm{P}
    \end{aligned}
    $$
    
    当 $t > \max\limits_{i = 1,\, \cdots,\, n} \left\{ \left\lvert \lambda_i \right\rvert \right\}$ 时，$\bm{A} + t \bm{E}$ 的特征值全为正，从而 $\bm{A} + t \bm{E}$ 为正定矩阵。

!!! info ""
    若 $f$ 既不是半正定二次型，也不是半负定二次型，则称 $f$ 为**不定二次型**，称 $\bm{A}$ 为**不定矩阵**。

!!! note ""
    $\bm{A}$ 为负定矩阵 $\iff $ $-\bm{A}$ 为正定矩阵。

    注意负定矩阵行列式不一定为负，实际上有

    $$
    (-1)^r \begin{vmatrix}
        a_{11} & a_{12} & \cdots & a_{1r} \\
        a_{21} & a_{22} &   & a_{2r} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{r1} & a_{r 2} & \cdots & a_{rr}
    \end{vmatrix} > 0
    $$

!!! note ""
    对实对称矩阵 $\bm{A}$，以下结论等价：
    1. $\bm{A}$ 为半正定矩阵
    2. $f$ 正惯性指数 $= \rank(\bm{A})$ 
    3. $\bm{A}$ 特征值均不小于零
    4. 存在实矩阵 $\bm{B}$，使得 $\bm{A} = \bm{B}^\intercal \bm{B}$
    5. $\bm{A}$ 所有主子式不小于零（不是*顺序主子式*！）[^1]

    [^1]: 顺序主子式全不小于零，不一定为半正定矩阵，如 $\begin{bmatrix} 0 & 0 \\ 0 & -1 \end{bmatrix}$
