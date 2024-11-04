---
layout: post
title: 集合的基数，归纳与递归
date: 2024-03-26 10:08:42
updated: 2024-04-02 10:01:07
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

### 基数

**等势**（Equipotent）：如果两个集合 $A$ 和 $B$ 之间存在一个双射，则称 $A$ 和 $B$ 等势，记作 $A \approx B$，否则称 $A$ 和 $B$ 不等势，记作 $A \not\nobreak\approx B$。

等势的集合被认为基数相等，即 $|A| = |B|$。

从而有，若存在自然数 $n$（集合论的自然数定义）与集合 $S$ 等势，则称 $S$ 为*有限集*，且 $n$ 为 $S$ 的基数，记作 $|S| = n$。否则称 $S$ 为*无限集*。

$S$ 是无限集当且仅当存在 $S$ 的一个真子集 $S'$ 与 $S$ 等势。可以推出 $S$ 一定包含一个与自然数集合等势的子集。

假设 $S = S - \left\lbrace a_0 \right\rbrace$，从而定义 $f\colon S \to S'$，当 $a_i \in S'$ 时，为 $f(a_i) = a_{i+1}$，否则 $f(a_i) = a_i$。显然 $f$ 是双射，从而 $S \approx S'$。

### 可数集

**可数集**（Countable Set）：若集合 $S$ 与自然数集 $\N$ 的某个子集等势，则称 $S$ 是*可数的*。

可数个可数集的并集仍然是是可数的。例如下面是可数无穷个可数集：

| $0$ | $1$ | $2$ | $3$ | $\cdots$ |
| :-: | :-: | :-: | :-: | :------: |
| $(0, 0)$ | $(1, 0)$ | $(2, 0)$ | $(3, 0)$ | $\cdots$ |
| $(0, 1)$ | $(1, 1)$ | $(2, 1)$ | $\cdots$ |          |
| $(0, 2)$ | $(1, 2)$ | $\cdots$ |          |          |
| $(0, 3)$ | $\cdots$ |          |          |          |
| $\cdots$ |          |          |          |          |

然后按反对角线，即 $(0, 0),\, (1, 0),\, (0, 1),\, (2, 0),\, (1, 1),\, (0, 2),\, \cdots$ 计数，这样得到的序列是可数的。

### 不可数集

实数集合 $\R$ 和自然数集合 $\N$ 不等势，即 $\R$ 不可数。证明方法即<u>康托尔对角线论证</u>。

#### 康托尔定理

**康托尔定理**：任何集合与其幂集不等势，即 $A \not\approx \mathcal{P}(A)$。

证明：设 $f\colon A \to \mathcal{P}(A)$ 是 $A$ 到其幂集的一个映射，定义集合 $B = \left\lbrace x \in A \mid x \notin f(x) \right\rbrace$。

显然 $B \in \mathcal{P}(A)$。但不存在 $x \in A$ 使得 $f(x) = B$，因为若存在 $x$ 使得 $f(x) = B$，则 $x \in B \implies x \notin f(x) = B;\; x \notin f(x) = B \implies x \in B$，矛盾。

因此 $f$ 不是满射，从而 $A \not\approx \mathcal{P}(A)$。

### 优势

如果存在从集合 $A$ 到集合 $B$ 的单射，则称**集合 $B$ 优势于集合 $A$**，记作 $|A| \le |B|$ 或 $A \preccurlyeq B$。

如果集合 $B$ 优势于集合 $A$，且 $A,\, B$ 不等势，则称**集合 $B$ 真优势于集合 $A$**，记作 $|A| < |B|$ 或 $A \prec B$[^diff_with-ppt]。

[^diff_with-ppt]: 与 PPT 中的符号不同，PPT 中用的是 $\prec\!\!\cdot $，意义不明，与 $\le , <$ 的对应关系也不同（同时也不方便打）。

从而康托尔定理实际上是在说：对于任意集合 $A$，$A \prec \mathcal{P}(A)$。

#### 康托尔·伯恩斯坦定理（Cantor-Bernstein Theorem）

!!! Info ""
    若 $A \preccurlyeq B$ 且 $B \preccurlyeq A$，则 $A \approx B$。

设 $f$ 为 $A \to B$ 的单射，$g$ 为 $B \to A$ 的单射。

令 $C_0 = A \backslash g(B),\, C_{n+1} = g(f(C_n))$，并令 $C = \bigcup\limits_{n=0}^\infty C_n$。

从而定义双射 $h: A \to B$ 如下：

$$
h(a) = \begin{cases}
    f(a), & a \in C, \\
    g^{-1}(a), & a \notin C.
\end{cases}
$$

有时候找双射不如找双向单射方便。

由此可得（证明略）实数集与 $\mathcal{P}(\N)$ 等势。

### 基数

$\aleph_{\alpha}$ 表示基数，其中 $\alpha$ 为序数。

- $\aleph_0$ 是可数集合的基数
- $\aleph_1$ 是实数集合的基数
- $\aleph_2$ 是平面上的曲线集合的基数

!!! info 连续统假设（Continuum Hypothesis）
    不存在介于 $\aleph_0$ 和 $\aleph_1$ 之间的基数，即不存在集合 $A$ 使得 $\aleph_0 < |A| < \aleph_1$。

## 归纳与递归

### 良序原理

!!! info 良序原理
    $\N$ 的任何非空子集 $S$ 都有最小元素。

### 霍尔三元组

**霍尔三元组**（Hoare Triple）：$\{P\} S \{Q\}$，其中 $P$ 为*前置断言*（Precondition）、$S$ 为*语句*（Statement）、$Q$ 为*后置断言*（Postcondition）。

三元组意思是：如果在 $S$ 执行前，$P$ 为真，那么在 $S$ 执行后，$Q$ 也为真。（假设 $P$ 成立是 $S$ 的<u>权利</u>，确保 $Q$ 成立是 $S$ 的<u>义务</u>）

!!! memo ""
    可记为 $P \xrightarrow[]{S} Q$（个人记法）。

    从而有 $P = \mathbf{F}$ 是最强的前置条件。

这称为**部分正确性**，因为 $S$ 能否执行完成需要另行说明。即程序的**完全正确性**还需要说明程序在有限步内终止。
