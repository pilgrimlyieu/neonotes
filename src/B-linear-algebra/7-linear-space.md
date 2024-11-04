---
layout: post
title: 线性空间
date: 2023-12-15 11:51:58
updated: 2023-12-29 10:06:40
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

### 概念

!!! info 数域
    设 $\mathbb{K}$ 是由一些*复数*组成的集合，其中包括 $0,\, 1$。若 $\mathbb{K}$ 中任意两个数的<u>和</u>、<u>差</u>、<u>积</u>、<u>商</u>（除数不为 $0$）仍在 $\mathbb{K}$ 中，则称 $\mathbb{K}$ 为一个**数域**。

    即 $\mathbb{K} \subseteq \C,\, \left\lbrace 0, 1 \right\rbrace \subseteq \mathbb{K}$，且 $\forall a,\, b \in \mathbb{K}$，有 $a \pm b,\, a \times b,\, a/b\; (b \ne 0)\in \mathbb{K}$（对加减乘除运算封闭），则称 $\mathbb{K}$ 为一个**数域**。

!!! note ""
    对数域 $\mathbb{K}$，有 $\Q \subseteq \mathbb{K}$。

    ---

    证明：

    显然 $\Z \subseteq \mathbb{K}$，而所有有理数可表示为两个整数的比值，故 $\Q \subseteq \mathbb{K}$。

    因此最小的数域是 $\Q$，而 $\C$ 是最大的数域。

    同时也知道整数 $\Z$ 不是数域，而是*数环*。

!!! info ""
    设非空集合 $V$，而 $\mathbb{K}$ 是一个数域。在 $V$ 上定义了两种运算（课本上 $\oplus$ 用的是 $+$，$\otimes$ 省略，即与普通加法和数乘运算相同。为了更好理解抽象的概念，我换了符号来表示）：
    - **加法**：对于任意 $\alpha, \beta \in V$，有唯一的 $\alpha \oplus \beta \in V$ 与之对应，记为 $\alpha \oplus \beta$。（$V \times V \to V;\; (\alpha, \beta) \mapsto \alpha \oplus \beta$）
    - **数乘**：对于任意 $k \in \mathbb{K}$，$\alpha \in V$，有唯一的 $k \otimes\alpha \in V$ 与之对应，记为 $k\otimes\alpha$。（$\mathbb{K} \times V \to V;\; (k, \alpha) \mapsto k \otimes \alpha$）

    若 $V$ 上定义了加法和数乘（并且对这两种运算封闭），且满足以下条件，则称 $V$ 是数域 $\mathbb{K}$ 上的**线性空间**：
    1. $\alpha \oplus \beta = \beta \oplus \alpha$
    2. $(\alpha \oplus \beta) \oplus \gamma = \alpha \oplus (\beta \oplus \gamma)$
    3. 存在 $\theta \in V$，使得 $\alpha \oplus \theta = \alpha$（$\theta$ 是**零元素**，也是一个抽象的概念）
    4. 对于任意 $\alpha \in V$，存在 $\beta \in V$，使得 $\alpha \oplus \beta = \theta$（$\beta$ 是 $\alpha$ 的**负元素**，记为 $\ominus\alpha$⟦$- \alpha$⟧）
    5. $1\otimes\alpha = \alpha$（$1$ 是 $\mathbb{K}$ 中的**单位数**）
    6. 对任意 $k,\,  l \in \mathbb{K}$，$\alpha \in V$，有 $(k \times l)\otimes\alpha = k\otimes(l\otimes\alpha)$
    7. 对任意 $k,\,  l \in \mathbb{K}$，$\alpha \in V$，有 $(k + l)\otimes\alpha = (k\otimes\alpha) \oplus (l\otimes\alpha)$
    8. 对任意 $k \in \mathbb{K}$，$\alpha,\,  \beta \in V$，有 $k\otimes(\alpha \oplus \beta) = (k\otimes\alpha) \oplus (k\otimes\beta)$

    若 $\mathbb{K} = \R$，则称 $V$ 是**实线性空间**；若 $\mathbb{K} = \C$，则称 $V$ 是**复线性空间**。

!!! note 一些线性空间的例子
    设 $\mathbb{K}$ 是一个数域：
    - $\mathbb{K}^n$ 是 $\mathbb{K}$ 上的线性空间（加法和数乘即为向量的加法和数乘）
    - $M_{m \times n}(\mathbb{K})$ 是 $\mathbb{K}$ 上的线性空间（加法和数乘即为矩阵的加法和数乘）
    - $P_n(\mathbb{K})[x]$（$\mathbb{K}_n[x]$）是 $\mathbb{K}$ 上的线性空间（$P_n(\mathbb{K})[x] = \left\lbrace \displaystyle \sum_{i = 0}^n a_i x^i \mathrel{\Biggm|} a_i \in \mathbb{K} \right\rbrace$，加法和数乘即为多项式的加法和数乘）
    - 设 $\bm{A} \in M_{m \times n}(\R)$，则齐次方程组的解集 $V = \left\lbrace x \in \R^n \mid \bm{A}x = 0 \right\rbrace$ 是实线性空间（加法和数乘即为向量的加法和数乘）
    - $C([0, 1]) = \left\lbrace  f \mid f\colon [0, 1] \to \R \text{ 连续}\right\rbrace$ 是实线性空间（加法和数乘即为函数的加法和数乘）
    - 零空间 $V=\left\lbrace \theta \right\rbrace$

!!! note ""
    零元素唯一。

    ---

    证明：

    $$
    \begin{rcases}
        \theta_1 \oplus \theta_2 = \theta_1 \\
        \theta_2 \oplus \theta_1 = \theta_2
    \end{rcases}
    \implies \theta_1 = \theta_2
    $$

!!! note ""
    负元素唯一。

    ---

    证明：

    $$
    \begin{aligned}
        \begin{rcases}
            \alpha \oplus \beta_1 = \theta \\
            \alpha \oplus \beta_2 = \theta
        \end{rcases}
        \implies \beta_1 &= \beta_1 \oplus \theta \\
        &= \beta_1 \oplus (\alpha \oplus \beta_2) \\
        &= (\beta_1 \oplus \alpha) \oplus \beta_2 \\
        &= \theta \oplus \beta_2 \\
        &= \beta_2
    \end{aligned}
    $$

!!! note ""
    $0 \otimes \alpha = \theta$。

    ---

    证明：

    $$
    \begin{aligned}
        0 \otimes \alpha &= (0 + 0) \otimes \alpha \\
        &= (0 \otimes \alpha) \oplus (0 \otimes \alpha) \\
        (0 \otimes \alpha) \oplus (\ominus (0 \otimes \alpha)) &= (0 \otimes \alpha) \oplus (0 \otimes \alpha) \oplus (\ominus (0 \otimes \alpha)) \\
        \theta &= (0 \otimes \alpha) \oplus \theta \\
        \implies 0 \otimes \alpha &= \theta
    \end{aligned}
    $$

!!! note ""
    $k \otimes \theta = \theta$。

    ---

    证明：

    $$
    \begin{aligned}
        k \otimes \theta &= k \otimes (\theta \oplus \theta) \\
        &= (k \otimes \theta) \oplus (k \otimes \theta) \\
        \implies k \otimes \theta &= \theta
    \end{aligned}
    $$

!!! note ""
    $(-1) \otimes \alpha = \ominus \alpha$。

    ---

    证明：

    $$
    \begin{aligned}
        \alpha \oplus \left(-1 \otimes \alpha\right) &= (1 \otimes \alpha) \oplus \left(-1 \otimes \alpha\right) \\
         &= (1 + (-1)) \otimes \alpha \\
        &= 0 \otimes \alpha \\
        &= \theta \\
        \implies (-1) \otimes \alpha &= \ominus \alpha
    \end{aligned}
    $$

!!! note ""
    若 $k \otimes \alpha = \theta$，则 $k = 0$ 或 $\alpha = \theta$。

    ---

    证明：

    不妨设 $k\ne 0$ 且 $\alpha \ne \theta$，则

    $$
    \begin{aligned}
        \alpha &= 1 \otimes \alpha \\
        &= \left(\dfrac{1}{k}\times k\right) \otimes \alpha \\
        &= \dfrac{1}{k} \times \left(k \otimes \alpha\right) \\
        &= \dfrac{1}{k} \otimes \theta \\
        &= \theta
    \end{aligned}
    $$

    矛盾！故 $k \ne 0$ 与 $\alpha \ne \theta$ 不能同时成立，也即 $k \otimes \alpha = \theta \implies k = 0$ 或 $\alpha = \theta$。

因此也称线性空间为**向量空间**，线性空间中的元素称为**向量**。

于是下面的向量及向量空间，将恢复使用 `\bm` 来表示。除非是更像是数（例如函数的线性空间）的部分，继续使用正常的字体。

由于加法和数乘运算的封闭性，$V$ 中向量组 $\alpha_1,\, \alpha_2,\, \cdots,\, \alpha_r$ 的任意线性组合

$$
(k_1 \otimes \alpha_1) \oplus (k_2 \otimes \alpha_2) \oplus \cdots \oplus (k_r \otimes \alpha_r) \in V
$$

其中 $k_1,\, k_2,\, \cdots,\, k_r \in \mathbb{K}$。

下面从抽象走向具体，就不再使用 $\oplus$ 和 $\otimes$ 了（就是懒）。

### 维数、基、坐标

!!! info ""
    对向量组 $\bm{V} = V(\mathbb{K})$ 中的向量 $\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_n$，若存在不全为 $0$ 的数 $k_1, k_2, \cdots, k_n \in \mathbb{K}$，使得

    $$
    k_1\bm{\alpha}_1 + k_2\bm{\alpha}_2 + \cdots + k_n\bm{\alpha}_n = \bm{\theta}
    $$

    则称 $\bm{\alpha}_1, \bm{\alpha}_2, \cdots, \bm{\alpha}_n$ **线性相关**，否则称**线性无关**。

!!! example ""
    对互不相等的 $k_1,\, k_2,\, \cdots,\, k_n \in \R$，有

    $$
    \e^{k_1 x},\, \e^{k_2 x},\, \cdots,\, \e^{k_n x}
    $$

    线性无关。

    ---

    证明：

    有 $l_1,\, l_2,\, \cdots,\, l_n \in \R$，使得

    $$
    l_1 \e^{k_1 x} + l_2 \e^{k_2 x} + \cdots + l_n \e^{k_n x} \equiv 0
    $$

    求导 $n - 1$ 次，得

    $$
    \begin{bmatrix}
        \e^{k_1 x} & \e^{k_2 x} & \cdots & \e^{k_n x} \\
        k_1 \e^{k_1 x} & k_2 \e^{k_2 x} & \cdots & k_n \e^{k_n x} \\
        \vdots & \vdots & \ddots & \vdots \\
        k_1^{n - 1} \e^{k_1 x} & k_2^{n - 1} \e^{k_2 x} & \cdots & k_n^{n - 1} \e^{k_n x}
    \end{bmatrix}
    \begin{bmatrix}
        l_1 \\
        l_2 \\
        \vdots \\
        l_n
    \end{bmatrix}=
    \begin{bmatrix}
        0 \\
        0 \\
        \vdots \\
        0
    \end{bmatrix}
    $$

    范德蒙德行列式知系数行列式不为零，从而 $l_1 = l_2 = \cdots = l_n = 0$，故 $\e^{k_1 x},\, \e^{k_2 x},\, \cdots,\, \e^{k_n x}$ 线性无关。

    具体而言，系数行列式

    $$
    \begin{aligned}
        D &= \exp\left(\sum\limits_{i=1}^{n}k_i x\right)
        \begin{vmatrix}
            1 & 1 & \cdots & 1 \\
            k_1 & k_2 & \cdots & k_n \\
            \vdots & \vdots & \ddots & \vdots \\
            k_1^{n - 1} & k_2^{n - 1} & \cdots & k_n^{n - 1}
        \end{vmatrix} \\
        &= \exp\left(\sum\limits_{i=1}^{n}k_i x\right)\prod_{1 \le i < j \le n}(k_j - k_i)\\
        &\ne 0
    \end{aligned}
    $$


!!! info ""
    若线性空间 $\bm{V}$ 中存在 $n$ 个线性无关的向量

    $$
    \bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n
    $$

    使得 $\bm{V}$ 中任意向量 $\alpha$ 都可由其线性表示，则称 $\bm{V}$ 是 **$n$ 维**线性空间，记作 $\operatorname{dim}(\bm{V}) = n$ ，$\bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n$ 是 $\bm{V}$ 的一组**基**。

    并记 $\operatorname{dim}(\left\lbrace \bm{\theta} \right\rbrace) = 0$，即零空间的维数为 $0$。

    若 $\bm{V}$ 中有<u>任意多</u>个线性无关的向量，则称 $\bm{V}$ 是**无限维**线性空间。

!!! example ""
    设 $\bm{V} = M_{m \times n}(\R),\, \mathbb{K} = \R$，则

    $$
    \begin{aligned}
        \bm{A} &= [a_{ij}]_{m \times n}\\
        &= \begin{bmatrix}
            a_{11} & a_{12} & \cdots & a_{1n} \\
            a_{21} & a_{22} & \cdots & a_{2n} \\
            \vdots & \vdots & \ddots & \vdots \\
            a_{m1} & a_{m2} & \cdots & a_{mn}
        \end{bmatrix} \\
        &= \sum_{j=1}^{n} \sum_{i=1}^{m} a_{ij} \bm{E}_{ij}
    \end{aligned}
    $$

    其中 $\bm{E}_{ij}$ 是 $m \times n$ 的矩阵，其第 $i$ 行第 $j$ 列元素为 $1$，其余元素为 $0$。

    由此可知 $M_{m \times n}(\R)$ 是 $mn$ 维线性空间，其基为 $\left\lbrace \bm{E}_{ij} \mid i = 1,\, 2,\, \cdots,\, m;\; j = 1,\, 2,\, \cdots,\, n \right\rbrace$。

!!! example ""
    设 $V = P_n(\R)[x]$，则

    $$
    f(x) = \sum_{i=0}^{n} a_i x^i
    $$

    设

    $$
    h(x) = k_0 \cdot 1 + k_1 x + k_2 x^2 + \cdots + k_n x^n \equiv 0
    $$

    从而 $k_0 = 0$，求导得 $k_1 = 0$，以此类推（$\dfrac{\d^m }{\d x^m}h(0) = m! \cdot k_m = 0$），可知 $k_0 = k_1 = \cdots = k_n = 0$，故 $1,\, x,\, x^2,\, \cdots,\, x^n$ 线性无关。

    <details>
    <summary>不同的基</summary>

    由于 $P_n(\R)[x]$ 是 $n + 1$ 维线性空间，故其基不止一组，例如

    $$
    1,\, (x - 1),\, (x - 1)^2,\, \cdots,\, (x - 1)^n
    $$

    也是一组基。

    先证明 $1,\, x,\, x^2,\, \cdots,\, x^n$ 可由 $1,\, (x - 1),\, (x - 1)^2,\, \cdots,\, (x - 1)^n$ 线性表示：

    $$
    \begin{aligned}
        x^i &= (x - 1 + 1)^i \\
        &= \sum_{j=0}^{i} \binom{i}{j} (x - 1)^j \\
    \end{aligned}
    $$

    再证明 $1,\, (x - 1),\, (x - 1)^2,\, \cdots,\, (x - 1)^n$ 线性无关：跟上面的证明类似，不再赘述。

    </details>

!!! example ""
    设 $V = C([0, 1])$，则 $V$ 是无限维线性空间。

    ---

    证明：

    $$
    1,\, x,\, \cdots,\, x^n,\, \cdots
    $$

    线性无关，而 $n$ 可以任意大，故 $V$ 是无限维线性空间。

!!! info ""
    设 $\bm{V} = V(\mathbb{K})$ 是 $n$ 维线性空间，$\bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n$ 是 $V$ 的一组基，则任意 $\bm{\alpha} \in \bm{V}$ 都可由 $\bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n$ 线性表示，即

    $$
    \begin{aligned}
        \bm{\alpha} &= \sum_{i=1}^{n} x_i \bm{\varepsilon}_i\\
        &= x_1 \bm{\varepsilon}_1 + x_2 \bm{\varepsilon}_2 + \cdots + x_n \bm{\varepsilon}_n
    \end{aligned}
    $$

    其中 $x_i \in \mathbb{K}$，且表示方式唯一。

    称 $x_1,\, x_2,\, \cdots,\, x_n$ 是 $\bm{\alpha}$ 在基 $\bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n$ 下的**坐标**，记作

    $$
    \bm{x} = (x_1,\, x_2,\, \cdots,\, x_n)
    $$

    或

    $$
    \bm{x} = \begin{bmatrix}
        x_1 \\
        x_2 \\
        \vdots \\
        x_n
    \end{bmatrix}
    $$

    有

    $$
    \bm{\alpha} = \begin{bmatrix}
        \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
    \end{bmatrix}
    \begin{bmatrix}
        x_1 \\
        x_2 \\
        \vdots \\
        x_n
    \end{bmatrix}
    $$

!!! info 基变换
    设 $\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_n$ 与 $\bm{\beta}_1,\, \bm{\beta}_2,\, \cdots,\, \bm{\beta}_n$ 是 $n$ 维向量空间 $\bm{V}$ 的两组基，且

    $$
    \left\lbrace\begin{aligned}
        \bm{\beta}_1 &= a_{11}\bm{\alpha}_1 + a_{21}\bm{\alpha}_2 + \cdots + a_{n1}\bm{\alpha}_n \\
        \bm{\beta}_2 &= a_{12}\bm{\alpha}_1 + a_{22}\bm{\alpha}_2 + \cdots + a_{n2}\bm{\alpha}_n \\
        \vdots \\
        \bm{\beta}_n &= a_{1n}\bm{\alpha}_1 + a_{2n}\bm{\alpha}_2 + \cdots + a_{nn}\bm{\alpha}_n
    \end{aligned}\right.
    $$

    即

    $$
    \begin{bmatrix}
        \bm{\beta}_1 & \bm{\beta}_2 & \cdots & \bm{\beta}_n
    \end{bmatrix}=
    \begin{bmatrix}
        \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n
    \end{bmatrix}
    \underbrace{\begin{bmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
        a_{21} & a_{22} & \cdots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{bmatrix}}_{\bm{P}}\tag{1}
    $$

    $\bm{P}$ 称为从基 $\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_n$ 到基 $\bm{\beta}_1,\, \bm{\beta}_2,\, \cdots,\, \bm{\beta}_n$ 的**过渡矩阵**，$(1)$ 式称为**基变换公式**。

!!! note ""
    设 $\bm{V}$ 中元素 $\bm{\gamma}$ 在基 $\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_n$ 下的坐标为 $\bm{x} = (x_1, x_2, \cdots, x_n)^\intercal$，在基 $\bm{\beta}_1,\, \bm{\beta}_2,\, \cdots,\, \bm{\beta}_n$ 下的坐标为 $\bm{y} = (y_1, y_2, \cdots, y_n)^\intercal$，则有**坐标变换公式**

    $$
    \bm{x} = \bm{P}\bm{y}
    $$

    或

    $$
    \bm{y} = \bm{P}^{-1}\bm{x}
    $$

    其中 $\bm{P}$ 为从基 $\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_n$ 到基 $\bm{\beta}_1,\, \bm{\beta}_2,\, \cdots,\, \bm{\beta}_n$ 的过渡矩阵。

    ---

    由

    $$
    \begin{aligned}
        \begin{bmatrix}
            \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n
        \end{bmatrix}
        \begin{bmatrix}
            x_1 \\ x_2 \\ \vdots \\ x_n
        \end{bmatrix}&=
        \begin{bmatrix}
            \bm{\beta}_1 & \bm{\beta}_2 & \cdots & \bm{\beta}_n
        \end{bmatrix}
        \begin{bmatrix}
            y_1 \\ y_2 \\ \vdots \\ y_n
        \end{bmatrix}\\
        &= \begin{bmatrix}
            \bm{\alpha}_1 & \bm{\alpha}_2 & \cdots & \bm{\alpha}_n
        \end{bmatrix}
        \bm{P}
        \begin{bmatrix}
            y_1 \\ y_2 \\ \vdots \\ y_n
        \end{bmatrix}
    \end{aligned}
    $$

    得

    $$
    \begin{bmatrix}
        x_1 \\ x_2 \\ \vdots \\ x_n
    \end{bmatrix} = \bm{P}
    \begin{bmatrix}
        y_1 \\ y_2 \\ \vdots \\ y_n
    \end{bmatrix}
    $$

    即

    $$
    \bm{x} = \bm{P}\bm{y}
    $$

### 线性子空间

#### 概念

!!! info ""
    设 $\bm{W}$ 是数域 $\mathbb{K}$ 上的线性空间 $\bm{V}$ 的一个*非空子集*，如果 $\bm{W}$ <u>关于 $\bm{V}$ 上的加法和数乘</u>运算也构成数域 $\mathbb{K}$ 上的一个线性空间，则称 $\bm{W}$ 是 $\bm{V}$ 的一个**线性子空间**（**子空间**），记作 $\bm{W} \subseteq \bm{V}$，若 $\bm{W} \neq \bm{V}$，则记作 $\bm{W} \subset \bm{V}$。

!!! example 子空间
    1. 零子空间：仅含零元素，最小的子空间。
    2. 平凡子空间：$\bm{V}$ 本身。
    3. 非平凡子空间：不是零子空间，也不是 $\bm{V}$ 本身的子空间。（不一定存在）

!!! note ""
    线性空间 $\bm{V}$ 的一个非空子集 $\bm{W}$ 是 $\bm{V}$ 的子空间的充要条件是：$\bm{W}$ 对于 $\bm{V}$ 上的加法和数乘运算封闭，可表示为对任意的 $\bm{\alpha},\, \bm{\beta} \in \bm{W}$ 和任意的 $\lambda,\, \mu \in \mathbb{K}$，有

    $$
    \lambda\bm{\alpha} + \mu\bm{\beta} \in \bm{W}
    $$

!!! info ""
    给定线性空间 $\bm{V}=V(\mathbb{K})$ 中向量组 $\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_s$，则它们的所有的线性组合构成一个 $\bm{V}$ 的子空间，称为**由向量组 $\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_s$ 生成的子空间**，记作

    $$
    \span\{\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_s\} \text{ 或 } L\{\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_s\}
    $$

    特别地，零子空间是由零向量生成的子空间 $\span\{\bm{\theta}\}$。

    显然

    $$
    \dim(\span\{\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_s\}) = \rank\{\bm{\alpha}_1,\, \bm{\alpha}_2,\, \cdots,\, \bm{\alpha}_s\}
    $$

!!! note ""
    实系数齐次方程组 $\bm{A} \bm{x} = \bm{\theta}$ 解空间 $\bm{W}$ 是 $\R^n$ 的子空间，则有

    $$
    \dim(\bm{W}) = n - \rank(\bm{A})
    $$

#### 运算

!!! info ""
    设 $\bm{W}_1$ 和 $\bm{W}_2$ 是线性空间 $\bm{V}$ 的两个子空间，定义 $\bm{W}_1$ 和 $\bm{W}_2$ 的**交**为

    $$
    \bm{W}_1 \cap \bm{W}_2 = \{\bm{\alpha} \mid \bm{\alpha} \in \bm{W}_1 \text{ 且 } \bm{\alpha} \in \bm{W}_2\}
    $$

    显然，$\bm{W}_1 \cap \bm{W}_2$ 也是 $\bm{V}$ 的子空间。


!!! info ""
    设 $\bm{W}_1$ 和 $\bm{W}_2$ 是线性空间 $\bm{V}$ 的两个子空间，定义 $\bm{W}_1$ 和 $\bm{W}_2$ 的**和**为

    $$
    \bm{W}_1 + \bm{W}_2 = \{\bm{\alpha} + \bm{\beta} \mid \bm{\alpha} \in \bm{W}_1,\, \bm{\beta} \in \bm{W}_2\}
    $$

    显然，$\bm{W}_1 + \bm{W}_2$ 也是 $\bm{V}$ 的子空间，且有 $\bm{W}_1 \cup \bm{W}_2 \subseteq \bm{W}_1 + \bm{W}_2$。

!!! tip ""
    对齐次线性方程组

    $$
    \left\lbrace\begin{aligned}
        a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n &= 0\\
        a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n &= 0\\
        \vdots\\
        a_{m1} x_1 + a_{m2} x_2 + \cdots + a_{mn} x_n &= 0
    \end{aligned}\right.
    $$

    令 $\bm{W}_k = \left\lbrace \bm{x} \in \R^n \mid a_{k1} x_1 + a_{k2} x_2 + \cdots + a_{kn} x_n = 0 \right\rbrace$，则 $\bm{W}_k$ 是 $\R^n$ 的子空间，且 $\bm{W} = \bm{W}_1 \cap \bm{W}_2 \cap \cdots \cap \bm{W}_m$ 是该方程组的解空间。

!!! note ""
    设 $\bm{W}_1$ 和 $\bm{W}_2$ 是线性空间 $\bm{V}$ 的两个子空间，则

    $$
    \dim(\bm{W}_1) + \dim(\bm{W}_2) = \dim(\bm{W}_1 + \bm{W}_2) + \dim(\bm{W}_1 \cap \bm{W}_2)
    $$

    特别地，若 $\bm{W}_1 \cap \bm{W}_2 = \{\bm{\theta}\}$，则

    $$
    \dim(\bm{W}_1) + \dim(\bm{W}_2) = \dim(\bm{W}_1 + \bm{W}_2)
    $$

    ---

    证明：

    仅考虑 $\dim(\bm{W}_1),\, \dim(\bm{W}_2)$ 有限的情况。

    设 $\dim(\bm{W}_1) = n_1,\, \dim(\bm{W}_2) = n_2$，设 $\dim(\bm{W}_1 \cap \bm{W}_2) = m$。

    记 $\bm{W}_1 \cap \bm{W}_2$ 的一组基为 $\bm{\alpha}_1,\, \cdots,\, \bm{\alpha}_m$。

    则 $\bm{\alpha}_1,\, \cdots,\, \bm{\alpha}_m$ 可以扩充为 $\bm{W}_1$ 的一组基 $\bm{\alpha}_1,\, \cdots,\, \bm{\alpha}_m,\, \bm{\beta}_1,\, \cdots,\, \bm{\beta}_{n_1 - m}$，还可以扩充为 $\bm{W}_2$ 的一组基 $\bm{\alpha}_1,\, \cdots,\, \bm{\alpha}_m,\, \bm{\gamma}_1,\,  \cdots,\, \bm{\gamma}_{n_2 - m}$。

    则

    $$
    \begin{aligned}
        \dim(\bm{W}_1 + \bm{W}_2) &= \dim(\span\{\bm{\alpha}_1,\, \cdots,\, \bm{\alpha}_m,\, \bm{\beta}_1,\, \cdots,\, \bm{\beta}_{n_1 - m},\, \bm{\gamma}_1,\, \cdots,\, \bm{\gamma}_{n_2 - m}\})\\
        &\le n_1 + n_2 - m\\
    \end{aligned}
    $$

    即证 $\bm{\alpha}_1,\, \cdots,\, \bm{\alpha}_m,\, \bm{\beta}_1,\, \cdots,\, \bm{\beta}_{n_1 - m},\, \bm{\gamma}_1,\, \cdots,\, \bm{\gamma}_{n_2 - m}$ 线性无关。

    设

    $$
    \begin{aligned}
        &\overbrace{(k_1 \bm{\alpha}_1 + \cdots + k_m \bm{\alpha}_m + p_1 \bm{\beta}_1 + \cdots + p_{n_1 - m} \bm{\beta}_{n_1 - m})}^{\bm{\alpha}} + \\
        &(q_1 \bm{\gamma}_1 + \cdots + q_{n_2 - m} \bm{\gamma}_{n_2 - m}) = \bm{\theta}
    \end{aligned}
    $$

    则 $\bm{\alpha} \in \bm{W}_1 \cap \bm{W}_2$，即

    $$
    \bm{\alpha} = c_1 \bm{\alpha}_1 + \cdots + c_m \bm{\alpha}_m
    $$

    又

    $$
    \bm{\alpha} = - (q_1 \bm{\gamma}_1 + \cdots + q_{n_2 - m} \bm{\gamma}_{n_2 - m})
    $$

    即

    $$
    c_1 \bm{\alpha}_1 + \cdots + c_m \bm{\alpha}_m + q_1 \bm{\gamma}_1 + \cdots + q_{n_2 - m} \bm{\gamma}_{n_2 - m} = \bm{\theta}
    $$

    而 $\bm{\alpha}_1,\, \cdots,\, \bm{\alpha}_m,\, \bm{\gamma}_1,\, \cdots,\, \bm{\gamma}_{n_2 - m}$ 线性无关，故 $c_1 = \cdots = c_m = q_1 = \cdots = q_{n_2 - m} = 0$，即 $\bm{\alpha} = \bm{\theta}$。

    即

    $$
    k_1 \bm{\alpha}_1 + \cdots + k_m \bm{\alpha}_m + p_1 \bm{\beta}_1 + \cdots + p_{n_1 - m} \bm{\beta}_{n_1 - m} = \bm{\theta}
    $$

    而 $\bm{\alpha}_1,\, \cdots,\, \bm{\alpha}_m,\, \bm{\beta}_1,\, \cdots,\, \bm{\beta}_{n_1 - m}$ 线性无关，故 $k_1 = \cdots = k_m = p_1 = \cdots = p_{n_1 - m} = 0$。

    从而 $\bm{\alpha}_1,\, \cdots,\, \bm{\alpha}_m,\, \bm{\beta}_1,\, \cdots,\, \bm{\beta}_{n_1 - m},\, \bm{\gamma}_1,\, \cdots,\, \bm{\gamma}_{n_2 - m}$ 线性无关，即

    $$
    \dim(\bm{W}_1 + \bm{W}_2) = n_1 + n_2 - m
    $$

!!! info ""
    设 $\bm{W}_1,\, \bm{W}_2$ 是线性空间 $\bm{V}$ 的两个子空间，若 $\bm{W}_1 + \bm{W}_2$ 中每个向量 $\bm{\alpha}$ 都可以唯一地表示为 $\bm{\alpha} = \bm{\alpha}_1 + \bm{\alpha}_2$，其中 $\bm{\alpha}_1 \in \bm{W}_1,\, \bm{\alpha}_2 \in \bm{W}_2$，则称 $\bm{W}_1 + \bm{W}_2$ 是**直和**，记作 $\bm{W}_1 \oplus \bm{W}_2$（或 $\bm{W}_1 \dotplus \bm{W}_2$）。

    若 $\bm{W} = \bm{W}_1 \oplus \bm{W}_2$，则称在 $\bm{W}$ 内 $\bm{W}_1$ 是 $\bm{W}_2$ 的**补空间**。

若 $\bm{W}_1 \cap \bm{W}_2 \ne \left\lbrace \bm{\theta} \right\rbrace$，则有 $\bm{p} \in \bm{W}_1 \cap \bm{W}_2$ 满足

$$
\begin{aligned}
    \bm{p} &= \bm{p} + \bm{\theta}\\
    \bm{p} &= \bm{\theta} + \bm{p}
\end{aligned}
$$

故 $\bm{W}_1 + \bm{W}_2$ 不是直和。从而有

!!! note ""
    $\bm{W}_1 + \bm{W}_2$ 是直和的充要条件是 $\bm{W}_1 \cap \bm{W}_2 = \left\lbrace \bm{\theta} \right\rbrace$。

    ---

    证明：

    必要性已经说明了，下证充分性。

    设 $\bm{W}_1 + \bm{W}_2$ 不是直和，则存在 $\bm{\gamma} \in \bm{W}_1 + \bm{W}_2$ 满足

    $$
    \begin{aligned}
        \bm{\gamma} &= \bm{\alpha}_1 + \bm{\beta}_1\\
        \bm{\gamma} &= \bm{\alpha}_2 + \bm{\beta}_2
    \end{aligned}
    $$

    其中 $\bm{\alpha}_1,\, \bm{\alpha}_2 \in \bm{W}_1,\, \bm{\beta}_1,\, \bm{\beta}_2 \in \bm{W}_2$，且 $\bm{\alpha}_1 \ne \bm{\alpha}_2,\, \bm{\beta}_1 \ne \bm{\beta}_2$。

    相减得

    $$
    (\bm{\alpha}_1 - \bm{\alpha}_2) + (\bm{\beta}_1 - \bm{\beta}_2) = \bm{\theta}
    $$

    从而

    $$
    \bm{w} = \bm{\alpha}_1 - \bm{\alpha}_2 = - (\bm{\beta}_1 - \bm{\beta}_2) \ne \bm{\theta}
    $$

    即 $\bm{w} \in \bm{W}_1 \cap \bm{W}_2$，故 $\bm{W}_1 \cap \bm{W}_2 \ne \left\lbrace \bm{\theta} \right\rbrace$，矛盾！

    故 $\bm{W}_1 + \bm{W}_2$ 是直和。

!!! note ""
    设 $M$ 是有限维线性空间 $V$ 的子空间，则必然存在 $V$ 另一子空间 $N$ 使得

    $$
    V = M \oplus N
    $$

    即补空间必然存在。

    ---

    证明：

    由于 $M$ 是有限维的，所以可以找到一组基 $\alpha_1, \alpha_2, \cdots, \alpha_m$，将其扩充为 $V$ 的一组基 $\alpha_1, \alpha_2, \cdots, \alpha_m, \alpha_{m+1}, \cdots, \alpha_n$。令 $N$ 为 $V$ 中由 $\alpha_{m+1}, \cdots, \alpha_n$ 张成的子空间，则 $V = M + N$。

    又因为 $M \cap N = \{\theta\}$（$\dim V = \dim M + \dim N$），所以 $V = M \oplus N$。

    同时可知补空间 $N$ 不唯一。

!!! example ""
    设 $W_1$ 为齐次方程组

    $$
    x_1 + x_2 + \cdots + x_n = 0
    $$

    的解空间，$W_2$ 为齐次方程组

    $$
    x_1 = x_2 = \cdots = x_n
    $$

    的解空间，证明

    $$
    \R^n = W_1 \oplus W_2
    $$

    ---

    证明：

    任意 $\alpha = \begin{bmatrix} a_1 \\ a_2 \\ \vdots \\ a_n \end{bmatrix} \in \R^n$，令

    $$
    \bar{\alpha} = \dfrac{1}{n}(a_1 + a_2 + \cdots + a_n)
    $$


    令

    $$
    \beta = \begin{bmatrix} a_1 - \bar{\alpha} \\ a_2 - \bar{\alpha} \\ \vdots \\ a_n - \bar{\alpha} \end{bmatrix},\quad \gamma = \begin{bmatrix} \bar{\alpha} \\ \bar{\alpha} \\ \vdots \\ \bar{\alpha} \end{bmatrix}
    $$

    从而 $\alpha = \beta + \gamma$，且 $\beta \in W_1, \gamma \in W_2$，即 $\R^n = W_1 + W_2$。

    任取 $\eta \in W_1 \cap W_2$，则由 $\eta \in W_2$ 有

    $$
    \eta = \begin{bmatrix} c \\ c \\ \vdots \\ c \end{bmatrix}
    $$

    由 $\eta \in W_1$ 有 $nc = 0$ 得 $c = 0$，即 $\eta = \theta$，所以 $W_1 \cap W_2 = \{\theta\}$，从而 $\R^n = W_1 \oplus W_2$。

!!! note ""
    $W = W_1 \oplus W_2 \oplus \cdots \oplus W_m$ 的充要条件是

    $$
    \dim W = \dim W_1 + \dim W_2 + \cdots + \dim W_m
    $$
