---
layout: post
title: 自然数与数论初步
date: 2024-03-21 10:21:47
updated: 2024-06-11 10:00:19
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 自然数

### 皮亚诺公理（Peano axioms for natural numbers）

1. $0$ 是自然数。
2. 每个自然数 $x$ 都有一个自然数后继 $S(x)$。
3. $0$ 不是任何自然数的后继。
4. 不同的自然数有不同的后继（即 $S(x) = S(y) \to x = y$）。
5. 如果一个集合 $A$ 包含 $0$，并且对于每个 $x \in S$，$S(x) \in A$，那么 $A$ 包含所有自然数。

形式化写法：
1. $0 \in \N$ 
2. $x \in \N \to S(x) \in \N$
3. $x \in \N \to S(x) \ne 0$ 
4. $x \in \N \land y \in \N \land S(x) = S(y) \to x = y$ 
5. $0 \in M \land \forall x(x \in \to S(x) \in M) \to \N \subseteq M \text{ for any property } M$ 

由皮亚诺公理可知，自然数 $\N$ 集合只取决于 $0$ 与 $S$。从集合和集合运算出发，构造一个结构 $\left\langle 0, \N, S \right\rangle$ 满足皮亚诺公理。

### 冯·诺伊曼构造（von Neumann construction）

- $0 = \empty$
- $S(x) = x \cup \left\lbrace x \right\rbrace$ 

有意思的是，$\operatorname{card} N = n$（$N$ 代表冯·诺依曼构造下 $n$ 的表示，意会即可）。同时也有 $N = \left\lbrace 0, 1, \cdots, n - 1 \right\rbrace$。

设 $a$ 为集合，称 $a \cup \left\lbrace a \right\rbrace$ 为 $a$ 的后继。记为 $S(a)$ 或 $a^{+}$。

设 $A$ 是集合，若 $A$ 满足下列条件，则称 $A$ 是**归纳集**：
- $\empty \in A$ 
- $\forall a (a \in A \to S(a) \in A)$ 

从而定义自然数集合 $\N$ 为<u>所有归纳集的*交集*</u>，即

$$
\N = \left\lbrace \empty, \left\lbrace \empty \right\rbrace, \left\lbrace \empty, \left\lbrace \empty \right\rbrace \right\rbrace, \cdots \right\rbrace
$$

也就可以定义**加法**：对任意自然数 $m,\, n$
- $m + 0 = m$
- $m + S(n) = S(m + n)$

!!! note 结合律的证明
    即证

    $$
    (a + b) + c = a + (b + c)
    $$
    
    先证引理

    $$
    0 + a = a
    $$
    
    对 $a$ 归纳，已知 $0 + 0 = 0$，设 $0 + k = k$ 成立，从而有

    $$
    \begin{aligned}
        0 + S(k) &= S(0 + k) \\ 
        &= S(k)
    \end{aligned}
    $$
    
    得证。

    则 $c = 0$ 时有

    $$
    \begin{aligned}
        (a + b) + 0 &= a + b\\ 
        a + (b + 0) &= a + b
    \end{aligned}
    $$
    
    即有 $(a + b) + c = a + (b + c)$ 在 $c = 0$ 时成立。

    再对 $c$ 归纳，设 $(a + b) + k = a + (b + k)$ 成立，从而有

    $$
    \begin{aligned}
        S\bigl((a + b) + k\bigr) &= S\bigl(a + (b + k)\bigr)\\
        (a + b) + S(k) &= a + S(b + k)\\ 
        (a + b) + S(k) &= a + \bigl(b + S(k)\bigr)
    \end{aligned}
    $$
    
    得证。

!!! note 交换律的证明
    即证

    $$
    a + b = b + a
    $$
    
    先证引理

    $$
    S(a) + b = S(a + b)
    $$
    
    $b = 0$ 时有 $S(a) + 0 = S(a),\, S(a + 0) = S(a)$，即 $S(a) + b = S(a + b)$ 在 $b = 0$ 时成立。

    对 $b$ 归纳，设 $S(a) + k = S(a + k)$ 成立，从而有

    $$
    \begin{aligned}
        S(a) + S(k) &= S\bigl(S(a) + k\bigr)\\
        &= S\bigl(S(a + k)\bigr)\\
        &= S\bigl(a + S(k)\bigr)
    \end{aligned}
    $$
    
    得证。

    从而对 $a$ 归纳，显然有 $0 + b = b = b + 0$，设 $a + b = b + a$ 成立，从而有

    $$
    \begin{aligned}
        S(a) + b &= S(a + b)\\
        &= S(b + a)\\
        &= b + S(a)
    \end{aligned}
    $$
    
    得证。

**乘法**：对任意自然数 $m,\, n$
- $m \times 0 = 0$ 
- $m \times S(n) = m + (m \times n)$

## 数论初步

### 整除

设 $a,\, b$ 为整数（$a\ne 0$），若存在整数 $c$ 使得 $b = ac$，则称 **$a$ 整除 $b$**（或 **$b$ 能被 $a$ 整除**），记作 $a \mid b$。

设 $a,\, b,\, c$ 是整数，$a \ne 0$，则
- 若 $a \mid b$，则 $a \mid bc$
- 若 $a \mid b$ 且 $b \mid c$，则 $a \mid c$
- 若 $a \mid b$ 且 $a \mid c$，则 $a \mid (b + c)$
    - 推广：若 $a \mid b$ 且 $a \mid c$，则 $a \mid (mb + nc)$，其中 $m,\, n$ 为任意整数

### 整数除法

令 $a$ 为整数，$d$ 为正整数，则存在唯一的整数 $q$ 和 $r$，且 $0 \le r<d$，满足 $a=d q+r$。记作 $q = a \operatorname{div} d,\, r = a \bmod d$
- $d$ 为**除数**
- $a$ 为**被除数**
- $q$ 为**商**
- $r$ 为**余数**

### 同余

设 $a$ 和 $b$ 为整数，$m$ 为正整数，若 $m \mid(b-a)$，则称 $a$ 与 $b$ 模 $m$ 同余，记作 $a \equiv b \pmod m$。

性质：
- $a \equiv b \pmod m \iff a \bmod m = b \bmod m$
- $a \equiv b \pmod m \iff \exists k \in \Z (a = b + km)$ 

同余算数：在模 $m$ 同余意义下，算数限制在了 $\Z_m = \left\lbrace 0, \cdots, m - 1 \right\rbrace$ 范围内。
- 模 $m$ 加：$a +_m b = (a + b) \bmod m$
- 模 $m$ 乘：$a \times_m b = (a \times b) \bmod m$

设 $a \equiv b \pmod n,\, a_1 \equiv b_1 \pmod n,\, a_2 \equiv b_2 \pmod n$，$k$ 为非负整数，则有：
- $a + k \equiv b + k \pmod n$
- $k a \equiv k b \pmod n$
- $a_1 + a_2 \equiv b_1 + b_2 \pmod n$
- $a_1 a_2 \equiv b_1 b_2 \pmod n$
- $ a^k \equiv b^k \pmod n$
- $p(a) \equiv p(b) \pmod n$，其中 $p(x)$ 为任意整系数多项式

需要注意的是，$k^a \equiv k^b \pmod n$ 未必成立。

### 素数

设 $p$ 为正整数，若 $p > 1$ 且 $p$ 的因数只有 $1$ 和 $p$ 两个，则称 $p$ 为**素数**（Prime）。

**算术基本定理**：任何一个大于 $1$ 的自然数 $n$ 可以唯一写成有限个素数的乘积。即形如

$$
n = p_1^{k_1} p_2^{k_2} \cdots p_s^{k_s}
$$

### 最大公约数

能整除两个整数（不全为 $0$）的最大整数称为这两个整数的**最大公约数**（Greatest Common Divisor），记作 $\gcd(a, b)$。即 $\gcd(a, b) = \max\bigl\lbrace d \in \Z^{+} \bigm| (d \mid a) \land (d \mid b) \bigr\rbrace\quad (a \ne 0 \lor b \ne 0)$。

即 $a,\, b$ 互素 $\iff \gcd(a, b) = 1$。

**辗转相除法**：设 $a,\, b$ 为整数（不全为 $0$），则有 $\gcd(a, b) = \gcd(b, a \bmod b)$。

```
function gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a mod b)
```

### 裴蜀定理

$\gcd(a, b)$ 一定可以表示为 $a,\, b$ 的线性组合。即

$$
\forall a, b \in \Z^{+},\, \exists s, t \in \Z,\, \gcd(a, b) = sa + tb
$$

换言之，$ax + by = c$ 有整数解当且仅当 $\gcd(a, b) \mid c$。

---

证明：

令 $x$ 为可写作 $sa + tb$ 的<u>最小正整数</u>，从而任意 $a,\, b$ 的公约数 $c$ 整除 $x$，即 $c \le x$。

令 $q = a \operatorname{div} x,\, r = a \bmod x$，则

$$
\begin{aligned}
    r &= a - qx\\ 
    &= a - q(sa + tb)\\
    &= (1 - qs)a - (qt)b
\end{aligned}
$$

即 $r$ 也能写成 $a,\, b$ 的线性组合，且 $r < x$，因此 $r$ 只能为 $0$（否则由于 $r < x$，$r$ 才是可以写成 $sa + tb$ 的最小正整数）。

所以 $x$ 为 $a,\, b$ 的公约数，又因为 $x$ 是所有公约数中的倍数，所以 $x = \gcd(a, b)$。

### 同余方程

方程 $a x \equiv b \pmod m$ 称为**线性同余方程**，其中 $a,\, b,\, m$ 为整数，且 $m > 0$。

线性同余方程未必有解。只需研究 $a x \equiv 1 \pmod m$ 的可解性即可，解称为 **$a$ 模 $m$ 的逆**，记作 $a^{-1}$。

当 $a,\, m$ 互素，且 $m > 1$ 时，$a$ 模 $m$ 的逆一定存在。由裴蜀定理，存在 $s,\, t$ 使得 $sa + tm = 1$，两边同时模 $m$，得到 $sa \equiv 1 \pmod m$。

### 中国剩余定理

设正整数 $m_1, m_2, \cdots, m_n$ 两两互素，则一元线性同余方程组

$$
\left\lbrace\begin{aligned}
    x &\equiv a_1 \pmod {m_1}\\
    x &\equiv a_2 \pmod {m_2}\\
    \vdots\\ 
    x &\equiv a_n \pmod {m_n}
\end{aligned}\right.
$$

有解，且在模 $M$ 同余下唯一，这里

$$
M = \prod_{i=1}^{n} m_i
$$

令 $M_i = \dfrac{M}{m_i}$，考虑 $t_i = M_i^{-1}$，即 $t_i M_i \equiv 1 \pmod{m_i}$，方程组解为

$$
\begin{aligned}
    x &= a_1 t_1 M_1 + a_2 t_2 M_2 + \cdots + a_n t_n M_n + kM\\
    &= \sum_{i=1}^{n} a_i t_i M_i + k M
\end{aligned}
$$

因为有

$$
\begin{aligned}
    x & \equiv a_i t_i M_i \pmod {m_i}\\
    & \equiv a_i (t_i M_i) \pmod {m_i}\\
    & \equiv a_i \pmod {m_i}
\end{aligned}
$$

唯一性需要注意到任意两个解的差值一定是 $M$ 的倍数。

### 费马小定理

若 $p$ 为素数，则

$$
a^{p} \equiv a \pmod p
$$

特别地，若 $a$ 与 $p$ 互素，则

$$
a^{p-1} \equiv 1 \pmod p
$$

我们熟知二项式系数

$$
\binom{n}{m} = \dfrac{n!}{m!(n-m)!}
$$

推广有多项式系数

$$
\binom{n}{m_1, m_2, \cdots, m_k} = \dfrac{n!}{m_1!m_2!\cdots m_k!}
$$

其中 $m_1 + m_2 + \cdots + m_k = n$。

因此有

$$
\begin{aligned}
    a^p &= \left(\sum_{i=1}^a 1\right)^p\\
    &= \sum_{m_1 + m_2 + \cdots + m_a = p} \dfrac{p!}{m_1!m_2!\cdots m_a!}
\end{aligned}
$$

考虑 $\dfrac{p!}{m_1!m_2!\cdots m_a!}$，若其中没有 $m_i = p$，则 $\dfrac{p!}{m_1!m_2!\cdots m_a!} \equiv 0 \pmod p$。

若有 $m_i = p$，则 $\dfrac{p!}{m_1!m_2!\cdots m_a!} \equiv 1 \pmod p$，此时 $m_j = 0\quad (j \ne i)$。共有 $a$ 种情况，因此

$$
a^p \equiv a \pmod p
$$

### 欧拉定理

费马小定理是欧拉定理的特例。

若正整数 $a,\, n$ 互素，则

$$
a^{\varphi(n)} \equiv 1 \pmod n
$$

其中 $\varphi(n)$ 为 Euler's totient，是不大于 $n$ 且与 $n$ 互素的正整数个数。

设 $n = p_1^{\alpha_1} p_2^{\alpha_2} \cdots p_k^{\alpha_k}$，则

$$
\varphi(n) = n \prod_{i=1}^{k} \left(1 - \dfrac{1}{p_i}\right)
$$

因为容易发现，若 $m,\, n$ 互素，则 $\varphi(mn) = \varphi(m) \varphi(n)$。

同时有 $\varphi(p^{\alpha}) = p^{\alpha}\left(1 - \dfrac{1}{p}\right)$，因为与 $p^{\alpha}$ 不互素的数肯定是 $p$ 的倍数，而 $p^{\alpha}$ 中有 $\dfrac{1}{p} p^{\alpha}$ 个数是 $p$ 的倍数。

从而有

$$
\begin{aligned}
    \varphi(n) &= \prod_{i=1}^{k} \varphi\left(p_i^{\alpha_i}\right)\\
    &= \prod_{i=1}^{k} p_i^{\alpha_i} \left(1 - \dfrac{1}{p_i}\right)\\
    &= n \prod_{i=1}^{k} \left(1 - \dfrac{1}{p_i}\right)\\ 
\end{aligned}
$$

也可以写成

$$
\varphi(n) = n \prod_{p \mid n} \left(1 - \dfrac{1}{p}\right)
$$

!!! memo ""
    新手村两节课速通数论……
