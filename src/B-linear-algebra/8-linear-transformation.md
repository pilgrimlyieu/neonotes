---
layout: post
title: 线性变换
date: 2023-12-29 10:06:54
updated: 2024-08-26 16:23:11
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

### 概念

!!! info ""
    设 $V_1,\, V_2$ 是数域 $\mathbb{K}$ 上的线性空间。如果映射 $T\colon V_1 \mapsto V_2$ 满足：（$\dot{\oplus},\, \dot{\otimes}$ 代表 $V_1$ 上的加法和数乘运算，$\ddot{\oplus},\, \ddot{\otimes}$ 代表 $V_2$ 上的加法和数乘运算）
    1. 对任意 $\alpha,\, \beta \in V_1$，有 $T(\alpha \dot{\oplus} \beta) = T(\alpha) \ddot{\oplus} T(\beta)$
    2. 对任意 $\alpha \in V_1$ 和 $\lambda \in \mathbb{K}$，有 $T(\lambda \dot{\otimes} \alpha) = \lambda \ddot{\otimes} T(\alpha)$

    则称 $T$ 是从 $V_1$ 到 $V_2$ 的**线性映射**。$V_1 = V_2 = V$ 时，称 $T$ 是 $V$ 上的**线性变换**。

!!! note 线性映射性质
    1. $T (\theta) = \theta$
    2. $\displaystyle T\left(\sum_{i=1}^n \lambda_i \alpha_i\right) = \sum_{i=1}^n \lambda_i T\left(\alpha_i\right)$
    3. 若 $\alpha_1,\, \alpha_2,\, \cdots \alpha_m$ 线性相关，则 $T(\alpha_1),\, T(\alpha_2),\, \cdots T(\alpha_m)$ 也线性相关（逆命题<u>不成立</u>）

!!! example 线性映射例子
    1. **矩阵**：$\bm{A} \in M_{m \times n}(\R)$，线性映射 $T\colon \R^n \mapsto \R^m$ 定义为 $T(\bm{\alpha}) = \bm{A}\bm{\alpha}$。
    2. **积分**：设 $V_1 = C([a, b]),\, V_2 = \R$，线性映射 $T\colon V_1 \mapsto V_2$ 定义为 $T(f) = \displaystyle \int_a^b f(x) \d x$。
    3. **微分**：设 $V_1 = C^1([a, b]),\, V_2 = C([a, b])$，线性映射 $T\colon V_1 \mapsto V_2$ 定义为 $T(f) = f'$。（$C^1([a, b])$ 表示 $[a, b]$ 上一阶连续可导函数的集合，$C([a, b])$ 表示 $[a, b]$ 上连续函数的集合）
    4. **数乘变换**：$T\colon V \mapsto V$ 定义为 $T(\alpha) = \lambda \alpha$，其中 $\lambda \in \mathbb{K}$。
    5. **恒等变换**（**单位变换**）：$T\colon V \mapsto V$ 定义为 $T(\alpha) = \alpha$。
    6. **零变换**：$T\colon V \mapsto V$ 定义为 $T(\alpha) = \theta$。

!!! note ""
    1. 验证线性映射为**单射**：若 $T(\alpha_1) = T(\alpha_2)$，则 $\alpha_1 = \alpha_2 \iff $ 若 $T(\alpha) = \theta$，则 $\alpha = \theta$。
    2. 验证线性映射为**满射**：对任意 $\beta \in V_2$，总有 $\alpha \in V_1$ 使得 $T(\alpha) = \beta$。

!!! info ""
    设 $V_1,\, V_2$ 是数域 $\mathbb{K}$ 上的线性空间，$T\colon V_1 \mapsto V_2$ 是线性映射。

    $T$ 的**核空间**定义为 $\ker (T) = \{\alpha \in V_1 \mid T(\alpha) = \theta\}$（$\theta$ 为 $V_2$ 的零元）。$T$ 的**像空间**定义为 $\operatorname{Im} (T) = \{T(\alpha) \mid \alpha \in V_1\}$（也可记作 $\mathcal{R}$ `\mathcal{R}`）。

    核空间和像空间都是线性子空间，其中 $\ker(T) \subseteq V_1,\, \operatorname{Im}(T) \subseteq V_2$。

!!! note ""
    对于矩阵线性映射 $T(\bm{\alpha}) = \bm{A}\bm{\alpha}$：
    1. 求 $\operatorname{Im}(T)$ 的基就是找 $\bm{A}$ 的列向量组的极大线性无关组。
    2. 求 $\ker(T)$ 的基就是找齐次方程组 $\bm{A} \bm{x} = \bm{\theta}$ 的基础解系。

### 线性变换的矩阵表示

!!! info ""
    设线性变换 $T\colon \bm{V} \mapsto \bm{V}$，其中线性空间 $\dim \bm{V} = n$，且 $\bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n$ 为 $\bm{V}$ 一组基。则对于任意 $\bm{\alpha} \in \bm{V}$，有

    $$
    \bm{\alpha} = \sum_{i=1}^n x_i \bm{\varepsilon}_i
    $$

    则有

    $$
    T(\bm{\alpha}) = T\left(\sum_{i=1}^n x_i \bm{\varepsilon}_i\right) = \sum_{i=1}^n x_i T(\bm{\varepsilon}_i)
    $$

    即 $T(\bm{\varepsilon}_1),\, T(\bm{\varepsilon}_2),\, \cdots,\, T(\bm{\varepsilon}_n)$ 唯一确定了 $T(\bm{\alpha})$。

    又 $T(\bm{\varepsilon}_i) \in \bm{V}$，从而

    $$
    T(\bm{\varepsilon}_i) = a_{1i} \bm{\varepsilon}_1 + a_{2i} \bm{\varepsilon}_2 + \cdots + a_{ni} \bm{\varepsilon}_n
    $$

    从而

    $$
    \begin{bmatrix}
        T(\bm{\varepsilon}_1) & T(\bm{\varepsilon}_2) & \cdots & T(\bm{\varepsilon}_n)
    \end{bmatrix}=
    \begin{bmatrix}
        \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
    \end{bmatrix}
    \underbrace{\begin{bmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
        a_{21} & a_{22} & \cdots & a_{2n} \\
        \vdots & \vdots & \ddots & \vdots \\
        a_{n1} & a_{n2} & \cdots & a_{nn}
    \end{bmatrix}}_{\bm{A}}
    $$

    $\bm{A}$ 称为<u>线性变换 $T$ 在基 $\bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n$ 下的矩阵</u>。

!!! note ""
    对任意 $\bm{\alpha} \in \bm{V}$，若 $\bm{\alpha}$ 在基 $\bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n$ 下的坐标为 $\bm{x}$，则 $T(\bm{\alpha})$ 在基 $\bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n$ 下的坐标为 $\bm{A}\bm{x}$。其中 $\bm{A}$ 为线性变换 $T$ 在基 $\bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n$ 下的矩阵。

    ---

    $$
    \begin{aligned}
        T(\bm{\alpha}) &= \begin{bmatrix}
            T(\bm{\varepsilon}_1) & T(\bm{\varepsilon}_2) & \cdots & T(\bm{\varepsilon}_n)
        \end{bmatrix}
        \begin{bmatrix}
            x_1 \\
            x_2 \\
            \vdots \\
            x_n
        \end{bmatrix} \\
        &= \begin{bmatrix}
            \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
        \end{bmatrix}
        \begin{bmatrix}
            a_{11} & a_{12} & \cdots & a_{1n} \\
            a_{21} & a_{22} & \cdots & a_{2n} \\
            \vdots & \vdots & \ddots & \vdots \\
            a_{n1} & a_{n2} & \cdots & a_{nn}
        \end{bmatrix}
        \begin{bmatrix}
            x_1 \\
            x_2 \\
            \vdots \\
            x_n
        \end{bmatrix} \\
        &= \begin{bmatrix}
            \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
        \end{bmatrix}
        \bm{A} \bm{x}
    \end{aligned}
    $$

!!! note ""
    设 $n$ 维线性空间 $\bm{V}$ 有两组基 $\bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n$ 和 $\bm{\omega}_1,\, \bm{\omega}_2,\, \cdots,\, \bm{\omega}_n$，线性变换 $T\colon \bm{V} \mapsto \bm{V}$ 在这两组基下的矩阵分别为 $\bm{A}$ 和 $\bm{B}$，由 $\bm{\omega}_1,\, \bm{\omega}_2,\, \cdots,\, \bm{\omega}_n$ 到 $\bm{\varepsilon}_1,\, \bm{\varepsilon}_2,\, \cdots,\, \bm{\varepsilon}_n$ 的过渡矩阵为 $\bm{P}$，则有

    $$
    \bm{B} = \bm{P}^{-1} \bm{A} \bm{P}
    $$

    即线性变换 $T$ 在不同基下的矩阵相似。

    ---

    证明：

    已知

    $$
    \begin{aligned}
        \begin{bmatrix}
            \bm{\omega}_1 & \bm{\omega}_2 & \cdots & \bm{\omega}_n
        \end{bmatrix} &=
        \begin{bmatrix}
            \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
        \end{bmatrix} \bm{P} \\
        \begin{bmatrix}
            T(\bm{\varepsilon}_1) & T(\bm{\varepsilon}_2) & \cdots & T(\bm{\varepsilon}_n)
        \end{bmatrix} &=
        \begin{bmatrix}
            \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
        \end{bmatrix} \bm{A} \\
        \begin{bmatrix}
            T(\bm{\omega}_1) & T(\bm{\omega}_2) & \cdots & T(\bm{\omega}_n)
        \end{bmatrix} &=
        \begin{bmatrix}
            \bm{\omega}_1 & \bm{\omega}_2 & \cdots & \bm{\omega}_n
        \end{bmatrix} \bm{B}
    \end{aligned}
    $$

    记 $\bm{P} = [c_{ij}]_{m \times n}$，则

    $$
    \begin{bmatrix}
        T(\bm{\omega}_1) & T(\bm{\omega}_2) & \cdots & T(\bm{\omega}_n)
    \end{bmatrix} =
    \begin{bmatrix}
        \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
    \end{bmatrix} \bm{P} \bm{B}
    $$

    从而

    $$
    \begin{aligned}
        T(\bm{\omega}_i) &= T\left(\begin{bmatrix}
            \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
        \end{bmatrix} \begin{bmatrix}
            c_{1i} \\
            c_{2i} \\
            \vdots \\
            c_{ni}
        \end{bmatrix}\right) \\
        &= T\left(\sum_{k=1}^n c_{ki} \bm{\varepsilon}_k\right) \\
        &= \begin{bmatrix}
            T(\bm{\varepsilon}_1) & T(\bm{\varepsilon}_2) & \cdots & T(\bm{\varepsilon}_n)
        \end{bmatrix} \begin{bmatrix}
            c_{1i} \\
            c_{2i} \\
            \vdots \\
            c_{ni}
        \end{bmatrix}
    \end{aligned}
    $$

    得

    $$
    \begin{aligned}
        \begin{bmatrix}
            T(\bm{\omega}_1) & T(\bm{\omega}_2) & \cdots & T(\bm{\omega}_n)
        \end{bmatrix} &=
        \begin{bmatrix}
            T(\bm{\varepsilon}_1) & T(\bm{\varepsilon}_2) & \cdots & T(\bm{\varepsilon}_n)
        \end{bmatrix} \bm{P} \\
        &= \begin{bmatrix}
            \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
        \end{bmatrix} \bm{A} \bm{P} \\
    \end{aligned}
    $$

    综合有

    $$
    \begin{bmatrix}
        \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
    \end{bmatrix} \bm{P} \bm{B} =
    \begin{bmatrix}
        \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
    \end{bmatrix} \bm{A} \bm{P}
    $$

    则

    $$
    \bm{P} \bm{B} = \bm{A} \bm{P}
    $$

    即

    $$
    \bm{B} = \bm{P}^{-1} \bm{A} \bm{P}
    $$

!!! note ""
    $$
    \begin{aligned}
        \begin{bmatrix}
            T(\bm{\omega}_1) & T(\bm{\omega}_2) & \cdots & T(\bm{\omega}_n)
        \end{bmatrix} &=
        T(\begin{bmatrix}
            \bm{\omega}_1 & \bm{\omega}_2 & \cdots & \bm{\omega}_n
        \end{bmatrix}) \\
        &= T(\begin{bmatrix}
            \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
        \end{bmatrix} \bm{P}) \\
        &= T(\begin{bmatrix}
            \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
        \end{bmatrix}) \bm{P} \\
        &= \begin{bmatrix}
            T(\bm{\varepsilon}_1) & T(\bm{\varepsilon}_2) & \cdots & T(\bm{\varepsilon}_n)
        \end{bmatrix} \bm{P} \\
    \end{aligned}
    $$

### 总结

对 $\bm{V} = V(\mathbb{K})$ 有：
- **基**：$\bm{\omega}_1 ,\, \cdots \bm{\omega}_n \xrightarrow{\bm{P}} \bm{\varepsilon}_1 ,\, \cdots \bm{\varepsilon}_n$
- $\bm{\alpha} \in \bm{V}$：$\bm{x} \in \R^n \xrightarrow{\bm{P}^{-1}} \bm{y} = \bm{P}^{-1} \bm{x} \in \R^n$
- **变换 $T$**：$\bm{A} \xrightarrow{T} \bm{B} = \bm{P}^{-1} \bm{A} \bm{P}$

!!! note 子空间的交
    已知

    $$
    \left\lbrace\begin{aligned}
        \bm{W}_1 &= \span \left\lbrace  \bm{\alpha}_1 ,\,  \cdots,\, \bm{\alpha}_m \right\rbrace \\
        \bm{W}_2 &= \span \left\lbrace  \bm{\beta}_1 ,\, \cdots,\, \bm{\beta}_n \right\rbrace
    \end{aligned}\right.
    $$

    则有 $\bm{W}_1 \cap \bm{W}_2 = \left\lbrace \bm{\xi}\colon \bm{\xi} \in \bm{W}_1 \land \bm{\xi} \in \bm{W}_2 \right\rbrace$，即任意一个 $\bm{\xi}$ 都有

    $$
    \bm{\xi} = \sum_{i = 1}^{m} \lambda_{i} \bm{\alpha}_i = \sum_{j = 1}^{n} \mu_{j} \bm{\beta}_j
    $$

    从而有

    $$
    \sum_{i = 1}^{m} \lambda_{i} \bm{\alpha}_i - \sum_{j = 1}^{n} \mu_{j} \bm{\beta}_j = \bm{\theta}
    $$

    矩阵形式为

    $$
    \begin{bmatrix}
        \bm{\alpha}_1 & \cdots & \bm{\alpha}_m & -\bm{\beta}_1 & \cdots & -\bm{\beta}_n
    \end{bmatrix}
    \begin{bmatrix}
        \lambda_1 \\ \vdots \\ \lambda_m \\ \mu_1 \\ \vdots \\ \mu_n
    \end{bmatrix}
    = \bm{\theta}
    $$

    解齐次线性方程组，得到基础解系，即为 $\bm{W}_1 \cap \bm{W}_2$ 的一组基。对基础解系任意一个向量，任选一组基即可，即下式中上下任选一个基即可。

    $$
    \begin{bmatrix}
        \lambda_1 \\ \vdots \\ \lambda_m \\ \hline \mu_1 \\ \vdots \\ \mu_n
    \end{bmatrix}
    $$


!!! note 子空间的和
    实质上是求出 $\left\lbrace \bm{\alpha}_1 ,\,  \cdots,\, \bm{\alpha}_m ,\, \bm{\beta}_1 ,\, \cdots,\, \bm{\beta}_n \right\rbrace$ 的一个极大线性无关组，即为 $\bm{W}_1 + \bm{W}_2$ 的一组基。

    一样是解上面的齐次方程组，最后从行简化梯形矩阵中选出极大线性无关组即可。

### 实战

!!! example ""
    定义

    $$
    f(t) = \begin{cases}
        0, & t = 2k\pi,\, k \in \Z \\
        \dfrac{\sin \left(\frac{n}{2} t\right) \sin \left(\frac{n+1}{2}t\right)}{\sin \frac{t}{2}}, & t \ne 2k\pi,\, k \in \Z
    \end{cases}
    $$
    
    求 $f(t)$ 在基 $\sin t,\, \sin 2t,\, \cdots,\, \sin nt$ 下的坐标。

    ---

    设

    $$
    f(t) = \sum_{k = 1}^{n} c_{k} \sin kt
    $$
    
    则有

    $$
    f(t) \sin mt = \sum_{k = 1}^{n} c_{k} \sin kt \sin mt
    $$
    
    两边从 $0$ 到 $2 \pi$ 积分，得

    $$
    \begin{aligned}
        \int_{0}^{2 \pi} f(t) \sin mt\d t &= \sum_{k = 1}^{n} c_{k} \int_{0}^{2 \pi} \sin kt \sin mt\d t \\
        &= \pi c_{m}
    \end{aligned}
    $$
    
    从而

    $$
    c_{m} = \frac{1}{\pi} \int_{0}^{2 \pi} f(t) \sin mt\d t
    $$
    
    余计算略。

    实际上有

    $$
    c_1 = c_2 = \cdots = c_n = 1
    $$
    
    因为记

    $$
    S = \sin t + \sin 2t + \cdots + \sin nt
    $$
    
    则有

    $$
    S \sin \tfrac{1}{2}t = \left(\cos \tfrac{1}{2}t - \cos \tfrac{3}{2}t\right) + \left(\cos \tfrac{3}{2}t - \cos \tfrac{5}{2}t\right) + \cdots + \left(\cos \tfrac{2n - 1}{2}t - \cos \tfrac{2n + 1}{2}t\right)
    $$
    
    从而有 $S = f(t)$。

!!! note 线代课学微积分
    对积分

    $$
    I = \int_{0}^{2 \pi} \sin kt \cdot \sin mt\d t
    $$

    其中 $k$ 和 $m$ 为正整数，且 $k \le m$，则

    $$
    I = \begin{cases}
        \pi, & k = m \\
        0, & k \ne m
    \end{cases}
    $$
    
    ---

    证明：

    $k \ne m$ 时，有

    $$
    \begin{aligned}
        I &= \int_{0}^{2 \pi} \sin kt \cdot \sin mt\d t \\
        &= \frac{1}{2} \int_{0}^{2 \pi} \left[\cos(k - m)t - \cos(k + m)t\right]\d t \\
        &= \frac{1}{2} \left[\frac{\sin(k - m)t}{k - m} - \frac{\sin(k + m)t}{k + m}\right]\as_{0}^{2 \pi} \\
        &= 0
    \end{aligned}
    $$
    
    而当 $k = m$ 时，有

    $$
    \begin{aligned}
        I &= \int_{0}^{2 \pi} \sin^{2} kt\d t = \pi\\ 
        &= \frac{1}{2} \int_{0}^{2 \pi} \left(1 - \cos 2kt\right)\d t \\
        &= \frac{1}{2} \left(t - \frac{\sin 2kt}{2k}\right)\as_{0}^{2 \pi} \\
        &= \pi
    \end{aligned}
    $$

!!! memo ""
    临近大二进行的补充，一学期没学线代，其实早已忘光了，所以接下来只是无情的复制机器。

### 特征值和特征向量

$n$ 维线性空间 $\bm{V}$ 上某个线性变换 $T$ 在不同基底下的矩阵是不同的。

因此想要找到一组基底，使得 $T$ 在这组基底下的矩阵具有尽可能简单的形式（对角矩阵）。

即找到一组基底

$$
\bm{\varepsilon}_1 ,\, \bm{\varepsilon}_2 ,\, \cdots ,\, \bm{\varepsilon}_n
$$

使得

$$
\begin{bmatrix}
    T(\bm{\varepsilon}_1) & T(\bm{\varepsilon}_2) & \cdots & T(\bm{\varepsilon}_n)
\end{bmatrix} = \begin{bmatrix}
    \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
\end{bmatrix} \begin{bmatrix}
    \lambda_1 & 0 & \cdots & 0 \\
    0 & \lambda_2 & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & \lambda_n
\end{bmatrix}
$$

亦即

$$
\left\lbrace\begin{aligned}
    T(\bm{\varepsilon}_1) &= \lambda_1 \bm{\varepsilon}_1 \\
    T(\bm{\varepsilon}_2) &= \lambda_2 \bm{\varepsilon}_2 \\
    &\cdots \\
    T(\bm{\varepsilon}_n) &= \lambda_n \bm{\varepsilon}_n
\end{aligned}\right.
$$

!!! info ""
    设 $\bm{V} = V(\mathbb{K})$，$T$ 是 $\bm{V}$ 上的一个线性变换。若对 $\mathbb{K}$ 中的一个数 $\lambda$，存在 $\bm{V}$ 中的一个非零向量 $\bm{\xi}$，使得

    $$
    T(\bm{\xi}) = \lambda \bm{\xi}
    $$
    
    则称 $\lambda$ 是 $T$ 的一个**特征值**，$\bm{\xi}$ 是 $T$ 的属于 $\lambda$ 的**特征向量**。

!!! note ""
    设 $\bm{V} = V(\mathbb{K})$，$T$ 是 $\bm{V}$ 上的一个线性变换。则 $T$ 的属于特征值 $\lambda$ 的所有特征向量与零向量共同构成了 $\bm{V}$ 的一个子空间，称为<u>线性变换 $T$ 对应于特征值 $\lambda$ 的**特征子空间**</u>，记作

    $$
    \bm{V}_{\lambda} = \left\lbrace \bm{\xi} \in \bm{V} \mid T(\bm{\xi}) = \lambda \bm{\xi} \right\rbrace
    $$

    <!-- {{{ 证明 -->
    <details>
    <summary>证明</summary>
    
    任取 $\bm{\xi}_1, \bm{\xi}_2 \in \bm{V}_{\lambda}$，当 $\bm{\xi}_1 + \bm{\xi}_2 \ne \bm{\theta}$ 时，因

    $$
    \begin{aligned}
        T(\bm{\xi}_1 + \bm{\xi}_2) &= T(\bm{\xi}_1) + T(\bm{\xi}_2) \\
        &= \lambda \bm{\xi}_1 + \lambda \bm{\xi}_2 \\
        &= \lambda (\bm{\xi}_1 + \bm{\xi}_2)
    \end{aligned}
    $$
    
    即 $\bm{\xi}_1 + \bm{\xi}_2 \in \bm{V}_{\lambda}$。

    当 $\bm{\xi} \in \bm{V}_{\lambda}$，$\lambda \in \mathbb{K}$ 时，对任意 $k \in \mathbb{K}, k \ne 0$，有

    $$
    \begin{aligned}
        T(k \bm{\xi}) &= k T(\bm{\xi}) \\
        &= k \lambda \bm{\xi} \\
        &= \lambda (k \bm{\xi})
    \end{aligned}
    $$
    
    即 $k \bm{\xi} \in \bm{V}_{\lambda}$。

    说明 $\bm{V}_{\lambda}$ 对加法和数乘封闭，故 $\bm{V}_{\lambda}$ 是 $\bm{V}$ 的一个子空间。
    
    </details>
    <!-- }}} -->

为了表示 $\bm{V}_{\lambda}$ 中全部向量，需要求得 $\bm{V}_{\lambda}$ 的一组基。

可以先求出 $T$ 的所有特征值，再求出每个特征值对应的线性无关的特征向量。

线性空间 $\bm{V} = V(\mathbb{K})$ 上的线性变换 $T$ 在选定的一组基 $\bm{\varepsilon}_1 ,\, \bm{\varepsilon}_2 ,\, \cdots ,\, \bm{\varepsilon}_n$ 下的矩阵为 $\bm{A} = [a_{ij}]_{n}$，即

$$
\begin{bmatrix}
    T(\bm{\varepsilon}_1) & T(\bm{\varepsilon}_2) & \cdots & T(\bm{\varepsilon}_n)
\end{bmatrix} = \begin{bmatrix}
    \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
\end{bmatrix} \bm{A}
$$

设 $\lambda \in \mathbb{K}$ 是 $T$ 的一个特征值，$\bm{\xi}$ 是 $T$ 对应于 $\lambda$ 的一个特征向量，即

$$
T(\bm{\xi}) = \lambda \bm{\xi},\quad \bm{\xi} \ne \bm{\theta}
$$

令

$$
\begin{aligned}
    \bm{\xi} &= \begin{bmatrix}
        \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
    \end{bmatrix} \bm{x}\\ 
    \bm{x} &= \begin{bmatrix}
        x_1 & x_2 & \cdots & x_n
    \end{bmatrix}^\intercal
\end{aligned}
$$

则

$$
\begin{aligned}
    T \bm{\xi} &= T\left(\begin{bmatrix} \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n \end{bmatrix} \bm{x}\right)\\ 
    &= T\left(\begin{bmatrix} \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n \end{bmatrix}\right) \bm{x}\\ 
    &= \begin{bmatrix} T(\bm{\varepsilon}_1) & T(\bm{\varepsilon}_2) & \cdots & T(\bm{\varepsilon}_n) \end{bmatrix} \bm{x}\\ 
    &= \begin{bmatrix} \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n \end{bmatrix} \bm{A} \bm{x}
\end{aligned}
$$

又

$$
\begin{aligned}
    T \bm{\xi} &= \lambda \bm{\xi}\\ 
    &= \begin{bmatrix} \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n \end{bmatrix} \lambda \bm{x}
\end{aligned}
$$

由于 $\bm{\varepsilon}_1 ,\, \bm{\varepsilon}_2 ,\, \cdots ,\, \bm{\varepsilon}_n$ 线性无关，故有

$$
\bm{A} \bm{x} = \lambda \bm{x}
$$

即特征向量 $\bm{\xi}$ 的坐标 $\bm{x} = \begin{bmatrix} x_1 & x_2 & \cdots & x_n \end{bmatrix}^\intercal$ 满足齐次线性方程组

$$
(\lambda \bm{E} - \bm{A}) \bm{x} = \bm{\theta}
$$

而 $\bm{\xi} \ne \bm{\theta}$，故 $\bm{x} \ne \bm{\theta}$，即 $\lambda \bm{E} - \bm{A}$ 为奇异矩阵，即

$$
\left\lvert \lambda \bm{E} - \bm{A} \right\rvert = 0
$$

即 $\lambda$ 是 $\bm{A}$ 的特征值。

### 不变子空间

!!! info ""
    设 $T$ 是线性空间 $\bm{V}$ 上的一个线性变换，$\bm{W}$ 是 $\bm{V}$ 的一个子空间。若对任意 $\bm{\alpha} \in \bm{W}$，有 $T(\bm{\alpha}) \in \bm{W}$，则称 $\bm{W}$ 是 $T$ 的一个**不变子空间**。

由于零子空间 $\left\lbrace \bm{\theta} \right\rbrace$ 和整个空间 $\bm{V}$ 对任意 $T$ 都是 $T$ 的不变子空间，故称为**平凡不变子空间**。除此以外的不变子空间称为**非平凡不变子空间**。

!!! note ""
    1. 线性空间 $\bm{V}$ 的任意子空间都是数乘变换的不变子空间。
    2. 线性空间 $\bm{V}$ 上的线性变换 $T$ 的像空间 $\operatorname{Im}(T)$、核空间 $\ker(T)$ 和特征子空间 $\bm{V}_{\lambda}$ 都是 $T$ 的不变子空间。 
    3. 线性变换 $T$ 的不变子空间的交与和都是 $T$ 的不变子空间。

    <!-- {{{ 证明 -->
    <details>
    <summary>证明</summary>
    
    1. 设 $\bm{W}$ 是 $\bm{V}$ 的一个子空间，$\bm{\alpha} \in \bm{W}$，设线性变换 $T$ 为 $T(\bm{\alpha}) = k \bm{\alpha}$，其中 $k \in \mathbb{K}$。则有 $T(\bm{\alpha}) \in \bm{W}$，即 $\bm{W}$ 是 $T$ 的不变子空间。

    2. 任取 $\bm{\alpha} \in \operatorname{Im}(T)$，因 $T \bm{\alpha} \in \operatorname{Im}(T)$，故 $\operatorname{Im}(T)$ 是 $T$ 的不变子空间。同理，$\ker(T)$ 也是 $T$ 的不变子空间。设 $\bm{V}_{\lambda}$ 是 $T$ 的任一特征子空间，任取 $\bm{\alpha} \in \bm{V}_{\lambda}$，因 $T \bm{\alpha} = \lambda \bm{\alpha} \in \bm{V}_{\lambda}$，所以 $\bm{V}_{\lambda}$ 是 $T$ 的不变子空间。

    3. 设 $\bm{W}_1$ 和 $\bm{W}_2$ 是 $T$ 的两个不变子空间，任取 $\bm{\alpha} \in \bm{W}_1 \cap \bm{W}_2$，则有 $T \bm{\alpha} \in \bm{W}_1$ 且 $T \bm{\alpha} \in \bm{W}_2$，即 $T \bm{\alpha} \in \bm{W}_1 \cap \bm{W}_2$，所以 $\bm{W}_1 \cap \bm{W}_2$ 是 $T$ 的不变子空间。设 $\bm{W}_1$ 和 $\bm{W}_2$ 是 $T$ 的两个不变子空间，任取 $\bm{\alpha} \in \bm{W}_1 + \bm{W}_2$，则有 $\bm{\alpha} = \bm{\alpha}_1 + \bm{\alpha}_2$，其中 $\bm{\alpha}_1 \in \bm{W}_1$ 且 $\bm{\alpha}_2 \in \bm{W}_2$，则有 $T \bm{\alpha} = T \bm{\alpha}_1 + T \bm{\alpha}_2$，即 $T \bm{\alpha} \in \bm{W}_1 + \bm{W}_2$，所以 $\bm{W}_1 + \bm{W}_2$ 是 $T$ 的不变子空间。

    </details>
    <!-- }}} -->
