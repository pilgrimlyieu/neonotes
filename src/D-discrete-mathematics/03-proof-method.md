---
layout: post
title: 证明方法
date: 2024-03-12 09:28:27
updated: 2024-03-14 18:49:27
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 引言

术语：
- **定理**（Theorem）：能够被证明为真的陈述，通常是比较重要的陈述。
- **证明**（Proof）：表明陈述（定理）为真的有效论证。
    - （当前）定理的前提
    - 术语的定义
    - 公理（假定）
    - 已经证明的定理（推论、命题、引理）
- **猜想**（Conjecture）：尚未被证明为真的陈述，通常是比较重要的陈述。尚未有效论证，也没有被证伪。
- **引理**（Lemma）：用于证明定理的辅助陈述。
- **推论**（Corollary）：由定理推出的陈述。

## 证明方法

### 逆否命题法（Proof by Contrapositive）

!!! info ""
    $$
    \varphi \to \psi \equiv \lnot \psi \to \lnot \varphi
    $$

要证明 $\varphi \to \psi$：
1. 假设 $\lnot \psi$ 为真。
2. 推出 $\lnot \varphi$ 为真。
3. 从而推出 $\varphi \to \psi$ 为真。

### 归谬法（Proof by Contradiction）

!!! info ""
    $$
    \varphi \equiv \lnot \varphi \to \bot
    $$

要证明 $\varphi$：
1. 假设 $\lnot \varphi$ 为真。
2. 导出矛盾 $\bot$（即 $\psi \land \lnot \psi$）。
3. 从而推出 $\varphi$ 为真。

### 等价性证明

!!! info ""
    $$
    \bigwedge\limits_{1 \le i < j \le n} (\varphi_i \leftrightarrow \varphi_j) \equiv \left( \bigwedge_{i = 1}^{n - 1} (\varphi_i \to \varphi_{i + 1}) \right) \land (\varphi_n \to \varphi_1)
    $$

要证明 $n$ 个命题 $\varphi_1, \varphi_2, \ldots, \varphi_n$ 两两等价：
1. $\varphi_1 \vdash \varphi_2$。
2. $\cdots$
3. $\varphi_{n - 1} \vdash \varphi_n$。
4. $\varphi_n \vdash \varphi_1$。
5. 从而推出 $\bigwedge\limits_{1 \le i < j \le n} (\varphi_i \leftrightarrow \varphi_j)$ 为真。

### 存在性证明

- 构造性证明
    - 如「存在这样的正整数，有两种方式表示为正整数的立方和」，有 $1729 = 10^3 + 9^3 = 12^3 + 1^3$。
- 非构造性证明
    - 如「存在无理数 $x,\, y$ 使得 $x^y$ 为有理数」，有 $\sqrt{2}^{\sqrt{2}},\, \left(\sqrt{2}^{\sqrt{2}}\right)^{\sqrt{2}}$ 中至少有一个为有理数。

### 分情形证明

!!! info ""
    $$
    \bigvee_{i = 1}^n \varphi_i \to \psi \equiv \bigwedge_{i = 1}^n (\varphi_i \to \psi)
    $$

要证明 $\displaystyle \bigvee_{i = 1}^n \varphi_i \to \psi$：
1. $\varphi_1 \vdash \psi$
2. $\cdots$
3. $\varphi_n \vdash \psi$
4. 从而推出 $\displaystyle \bigvee_{i = 1}^n \varphi_i \to \psi$ 为真。

### 唯一性证明

存在一个且仅有一个 $x$ 使得 $P(x)$ 成立，记作 $\exists! x \, P(x)$。
- $\exists x(P(x) \land \forall y (y \ne x \to \lnot P(y)))$
- $\exists x \, P(x) \land \forall y \forall z (P(y) \land P(z) \to y = z)$

### 找反例

!!! info ""
    $$
    \lnot \forall x \, P(x) \equiv \exists x \, \lnot P(x)
    $$
