---
layout: post
title: 常微分方程初步
date: 2024-05-23 16:14:02
updated: 2024-08-30 15:42:51
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

一般来说，一个表示未知函数、未知函数的导数以及自变量之间的关系的方程，称为**微分方程**，微分方程中所出现的未知函数的最高阶导数或偏导数的阶数，称为微分方程的**阶**。只有一个自变量的微分方程称为**常微分方程**，否则成为**偏微分方程**。

形如

$$
F(x, y, y', \cdots, y^{(n)}) = 0
$$

的等式称为以 $x$ 为自变量，$y(x)$ 为未知函数的 **$n$ 阶常微分方程**。本篇笔记基本只考虑常微分方程，即下面的微分方程如无特殊说明，指的都是常微分方程。

$n$ 阶微分方程有解 $y = \varphi(x, C_1, C_2, \cdots, C_n)$，其中 $C_1, C_2, \cdots, C_n$ 是 $\varphi$ 中 $n$ 个独立的任意常数，即 $C_1, C_2, \cdots, C_n$ 满足

$$
\dfrac{D(\varphi, \varphi', \cdots, \varphi^{(n-1)})}{D(C_1, C_2, \cdots, C_n)} = \begin{vmatrix}
    \dfrac{\partial \varphi}{\partial C_1} & \dfrac{\partial \varphi}{\partial C_2} & \cdots & \dfrac{\partial \varphi}{\partial C_n} \\
    \dfrac{\partial \varphi'}{\partial C_1} & \dfrac{\partial \varphi'}{\partial C_2} & \cdots & \dfrac{\partial \varphi'}{\partial C_n} \\
    \vdots & \vdots & \ddots & \vdots \\
    \dfrac{\partial \varphi^{(n-1)}}{\partial C_1} & \dfrac{\partial \varphi^{(n-1)}}{\partial C_2} & \cdots & \dfrac{\partial \varphi^{(n-1)}}{\partial C_n}
\end{vmatrix} \ne 0
$$

则称 $y = \varphi(x, C_1, C_2, \cdots, C_n)$ 为方程 $F(x, y, y', \cdots, y^{(n)}) = 0$ 的**通解**。

$n$ 阶微分方程的**初始条件**指的是 $x = x_0$ 时，有

$$
\left\lbrace\begin{aligned}
    y &= y_0\\
    \dfrac{\d y}{\d x} &= y_0'\\
    &\kern{0.24em}\vdots\\
    \dfrac{\d^{n-1} y}{\d x^{n-1}} &= y_0^{(n-1)}
\end{aligned}\right.
$$

其中 $y_0, y_0', \cdots, y_0^{(n-1)}$ 为常数。满足这些初始条件的微分方程称为**初值问题**。

若通解不能用显函数形式给出，而是以隐函数 $\Phi(x, y; C_1, C_2, \cdots, C_n) = 0$ 给出，则把其称为微分方程的**隐式通解**或**通积分**。

下面为了简单起见，将 $\displaystyle \int f(x) \d x$ 视为 $f(x)$ 的某一个原函数。

## 一阶微分方程初等解法

### 变量分离方程

形如

$$
\dfrac{\d y}{\d x} = f(x) g(y)
$$

的微分方程称为**变量分离方程**（或**可分离变量的方程**），其中 $f(x), g(y)$ 为连续函数。

若 $g(y) \ne 0$，则

$$
\dfrac{\d y}{g(y)} = f(x) \d x
$$

则有

$$
\int \dfrac{\d y}{g(y)} = \int f(x) \d x + C\\
$$

从而上式为方程的隐式通解。若存在 $y_0$ 使得 $g(y_0) = 0$，则 $y = y_0$ 满足方程，但不在通解表达式，因此该解称为**奇解**。

### 可化为变量分离方程的类型

形如

$$
\dfrac{\d y}{\d x} = f(ax + by + c)
$$

的微分方程。

令 $u = ax + by + c$，从而 $\d u = a \d x + b \d y$，于是

$$
\dfrac{\d u}{\d x} = a + b \dfrac{\d y}{\d x}
$$

则微分方程可化为

$$
\dfrac{\d u}{\d x} = a + bf(u)
$$

这样就化为了可分离变量的方程。若通解为 $u = \varphi(x, C)$，则方程通积分为

$$
ax + by + c = \varphi(x, C)
$$

---

形如

$$
\dfrac{\d y}{\d x} = f\left(\dfrac{y}{x}\right)
$$

的微分方程，称为**一阶齐次微分方程**。这里的「齐次」和后面将要提到的并不一致，这里的「齐次」指的是，$y, x$ 同时乘以一个非零常数，方程不变。

可化为可分离变量的方程。令 $u = \dfrac{x}{y}$，则 $ux = y$，微分得

$$
\d y = u \d x + x \d u
$$

于是

$$
\dfrac{\d y}{\d x} = u + x \dfrac{\d u}{\d x}
$$

方程化为

$$
f(u) = u + x \dfrac{\d u}{\d x}
$$

即

$$
\dfrac{\d u}{\d x} = \dfrac{1}{x}(f(u) - u)
$$

若通解为 $u = \varphi(x, C)$，则方程通积分为

$$
\dfrac{y}{x} = \varphi(x, C)
$$

---

形如

$$
\dfrac{\d y}{\d x} = f\left( \dfrac{a_1 x + b_1 y + c_1}{a_2 x + b_2 y + c_2} \right)
$$

的微分方程，假设 $c_1, c_2$ 不全为零。当 $\begin{vmatrix} a_1 & a_2 \\ b_1 & b_2 \end{vmatrix} = a_1 b_2 - a_2 b_1 \ne 0$ 时（为零时分式上下除常数部分成比例），设

$$
\left\lbrace\begin{aligned}
    a_1 (x + h) + b_1 (y + k) &= a_1 x + b_1 y + c_1 \\
    a_2 (x + h) + b_2 (y + k) &= a_2 x + b_2 y + c_2
\end{aligned}\right.
$$

即

$$
\left\lbrace\begin{aligned}
    a_1 h + b_1 k &= c_1 \\
    a_2 h + b_2 k &= c_2
\end{aligned}\right.
$$

解得

$$
\left\lbrace\begin{aligned}
    h &= \dfrac{\begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix}}{\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}} \\
    k &= \dfrac{\begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix}}{\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}}
\end{aligned}\right.
$$

令 $u = x + h, v = y + k$，则

$$
\begin{aligned}
    \dfrac{\d v}{\d u} &= \dfrac{\d y}{\d x} \\
    &= f\left( \dfrac{a_1 x + b_1 y + c_1}{a_2 x + b_2 y + c_2} \right) \\
    &= f\left( \dfrac{a_1 u + b_1 v}{a_2 u + b_2 v} \right)\\
    &= f\left( \dfrac{a_1 + b_1 \frac{v}{u}}{a_2 + b_2 \frac{v}{u}}\right)
\end{aligned}
$$

令 $w = \dfrac{v}{u}$，则

$$
w + u \dfrac{\d w}{\d u} = f\left( \dfrac{a_1 + b_1 w}{a_2 + b_2 w} \right)
$$

化为了齐次的形式，可由前面的方法解出。

<!-- {{{也可以用课本上的方式 -->
<details>
<summary>也可以用课本上的方式</summary>

当 $\begin{vmatrix} a_1 & b_2 \\ a_2 & v_1 \end{vmatrix} = a_1 b_2 - a_2 b_1 \ne 0$ 时，令

$$
\left\lbrace\begin{aligned}
    u &= a_1 x + b_1 y + c_1 \\
    v &= a_2 x + b_2 y + c_2
\end{aligned}\right.
$$

则

$$
\left\lbrace\begin{aligned}
    \d u &= a_1 \d x + b_1 \d y \\
    \d v &= a_2 \d x + b_2 \d y
\end{aligned}\right.
$$

于是

$$
\left\lbrace\begin{aligned}
    \d x &= \dfrac{b_2 \d u - b_1 \d v}{a_1 b_2 - a_2 b_1} \\
    \d y &= \dfrac{-a_2 \d u + a_1 \d v}{a_1 b_2 - a_2 b_1}
\end{aligned}\right.
$$

从而原方程可化为

$$
\dfrac{a_1 \d v - a_2 \d u}{b_2 \d u - b_1 \d v} = f\left( \dfrac{u}{v} \right)
$$

进一步地

$$
\left( a_2 + b_2f\left( \dfrac{u}{v} \right)  \right) d u = \left( a_1 + b_1f\left( \dfrac{u}{v} \right)  \right) d v
$$

这是一个齐次微分方程，可用前面的方式解决。

</details>
<!-- }}} -->

若 $a_1 b_2 - a_2 b_1 = 0$，则存在 $k$ 使得 $(a_1, b_1) = k(a_2, b_2)$。此时令 $u = a_2 x + b_2 y$，有

$$
\begin{aligned}
    \dfrac{\d u}{\d x} &= a_2 + b_2 \dfrac{\d y}{\d x}\\ &= a_2 + b_2 f\left( \dfrac{ku + c_1}{u + c_2} \right)
\end{aligned}
$$

化为了变量分离方程。

## 一阶线性微分方程

!!! info ""
    形如

    $$
    \dfrac{\d y}{\d x} + P(x) y = Q(x)
    $$

    的方程称为**一阶线性微分方程**。

    当 $Q(x) \equiv 0$ 时，称为**一阶齐次线性微分方程**，否则称为**一阶非齐次线性微分方程**。

齐次的时候显然，方程化为

$$
\dfrac{\d y}{\d x} + P(x) y = 0
$$

即

$$
y = C \exp\left( -\int P(x) \d x \right)
$$

或者

$$
\boxed{
    y = C \e^{-\int P(x) \d x}
}
$$

对于非齐次的，注意到 $(uv)' = uv' + u'v$，而方程中 $\dfrac{\d y}{\d x}$ 就是 $v'$，$v$ 就是 $y$。可惜的是并不知道 $u$ 是什么。

但是可以两边同时乘一个函数 $t(x)$，使得 $u = t(x), u' = P(x) t(x)$ 就行了。

也即

$$
\dfrac{\d t(x)}{\d x} = P(x) t(x)
$$

转化为

$$
\dfrac{\d t(x)}{\d x} - P(x) t(x) = 0
$$

这就是原微分方程的齐次形式，即 $t(x) = C \exp\left( \displaystyle \int P(x) \d x \right)$，取 $C = 1$ 就是所谓的「积分因子」。

代回去有

$$
\begin{aligned}
    \dfrac{\d }{\d x}\left[ \exp\left( \int P(x) \d x \right) y \right] &= \exp\left( \int P(x) \d x \right) Q(x)\\
    \exp\left( \int P(x) \d x \right) y &= \int \exp\left( \int P(x) \d x \right) Q(x) \d x + C\\
    y &= \exp\left( -\int P(x) \d x \right) \left[ \int \exp\left( \int P(x) \d x \right) Q(x) \d x + C \right]
\end{aligned}
$$

用 $\exp$ 似乎不太好看，换回原始形式就是

$$
\boxed{
    y = \e^{-\int P(x) \d x} \left( \int \e^{\int P(x) \d x} Q(x) \d x + C \right)
}
$$

而注意到 $C \e^{-\int P(x) \d x}$ 为齐次微分方程的通解，另一边为非齐次微分方程的特解，因此可以猜测一个结论——<u>非齐次微分方程的通解为*齐次微分方程的通解*加上*非齐次微分方程的特解*</u>。

总结来说就是

!!! note ""
    对于一阶线性微分方程

    $$
    \dfrac{\d y}{\d x} + P(x) y = Q(x)
    $$

    有通解

    $$
    y = \e^{-\int P(x) \d x} \left( \int \e^{\int P(x) \d x} Q(x) \d x + C \right)
    $$

### 伯努利方程

!!! info ""
    形如

    $$
    \dfrac{\d y}{\d x} + P(x) y = Q(x) y^{\alpha}
    $$

    其中 $P(x), Q(x)$ 为关于 $x$ 的连续函数，$\alpha \ne 0, 1$ 为常数，称为**伯努利方程**。

    <!-- {{{解法 -->
    <details>
    <summary>解法</summary>

    伯努利方程可以转化为一阶线性微分方程。

    $y \ne 0$ 时，等式两边同乘 $y^{-\alpha}$，得

    $$
    y^{-\alpha} \dfrac{\d y}{\d x} + P(x) y^{1 - \alpha} = Q(x)
    $$

    即

    $$
    \dfrac{1}{1 - \alpha} \dfrac{\d y^{1-\alpha}}{\d x} + P(x) y^{1 - \alpha} = Q(x)
    $$

    令 $u = y^{1-\alpha}$，则化为

    $$
    \boxed{\dfrac{\d u}{\d x} + (1 - \alpha) P(x) u = (1 - \alpha) Q(x)}
    $$

    这便是关于函数 $u(x)$ 的一阶线性微分方程。解出 $u(x)$，再令 $y = u^{\frac{1}{1-\alpha}}$ 即可。

    另外，$\alpha > 0$ 时 $y \equiv 0$ 也满足方程，若特解不包含 $y = 0$，则需补上。

    </details>
    <!-- }}} -->

## 全微分方程与积分因子

### 全微分方程

考虑一阶微分方程

$$
P(x, y) \d x + Q(x, y) \d y = 0
$$

若存在函数 $\lambda(x, y)$，使得

$$
\d \lambda = P(x, y) \d x + Q(x, y) \d y
$$

则称 $P(x, y) \d x + Q(x, y)$ 为**恰当微分**，称上面的方程为**全微分方程**（也称为**恰当方程**）。

则 $\lambda(x, y) = C$ 为该全微分方程的隐式通解。

根据[曲线积分和格林公式的相关知识](./11-curve-integral#平面上第二类曲线积分与路径无关的条件)，$P(x, y) \d x + Q(x, y) \d y$ 为恰当微分的充要条件是

$$
\dfrac{\partial Q(x, y)}{\partial x} = \dfrac{\partial P(x, y)}{\partial y}
$$

同时 $\lambda(x, y)$ 可由以下两个式子之一确定（$\lambda(x, y) = \displaystyle \int_{(x_0, y_0)}^{(x, y)} P(x, y) \d x + Q(x, y) \d y$，再选取其中一条直角折线进行积分）

$$
\lambda(x, y) = \int_{x_0}^x P(x, y_0) \d x + \int_{y_0}^y Q(x, y) \d y
$$

或

$$
\lambda(x, y) = \int_{x_0}^x P(x, y) \d x + \int_{y_0}^{y} Q(x_0, y) \d y
$$

其中 $(x_0, y_0)$ 为 $P, Q$ 公共定义域任意一点。

有时候也不必去计算曲线积分，例如

$$
\e^{-y} \d x - (2y + x\e^y) \d y = 0
$$

则有

$$
\begin{aligned}
    \e^{-y} \d x - x \e ^{-y} \d y - 2y \d y &= \d C\\
    \d (x\e^{-y}) - \d y^2 &= \d C\\
    \d (x\e^{-y} - y^2) &= \d C
\end{aligned}
$$

### 积分因子

类似上面所谈到的积分因子，微分方程也有类似的概念。

!!! info ""
    若存在连续可微函数 $\mu(x, y)$，使得

    $$
    \mu(x, y) P(x, y) \d x + \mu(x, y) Q(x, y) \d y = 0
    $$

    为全微分方程，则称 $\mu(x, y)$ 为该方程的**积分因子**。

    <!-- {{{推导过程 -->
    <details>
    <summary>推导过程</summary>

    设 $\mu(x, y)$ 为积分因子，那么

    $$
    \dfrac{\partial \mu Q}{\partial x} = \dfrac{\partial \mu P}{\partial y}
    $$

    即

    $$
    P \dfrac{\partial \mu}{\partial y} - Q \dfrac{\partial \mu}{\partial x} = \left( \dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y} \right) \mu
    $$

    这是以 $\mu$ 为未知函数的一阶线性偏微分方程，通常通过这个方程进行积分因子的求解比较困难。但是在一些特殊的情形可以求出该方程的特解。

    </details>
    <!-- }}} -->

!!! note 积分因子的存在性定理
    设有定义在区域 $D \subset \R^2$ 上的一次微分形式

    $$
    f(x, y) \d x + g(x, y) \d y
    $$

    其中 $f, g$ 是两个连续可微函数。

    对于任意一点 $(x_0, y_0) \in D$，若 $f(x_0, y_0),\, g(x_0, y_0)$ 不同时为零，则必有 $(x_0, y_0)$ 的一个邻域 $U \subset D$ 及定义在 $U$ 上的非零连续可微函数 $\mu(x, y)$ 使得

    $$
    \mu(x, y) (f(x, y) \d x + g(x, y) \d y)
    $$

    为 $U$ 上某个函数 $h(x, y)$ 的全微分。

设 $\mu = \mu(x)$，则可化为

$$
-Q \dfrac{\d \mu}{\d x} = \left( \dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y} \right) \mu
$$

若 $\dfrac{1}{Q}\left( \dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y} \right) $ 仅与 $x$ 有关，记为 $\varphi(x)$，则可化为

$$
\d \ln \mu = -\varphi(x) \d x
$$

得

$$
\mu(x) = \e^{-\int \varphi(x) \d x}
$$

从而有


!!! note ""
    若有 $\dfrac{1}{Q}\left(\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}\right) = \varphi(x)$，则微分方程有积分因子

    $$
    \mu(x) = \e^{-\int \varphi(x) \d x}
    $$

    类似地，若有 $\dfrac{1}{P}\left(\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}\right) = \varphi(y)$，则微分方程有积分因子

    $$
    \mu(y) = \e^{\int \varphi(y) \d y}
    $$

    ---

    若有 $\dfrac{1}{xP-yQ}\left( \dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y} \right) = \varphi(xy)$，则微分方程有积分因子

    $$
    \mu(xy) = \e^{\int \varphi(xy) \d xy}
    $$

观察大法

!!! note ""
    1. $\d (xy) = y\d x + x \d y$
    2. $\d (x^2 \pm y^2) = 2(x \d x \pm y \d y)$
    3. $\d \left( \dfrac{y}{x} \right) = \dfrac{x \d y - y \d x}{x^2}$
    4. $\d \left( \dfrac{x}{y} \right) = \dfrac{y \d x - x \d y}{y^2}$
    5. $\d \left( \arctan \dfrac{y}{x} \right) = \dfrac{x \d y - y \d x}{x^2 + y^2}$
    6. $\d \left( \ln \dfrac{x + y}{x - y} \right) = \dfrac{2(x \d y - y \d x)}{x^2 - y^2}$
    7. $\d \left( \dfrac{x + y}{x - y} \right) = \dfrac{2(x \d y - y \d x)}{(x - y)^2}$

## 解的存在唯一性定理

!!! memo ""
    本部分是打星号部分，仅作了解即可，并不在考试范围内，是大二开学返校前最后一天才开始补的原定任务。

!!! info ""
    函数 $f(x, y)$ 在区域 $D$ 上关于 $y$ 满足**利普希茨条件**（Lipschitz condition），当且仅当存在常数 $L > 0$，使得不等式

    $$
    \left\lvert f(x, y_1) - f(x, y_2) \right\rvert \le L \left\lvert y_1 - y_2 \right\rvert
    $$

    对任意 $(x, y_1), (x, y_2) \in D$ 成立。其中 $L$ 称为**利普希茨常数**。

考虑一阶微分方程

$$
\begin{equation}
    \dfrac{\d y}{\d x} = f(x, y) \label{1}
\end{equation}
$$

!!! info 皮卡存在唯一性定理（Picard's existence and uniqueness theorem）
    若 $f(x, y)$ 在闭区域 $D\colon |x - x_0| \le a, |y - y_0| \le  b$ 上连续且关于 $y$ 满足利普希茨条件，则方程 $\eqref{1}$ 存在唯一解 $y = \varphi(x)$。

    其中它在 $|x - x_0| \le h$ 上连续，且满足初始条件 $\varphi(x_0) = y_0$。这里 $h = \min \left\lbrace a, \dfrac{b}{M} \right\rbrace,\, M = \max\limits_{(x, y) \in D} |f(x, y)|$

    <!-- {{{ 证明 -->
    <details>
    <summary>证明</summary>

    为了方便，仅就 $x_0 \le x \le x_0 + h$ 证明。

    > **引理 1**
    >
    > $y = \varphi(x)$ 是方程 $\eqref{1}$ 的定义在区间 $x_0 \le x \le x + h$ 且满足初始条件 $\varphi(x_0) = y_0$ 的解，当且仅当 $y = \varphi(x)$ 在该区间上连续且满足
    >
    > $$
      \varphi(x) = y_0 + \int_{x_0}^x f(x, y) \d x\quad (x_0 \le x \le x_0 + h)
      $$

    由于 $y = \varphi(x)$ 是方程 $\eqref{1}$ 的解，所以有

    $$
    \dfrac{\d \varphi(x)}{\d x} = f(x, \varphi(x))
    $$

    从 $x_0$ 到 $x$ 积分，得

    $$
    \varphi(x) - \varphi(x_0) = \int_{x_0}^x f(x, \varphi(x)) \d x\quad (x_0 \le x \le x_0 + h)
    $$

    由于 $\varphi(x_0) = y_0$，所以

    $$
    \varphi(x) = y_0 + \int_{x_0}^x f(x, \varphi(x)) \d x\quad (x_0 \le x \le x_0 + h)
    $$

    证毕。

    另一方面，若 $\varphi(x)$ 满足上式，则

    $$
    \dfrac{\d \varphi(x)}{\d x} = f(x, \varphi(x))\quad (x_0 \le x \le x_0 + h)
    $$

    代入 $x = x_0$，得得 $\varphi(x_0) = y_0$，所以 $\varphi(x)$ 是满足初始条件 $\varphi(x_0) = y_0$ 的解。

    > **引理 2**
    >
    > 构造*皮卡逐步逼近函数序列*如下
    >
    > $$
      \left\lbrace\begin{aligned}
          \varphi_0(x_0) &= y_0,\\
          \varphi_n(x) &= y_0 + \int_{x_0}^x f\left( t, \varphi_{n-1}(t) \right) \d t\quad (x_0 \le x \le x_0 + h)
      \end{aligned}\right.$$
    >
    > 则有对于所有的 $n$，$\varphi_n(x)$ 在 $x_0 \le x \le x_0 + h$ 上连续，且满足
    >
    > $$
      \left\lvert \varphi_n(x) - y_0 \right\rvert \le b
      $$

    采用数学归纳法证明。

    $n = 1$ 时，$\displaystyle \varphi_1(x) = y_0 + \int_{x_0}^x f(t, y_0)\d t$。显然 $\varphi_1(x)$ 在 $x_0 \le x \le x_0 + h$ 上有定义且连续，同时

    $$
    \begin{aligned}
        \left\lvert \varphi_1(x) - y_0 \right\rvert &= \left\lvert \int_{x_0}^x f(t, y_0) \d t \right\rvert\\
        &\le \int_{x_0}^x \left\lvert f(t, y_0) \right\rvert \d t\\
        &\le \int_{x_0}^x M \d t\\
        &= M(x - x_0)\\
        &\le Mh\\
        &\le b
    \end{aligned}
    $$

    故 $n = 1$ 时结论成立。

    假设 $n = k$ 时结论成立，即 $\varphi_k(x)$ 在 $x_0 \le x \le x_0 + h$ 上连续，且满足 $\left\lvert \varphi_k(x) - y_0 \right\rvert \le b$。则

    $$
    \varphi_{k+1}(x) = y_0 + \int_{x_0}^x f(t, \varphi_k(t)) \d t
    $$

    由于 $f(x, y)$ 在闭区域 $D$ 上连续，所以 $f(t, \varphi_k(t))$ 在 $x_0 \le t \le x_0 + h$ 上连续，从而 $\varphi_{k+1}(x)$ 在 $x_0 \le x \le x_0 + h$ 上连续。又

    $$
    \begin{aligned}
        \left\lvert \varphi_{k+1}(x) - y_0 \right\rvert &= \left\lvert \int_{x_0}^x f(t, \varphi_k(t)) \d t \right\rvert\\
        &\le \int_{x_0}^x \left\lvert f(t, \varphi_k(t)) \right\rvert \d t\\
        &\le \int_{x_0}^x M \d t\\
        &= M(x - x_0)\\
        &\le Mh\\
        &\le b
    \end{aligned}
    $$

    故 $n = k + 1$ 时结论成立。

    综上，对于所有的 $n$，$\varphi_n(x)$ 在 $x_0 \le x \le x_0 + h$ 上连续，且满足 $\left\lvert \varphi_n(x) - y_0 \right\rvert \le b$。

    > **引理 3**
    >
    > 函数序列 $\left\lbrace \varphi_n(x) \right\rbrace$ 在 $x_0 \le x \le x_0 + h$ 上一致收敛于某个函数 $\varphi(x)$。

    函数项级数

    $$
    \varphi_0(x) + \sum_{k=1}^{\infty}\left[ \varphi_{k}(x) - \varphi_{k-1}(x) \right]   \quad (x_0 \le x \le x_0 + h)
    $$

    的部分和为

    $$
    \varphi_0(x) + \sum_{k=1}^{n}\left[ \varphi_{k}(x) - \varphi_{k-1}(x) \right]
    $$

    只需证明这个级数在 $x_0 \le x \le x_0 + h$ 上一致收敛即可。

    现用数学归纳法证明

    $$
    \left\lvert \varphi_{k} - \varphi_{k-1}(x) \right\rvert \le \dfrac{ML^{k-1}}{k!}(x-x_0)^{k},\quad (x_0 \le x \le x_0 + h)
    $$

    当 $k = 1$ 时，为

    $$
    \left\lvert \varphi_{1} - \varphi_{0}(x) \right\rvert = \left\lvert \int_{x_0}^x f(t, y_0) \d t \right\rvert \le M(x - x_0)
    $$

    即 $k = 1$ 时结论成立。假设 $k = n$ 时结论成立，即

    $$
    \left\lvert \varphi_{n} - \varphi_{n-1}(x) \right\rvert \le \dfrac{ML^{n-1}}{n!}(x-x_0)^{n},\quad (x_0 \le x \le x_0 + h)
    $$

    则

    $$
    \begin{aligned}
        \left\lvert \varphi_{n+1} - \varphi_{n}(x) \right\rvert &= \left\lvert \int_{x_0}^x f(t, \varphi_n(t)) \d t - \int_{x_0}^x f(t, \varphi_{n-1}(t)) \d t \right\rvert\\
        &\le \int_{x_0}^x \left\lvert f(t, \varphi_n(t)) - f(t, \varphi_{n-1}(t)) \right\rvert \d t\\
        &\le L \int_{x_0}^x \left\lvert \varphi_n(t) - \varphi_{n-1}(t) \right\rvert \d t\\
        &\le \dfrac{ML^n}{n!} \int_{x_0}^x (t - x_0)^n \d t\\
        &= \dfrac{ML^n}{n!} \dfrac{(x - x_0)^{n+1}}{n+1}\\
        &= \dfrac{ML^{n+1}}{(n+1)!} (x - x_0)^{n+1}
    \end{aligned}
    $$

    故 $k = n + 1$ 时结论成立，归纳得证。

    从而

    $$
    \left\lvert \varphi_{k} - \varphi_{k-1}(x) \right\rvert \le \dfrac{ML^{k-1}}{k!}(x-x_0)^{k} \le \dfrac{ML^{k-1}}{k!}h^{k},\quad (x_0 \le x \le x_0 + h)
    $$

    由于 $\displaystyle \sum_{k=1}^{\infty} \dfrac{ML^{k-1}}{k!}h^{k}$ 收敛，所以 $\displaystyle \sum_{k=1}^{\infty} \left\lvert \varphi_{k} - \varphi_{k-1}(x) \right\rvert$ 在 $x_0 \le x \le x_0 + h$ 上一致收敛（[强级数判别法](/notes/A-calculus/13-infinite-series#一致收敛)），记 $\varphi(x) = \displaystyle \lim_{n \to \infty} \varphi_n(x)$，则 $\varphi(x)$ 在 $x_0 \le x \le x_0 + h$ 上有定义且连续，同时有

    $$
    \left\lvert \varphi(x) - y_0 \right\rvert \le b
    $$

    证毕。

    > **引理 4**
    >
    > 当 $x_0 \le x \le x_0 + h$ 时有
    >
    > $$
    \varphi(x) = y_0 + \int_{x_0}^x f(t, \varphi(t)) \d t
    $$

    对皮卡逐步逼近函数序列 $\left\lbrace \varphi_n(x) \right\rbrace$ 两边取极限，得

    $$
    \begin{aligned}
        \lim_{n \to \infty} \varphi_n(x) &= y_0 + \lim_{n \to \infty} \int_{x_0}^x f(t, \varphi_{n-1}(t)) \d t\\
        &= y_0 + \int_{x_0}^x \lim_{n\to \infty}f(t, \varphi_{n-1}(t)) \d t
    \end{aligned}
    $$

    得

    $$
    \varphi(x) = y_0 + \int_{x_0}^x f(t, \varphi(t)) \d t
    $$

    证毕。

    > **引理 5**
    >
    > 函数 $\varphi(x)$ 是方程 $\eqref{1}$ 满足初始条件 $\varphi(x_0) = y_0$ 的唯一解。

    设 $y = \phi(x)$ 也是方程 $\eqref{1}$ 满足初始条件 $\phi(x_0) = y_0$ 的解，则

    $$
    \phi(x) = y_0 + \int_{x_0}^x f(t, \phi(t)) \d t
    $$

    现证明

    $$
    \left\lvert \phi(x) - \varphi_n(x) \right\rvert \le \dfrac{ML^{n}}{(n+1)!}(x-x_0)^{n+1}
    $$

    采用数学归纳法证明。

    当 $n = 0$ 时，有

    $$
    \begin{aligned}
        \left\lvert \phi(x) - \varphi_0(x) \right\rvert &= \left\lvert \int_{x_0}^x f(t, \phi(t)) \d t \right\rvert\\
        &\le \int_{x_0}^x \left\lvert f(t, \phi(t)) \right\rvert \d t\\
        &\le M(x - x_0)
    \end{aligned}
    $$

    即 $n = 0$ 时结论成立。假设 $n = k$ 时结论成立，即

    $$
    \left\lvert \phi(x) - \varphi_k(x) \right\rvert \le \dfrac{ML^{k}}{(k+1)!}(x-x_0)^{k+1}
    $$

    则

    $$
    \begin{aligned}
        \left\lvert \phi(x) - \varphi_{k+1}(x) \right\rvert &= \left\lvert \int_{x_0}^x f(t, \phi(t)) \d t - \int_{x_0}^x f(t, \varphi_k(t)) \d t \right\rvert\\
        &\le \int_{x_0}^x \left\lvert f(t, \phi(t)) - f(t, \varphi_k(t)) \right\rvert \d t\\
        &\le L \int_{x_0}^x \left\lvert \phi(t) - \varphi_k(t) \right\rvert \d t\\
        &\le \dfrac{ML^{k+1}}{(k+1)!} \int_{x_0}^x (t - x_0)^{k+1} \d t\\
        &= \dfrac{ML^{k+1}}{(k+2)!} (x - x_0)^{k+2}
    \end{aligned}
    $$

    故 $n = k + 1$ 时结论成立，归纳得证。

    从而

    $$
    \left\lvert \phi(x) - \varphi_n(x) \right\rvert \le \dfrac{ML^{n}}{(n+1)!}(x-x_0)^{n+1} \le  \dfrac{ML^{n}}{(n+1)!}h^{n+1}
    $$

    又

    $$
    \lim_{n \to \infty} \dfrac{ML^{n}h^{n+1}}{(n+1)!} = 0
    $$

    从而 $\left\lbrace \varphi_n(x) \right\rbrace$ 在 $x_0 \le x \le x_0 + h$ 上一致收敛于 $\varphi(x)$。由收敛函数的唯一性可知，$\phi(x) = \varphi(x)$，即 $\varphi(x)$ 是方程 $\eqref{1}$ 满足初始条件 $\varphi(x_0) = y_0$ 的唯一解。

    由五个引理依次推论，就完成了证明。

    </details>
    <!-- }}} -->

## 高阶微分方程

### 可降阶的高阶微分方程

形如

$$
y^{(n)} = f(x)
$$

的微分方程。显然 $\displaystyle y^{(n-1)} = \int f(x) \d x + C_1,\, y^{(n-2)} = \int \left( \int f(x) \d x + C_1 \right) \d x + C_2 = \int \d x \int f(x) \d x + C_1 x + C_2,\, \cdots$。

以此类推，得到含有 $n$ 个任意独立常数 $C_i$ 的解，即通解。

---

形如

$$
f(x, y', y'') = 0
$$

的微分方程。

这种方程中不显含 $y$，可令 $y' = p(x)$，则 $y'' = \dfrac{\d p}{\d x}$，则可化为

$$
f\left(x, p, \dfrac{\d p}{\d x}\right) = 0
$$

这就是以 $x$ 为自变量，以 $p$ 为未知函数的一阶微分方程。若能解得其通解 $p = \varphi(x, C_1)$，则有 $\dfrac{\d y}{\d x} = \varphi(x, C_1)$ 又是一个以 $x$ 为自变量，以 $y$ 为未知函数的一阶微分方程，可解得 $y = \psi(x, C_1, C_2)$，这就是原方程的通解。

---

形如

$$
f(y, y', y'') = 0
$$

的微分方程。

这种方程中不显含 $x$，可令 $y' = p(y)$，则 $y'' = \dfrac{\d p}{\d x} = \dfrac{\d p}{\d y} \dfrac{\d y}{\d x} = p \dfrac{\d p}{\d y}$，则可化为

$$
f\left(y, p, p \dfrac{\d p}{\d y}\right) = 0
$$

这就是以 $y$ 为自变量，以 $p$ 为未知函数的一阶微分方程。若能解得其通解 $p = \varphi(y, C_1)$，则有 $\dfrac{\d y}{\d x} = \varphi(y, C_1)$ 又是一个以 $y$ 为自变量，以 $x$ 为未知函数的一阶微分方程，可解得 $x = \psi(y, C_1, C_2)$，这就是原方程的通解。

### 二阶线性微分方程

$n$ 阶线性微分方程一般形式为

$$
y^{(n)} + p_1(x) y^{(n-1)} + \cdots + p_n(x) y = f(x)
$$

当 $f(x) \equiv 0$ 时，对应的方程

$$
y^{(n)} + p_1(x) y^{(n-1)} + \cdots + p_n(x) y = 0
$$

称为 **$n$ 阶齐次线性微分方程**，否则称为 **$n$ 阶非齐次线性微分方程**。

本节主要讨论二阶线性微分方程，即形如

$$
y'' + p(x) y' + q(x) y = f(x)
$$

的方程称为**二阶线性微分方程**。

#### 朗斯基行列式

!!! info ""
    设 $y_1(x), y_2(x), \cdots, y_n(x)$ 为 $[a, b]$ 上的 $(n-1)$ 阶可微函数，行列式 $W_{ij}(x) = y_{j}^{(i-1)}(x)$，或写成

    $$
    W(x) = \begin{vmatrix}
        y_1(x) & y_2(x) & \cdots & y_n(x) \\
        y_1'(x) & y_2'(x) & \cdots & y_n'(x) \\
        \vdots & \vdots & \ddots & \vdots \\
        y_1^{(n-1)}(x) & y_2^{(n-1)}(x) & \cdots & y_n^{(n-1)}(x)
    \end{vmatrix}
    $$

    称为 $y_1(x), y_2(x), \cdots, y_n(x)$ 的**朗斯基行列式**（Wronski determinant）。

设 $y_1(x), y_2(x), \cdots, y_n(x)$ 为上面的 $n$ 阶齐次线性微分方程的解，它们均在 $[a, b]$ 上有定义，若其朗斯基行列式在 $[a, b]$ 上恒为 $0$，则称 $y_1(x), y_2(x), \cdots, y_n(x)$ **线性相关**；否则则称 $y_1(x), y_2(x), \cdots, y_n(x)$ **线性无关**。

若一组函数在某一点线性无关，则在其它点也线性无关，即若朗斯基行列式在某点等于 $0$，则其在整个区间上恒等于 $0$。

!!! note 刘维尔公式
    设 $y_1(x), y_2(x)$ 是二阶齐次线性微分方程 $y'' + p(x)y' + q(x)y = 0$ 的两个解，则它们的朗斯基行列式满足

    $$
    W(x) = W(x_0) \e^{-\int_{x_0}^x p(x) \d x}
    $$

    其中 $x_0 \in [a, b]$ 为任意一点。

#### 二阶齐次线性微分方程解的结构

!!! note ""
    设 $y_1(x), y_2(x)$ 是二阶线性微分方程的两个线性无关的特解，则该方程通解为

    $$
    y = C_1 y_1(x) + C_2 y_2(x)
    $$

    其中 $C_1, C_2$ 为任意常数。

    ---

    由题意

    $$
    \left\lbrace\begin{aligned}
        y_1'' + p(x) y_1' + q(x) y_1 &= 0 \\
        y_2'' + p(x) y_2' + q(x) y_2 &= 0
    \end{aligned}\right.
    $$

    将 $y = C_1 y_1(x) + C_2 y_2(x)$ 代入方程得

    $$
    \begin{aligned}
        y'' + p(x) y' + q(x) y &= C_1 y_1'' + C_2 y_2'' + p(x) (C_1 y_1' + C_2 y_2') + q(x) (C_1 y_1 + C_2 y_2) \\
        &= C_1 (y_1'' + p(x) y_1' + q(x) y_1) + C_2 (y_2'' + p(x) y_2' + q(x) y_2) \\
        &= 0
    \end{aligned}
    $$

    因为 $y_1(x), y_2(x)$ 线性无关，所以

    $$
    W(x) = \begin{vmatrix}
        y_1(x) & y_2(x) \\
        y_1'(x) & y_2'(x)
    \end{vmatrix} \ne 0
    $$

    则

    $$
    \dfrac{D(y, y')}{D(C_1, C_2)} = W(x) \ne 0
    $$

    则 $C_1, C_2$ 为 $y$ 中两个独立的任意常数，故 $y = C_1 y_1(x) + C_2 y_2(x)$ 为方程的通解。

推广有

!!! note ""
    设 $y_1(x), y_2(x), \cdots, y_n(x)$ 是 $n$ 阶齐次线性微分方程

    $$
    y^{(n)} + p_1(x) y^{(n-1)} + p_2(x) y^{(n-2)} + \cdots + p_n(x) y = 0
    $$

    的 $n$ 个线性无关的解，则该方程的通解为

    $$
    y = C_1 y_1(x) + C_2 y_2(x) + \cdots + C_n y_n(x)
    $$

    其中 $C_1, C_2, \cdots, C_n$ 为任意常数。

#### 二阶非齐次线性微分方程解的结构

!!! note ""
    设 $y_1^{*}(x)$ 是二阶非齐次线性微分方程 $y'' + p(x) y' + q(x) y = f(x)$ 的一个特解，$y_2^{*}(x)$ 是对应的齐次线性微分方程的通解，则 $y = y_1^{*}(x) + y_2^{*}(x)$ 是非齐次线性微分方程的通解。

因此还有：若 $y_1^{*}(x), y_2^{*}(x)$ 是非齐次线性微分方程的两个特解，则其对应的齐次线性微分方程的通解为 $y = y_1^{*}(x) - y_2^{*}(x)$。

#### 常数变易法

设 $y_1(x), y_2(x)$ 是二阶齐次线性微分方程 $y'' + p(x) y' + q(x) y = 0$ 的两个线性无关的解，则 $y = C_1 y_1(x) + C_2 y_2(x)$ 是该方程的通解，接下来寻求方程形如

$$
\begin{equation}
    y^{*} = C_1(x) y_1(x) + C_2(x) y_2(x) \label{2}
\end{equation}
$$

的特解。即将任意常数 $C_1, C_2$ 换成了两个待定函数 $C_1(x), C_2(x)$，因此称为**常数变易法**。

两边求导得

$$
(y^{*})' = C_1(x) y_1'(x) + C_2(x) y_2'(x) + C_1'(x) y_1(x) + C_2'(x) y_2(x)
$$

只需找出某一对 $C_1(x), C_2(x)$，使得 $y^{*}$为二阶齐次线性微分方程的解即可。即为此令

$$
C_1'(x) y_1(x) + C_2'(x) y_2(x) = 0
$$

这样可以避免出现 $C_1(x), C_2(x)$ 的二阶导数。因此有

$$
(y^{*})' = C_1(x) y_1'(x) + C_2(x) y_2'(x)
$$

再求一次导数

$$
(y^{*})'' = C_1(x) y_1''(x) + C_2(x) y_2''(x) + C_1'(x) y_1'(x) + C_2'(x) y_2'(x)
$$

代入原方程得

$$
\begin{aligned}
    (y^{*})'' &= C_1(x) y_1''(x) + C_2(x) y_2''(x) + C_1'(x) y_1'(x) + C_2'(x) y_2'(x)\\
    (y^{*})'' + \textcolor{FF9900}{p(x) (y^{*})'} + \textcolor{00B050}{q(x) y^{*}} &= C_1'(x) y_1'(x) + C_2'(x) y_2'(x) +\\
    &\phantom{=} C_1(x) \left( y_1''(x) + \textcolor{FF9900}{p(x)y_1'(x)} + \textcolor{00B050}{q(x)y_1(x)} \right) +\\
    &\phantom{=} C_2(x) \left( y_2''(x) + \textcolor{FF9900}{p(x)y_2'(x)} + \textcolor{00B050}{q(x)y_2(x)} \right)\\
    f(x) &= C_1'(x) y_1'(x) + C_2'(x) y_2'(x)
\end{aligned}
$$

联立有

$$
\left\lbrace\begin{aligned}
    C_1'(x) y_1(x) + C_2'(x) y_2(x) &= 0\\
    C_1'(x) y_1'(x) + C_2'(x) y_2'(x) &= f(x)
\end{aligned}\right.
$$

该方程组系数矩阵行列式恰为关于 $y_1(x), y_2(x)$ 的朗斯基行列式 $W(x)$，由于 $y_1(x), y_2(x)$ 线性无关，故 $W(x) \ne 0$，因此该方程组能唯一解出 $C_1'(x), C_2'(x)$，积分后可得 $C_1(x), C_2(x)$，于是就能找到形如 $y^{*} = C_1(x) y_1(x) + C_2(x) y_2(x)$ 的特解。

即

!!! note ""
    若函数 $C_1(x), C_2(x)$ 满足方程组

    $$
    \left\lbrace\begin{aligned}
        C_1'(x) y_1(x) + C_2'(x) y_2(x) &= 0\\
        C_1'(x) y_1'(x) + C_2'(x) y_2'(x) &= f(x)
    \end{aligned}\right.
    $$

    其中 $y_1(x), y_2(x)$ 为齐次线性微分方程

    $$
    y'' + p(x) y' + q(x) y = 0
    $$

    的两个线性无关的解，则非齐次线性微分方程

    $$
    y'' + p(x) y' + q(x) y = f(x)
    $$

    有特解

    $$
    y^{*} = C_1(x) y_1(x) + C_2(x) y_2(x)
    $$

推广有

!!! note ""
    若函数 $C_1(x), C_2(x), \cdots, C_n(x)$ 满足方程组

    $$
    \left\lbrace\begin{aligned}
        \displaystyle \sum_{i=1}^{n} C_i'(x) y_i(x) &= 0\\
        \displaystyle \sum_{i=1}^{n} C_i'(x) y_i'(x) &= 0\\
        \vdots\\
        \displaystyle \sum_{i=1}^{n} C_i'(x) y_i^{(n-2)}(x) &= 0\\
        \displaystyle \sum_{i=1}^{n} C_i'(x) y_i^{(n-1)}(x) &= f(x)\\
    \end{aligned}\right.
    $$

    其中 $y_1(x), y_2(x), \cdots, y_n(x)$ 为齐次线性微分方程

    $$
    y^{(n)} + p_1(x) y^{(n-1)} + p_2(x) y^{(n-2)} + \cdots + p_n(x) y = 0
    $$

    的 $n$ 个线性无关的解，则非齐次线性微分方程

    $$
    y^{(n)} + p_1(x) y^{(n-1)} + p_2(x) y^{(n-2)} + \cdots + p_n(x) y = f(x)
    $$

    有特解

    $$
    y^{*} = C_1(x) y_1(x) + C_2(x) y_2(x) + \cdots + C_n(x) y_n(x)
    $$

#### 二阶线性常系数微分方程

当 $p(x), q(x)$ 是常数 $p, q$ 时，二阶线性微分方程变为

$$
y'' + py' + qy = f(x)
$$

称为**二阶线性常系数微分方程**。

高阶同理

$$
y^{(n)} + p_1 y^{(n-1)} + p_2 y^{(n-2)} + \cdots + p_n y = f(x)
$$

称为 **$n$ 阶线性常系数微分方程**。

考虑齐次方程

$$
y'' + p y' + q y = 0
$$

设 $y = \e^{\lambda x}$，则有

$$
\e^{\lambda x}(\lambda^2 + p\lambda + q) = 0
$$

即 $\lambda^2 + p \lambda + q = 0$，该方程称为**特征方程**。因为若该方程若能给出不同的两个解，则得到了两个线性无关的解，从而得到了通解。

$p^2 - 4q > 0$ 时特征方程有二实根 $\lambda_1, \lambda_2$，通解为 $y = C_1 \e^{\lambda_1 x} + C_2 \e^{\lambda_2 x}$。

$p^2 - 4q = 0$ 时特征方程有重根 $\lambda$，此时有一个特解 $y_1 = \e^{\lambda x}$，为求另一个特解 $y_2$，由刘维尔公式

$$
\begin{aligned}
    W(x) &= \begin{vmatrix}
        \e^{\lambda x} & y_2(x)\\
        \lambda \e^{\lambda x} & y_2'(x)
    \end{vmatrix}\\
    &= c_1 \e^{-px}
\end{aligned}
$$

化简后有

$$
y_2' - \lambda y_2 = c_1\e^{-(p+\lambda)x}
$$

得

$$
y_2 = \e^{\lambda x}(c_2 + c_1x)
$$

取 $c_2 = 0, c_1 = 1$ 得 $y_2 = x \e^{\lambda x}$，因此通解为 $y = (C_1 + C_2 x) \e^{\lambda x}$。

$p^2 - 4q < 0$ 时特征方程有共轭复根 $\alpha \pm \beta \i$，则通解为

$$
\begin{aligned}
    C_1^{*} \e^{(\alpha + \beta \i)x} + C_2^{*} \e^{(\alpha - \beta \i)x} &= \e^{\alpha x} \left(C_1^{*} \e^{\beta \i x} + C_2^{*} \e^{-\beta \i x}\right)\\
    &= \e^{\alpha x} \left(C_1^{*} \cos \beta x + C_1^{*} \i \sin \beta x + C_2^{*} \cos \beta x - C_2^{*} \i \sin \beta x\right)\\
    &= \e^{\alpha x} \left((C_1^{*} + C_2^{*}) \cos \beta x + (C_1^{*} - C_2^{*}) \i \sin \beta x\right)\\
    &= \e^{\alpha x}\left(C_1 \cos \beta x + C_2 \sin \beta x\right)
\end{aligned}
$$

总结有

!!! note ""
    设二阶齐次线性常系数微分方程为

    $$
    y'' + py' + qy = 0
    $$

    则有
    1. $p^2 - 4q > 0$：通解为 $y = C_1 \e^{\lambda_1 x} + C_2 \e^{\lambda_2 x}$
        - $\lambda_1, \lambda_2$ 是特征方程二实根
    2. $p^2 - 4q = 0$：通解为 $y = (C_1 + C_2 x) \e^{\lambda x}$
    3. $p^2 - 4q < 0$：通解为 $y = \e^{\alpha x}\left(C_1 \cos \beta x + C_2 \sin \beta x\right)$
        - $\alpha = -\dfrac{p}{2}$
        - $\beta = \dfrac{\sqrt{4q - p^2}}{2}$

对于 $n$ 阶齐次线性常系数微分方程

$$
y^{(n)} + p_1 y^{(n-1)} + p_2 y^{(n-2)} + \cdots + p_n y = 0
$$

特征方程为

$$
\lambda^n + p_1 \lambda^{n-1} + p_2 \lambda^{n-2} + \cdots + p_n = 0
$$

其 $n$ 个特征根为 $\lambda_1, \lambda_2, \cdots, \lambda_n$（允许有重根），则

|                特征根                |                                                               对应的线性无关的特解                                                                |
|                 :-:                  |                                                                        :-:                                                                        |
|         $k$ 重实根 $\lambda$         |                                                  $\e^{\lambda x}, \cdots, x^{k-1}\e^{\lambda x}$                                                  |
| $k$ 重共轭复根 $\alpha \pm \beta \i$ | $\e^{\alpha x} \cos \beta x, \e^{\alpha x} \sin \beta x, \cdots, x^{k-1}\e^{\alpha x} \cos \beta x, x^{k-1}\e^{\alpha x} \sin \beta x$ |

对于非齐次，常数变易法比较麻烦。对于特定形式的 $f(x)$，有**待定系数法**。

!!! info ""
    设 $f(x) = A_m(x)\e^{\mu x}$，其中 $\mu$ 为实常数，$A_m(x)$ 为 $x$ 的 $m$ 次多项式，则方程有形如

    $$
    y^{*} = x^k B_m(x)\e^{\mu x}
    $$

    的特解，其中 $k$ 为 $\mu$ 在特征方程 $\lambda^2 + p \lambda + q = 0$ 的根的重数（$\mu$ 不是特征根时令 $k = 0$），$B_m(x)$ 为待定的 $x$ 的 $m$ 次多项式。

    <!-- {{{证明 -->
    <details>
    <summary>证明</summary>

    (1) $\mu = 0$

    $$
    f(x) = A_m(x)
    $$

    (1.1) 若 $\mu $ 不是特征根，则 $q \ne 0$，设 $y^{*} = x^k B_m(x)$，代入方程左边。

    此时方程左右两边均为关于 $x$ 的 $m$ 次多项式，对比系数可确定 $B_m(x)$。

    (1.2) 若 $0$ 为特征方程的单根，则 $q = 0, p \ne 0$。

    若解内仍为 $m$ 阶多项式，因 $q = 0$，左边只有 $m-1$ 次，因而无解。故解内为 $m + 1$ 阶多项式。

    (1.3) 若 $0$ 为特征方程的重根，则 $q = p = 0$。

    若解内多项式次数小于 $m+2$，因 $p = q = 0$，左边小于 $m$ 次，无解。故解内为 $m + 2$ 阶多项式。

    (2) $\mu \ne 0$

    $$
    f(x) = A_m(x)\e^{\mu x}
    $$

    令 $z = y \e^{-\mu x}$，即 $y = z \e^{\mu x}$。

    从而 $y' = \e^{\mu x}(z' + \mu z), y'' = \e^{\mu x}(z'' + 2 \mu z' + \mu^2 z)$，代入方程得

    $$
    \begin{aligned}
        \e^{\mu x}(z'' + 2 \mu z' + \mu^2 z) + \e^{\mu x}p(z' + \mu z) + \e^{\mu x}qz &= A_m(x) \e^{\mu x}\\
        z'' + (2\mu + p)z' + (\mu^2 + p\mu + q)z &= A_m(x)
    \end{aligned}
    $$

    这便化为了 (1) 的情形（新特征方程为 $\eta^2 + (2 \mu + p) \eta + (\mu^2 + p \mu + q)$，$\eta = 0$ 是不是该特征方程的根，等价于 $\mu^2 + p \mu + q$ 是否为 $0$，也即 $\mu$ 是否为原特征方程的根。根的重数也是一样的）。

    </details>
    <!-- }}} -->

!!! info ""
    设 $f(x) = \left( A_s(x) \cos \beta x + B_t(x) \sin \beta x \right) \e^{\alpha x}$，其中 $\alpha, \beta$ 为实常数，$A_s(x), B_t(x)$ 分别为 $x$ 的 $s, t$ 次多项式。令 $m = \max\left\lbrace s, t \right\rbrace$，则方程有形如

    $$
    y^{*} = x^k \left( P_m(x) \cos \beta x + Q_m(x) \sin \beta x \right) \e^{\alpha x}
    $$

    的特解，其中 $k$ 为 $\alpha \pm \beta \i$ 在特征方程 $\lambda^2 + p \lambda + q = 0$ 的根的重数，$P_m(x), Q_m(x)$ 为待定的 $x$ 的 $m$ 次多项式。

    <!-- {{{证明 -->
    <details>
    <summary>证明</summary>

    $$
    \begin{aligned}
        f(x) &= \left[ A_s(x) \cos \beta x + B_t(x) \sin \beta x \right] \e^{\alpha x}\\
        &= \e^{\alpha x} \left( A_s(x) \dfrac{\e^{\beta x \i} + \e^{-\beta x \i}}{2} + B_t(x) \dfrac{\e^{\beta x \i} - \e^{-\beta x \i}}{2\i} \right)\\
        &= \left( \dfrac{A_s(x)}{2} + \dfrac{B_t(x)}{2 \i} \right) \e^{(\alpha + \beta \i)x} + \left( \dfrac{A_s(x)}{2} - \dfrac{B_t(x)}{2 \i} \right) \e^{(\alpha - \beta \i)x}
    \end{aligned}
    $$

    使用上面的结论即可。

    </details>
    <!-- }}} -->

#### 欧拉方程

形如

$$
x^n y^{(n)} + p_1 x^{n-1} y^{(n-1)} + \cdots + p_n y = f(x)
$$

的 $n$ 阶线性微分方程称为 **$n$ 阶欧拉方程**。其中 $p_i$ 为常数，$f(x)$ 为连续函数。

本节主要讨论二阶欧拉方程，即

$$
x^2 y'' + p_1 x y' + p_2 y = f(x)
$$

令 $x = \e^t$，则

$$
\begin{aligned}
    \dfrac{\d y}{\d x} &= \dfrac{\d y}{\d t} \dfrac{\d t}{\d x} = \dfrac{1}{x} \dfrac{\d y}{\d t}\\
    \dfrac{\d^2 y}{\d x^2} &= -\dfrac{1}{x^2}\dfrac{\d y}{\d t} + \dfrac{1}{x} \dfrac{\d t}{\d x}\dfrac{\d \frac{\d y}{\d t}}{\d t}  = \dfrac{1}{x^2} \left[ \dfrac{\d }{\d t}\left( \dfrac{\d }{\d t} - 1 \right) \right] y
\end{aligned}
$$

代入得

$$
\dfrac{\d^2 y}{\d t^2} + (p_1 - 1) \dfrac{\d y}{\d t} + p_2 y = f(\e^t)
$$

即成为了二阶常系数线性微分方程。可用前面的方法求解。

!!! tip ""
    $x < 0$ 时，可令 $t = \ln |x|$，其它同理。
