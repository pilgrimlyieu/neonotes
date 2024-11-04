---
layout: post
title: 特征值与特征向量
date: 2023-11-22 20:44:20
updated: 2023-12-21 14:18:28
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 特征值与特征向量

### 定义

一些向量在经过矩阵的线性变换后，仍然保有原来的方向，使得这些向量像是只进行了<u>伸缩变换</u>一样。我们便将这些向量称为矩阵的**特征向量**，而这些向量所对应的伸缩比例便是矩阵的**特征值**。

根据定义，我们可以得到矩阵的特征向量和特征值的定义式：

$$
\bm{A} \bm{\eta} = \lambda \bm{\eta}
$$

其中，$\bm{\eta}$ 为特征向量，$\lambda$ 为特征值。

显然 $\bm{\eta}\ne \bm{\theta}$，那么

$$
\begin{aligned}
    \bm{A} \bm{\eta} - \lambda \bm{E} \bm{\eta} &= \bm{0}\\
    (\bm{A} - \lambda \bm{E}) \bm{\eta} &= \bm{0}
\end{aligned}
$$

既然这个齐次线性方程组有非零解 $\bm{\eta}$，那么系数矩阵 $\bm{A} - \lambda \bm{E}$ 的行列式必然为零，即

$$
\left\lvert \bm{A} - \lambda \bm{E} \right\rvert = 0
$$

!!! memo ""
    课本上比较常用 $\left\lvert \lambda \bm{E} - \bm{A} \right\rvert = 0$。不过因为实际用时用课本的表示方式需要将矩阵元素取负，容易出错，所以这里采用了另一种表示方式。

这个方程称为矩阵 $\bm{A}$ 的**特征方程**，它是一个关于 $\lambda$ 的 $n$ 次多项式，称为**特征多项式**,方程的解称为**特征根**。解这个方程，就可以得到矩阵 $\bm{A}$ 的所有特征值。

把特征值代入特征方程，就可以得到对应的特征向量。

### 意义

为什么我们要研究伸缩变换，因为伸缩变换真的很好啊！

如果矩阵只进行伸缩变换，那么只需要将原向量各基向量进行对应的伸缩变换，就可以得到经过矩阵线性变换向量的结果。同样地，如果矩阵只进行伸缩变换，矩阵的乘法也就非常简单了。

只进行伸缩变换的矩阵形如

$$
\begin{bmatrix}
    \lambda_1 & 0 & \cdots & 0\\
    0 & \lambda_2 & \cdots & 0\\
    \vdots & \vdots & \ddots & \vdots\\
    0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$

对第 $i$ 个基向量进行 $\lambda_i$ 倍的伸缩变换。

然而遗憾的是，大部分矩阵并不止进行伸缩变换。

我们可以设想，在经过某个线性变换后，一个一般的矩阵 $\bm{A}$ 变成了一个新矩阵 $\bm{\Lambda}$，这个矩阵只进行伸缩变换，因此就可以方便地进行线性变换。然而这是在另一个向量空间进行的变换，我们还需要将结果「翻译」回原来的向量空间，即再乘以那个线性变换的逆变换。翻译成数学语言就是

$$
\bm{A} = \bm{P} \bm{\Lambda} \bm{P}^{-1}
$$

也即 $\bm{A} \bm{P} = \bm{P} \bm{\Lambda}$。

不妨设 $\bm{P} = \begin{bmatrix} \bm{\eta}_1 & \bm{\eta}_2 & \cdots & \bm{\eta}_n \end{bmatrix}$，那么

$$
\begin{aligned}
    \bm{A} \bm{P} &= \bm{A} \begin{bmatrix} \bm{\eta}_1 & \bm{\eta}_2 & \cdots & \bm{\eta}_n \end{bmatrix}\\
    &= \begin{bmatrix} \bm{A} \bm{\eta}_1 & \bm{A} \bm{\eta}_2 & \cdots & \bm{A} \bm{\eta}_n \end{bmatrix}\\
\end{aligned}
$$

而

$$
\begin{aligned}
    \bm{P} \bm{\Lambda} &= \begin{bmatrix} \bm{\eta}_1 & \bm{\eta}_2 & \cdots & \bm{\eta}_n \end{bmatrix} \begin{bmatrix}
        \lambda_1 & 0 & \cdots & 0\\
        0 & \lambda_2 & \cdots & 0\\
        \vdots & \vdots & \ddots & \vdots\\
        0 & 0 & \cdots & \lambda_n
    \end{bmatrix}\\
    &= \begin{bmatrix} \lambda_1 \bm{\eta}_1 & \lambda_2 \bm{\eta}_2 & \cdots & \lambda_n \bm{\eta}_n \end{bmatrix}
\end{aligned}
$$

因此

$$
\left\lbrace\begin{aligned}
    \bm{A} \bm{\eta}_1 &= \lambda_1 \bm{\eta}_1\\
    \bm{A} \bm{\eta}_2 &= \lambda_2 \bm{\eta}_2\\
    \vdots\\
    \bm{A} \bm{\eta}_n &= \lambda_n \bm{\eta}_n
\end{aligned}\right.
$$

也就是说，要解 $\bm{A} \bm{\eta} = \lambda \bm{\eta}$，即解特征方程。这也从另一个角度提供了特征值的意义。

有了 $\bm{A} = \bm{P} \bm{\Lambda} \bm{P}^{-1}$，就可以比较方便地计算矩阵的幂：

$$
\begin{aligned}
    \bm{A}^n &= \left( \bm{P} \bm{\Lambda} \bm{P}^{-1} \right)^n\\
    &= \overbrace{\left( \bm{P} \bm{\Lambda} \bm{P}^{-1} \right) \left( \bm{P} \bm{\Lambda} \bm{P}^{-1} \right) \cdots \left( \bm{P} \bm{\Lambda} \bm{P}^{-1} \right)}^n\\
    &= \overbrace{\bm{P} \bm{\Lambda} \bm{P}^{-1} \bm{P} \bm{\Lambda} \bm{P}^{-1} \cdots \bm{P} \bm{\Lambda} \bm{P}^{-1}}^n\\
    &= \bm{P} \overbrace{\bm{\Lambda} \bm{\Lambda} \cdots \bm{\Lambda}}^n \bm{P}^{-1}\\
    &= \bm{P} \bm{\Lambda}^n \bm{P}^{-1}
\end{aligned}
$$

### 计算

计算特征向量时，对于重根的特征值，往往会出现多个解向量。可以证明，任取 $k$ 个特征值 $\lambda_1, \lambda_2, \cdots, \lambda_k$，对应的特征向量 $\bm{\eta}_1, \bm{\eta}_2, \cdots, \bm{\eta}_k$，那么这 $k$ 个特征向量线性无关。

证明：

即证 $\rank\left\lbrace \bm{\eta}_1,\, \cdots,\, \bm{\eta}_k \right\rbrace = k$。

反证法，设 $\rank\left\lbrace \bm{\eta}_1,\, \cdots,\, \bm{\eta}_k \right\rbrace = s \le k - 1$，那么不妨设 $\bm{\eta}_1,\, \cdots,\, \bm{\eta}_s$ 为一个极大无关组，从而 $\exist_{k_1,\, \cdots,\, k_s},$

$$
\bm{\eta}_{s + 1} = k_1 \bm{\eta}_1 + \cdots + k_s \bm{\eta}_s\tag{1}
$$

那么

$$
\begin{aligned}
\bm{A} \bm{\eta}_{s + 1} &= \bm{A} \left( k_1 \bm{\eta}_1 + \cdots + k_s \bm{\eta}_s \right)\\
        &= k_1 \bm{A} \bm{\eta}_1 + \cdots + k_s \bm{A} \bm{\eta}_s\\
    \lambda_{s+1} \bm{\eta}_{s+1} &= k_1 \lambda_1 \bm{\eta}_1 + \cdots + k_s \lambda_s \bm{\eta}_s\tag{2}
\end{aligned}
$$

$\lambda_{s + 1}(1) - (2)$ 得

$$
k_1(\lambda_{s + 1} - \lambda_1) \bm{\eta}_1 + \cdots + k_s(\lambda_{s + 1} - \lambda_s) \bm{\eta}_s = \bm{\theta}
$$

既然 $\bm{\eta}_1,\, \cdots,\, \bm{\eta}_s$ 为一个极大无关组。那么其系数必然全为零。又由于 $\lambda$ 的任意性，从而 $k_1 = \cdots = k_s = 0$，于是 $\bm{\eta}_{s + 1} = \bm{\theta}$，与 $\bm{\eta}_{s + 1}$ 为特征向量矛盾。

因此 $\rank\left\lbrace \bm{\eta}_1,\, \cdots,\, \bm{\eta}_k \right\rbrace = k$，即 $\bm{\eta}_1,\, \cdots,\, \bm{\eta}_k$ 线性无关。

!!! note ""
    这不意味着重根数 $=$ 对应特征矩阵基础解系向量的个数。

    如 $\bm{A} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$，有 $\left\lvert \lambda \bm{E} - \bm{A} \right\rvert = (\lambda - 1)^2$ 有重根 $\lambda = 1$，但是只有一个特征向量 $\bm{\eta} = k\begin{bmatrix} 1 \\ 0 \end{bmatrix}\;(k \ne  0)$。

### 性质

!!! note ""
    $\bm{A} \leftrightarrow \bm{B} \iff \bm{A},\, \bm{B}$ 有相同特征多项式。

    ---

    证明：

    $$
    \begin{aligned}
    f_{\bm{B}}(\lambda) &= \left\lvert \lambda \bm{E} - \bm{B} \right\rvert\\
    &= \left\lvert \lambda \bm{E} - \bm{P}^{-1} \bm{A} \bm{P} \right\rvert\\
    &= \left\lvert  \bm{P}^{-1} \lambda \bm{E} \bm{P} - \bm{P}^{-1} \bm{A} \bm{P} \right\rvert\\
    &= \left\lvert \bm{P}^{-1} (\lambda \bm{E} - \bm{A}) \bm{P} \right\rvert\\
    &= \left\lvert \bm{P}^{-1} \right\rvert \left\lvert \lambda \bm{E} - \bm{A} \right\rvert \left\lvert \bm{P} \right\rvert\\
    &= \left\lvert \lambda \bm{E} - \bm{A} \right\rvert\\
    &= f_{\bm{A}}(\lambda)
    \end{aligned}
    $$

!!! note ""
    设 $f(x)$ 为关于 $x$ 的多项式，若 $\lambda$ 为 $\bm{A}$ 的特征值，$f(\lambda)$ 为 $f(\bm{A})$ 的特征值。

!!! note ""
    $$
    \prod_{i=1}^{n} \lambda_i = \left\lvert \bm{A}_n \right\rvert
    $$

    ---

    证明：

    $$
    \begin{aligned}
        \left\lvert \lambda \bm{E} - \bm{A} \right\rvert &= \begin{vmatrix}
            \lambda - a_{11} & -a_{12} & \cdots & -a_{1n}\\
            -a_{21} & \lambda - a_{22} & \cdots & -a_{2n}\\
            \vdots & \vdots & \ddots & \vdots\\
            -a_{n1} & -a_{n2} & \cdots & \lambda - a_{nn}
        \end{vmatrix}\\
        &= \lambda^n + c_{n - 1} \lambda^{n - 1} + \cdots + c_1 \lambda + c_0\\
        &= \prod_{i=1}^{n} (\lambda - \lambda_i)
    \end{aligned}
    $$

    从而有 $c_0 = (-1)^n \displaystyle \prod_{i=1}^{n} \lambda_i$。

    令 $\lambda = 0$，得 $c_0 = \left\lvert - \bm{A} \right\rvert = (-1)^n \left\lvert \bm{A}_n \right\rvert$，即

    $$
    \prod_{i=1}^{n} \lambda_i = \left\lvert \bm{A}_n \right\rvert
    $$

定义方阵的**迹**为主对角线上元素之和，记作 $\trace(\bm{A})$。

!!! note ""
    $$
    \sum_{i=1}^{n} \lambda_i = \trace(\bm{A}_n)
    $$

    ---

    证明：

    按行展开，有

    $$
    \begin{aligned}
        \left\lvert \lambda \bm{E} - \bm{A} \right\rvert &= \begin{vmatrix}
            \lambda - a_{11} & -a_{12} & \cdots & -a_{1n}\\
            -a_{21} & \lambda - a_{22} & \cdots & -a_{2n}\\
            \vdots & \vdots & \ddots & \vdots\\
            -a_{n1} & -a_{n2} & \cdots & \lambda - a_{nn}
        \end{vmatrix}\\
        &= (\lambda - a_{11}) A_{11} + (-1)^{1 + 2} (-a_{12}) A_{12} + \cdots + (-1)^{1 + n} (-a_{1n}) A_{1n}\\
    \end{aligned}
    $$

    而 $A_{12},\, \cdots,\, A_{1n}$ 中 $\lambda$ 的次数最高为 $n - 2$，于是可以不用考虑，同理有

    $$
    \begin{aligned}
        \left\lvert \lambda \bm{E} - \bm{A} \right\rvert ={} & (\lambda - a_{11}) A_{11}\\
        ={} & (\lambda - a_{11}) (\lambda - a_{22}) \cdots (\lambda - a_{nn}) \\
         &+ d_{n - 2} \lambda^{n - 2} + \cdots + d_1 \lambda + d_0\\
    \end{aligned}
    $$

    则 $\lambda^{n - 1}$ 的系数为 $- \displaystyle \sum_{i=1}^{n} a_{ii} = \trace(\bm{A})$，而 $\left\lvert \lambda \bm{E} - \bm{A} \right\rvert = \displaystyle \prod_{i=1}^{n} (\lambda - \lambda_i)$，从而还有 $\lambda^{n - 1}$ 的系数为 $- \displaystyle \sum_{i=1}^{n} \lambda_i$，于是有

    $$
    \sum_{i=1}^{n} \lambda_i = \trace(\bm{A}_n)
    $$

!!! note ""
    设 $\bm{A} \in \R^{m \times n},\, \bm{B} \in \R^{n \times m}$，则有

    $$
    \lambda^n \left\lvert \lambda \bm{E}_m - \bm{A} \bm{B} \right\rvert = \lambda^m \left\lvert \lambda \bm{E}_n - \bm{B} \bm{A} \right\rvert
    $$

    ---

    证明：

    注意到

    $$
    \left\lbrace\begin{aligned}
        \lambda^n \left\lvert \lambda \bm{E}_m - \bm{A} \bm{B} \right\rvert = \begin{vmatrix}
            \lambda \bm{E}_m - \bm{A} \bm{B} &   \\
              & \lambda \bm{E}_n
        \end{vmatrix} \kern{-0.3em}&= \left\lvert \lambda \bm{E}_{m + n} - \begin{bmatrix}
            \bm{A} \bm{B} &   \\
              & \bm{O}_n
        \end{bmatrix} \right\rvert\\
        \lambda^m \left\lvert \lambda \bm{E}_n - \bm{B} \bm{A} \right\rvert = \begin{vmatrix}
            \lambda \bm{E}_m &   \\
              & \lambda \bm{E}_n - \bm{B} \bm{A}
        \end{vmatrix} \kern{-0.3em}&= \left\lvert \lambda \bm{E}_{m + n} - \begin{bmatrix}
            \bm{O}_m &   \\
              & \bm{B} \bm{A}
        \end{bmatrix} \right\rvert
    \end{aligned}\right.
    $$

    即证

    $$
    \left\lvert \lambda \bm{E}_{m + n} - \begin{bmatrix}
        \bm{A} \bm{B} &   \\
          & \bm{O}_n
    \end{bmatrix} \right\rvert = \left\lvert \lambda \bm{E}_{m + n} - \begin{bmatrix}
        \bm{O}_m &   \\
          & \bm{B} \bm{A}
    \end{bmatrix} \right\rvert
    $$

    而

    $$
    \left\lbrace\begin{aligned}
        \begin{bmatrix}
            \bm{A} \bm{B} &   \\
              & \bm{O}_n
        \end{bmatrix} &= \begin{bmatrix}
            \bm{O} & \bm{A} \\
            \bm{O} & \bm{O}
        \end{bmatrix} \begin{bmatrix}
            \bm{O} & \bm{O} \\
            \bm{B} & \bm{O}
        \end{bmatrix}\\
        \begin{bmatrix}
            \bm{O}_m &   \\
              & \bm{B} \bm{A}
        \end{bmatrix} &= \begin{bmatrix}
            \bm{O} & \bm{O} \\
            \bm{B} & \bm{O}
        \end{bmatrix} \begin{bmatrix}
            \bm{A} & \bm{O} \\
            \bm{O} & \bm{O}
        \end{bmatrix}
    \end{aligned}\right.
    $$

    而「若 $\bm{A},\, \bm{B}$ 为同阶方阵，则有 $\bm{A} \bm{B}$ 与 $\bm{B} \bm{A}$ 特征值相同」[^1]，得证。

    ---

    由此可知 $m$ 阶方阵 $\bm{A} \bm{B}$ 与 $n$ 阶方阵 $\bm{B} \bm{A}$ 的特征值相同，且相同的非零特征值的代数重数相同（即 $\trace(\bm{A} \bm{B}) = \trace(\bm{B} \bm{A})$）。

    [^1]: 严谨证明略。对于 $\left\lvert \bm{A} \right\rvert\ne 0$ 的情况，有 $\bm{A} (\bm{B} \bm{A}) \bm{A}^{-1} = \bm{A} \bm{B}$，即 $\bm{A} \bm{B}$ 与 $\bm{B} \bm{A}$ 相似，故特征值相同。对于 $\left\lvert \bm{A} \right\rvert= 0$ 的情况，按线代老师的说法，用「扰动」，算极限。只不过我不喜欢这个方法，所以从略。

!!! note ""
    若 $\bm{A} \bm{\eta} = \lambda \bm{\eta}$，则 $\bm{A}^{-1} \bm{\eta} = \dfrac{1}{\lambda} \bm{\eta}$。

    即 $\bm{A}$ 的特征向量 $\bm{\eta}$ 也是 $\bm{A}^{-1}$ 的特征向量，且特征值互为倒数。
