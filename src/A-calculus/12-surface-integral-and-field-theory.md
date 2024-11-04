---
layout: post
title: 曲面积分与场论
date: 2024-04-16 11:06:31
updated: 2024-04-30 17:49:43
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 第一类曲面积分

设曲面 $S$ 是光滑的，函数 $f(x, y, z)$ 在 $S$ 上有定义，将 $S$ 任意分为 $n$ 小块 $\Delta S_{i}(i=1,2, \cdots, n)$，$\Delta S_{i}$ 同时也表示这个小的曲面面积。

令 $\lambda=\max\limits_{1 \le i \le n}\left\{d(\Delta S_{i})\right\}$。在 $\Delta S_{i}$ 上任取一点 $\left(\xi_{i}, \eta_{i}, \zeta_{i}\right)$，作乘积 $f\left(\xi_{i}, \eta_{i}, \zeta_{i}\right) \Delta S_{i}$，并作和 $\displaystyle \sum_{i=1}^{n} f\left(\xi_{i}, \eta_{i}, \zeta_{i}\right) \Delta S_{i}$。

如果当 $\lambda \to 0$ 时，这个和式的极限总存在（且与曲面 $S$ 的分割和点 $\left(\xi_{i}, \eta_{i}, \zeta_{i}\right)$ 的取法无关），则称此极限为函数 $f(x, y, z)$ 在曲面 $S$ 上的**第一类曲面积分**或**对面积的曲面积分**，记为

$$
\iint_S f(x, y, z) \d S
$$

!!! info ""
    设 $S$ 可参数化为 $\bm{r}(x, y) = (x, y, g(x, y)),\, (x, y) \in D$，且 $g$ 在 $D$ 上连续可微，则

    $$
    \begin{aligned}
        \d S &= |\bm{r}_x' \boldsymbol{\times} \bm{r}_y'| \d x \d y\\
        &= \left|\left(1, 0, \dfrac{\partial g}{\partial x}\right) \boldsymbol{\times} \left(0, 1, \dfrac{\partial g}{\partial y}\right)\right| \d x \d y\\
        &= \left\lvert \left( -\dfrac{\partial g}{\partial x}, -\dfrac{\partial g}{\partial y}, 1 \right)  \right\rvert \d x \d y\\
        &= \sqrt{1 + \left(\frac{\partial g}{\partial x}\right)^2 + \left(\frac{\partial g}{\partial y}\right)^2} \d x \d y
    \end{aligned}
    $$

    则

    $$
    \iint_S f(x, y, z) \d S =\\ \boxed{\iint_D f(x, y, g(x, y)) \sqrt{1 + \left(\frac{\partial g}{\partial x}\right)^2 + \left(\frac{\partial g}{\partial y}\right)^2} \d x \d y}
    $$

!!! info ""
    设 $S$ 可参数化为 $\bm{r}(u, v) = \bigl(x(u, v), y(u, v), z(u, v)\bigr),\, (u, v) \in D$，且 $\bm{r}_u' \boldsymbol{\times} \bm{r}_v' \neq \bm{0}$，则

    $$
    \begin{aligned}
        \d S &= |\bm{r}_u' \boldsymbol{\times} \bm{r}_v'| \d u \d v\\
        &= \sqrt{|\bm{r}_u'|^2 \cdot |\bm{r}_v'|^2 - (\bm{r}_u' \boldsymbol{\cdot} \bm{r}_v')^2} \d u \d v\\
        &= \sqrt{EG - F^2} \d u \d v
    \end{aligned}
    $$

## 第二类曲面积分

考虑光滑曲面。在 $S$ 上取定一点 $P_{0}$，那么 $S$ 在 $P_{0}$ 点有两个方向相反的法向量。任意取定其中一个作为从 $P_{0}$ 点的出发方向，记作 $\bm{n}\left(P_{0}\right)$。

设一动点 $P$ 从 $P_{0}$ 点出发，沿完全落在曲面 $S$ 上的任何一条连续闭曲线 $C$ 变动，再回到点 $P_{0}$，如 $S$ 是非闭的，还假设 $C$ 不越过 $S$ 的边界曲线。当点 $P$ 在 $C$ 上运动时，其法向量 $\bm{n}(P)$ 也随之连续变化，当点 $P$ 返回到起始点 $P_{0}$ 时，$\bm{n}(P)$ 的指向<u>没有发生改变</u>，则称 $S$ 为**双侧曲面**。反之，称 $S$ 为**单侧曲面**。选好法向量（一侧）的曲面称为定向曲面。

为简便起见，仅讨论双侧曲面。并规定与 $z$ 轴正向夹角为钝角的法向量为*指向下方*，同时该法向量确定的一侧为*下侧*。

设一不可压缩流体经过曲面 $S$，其流速与时间 $t$ 无关，仅与其点的位置 $(x, y, z) \in S$ 有关，设为

$$
\bm{v}(x, y, z) = P(x, y, z) \bm{i} + Q(x, y, z) \bm{j} + R(x, y, z) \bm{k}
$$

其中 $P, Q, R$ 都在 $S$ 上连续，则单位时间内流向 $S$ 指定侧流体的质量为流量 $\Phi$[^density]。

[^density]: 假设密度为 $1$。

设 $\bm{n}$ 为平面单位法向量，则有

$$
\begin{aligned}
    \Phi &= \lim_{\lambda \to 0} \sum_{i=1}^{n} \bm{v}_i \boldsymbol{\cdot} \bm{n}_i \Delta S_{i}\\
\end{aligned}
$$

从而引入第二类曲面积分

设 $S$ 为光滑的有向曲面，$S$ 一侧单位法向量为 $\bm{n}(P)$，$\bm{F}(x, y, z)$ 为定义在 $S$ 上的一个向量函数。将 $S$ 任意分成 $n$ 块小区面 $\Delta S_i$，在 $\Delta S_i$ 上任取一点 $P_i(\xi_i, \eta_i, \zeta_i)$，若当各小块直径最大值 $\lambda \to 0$ 时，和式

$$
\lim_{\lambda \to 0} \sum_{i=1}^{n} \bm{F}\left(\xi_i, \eta_i, \zeta_i\right) \boldsymbol{\cdot} \bm{n}_i \Delta S_i
$$

存在，且与 $S$ 分割和 $P_i(\xi_i, \eta_i, \zeta_i)$ 的取法无关，则称此极限为函数 $\bm{F}(x, y, z)$ 在曲面 $S$ 上的**第二类曲面积分**，记为

$$
\iint_S \bm{F}(x, y, z) \boldsymbol{\cdot} \bm{n}(x, y, z) \d S
$$

或

$$
\iint_S \bm{F} \boldsymbol{\cdot} \d \bm{S}
$$

设 $\bm{n}$ 方向角为 $\alpha, \beta, \gamma$，则

$$
\iint \bm{F} \boldsymbol{\cdot} \bm{n} \d S = \iint (P \cos \alpha + Q \cos \beta + R \cos \gamma) \d S
$$

这也就是第二类曲面积分转化为第一类曲面积分的方法。

又注意到（例如第一个，可视为 $S$ 在 $yOz$ 平面的*有向投影面积*）

$$
\left\lbrace\begin{aligned}
    \cos \alpha \d S &= \d y \d z\\
    \cos \beta \d S &= \d z \d x\\
    \cos \gamma \d S &= \d x \d y
\end{aligned}\right.
$$

从而有

$$
\iint \bm{F} \boldsymbol{\cdot} \bm{n} \d S = \boxed{\iint P \d y \d z + Q \d z \d x + R \d x \d y}
$$

因此第二类曲面积分也称为**对坐标的曲面积分**。

!!! info ""
    设 $S$ 为一有向曲面，其方程为

    $$
    z = f(x, y),\qquad (x, y) \in D_{xy}
    $$

    且函数 $f(x, y)$ 在 $D_{xy}$ 上连续可微。函数 $P, Q, R$ 为定义在曲面 $S$ 上的连续函数（即 $P\bigl(x, y, f(x, y)\bigr)$ 等），则有

    $$
    \begin{aligned}
        \iint_S P \d y \d z + Q \d z \d x + R \d x \d y &= \boxed{
                \pm \iint_{D_{xy}} \left( -P \frac{\partial f}{\partial x} - Q \frac{\partial f}{\partial y} + R \right) \d x \d y
            }
    \end{aligned}
    $$

    其中正负号取决于曲面 $S$ 的定向，<u>法向量指向上侧时取正，反之取负</u>。

    因为法向量 $\left( -\dfrac{\partial f}{\partial x}, -\dfrac{\partial f}{\partial y}, 1  \right)$ 的方向是指向上侧的（靠近 $z$ 轴正方向一侧）。

    另外换成 $y = g(z, x)$ 或 $x = h(y, z)$ 也是一样的，包括正负号的选取，不再赘写。

从而有推论

!!! info ""
    设 $S$ 方程为 $z = f(x, y),\, (x, y) \in D_{xy}$，函数 $f$ 在 $D_{xy}$ 上连续可微，则

    $$
    \iint_S R(x, y, z) \d x \d y = \pm \iint_{D_{xy}} R\bigl(x, y, f(x, y)\bigr) \d x \d y
    $$

对于参数方程，有

!!! info ""
    设 $S$ 为一有向曲面，其参数方程为

    $$
    \left\lbrace\begin{aligned}
        x &= x(u, v) \\
        y &= y(u, v) \\
        z &= z(u, v)
    \end{aligned}\right.,\qquad (u, v) \in D
    $$

    且函数 $x, y, z$ 在 $D$ 上连续可微。函数 $P, Q, R$ 为定义在曲面 $S$ 上的连续函数，则有

    $$
    \begin{aligned}
        \iint_S P \d y \d z + Q \d z \d x + R \d x \d y &= \boxed{
                \pm \iint_{D} (PA + QB + RC) \d u \d v
            }
    \end{aligned}
    $$

    其中

    $$
    \left\lbrace\begin{aligned}
        A &= \dfrac{D(y, z)}{D(u, v)} \\
        B &= \dfrac{D(z, x)}{D(u, v)} \\
        C &= \dfrac{D(x, y)}{D(u, v)}
    \end{aligned}\right.
    $$

    当 $(A, B, C)$ 方向与曲面 $S$ 的定向一致时取正，反之取负。

## 高斯公式（Gauss 公式）

高斯公式是格林公式的推广，也称为散度定理、奥式公式、奥斯特洛格拉德斯基-高斯公式（Ostrogradsky-Gauss 公式，奥-高公式）。

!!! info ""
    设空间闭区域 $V$ 是由分片光滑的闭曲面 $S$ 围成，函数 $P, Q, R$ 在 $V$ 上具有一阶连续偏导数，则有

    $$
    \iint_S P \d y \d z + Q \d z \d x + R \d x \d y = \iiint_V \left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} \right) \d V
    $$

    或

    $$
    \iint_S (P \cos \alpha + Q \cos \beta + R \cos \gamma) \d S = \iiint_V \left( \frac{\partial P}{\partial x} + \frac{\partial Q}{\partial y} + \frac{\partial R}{\partial z} \right) \d V
    $$

    这里 $S$ 是 $V$ 的边界曲面的外侧，$\alpha, \beta, \gamma$ 是 $S$ 在点 $(x, y, z)$ 处的法向量的方向角。

<!-- {{{找规律 -->
<details>
<summary>找规律</summary>

猜测啊，$n$ 重积分，有 $x_1, \cdots, x_n$ 个变量，有

$$
\overbrace{\int \dotsi \int_S}^{n-1} \sum_{i=1}^{n} f_i(x_1, \cdots, x_n) \boxed{\d x_{i+1}\cdots \d x_{i-1}} = \overbrace{\int \dotsi \int_V}^{n} \sum_{i=1}^{n} \dfrac{\partial f_i}{\partial x_i} \d x_i \cdots \d x_{i-1}
$$

或

$$
\overbrace{\int \dotsi \int_S}^{n-1} \sum_{i=1}^{n} f_i(x_1, \cdots, x_n) \cos \theta_i \d S = \overbrace{\int \dotsi \int_V}^{n} \sum_{i=1}^{n} \dfrac{\partial f_i}{\partial x_i} \d x_i \cdots \d x_{i-1}
$$


方框中的 $\d x_{i+1}\cdots \d x_{i-1}$，意思是将 $\d x_1, \cdots, \d x_n$ 形成一个环（即 $\d x_n$ 下一个是 $\d x_1$），然后将 $\d x_i$ 从环中拿出来，剩下的就是 $\d x_{i+1}\cdots \d x_{i-1}$。

还记得格林公式为

$$
\int_C P \d x + Q \d y = \iint_D \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \d x \d y
$$

实际上就是

$$
\int_C Q \d y + P \d x = \iint_D \dfrac{\partial Q}{\partial x}\d x \d y + \dfrac{\partial P}{\partial y} \d y \d x
$$

只是戏言，辅助记忆的伎俩。

高斯定理证明懒得写了。

</details>
<!-- }}} -->

!!! info ""
    向量场 $\bm{F}$ 的**散度**（sàn dù[^pinyin], divergence）定义为

    $$
    \operatorname{div} \bm{F} = \grad \boldsymbol{\cdot} \bm{F}
    $$

    [^pinyin]: 别说，还真是 sǎn 念得更顺，都差点忘记之前看到的读音是四声了。

则高斯定理可写作

$$
\oiint_S \bm{F} \boldsymbol{\cdot} \d \bm{S} = \iiint_V \operatorname{div} \bm{F} \d V
$$

即向量场 $\bm{F}$ 在闭曲面 $S$ 上的通量，等于该向量场的散度在包围该闭曲面的体积 $V$ 上的体积分。（$S = \partial V$）

高斯公式中取 $P = x, Q = y, R = z$，则有

$$
\iint_S x \d y \d z + y \d z \d x + z \d x \d y = \iiint_V 3 \d V = 3 V
$$

即

$$
\begin{aligned}
    V &= \dfrac{1}{3} \iint_{\partial V} x \d y \d z + y \d z \d x + z \d x \d y\\
    &= \iint_{\partial V} x \d y \d z\\
    &= \iint_{\partial V} y \d z \d x\\
    &= \iint_{\partial V} z \d x \d y
\end{aligned}
$$

## 斯托克斯公式（Stokes 公式）

!!! info ""
    设 $S$ 为分片光滑的有向曲面，其边界 $\Gamma$ 为逐段光滑的有向闭曲线，$\Gamma$ 正向与 $S$ 正侧符合右手法则[^right-hand-rule]。函数 $P, Q, R$ 在 $S, \Gamma$ 上具有一阶连续偏导数，则有

    [^right-hand-rule]: 右手除大拇指外四指依 $\Gamma$ 正向绕行时（掌心朝曲面），大拇指所指的方向与 $S$ 上法向量所指的方向一致。此时称 $\Gamma$ 为有向曲面 $S$ 的正向边界曲线。或者说，记曲面方向向量为 $\bm{n}$，$\Gamma$ 在 $S$ 中的外法向量为 $\bm{\nu}$，则规定 $\Gamma$ 正方向向量为 $\bm{t} = \bm{n} \boldsymbol{\times} \bm{\nu}$。

    $$
    \oint_{\Gamma} P \d x + Q \d y + R \d z =\\  \iint_S \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z} \right) \d y \d z + \left( \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x} \right) \d z \d x + \left( \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right) \d x \d y
    $$

    ---

    记成

    $$
    \iint_S \left( \dfrac{\partial R}{\partial y}\d y \d z + \dfrac{\partial Q}{\partial z}\d z \d y \right) + \left( \dfrac{\partial P}{\partial z}\d z \d x + \dfrac{\partial R}{\partial x}\d x \d z \right) + \left( \dfrac{\partial Q}{\partial x}\d x \d y + \dfrac{\partial P}{\partial y}\d y \d x \right)
    $$

    就行了。

    或者

    $$
    \begin{aligned}
        \oint_{\Gamma} P \d x + Q \d y + R \d z &= \iint_S \begin{vmatrix}
            \d y \d z & \d z \d x & \d x \d y \\
            \dfrac{\partial }{\partial x} & \dfrac{\partial }{\partial y} & \dfrac{\partial }{\partial z} \\
            P & Q & R
        \end{vmatrix}\\
        &= \iint_S \begin{vmatrix}
            \cos \alpha & \cos \beta & \cos \gamma \\
            \dfrac{\partial }{\partial x} & \dfrac{\partial }{\partial y} &\dfrac{\partial }{\partial z}  \\
            P & Q & R
        \end{vmatrix} \d S
    \end{aligned}
    $$

    其中 $\alpha, \beta, \gamma$ 是 $S$ 在点 $(x, y, z)$ 处的法向量的方向角。

<!-- {{{证明 -->
<details>
<summary>证明</summary>

> 未认真看

设 $S$ 可参数化为 $\bm{r}(u, v) = \bigl(x(u, v), y(u, v), z(u, v)\bigr),\quad (u, v) \in D$（如有必要可分割），不妨设 $S$ 的方向与 $\bm{r}_u' \boldsymbol{\times} \bm{r}_v'$ 的方向一致。则

$$
\begin{aligned}
    \oint_{\Gamma} \bm{F} \boldsymbol{\cdot} \d \bm{r} &= \oint_{\Gamma} P \d x + Q \d y + R \d z\\
    &= \oint_{\partial D} P\left( \dfrac{\partial x}{\partial u} \d u + \dfrac{\partial x}{\partial v}\d v \right) + Q\left( \dfrac{\partial y}{\partial u} \d u + \dfrac{\partial y}{\partial v}\d v \right) + R\left( \dfrac{\partial z}{\partial u} \d u + \dfrac{\partial z}{\partial v}\d v \right)\\
    &= \oint_{\partial D} \left(P \dfrac{\partial x}{\partial u} + Q \dfrac{\partial y}{\partial u} + R \dfrac{\partial z}{\partial u}\right) \d u + \left(P \dfrac{\partial x}{\partial v} + Q \dfrac{\partial y}{\partial v} + R \dfrac{\partial z}{\partial v}\right) \d v\\
    &= \iint_D \left[- \dfrac{\partial }{\partial v}\left(P \dfrac{\partial x}{\partial u} + Q \dfrac{\partial y}{\partial u} + R \dfrac{\partial z}{\partial u}\right) + \dfrac{\partial }{\partial u}\left(P \dfrac{\partial x}{\partial v} + Q \dfrac{\partial y}{\partial v} + R \dfrac{\partial z}{\partial v}\right)\right] \d u \d v\\
    &= \iint_D \left[- \left(\dfrac{\partial P}{\partial \\v} \dfrac{\partial x}{\partial u} + \dfrac{\partial Q}{\partial v} \dfrac{\partial y}{\partial u} + \dfrac{\partial R}{\partial v} \dfrac{\partial z}{\partial u}\right) + \left(\dfrac{\partial P}{\partial u} \dfrac{\partial x}{\partial v} + \dfrac{\partial Q}{\partial u} \dfrac{\partial y}{\partial v} + \dfrac{\partial R}{\partial u} \dfrac{\partial z}{\partial v}\right)\right] \d u \d v\\
    &= \iint_D \biggl[-\left(\dfrac{\partial P}{\partial x} \dfrac{\partial x}{\partial v} + \dfrac{\partial P}{\partial y} \dfrac{\partial y}{\partial v} + \dfrac{\partial P}{\partial z} \dfrac{\partial z}{\partial v}\right) \dfrac{\partial x}{\partial u} - \left(\dfrac{\partial Q}{\partial x} \dfrac{\partial x}{\partial v} + \dfrac{\partial Q}{\partial y} \dfrac{\partial y}{\partial v} + \dfrac{\partial Q}{\partial z} \dfrac{\partial z}{\partial v}\right) \dfrac{\partial x}{\partial u}- \left(\dfrac{\partial R}{\partial x} \dfrac{\partial x}{\partial v} + \dfrac{\partial R}{\partial y} \dfrac{\partial y}{\partial v} + \dfrac{\partial R}{\partial z} \dfrac{\partial z}{\partial v}\right) \dfrac{\partial z}{\partial u} + \\
    & \left(\dfrac{\partial P}{\partial x} \dfrac{\partial x}{\partial u} + \dfrac{\partial P}{\partial y} \dfrac{\partial y}{\partial u} + \dfrac{\partial P}{\partial z} \dfrac{\partial z}{\partial u}\right) \dfrac{\partial x}{\partial v} + \left(\dfrac{\partial Q}{\partial x} \dfrac{\partial x}{\partial u} + \dfrac{\partial Q}{\partial y} \dfrac{\partial y}{\partial u} + \dfrac{\partial Q}{\partial z} \dfrac{\partial z}{\partial u}\right) \dfrac{\partial y}{\partial v} + \left(\dfrac{\partial R}{\partial x} \dfrac{\partial x}{\partial u} + \dfrac{\partial R}{\partial y} \dfrac{\partial y}{\partial u} + \dfrac{\partial R}{\partial z} \dfrac{\partial z}{\partial u}\right) \dfrac{\partial z}{\partial v}\biggr] \d u \d v\\
    &= \iint_D \left[\left(\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}\right) \dfrac{D(x, y)}{D(u, v)} + \left(\dfrac{\partial R}{\partial y} - \dfrac{\partial Q}{\partial z}\right) \dfrac{D(y, z)}{D(u, v)} + \left(\dfrac{\partial P}{\partial z} - \dfrac{\partial R}{\partial x}\right) \dfrac{D(z, x)}{D(u, v)}\right] \d u \d v\\
    &= \iint_D \left(\dfrac{\partial R}{\partial y} - \dfrac{\partial Q}{\partial z}, \dfrac{\partial P}{\partial z} - \dfrac{\partial R}{\partial x}, \dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}\right) \boldsymbol{\cdot} \left(\bm{r}_u' \boldsymbol{\times} \bm{r}_v'\right) \d u \d v\\
    &= \iint_D \left(\dfrac{\partial R}{\partial y} - \dfrac{\partial Q}{\partial z}\right) \d y \d z + \left(\dfrac{\partial P}{\partial z} - \dfrac{\partial R}{\partial x}\right) \d z \d x + \left(\dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}\right) \d x \d y
\end{aligned}
$$

</details>
<!-- }}} -->


!!! info ""
    向量场 $\bm{F}$ 的**旋度**（curl）定义为

    $$
    \operatorname{curl} \bm{F} = \grad \boldsymbol{\times} \bm{F}
    $$

    也可记作 $\operatorname{rot} \bm{F}$（回转度，rotation）。

    ---

    例如 $\bm{F} = P \bm{i} + Q \bm{j} + R \bm{k}$，则有

    $$
    \begin{aligned}
        \operatorname{curl} \bm{F} &= \grad \boldsymbol{\times} \bm{F}\\
        &= \left(\dfrac{\partial }{\partial x}, \dfrac{\partial }{\partial y}, \dfrac{\partial }{\partial z}\right) \boldsymbol{\times} (P, Q, R)\\
        &= \left(\dfrac{\partial R}{\partial y} - \dfrac{\partial Q}{\partial z}, \dfrac{\partial P}{\partial z} - \dfrac{\partial R}{\partial x}, \dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y}\right)\\
        &= \left( \dfrac{\partial R}{\partial y} - \dfrac{\partial Q}{\partial z} \right) \bm{i} + \left( \dfrac{\partial P}{\partial z} - \dfrac{\partial R}{\partial x} \right) \bm{j} + \left( \dfrac{\partial Q}{\partial x} - \dfrac{\partial P}{\partial y} \right) \bm{k}\\
        &= \begin{vmatrix}
            \bm{i} & \bm{j} & \bm{k}\\
            \dfrac{\partial }{\partial x} & \dfrac{\partial }{\partial y} & \dfrac{\partial }{\partial z}\\
            P & Q & R
        \end{vmatrix}
    \end{aligned}
    $$

则斯托克斯定理可写作

$$
\oint_{\Gamma} \bm{F} \boldsymbol{\cdot} \d \bm{r} = \iint_S \operatorname{curl} \bm{F} \boldsymbol{\cdot} \d \bm{S}
$$

即向量场 $\bm{F}$ 沿闭曲线 $\Gamma$ 的环量，等于该向量场的旋度在该闭曲线围成的曲面 $S$ 上的通量。（$\Gamma = \partial S$）

## 空间曲线积分与路径无关的条件

!!! info ""
    设 $V$ 为单连通区域，$P, Q, R$ 在 $V$ 内具有一阶连续偏导数，则空间曲线积分

    $$
    \int_C P \d x + Q \d y + R \d z
    $$

    在 $V$ 内与路径无关的充要条件是

    $$
    \left\lbrace\begin{aligned}
        \dfrac{\partial R}{\partial y} &= \dfrac{\partial Q}{\partial z} \\
        \dfrac{\partial P}{\partial z} &= \dfrac{\partial R}{\partial x} \\
        \dfrac{\partial Q}{\partial x} &= \dfrac{\partial P}{\partial y}
    \end{aligned}\right.
    $$

    在 $V$ 内恒成立。

类似地，有：

设空间区域 $V$ 是单连通区域，函数 $P, Q, R$ 在 $V$ 内具有一阶连续偏导数，则满足上面的条件，等价于存在 $V$ 内的可微函数 $u(x, y, z)$ 使得

$$
\d u = P \d x + Q \d y + R \d z
$$

且

$$
u(x, y, z) = \int_{(x_0, y_0, z_0)}^{(x, y, z)} P \d x + Q \d y + R \d z
$$

## 场论初步

**数量场**

$$
f \colon \R^n \to \R
$$

**向量场**

$$
\bm{f} \colon \R^n \to \R^n
$$

依赖于时间的场称为<u>不定长场</u>或<u>不稳定场</u>，不依赖于时间的场称为<u>定长场</u>或<u>稳定场</u>。

对于数量场，我们有梯度、散度、旋度等概念。

数量场 $f(x, y, z)$ 有等值面 $f(x, y, z) = c$。

梯度、旋度、散度之前都介绍过了，这里整合一下。

### 梯度

!!! info ""
    $$
    \grad f = \left( \dfrac{\pd f}{\pd x}, \dfrac{\pd f}{\pd y}, \dfrac{\pd f}{\pd z} \right)
    $$

    称为函数 $f(x, y, z)$ 的**梯度**（gradient），记作 $\grad f$ 或 $\operatorname{grad} f$ 或 $\dfrac{\pd f}{\pd x} \bm{i} + \dfrac{\pd f}{\pd y} \bm{j} + \dfrac{\pd f}{\pd z} \bm{k}$。

!!! info ""
    $$
    \Delta = \grad \boldsymbol{\cdot} \grad = \dfrac{\pd^2}{\pd x^2} + \dfrac{\pd^2}{\pd y^2} + \dfrac{\pd^2}{\pd z^2}
    $$

    称为**拉普拉斯算子**（Laplace operator）。

!!! note ""
    1. $\grad C = \bm{0}$
    2. $\grad (u \pm v) = \grad u + \grad v$
    3. $\grad (uv) = u \grad v + v \grad u$
    4. $\grad \left( \dfrac{u}{v} \right) = \dfrac{v \grad u - u \grad v}{v^2}$
    5. $\grad \varphi(u) = \varphi'(u) \grad u$
    6. $\grad \varphi(u, v) = \dfrac{\partial \varphi}{\partial u} \grad u + \dfrac{\partial \varphi}{\partial v} \grad v$

### 散度

向量场 $\bm{A}$ 通过曲面 $S$ 指定侧的流量（通量）定义为

$$
\Phi = \iint_S \bm{A} \d \bm{S}
$$

!!! info ""
    向量场 $\bm{A}$ 的**散度**（divergence）定义为

    $$
    \operatorname{div} \bm{A}(M_0) = \lim_{\Omega \to M_0} \dfrac{\displaystyle \iint_{\partial \Omega} \bm{A} \d \bm{S}}{\displaystyle \iiint_{\Omega}\d x \d y \d z}
    $$

    即

    $$
    \operatorname{div} \bm{A} = \grad \boldsymbol{\cdot} \bm{A}
    $$

若散度在一点*大于零*，表明在该点附近流向该点的量少于该点流出的量，称该点为「源」，若散度在一点处*小于零*，则表明在该点附近流向该点的量多于自该点流出的量，称该点为「漏」。

若向量场 $\bm{A}$ 散度 $\operatorname{div} \bm{A}$ 处处为零，则称 $\bm{A}$ 为**无源场**（管型场）。

!!! note ""
    1. $\operatorname{div}(\lambda \bm{A}) = \lambda \operatorname{div} \bm{A}$
    2. $\operatorname{div}(\bm{A}_1 \pm \bm{A}_2) = \operatorname{div} \bm{A}_1 \pm \operatorname{div} \bm{A}_2$
    3. $\operatorname{div} (\varphi \bm{A}) = \varphi \operatorname{div} \bm{A} + \bm{A} \boldsymbol{\cdot} \grad \varphi$（$\varphi$ 为数量场）
    4. $\operatorname{div}(\grad \varphi) = \Delta \varphi$

### 旋度

向量场 $\bm{A}$ 沿曲线 $C$ 的环流量定义为

$$
I = \oint_C \bm{A} \boldsymbol{\cdot} \d \bm{r}
$$

!!! info ""
    向量场 $\bm{A}$ 的**旋度**（curl）定义为

    $$
    \operatorname{curl} \bm{A} = \grad \boldsymbol{\times} \bm{A}
    $$

    也可记作 $\operatorname{rot} \bm{A}$（回转度，rotation）。

物理含义是，流速场 $\bm{A}$ 沿闭曲线 $C$ 整体上看是否旋转。

!!! note ""
    1. $\operatorname{rot} (\lambda \bm{A}) = \lambda \operatorname{rot} \bm{A}$
    2. $\operatorname{rot} (\bm{A}_1 \pm \bm{A}_2) = \operatorname{rot} \bm{A}_1 \pm \operatorname{rot} \bm{A}_2$
    3. $\operatorname{rot} (\varphi \bm{A}) = \varphi \operatorname{rot} \bm{A} + \grad \varphi \boldsymbol{\times} \bm{A}$（$\varphi$ 为数量场）
    4. $\operatorname{div}(\bm{A} \boldsymbol{\times} \bm{B}) = \bm{B} \boldsymbol{\cdot} \operatorname{rot} \bm{A} - \bm{A} \boldsymbol{\cdot} \operatorname{rot} \bm{B}$
    5. $\operatorname{rot}(\grad \varphi) = \bm{0}$
    6. $\operatorname{div}(\operatorname{rot} \bm{A}) = 0$

### 有势场

!!! info ""
    若向量场 $\bm{A}$ 可表示为某个数量场 $\varphi$ 的梯度，即 $\bm{A} = \grad \varphi$，则称 $\bm{A}$ 为**有势场**（位势场、保守场，potential field）。

向量场 $\bm{A}$ 为有势场的<u>充要条件</u>为 $\operatorname{rot} \bm{A} = \bm{0}$。

若向量场 $\bm{A}$ 旋度处处为零，则称向量场 $\bm{A}$ 为**无旋场**。则有势场为无旋场。

若向量场 $\bm{A}$ 既是无源场又是无旋场，则称 $\bm{A}$ 为**调和场**。

调和场 $\bm{A}$ 的势函数 $f(x, y, z)$ 满足*拉普拉斯方程*

$$
\Delta f = \dfrac{\partial^2 f}{\partial x^2} + \dfrac{\partial^2 f}{\partial y^2} + \dfrac{\partial^2 f}{\partial z^2} = 0
$$
