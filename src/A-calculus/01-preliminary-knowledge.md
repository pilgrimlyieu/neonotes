---
layout: post
title: 预备知识
date: 2023-09-12 13:37:22
updated: 2024-04-30 17:51:15
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 第 1 章 极限与连续性

### 1.1 预备知识

##### 一、常用集合

$\N$：从 $1$ 开始的自然数集合（即**正整数集合**）

$\N_0$：从 $0$ 开始的自然数集合（即**自然数集合**）

##### 二、逻辑符号介绍

$\exist !$：<u>存在且唯一</u>。

$\square$：<u>证明或解答完毕</u>。

#### 1.1.1 集合

补集的四种写法：

1. 标准写法：$\complement_UA$
2. 教材写法：$C_UA$
3. 老师写法（省略全集）：$A^C$
4. 个人写法（省略全集）：$\bar{A}$

#### 1.1.2 数学归纳法·不等式·极坐标系·复数

##### 一、数学归纳法

**第一数学归纳法**

1. 证明 $n=1$ 时命题 $P(1)$ 成立
2. 假设 $n\ge 2$ 时，命题 $P(n-1)$ 成立，由此推得 $P(n)$ 成立

则命题 $P(n)$ 对所有 $n \in \N$ 成立。

**第二数学归纳法**

1. 证明 $n=1$ 时命题 $P(1)$ 成立
2. 假设 $n\ge 2$ 时，命题 $P(1),\, \dots ,\,P(n-1)$ 成立，由此推得 $P(n)$ 成立

则命题 $P(n)$ 对所有 $n \in \N$ 成立。

##### 二、不等式

1. **三角不等式**

$$
\bigl\lvert |a|-|b|\bigr\rvert \le |a\pm b|\le |a|+|b|
$$

2. **Bernoulli 不等式**

$a_i>-1$ 且符号相同。

$$
\prod_{i=1}^{n}(1+a_i)\ge 1+\sum_{i=1}^{n}a_i
$$

证明：

使用第一数学归纳法证明。

$n=1$ 时显然成立。下证 $n-1$ 时命题成立能推出 $n$ 时命题成立。

$$
\begin{aligned}
\prod_{i=1}^{n}(1+a_i)&=(1+a_n)\prod_{i=1}^{n-1}(1+a_i)\\
&\ge (1+a_n)\left(1+\sum_{i=1}^{n-1}a_i\right)\\
&=1+\sum_{i=1}^{n}a_i+a_n \sum_{i=1}^{n-1}a_i\\
&\ge 1+\sum_{i=1}^{n}a_i
\end{aligned}
$$

$$
\tag*{$\square$}
$$

由此得对任意 $n \in\N$，有不等式成立。取等条件为 $n=1$ 或 $a_1=\dots=a_n=0$。

3. **Minkowski 不等式**

$$
\sqrt{\sum_{i=1}^{n}(a_i+b_i)^{2}}\le \sqrt{\sum_{i=1}^{n}a_i^2}+\sqrt{\sum_{i=1}^{n}b_i^2}
$$

证明：

即证

$$
\sum_{i=1}^{n}(a_i+b_i)^2\le \sum_{i=1}^{n}a_i^2+\sum_{i=1}^{n}b_i^2+2 \sqrt{\sum_{i=1}^{n}a_i^2 \sum_{i=1}^{n}b_i^2}
$$

即证

$$
\sum_{i=1}^{n}a_ib_i\le \sqrt{\sum_{i=1}^{n}a_i^2 \sum_{i=1}^{n}b_i^2}
$$

$$
\tag*{$\square$}
$$

由 **Cauchy-Schwarz 不等式**立得证。

#### 1.1.3 区间·邻域·数集的界

设 $\delta>0$，则称 $(x_0-\delta,\,x_0+\delta)$ 为 **$x_0$ 的 $\delta$ 邻域**，简称 **$x_0$ 的邻域**，记为 $N_{\delta}(x_0)$。

称 $N_{\delta}(x_0)\backslash \lbrace x_0 \rbrace$ 为 **$x_0$ 的 $\delta$ 去心邻域**，简称 **$x_0$ 的去心邻域**，记为 $\mathring{N}_{\delta}(x_0)$。

称 $(x_0,\,x_0+\delta)$ 为 **$x_0$ 的右邻域**，记为 $N_{\delta}^{+}(x_0)$；$(x_0-\delta,\,x_0)$ 为 **$x_0$ 的左邻域**，记为 $N_{\delta}^{-}(x_0)$。

设 $M$ 为充分大的正数，则称 $U(\infty )=\lbrace x \mid |x|>M\rbrace$ 为 **$\infty $ 邻域**；$U(+\infty )=\lbrace x \mid x>M\rbrace$ 为 **$+\infty $ 邻域**；$U(-\infty )=\lbrace x\mid x< -M\rbrace$ 为 **$-\infty $ 邻域**。

若数集 $S$ <u>既有上界又有下界</u>，则称 $S$ 为**有界集合**；*上无界集合*和*下无界集合*统称**无界集合**。

**确界存在定理**：每一个非空上有界（或下有界）集合必有唯一的实数作为其上确界（或下确界）。

$S$ 上确界记为 $\sup S$；$S$ 下确界记为 $\inf S$。
