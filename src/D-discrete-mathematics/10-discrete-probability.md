---
layout: post
title: 离散概率
date: 2024-04-09 10:05:58
updated: 2024-04-23 09:59:51
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 离散概率分析

概率分析四步法：
1. 选定样本空间（Find the sample space）
2. 定义相关事件（Define events of interests）
3. 确定结果概率（Determine outcome probabilities）
4. 计算事件概率（Compute event probabilities）

### 选定样本空间

**样本空间**是所有可能结果的集合。

### 定义相关事件

**事件**是样本空间的一个子集。

## 概率的定义

**古典概率**（Laplacian probability）：对于结果具有相同可能性的有限样本空间 $\mathcal{S}$ 及其一个事件 $E$，则称事件 $E$ 的概率为

$$
P(E) = \frac{|E|}{|\mathcal{S}|}
$$

频率主义的概率（frequentist probability）：定义事件 $E$ 的概率为

$$
P(E) = \lim_{n \to \infty} \frac{n_E}{n}
$$

伯特兰悖论（Bertrand's paradox）：对于一个圆上的随机弦，其长度的概率分布是不确定的。

<style>
@media (prefers-color-scheme: dark) {
    img[src$='#invert'] {
        -webkit-filter: invert(1);
        filter: invert(1) hue-rotate(180deg);
        mix-blend-mode: screen;
    }
}
</style>

![](10-discrete-probability/bertrand-1.svg#invert)

随机端点：$\dfrac{\frac{2 \pi r}{3}}{2 \pi r} = \dfrac{1}{3}$

![](10-discrete-probability/bertrand-2.svg#invert)

随机弦：$\dfrac{\frac{r}{2}}{r} = \dfrac{1}{2}$

![](10-discrete-probability/bertrand-3.svg#invert)

随机中点：$\dfrac{\pi \left(\frac{r}{2}\right)^2}{\pi r^2} = \dfrac{1}{4}$

其原因在于「随机」的定义不明确，从而使样本空间不确定。

## 基于集合论的概率

### 基于集合论的概率定义

可数**样本空间** $\mathcal{S}$ 是一个可数集合，$\mathcal{S}$ 的每一个元素 $\omega$ 称为一个**结果**。

满足下列条件的函数 $\Pr\colon \mathcal{S} \to \R$ 称为样本空间 $\mathcal{S}$ 上的一个**概率函数**：
- 非负性：对于任意 $\omega \in \mathcal{S}$，有 $\Pr[\omega] \ge 0$；
- 规范性：$\displaystyle \sum_{\omega \in \mathcal{S}} \Pr[\omega] = 1$；

样本空间 $\mathcal{S}$ 的一个子集 $E \subseteq \mathcal{S}$ 称为一个**事件**。事件 $E$ 的**概率**定义为 $\Pr[E] = \displaystyle \sum_{\omega \in E} \Pr[\omega]$[^probability]。

[^probability]: 课件用的是 $\Coloneqq$ `\Coloneqq`，我比较懒，反正也没歧义……下同。

### 基于集合论的概率计算

!!! info ""
    设 $E$ 是样本空间 $\mathcal{S}$ 的一个事件，$E$ 的**补事件** $\bar{E}$ 的概率定义为 $\Pr[\bar{E}] = 1 - \Pr[E]$。

!!! info ""
    设 $E_1, E_2$ 是样本空间 $\mathcal{S}$ 的两个事件，$E_1 \cup E_2$ 的概率定义为 $\Pr[E_1 \cup E_2] = \Pr[E_1] + \Pr[E_2] - \Pr[E_1 \cap E_2]$。

!!! info ""
    假设 $\mathcal{S}$ 是一个含 $n$ 个元素的样本空间，**均匀分布**（Uniform Distribution）赋给 $\mathcal{S}$ 中的每一个元素的概率都是 $\dfrac{1}{n}$。

### 条件概率

!!! info ""
    设 $E, F$ 为事件，且 $\Pr[F] > 0$，则 $E$ <u>在事件 $F$ 发生的条件下</u>的**条件概率**（Conditional Probability）定义为 $\Pr[E \mid F] = \dfrac{\Pr[E \cap F]}{\Pr[F]}$。

### 贝叶斯定理

!!! info 贝叶斯定理
    设 $E, F$ 是样本空间 $\mathcal{S}$ 中的事件，且 $\Pr[E], \Pr[F] \ne 0$，则

    $$
    \begin{aligned}
    \Pr[E \mid F] &= \dfrac{\Pr[F \mid E] \Pr[E]}{\Pr[F]} \\
    &= \dfrac{\Pr[F \mid E] \Pr[E]}{\Pr[F \mid E] \Pr[E] + \Pr[F \mid \bar{E}] \Pr[\bar{E}]}
    \end{aligned}
    $$

    ---

    证明：

    由条件概率，有

    $$
    \begin{aligned}
        \Pr[E \mid F] \Pr[E] &= \Pr[E \cap F]\\ 
        &= \Pr[F \cap E]\\
        &= \Pr[F \mid E] \Pr[E]
    \end{aligned}
    $$
    
    又

    $$
    \begin{aligned}
        \Pr[F] &= \Pr[(E \cap F) \cup (\bar{E} \cap F)]\\
        &= \Pr[E \cap F] + \Pr[\bar{E} \cap F]\\
        &= \Pr[F \mid E] \Pr[E] + \Pr[F \mid \bar{E}] \Pr[\bar{E}]
    \end{aligned}
    $$

- $\Pr[A]$ 是 $A$ 的**先验概率**（Prior Probability），因为它是在考虑任何新证据（$B$）之前的概率
- $\Pr[A \mid B]$ 是已知 $B$ 发生后 $A$ 的**后验概率**（Posterior Probability）
- $\Pr[B \mid A]$ 是已知 $A$ 发生后 $B$ 的后验概率
- $\Pr[B]$ 是 $B$ 的先验概率，也作**标准化常量**（Normalizing Constant）

贝叶斯定理在罕见病的例子，可以见 3Blue1Brown[^3b1b] 视频：[医检阳性≠得了病？重新理解贝叶斯定理](https://www.bilibili.com/video/BV1Ei4y1F72M)。

[^3b1b]: 3B 一出来，Copilot 就有提示了。

### 事件独立性

!!! info ""
    事件 $E, F$ 是**独立**的，当且仅当 $\Pr[E \cap F] = \Pr[E] \cdot \Pr[F]$。

## 随机变量、期望和方差

### 随机变量

!!! info 随机变量
    一个随机变量 $X$ 是一个定义域为样本空间 $\mathcal{S}$ 的函数。

    其伴域可为任意非空集合，但通常取为实数集 $\R$，即 $X\colon \mathcal{S} \to \R$。

随机变量既不「随机」，也非「变量」，而是一个函数。[^lf]

[^lf]: lf 好像提到过？似乎要与「随机事件」区分开来？

!!! info 随机变量的分布
    $X$ 是样本空间 $\mathcal{S}$ 上的一个随机变量，$X$ 的**分布**（Distribution）是形如 $(r, \Pr[X = r])$ 的二元组集合，其中 $r \in X(\mathcal{S})$，$\Pr[X = r]$ 是 $X$ 取值为 $r$ 的概率。

### 期望

!!! info 期望
    设 $X$ 是样本空间 $\mathcal{S}$ 上的一个随机变量，$X$ 的**期望**（Expectation）定义为[^expectation]

    [^expectation]: 课件用的是 $\operatorname{Ex}$ `\operatorname{Ex}`，太长了，也懒得加宏了，就用 $\mathbb{E}$ `\mathbb{E}`（这个有 snippets 加持），也是高中时用的吧。

    $$
    \mathbb{E}[X] = \sum_{\omega \in \mathcal{S}} X(\omega) \cdot \Pr[\omega]
    $$

$X(\omega) - \mathbb{E}[X]$ 称为 $X$ 在 $\omega$ 处的**偏差**（Deviation）。

显然有

$$
\mathbb{E}\left[\dfrac{1}{X}\right] \ne \dfrac{1}{\mathbb{E}[X]}
$$

等价定义：

$$
\mathbb{E}[X] = \sum_{x \in X(\mathcal{S})} x \cdot \Pr[X = x]
$$

因为有

$$
\begin{aligned}
    \mathbb{E}[X] &= \sum_{\omega \in \mathcal{S}} X(\omega) \cdot \Pr[\omega]\\
    &= \sum_{x \in X(\mathcal{S})} \sum_{\omega \in [X = x]} X(\omega) \cdot \Pr[\omega]\\
    &= \sum_{x \in X(\mathcal{S})} \sum_{\omega \in [X = x]} x \cdot \Pr[\omega]\\
    &= \sum_{x \in X(\mathcal{S})} x \cdot \left(\sum_{\omega \in [X = x]} \Pr[\omega]\right)\\
    &= \sum_{x \in X(\mathcal{S})} x \cdot \Pr[X = x]
\end{aligned}
$$

!!! info 条件期望
    给定随机变量 $R$，$R$ 在已知事件 $A$ 条件下的期望值是 $R$ 在 $A$ 中结果上的取值的概率加权平均值，即

    $$
    \mathbb{E}[R \mid A] = \sum_{r \in R(\mathcal{S})} r \cdot \Pr[R = r \mid A]
    $$

!!! info 全期望公式
    令 $R$ 为样本空间 $\mathcal{S}$ 上的一个随机变量，且 $\mathcal{S}$ 可以分解为一系列互斥事件 $A_1, A_2, \cdots$，则

    $$
    \mathbb{E}[R] = \sum_{i} \mathbb{E}[R \mid A_i] \cdot \Pr[A_i]
    $$
    
期望的线性性质：
- $\displaystyle \mathbb{E}\left[\sum_{i=1}^{n}X_i\right] = \sum_{i=1}^{n}\mathbb{E}[X_i]$ 
- $\mathbb{E}[aX + b] = a\mathbb{E}[X] + b$

!!! info 独立随机变量
    样本空间 $\mathcal{S}$ 上的随机变量 $X, Y$ 是**独立**的，当且仅当对于所有 $x \in X(\mathcal{S})$ 和 $y \in Y(\mathcal{S})$，有 $\Pr[X = x \land Y = y] = \Pr[X = x] \cdot \Pr[Y = y]$。

对于样本空间 $\mathcal{S}$ 上*独立*的随机变量 $X, Y$，有 $\mathbb{E}[XY] = \mathbb{E}[X] \cdot \mathbb{E}[Y]$。

### 方差

!!! info 方差
    设 $X$ 是样本空间 $\mathcal{S}$ 上的一个随机变量，$X$ 的**方差**（Variance）定义为[^variance]

    [^variance]: 一样的，课件用的是 $\operatorname{Var}$ `\operatorname{Var}`，我还是用 $\mathbb{V}$ `\mathbb{V}`…当然其实还能用 $\sigma^2$ `\sigma^2` 等。

    $$
    \mathbb{V}[X] = \mathbb{E}\left[(X - \mathbb{E}[X])^2\right]
    $$

    即方差是「随机变量 $X$ 在 $\omega$ 处偏差的平方的加权平均值」。

!!! info 标准差
    随机变量 $X$ 的**标准差**（Standard Deviation）定义为 $\sqrt{\mathbb{V}[X]}$，记作 $\sigma_X$ 或 $\sigma(X)$ 

样本空间 $\mathcal{S}$ 上的随机变量 $X$ 的方差有

$$
\mathbb{V}[X] = \mathbb{E}[X^2] - \mathbb{E}[X]^2
$$

- 对于样本空间 $\mathcal{S}$ 上的两两*独立*随机变量 $X_1, X_2, \cdots X_n$，有 $\displaystyle \mathbb{V}\left[\sum_{i=1}^{n}X_i\right] = \sum_{i=1}^{n}\mathbb{V}[X_i]$
- $\mathbb{V}[aX + b] = a^2\mathbb{V}[X]$

!!! info Bienaymé 公式
    对样本空间 $\mathcal{S}$ 上<u>独立</u>的随机变量 $X, Y$ 有：

    $$
    \mathbb{V}[X + Y] = \mathbb{V}[X] + \mathbb{V}[Y]
    $$
    
    并推广到 $n$ 个独立随机变量的情况：

    $$
    \mathbb{V}\left[\sum_{i=1}^n X_i\right] = \sum_{i=1}^n \mathbb{V}[X_i]
    $$
