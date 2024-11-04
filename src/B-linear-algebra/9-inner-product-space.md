---
layout: post
title: 内积空间
date: 2024-08-26 16:24:00
updated: 2024-08-26 16:24:00
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

!!! memo ""
    临近大二进行的补充，一学期没学线代，其实早已忘光了，所以接下来只是无情的复制机器。

## 内积空间

!!! info ""
    设 $\bm{V}$ 是实数域 $\mathbb{R}$ 上的线性空间，对 $\bm{V}$ 中的任意两个向量 $\bm{\alpha}, \bm{\beta}$，由某种规则确定了一个实数，记为 $(\bm{\alpha}, \bm{\beta})$，并满足以下条件（内积公理）：
    1. 对称性：$(\bm{\alpha}, \bm{\beta}) = (\bm{\beta}, \bm{\alpha})$；
    2. 可加性：$(\bm{\alpha}_1 + \bm{\alpha}_2, \bm{\beta}) = (\bm{\alpha}_1, \bm{\beta}) + (\bm{\alpha}_2, \bm{\beta})$；
    3. 齐次性：$(k\bm{\alpha}, \bm{\beta}) = k(\bm{\alpha}, \bm{\beta})$；
    4. 非负性：$(\bm{\alpha}, \bm{\alpha}) \ge 0$，且 $(\bm{\alpha}, \bm{\alpha}) = 0$ 当且仅当 $\bm{\alpha} = \bm{0}$。

    则称 $(\bm{\alpha}, \bm{\beta})$ 为向量 $\bm{\alpha}, \bm{\beta}$ 的**实内积**，简称**内积**。定义了实内积的实数域 $\mathbb{R}$ 上的线性空间称为**实内积空间**，其中有限维实内积空间称为**欧几里得空间**，简称**欧氏空间**。

$$
\begin{aligned}
    \left( \sum_{i=1}^{m}a_i \bm{\alpha}_i, \sum_{j=1}^{n}b_{j} \bm{\beta}_{j} \right) &= \sum_{i=1}^{m}\sum_{j=1}^{n}a_i b_j (\bm{\alpha}_i, \bm{\beta}_j) \\ 
    &= \begin{bmatrix}
        a_1 & a_2 & \cdots & a_m
    \end{bmatrix} \begin{bmatrix}
        (\bm{\alpha}_1, \bm{\beta}_1) & (\bm{\alpha}_1, \bm{\beta}_2) & \cdots & (\bm{\alpha}_1, \bm{\beta}_n) \\
        (\bm{\alpha}_2, \bm{\beta}_1) & (\bm{\alpha}_2, \bm{\beta}_2) & \cdots & (\bm{\alpha}_2, \bm{\beta}_n) \\
        \vdots & \vdots & \ddots & \vdots \\
        (\bm{\alpha}_m, \bm{\beta}_1) & (\bm{\alpha}_m, \bm{\beta}_2) & \cdots & (\bm{\alpha}_m, \bm{\beta}_n)
    \end{bmatrix} \begin{bmatrix}
        b_1 \\
        b_2 \\
        \vdots \\
        b_n
    \end{bmatrix} 
\end{aligned}
$$

!!! info ""
    设 $\bm{V}$ 是实内积空间，$\bm{\alpha} \in \bm{V}$，则称 $\left\lVert \alpha \right\rVert = \sqrt{(\bm{\alpha}, \bm{\alpha})}$ 为向量 $\bm{\alpha}$ 的**范数**（**长度**），有如下性质：
    1. $\left\lVert \bm{\alpha} \right\rVert = 0 \iff \bm{\alpha} = \bm{0}$
    2. $\left\lVert k\bm{\alpha} \right\rVert = \left| k \right| \left\lVert \bm{\alpha} \right\rVert$
    3. $\bm{\alpha}^0 = \dfrac{\bm{\alpha}}{\left\lVert \bm{\alpha} \right\rVert}$ 称为 $\bm{\alpha}$ 的**单位向量**

!!! info ""
    设 $\bm{V}$ 是实内积空间，$\bm{\alpha}, \bm{\beta} \in \bm{V}$，则它们的夹角 $\theta \in [0, \pi]$ 定义为

    $$
    \theta = \arccos \dfrac{(\bm{\alpha}, \bm{\beta})}{\left\lVert \bm{\alpha} \right\rVert \left\lVert \bm{\beta} \right\rVert}
    $$

!!! info ""
    设 $\bm{V} = V(\mathbb{C})$，在 $\bm{V}$ 上定义一个二元复函数，称为**复内积**，记作 $(\bm{\alpha}, \bm{\beta})$，满足以下条件：
    1. 对称性：$(\bm{\alpha}, \bm{\beta}) = \overline{(\bm{\beta}, \bm{\alpha})}$；
    2. 可加性：$(\bm{\alpha}_1 + \bm{\alpha}_2, \bm{\beta}) = (\bm{\alpha}_1, \bm{\beta}) + (\bm{\alpha}_2, \bm{\beta})$；
    3. 齐次性：$(k\bm{\alpha}, \bm{\beta}) = k(\bm{\alpha}, \bm{\beta})$（其中 $k \in \mathbb{C}$）；
    4. 非负性：$(\bm{\alpha}, \bm{\alpha}) \ge 0$，且 $(\bm{\alpha}, \bm{\alpha}) = 0$ 当且仅当 $\bm{\alpha} = \bm{0}$。

    则称 $(\bm{\alpha}, \bm{\beta})$ 为向量 $\bm{\alpha}, \bm{\beta}$ 的**复内积**，简称**内积**。定义了复内积的复数域 $\mathbb{C}$ 上的线性空间称为**复内积空间**，其中有限维复内积空间称为**酉空间**。

!!! note 酉空间的主要性质
    1. $(\bm{\alpha}, \lambda \bm{\beta}) = \bar{\lambda} (\bm{\alpha}, \bm{\beta})$
    2. $(\bm{\alpha}, \bm{\beta}_1 + \bm{\beta}_2) = (\bm{\alpha}, \bm{\beta}_1) + (\bm{\alpha}, \bm{\beta}_2)$
    3. $\displaystyle \left( \sum_{i=1}^{m} \lambda_i \bm{\alpha}_i, \sum_{j=1}^{n} \mu_{j} \bm{\beta}_{j} \right) = \sum_{i=1}^{m}\sum_{j=1}^{n}\lambda_i \bar{\mu}_j (\bm{\alpha}_i, \bm{\beta}_j)$
    4. **施瓦兹不等式**：$\left| (\bm{\alpha}, \bm{\beta}) \right| \le \left\lVert \bm{\alpha} \right\rVert \left\lVert \bm{\beta} \right\rVert$（当且仅当 $\bm{\alpha}$ 与 $\bm{\beta}$ 线性相关时等号成立）

## 欧氏空间中的正交变换

设 $\bm{V}$ 是欧氏空间，$\bm{\varepsilon}_1, \bm{\varepsilon}_2, \cdots, \bm{\varepsilon}_n$ 是它的一组基底，且任意 $\bm{\alpha}, \bm{\beta} \in \bm{V}$，都有

$$
\begin{aligned}
    \bm{\alpha} &= x_1 \bm{\varepsilon}_1 + x_2 \bm{\varepsilon}_2 + \cdots + x_n \bm{\varepsilon}_n \\ 
    \bm{\beta} &= y_1 \bm{\varepsilon}_1 + y_2 \bm{\varepsilon}_2 + \cdots + y_n \bm{\varepsilon}_n
\end{aligned}
$$

由内积的性质，有

$$
\begin{aligned}
    (\bm{\alpha}, \bm{\beta}) &= \left( \sum_{i=1}^{n}x_i \bm{\varepsilon}_i, \sum_{j=1}^{n}y_j \bm{\varepsilon}_j \right) \\ 
    &= \sum_{i=1}^{n}\sum_{j=1}^{n}x_i y_j (\bm{\varepsilon}_i, \bm{\varepsilon}_j)
\end{aligned}
$$

记 $\bm{A} = \left[ (\bm{\varepsilon}_i, \bm{\varepsilon}_j) \right]$，则有

$$
\begin{aligned}
    \bm{A} &= \begin{bmatrix}
        (\bm{\varepsilon}_1, \bm{\varepsilon}_1) & (\bm{\varepsilon}_1, \bm{\varepsilon}_2) & \cdots & (\bm{\varepsilon}_1, \bm{\varepsilon}_n) \\
        (\bm{\varepsilon}_2, \bm{\varepsilon}_1) & (\bm{\varepsilon}_2, \bm{\varepsilon}_2) & \cdots & (\bm{\varepsilon}_2, \bm{\varepsilon}_n) \\
        \vdots & \vdots & \ddots & \vdots \\
        (\bm{\varepsilon}_n, \bm{\varepsilon}_1) & (\bm{\varepsilon}_n, \bm{\varepsilon}_2) & \cdots & (\bm{\varepsilon}_n, \bm{\varepsilon}_n)
    \end{bmatrix} \\ 
    &= \begin{bmatrix}
        \bm{\varepsilon}_1 \\
        \bm{\varepsilon}_2 \\ 
        \vdots \\ 
        \bm{\varepsilon}_n
    \end{bmatrix} \begin{bmatrix}
        \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
    \end{bmatrix} 
\end{aligned}
$$

向量 $\bm{\alpha}, \bm{\beta}$ 在基底 $\bm{\varepsilon}_1, \bm{\varepsilon}_2, \cdots, \bm{\varepsilon}_n$ 下的坐标为

$$
\left\lbrace\begin{aligned}
    \bm{X} &= \begin{bmatrix}
        x_1 \\
        x_2 \\
        \vdots \\
        x_n
    \end{bmatrix} \\ 
    \bm{Y} &= \begin{bmatrix}
        y_1 \\
        y_2 \\
        \vdots \\
        y_n
    \end{bmatrix}
\end{aligned}\right.
$$

则内积可表示为

$$
(\bm{\alpha}, \bm{\beta}) = \bm{X}^\intercal \bm{A} \bm{Y}
$$

则称矩阵 $\bm{A}$ 为欧氏空间 $\bm{V}$ 在基底 $\bm{\varepsilon}_1, \bm{\varepsilon}_2, \cdots, \bm{\varepsilon}_n$ 下的**度量矩阵**（**格拉姆矩阵**）。显然，$\bm{A}$ 是对称正定矩阵。

!!! note ""
    欧氏空间中两组不同基底下的度量矩阵合同。

    <!-- {{{ 证明 -->
    <details>
    <summary>证明</summary>
    
    设 $\bm{\varepsilon}_1, \cdots, \bm{\varepsilon}_n$ 与 $\bm{\omega}_1, \cdots, \bm{\omega}_n$ 是欧氏空间的两组不同的基底，度量矩阵分别为 $\bm{A}, \bm{B}$，这两组不同基底之间的过渡矩阵为 $\bm{P}$，即

    $$
    \begin{bmatrix}
        \bm{\omega}_1 & \cdots & \bm{\omega}_n
    \end{bmatrix} = \begin{bmatrix}
        \bm{\varepsilon}_1 & \cdots & \bm{\varepsilon}_n
    \end{bmatrix} \bm{P}
    $$
    
    由于

    $$
    \begin{aligned}
        \bm{A} &= \begin{bmatrix}
            \bm{\varepsilon}_1 \\
            \vdots \\
            \bm{\varepsilon}_n
        \end{bmatrix} \begin{bmatrix}
            \bm{\varepsilon}_1 & \cdots & \bm{\varepsilon}_n
        \end{bmatrix} \\ 
        \bm{B} &= \begin{bmatrix}
            \bm{\omega}_1 \\
            \vdots \\
            \bm{\omega}_n
        \end{bmatrix} \begin{bmatrix}
            \bm{\omega}_1 & \cdots & \bm{\omega}_n
        \end{bmatrix}
    \end{aligned}
    $$

    故

    $$
    \bm{B} = \bm{P}^\intercal \bm{A} \bm{P}
    $$
    
    即 $\bm{A}$ 与 $\bm{B}$ 合同。
    
    </details>
    <!-- }}} -->

若欧氏空间下某组基底的度量矩阵是单位矩阵，则称这组基底是**标准正交基**。

施密特正交化略，可以参看[前面的笔记——正交矩阵及实对称矩阵的对角化](./5-orthogonal-matrix-and-diagonalization-of-real-symmetric-matrix#施密特正交化)。

!!! info ""
    设 $\bm{V}$ 是一个欧氏空间，$T$ 是 $\bm{V}$ 上的线性变换，若对任意向量 $\bm{x}, \bm{y} \in \bm{V}$，变换 $T$ 满足

    $$
    \left(T(\bm{x}), T(\bm{y})\right) = (\bm{x}, \bm{y})
    $$
    
    恒成立，则称 $T$ 为 $\bm{V}$ 上的**正交变换**。

!!! note ""
    设 $T$ 是欧氏空间 $\bm{V}$ 上的线性变换，下面每一个都是使 $T$ 为正交变换的充要条件：
    - $T$ 保持向量长度不变（即任意 $\bm{x} \in \bm{V}$，有 $\left\lVert T(\bm{x}) \right\rVert = \left\lVert \bm{x} \right\rVert$）
    - 任一组标准正交基经过 $T$ 变换后仍是标准正交基
    - $T$ 在任一组标准正交基下的矩阵是正交矩阵

    <!-- {{{ 证明 -->
    <details>
    <summary>证明</summary>
    
    1. 必要性只需令 $\bm{y} = \bm{x}$ 可得。充分性，对 $\bm{x}, \bm{y}, \bm{x} + \bm{y}$ 使用得

    $$
    \begin{aligned}
        \left( T(\bm{x}), T(\bm{x}) \right) &= \left( \bm{x}, \bm{x} \right) \\ 
        \left( T(\bm{y}), T(\bm{y}) \right) &= \left( \bm{y}, \bm{y} \right) \\ 
        \left( T(\bm{x} + \bm{y}), T(\bm{x} + \bm{y}) \right) &= \left( \bm{x} + \bm{y}, \bm{x} + \bm{y} \right)
    \end{aligned}
    $$
    
    而

    $$
    \begin{aligned}
        \left( T(\bm{x} + \bm{y}), T(\bm{x} + \bm{y}) \right) &= \left( T(\bm{x}) + T(\bm{y}), T(\bm{x}) + T(\bm{y}) \right)\\ 
        (\bm{x} + \bm{y}, \bm{x} + \bm{y}) &= \left( T(\bm{x}), T(\bm{x}) \right) + 2\left( T(\bm{x}), T(\bm{y}) \right) + \left( T(\bm{y}), T(\bm{y}) \right)\\ 
        \left( \bm{x}, \bm{x} \right) + 2\left( \bm{x}, \bm{y} \right) + \left( \bm{y}, \bm{y} \right) &= \left( \bm{x}, \bm{x} \right) + 2\left( T(\bm{x}), T(\bm{y}) \right) + \left( \bm{y}, \bm{y} \right)
    \end{aligned}
    $$
    
    得到 $\left( T(\bm{x}), T(\bm{y}) \right) = \left( \bm{x}, \bm{y} \right)$。

    2. 设 $\bm{\varepsilon}_1, \bm{\varepsilon}_2, \cdots, \bm{\varepsilon}_n$ 为欧氏空间 $\bm{V}$ 的标准正交基，则有 $\left( T(\bm{\varepsilon}_i), T(\bm{\varepsilon}_{j}) \right) = (\bm{\varepsilon}_i, \bm{\varepsilon}_{j}) = \delta_{ij}$（当且仅当 $i = j$ 时 $\delta_{ij} = 1$，否则为 $0$）。令 $\bm{x} = \displaystyle \sum_{i=1}^{n}x_i \bm{\varepsilon}_i, \bm{y} = \sum_{j=1}^{n} y_{j}\bm{\varepsilon}_{j}$，可得

    $$
    \begin{aligned}
        \left( T(\bm{x}), T(\bm{y}) \right) &= \left( T\left(\sum_{i=1}^{n}x_i \bm{\varepsilon}_i\right), T\left(\sum_{j=1}^{n}y_j \bm{\varepsilon}_j\right) \right) \\ 
        &= \left( \sum_{i=1}^{n}x_i T(\bm{\varepsilon}_i), \sum_{j=1}^{n}y_j T(\bm{\varepsilon}_j) \right) \\ 
        &= \sum_{i=1}^{n}\sum_{j=1}^{n}x_i y_j \delta_{ij} \\ 
        &= \sum_{i=1}^{n}x_i y_i \\ 
        &= \left( \sum_{i=1}^{n}x_i \bm{\varepsilon}_i, \sum_{j=1}^{n}y_j \bm{\varepsilon}_j \right) \\ 
        &= \left( \bm{x}, \bm{y} \right)
    \end{aligned}
    $$
    
    3. 假设 $T$ 在标准正交基 $\bm{\varepsilon}_1, \bm{\varepsilon}_2, \cdots, \bm{\varepsilon}_n$ 下的矩阵为 $\bm{A}$，则有

    $$
    T(\bm{\varepsilon}_i) = \sum_{j=1}^{n}a_{ji}\bm{\varepsilon}_j
    $$
    
    即

    $$
    T\left( \begin{bmatrix}
        \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
    \end{bmatrix} \right) = \begin{bmatrix}
        \bm{\varepsilon}_1 & \bm{\varepsilon}_2 & \cdots & \bm{\varepsilon}_n
    \end{bmatrix} \bm{A}
    $$
    
    其中 $\bm{A} = [a_{ij}]_n$。另一方面有

    $$
    \begin{aligned}
        \left( T(\bm{\varepsilon}_i), T(\bm{\varepsilon}_j) \right) &= \left( \sum_{k=1}^{n}a_{ki}\bm{\varepsilon}_k, \sum_{l=1}^{n}a_{lj}\bm{\varepsilon}_l \right) \\ 
        &= \sum_{k=1}^{n}\sum_{l=1}^{n}a_{ki}a_{lj}(\bm{\varepsilon}_k, \bm{\varepsilon}_l) \\ 
        &= \sum_{k=1}^{n}a_{ki}a_{kj} \\ 
        &= \delta_{ij}
    \end{aligned}
    $$
    
    由 2. 知

    $$
    \begin{aligned}
        T \text{ 为正交变换} &\iff \left( T(\bm{\varepsilon}_i), T(\bm{\varepsilon}_{j}) \right) = \delta_{ij}\\ 
        &\iff \sum_{k=1}^{n}a_{ki}a_{kj} = \delta_{ij} \\ 
        &\iff \bm{A}^\intercal \bm{A} = \bm{E} \\ 
    \end{aligned}
    $$
    
    即 $\bm{A}$ 是正交矩阵。

    </details>
    <!-- }}} -->

## 酉空间中的酉变换

### 酉变换

类似地，有

!!! info ""
    设 $\bm{V}$ 是一个酉空间，$\sigma$ 是 $\bm{V}$ 上的线性变换，若对任意向量 $\bm{x}, \bm{y} \in \bm{V}$，变换 $\sigma$ 满足

    $$
    \left(\sigma(\bm{x}), T(\bm{y})\right) = (\bm{x}, \bm{y})
    $$
    
    恒成立，则称 $\sigma$ 为 $\bm{V}$ 上的**酉变换**。

!!! note ""
    设 $\sigma$ 是酉空间 $\bm{V}$ 上的线性变换，下面每一个都是使 $\sigma$ 为酉变换的充要条件：
    - 任一组标准正交基经过 $\sigma$ 变换后仍是标准正交基
    - $\sigma$ 在任一组标准正交基下的矩阵是酉矩阵

!!! info ""
    若酉空间 $\bm{V}$ 上的一个线性变换 $\sigma$ 满足，对一切 $\bm{\alpha}, \bm{\beta} \in  \bm{V}$，都有

    $$
    \left( \sigma(\bm{\alpha}), \bm{\beta} \right) = \left( \bm{\alpha}, \sigma(\bm{\beta}) \right)
    $$

    则称 $\sigma$ 为 $\bm{V}$ 上的**对称变换**。

!!! info ""
    设 $\bm{A} \in \C^{n \times n}$，若 $\bar{\bm{A}}^\intercal = \bm{A}$，则称 $\bm{A}$ 是一个**厄米特矩阵**（Hermitian matrix）。

    即实对称矩阵是厄米特矩阵的特例。

!!! note ""
    设 $\sigma$ 是 $n$ 维酉空间 $\bm{V}$ 上的线性变换，则 $\sigma$ 是对称变换的充要条件是 $\sigma$ 在 $\bm{V}$ 的任一组标准正交基下的矩阵是厄米特矩阵。

!!! note ""
    若 $\sigma$ 是 $n$ 维酉空间 $\bm{V}$ 的一个对称变换，那么
    1. $\sigma$ 的特征值都是实数
    2. $\sigma$ 的特征向量对应于不同特征值的是正交的
    3. 存在 $\bm{V}$ 的一个标准正交基，使得 $\sigma$ 在这个基下的矩阵是实对角矩阵

### 厄米特矩阵

!!! note ""
    设 $\bm{A}$ 是一个 $n$ 阶厄米特矩阵，则存在一个 $n$ 阶酉矩阵 $\bm{U}$，使得 $\bar{\bm{U}}^\intercal \bm{A} \bm{U} = \bm{U}^{-1} \bm{A} \bm{U}$ 是一个实对角矩阵。即任意厄米特矩阵都**酉相似**于一个实对角矩阵。

    证明类似于[实对阵矩阵的对角化笔记最后一部分](5-orthogonal-matrix-and-diagonalization-of-real-symmetric-matrix#实对称矩阵的对角化)。

!!! info ""
    若对任意 $\bm{\alpha} \in \C^n, \bm{\alpha} \ne \bm{0}$，有

    $$
    \bar{\bm{\alpha}}^\intercal \bm{A} \bm{\alpha} > 0
    $$
    
    则称 $\bm{A}$ 是**正定厄米特矩阵**，$\bar{\bm{X}}^\intercal \bm{A} \bm{X}$ 是一个**正定厄米特型**。

类似地有

!!! note ""
    设 $\bm{A}$ 是一个 $n$ 阶厄米特矩阵，则下列陈述彼此等价：
    1. $\bm{A}$ 是正定厄米特矩阵
    2. 对任意 $n$ 阶复可逆矩阵 $\bm{P}$，$\bar{\bm{P}}^\intercal \bm{A} \bm{P}$ 是正定厄米特矩阵
    3. $\bm{A}$ 的特征值都是正实数
    4. 存在 $n$ 阶复可逆矩阵 $\bm{P}$ 使得 $\bar{\bm{P}}^\intercal \bm{A} \bm{P} = \bm{E}_n$ 
    5. $\bm{A}$ 可以分解为 $\bar{\bm{Q}}^\intercal \bm{Q}$，其中 $\bm{Q}$ 是 $n$ 阶可逆复矩阵。
    6. $\bm{A}$ 的各阶顺序主子式都是正数

## 欧氏空间的同构

!!! info 线性空间的同构
    数域 $\mathbb{K}$ 上的两个线性空间 $\bm{V}, \bm{W}$ 同构，当且仅当存在一个双射 $f$ 满足：
    1. $f(\bm{\alpha} + \bm{\beta}) = f(\bm{\alpha}) + f(\bm{\beta})$ 
    2. $f(k\bm{\alpha}) = kf(\bm{\alpha})$

    这里 $\bm{\alpha}, \bm{\beta} \in \bm{V}, k \in \mathbb{K}$。则称 $f$ 为 $\bm{V}$ 到 $\bm{W}$ 的**同构映射**，$\bm{V}$ 与 $\bm{W}$ 同构。

!!! info 欧氏空间的同构
    欧氏空间 $\bm{V}, \bm{W}$ 同构，当且仅当存在一个双射 $f$ 满足：
    1. $f(\bm{\alpha} + \bm{\beta}) = f(\bm{\alpha}) + f(\bm{\beta})$
    2. $f(k\bm{\alpha}) = kf(\bm{\alpha})$
    3. $\left( f(\bm{\alpha}), f(\bm{\beta}) \right) = \left( \bm{\alpha}, \bm{\beta} \right)$

    这里 $\bm{\alpha}, \bm{\beta} \in \bm{V}, k \in \mathbb{R}$。则称 $f$ 为 $\bm{V}$ 到 $\bm{W}$ 的**同构映射**，$\bm{V}$ 与 $\bm{W}$ 同构。

!!! note ""
    设 $\bm{V}, \bm{W}$ 都是数域 $\mathbb{K}$ 上的有限维线性空间，则它们同构的充要条件是<u>它们的维数相同</u>。

    数域 $\mathbb{K}$ 上的任意 $n$ 维线性空间同构于 $\mathbb{K}^n$。

!!! note ""
    两个有限维欧氏空间同构的充要条件是<u>它们的维数相同</u>。
