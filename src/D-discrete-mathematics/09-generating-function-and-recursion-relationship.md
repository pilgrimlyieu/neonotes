---
layout: post
title: 生成函数与递推关系
date: 2024-04-09 09:40:46
updated: 2024-08-30 19:29:28
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 生成函数

!!! memo ""
    这里也是结课后才补充的内容，仅作了解。

### 概念

先从一个简单的例子入手：今有猪肉包、牛肉包、梅菜包、三丁包、豆沙包各一；小明要吃两个，有几种吃法？

答案显然是 $\dbinom{5}{2} = 10$ 种。

但是换种思路，是「$0$ 或 $1$ 个猪肉包」「$0$ 或 $1$ 个牛肉包」……这样，于是就是

$$
\begin{aligned}
    (x^0 + x^1)(x^0 + x^1)\cdots &= (1 + x)^5\\ 
    &= 1 + 5x + \textcolor{FF0099}{10}x^2 + 10x^3 + 5x^4 + x^5
\end{aligned}
$$

这样，$x^2$ 的系数就是答案。

再复杂一点，若猪肉包有两个，没有牛肉包，则有几种吃法？

这会就是

$$
(x^0 + x^1 + x^2)(x^0 + x^1)(x^0 + x^1)(x^0 + x^1) = 1 + 4x + 7x^2 + 7x^3 + 4x^4 + x^5
$$

!!! info ""
    简单来说，**生成函数**（generating function）是一种把无限数列表示成*幂序列的系数*的表示法：
    
    $$
    F(x) = f_0 + f_1 x + f_2 x^2 + \cdots
    $$
    
    使用 $[x^n]F(x)$ 指代这个生成函数中 $x^n$ 的系数 $f_n$。

一些额外说明：
1. 生成函数又叫作「母函数」
2. 这里只讨论所谓「普通（ordinary）」生成函数
3. 不关心函数是否收敛
4. 这里仅做直观介绍

### 生成函数的乘积

令

$$
\left\lbrace\begin{aligned}
    A(x) &= \sum_{n=0}^{\infty} a_n x^n\\ 
    B(x) &= \sum_{n=0}^{\infty} b_n x^n
\end{aligned}\right.
$$

有

$$
[x^n]\left(A(x) \cdot B(x)\right) = \sum_{k=0}^{n} a_k b_{n-k}
$$

这也就是**卷积**（convolution）。

显然还有

$$
\left\lbrace\begin{aligned}
    [x^n]\left(c \cdot F(x)\right) &= c \cdot [x^n]F(x)\\ 
    [x^n]\left(F(\alpha \cdot x)\right) &= \alpha^n \cdot [x^n]F(x)
\end{aligned}\right.
$$

### 卷积规则

!!! info 计数的卷积规则
    令 $A(x)$ 为从集合 $\mathcal{A}$ 中选择对象的计数法所对应的生成函数，$B(x)$ 为从集合 $\mathcal{B}$ 中选择对象的计数法所对应的生成函数，且 $\mathcal{A} \cap \mathcal{B} = \empty$，则 $A(x) \cdot B(x)$ 为从 $\mathcal{A} \cup \mathcal{B}$ 中选择对象的计数法所对应的生成函数。

    更严格地说，这里要求从 $\mathcal{A} \cup \mathcal{B}$ 中选择对象的方法更像是 $\mathcal{A} \times \mathcal{B}$，即一一对应于有序对 $(a, b)$，其中 $a$ 为从集合 $\mathcal{A}$ 中选择对象的方法，$b$ 为从集合 $\mathcal{B}$ 中选择对象的方法。

### 部分分式分解

现在使用 $1, 2, 3, 4$ 代称包子，买包子现在有下面的规则：
1. $1$ 号必须是偶数个
2. $2$ 号必须是 $5$ 的倍数
3. 最多买 $4$ 个 $3$ 号
4. 最多买 $1$ 个 $4$ 号

若总共买 $6$ 个，有以下几种方案

| 方案/包子编号 | $1$ 号 | $2$ 号 | $3$ 号 | $4$ 号 |
|      :-:      |  :-:   |  :-:   |  :-:   |  :-:   |
|       1       |  $6$   |  $0$   |  $0$   |  $0$   |
|       2       |  $4$   |  $0$   |  $2$   |  $0$   |
|       3       |  $4$   |  $0$   |  $1$   |  $1$   |
|       4       |  $2$   |  $0$   |  $4$   |  $0$   |
|       5       |  $2$   |  $0$   |  $3$   |  $1$   |
|       6       |  $0$   |  $5$   |  $1$   |  $0$   |
|       7       |  $0$   |  $5$   |  $0$   |  $1$   |

这里我们可以得到四个生成函数：

$$
\left\lbrace\begin{aligned}
    A_1(x) &= 1 + x^2 + x^4 + \cdots = \frac{1}{1 - x^2}\\ 
    A_2(x) &= x^5 + x^{10} + x^{15} + \cdots = \frac{x^5}{1 - x^5}\\ 
    A_3(x) &= 1 + x + x^2 + x^3 + x^4 = \frac{1 - x^5}{1 - x}\\
    A_4(x) &= 1 + x
\end{aligned}\right.
$$

则

$$
\begin{aligned}
    A(x) &= A_1(x) \cdot A_2(x) \cdot A_3(x) \cdot A_4(x)\\ 
    &= \dfrac{1}{1- x^2} \cdot \dfrac{x^5}{1 - x^5} \cdot \dfrac{1 - x^5}{1 - x} \cdot (1 + x)\\ 
    &= \dfrac{1}{(1-x)^2}\\ 
    &= 1 + 2x + 3x^2 + \cdots + nx^{n-1} + \cdots
\end{aligned}
$$

!!! note 部分分式分解
    设 $p(x)$ 为次数小于 $n$ 的多项式，$a_1, \cdots, a_n$ 为互不相同的非零数，则存在常数 $c_1, \cdots, c_n$ 使得

    $$
    \dfrac{p(x)}{(1 - a_1 x)\cdots(1 - a_n x)} = \dfrac{c_1}{1 - a_1 x} + \cdots + \dfrac{c_n}{1 - a_n x}
    $$

!!! example ""
    求 $[x^n]R(x)$，其中 $R(x) = \dfrac{x}{1 - x - x^2}$。

    <!-- {{{ 解答 -->
    <details>
    <summary>解答</summary>
    
    注意到 $1 - x - x^2 = (1 - a_1 x)(1 - a_2 x)$，容易解得 $a_1 = \dfrac{1 + \sqrt{5}}{2},\, a_2 = \dfrac{1 - \sqrt{5}}{2}$。从而

    $$
    R(x) = \dfrac{c_1}{1 - a_1 x} + \dfrac{c_2}{1 - a_2 x}
    $$
    
    再解得 $c_1 = \dfrac{1}{\sqrt{5}},\, c_2 = -\dfrac{1}{\sqrt{5}}$，从而有

    $$
    R(x) = \dfrac{1}{\sqrt{5}}\left(\dfrac{1}{1 - a_1 x} - \dfrac{1}{1 - a_2 x}\right)
    $$
    
    又

    $$
    \begin{aligned}
        \dfrac{1}{1 - a_1 x} &= 1 + a_1 x + a_1^2 x^2 + \cdots\\
        \dfrac{1}{1 - a_2 x} &= 1 + a_2 x + a_2^2 x^2 + \cdots
    \end{aligned}
    $$
    
    则有

    $$
    \begin{aligned}
        [x^n]R(x) &= \dfrac{a_1^n - a_2^n}{\sqrt{5}}\\ 
        &= \dfrac{1}{\sqrt{5}}\left( \left(\dfrac{1 + \sqrt{5}}{2}\right)^n - \left(\dfrac{1 - \sqrt{5}}{2}\right)^n \right)
    \end{aligned}
    $$
    
    </details>
    <!-- }}} -->


!!! note 部分分式分解
    分母多项式若有非零 $m$ 重根，则可将整个商式表示为形如 $\dfrac{c}{(1 - ax)^{k}}$ 的项的和的形式，其中 $k \le m$。

    $$
    [x^n]\dfrac{c}{(1 - ax)^k} = c a^n \dbinom{n + (k - 1)}{n}
    $$
    
    这是由 $[x^n]\dfrac{1}{(1-x)^{k}} = \dbinom{n + (k - 1)}{n}$ 推出的。

### 常用生成函数

| $G(x)$ | $a_{k}$ | 展开式
| :-:   |   :-:   | :-: |
| $(1 + x)^n$ | $\dbinom{n}{k}$ | $1 + \dbinom{n}{1}x + \dbinom{n}{2}x^2 + \cdots + x^n$ |
| $(1 + ax)^n$ | $\dbinom{n}{k}a^k$ | $1 + \dbinom{n}{1}ax + \dbinom{n}{2}a^2x^2 + \cdots + a^nx^n$ |
| $(1 + x^r)^n$ | $\left\lbrace\begin{aligned} &\dbinom{n}{\frac{k}{r}}, &\text{if } r \mid k\\ &0, &\text{otherwise} \end{aligned}\right.$ | $1 + \dbinom{n}{r}x^r + \dbinom{n}{2r}x^{2r} + \cdots + x^{nr}$ |
| $\dfrac{1 - x^{n+1}}{1 - x}$ | $\left\lbrace\begin{aligned} &1, &\text{if } k \le n\\ &0, &\text{otherwise} \end{aligned}\right.$ | $1 + x + x^2 + \cdots + x^n$ |
| $\dfrac{1}{1 - x}$ | $1$ | $1 + x + x^2 + \cdots$ |
| $\dfrac{1}{1 - ax}$ | $a^k$ | $1 + ax + a^2x^2 + \cdots$ |
| $\dfrac{1}{1 - x^r}$ | $\left\lbrace\begin{aligned} &1, &\text{if } r \mid k\\ &0, &\text{otherwise} \end{aligned}\right.$ | $1 + x^r + x^{2r} + \cdots$ |
| $\dfrac{1}{(1 - x)^2}$ | $k + 1$ | $1 + 2x + 3x^2 + \cdots$ |
| $\dfrac{1}{(1 - x)^n}$ | $\dbinom{n + k - 1}{k}$ | $1 + \dbinom{n}{1}x + \dbinom{n + 1}{2}x^2 + \cdots$ |
| $\dfrac{1}{(1 + x)^n}$ | $\dbinom{n + k - 1}{k}(-1)^k$ | $1 - \dbinom{n}{1}x + \dbinom{n + 1}{2}x^2 - \cdots$ |
| $\dfrac{1}{(1 - ax)^n}$ | $\dbinom{n + k - 1}{k}a^k$ | $1 + \dbinom{n}{1}ax + \dbinom{n + 1}{2}a^2x^2 + \cdots$ |
| $\e^x$ | $\dfrac{1}{k!}$ | $1 + \dfrac{1}{1!}x + \dfrac{1}{2!}x^2 + \cdots$ |
| $\ln(1 + x)$ | $\dfrac{(-1)^{k-1}}{k}$ | $x - \dfrac{1}{2}x^2 + \dfrac{1}{3}x^3 - \cdots$ |

### 实例

斐波那契数列有

$$
\left\lbrace\begin{aligned}
    f_0 &= 0,\\ 
    f_1 &= 1,\\ 
    f_{n+2} &= f_{n+1} + f_n
\end{aligned}\right.
$$

生成函数

$$
F(x) = f_0 + f_1x + f_2x^2 + \cdots + f_nx^n + \cdots
$$

则有

$$
\begin{aligned}
    (1 - x - x^2)F(x) &= f_0 + (f_1 - f_0)x + (f_2 - f_1 - f_0)x^2 + (f_3 - f_2 - f_1)x^3 + \cdots\\
    &= (f_1 - f_0) x\\ 
    &= x
\end{aligned}
$$

得 $F(x) = \dfrac{x}{1 - x - x^2}$。

## 递推关系

### 第二类斯特林数

第二类斯特林数：$n$ 个元素的集合分成 $k$ 个*非空子集*的方法数。记作 $S(n, k)$ 或 $\displaystyle {n \brace k}$。

则有

$$
\begin{cases}
    S(0, 0) = 1,\\
    S(n, 0) = S(0, n) = 0, &n > 0\\
    S(n + 1, k) = k \cdot S(n, k) + S(n, k - 1), &k > 0
\end{cases}
$$

!!! note ""
    递推怎么得出来的呢？

    考虑第 $n + 1$ 个元素，它可以在这 $k$ 个集合中任选一个加入，而前 $k$ 种集合划分 $n$ 个元素方法有 $S(n, k)$ 种，从而这种情况有 $k \cdot S(n, k)$ 种；当然，第 $n + 1$ 个元素也可以「自成一派」，这时候前 $n$ 个元素就只有 $k - 1$ 个非空子集可供选择了，此时就只有 $S(n, k - 1)$ 种，加法原理有 $S(n + 1, k) = k \cdot S(n, k) + S(n, k - 1)$ 种。

利用容斥原理求第二类斯特林数 $S(n, k)$：

记 $\mathcal{N} = \bigl\lbrace f \text{ 为满射} \mid f\colon \left\lbrace 1, \cdots, n \right\rbrace \to \left\lbrace 1, \cdots, k \right\rbrace  \bigr\rbrace$，从而有 $|\mathcal{N}| = k! \cdot S(n, k)$（因为 $\mathcal{N}$ 指定了 $k$ 个非空子集的顺序）。

令 $\mathcal{X} = \bigl\lbrace f \mid f\colon \left\lbrace 1, \cdots, n \right\rbrace \to \left\lbrace 1, \cdots, k \right\rbrace  \bigr\rbrace,\, \mathcal{X}_{j} = \bigl\lbrace f \in \mathcal{X} \mid f \text{ 值域不包括 }j \bigr\rbrace$，则有 $|\mathcal{X}| = k^n,\, |\mathcal{X}_{j}| = (k-1)^n$，从而有

$$
\begin{aligned}
    |\mathcal{N}| &= \left\lvert \bigcap_{j=1}^n \bar{\mathcal{X}}_{j} \right\rvert\\ 
    &= \left\lvert \mathcal{X} - \bigcup_{j=1}^n \mathcal{X}_{j}\right\rvert\\ 
    &= k^n - \left( \sum_{j=1}^{k}(-1)^{j+1}\dbinom{k}{j}(k - j)^n \right)\\ 
    &= \sum_{j=0}^{k}(-1)^j\dbinom{k}{j}(k - j)^n
\end{aligned}
$$

即

$$
S(n, k) = \frac{1}{k!} \sum_{j=0}^{k}(-1)^j\dbinom{k}{j}(k - j)^n
$$

### 物体分配到盒子里的方法计数

1. $n$ 个不同物体分配到 $k$ 个不同的盒子中，使第 $i$ 个盒子包含 $n_i$ 个物体（$i = 1, \cdots, k$）
    - $\dbinom{n}{n_1, \cdots, n_k}$
2. $n$ 个不同物体分配到 $k$ 个相同的盒子中，不允许空盒
    - 第二类斯特林数 $S(n, k)$
3. $n$ 个相同物体分配到 $k$ 个不同的盒子中
    - $\dbinom{n + k - 1}{n}$
4. $n$ 个相同物体分配到 $k$ 个相同的盒子中，不允许空盒
    - 无简单解析式

### 鸽笼原理

!!! note 鸽笼原理
    若要将 $n$ 只鸽子放到 $m$ 个笼子中，且 $m<n$，则至少有一个笼子要装 $2$ 个或更多的鸽子。

    ---
    
    若 $|A| > |B|$，则不存在从 $A$ 到 $B$ 的单射。

!!! note 鸽笼原理的推广
    若要将 $n$ 个物体放到 $m$ 个盒子中，且 $m<n$，则至少有一个笼子需容纳 $\left\lceil \dfrac{n}{m}\right\rceil$ 个或更多物体。

    ---

    换言之，若 $|A| > k \cdot|B|$，对于任何一个 $f\colon A \to B$，它把至少 $k+1$ 个 $A$ 中的不同元素映射到 $B$ 中的同一个元素。

### 拉姆齐数（Ramsey number）

拉姆齐数（Ramsey number）$R(k, l) = n$ 是最小的 $n$ 使 $n$ 个人中至少有 $k$ 个人互相认识或至少有 $l$ 个人互相不认识。
