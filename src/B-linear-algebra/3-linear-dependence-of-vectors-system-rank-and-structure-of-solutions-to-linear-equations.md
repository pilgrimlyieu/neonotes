---
layout: post
title: 向量组线性相关性、秩与线性方程组解的结构
date: 2023-11-05 17:59:59
updated: 2023-12-21 13:55:32
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

### 向量组的线性相关性和线性无关性

#### 线性表示和线性组合

!!! info 线性表示
    给定 $n$ 维向量组 $\bm{A} \colon \bm{\alpha}_1,\, \bm{\alpha}_2 ,\, \cdots ,\, \bm{\alpha}_m$ 和 $n$ 维向量 $\bm{\beta}$，如果存在 $m$ 个数 $k_1,\, k_2,\, \cdots ,\, k_m$，使得

    $$
    \bm{\beta} = k_1 \bm{\alpha}_1 + k_2 \bm{\alpha}_2 + \cdots + k_m \bm{\alpha}_m
    $$

    则称 $\bm{\beta}$ 可以由向量组 $\bm{A}$ **线性表示**，或 $\bm{\beta}$ 是向量组 $\bm{A}$ 的一个**线性组合**。

#### 等价向量组

!!! info 等价向量组
    如果向量组 $\bm{A} \colon \bm{\alpha}_1,\, \bm{\alpha}_2 ,\, \cdots ,\, \bm{\alpha}_m$ 可以由向量组 $\bm{B} \colon \bm{\beta}_1,\, \bm{\beta}_2 ,\, \cdots ,\, \bm{\beta}_s$ 线性表示，且向量组 $\bm{B}$ 可以由向量组 $\bm{A}$ 线性表示，则称向量组 $\bm{A}$ 和 $\bm{B}$ **等价**，表示为 $\bm{A} \leftrightarrow \bm{B}$。

#### 线性相关和线性无关

!!! info 线性相关
    给定向量组 $\bm{A}\colon \bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots ,\, \bm{\alpha}_m$，如果存在不全为零的数 $k_1,\, k_2,\, \cdots ,\, k_m$，使得

    $$
    k_1 \bm{\alpha}_1 + k_2 \bm{\alpha}_2 + \cdots + k_m \bm{\alpha}_m = \bm{\theta}
    $$

    则称向量组 $\bm{A}$ **线性相关**，否则称向量组 $\bm{A}$ **线性无关**。

!!! memo ""
    以后我可能更常用 $\bm{\theta}$ 表示零向量，而不是 $\bm{0}$。

!!! note ""
    另外，$\bm{A} \leftrightarrow \bm{B} \nimplies \bm{A},\, \bm{B}$ 线性相关性相同。

    例如 $\bm{A} = \left( \bm{\alpha}_1,\, \bm{\alpha}_2 \right),\; \bm{B} = \left( \bm{\alpha}_1,\, \bm{\alpha}_2,\, \bm{\alpha}_1 + \bm{\alpha}_2 \right) $，则 $\bm{A} \leftrightarrow \bm{B}$，但 $\bm{A}$ 线性无关，$\bm{B}$ 线性相关。

设 $\bm{\alpha}_i \in \R^{n}$，则 $\left( \bm{\alpha}_1,\, \cdots,\, \bm{\alpha}_n \right) $ 线性相关 $\iff \det\left( \left[ \bm{\alpha}_1,\, \cdots ,\, \bm{\alpha}_n \right]  \right) = 0$。

!!! note ""
    1. 如果一向量组的部分向量组线性相关，则整个向量组线性相关。
    2. 如果一向量组线性无关，则它的任意部分向量组也线性无关。

!!! note ""
    向量组线性相关 $\iff $ 齐次线性方程组有非零解 $\iff $ 齐次线性方程组的系数行列式为 $0$。

!!! info ""
    设向量组 $\bm{A} \colon \bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots ,\, \bm{\alpha}_r$ 线性无关，而向量组 $\bm{B} \colon \bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots ,\, \bm{\alpha}_r,\, \bm{\beta}$ 线性相关，则向量 $\bm{\beta}$ 可由向量组 $\bm{A}$ 线性表示。

!!! example ""
    证明：设 $n$ 维向量组 $\bm{A} \colon \bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots ,\, \bm{\alpha}_n$ 线性无关，$\bm{B}$ 为 $n$ 阶方阵，则向量组 $\bm{B} \bm{\alpha}_1,\, \bm{B} \bm{\alpha}_2,\, \cdots ,\, \bm{B} \bm{\alpha}_n$ 线性无关 $\iff \bm{B}$ 可逆。

    ---

    $\implies $：

    $\left[\bm{B} \bm{\alpha}_1,\, \bm{B} \bm{\alpha}_2,\, \cdots ,\, \bm{B} \bm{\alpha}_n\right] = \bm{B} \left[ \bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots ,\, \bm{\alpha}_n \right] = \bm{B} \bm{A}$

    而 $ \det \left( \bm{B} \bm{A} \right) = \det \left( \bm{B} \right) \det \left( \bm{A} \right) \ne 0$，所以 $\bm{B}$ 可逆。

    $\impliedby $：

    令 $k_1 \bm{B} \bm{\alpha}_1 + k_2 \bm{B} \bm{\alpha}_2 + \cdots + k_n \bm{B} \bm{\alpha}_n = \bm{\theta}$，则左乘 $\bm{B}^{-1}$，得

    $$
    k_1 \bm{\alpha}_1 + k_2 \bm{\alpha}_2 + \cdots + k_n \bm{\alpha}_n = \bm{\theta}
    $$

    而 $\bm{A}$ 线性无关，所以 $k_1 = k_2 = \cdots = k_n = 0$，所以 $\bm{B} \bm{\alpha}_1,\, \bm{B} \bm{\alpha}_2,\, \cdots ,\, \bm{B} \bm{\alpha}_n$ 线性无关。

### 极大无关组 秩

#### 极大无关组

!!! info 极大无关组
    最小的能张成原向量组 $\bm{A}$ 的子向量组称为 $\bm{A}$ 的一个**极大无关组**。

    按书本的定义即是：

    极大无关组是原向量组的一个分组，满足：
    1. 其线性无关
    2. 原向量组的任意一个向量都可以由它线性表示

#### 秩

!!! info 秩
    向量组 $\bm{A}$ 的极大无关组的向量个数称为 $\bm{A}$ 的**秩**，记为 $\rank\left( \bm{A} \right)$。

    极大无关组向量个数相同的证明我忘了。由于课本先讲的矩阵的秩，课本的证明用了矩阵的秩。

可理解为，秩是向量组张成的空间的维数。

若 $\bm{A}$ 可由 $\bm{B}$ 线性表示，则 $\rank\left( \bm{A} \right) \le \rank\left( \bm{B} \right)$。

既然 $\bm{B}$ 能线性表示 $\bm{A}$，则说明 $\bm{A}$ 张成的空间是 $\bm{B}$ 张成的空间的子空间。

由于矩阵 $\bm{A}_{m \times n}$ 可以看作是 $m$ 个 $n$ 维行向量组成的向量组，及 $n$ 个 $m$ 维列向量组成的向量组，所以矩阵的秩分为行秩和列秩。

!!! info ""
    对矩阵作初等变换（包括初等行变换和初等列变换）不改变其行秩和列秩。

行秩和列秩相等，称为矩阵的秩。证明我也忘了（非常关键重要的部分怎么感觉上课好像没怎么听）。

!!! info ""
    设 $\bm{A}$ 为 $m \times n$ 矩阵，则 $\rank\left( \bm{A} \right) \le \min \left\lbrace m,\, n \right\rbrace$。

!!! note ""
    对 $\bm{A}_{m \times n},\, \bm{P}_m,\, \bm{Q}_n$，且有 $\left\lvert \bm{P} \right\rvert \left\lvert \bm{Q} \right\rvert \ne 0$ 有

    $$
    \rank\left( \bm{P} \bm{A} \bm{Q} \right) = \rank\left( \bm{A} \right)
    $$

    即对矩阵作初等变换不改变其秩。

!!! note ""
    对 $k\ne 0$，有

    $$
    \rank(k \bm{A}) = \rank(\bm{A})
    $$

!!! note ""
    对 $\bm{A} = \left[ a_{ij} \right]_{m \times n},\, \bm{B} = \left[ b_{ij} \right]_{m \times r},\, \bm{C} = \begin{bmatrix} \bm{A} & \bm{B} \end{bmatrix}_{m \times (n + r)}$ 有

    $$
    \rank(\bm{A}) + \rank(\bm{B}) \ge \rank(\bm{C}) \ge \max\left\lbrace \rank(\bm{A}), \rank(\bm{B}) \right\rbrace
    $$

    也非常好理解，毕竟 $\bm{A}$ 和 $\bm{B}$ 向量组的极大无关组的向量一定也是 $\bm{C}$ 的极大无关组的向量（或可由里面的向量表示），所以 $\rank(\bm{C}) \ge \max\left\lbrace \rank(\bm{A}), \rank(\bm{B}) \right\rbrace$。

    而如果 $\bm{B}$ 极大无关组的每个向量都不可由 $\bm{A}$ 的极大无关组线性表示，那么 $\bm{B}$ 就提供了最多的新信息，所以这种情况下有 $\rank(\bm{A}) + \rank(\bm{B}) = \rank(\bm{C})$。

    当然，这不是严谨的证明。

!!! note ""
    对同阶矩阵 $\bm{A},\, \bm{B}$，有

    $$
    \rank(\bm{A}) + \rank(\bm{B}) \ge \rank(\bm{A} + \bm{B}) \ge \left| \rank(\bm{A}) - \rank(\bm{B}) \right|
    $$

    下界的证明：

    $$
    \begin{aligned}
        \rank(\bm{A}) &= \rank[(\bm{A} + \bm{B}) + (- \bm{B})]\\
        &\le \rank(\bm{A} + \bm{B}) + \rank(- \bm{B}) \\
        &= \rank(\bm{A} + \bm{B}) + \rank(\bm{B})
    \end{aligned}
    $$

    从而有

    $$
    \rank(\bm{A} + \bm{B}) \ge \rank(\bm{A}) - \rank(\bm{B})
    $$

!!! note ""
    对 $\bm{A}_{m \times n},\, \bm{B}_{n \times r}$，有

    $$
    \min \left\lbrace \rank(\bm{A}), \rank(\bm{B}) \right\rbrace \ge \rank(\bm{A} \bm{B}) \ge \rank(\bm{A}) + \rank(\bm{B}) - n
    $$

    上界的证明：

    设 $\rank(\bm{A}) = r_1,\, \rank(\bm{B}) = r_2$，则有可逆矩阵 $\bm{P},\, \bm{Q}$ 使得 $\bm{A} = \bm{P} \bm{A}',\, \bm{B} = \bm{B}' \bm{Q}$，其中 $\bm{A}'$ 为行梯形矩阵。$\bm{B}'$ 为列梯形矩阵。

    那么有 $\bm{A} \bm{B} = \bm{P} \bm{A}' \bm{B}' \bm{Q}$，所以 $\rank(\bm{A} \bm{B}) = \rank(\bm{A}' \bm{B}')$。

    而 $\bm{A}'$ 至多有 $r_1$ 个非零行，$\bm{B}'$ 至多有 $r_2$ 个非零列，所以 $\bm{A}' \bm{B}'$ 至多有 $r_1$ 个非零行，$r_2$ 个非零列，所以 $\rank(\bm{A}' \bm{B}') \le \min \left\lbrace r_1,\, r_2 \right\rbrace$。

    所以 $\rank(\bm{A} \bm{B}) \le \min \left\lbrace r_1,\, r_2 \right\rbrace$。

    下界的证明：

    设 $\rank(\bm{A}) = s$，设 $\bm{P}\bm{A}\bm{Q}$ 为标准形矩阵，其中 $\bm{P},\, \bm{Q}$ 为可逆矩阵，则

    $$
    \begin{aligned}
        \rank(\bm{A}\bm{B}) &= \rank\left[\left(\bm{P}\bm{A}\bm{Q}\right)\left(\bm{Q}^{-1}\bm{B}\right)\right] \\
        &= \rank\left( \begin{bmatrix}
            \bm{E}_s & \bm{O} \\
            \bm{O} & \bm{O}
        \end{bmatrix} \begin{bmatrix}
            \bm{B}_1 \\
            \bm{B}_2
        \end{bmatrix} \begin{matrix}
            s \\
            n-s
        \end{matrix}\right) \\
        &= \rank\left( \begin{bmatrix}
            \bm{B}_1 \\
            \bm{O}
        \end{bmatrix} \right)\\
        &\ge \rank\left( \begin{bmatrix}
            \bm{B}_1 \\
            \bm{B}_2
        \end{bmatrix} \right) - \rank\left( \begin{bmatrix}
            \bm{O} \\
            \bm{B}_2
        \end{bmatrix} \right)\\
        &= \rank(\bm{B}) - \rank(\bm{B}_2)\\
        &\ge \rank(\bm{B}) - (n - s)\\
        &= \rank(\bm{A}) + \rank(\bm{B}) - n
    \end{aligned}
    $$

!!! note ""
    对 $\bm{A} = \begin{bmatrix} \bm{P} & \bm{O} \\ \bm{O} & \bm{Q} \end{bmatrix},\, \bm{B} = \begin{bmatrix} \bm{P} & \bm{R} \\ \bm{O} & \bm{Q} \end{bmatrix}$ 有
    $$
    \begin{aligned}
    \rank(\bm{A}) &= \rank(\bm{P}) + \rank(\bm{Q})\\
    \rank(\bm{B}) &\ge \rank(\bm{P}) + \rank(\bm{Q})
    \end{aligned}
    $$

### 线性方程组解的结构

#### 高斯消元法

以前写过了，这里主要提一点比较容易错的。~~顺便试着写一下增广矩阵~~。

!!! note ""
    解 $\bm{A}\bm{X}=\bm{B}$，即是解增广矩阵 $\bm{C} = \begin{bmatrix}\bm{A} & \bm{B}\end{bmatrix}$。仅可以进行**行变换**。

    最后会变为 $\bm{C}' = \begin{bmatrix}\bm{E} & \bm{A}^{-1}\bm{B}\end{bmatrix}$，有 $\bm{X} = \bm{A}^{-1}\bm{B}$。

    ---

    解 $\bm{X}\bm{A} = \bm{B}$，即是解增广矩阵 $\bm{C} = \begin{bmatrix} \bm{A} \\ \bm{B} \end{bmatrix}$。仅可以进行**列变换**。

    最后会变为 $\bm{C}' = \begin{bmatrix} \bm{E} \\ \bm{B}\bm{A}^{-1} \end{bmatrix}$，有 $\bm{X} = \bm{B}\bm{A}^{-1}$。

!!! memo ""
    咦，似乎还没有写具体的增广矩阵的例子。

#### 线性方程组的可解性

一般线性方程组可表示为

$$
\left\lbrace\begin{aligned}
    a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n &= b_1 \\
    a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n &= b_2 \\
    \vdots \\
    a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n &= b_m
\end{aligned}\right.
$$

矩阵形式为

$$
\bm{A}\bm{x} = \bm{\beta}
$$

!!! info ""
    线性方程组 $\bm{A}\bm{x}=\bm{\beta}$ 有解 $\iff$ 系数矩阵的秩等于增广矩阵的秩。

    1. 当 $\rank(\bm{A}) = \rank(\bm{B}) = n$ 时，方程组有唯一解。
    2. 当 $\rank(\bm{A}) = \rank(\bm{B}) < n$ 时，方程组有无穷多解。

    其中

    $$
    \bm{A} = \begin{bmatrix}
        a_{11} & a_{12} & \cdots & a_{1n} \\
        a_{21} & a_{22} & \cdots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{m1} & a_{m2} & \cdots & a_{mn}
    \end{bmatrix}
    $$

    $$
    \bm{B} = \begin{bmatrix}
        \bm{A} & \bm{\beta}
    \end{bmatrix}= \begin{bmatrix}
        \begin{array}{cccc|c}
            a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\
            a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\
            \vdots & \vdots & \ddots & \vdots & \vdots \\
            a_{m1} & a_{m2} & \cdots & a_{mn} & b_m
            \end{array}
        \end{bmatrix}
    $$

<details>
<summary>增广矩阵 LaTeX 代码</summary>

```latex
\begin{bmatrix}
    \begin{array}{cccc|c}
        a_{11} & a_{12} & \cdots & a_{1n} & b_1 \\
        a_{21} & a_{22} & \cdots & a_{2n} & b_2 \\
        \vdots & \vdots & \ddots & \vdots & \vdots \\
        a_{m1} & a_{m2} & \cdots & a_{mn} & b_m
    \end{array}
\end{bmatrix}
```

</details>

#### 齐次线性方程组

齐次线性方程组可表示为 $\bm{A}\bm{x}=\bm{\theta}$。

而注意到齐次线性方程组的解的线性组合仍然是它的解，所以称表示出齐次线性方程组所有解的极大无关向量组为齐次线性方程组的**基础解系**。

!!! info ""
    设 $\bm{A}\in\R^{m \times n}$，若 $\rank(\bm{A}) = n$，则齐次线性方程组 $\bm{A}\bm{x}=\bm{\theta}$ 只有零解；若 $\rank(\bm{A}) < n$，则齐次线性方程组 $\bm{A}\bm{x}=\bm{\theta}$ 有非零解。

    若 $\rank(\bm{A}) = n$，由前知方程组有唯一解，显然零解是唯一解。

!!! note 齐次线性方程组基础解系的解法
    1. 将齐次线性方程组的系数矩阵化为行梯形矩阵。
    2. 将每个只有一个 $1$ 的列向量作为非自由变量，其余列向量作为自由变量，得到基础解系。
    3. 将自由变量自由取值（通常取为只有一个维数为 $1$，其余全为 $0$ 的向量 $\bm{e}_i$ ），表示非自由变量，从而得到所有解向量，即基础解系。

由此可知基础解系向量的个数为 $n - \rank(\bm{A})$。

!!! note ""
    对于一般的情况，化简为以下形式：

    $$
    \begin{bmatrix}
        1 & d_{12} & \cdots & 0 & d_{1, i_2 + 1} & \cdots & 0 & d_{i, i_r + 1} & \cdots & d_{1n} \\
        0 & 0 & \cdots & 1 & d_{2, i_2 + 1} & \cdots & 0 & d_{2, i_r + 1} & \cdots & d_{2n} \\
        \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & \cdots & 0 & 0 & \cdots & 1 & d_{r, i_r + 1} & \cdots & d_{rn} \\
        0 & 0 & \cdots & 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\
        \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & \cdots & 0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\
    \end{bmatrix}\\
    \begin{matrix}
        1 & 2 & \cdots & i_2 & i_2 + 1 & \cdots & i_r & i_r + 1 & \cdots & n \\
        \hphantom{1} & \hphantom{d_{12}} & \hphantom{\cdots} & \hphantom{0} & \hphantom{d_{1, i_2 + 1}} & \hphantom{\cdots} & \hphantom{0} & \hphantom{d_{i, i_r + 1}} & \hphantom{\cdots} & \hphantom{d_{1n}} \\
    \end{matrix}
    $$

    解释一下，$i_{j}\;(j = 2, 3, \cdots, r)$ 代表第 $j$ 个非自由变量的位置（没有 $i_1$ 因为 $i_1$ 就是 $1$）。

    然后看每行，根据其方程组的含义，可以将每行的 $1$ 解出来。也就是说我们可以用剩下的 $n-r$ 个变量，给它们赋值（彼此赋值线性无关），也就是作为*自由变量*。

    为了方便起见，往往是依次将一个自由变量取为 $1$，而其它取为 $0$，总计 $n - r$ 种取法（$n - r$ 个变量每个取一次 $1$）。

!!! note ""
    若系数矩阵化简后为
    
    $$
    \begin{bmatrix}
        1 & 0 & \cdots & 0 & d_{1, r+1} & \cdots & d_{1n} \\
        0 & 1 & \cdots & 0 & d_{2, r+1} & \cdots & d_{2n} \\
        \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & \cdots & 1 & d_{r, r+1} & \cdots & d_{rn} \\
        0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\
        \vdots & \vdots & \ddots & \vdots & \vdots & \ddots & \vdots \\
        0 & 0 & \cdots & 0 & 0 & \cdots & 0 \\
    \end{bmatrix}
    $$
    
    或者写成块的形式
    
    $$
    \begin{bmatrix}
        \bm{E}_r & \bm{\beta}_1 & \bm{\beta}_2 & \cdots & \bm{\beta}_{n-r} \\
        \bm{O} & \bm{\theta} & \bm{\theta} & \cdots & \bm{\theta}
    \end{bmatrix}
    $$
    
    那么基础解系为
    
    $$
    \bm{\alpha}_1 = 
    \begin{bmatrix}
        -\bm{\beta}_1 \\
        1 \\
        0 \\
        \vdots \\
        0
    \end{bmatrix},\,
    \bm{\alpha}_2 =
    \begin{bmatrix}
        -\bm{\beta}_2 \\
        0 \\
        1 \\
        \vdots \\
        0
    \end{bmatrix},\,
    \cdots,\,
    \bm{\alpha}_{n-r} =
    \begin{bmatrix}
        -\bm{\beta}_{n-r} \\
        0 \\
        0 \\
        \vdots \\
        1
    \end{bmatrix}
    $$

若 $\bm{A} \in \R^{n}$，则有

$$
\rank(\bm{A}^{*}) = \begin{cases}
    n, & \rank(\bm{A}) = n\\
    1, & \rank(\bm{A}) = n - 1\\
    0, & \rank(\bm{A}) \le n - 2
\end{cases}
$$

证明：

1. 若 $\rank(\bm{A}) = n$，则 $\bm{A}$ 可逆，所以 $\left\lvert \bm{A}^{*} \right\rvert \ne 0$，所以 $\rank(\bm{A}^{*}) = n$。
2. 若 $\rank(\bm{A}) \le n - 2$，根据秩的子式定义，有 $\bm{A}$ 所有 $n - 1$ 阶子式为 $0$，所以 $\bm{A}^{*} = \bm{O}$，所以 $\rank(\bm{A}^{*}) = 0$。
3. 若 $\rank(\bm{A}) = n - 1$，由于 $\bm{A}\bm{A}^{*}=\left\lvert \bm{A} \right\rvert \bm{E} = \bm{O}$，根据矩阵乘积秩的大小关系，有 $\rank(\bm{A}) + \rank(\bm{A}^{*}) - n \le \rank(\bm{O}) = 0$，即 $\rank(\bm{A}^{*}) \le 1$。而 $\bm{A}^{*}\ne \bm{O}$，有 $\rank(\bm{A}^{*})\ne 0$。所以 $\rank(\bm{A}^{*}) = 1$。

#### 非齐次线性方程组

非齐次线性方程组可表示为 $\bm{A}\bm{x}=\bm{\beta}$。通解可表示为

$$
\bm{\eta} + \bm{\alpha}
$$

其中 $\bm{A}\bm{\eta}=\bm{\beta}$（称为**特解**），$\bm{\alpha}$ 为齐次线性方程组 $\bm{A}\bm{x}=\bm{\theta}$ 的解。

### 等价表述及证明

设 $\bm{A} \in \R^{m \times n},\, \bm{B} \in \R^{k \times n}$，则以下三种表述等价：
1. $\bm{A} \bm{x} = \bm{\theta}$ 与 $\bm{B} \bm{x} = \bm{\theta}$ 同解。
2. $\rank\left( \begin{bmatrix} \bm{A} \\ \bm{B} \end{bmatrix} \right) = \rank(\bm{A}) = \rank(\bm{B})$ 
3. $\bm{A},\, \bm{B}$ 行向量组等价

只需证明 (1) $\implies $ (2) $\implies $ (3) $\implies $ (1) 即可。

(1) $\implies $ (2)：

设解集分别为 $W_1,\, W_2$，则 $W_1 = W_2$。

那么 $\bm{A},\, \bm{B}$ 的极大无关组向量个数相同，即 $n - \rank(\bm{A}) = n - \rank(\bm{B})$，从而 $\rank(\bm{A}) = \rank(\bm{B})$。

既然 $\bm{A} \bm{x} = \bm{\theta}$ 与 $\bm{B} \bm{x} = \bm{\theta}$ 同解，那么 $\bm{A} \bm{\eta} = \bm{\theta} \implies \bm{B} \bm{\eta} = \bm{\theta} \implies \begin{bmatrix} \bm{A} \\ \bm{B} \end{bmatrix} \bm{\eta} = \bm{\theta}$。

而 $\begin{bmatrix} \bm{A} \\ \bm{B} \end{bmatrix} \bm{\eta} = \bm{\theta} \implies \begin{bmatrix} \bm{A} \bm{\eta} \\ \bm{B} \bm{\eta} \end{bmatrix} = \bm{\theta} \implies \left\lbrace\begin{aligned} \bm{A} \bm{\eta} &= \bm{\theta} \\ \bm{B} \bm{\eta} &= \bm{\theta} \end{aligned}\right.$，也就是说 $\bm{A} \bm{\eta} = \bm{\theta}$ 与 $\bm{B} \bm{\eta} = \bm{\theta}$ 同解。

根据上面的结论，也有 $\rank(\bm{A}) = \rank(\bm{B}) =  \rank\left( \begin{bmatrix} \bm{A} \\ \bm{B} \end{bmatrix} \right) $。

(2) $\implies $ (3)：

设 $\bm{A} = \left[  \bm{\alpha}_i \right]_m,\, \bm{B} = \left[ \bm{\beta}_i \right]_k$。

则 $\rank(\bm{A}) = \rank\left( \begin{bmatrix} \bm{A} \\ \bm{B} \end{bmatrix} \right) \implies \rank\left\lbrace \bm{\alpha}_1 ,\, \cdots ,\, \bm{\alpha}_m \right\rbrace = \rank\left\lbrace \bm{\alpha}_1 ,\, \cdots ,\, \bm{\alpha}_m ,\, \bm{\beta}_1 ,\, \cdots ,\, \bm{\beta}_k \right\rbrace$。

即 $\bm{\beta}_1 ,\, \cdots ,\, \bm{\beta}_k$ 可由 $\bm{\alpha}_1 ,\, \cdots ,\, \bm{\alpha}_m$ 线性表示，反之亦然。所以 $\bm{A},\, \bm{B}$ 行向量组等价。

(3) $\implies $ (1)：

既然 $\bm{A},\, \bm{B}$ 行向量组等价，那么有 $\bm{A} = \bm{C}_{m \times k}\bm{B},\, \bm{B} = \bm{D}_{k \times m} \bm{A}$ 且 $\bm{C},\, \bm{D}$ 可逆。

若 $\bm{A} \bm{x} = \bm{\theta}$，则有 $\bm{B} \bm{x} = \bm{D} \bm{A} \bm{x} = \bm{D} \bm{\theta} = \bm{\theta}$，反之亦然。即 $\bm{A} \bm{x} = \bm{\theta}$ 与 $\bm{B} \bm{x} = \bm{\theta}$ 同解。

!!! info ""
    若 $\bm{A},\, \bm{B} \in \R^{m \times n}$，则 $\bm{A} \leftrightarrow \bm{B} \iff \rank(\bm{A}) = \rank(\bm{B})$，也就是说，无法推出 $\bm{A}$ 与 $\bm{B}$ 行向量组等价。这是一个弱化的结论。

### 其它

#### 1.

!!! quote ""
    若 $\rank(\bm{A}_n) = n - 1$，证明 $\left( \bm{A}^{*} \right)^2 = \lambda \bm{A}^{*}$。

由前可知 $\rank(\bm{A}^{*}) = 1$，从而可以将 $\bm{A}^{*}$ 分解为 $\bm{P}\bm{\Lambda}\bm{Q}$，其中 $\bm{P},\, \bm{Q}$ 为可逆矩阵，$\bm{\Lambda}$ 为 $\begin{bmatrix} 1 & \bm{O}_{1 \times (n-1)} \\ \bm{O}_{(n - 1)\times 1} & \bm{O}_{(n - 1)\times (n - 1)} \end{bmatrix}$。

而 $\bm{\Lambda}$ 又可以分解为两个 $n$ 维向量（列向量）的乘积，即

$$
\bm{\Lambda} = \begin{bmatrix}
    1 \\
    0 \\
    \vdots \\
    0
\end{bmatrix} \begin{bmatrix}
    1 & 0 & \cdots & 0
\end{bmatrix}
$$

若记 $\bm{P} = \begin{bmatrix} \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n \end{bmatrix}$，$\bm{Q} = \begin{bmatrix} \bm{\beta}_1^\intercal \\ \bm{\beta}_2^\intercal \\ \cdots \\ \bm{\beta}_n^\intercal \end{bmatrix}$，则有

$$
\begin{aligned}
    \bm{A}^{*} &= \bm{P}\bm{\Lambda}\bm{Q}\\
    &= \begin{bmatrix}
        \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n
    \end{bmatrix} \begin{bmatrix}
    1 \\
    0 \\
    \vdots \\
    0
    \end{bmatrix}
    \begin{bmatrix}
        1 & 0 & \cdots & 0
    \end{bmatrix}
    \begin{bmatrix}
        \bm{\beta}_1^\intercal \\ \bm{\beta}_2^\intercal \\ \cdots \\ \bm{\beta}_n^\intercal
    \end{bmatrix}\\
    &= \bm{\alpha}_1 \bm{\beta}_1^\intercal
\end{aligned}
$$

从而

$$
\begin{aligned}
    \bm{A}^{*} \bm{A}^{*} &= \bm{\alpha}_1 \bm{\beta}_1^\intercal \bm{\alpha}_1 \bm{\beta}_1^\intercal\\
    &= \bm{\alpha}_1 \left( \bm{\beta}_1^\intercal \bm{\alpha}_1 \right) \bm{\beta}_1^\intercal\\
    &= \bm{\alpha}_1 \left(\lambda \right) \bm{\beta}_1^\intercal\\
    &= \lambda \bm{\alpha}_1 \bm{\beta}_1^\intercal\\
    &= \lambda \bm{A}^{*}
\end{aligned}
$$
