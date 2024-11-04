---
layout: post
title: 随机变量
date: 2024-09-20 11:19:29
updated: 2024-10-27 20:12:31
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 随机变量

### 定义

!!! info ""
    给定概率空间 $(\Omega, \Sigma, \Pr)$，**随机变量**（random variable）是一个*函数* $X\colon \Omega \to \R$，满足

    $$
    \forall x \in \R,\, \left\lbrace \omega \in \Omega \mid X(\omega) \le x \right\rbrace \in \Sigma
    $$
    
    即 $X$ 是 **$\Sigma$-可测**（$\Sigma$-measurable）的。

    一些记号：
    - $X \le x$（其中 $x \in \R$）表示事件族 $\left\lbrace \omega \in \Omega \mid X(\omega) \le x \right\rbrace$，即 $X$ 取值不超过 $x$ 的事件的集合。
    - $X > x$（其中 $x \in \R$）表示事件族 $\left\lbrace \omega \in \Omega \mid X(\omega) > x \right\rbrace$，即 $X$ 取值超过 $x$ 的事件的集合。
    - $X \in S$（其中 $S \subseteq \R$ 是一个由可数个区间 $(y, x]$ 通过交或并构造的集合）表示事件族 $\left\lbrace \omega \in \Omega \mid X(\omega) \in S \right\rbrace$，即 $X$ 取值在 $S$ 中的事件的集合。

    对于离散随机变量，有 $X\colon \Omega \to\Z$，这包含了所有子集 $S \subseteq \Z$。

### 分布（Distribution）

!!! info 累积分布函数（CDF）
    随机变量 $X$ 的**累积分布函数**（cumulative distribution function, CDF），或简称为**分布函数**（distribution function）是一个函数 $F_X\colon \R \to [0, 1]$，定义为

    $$
    F_X(x) = \Pr(X \le x)
    $$

所有关于 $X$ 的概率（all probabilities regarding $X$）都可以从 $F_X$ 中推断（deduce）出来。

!!! info ""
    两个随机变量 $X$ 和 $Y$ 称为**同分布**（identically distributed）的，如果它们有相同的分布函数，即 $F_X = F_Y$。
    
    同分布的随机变量未必是同定义的。

- 单调性（Monotone）：$\forall x, y \in \R,\, x \le y \implies F_X(x) \le F_X(y)$
- 有界性（Bounded）：$\lim\limits_{x \to -\infty} F_X(x) = 0$ 和 $\lim\limits_{x \to \infty} F_X(x) = 1$

### 离散随机变量

!!! info ""
    随机变量 $X$ 是**离散**（discrete）的，如果它的值域 $X(\Omega)$ 是有限或可数的（countable）。

!!! note ""
    对于一个离散随机变量 $X$，它的**概率质量函数**（probability mass function, pmf）是一个函数 $p_X\colon \R \to [0, 1]$，定义为

    $$
    p_X(x) = \Pr(X = x)
    $$

    CDF $F_X$ 满足

    $$
    F_X(y) = \sum_{x \le y} p_X(x)
    $$

### 连续随机变量

先给一个暂时的定义。

!!! info ""
    随机变量 $X$ 是**连续**（continuous）的，如果它的 CDF 可以表示为

    $$
    F_X(y) = \Pr(X \le y) = \int_{-\infty}^y f_X(x) \,dx
    $$
    
    其中可积函数 $f_X\colon \R \to [0, \infty)$ 是 $X$ 的**概率密度函数**（probability density function, pdf），满足

    这里先不考虑是什么积分（黎曼 Riemann 积分抑或是勒贝格 Lebesgue 积分）。

有些随机变量既不是离散的也不是连续的。

### 独立性

!!! info ""
    两个离散随机变量 $X, Y$ 是**独立**（independent）的，如果对于所有 $x, y \in \R$，有 $X = x$ 与 $Y = y$ 是独立的事件。

    离散随机变量 $X_1, \cdots, X_n$ 是 **（相互）独立**，如果对于所有 $x_1, \cdots, x_n \in \R$，有 $X_1 = x_1, \cdots, X_n = x_n$ 是独立的事件。
    $$
    p_{(X_1, \cdots, X_n)}(x_1, \cdots, x_n) = p_{X_1}(x_1) \cdots p_{X_n}(x_n)
    $$

有一种通过 $n$ 个*相互独立*的随机比特（bits）构造 $2^n-1$ 个成对独立的*随机变量*的方法。

假设有 $n$ 个相互独立的随机比特 $X_1, \cdots, X_n$，取值为 $\left\lbrace 0, 1 \right\rbrace$。对任意 $\empty \ne S \subseteq [n]$，定义 $Y_S = \bigoplus\limits_{i \in S} X_i$，其中 $\bigoplus$ 表示异或（XOR）操作。

则对任意 $S_1 \ne S_2$，$Y_{S_1}$ 和 $Y_{S_2}$ 是成对独立的。但对于两个以上的 $Y_S$ 而言，却不一定是独立的。

### 随机向量（Random Vector）

!!! info 随机向量
    给定概率空间 $(\Omega, \Sigma, \Pr)$，一个 $n$-维**随机向量**（random vector）$\bm{X}$ 是一个向量 $(X_1, \cdots, X_n)$，其中 $X_i$ 是一个定义在概率空间 $(\Omega, \Sigma, \Pr)$ 上的随机变量。

!!! info 联合累积分布函数
    **联合累积分布函数**（joint CDF）是函数 $F_{\bm{X}}\colon \R^n \to [0, 1]$，定义为

    $$
    F_{\bm{X}}(x_1, \cdots, x_n) = \Pr(X_1 \le x_1 \cap \cdots \cap X_n \le x_n)
    $$

!!! info 联合质量函数
    对于离散随机向量，**联合质量函数**（joint mass function）是函数 $p_{\bm{X}}\colon \R^n \to [0, 1]$，定义为

    $$
    p_{\bm{X}}(x_1, \cdots, x_n) = \Pr(X_1 = x_1 \cap \cdots \cap X_n = x_n)
    $$

!!! info 边缘分布
    $(X_1, \cdots, X_n)$ 中的 $X_i$ 的**边缘分布**（marginal distribution）定义为

    $$
    p_{X_i}(x_i) = \sum_{x_1, \cdots, x_{i-1}, x_{i+1}, \cdots, x_n} p_{\bm{X}}(x_1, \cdots, x_n)
    $$

## 离散随机变量

### 概率质量函数

!!! info ""
    考虑整数值（integer-valued）离散随机变量 $X\colon \Omega \to\Z$，它的**概率质量函数**（probability mass function, pmf）$p_X\colon \Z \to[0, 1]$ 定义为

    $$
    p_X(k) = \Pr(X = k)
    $$
    
- $p_X$ 代表概率分布的「直方图」（histogram）。
- $p_X$ 可被视为一个向量 $p_X \in [0, 1]^{R}$ 使得 $\left\lVert p_X(x) \right\rVert_1 = 1$，其中 $R = X(\Omega)$ 是 $X$ 的值域。

它的函数 $Y = f(X)$ 也是一个离散随机变量，其中 $\displaystyle p_Y(y)= \sum_{x\colon f(x) = y}p_X(x)$。

### 伯努利试验（Bernoulli Trial）

!!! info ""
    一个**伯努利试验**（Bernoulli trial）是<u>一个只有两个可能结果的随机试验</u>。

    一个**伯努利随机变量**（Bernoulli random variable）$X$ 是一个只能取 $0$ 和 $1$ 两个值的随机变量，满足

    $$
    p_X(k) = \Pr(X = k) = \begin{cases}
        p, & \text{if } k = 1 \\
        1 - p, & \text{if } k = 0
    \end{cases}
    $$

    其中 $p \in [0, 1]$ 是一个参数。

!!! info Indicator
    对于一个事件 $A$，它的 **indicator**（指示）$X$ 是一个随机变量定义为

    $$
    X = I(A) = \begin{cases}
        1, & \text{if } A \text{ occurs} \\
        0, & \text{otherwise}
    \end{cases}
    $$

### 二项分布（Binomial Distribution）

> $n$ 次抛掷硬币，硬币正面朝上的次数。
> Number of HEADs in $n$ coin flips.

!!! info ""
    随机变量 $X$：进行 $n$ 次独立均等分布（independent and identically distributed, **i.i.d.**）的伯努利试验，每次试验成功的概率为 $p$，则 $X$ 表示成功的次数。

    一个**二项随机变量**（binomial random variable）$X$ 是一个随机变量，取值为 $\left\lbrace 0, 1, \dots, n \right\rbrace$，满足

    $$
    p_X(k) = \Pr(X = k) = \binom{n}{k} p^k (1 - p)^{n-k},\quad k = 0, 1, \dots, n
    $$

    我们称 $X$ 服从（follow）参数为 $n, p$ 的**二项分布**（binomial distribution）[^binomial_distribution]，记作

    $$
    X \sim \operatorname{Bin}(n, p) \quad \text{or} \quad X \sim \operatorname{B}(n, p)
    $$

    [^binomial_distribution]: We say that $X$ follows the binomial distribution with parameters $n$ and $p$.

二项分布具有独立性：如果 $X_1 \sim \operatorname{Bin}(n_1, p)$ 和 $X_2 \sim \operatorname{Bin}(n_2, p)$，则 $X_1 + X_2 \sim \operatorname{Bin}(n_1 + n_2, p)$。

<!-- {{{ 证明 -->
<details>
<summary>证明</summary>

$$
\begin{aligned}
    p_{X_1+X_2}(k) &= \sum_{i=0}^{k} p_{X_1}(i) p_{X_2}(k-i)\\
                   &= \sum_{i=0}^{k} \dbinom{n_1}{i} p^{i} (1-p)^{n_1-i} \dbinom{n_2}{k-i} p^{k-i} (1-p)^{n_2-k+i}\\
                   &= \sum_{i=0}^{k} \dbinom{n_1}{i} \dbinom{n_2}{k-i} p^{k} (1-p)^{n_1+n_2-k}\\
                   &= \dbinom{n_1+n_2}{k} p^{k} (1-p)^{n_1+n_2-k}
\end{aligned}
$$

最后一个等号运用了范德蒙德恒等式。

从而 $X_1 + X_2 \sim \operatorname{Bin}(n_1 + n_2, p)$。

</details>
<!-- }}} -->

### 几何分布（Geometric Distribution）

> 第一次出现正面朝上的硬币抛掷次数。
> Number of coin flips to get a HEADs.

!!! info ""
    随机变量 $X$：进行 i.i.d. 的伯努利试验，每次试验成功的概率为 $p$，$X$ 表示第一次成功时进行的试验次数。

    一个**几何随机变量**（geometric random variable）$X$ 是一个随机变量，取值为 $\left\lbrace 1, 2, \dots \right\rbrace$，满足

    $$
    p_X(k) = \Pr(X = k) = (1 - p)^{k-1} p,\quad k = 1, 2, \dots
    $$
    
    我们称 $X$ 服从参数为 $p$ 的**几何分布**（geometric distribution），记作

    $$
    X \sim \operatorname{Geo}(p)\quad \text{or}\quad X \sim \operatorname{Geometric}(p)
    $$

几何随机变量（geometric random variable）$X \sim \operatorname{Geo}(p)$ 是 memoryless（无记忆性）的，即对 $k \ge 1, n\ge 0$ 有

$$
\Pr(X = n + k \mid X > n) = \Pr(X = k)
$$

<!-- {{{ 证明 -->
<details>
<summary>证明</summary>

$$
\begin{aligned}
    \Pr(X = n + k \mid X > n) &= \frac{\Pr(X = n + k \cap X > n)}{\Pr(X > n)} \\ 
    &= \frac{\Pr(X = n + k)}{\Pr(X > n)} \\
    &= \dfrac{(1-p)^{n+k-1}p}{\sum\limits_{k=n}^{\infty}(1-p)^{k}p}\\
    &= \dfrac{(1-p)^{k-1}p}{\sum\limits_{k=0}^{\infty}(1-p)^{k}p}\\
    &= (1-p)^{k-1}p
\end{aligned}
$$

</details>
<!-- }}} -->

几何分布是*唯一*的具有无记忆性的离散概率分布（以 $\left\lbrace 1, 2, \dots \right\rbrace$ 为取值范围）。

<!-- {{{ 证明 -->
<details>
<summary>证明</summary>

考虑一个以 $\N_{+}$ 为取值的随机变量 $X$，其具有无记忆性，即
$$
\Pr(X = m + n \mid X > m) = \Pr(X = n)
$$

由于 $X$ 具有无记忆性，从而有
$$
\begin{aligned}
    \Pr(X = m + n \mid X > m) &= \dfrac{\Pr(X = m + n \cap X > m)}{\Pr(X > m)}\\
                              &= \dfrac{\Pr(X = m + n)}{\Pr(X > m)}\\ 
                              &= \Pr(X = n)
\end{aligned}
$$

于是
$$
\begin{aligned}
    p_X(m + n) &= p_X(n) \Pr(X > m)\\
    &= p_X(n) \left(1 - \sum_{i=1}^m p_X(i)\right)\\
\end{aligned}
$$

设 $p_X(1) = p$，取 $m = 1, n = x$，则有递推
$$
\begin{aligned}
    p_X(x + 1) &= p_X(x) (1 - p_X(1))\\
    &= p_X(x) (1 - p) 
\end{aligned}
$$

可得 $p_X(x) = (1 - p)^{x-1}p$，即 $X$ 服从几何分布。

</details>
<!-- }}} -->

### 独立随机变量之和

!!! note ""
    若离散随机变量 $X, Y$ 相互独立，则

    $$
    \begin{aligned}
        p_{X+Y}(z) &= \Pr(X + Y = z)\\
        &= \sum_{x} \Pr(X = x \cap Y = z - x) \\
        &= \sum_{x} p_X(x) p_Y(z - x) = \sum_{y} p_X(z - y) p_Y(y)
    \end{aligned}
    $$

由此可以定义卷积：

!!! info 卷积
    两个概率质量函数 $p_X, p_Y$ 的**卷积**（convolution）定义为

    $$
    p_{X+Y} = p_X * p_Y
    $$

对于 i.i.d. 伯努利随机变量 $X_1, \dots, X_n \in \left\lbrace 0, 1 \right\rbrace$，有

$$
\begin{aligned}
    p_{X_1 + \cdots + X_n}(k) &= p \cdot p_{X_1+\dots+X_{n-1}}(k-1) + (1-p)p_{X_1+\dots+X_{n-1}}(k) \\ 
    &= \dbinom{n}{k}p^{k}(1-p)^{n-k}
\end{aligned}
$$

### 负二项分布（Negative Binomial Distribution）

> $r$ 次成功后，前面失败的试验次数。
> multiple successes generalization of geometric distribution.

!!! info ""
    随机变量 $X$：进行 i.i.d. 的伯努利试验，每次试验成功的概率为 $p$，$X$ 表示第 $r$ 次成功时前面失败的次数。

    一个**负二项随机变量**（negative binomial random variable）$X$ 是一个随机变量，取值为 $\left\lbrace 0, 1, \dots \right\rbrace$，满足

    $$
    \begin{aligned}
        p_X(k) &= \Pr(X = k)\\
        &= \dbinom{k+r-1}{k}(1-p)^{k}p^r\\
        &= (-1)^{k}\dbinom{-r}{k}(1-p)^{k}p^r
    \end{aligned}
    $$
    
    我们称 $X$ 服从参数为 $r, p$ 的**负二项分布**（negative binomial distribution）。

    另外其中的 $\dbinom{-r}{k}$ 表示 $\dfrac{(-r)(-r-1)\cdots(-r-k+1)}{k!}$。

里面有「二项分布」，只是因为其中的二项式有负号，但其实这是几何分布的推广。

对于 $X_i \sim \operatorname{Geo}(p)$，有
$$
X = (X_1 - 1) + \dots + (X_r - 1)
$$

因为对于 $r$ 次成功中的间隙，都可以视为几何分布。而几何分布包含了成功次数，所以还需要 $-1$。

### 超几何分布（Hypergeometric Distribution）

> 无放回的伯努利试验。
> without replacement variant of binomial distribution.

!!! info ""
    随机变量 $X$：从有限数目（finite population）的 $N$ 个物品中无放回（without replacement）抽取 $n$ 个，其中恰有 $M$ 个目标物品，$X$ 表示 $n$ 次抽取中，抽到目标物品的数量。

    一个**超几何随机变量**（hypergeometric random variable）$X$ 是一个随机变量，取值为 $\left\lbrace 0, 1, \dots, n \right\rbrace$，满足

    $$
    \begin{aligned}
        p_X(k) &= \Pr(X = k)\\
        &= \dfrac{\dbinom{M}{k}\dbinom{N-M}{n-k}}{\dbinom{N}{n}},\quad k = 0, 1, \dots, n
    \end{aligned}
    $$

    我们称 $X$ 服从参数为 $N, M, n$ 的**超几何分布**（hypergeometric distribution），其中 $N \ge 0, 0 \le M \le N, 0 \le n \le N$ 均为整数。

### 多项式分布（Multinomial Distribution）

> multi-dimensional generalization of binomial distribution.

- 有多个结果的试验（trails with multiple outcomes）
    - 有 $n$ 次 i.i.d. 试验，每个都有 $m$ 种可能的结果，第 $i$ 个结果的概率为 $p_i$，令 $X_i$ 为第 $i$ 种结果出现的次数。
- Balls-into-bins 模型：扔 $n$ 个球到 $m$ 个桶中，每个球被独立地扔到桶中，第 $i$ 个桶被选中的概率为 $p_i$，则 $X_i$ 为第 $i$ 个桶中的球的数量。

由定义有 $p_1 + \dots + p_m = 1$。

$(X_1, \dots, X_m)$ 取值为 $(k_1, \dots, k_m) \in \left\lbrace 0, 1, \dots, n \right\rbrace^m$ 使得 $k_1 + \dots + k_m = n$，满足

$$
\begin{aligned}
    p_{(X_1, \dots, X_m)}(k_1, \dots, k_m) &= \Pr\left(\bigcap_{i=1}^m(X_i=k_{i})\right)\\
    &= \dbinom{n}{k_1, \dots, k_m}p_1^{k_1}\cdots p_m^{k_m}\\
    &= \dfrac{n!}{k_1!\cdots k_m!}p_1^{k_1}\cdots p_m^{k_m}
\end{aligned}
$$

则称 $(X_1, \dots, X_m)$ 服从参数为 $m, n, (p_1, \dots, p_m) \in [0, 1]^m$ 并使得 $p_1 + \dots + p_m = 1$ 的**多项式分布**（multinomial distribution）。

$X_i \sim \operatorname{Bin}(n, p_i)$，即 $X_i$ 的边缘分布是二项分布。

### 泊松分布（Poisson Distribution）

#### 定义

二项随机变量 $X$ 取值为 $\left\lbrace 0, 1, \dots, n \right\rbrace$，且有

$$
p_X(k) = \Pr(X = k) = \dbinom{n}{k}p^{k}(1-p)^{n-k}
$$

当数量 $n \to \infty $ 且 $np = \lambda$ 时，有

$$
\begin{aligned}
    p_{\operatorname{Bin}(n, \lambda / n)}(k) &= \dbinom{n}{k} \left( \dfrac{\lambda}{n} \right)^{k} \left( 1 - \dfrac{\lambda}{n} \right)^{n-k}\\
    &= \dfrac{n}{n} \dfrac{n-1}{n} \dots \dfrac{n-k+1}{n} \cdot \dfrac{\lambda^{k}}{k!}\left( 1 - \dfrac{\lambda}{n} \right)^n \left( 1 - \dfrac{\lambda}{n} \right)^{-k}\\
    &\approx \dfrac{\lambda^{k}}{k!}\e^{-\lambda}
\end{aligned}
$$

!!! info ""
    一个**泊松随机变量**（Poisson random variable）$X$ 是一个随机变量，取值为 $\left\lbrace 0, 1, \dots \right\rbrace$，满足

    $$
    p_X(k) = \Pr(X = k) = \e^{-\lambda} \dfrac{\lambda^k}{k!},\quad k = 0, 1, \dots
    $$
    
    我们称 $X$ 服从参数为 $\lambda > 0$ 的**泊松分布**（Poisson distribution），记作

    $$
    X \sim \operatorname{Pois}(\lambda)
    $$

这是一个在 $\left\lbrace 0, 1, \dots \right\rbrace$ 上的 well-defined 的概率分布，即 $\displaystyle \sum_{k=0}^{\infty} \e^{-\lambda} \dfrac{\lambda^k}{k!} = 1$。

#### 泊松变量（Poisson variables）之和

!!! note ""
    若 $X_1, X_2$ 是独立的泊松随机变量，且 $X_1 \sim \operatorname{Pois}(\lambda_1), X_2 \sim \operatorname{Pois}(\lambda_2)$，则 $X_1 + X_2 \sim \operatorname{Pois}(\lambda_1 + \lambda_2)$。

    <!-- {{{ 证明 -->
    <details>
    <summary>证明</summary>
    
    $$
    \begin{aligned}
        p_{X+Y}(k) &= \Pr(X+Y=k)\\
        &= \sum_{i=0}^{k}\Pr(X = i \cap Y = k - i)\\
        &= \sum_{i=0}^{k}p_X(i)p_Y(k-i)\\
        &= \sum_{i=0}^{k}\dfrac{\e^{-\lambda_1}\lambda_1^i}{i!}\dfrac{\e^{-\lambda_2}\lambda_2^{k-i}}{(k-i)!}\\
        &= \dfrac{\e^{-(\lambda_1+\lambda_2)}}{k!}\sum_{i=0}^{k}\dfrac{k!}{i!(k-i)!}\lambda_1^i\lambda_2^{k-i}\\ 
        &= \dfrac{\e^{-(\lambda_1+\lambda_2)}}{k!}(\lambda_1+\lambda_2)^k
    \end{aligned}
    $$
    
    </details>
    <!-- }}} -->

#### 泊松近似（Poisson approximation）

$(X_1, \dots, X_m)$ 服从以 $m, n, p_1 + \dots + p_m = 1$ 为参数的多项式分布。

$(Y_1, \dots, Y_m)$，其中每个 $Y_i \sim \operatorname{Pois}(\lambda_i)$ 相互独立，且 $\lambda_i = np_i$。

!!! note ""
    给定 $\displaystyle \sum_{i=1}^{m}Y_i=n$，有 $(X_1, \dots, X_m)$ 与 $(Y_1, \dots, Y_m)$ 同分布。

    <!-- {{{ 证明 -->
    <details>
    <summary>证明</summary>
    
    注意到 $Y_1 + \dots + Y_m \sim \operatorname{Pois}(n)$，对于任意 $k_1, \dots, k_m \ge 0$ 使得 $k_1 + \dots + k_m = n$，有

    $$
    \begin{aligned}
        p_{\bm{Y}}\left[(k_1, \dots, k_m) \Biggm| \displaystyle \sum_{i=1}^{m}Y_i=n\right] &= \dfrac{\prod\limits_{i=1}^{m} \frac{\e^{-np_i}(np_i)^{k_i}}{k_i!}}{\e^{-n}\frac{n^n}{n!}}\\ 
        &= \dbinom{n}{k_1, \dots, k_m} p_1^{k_1} \dots p_m^{k_m}\\
        &= p_{\bm{X}}[(k_1, \dots, k_m)]
    \end{aligned}
    $$
    
    </details>
    <!-- }}} -->

### Balls into Bins (Random mapping)

将 $n$ 个球均匀随机地（uniformly at random, **u.a.r.**）丢到 $m$ 个桶中。即均匀随机函数 $f\colon [n] \to [m]$。

每个桶接收到的球的个数 $(X_1, \dots, X_m)$ 服从以 $m, n, (\frac{1}{m}, \dots, \frac{1}{m})$ 为参数的多项式分布。

- 生日问题（Birthday problem）
    - the property of being injective (1-1)
- [赠券收集问题（Coupon collector's problem）](https://zh.wikipedia.org/zh-cn/赠券收集问题)
    - the property of being subjective (onto)
- 负载问题（Occupancy (load balancing) problem）
    - the maximum load $\max_i X_i$

### 随机图（Random Graph）

> Erdős–Rényi random graph model

$G \sim G(n, p)$：有 $n$ 个顶点（vertice），对于每个顶点对（pair）$u, v$，进行（conduct）一个 i.i.d. 的以 $p$ 为参数的伯努利试验。如果试验成功，添加一条边（edge）$\{u, v\}$。

$G(n, \frac{1}{2})$ 表示在 $n$ 个顶点上*均匀分布*（uniformly distributed）的随机图。

$G \sim G(n, p)$ 中边的数目服从二项分布 $\operatorname{Bin}\left(\binom{n}{2}, p\right)$，因此 $G(n, p)$ 有时也被称为*二项随机图*。

由 $G \sim G(n, p)$ 定义的随机变量：
- chromatic number $\chi(G)$
- independence number $\alpha(G)$
- clique number $\omega(G)$
- diameter $\operatorname{diam}(G)$
- connectivity
- max-degree $\Delta(G)$
- number of triangles
- number of Hamiltonian cycles
- ...

### 随机树（Random Tree）

> Galton-Watson branching process

对于一个随机变量序列 $X_0, X_1, \dots$，递归（recursively）定义

$$
\left\lbrace\begin{aligned}
    X_0 &= 1\\
    X_{n+1} &= \sum_{j=1}^{X_n} \xi_j^{(n)}
\end{aligned}\right.
$$

其中 $\left\lbrace \xi_{j}^{(n)} \mid n, j \ge 0 \right\rbrace$ 是 i.i.d. 非负整数值（non-negative integer-valued）随机变量（例如泊松随机变量）。

随机家庭树（random family tree）：第 $n$ 代的 $j$ 个家庭成员有 $\xi_{j}^{(n)}$ 个后代。

$X_n$ 代表第 $n$ 代的总人数。
