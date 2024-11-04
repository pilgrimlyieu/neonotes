---
layout: post
title: 基本计数技术
date: 2024-04-02 10:03:50
updated: 2024-06-13 14:16:36
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 排列、组合与多项式系数

### 计数基本原则

- 乘法原则
- 加法原则

### 排列组合

**排列**（Permutation）：从 $n$ 个元素中取出 $k$ 个元素，按照一定的顺序排成一列，称为 $n$ 个元素中取出 $k$ 个元素的排列数，记作 $A(n, k)$ 或 $P(n, k)$。有

$$
A(n, k) = P(n, k) = \dfrac{n!}{(n-k)!}
$$

**组合**（Combination）：从 $n$ 个元素中取出 $k$ 个元素，不考虑顺序，称为 $n$ 个元素中取出 $k$ 个元素的组合数，记作 $C(n, k)$ 或 $\dbinom{n}{k}$。有

$$
C(n, k) = \dbinom{n}{k} = \dfrac{P(n, k)}{P(k, k)} = \dfrac{n!}{k!(n-k)!}
$$

#### 圆排列

从 $n$ 个不同元素中，取 $r$ 个不重复的元素排成一个圆圈，有 $P(n, r) / r$ 种排列方法。

#### 有相同物体的排列

在 $n$ 个有相同项的对象集中，得到不同的 $n$-排列个数是：令 $m_i$ 是第 $i$ 个重复项的重复次数

$$
\dfrac{P(n, n)}{\prod m_i!}
$$

#### $n$ 个元素集合中允许重复的 $r$-组合

有 $\dbinom{n+r-1}{r}$ 种组合方法。

!!! note ""
    相当于用 $n - 1$ 个隔板分割 $r$ 个物体，将隔板与物体视为一种东西，每种东西占据一个空间的位置，从而有 $n + r - 1$ 个位置，在其中选择 $r$ 个位置放物体，即为 $\dbinom{n+r-1}{r}$ 种。

即

|   类型   | 允许重复？ |                       公式                       |
|   :--:   | :--------: |                       :--:                       |
| $r$-排列 |   不允许   |          $P(n, r) = \dfrac{n!}{(n-r)!}$          |
| $r$-组合 |   不允许   |      $\dbinom{n}{r} = \dfrac{n!}{r!(n-r)!}$      |
| $r$-排列 |    允许    |                      $n^r$                       |
| $r$-组合 |    允许    | $\dbinom{n+r-1}{r} = \dfrac{(n+r-1)!}{r!(n-1)!}$ |

### 多项式系数

二项式系数：

$$
(a + b)^n = \sum_{k=0}^{n} \dbinom{n}{k} a^{n-k} b^k
$$

杨辉三角：

$$
\dbinom{n+1}{k} = \dbinom{n}{k-1} + \dbinom{n}{k}
$$

范德蒙德恒等式（Vandermonde's Identity）：

$$
\dbinom{m+n}{r} = \sum_{k=0}^{r} \dbinom{m}{k} \dbinom{n}{r-k}
$$

多项式系数

$$
\left(\sum_{i=1}^{m} a_i\right)^n = \sum_{\sum_{i=1}^m k_i = n} \dbinom{n}{k_1, k_2, \cdots, k_m} \prod_{i=1}^{m} a_i^{k_i}
$$

其中

$$
\dbinom{n}{k_1, k_2, \cdots, k_m} = \dfrac{n!}{k_1! k_2! \cdots k_m!}
$$

考虑从 $\displaystyle \sum_{i=1}^{m}k_i = n$ 中选择 $k_i$ 个 $a_i$，有

$$
\begin{aligned}
    \dbinom{n}{k_1} \dbinom{n-k_1}{k_2} \cdots \dbinom{n-k_1- \cdots - k_{m-1}}{k_m} & = \dfrac{n!}{k_1! \bcancel{(n-k_1)!}} \dfrac{\bcancel{(n-k_1)!}}{k_2! \bcancel{(n-k_1-k_2)!}} \cdots \dfrac{\bcancel{(n-k_1-\cdots-k_{m-1})!}}{k_m! (n-k_1-\cdots-k_{m-1}-k_m)!} \\
    &= \dfrac{n!}{k_1! k_2! \cdots k_m!}
\end{aligned}
$$

## 集合分类计数与容斥原理

### 容斥原理

容斥原理（Principle of Inclusion-Exclusion）：对于有限集合 $A_1, A_2, \cdots, A_n$，有

$$
\begin{aligned}
    \left\lvert \bigcup_{i=1}^n A_i \right\rvert &= \sum_{k=1}^{n}(-1)^{k-1}S_k\qquad \text{其中 } S_k = \sum_{1 \leq i_1 < \cdots < i_k \leq n} \left\lvert\bigcap_{j=1}^{k} A_{i_j}\right\rvert\\
    &= \sum_{k=1}^{n}(-1)^{k-1} \sum_{1 \leq i_1 < \cdots < i_k \leq n} \left\lvert\bigcap_{j=1}^{k} A_{i_j}\right\rvert
\end{aligned}
$$

### 错排问题

错排问题：$n$ 个元素的错排问题是指 $n$ 个元素的排列中，没有一个元素在自己的位置上的排列个数。

对 $n$ 个帽子重排列，新序号为 $i_{j}$，令满足 $i_{j} = j$ 的排列的集合为 $A_{j}$，从而容斥原理有

$$
\begin{aligned}
    \left\lvert\bigcap_{j=1}^{n} \bar{A}_{j}\right\rvert &= N - \left\lvert \bigcup_{j=1}^n A_{j} \right\rvert\\ 
    &= N + \sum_{j=1}^{n}(-1)^{j} S_{j}
\end{aligned}
$$

其中 $N = n!$。保留 $j$ 项不变，其它 $n - j$ 可任意排列，有

$$
S_j = \dbinom{n}{j} (n - j)! = \frac{n!}{j!}
$$

代入得

$$
\begin{aligned}
    \left\lvert\bigcap_{j=1}^{n} \bar{A}_{j}\right\rvert &= n! + \sum_{j=1}^{n}(-1)^{j} \frac{n!}{j!}\\
    &= n! \sum_{j=0}^{n} \frac{(-1)^{j}}{j!}
\end{aligned}
$$

从而概率为 $p = \displaystyle \sum_{j=0}^{n} \dfrac{(-1)^{j}}{j!} \to \e^{-1} \approx 0.36788$。
