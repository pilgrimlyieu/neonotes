---
layout: post
title: 多元函数几何应用与极值
date: 2024-03-12 10:45:08
updated: 2024-04-30 17:50:14
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 几何应用

### 空间曲线的切线与法平面

类似地，有

!!! info ""
    设有空间曲线 $C$，$P_{0}$ 是曲线 $C$ 上一定点，$P$ 是曲线上的动点，作割线 $P_{0} P$，当 $P$ 沿着曲线 $C$ 无限地接近 $P_{0}$ 时，若割线 $P_{0} P$ 的极限位置存在，对应的直线记为 $L$，我们称直线 $L$ 为曲线 $C$ 在点 $P_{0}$ 的**切线**。

    通过点 $P_{0}$ 且与切线 $L$ 垂直的平面, 称为曲线 $C$ 在点 $P_{0}$ 的**法平面**。切线 $L$ 的方向向量称为曲线 $C$ 在点 $P_{0}$ 的**切向量**。

!!! note ""
    设空间曲线 $C$ 的参数方程为

    $$
    \left\lbrace\begin{aligned}
        x &= \varphi(t)\\
        y &= \psi(t)\\
        z &= \omega(t)
    \end{aligned}\right.,\quad t \in [a, b]
    $$

    这里 $\varphi(t), \psi(t), \omega(t)$ 在 $t = t_0$ 处皆可导，且 $\varphi'(t_0), \psi'(t_0), \omega'(t_0)$ 不全为 $0$，则曲线 $C$ 在点 $P_0$ 处的<u>切向量</u>为

    $$
    \Big( \varphi'(t_0), \psi'(t_0), \omega'(t_0) \Big)
    $$

    曲线 $C$ 在点 $P_0$ 处的<u>法平面</u>为

    $$
    \varphi'(t_0)\Big(x - \varphi(t_0)\Big) + \psi'(t_0)\Big(y - \psi(t_0)\Big) + \omega'(t_0)\Big(z - \omega(t_0)\Big) = 0
    $$

!!! note ""
    设空间曲线 $C$ 一般方程为

    $$
    \left\lbrace\begin{aligned}
        F(x, y, z) &= 0,\\
        H(x, y, z) &= 0
    \end{aligned}\right.
    $$

    这里 $F,\, H$ 连续可微，且 $\dfrac{D(F, H)}{D(y, z)},\, \dfrac{D(F, H)}{D(z, x)},\, \dfrac{D(F, H)}{D(x, y)}$ 不全为 $0$，则化为参数方程有

    $$
    \left\lbrace\begin{aligned}
        x &= \varphi(t)\\
        y &= \psi(t)\\
        z &= \omega(t)
    \end{aligned}\right.
    $$

    有关于 $t$ 恒等式

    $$
    \left\lbrace\begin{aligned}
        F\Big(\varphi(t), \psi(t), \omega(t)\Big) &= 0,\\
        H\Big(\varphi(t), \psi(t), \omega(t)\Big) &= 0
    \end{aligned}\right.
    $$

    对 $t$ 求全导数有

    $$
    \left\lbrace\begin{aligned}
        F_x'\varphi'(t) + F_y'\psi'(t) + F_z'\omega'(t) &= 0,\\
        H_x'\varphi'(t) + H_y'\psi'(t) + H_z'\omega'(t) &= 0
    \end{aligned}\right.
    $$

    记

    $$
    \left\lbrace\begin{aligned}
        \bm{n_1} &= (F_x', F_y', F_z'),\\
        \bm{n_2} &= (H_x', H_y', H_z')
    \end{aligned}\right.
    $$

    则<u>切向量</u>与 $\bm{n_1} \boldsymbol{\times} \bm{n_2}$ 平行，其中

    $$
    \bm{n_1} \boldsymbol{\times} \bm{n_2} = \left( \dfrac{D(F, H)}{D(y, z)}, \dfrac{D(F, H)}{D(z, x)}, \dfrac{D(F, H)}{D(x, y)} \right)
    $$

    <u>切向量</u>可取

    $$
    \left( \dfrac{D(F, H)}{D(y, z)}\as_{P_0}, \dfrac{D(F, H)}{D(z, x)}\as_{P_0}, \dfrac{D(F, H)}{D(x, y)}\as_{P_0} \right)
    $$

    曲线 $C$ 在点 $P_0$ 处的<u>法平面</u>为

    $$
    \dfrac{D(F, H)}{D(y, z)}\as_{P_0}(x - x_0) + \dfrac{D(F, H)}{D(z, x)}\as_{P_0}(y - y_0) + \dfrac{D(F, H)}{D(x, y)}\as_{P_0}(z - z_0) = 0
    $$

    或表示为

    $$
    \begin{vmatrix}
        x - x_0 & y - y_0 & z - z_0 \\
        F_x'(P_0) & F_y'(P_0) & F_z'(P_0) \\
        H_x'(P_0) & H_y'(P_0) & H_z'(P_0)
    \end{vmatrix} = 0
    $$

### 空间曲面的切平面与法线

!!! info ""
    设有空间曲面 $S, P_{0}$ 是曲面 $S$ 上一定点，$C$ 是曲面 $S$ 上通过点 $P_{0}$ 的任意一条光滑曲线，如果曲线 $C$ 在点 $P_{0}$ 的切线总保持在某一平面 $\Pi$ 上，则称平面 $\Pi$ 为曲面 $S$ 在点 $P_{0}$ 的**切平面**。通过点 $P_{0}$ 且与切平面 $\Pi$ 垂直的直线称为曲面 $S$ 在点 $P_{0}$ 的**法线**。切平面 $\Pi$ 的法向量称为曲面 $S$ 在点 $P_{0}$ 的**法向量**。

!!! info ""
    设空间曲面 $S$ 一般式方程为

    $$
    F(x, y, z) = 0
    $$

    这里 $F$ 连续可微，且 $F_x',\, F_y',\, F_z'$ 不全为 $0$。

    在 $S$ 上任取通过 $P_0$ 的一条光滑曲线 $C$，设 $C$ 的参数方程为

    $$
    \left\lbrace\begin{aligned}
        x &= \varphi(t)\\
        y &= \psi(t)\\
        z &= \omega(t)
    \end{aligned}\right.
    $$

    则有恒等式

    $$
    F(\varphi(t), \psi(t), \omega(t)) \equiv 0
    $$

    对 $t$ 求全导数有

    $$
    F_x'\varphi'(t) + F_y'\psi'(t) + F_z'\omega'(t) = 0
    $$

    也就是说，切向量 $\bm{r}' = \Big(\varphi'(t), \psi'(t), \omega'(t)\Big) \perp \bm{n}$，其中

    $$
    \bm{n} = (F_x', F_y', F_z')
    $$

    所以 $\bm{n}$ 是空间曲面 $S$ 在 $P_0$ 的法向量，<u>切平面</u>的方程为

    $$
    F_x'(P_0)(x - x_0) + F_y'(P_0)(y - y_0) + F_z'(P_0)(z - z_0) = 0
    $$

    <u>法线</u>方程为

    $$
    \dfrac{x - x_0}{F_x'(P_0)} = \dfrac{y - y_0}{F_y'(P_0)} = \dfrac{z - z_0}{F_z'(P_0)}
    $$

!!! info ""
    设空间曲面 $S$ 的参数方程为

    $$
    \left\lbrace\begin{aligned}
        x &= x(u, v)\\
        y &= y(u, v)\\
        z &= z(u, v)
    \end{aligned}\right.
    $$

    则有恒等式

    $$
    F\Big(x(u, v), y(u, v), z(u, v)\Big) \equiv 0
    $$

    分别对 $u, v$ 求偏导得

    $$
    \left\lbrace\begin{aligned}
        F_x'x_u' + F_y'y_u' + F_z'z_u' &= 0,\\
        F_x'x_v' + F_y'y_v' + F_z'z_v' &= 0
    \end{aligned}\right.
    $$

    记

    $$
    \bm{r}(u, v) = \Big(x(u, v), y(u, v), z(u, v)\Big)
    $$

    则 $S$ 的法向量 $\bm{n} = (F_x', F_y', F_z')$ 有 $\bm{n} \perp \bm{r}_u',\, \bm{n} \perp \bm{r}_v'$，从而 $\bm{n}$ 与 $\bm{r}_u' \boldsymbol{\times} \bm{r}_v'$ 平行，其中

    $$
    \bm{r}_u' \boldsymbol{\times} \bm{r}_v' = (A, B, C) = \left( \dfrac{D(y, z)}{D(u, v)}, \dfrac{D(z, x)}{D(u, v)}, \dfrac{D(x, y)}{D(u, v)} \right)
    $$

    法向量可取

    $$
    \Big(A(u_0, v_0), B(u_0, v_0), C(u_0, v_0)\Big)
    $$

    切平面方程为

    $$
    A(u_0, v_0)(x - x_0) + B(u_0, v_0)(y - y_0) + C(u_0, v_0)(z - z_0) = 0
    $$

    或

    $$
    \begin{vmatrix}
        x - x_0 & y - y_0 & z - z_0\\
        x_u'(u_0, v_0) & y_u'(u_0, v_0) & z_u'(u_0, v_0)\\
        x_v'(u_0, v_0) & y_v'(u_0, v_0) & z_v'(u_0, v_0)
    \end{vmatrix} = 0
    $$

    法线方程为

    $$
    \dfrac{x - x_0}{A(u_0, v_0)} = \dfrac{y - y_0}{B(u_0, v_0)} = \dfrac{z - z_0}{C(u_0, v_0)}
    $$

## 极值

极值定义与一元函数类似，懒得写了。

!!! note 极值的必要条件
    设函数 $f(x, y)$ 在 $(x_0, y_0)$ 可偏导，且 $f(x_0, y_0)$ 是 $f$ 的极值，则

    $$
    f_x'(x_0, y_0) = f_y'(x_0, y_0) = 0
    $$

同样也可以定义**驻点**，即使

$$
f_x'(x_0, y_0) = f_y'(x_0, y_0) = 0
$$

的点 $(x_0, y_0)$。

!!! info ""
    对于 $n$ 元函数

    $$
    f(x_1, \cdots, x_n)
    $$

    **黑塞矩阵** $\bm{H}_{ij} (f) = \left[ \dfrac{\pd^2 f}{\pd x_i x_j} \right]$，即

    $$
    \bm{H} (f) = \begin{bmatrix}
        \dfrac{\pd^2 f}{\pd x_1^2} & \cdots  & \dfrac{\pd^2 f}{\pd x_1 x_n} \\
        \vdots & \ddots & \vdots \\
        \dfrac{\pd^2 f}{\pd x_n x_1} & \cdots & \dfrac{\pd^2 f}{\pd x_n^2}
    \end{bmatrix}
    $$

    显然 $\bm{H} (f)$ 是一个 $n \times n$ 的对称矩阵（当 $f$ 有 $n$ 个偏导连续性时）。

    而且有

    $$
    \bm{H}(f) = \bm{J}(\grad f)^\intercal
    $$

    即函数的黑塞矩阵是其梯度的雅可比矩阵的转置。

!!! note 极值判别法
    设 $\bm{a} = (a_1, \cdots, a_n) \in \R^n$，函数 $f(\bm{x}) = f(x_1, \cdots, x_n)$ 在 $\bm{a}$ 的某邻域二阶连续可微，且 $\grad f(\bm{a}) = \bm{0}$（即 $f'_{x_i}(\bm{a}) = 0\:(1 \le i \le n)$），设函数 $f$ 的黑塞矩阵为 $\bm{H} (f(\bm{x}))$，则
    1. 若 $\bm{H} (f(\bm{a}))$ 是<u>正定矩阵</u>，则 $f$ 在 $\bm{a}$ 处取得**严格极小值**；
    2. 若 $\bm{H} (f(\bm{a}))$ 是<u>负定矩阵</u>，则 $f$ 在 $\bm{a}$ 处取得**严格极大值**；
    3. 若 $\bm{H} (f(\bm{a}))$ 是<u>不定矩阵</u>，则 $f$ 在 $\bm{a}$ 处不取极值。

!!! note ""
    设 $P_0(x_0, y_0) \in \R^2,\, G = N_{\delta}(P_0)$，函数 $f$ 在 $G$ 内二阶连续可微，且 $f_x'(x_0, y_0) = f_y'(x_0, y_0) = 0$，则黑塞矩阵

    $$
    \begin{bmatrix}
        A & B \\
        B & C
    \end{bmatrix} =
    \begin{bmatrix}
        f_{x x}''(x_0, y_0) & f_{x y}''(x_0, y_0) \\
        f_{y x}''(x_0, y_0) & f_{y y}''(x_0, y_0)
    \end{bmatrix}
    $$

    1. 若 $B^2 - AC < 0,\, A > 0$，则 $f$ 在 $P_0$ 处取得*严格极小值*；
    2. 若 $B^2 - AC < 0,\, A < 0$，则 $f$ 在 $P_0$ 处取得*严格极大值*；
    3. 若 $B^2 - AC > 0$，则 $f$ 在 $P_0$ 处*不取极值*；
    4. 若 $B^2 - AC = 0$，则 $f$ *不一定*在 $P_0$ 处取得极值。

!!! info ""
    设 $n$ 元函数 $f(\bm{x}) = f(x_1, \cdots, x_n)$，其 $\bm{a}$ 处泰勒公式为

    $$
    f(\bm{x}) = f(\bm{a}) + \grad f(\bm{a}) \boldsymbol{\cdot} \bm{h} + \dfrac{1}{2} \bm{h}^\intercal \bm{H} (f(\bm{a} + \theta \bm{h})) \bm{h},\quad \bm{h} = \bm{x} - \bm{a},\, \theta \in (0, 1)
    $$

    若在 $\bm{a}$ 处 $\grad f(\bm{a}) = 0$，且 $\bm{H} (f(\bm{a}))$ 是正定矩阵，则 $f(\bm{x})$ 在 $\bm{a}$ 处取得严格极小值。

    ---

    由于线代已经忘光了，上面的就懒得写推导过程了。

### 条件极值

#### 拉格朗日乘子法

!!! info ""
    函数 $f(x_1, \cdots, x_n)$ 在满足约束条件 $\varphi_i(x_1, \cdots, x_n) = 0\quad (i = 1, \cdots m;\; m < n)$ 下的极值问题，可归结为对**拉格朗日函数**

    $$
    \mathcal{L}(x_1, \cdots, x_n, \lambda_1, \cdots, \lambda_m) = f(x_1, \cdots, x_n) + \sum_{i=1}^m \lambda_i \varphi_i(x_1, \cdots, x_n)
    $$

    求普通（无约束）函数极值的问题。其中 $\lambda_i$ 为**拉格朗日乘子**。

通过一个简单的情形，理解一下内涵。令 $n = 3, m = 1$，则为函数 $f(x, y, z)$ 在约束条件 $\varphi(x, y, z) = 0$ 下的极值问题。

$f(x, y, z)$ 相当于空间中无数个（$f(x, y, z) = k$ 才确定了是哪一个）曲面 $\Sigma$，对任意极值点 $P \in \Sigma$，有经过 $P$ 的 $\Sigma$ 的切向量 $\vec{v} \in \R^3$，则有 $\grad f(P) \boldsymbol{\cdot} \vec{v} = 0$（否则沿 $\vec{v}$ 方向的方向导数不为 $0$，$P$ 邻域沿 $\vec{v}$ 方向上 $f$ 会增大或减小，不再是极值）。同理 $\grad \varphi(P) \boldsymbol{\cdot} \vec{v} = 0$，也就是说 $\grad f(P) \par \grad \varphi(P)$，即存在 $\lambda$ 使得 $\grad f(P) + \lambda \grad \varphi(P) = \grad (f + \lambda \varphi)(P) = \vec{0}$。

此时构造拉格朗日函数 $\mathcal{L}(x, y, z, \lambda) = f(x, y, z) + \lambda \varphi(x, y, z)$，则 $\grad \mathcal{L}(P) = \vec{0}$，即 $P$ 是 $\mathcal{L}$ 的驻点。

然后是课本上的这种情形的严格证明。

!!! note ""
    设函数 $f(x, y, z),\, \varphi(x, y, z)$ 连续可微，且 $\varphi_z' \ne 0$，设函数 $f(x, y, z)$ 在满足约束方程 $\varphi(x, y, z) = 0$ 的条件极值在点 $P_0(x_0, y_0, z_0)$ 处取得，令

    $$
    \mathcal{L}(x, y, z, \lambda) = f(x, y, z) + \lambda \varphi(x, y, z)
    $$

    则 $P_0$ 满足方程组

    $$
    \left\lbrace\begin{aligned}
        \mathcal{L}_x'(P_0) &= f_x'(P_0) + \lambda \varphi_x'(P_0) &= 0 \\
        \mathcal{L}_y'(P_0) &= f_y'(P_0) + \lambda \varphi_y'(P_0) &= 0 \\
        \mathcal{L}_z'(P_0) &= f_z'(P_0) + \lambda \varphi_z'(P_0) &= 0 \\
        \mathcal{L}_{\lambda}'(P_0) &= \varphi(P_0) &= 0
    \end{aligned}\right.
    $$

    ---

    证明：

    既然 $f$ 在 $P_0$ 取得条件极值，首先有

    $$
    \varphi(P_0) = 0
    $$

    因为 $\varphi_z'(P_0) \ne 0$，隐函数存在定理知存在 $(x_0, y_0)$ 的邻域 $U$ 使得 $\varphi(x, y, z) = 0$ 有唯一解 $z = z(x, y)$，同时

    $$
    z_0 = z(x_0, y_0),\quad \varphi(x, y, z(x, y)) = 0,\quad \forall (x, y) \in U\\
    z_x'(x_0, y_0) = -\frac{\varphi_x'(P_0)}{\varphi_z'(P_0)},\quad z_y'(x_0, y_0) = -\frac{\varphi_y'(P_0)}{\varphi_z'(P_0)} \tag{1}
    $$

    由于 $f(x, y, z(x, y))$ 在 $(x_0, y_0)$ 取得极值，所以

    $$
    \left\lbrace\begin{aligned}
        f_x'(P_0) + f_z'(P_0)z_x'(x_0, y_0) &= 0 \\
        f_y'(P_0) + f_z'(P_0)z_y'(x_0, y_0) &= 0
    \end{aligned}\right.
    $$

    代入 $(1)$ 式，得

    $$
    \left\lbrace\begin{aligned}
        f_x'(P_0) - \dfrac{1}{\varphi_z'(P_0)} f_z'(P_0) \varphi_x'(P_0) &= 0 \\
        f_y'(P_0) - \dfrac{1}{\varphi_z'(P_0)} f_z'(P_0) \varphi_y'(P_0) &= 0
    \end{aligned}\right.
    $$

    记 $\lambda = -\dfrac{f_z'(P_0)}{\varphi_z'(P_0)}$，则有

    $$
    \left\lbrace\begin{aligned}
        f_x'(P_0) + \lambda \varphi_x'(P_0) &= 0 \\
        f_y'(P_0) + \lambda \varphi_y'(P_0) &= 0 \\
        f_z'(P_0) + \lambda \varphi_z'(P_0) &= 0\\
        \varphi(P_0) &= 0
    \end{aligned}\right.
    $$
