---
layout: post
title: 独立性
date: 2024-09-20 09:11:52
updated: 2024-09-20 09:11:52
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

!!! memo ""
    半英文授课（课件全英文，专有名词也是讲英文），因此一些不好翻译的专有名词以 `English (中文)` 形式出现；一些可能翻错的词语在后面补充原词，即 `词语（phrase）`；一些难以翻译的句子在后面给出原文，即 `句子（sentence）`。

    后面可能也难以维持，而也像另一个也带有「数据」的课程一样，改成英文笔记。

## 独立性

### 两个事件的独立性

!!! info ""
    若 $B$ 的发生对于 $A$ 的发生没有影响，即 $\Pr(A \mid B) = \Pr(A)$，则称事件 $A$ 与事件 $B$ **独立**（$A$ is said to be **independent** of $B$）。

!!! info ""
    两个事件 $A, B$ **独立**若

    $$
    \Pr(A \cap B) = \Pr(A) \Pr(B)
    $$

命题：
- 若 $\Pr(B) > 0$，则 $\Pr(A \mid B) = \Pr(A) \iff \Pr(A \cap B) = \Pr(A) \Pr(B)$ 
- $\Pr(A \cap B) = \Pr(A) \Pr(B) \iff \Pr(A \cap B^c) = \Pr(A) \Pr(B^c)$

### 多个事件的独立性

!!! info ""
    一个事件的集合（family）$\left\lbrace A_i \mid i \in I \right\rbrace$ 称为 **（相互）独立**如果对于所有有限子集 $J \subseteq I$，有

    $$
    \Pr\left(\bigcap_{i \in J} A_i\right) = \prod_{i \in J} \Pr(A_i)
    $$

!!! info ""
    一个事件 $A$ 称为与一个事件的集合 $\left\lbrace B_i \mid i \in I \right\rbrace$**（相互）独立**，如果对于所有互斥的有限子集 $J^{+}，J^{-} \subseteq I$，有

    $$
    \Pr(A) = \Pr\left(A \Biggm| \bigcap_{i \in J^{+}} B_i \cap \bigcap_{i \in J^{-}} B_i^c\right)
    $$

## Product Probability Space (积概率空间)

概率空间由一系列*独立实验*构成。

考虑离散概率空间 $(\Omega_1, p_1),\, (\Omega_2, p_2),\, \cdots,\, (\Omega_n, p_n)$，**product probability space**（积概率空间）被定义为
- 样本空间 $\Omega = \Omega_1 \times \Omega_2 \times \cdots \times \Omega_n$
- $\forall \omega = (\omega_1, \omega_2, \cdots, \omega_n) \in \Omega\colon \operatorname{pmf} p(\omega) = p_1(\omega_1) p_2(\omega_2) \cdots p_n(\omega_n)$（pmf 即「概率质量函数」）

!!! note ""
    对于一般（general）的概率空间 $(\Omega_1, \Sigma_1, \Pr_1), \cdots, (\Omega_n, \Sigma_n, \Pr_n)$，product probability space $(\Omega, \Sigma, \Pr)$ 可以被类似地构造。

    其中 $\Sigma$ 是唯一的（unique）最小 $\sigma$-代数，使得其包括（contain）$\Sigma_1 \times \cdots \times \Sigma_n$，同时概率测度 $\Pr$ 是一个在 $\Sigma$ 上的自然拓展（the law $\Pr$ is a natural extension onto such $\Sigma$ from the product probabilities）：

    $$
    \forall A = A_1 \times \cdots \times A_n \in \Sigma\colon \Pr(A) = \Pr\nolimits_1(A_1) \cdots \Pr\nolimits_n(A_n)
    $$

## 有限独立性（Limited Independence）

!!! info 成对独立（Pairwise Independence）
    一个事件的集合 $\left\lbrace A_i \mid i \in I \right\rbrace$ 称为 **成对独立**（pairwise independent），如果对于所有不同的 $i, j \in I$，有

    $$
    \Pr(A_i \cap A_j) = \Pr(A_i) \Pr(A_j)
    $$

    <!-- {{{ k-wise -->
    <details>
    <summary>类似地可定义 k-wise Independence</summary>
    
    一个事件的集合 $\left\lbrace A_i \mid i \in I \right\rbrace$ 称为 **$k$-wise 独立**（$k$-wise independent），如果对于所有不同的 $i_1, i_2, \cdots, i_k \in I$，有

    $$
    \Pr\left(\bigcap_{i=1}^{k} A_{i}\right) = \prod_{i=1}^{k} \Pr(A_{i})
    $$
    
    </details>
    <!-- }}} -->

!!! note ""
    （相互）独立一定是成对独立，但反之不一定成立。

    triply independent 不一定是 pairwise independent。

## Error Reduction (one-sided case)

对于 decision problem $f\colon \left\lbrace 0, 1 \right\rbrace^{*} \to \left\lbrace 0, 1 \right\rbrace$ ，蒙特卡洛（Monte Carlo）随机算法 $\mathscr{A}$ 有 one-sided error：
- $\forall x \in \left\lbrace 0, 1 \right\rbrace^{*}\colon f(x) = 1 \implies \mathscr{A}(x) = 1$
- $\forall x \in \left\lbrace 0, 1 \right\rbrace^{*}\colon f(x) = 0 \implies \Pr[\mathscr{A}(x) = 0] \ge p$

$\mathscr{A}^n$ 为*独立*运行 $\mathscr{A}$ $n$ 次，输出结果的 $\land $（即「与」），因为

$$
f(x) = 0 \implies \Pr[\mathscr{A}^n(x) = 1] \le (1 - p)^n
$$

为将 one-sided error 减小到 $\varepsilon$，大致需要重复 $n \approx \dfrac{1}{p} \ln \dfrac{1}{\varepsilon}$ 次。

## Binomial Probability (二项概率)

!!! info ""
    考虑 $n$ 个独立抛掷硬币实验，每个硬币正面朝上相互独立，且概率为 $p$。
    
    我们称我们有一系列（sequence）**伯努利实验**（Bernoulli trials），其中每个实验成功（succeed）的概率为 $p$。
    
    **Binomial Probability** (二项概率) $p(k)$ 定义为 $n$ 次实验中成功 $k$ 次的概率：

    $$
    \begin{aligned}
        p(k) &= \sum_{S \in \binom{[n]}{k}} \Pr(\forall i \in S\colon \text{第 $i$ 次成功}) \Pr(\forall i \in [n] \backslash S\colon \text{第 $i$ 次失败}) \\ 
        &= \sum_{S \in \binom{[n]}{k}} p^{|S|} (1 - p)^{n - |S|} \\
        &= \dbinom{n}{k} p^k (1 - p)^{n - k}
    \end{aligned}
    $$

    $p(k)$ 是在 $\Omega = \left\lbrace 0, 1, \cdots, n \right\rbrace$ 良定义的概率密度函数，即 $\displaystyle \sum_{k=0}^{n} p(k) = 1$（二项式定理）。

~~如何操纵 2024 美国大选~~？假设在一个社会上有 $n$ 个独立随机投票的选民，需要大概多少人才能以 $t = 95\%$ 的概率操纵选举（假设只有两个候选人）？

下面推导用硬币的 HEAD 和 TAIL 替代（因为想不到合适的词）：

$$
\begin{aligned}
    \Pr[|\text{HEADs} - \text{TAILs}| \ge t] &= \Pr\left[\text{HEADs} \le \tfrac{n}{2} - \tfrac{t}{2}\right] + \Pr\left[\text{HEADs} \ge \tfrac{n}{2} + \tfrac{t}{2}\right] \\ 
    &= \sum_{k \le  \frac{n-t}{2}} \dbinom{n}{k} 2^{-n} + \sum_{k \ge \frac{n+t}{2}} \dbinom{n}{k} 2^{-n} \\ 
    &= 2^{1-n} \sum_{k \le  \frac{n-t}{2}} \dbinom{n}{k}\\ 
    &\le 2^{1-n+nH(\frac{1}{2} - \frac{t}{2n})}\\ 
    &\approx 2 \exp\left(-\tfrac{t^2}{n}\right)
\end{aligned}
$$

当 $t \ge 2 \sqrt{n}$ 时有 $\Pr[|\text{HEADs} - \text{TAILs}| \ge t] \le 0.05$。

## Error Reduction (two-sided case)

对于 decision problem $f\colon \left\lbrace 0, 1 \right\rbrace^{*} \to \left\lbrace 0, 1 \right\rbrace$ ，蒙特卡洛（Monte Carlo）随机算法 $\mathscr{A}$ 有 two-sided error：
- $\forall x \in \left\lbrace 0, 1 \right\rbrace^{*}\colon f(x) = 1 \implies \Pr[\mathscr{A}(x) = f(x)] \ge \dfrac{1}{2} + p$

$\mathscr{A}^n$ 为*独立*运行 $\mathscr{A}$ $n$ 次，输出 $n$ 次结果的「多数」（majority），因为

$$
\Pr[\mathscr{A}^n(x) \ne f(x)] \le \sum_{k < \frac{n}{2}} \dbinom{n}{k} \left( \dfrac{1}{2} + p \right)^{k} \left( \dfrac{1}{2} - p \right)^{n - k} \textcolor{FF0099}{\le \exp(-np^2)}
$$

在 $n \ge \dfrac{1}{p^2} \ln \dfrac{1}{\varepsilon}$ 时有 $\Pr[\mathscr{A}^n(x) \ne f(x)] \le \varepsilon$。

彩色部分如何计算？[集中不等式（concentration inequality）](https://zh.wikipedia.org/wiki/集中不等式)。暂略。

## 条件独立性（Conditional Independence）

!!! info ""
    两个事件 $A, B$ 在给定事件 $C$（$\Pr(C) > 0$）下**条件独立**（conditionally independent），如果

    $$
    \Pr(A \cap B \mid C) = \Pr(A \mid C) \Pr(B \mid C)
    $$

!!! note ""
    若 $\Pr(B \cap C) > 0$，则 $\Pr(A \cap B \mid C) = \Pr(A \mid C) \Pr(B \mid C) \iff \Pr(A \mid B \cap C) = \Pr(A \mid C)$。

!!! note ""
    两个独立事件可能并不是条件独立的。两个非独立事件可能是条件独立的。

    例如：
    1. 第一个例子：显然 $A, B$ 独立，但不条件独立。
        - $A$：第一个硬币 HEAD
        - $B$：第二个硬币 HEAD
        - $C$：两个硬币结果不同
    2. 第二个例子：$A$ 与 $A$ 在给定 $A$ 的情况下是条件独立的，但 $A$ 和 $A$ 并不一定独立。

### 例子

[布隆过滤器（Bloom Filter）](https://zh.wikipedia.org/wiki/布隆过滤器)是一种空间效率高的概率型数据结构，用于检测一个元素是否在一个集合中。

假设数据集 $S \subseteq U$，大小为 $n$，决定查询 $x \in U$ 是否在 $S$ 当中。

采用布隆过滤器这个数据结构。设一个字节数组（bit array）$A \in \left\lbrace 0, 1 \right\rbrace^m$，其被初始化为全 $0$。

有 $k$ 个均匀独立（uniform & independent）哈希函数 $h_1, \cdots, h_k\colon U \to [m]$。对于任意 $x_i \in S$，将 $A[h_1(x_i)], \cdots, A[h_k(x_i)]$ 置为 $1$。

查询时，若 $A[h_1(x)], \cdots, A[h_k(x)]$ 均为 $1$，则返回 $x \in S$；否则返回 $x \notin S$。

当 $x \in S$ 时，查询结果一定是正确的；当 $x \notin S$ 时，查询结果可能误报（false positive）。对这种可能进行概率分析：

$$
\begin{aligned}
    \Pr\left[\forall 1 \le j \le k\colon A[h_{j}(x)] = 1\right] &\textcolor{FF0099}{=} \left( \Pr[A[h_{j}(x)] = 1] \right)^{k}\\ 
    &= \left( 1 - \Pr[A[h_{j}(x)] = 0] \right)^{k}\\ 
    &\le \left( 1 - \left( 1 - \dfrac{1}{m} \right)^{kn} \right)^{k}\\ 
    &\approx \left(1 - \exp\left(- \dfrac{kn}{m}\right)\right)^{k}\\ 
    &= 2^{-c \ln 2}\\ 
    &\le 0.6185^{c}
\end{aligned}
$$

其中取 $\left\lbrace\begin{aligned} k &= c \ln 2\\ m &= cn \end{aligned}\right.$。

但是这个分析实际上是错误的，在第一个等号就出问题了。不同的 $h_{j}(x)$ 实际上可以映射到同一个位置（希望我没理解错）。

这部分可见[英文维基部分](https://en.wikipedia.org/wiki/Bloom_filter#Probability_of_false_positives)。
