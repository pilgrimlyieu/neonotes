---
layout: post
title: 函数及其运算
date: 2024-03-19 09:45:18
updated: 2024-03-19 09:45:18
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 关系

若 $A, B$ 是集合，从 $A$ 到 $B$ 的一个（二元）**关系**（Relation）是 $A \times B$ 的一个子集，即

$$
R \subseteq A \times B
$$

若 $A = B$，称为集合 $A$ 上的（二元）关系。

- 集合 $A$ 上的**空关系** $\empty$，即空集。
- **全域关系** $E_A = A \times A$
- **恒等关系**：$I_A = \{(a, a) \mid a \in A\}$

## 函数

### 概念

设 $A, B$ 为非空集合，从集合 $A$ 到 $B$ 的**函数**（Function）$f$ 是对元素的一种指派：给 $A$ 的每个元素均指派 $B$ 的一个元素，记作 $f\colon A \to B$，其中：
- $f\colon A \to B$：函数的**型构**（Signature）
- $A$：函数的**定义域**（Domain）
- $B$：函数的**伴域**（Codomain）
- $f(a) = b$：$a$ 在 $f$ 下的像是 $b$，$b$ 是 $a$ 的**像**（Image），$a$ 是 $b$ 的**原像**（Preimage）
- $f(A) = \{f(a) \mid a \in A\}$：$f$ 的**值域**（Range），显然有 $f(A) \subseteq B$（一般的，对于 $S \subseteq A$，有 $f(S) = \{f(a) \mid a \in S\}$）
- 函数也称为**映射**（Mapping）或**变换**（Transformation）

函数相等，$f = g$ 当且仅当：
- $\operatorname{dom} f = \operatorname{dom} g$ 
- $\forall x \in \operatorname{dom} f,\, f(x) = g(x)$
- $\operatorname{codom} f = \operatorname{codom} g$

从 $A$ 到 $B$ 的不同函数有 $|B|^{|A|}$ 个。

函数是一种特殊的关系：若 $f$ 是从 $A$ 到 $B$ 的函数，则 $R = \{(x, f(x)) \mid x \in A\}$ 是一个从 $A$ 到 $B$ 的关系。亦即对于 $A$ 中每个元素 $x$，$B$ 中都有且仅有一个元素使得 $R(a, b)$（或记作中缀形式 $aRb$），则 $R$ 是一个从 $A$ 到 $B$ 的函数。

### 特殊函数

设 $A$ 为非空集合，$A$ 上的**恒等函数** $\iota_A\colon A \to A$ 定义为：

$$
\iota_A(x) = x,\quad x \in A
$$

设 $U$ 为非空集合，对任意 $A \subseteq U$，**特征函数** $\chi_A\colon U \to \{0, 1\}$ 定义为：

$$
\chi_A(x) = \begin{cases}
    1, & x \in A \\
    0, & x \notin A
\end{cases}
$$

设函数 $f\colon A \to B$，且 $X, Y \subseteq A$，则
- $f(X \cup Y) = f(X) \cup f(Y)$
- $f(X \cap Y) \subseteq f(X) \cap f(Y)$

- 函数 $f\colon A \to B$ 是**单射**（Interjection, Interjective function, One-to-one function）
    - $\forall x_1, x_2 \in A$，若 $x_1 \ne x_2$，则 $f(x_1) \ne f(x_2)$
    - 亦即 $\forall x_1, x_2 \in A$，若 $f(x_1) = f(x_2)$，则 $x_1 = x_2$
- 函数 $f\colon A \to B$ 是**满射**（Surjection, Surjective function, Onto function）
    - $\forall y \in B,\,  \exists x \in A$，使得 $f(x) = y$
    - 亦即 $f(A) = B$
- 函数 $f\colon A \to B$ 是**双射**（Bijection, Bijective function, One-to-one correspondence）
    - 既是单射又是满射

对于有限集合 $A$，$f$ 是从 $A$ 到 $A$ 的函数，$f$ 是单射当且仅当 $f$ 是满射。（对有限集合才成立，否则可以像希尔伯特的旅馆问题一样构造）

设 $f$ 是从 $A$ 到 $B$ 的双射，$f$ 的**反函数**是从 $B$ 到 $A$ 的函数 $f^{-1}$，它指派给 $B$ 中元素 $b$ 的是 $A$ 中满足 $f(a) = b$ 的唯一元素 $a$。

### 函数的运算

设 $g\colon A \to B,\, f\colon B \to C$，则 $(f \circ g)(x) = f(g(x)),\, x \in A$ 是 $f$ 和 $g$ 的**复合函数**（Composition）。

- 复合函数的结合律：$(f \circ g) \circ h = f \circ (g \circ h)$
- 满射的复合函数是满射
    - $f \circ g$ 是满射只能推出 $f$ 是满射，不能推出 $g$ 是满射
- 单射的复合函数是单射
    - $f \circ g$ 是单射只能推出 $g$ 是单射，不能推出 $f$ 是单射
- 双射的复合函数是双射
- 设 $f$ 是从 $A$ 到 $B$ 的双射，$f^{-1}$ 是 $f$ 的反函数，则
    - $f^{-1} \circ f = \iota_A$
    - $f \circ f^{-1} = \iota_B$

函数的加法乘法类似，$(f + g)(x)$ 与 $(f \cdot g)(x)$（懒鬼写法：$fg(x)$ ）分别定义为 $f(x) + g(x)$ 与 $f(x) \cdot g(x)$。
- 需要注意的是，$(f + g)(x)$ 的 $+$ 和 $f(x) + g(x)$ 的 $+$ 并不意义相等，前者可以看作是 $+ \colon (A \to B_1) \times (A \to B_2) \to (A \to C)$ 的中缀形式，后者则是 $+ \colon B_1 \times B_2 \to C$ 的中缀形式。

递增函数：
- $f$ 递增：$\forall x \forall y \bigl(x < y \to f(x) \le f(y)\bigr)$ 
- $f$ 严格递增：$\forall x \forall y \bigl(x < y \to f(x) < f(y)\bigr)$

### 部分函数

设 $A, B$ 为非空集合，$A$ 到 $B$ 的**部分函数**（Partial Function）$f$ 是对元素的一种指派，对 $A$ 中的某些元素各指派 $B$ 中的一个元素，记作 $f\colon A \rightharpoonup B$（还有一些诡异的记号，如 $f\colon A \nrightarrow B,\, f\colon A \hookrightarrow B$）。

### 函数构成的集合

$B^A$：从非空集合 $A$ 到非空集合 $B$ 的函数构成的集合，
- 对有限集合 $A, B$，$\left|B^A\right| = |B|^{|A|}$

### 序列

一个**序列**（Sequence）是从 $\Z$ 的一个子集（通常是 $\N$ 或 $\Z^{+}$) 到某个集合 $S$ 的一个函数。我们用 $a_{n}$ 代表整数 $n$ 的**像**，称为这个序列的**项**，$\left\{a_{n}\right\}$ 代表这个序列。
