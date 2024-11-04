---
layout: post
title: 谓词逻辑初步
date: 2024-03-07 09:58:48
updated: 2024-03-31 11:16:00
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

$$
\forall n\biggl(\operatorname{isEven}(n) \land\bigl(n>2\bigr) \rightarrow \exists m \exists k\Bigl(\operatorname{isPrime}(m) \land \operatorname{isPrime}(k) \land\bigl(n=m+k\bigr)\Bigr)\biggr)
$$

哥德巴赫猜想无法用命题逻辑表达，因为 $n$ 等是变量。

**谓词**（Predicate）
- 一元谓词 $P(x)$：给定 $x$，$P(x)$ 为真或假。
- 二元谓词 $Q(x,y)$：给定 $x$ 和 $y$，$Q(x,y)$ 为真或假。
- ……

原子陈述
- $P(t_1, \cdots, t_n)$
- 其中 $P$ 是 $n$ 元谓词，$t_1, \cdots, t_n$ 是常量、变量或函数取值

**逻辑公式**（陈述，Formula）
- 原子陈述是逻辑公式
- 若 $P$ 是逻辑公式，$x$ 是自由变量，则 $\forall x\, P$ 和 $\exists x\, P$ 是逻辑公式
- 若 $P$ 和 $Q$ 是逻辑公式，则 $\lnot P,\, P \land Q,\, P \lor Q,\, P \to Q$ 是逻辑公式

!!! Note ""
    量词的优先级高于其它逻辑运算符。

- 约束变元
    - $\forall x \exists y (y > x)$（即 $\forall x (\exists y (y > x))$）中，$x, y$ 是约束变元
- 自由变元
    - $\exists (y > x) \land (x + 2 > y)$ 中，$x$ 与后面的 $y$ 是自由变元（后面是自由变元，因为前面的 $\exists $ 作用不到后面的 $y$）
- 量词作用域
    - $\forall x \exists y (y > x)$ 中，$\forall x$ 的作用域是 $(\exists y (y > x))$，$\exists y$ 的作用域是 $(y > x)$
- 重命名（对约束变元）
    $\exists (y > x) \land (x + 2 > y) \equiv \exists z (z > x) \land (x + 2 > y)$

量词：
- **全称量词** $\forall x \, P(x)$：对所有 $x$，$P(x)$ 为真
- **存在量词** $\exists x \, P(x)$：存在 $x$，使得 $P(x)$ 为真

多个量词并用：
- $\forall x \forall y \, P(x, y) \equiv \forall y \forall x \, P(x, y)$
- $\exists x \exists y \, P(x, y) \equiv \exists y \exists x \, P(x, y)$
- $\forall x \exists y \, P(x, y) \not\equiv \exists y \forall x \, P(x, y)$

常用逻辑等价式/蕴含式（$R$ 中不含自由变量 $x$）

!!! note ""
    - $\lnot \forall x \, P(x) \equiv \exists x \, \lnot P(x)$
    - $\lnot \exists x \, P(x) \equiv \forall x \, \lnot P(x)$

!!! note ""
    - $\forall x \bigl(P(x) \land Q(x)\bigr) \equiv \forall x \, P(x) \land \forall x \, Q(x)$
    - $\exists x \bigl(P(x) \lor Q(x)\bigr) \equiv \exists x \, P(x) \lor \exists x \, Q(x)$

!!! note ""
    - $\forall x \, P(x) \lor \forall x \, Q(x) \models \forall x \bigl(P(x) \lor Q(x)\bigr)$（奇偶）
    - $\exists x \bigl(P(x) \land Q(x)\bigr) \models \exists x \, P(x) \land \exists x \, Q(x)$ 

!!! note ""
    - $\forall x \bigl(P(x) \lor R\bigr) \equiv \bigl(\forall x \, P(x)\bigr) \lor R$
    - $\exists x \bigl(P(x) \land R\bigr) \equiv \bigl(\exists x \, P(x)\bigr) \land R$

!!! note ""
    - $\forall x \bigl(R \to P(x)\bigr) \equiv R \to \forall x \, P(x)$（即 $\forall x \bigl(\lnot R \lor P(x)\bigr) \equiv \lnot R \lor \bigl(\forall x \, P(x)\bigr)$）
    - $\exists x \bigl(R \to P(x)\bigr) \equiv R \to \exists x \, P(x)$

!!! note ""
    - $\forall x \bigl(P(x) \to R\bigr) \equiv \bigl(\exists x \, P(x)\bigr) \to R$
    - $\exists x \bigl(P(x) \to R\bigr) \equiv \bigl(\forall x \, P(x)\bigr) \to R$（即 $\exists x \bigl(P(x) \to R\bigr) \equiv \bigl(\exists x \lnot P(x)\bigr) \lor R \equiv \lnot \bigl(\forall x \, P(x)\bigr) \lor R$）

**前束范式**（Prenex Normal Form）
$$
\forall x\left(x \leq 0 \lor \exists y\left(y>0 \land x=y^{2}\right)\right) \equiv \forall x \exists y\left(x \leq 0 \lor\left(y>0 \land x=y^{2}\right)\right)
$$

量词相关自然演绎规则

| | 引入 | 消去 |
| :-: | :-: | :-: |
| **全称量词** $\forall $ | $ \begin{aligned} \boxed{\begin{aligned} &\kern{1.2em}x_0\\ &\kern{1.6em}\vdots\\ &\varphi[x_0 / x] \end{aligned}}\\ \hline \forall x \,\varphi \kern{1em} \end{aligned} \; \nobreak \raisebox{-2.4em}{\(\forall x \, \nobreak \mathrm{i.}\)} $ |  $ \begin{aligned} \forall x \,\varphi \hspace{0.25em}\\ \hline \varphi[t / x] \end{aligned} \; \nobreak \forall x \, \nobreak \mathrm{e.} $ |
| **存在量词** $\exists $ | $ \begin{aligned} \varphi[t / x] \\ \hline \exists x \,\varphi \kern{0.25em} \end{aligned} \, \nobreak \exists x \, \nobreak \mathrm{i.} $ | $ \begin{aligned} \exists x \,\varphi\quad\boxed{\begin{aligned} &x_0\quad \varphi[x_0 / x] \\ &\kern{2.7em}\vdots \\ &\kern{2.45em}\chi \end{aligned}} \\ \hline \chi \kern{3.7em} \end{aligned} \; \nobreak \raisebox{-2.25em}{\(\exists x \, \nobreak \mathrm{e.}\)} $ |
