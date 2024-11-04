---
layout: post
title: 集合及其运算
date: 2024-03-14 09:56:23
updated: 2024-04-16 08:44:53
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 集合定义

直观定义：一个**集合**是一组无序的对象，这些对象称为这个集合的**元素**或**成员**。$a \in A$ 表示 $a$ 是集合 $A$ 的一个成员，$a \notin A$ 表示 $a$ 不是 $A$ 的成员。

康托尔（Georg Cantor）：A **set** is a collection into a whole of <u>definite, distinct objects</u> of our intuition or our thought. The objects are called <u>elements (member) of the set</u>.

朴素集合论高中学过，就懒得记了……

## 集合关系

!!! info ""
    **集合相等**当且仅当它们有相同的元素。

    $A = B$ 当且仅当 $\forall x (x \in A \leftrightarrow x \in B)$。

!!! info ""
    集合 $A$ 称为集合 $B$ 的**子集**，当且仅当 $\forall x (x \in A \rightarrow x \in B)$，记作 $A \subseteq B$。

    如果 $A \subseteq B$ 且 $A \neq B$，则称 $A$ 是 $B$ 的**真子集**，记作 $A \subset B$。

    从而可知 $A = B \iff A \subseteq B \land B \subseteq A$。

!!! note ""
    $$
    X \subseteq Y \land Y \subseteq Z \implies X \subseteq Z
    $$

## 集合大小

对于有限集合，若集合 $S$ 恰有 $n \in \N$ 个不同的元素，则称 $S$ 为**有限集合**（finite set），并记 $|S| = n$ 为 $S$ 的**基数**。

如果一个集合不是有限集合，则称其为**无限集合**（infinite set）。

特别地，**空集** $\empty$ 是唯一的零集。

## 幂集

集合 $S$ 的**幂集**（power set）是 $S$ 的所有子集的集合，记作 $\mathcal{P}(S)$。即 $\mathcal{P}(S) = \{A \mid A \subseteq S\}$。

显然，$|\mathcal{P}(S)| = 2^{|S|}$[^why]，因此 $S$ 的幂集还可以记作 $2^S$。

[^why]: 任意一个子集对应一个函数 $f\colon S \to \left\lbrace 0, 1 \right\rbrace$，这样的函数的个数，可以参见下一节内容。当然也可以发现对于任意一个元素 $s \in S$，取值有 $0, 1$ 两种情况，乘法原理知为 $2^{|S|}$。

$$
A \subset B \iff \mathcal{P}(A) \subseteq \mathcal{P}(B)
$$

## 集合运算

- **并集**（union）：$A \cup B = \{x \mid x \in A \lor x \in B\}$。
- **交集**（intersection）：$A \cap B = \{x \mid x \in A \land x \in B\}$。
- **差集**（difference）：$A - B = \{x \mid x \in A \land x \notin B\}$，也称作 $B$ 对于 $A$ 的**补集**。
    - 对于全集 $U$，$U - A$ 称为 $A$ 的**补集**，记作 $\sim B$
- **对称差**（symmetric difference）：$A \oplus B = (A - B) \cup (B - A)$[^oplus]。
    - $A \oplus B = (A \cup B) - (A \cap B)$
- **广义并**（generalized union）：$\bigcup A = \left\lbrace x \mid \exists y (y \in A \land x \in y) \right\rbrace$。
    - 例如 $\left\lbrace  \{1, 2\}, \{2, 3\} \right\rbrace$ 的广义并是 $\{1, 2, 3\}$。
- **广义交**（generalized intersection）：$\bigcap A = \left\lbrace x \mid \forall y (y \in A \to x \in y) \right\rbrace$（其中 $A \ne \empty$）
    - 例如 $\left\lbrace  \{1, 2\}, \{2, 3\} \right\rbrace$ 的广义交是 $\{2\}$。
    - $\bigcap \empty$ 无意义。

[^oplus]: 明明是「差」「difference」，但用的却是 `\oplus`…维基用的是 $\triangle $（`\tiangle`），难怪 Copilot 如此提示。

$A \cup B$ 是 $A$ 和 $B$ 的**最小上界**，$A \cap B$ 是 $A$ 和 $B$ 的**最大下界**。

恒等式：
- 恒等律
    - $A \cup \empty = A$
    - $A \cap U = A$
- 支配律
    - $A \cup U = A$
    - $A \cap \empty = \empty$
- 幂等律
    - $A \cup A = A$
    - $A \cap A = A$
- 补集律：$\sim (\sim A) = A$
- 交换律
    - $A \cup B = B \cup A$
    - $A \cap B = B \cap A$
- 结合律
    - $(A \cup B) \cup C = A \cup (B \cup C)$
    - $(A \cap B) \cap C = A \cap (B \cap C)$
- 分配律
    - $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$
    - $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$
- 德摩根律
    - $\sim (A \cup B) = \sim A \cap \sim B$
    - $\sim (A \cap B) = \sim A \cup \sim B$
- 吸收律
    - $A \cup (A \cap B) = A$
    - $A \cap (A \cup B) = A$
- 补律
    - $A \cup \sim A = U$
    - $A \cap \sim A = \empty$

## 集合与谓词逻辑

$$
\begin{aligned}
    \forall x (x \in S \to P(x)) &\iff \forall x \in S.\, P(x) &\iff \mathop{\Large\forall}\limits_{x \in S} P(x)\\ 
    \exists x (x \in S \land P(x)) &\iff \exists x \in S.\, P(x) &\iff \mathop{\Large\exists}\limits_{x \in S} P(x)
\end{aligned}
$$

## 笛卡尔乘积

**有序偶**（ordered pair）：$(a, b)$ 表示 $a$ 和 $b$ 的有序偶。$(a, b) = (x, y) \iff a = x \land b = y$。
- $(a, b) \triangleq \left\lbrace \{a\}, \{a, b\} \right\rbrace$

**笛卡尔乘积**（Cartesian product）：$A \times B = \{(a, b) \mid a \in A \land b \in B\}$。

- $A \times B$ 不一定等于 $B \times A$，$A \times B = B \times A$ 当且仅当 $A = B$ 或 $A = \empty$ 或 $B = \empty$。

$n$ 个集合的笛卡尔乘积：

$$
A_1 \times \cdots \times A_n = \{(a_1, \ldots, a_n) \mid a_1 \in A_1 \land \cdots \land a_n \in A_n\}
$$

对有限集合，有

$$
|A \times B| = |A| \times |B|
$$
