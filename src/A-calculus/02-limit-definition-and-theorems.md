---
layout: post
title: 极限定义与有关定理
date: 2023-10-09 18:53:48
updated: 2024-04-30 17:51:08
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

!!! memo ""
    最近上课没怎么听了，都在写题目。因此笔记也就瞎记了。

## 1.2 极限

### 子数列

设有数列 $\left\lbrace x_n \right\rbrace$，从 $\left\lbrace x_n \right\rbrace$ 中抽出无穷多项，按其在原数列的顺序排成的新数列称为 $\left\lbrace x_n \right\rbrace$ 的一个**子数列**或*部分数列*。

### 定理 1.2.6

!!! info ""
    设 $\lim\limits_{n \to \infty}x_n=A \in \R$，$\left\lbrace x_{n_k} \right\rbrace$ 是 $\left\lbrace x_n \right\rbrace$ 的一个子数列，则

    $$
    \lim\limits_{k \to \infty}x_{n_k}=A
    $$

#### 推论 1.2.7

若某数列有两个取不同极限的子数列，则该数列**发散**。

### 定理 1.2.9（有界性）

!!! info ""
    若 $\lim\limits_{x \to x_0}f(x)=A$，则存在点 $x_0$ 的某去心邻域 $\mathring{N}_{\delta_0}(x_0)$ 使得 $f(x)$ 在该邻域内有界。

### 定理 1.2.10（唯一性）

!!! info ""
    若 $\lim\limits_{x \to x_0}f(x)=A,\, \lim\limits_{x \to x_0}f(x)=B$，则 $A=B$。

证明：反证法。

若 $A\ne B$，取 $\varepsilon=\dfrac{\left\lvert B-A \right\rvert}{2}>0$。

由 $\lim\limits_{x \to x_0}f(x)=A$ 与 $\lim\limits_{x \to x_0}f(x)=B$ 可得，$\exist_{\delta > 0}$，当 $0<\left\lvert x-x_0 \right\rvert<\delta$ 时，有 $\left\lvert f(x)-A \right\rvert<\varepsilon,\,\left\lvert f(x)-B \right\rvert<\varepsilon$，但 $2 \varepsilon=\left\lvert B-A \right\rvert=\left\lvert B-f(x)+f(x)-A \right\rvert\le \left\lvert f(x)-B \right\rvert+\left\lvert f(x)-A \right\rvert<2 \varepsilon$，矛盾！

### 定理 1.2.14

!!! info ""
    $\lim\limits_{x \to x_0}f(x)=A\iff $ 对任何数列 $\left\lbrace x_n \right\rbrace$，且 $x_n$ 在 $x_0$ 的某去心邻域内，$\lim\limits_{n \to \infty}x_n=x_0$，有 $\lim\limits_{n \to \infty}f(x_n)=A$。

证明：

$\implies $：

设 $\lim\limits_{x \to x_0}f(x)=A$，则 $\forall_{\varepsilon>0},\,\exist_{\delta > 0}$，当 $0<\left\lvert x-x_0 \right\rvert<\delta$ 时，有 $\left\lvert f(x)-A \right\rvert<\varepsilon$。

因为 $\lim\limits_{n \to \infty}x_n=x_0$，所以 $\forall_{\delta > 0},\,\exist_{N \in \N}$，当 $n>N$ 时，有 $\left\lvert x_n-x_0 \right\rvert<\delta$。

于是当 $n>N$ 时，有 $\left\lvert f(x_n)-A \right\rvert<\varepsilon$，即 $\lim\limits_{n \to \infty}f(x_n)=A$。

$\impliedby $：

用反证法证明。

设 $\lim\limits_{x \to x_0}f(x)\ne A$，则 $\exist_{\varepsilon_0>0}$，$\forall_{\delta > 0},\,\exist_{\bar{x}_n \in \mathring{N}_{\delta}(x_0)}$，有 $\left\lvert f(\bar{x}_n)-A \right\rvert \ge \varepsilon_0$。

取 $\delta=\dfrac{1}{n}$，因为 $0<\left\lvert \bar{x}_n-x_0 \right\rvert<\delta$，所以 $\lim\limits_{n \to \infty}\bar{x}_n=x_0$。

但 $\lim\limits_{n \to \infty}f(\bar{x}_n)\ne A$，与条件矛盾！

!!! note ""
    $\delta=\dfrac{1}{n}$ 的选取是为了使得 $\lim\limits_{n \to \infty}\delta=0$，从而使得 $\lim\limits_{n \to \infty}\bar{x}_n=x_0$。


#### 推论 1.2.15

!!! info ""
    设 $x_0 \in\R$，$\mathring{N}(x_0)$ 为 $x_0$ 的某去心邻域。若存在 $x_n ,\, y_n \in \mathring{N}(x_0)$，且 $\lim\limits_{n \to \infty}x_n=x_0 ,\, \lim\limits_{n \to \infty}y_n =x_0$，使得 $\lim\limits_{n \to \infty }f(x_n)=A,\,\lim\limits_{n \to \infty }f(y_n)=B$，且 $A\ne B$，则 $\lim\limits_{x \to x_0}f(x)$ 不存在。

!!! memo ""
    这周要赶工英语听说 Presentation，先到这里。等我应付完再来补笔记。

    好了，我应付过了。还好没忘词，一看人就紧张，全程眼神四处乱飞就是不看人。

### 定理 1.2.21

!!! info ""
    $\lim\limits_{x \to x_0}f(x)=A\iff f(x)=A+\alpha(x),\, \lim\limits_{x \to x_0}\alpha(x) =0$。

证明：

$\implies $：

设 $\lim\limits_{x \to x_0}f(x)=A$，则 $\forall_{\varepsilon>0},\,\exist_{\delta > 0}$，当 $0<\left\lvert x-x_0 \right\rvert<\delta$ 时，有 $\left\lvert f(x)-A \right\rvert<\varepsilon$。

令 $\alpha(x)=f(x)-A$，则 $\left\lvert \alpha(x) \right\rvert<\varepsilon$，即 $\lim\limits_{x \to x_0}\alpha(x) =0$。

$\impliedby $：

若 $f(x)=A+\alpha(x),\, \lim\limits_{x \to x_0}\alpha(x)=0$，则 $\forall_{\varepsilon>0},\,\exist_{\delta > 0}$，当 $0<\left\lvert x-x_0 \right\rvert<\delta$ 时，有 $\left\lvert \alpha(x) \right\rvert<\varepsilon$。

而 $\alpha(x)=f(x)-A$，所以 $\left\lvert f(x)-A \right\rvert<\varepsilon$，即 $\lim\limits_{x \to x_0}f(x)=A$。

### 柯西准则

#### 定理 1.2.27（数列极限的柯西准则）

!!! info ""
    数列 $\left\lbrace x_n \right\rbrace$ 收敛的充要条件是：$\forall_{\varepsilon>0},\,\exist_{N \in \N}$，当 $m,\,n>N$ 时，有 $\left\lvert x_m-x_n \right\rvert<\varepsilon$。

#### 定理 1.2.28（函数极限的柯西准则）

!!! info ""
    $\lim\limits_{x \to x_0}f(x)=A\iff \forall_{\varepsilon>0},\,\exist_{\delta > 0}$，当 $x,\,y \in \mathring{N}_{\delta}(x_0)$ 时，有 $\left\lvert f(x)-f(y) \right\rvert<\varepsilon$。

!!! memo ""
    我夹逼准则、单调有界准则都用过，但柯西准则一直没用过，因此记忆也不是很深刻。


### 无穷小量

#### 定义 1.2.14

!!! info ""
    若 $\lim \dfrac{\alpha}{\beta}=0$，则称 $\alpha$ 是 $\beta$ 的**高阶无穷小**，记作 $\alpha=o(\beta)$。

    若 $\lim \dfrac{\alpha}{\beta^k}=c\quad\left(c\ne 0,\,k>0\right)$，则称 $\alpha$ 是 $\beta$ 的 **$k$ 阶无穷小**。

    若 $k=1$，则称 $\alpha$ 是 $\beta$ 的**同阶无穷小**。

    若 $k=c=1$，则称 $\alpha$ 是 $\beta$ 的**等价无穷小**，记作 $\alpha \sim \beta$。

#### 定义 1.2.15

!!! info ""
    在某极限过程中，选取 $\beta$ 为*基准无穷小*，若 $\alpha \sim c \beta^k\quad\left(c\ne 0,\, k>0\right)$，则称 $c \beta^k$ 为无穷小 $\alpha$ 的**主要部分**，简称 $\alpha$ 的**主部**。

## 其它

### 1.

!!! quote 证明
    $$
    \lim\limits_{n \to \infty} \dfrac{\sum\limits_{i=1}^{n}x_i}{n}=\lim\limits_{n \to \infty}x_n
    $$

$\forall_{\varepsilon>0},\, \exist_{N \in \N},\, \forall_{n>N},\, \left\lvert x_n - \lim\limits_{n \to \infty}x_n\right\rvert<\dfrac{\varepsilon}{2}$。

而

$$
\begin{aligned}
    \left\lvert \dfrac{\sum\limits_{i=1}^{n}x_i}{n} - \lim\limits_{n\to \infty}x_n  \right\rvert &\le \left\lvert \dfrac{\sum\limits_{i=1}^{N}x_i}{n} \right\rvert + \left\lvert \dfrac{\sum\limits_{i=N+1}^{n}x_i}{n} - \lim\limits_{n\to \infty}x_n \right\rvert \\
    &< \left\lvert \dfrac{\sum\limits_{i=1}^{N}x_i}{n}  \right\rvert + \dfrac{\varepsilon}{2} \\
\end{aligned}
$$

而 $\displaystyle \sum\limits_{i=1}^{N}x_i$ 为常数，有 $\exist_{N'>N},\, \forall_{n>N'},\, \left\lvert \dfrac{\sum\limits_{i=1}^{N}x_i}{n}  \right\rvert < \dfrac{\varepsilon}{2}$。

综上即有

$$
\left\lvert \dfrac{\sum\limits_{i=1}^{n}x_i}{n} - \lim\limits_{n\to \infty}x_n  \right\rvert < \varepsilon
$$

即 $\displaystyle \lim\limits_{n \to \infty} \dfrac{\sum\limits_{i=1}^{n}x_i}{n}=\lim\limits_{n \to \infty}x_n$。

### 2.

!!! quote 证明
    $$
    \displaystyle \lim\limits_{n \to \infty}\sqrt[n]{\prod_{i=1}^{n}x_i}= \lim\limits_{n \to \infty}x_n
    $$

若 $\lim\limits_{n \to \infty}x_n=0$，则 $0<\displaystyle \lim\limits_{n \to \infty}\sqrt[n]{\prod_{i=1}^{n}x_i}\le  \dfrac{\sum\limits_{i=1}^{n}x_i}{n}$，夹逼准则知 $\displaystyle \lim\limits_{n \to \infty}\sqrt[n]{\prod_{i=1}^{n}x_i}=0=\lim\limits_{n \to \infty}x_n$。

若 $\lim\limits_{n \to \infty}x_n\ne 0$，则 $\lim\limits_{n \to \infty} \dfrac{\sum\limits_{i=1}^{n}\dfrac{1}{x_i}}{n}=\dfrac{1}{\lim\limits_{n \to \infty}x_n}$。

又 $\dfrac{n}{\sum\limits_{i=1}^{n}\dfrac{1}{x_i}} \le \displaystyle \lim\limits_{n \to \infty}\sqrt[n]{\prod_{i=1}^{n}x_i}<\dfrac{\sum\limits_{i=1}^{n}x_i}{n}$，夹逼准则知 $\displaystyle \lim\limits_{n \to \infty}\sqrt[n]{\prod_{i=1}^{n}x_i}=\lim\limits_{n \to \infty}x_n$。

### 3.

!!! quote ""
    $a_i>0 \;\not\nobreak\!\!\!\!\implies \lim\limits_{n \to \infty}a_n>0$

可能为 $\lim\limits_{n \to \infty}a_n$ 不存在，或 $\lim\limits_{n \to \infty}a_n=0$（如 $a_n=\dfrac{1}{n}$）。
