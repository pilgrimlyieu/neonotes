---
layout: post
title: 偏导数和全微分
date: 2023-11-30 15:44:16
updated: 2024-04-30 17:50:31
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 偏导数

!!! info ""
    设 $P_0(x_0, y_0) \in \R^2$，函数 $z = f(x, y)$ 在 $P_0$ 的 $\delta$ 邻域 $N_{\delta}(P_0)$ 内有定义，在 $N_{\delta}(P_0)$ 中固定 $y = y_0$，得到一个关于 $x$ 的函数 $f(x, y_0)$，若 $f(x, y_0)$ 在 $x = x_0$ 处可导，即

    $$
    \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x, y_0) - f(x_0, y_0)}{\Delta x}
    $$

    存在，则称**函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 处对 $x$ 的*偏导数***存在，记作

    $$
    f'_x(x_0, y_0),\\
    f'_1(x_0, y_0),\\
    \frac{\partial f}{\partial x}(x_0, y_0),\\
    \frac{\partial f}{\partial x}\as_{\left(x_0, y_0\right)},\\
    \frac{\partial z}{\partial x}\left(x_0, y_0\right),\\
    \frac{\partial z}{\partial x}\as_{\left(x_0, y_0\right)}
    $$

    同理可定义**函数 $z = f(x, y)$ 在点 $(x_0, y_0)$ 处对 $y$ 的*偏导数***。

    若二元函数 $f(x, y)$ 在点 $(x_0, y_0)$ 处对 $x,\, y$ 的偏导数均存在，则称 $f(x, y)$ 在点 $(x_0, y_0)$ 处**可偏导**。若 $f(x, y)$ 在 $G$ 中每一点都可偏导，则称 $f(x, y)$ 在 $G$ 上**可偏导**。

    设 $(x_0, y_0) \in G$，函数 $z = f(x, y)$ 在 $(x_0, y_0)$ 处对 $x$ 的偏导数记为

    $$
    f'_x(x_0, y_0),\\
    f'_x,\\
    f'_1,\\
    \frac{\partial f}{\partial x},\\
    \frac{\partial z}{\partial x}
    $$

    在 $(x_0, y_0)$ 处对 $y$ 的偏导数、$n$ 元函数的偏导数等类似。

偏导数的几何意义，可以看作是多元函数在某一方向上的变化率。

例如，对于二元函数 $z = f(x, y)$ 在空间中为一个曲面，$z = f(x, y_0)$ 表示 $z$ 与平面 $y = y_0$ 的交线，也就是说，$f$ 对 $x$ 的偏导数 $f'_x(x_0, y_0)$ 表示 $P(x_0, y_0, f(x_0, y_0))$ 点处切线对 $x$ 轴的斜率，这条切线显然与 $x O z$ 平面平行。

!!! info ""
    设函数 $z = f(x, y)$ 在 $P_0 (x_0, y_0)$ 的某邻域 $N_{\delta}(P_0)$ 内可偏导，且 $f'_x(x, y),\, f'_y(x, y)$ 在 $N_{\delta}(P_0)$ 内有界，则函数 $z = f(x, y)$ 在 $P_0$ 处连续。

    ---

    证明：

    $$
    \begin{aligned}
        \Delta z &= f(x_0 + \Delta x, y_0 + \Delta y) - f(x_0, y_0)\\
        &= \Bigl(f(x, y) - f(x_0, y)\Bigr) + \Bigl(f(x_0, y) - f(x_0, y_0)\Bigr)\\
    \end{aligned}
    $$

    由一元函数微分中值定理知存在 $\xi,\, \eta$ 分别介于 $x$ 与 $x_0$，$y$ 与 $y_0$ 之间，使得

    $$
    \Delta z = f'_x(\xi, y) (x - x_0) + f'_y(x_0, \eta) (y - y_0)
    $$

    由于 $f'_x(x, y),\, f'_y(x, y)$ 在 $N_{\delta}(P_0)$ 内有界，故

    $$
    \lim_{\substack{x \to x_0\\ y \to y_0}} \Delta z = 0
    $$

    即 $f(x, y)$ 在 $P_0$ 处连续。

不同于一元函数，对于多元函数，即使其在某点处可偏导，也不一定在该点处连续。

例如函数

$$
f(x, y) = \begin{cases}
    \dfrac{xy}{x^2 + y^2}, & (x, y) \ne (0, 0)\\
    0, & (x, y) = (0, 0)
\end{cases}
$$

有

$$
\begin{aligned}
    f'_x(0, 0) &= \lim\limits_{x \to 0} \frac{f(x, 0) - f(0, 0)}{x - 0} &= \lim\limits_{x \to 0} \frac{0 - 0}{x} &= 0\\
    f'_y(0, 0) &= \lim\limits_{y \to 0} \frac{f(0, y) - f(0, 0)}{y - 0} &= \lim\limits_{y \to 0} \frac{0 - 0}{y} &= 0
\end{aligned}
$$

即 $f(x, y)$ 在 $(0, 0)$ 处可偏导，但

$$
\lim_{\substack{x \to 0\\ y \to 0}} f(x, y)
$$

不存在，故 $f(x, y)$ 在 $(0, 0)$ 处不连续。

极限不存在的证明：

当 $(x, y)$ 沿着 $y = x$ 趋于 $(0, 0)$ 时，有

$$
\begin{aligned}
    \lim_{\substack{x \to 0\\ y \to 0}} f(x, y) &= \lim_{x \to 0} \frac{x^2}{x^2 + x^2}\\
    &= \frac{1}{2}
\end{aligned}
$$

当 $(x, y)$ 沿着 $y = 0$ 趋于 $(0, 0)$ 时，有

$$
\begin{aligned}
    \lim_{\substack{x \to 0\\ y \to 0}} f(x, y) &= \lim_{x \to 0} \frac{0}{x^2}\\
    &= 0
\end{aligned}
$$

两个极限不相等，故 $f(x, y)$ 在 $(0, 0)$ 处不存在极限。

而连续也无法推出可偏导，这点比较显然，毕竟一元函数连续无法推出可导。

类似于一元函数的高阶导数，多元函数也有高阶偏导数的概念。由于多元函数的自变量有多个，因此高阶偏导数有多种求法，例如对于二元函数 $z = f(x, y)$，可以先对 $x$ 求偏导，再对 $y$ 求偏导，也可以先对 $y$ 求偏导，再对 $x$ 求偏导，还可以对 $x$ 求两次偏导，也可以对 $y$ 求两次偏导，等等。具体求法与一元函数类似，这里不再赘述。

!!! info ""
    若二阶混合偏导数 $f''_{xy}(x, y)$ 与 $f''_{yx}(x, y)$ 在点 $(x, y)$ 处<u>连续</u>，则

    $$
    f''_{xy}(x, y) = f''_{yx}(x, y)
    $$

    即混合偏导数与求导次序无关，有

    $$
    \frac{\partial^2 f}{\partial x \partial y} = \frac{\partial^2 f}{\partial y \partial x}
    $$

    ---

    证明：

    记辅助函数

    $$
    F(h, k) = f(x + h, y + k) - f(x + h, y) - f(x, y + k) + f(x, y)
    $$

    其中 $\left\lvert h \right\rvert,\, \left\lvert k \right\rvert$ 充分小时，令

    $$
    \varphi (X) = f(X, y + k) - f(X, y)
    $$

    则

    $$
    F(h, k) = \varphi (x + h) - \varphi (x)
    $$

    运用一元函数的拉格朗日中值定理，存在 $\theta_1,\, \theta_2 \in (0, 1)$，使得

    $$
    \begin{aligned}
        F(h, k) &= \varphi'(x + \theta_1 h) h\\
        &= \Bigl( f'_x(x + \theta_1 h, y + k) - f'_x(x + \theta_1 h, y) \Bigr) h\\
        &= f''_{xy}(x + \theta_1 h, y + \theta_2 k) h k
    \end{aligned}
    $$

    同理令

    $$
    \psi (Y) = f(x + h, Y) - f(x, Y)
    $$

    又存在 $\theta_3,\, \theta_4 \in (0, 1)$，使得

    $$
    \begin{aligned}
        F(h, k) &= \psi'(y + \theta_3 k) k\\
        &= \Bigl( f'_y(x + h, y + \theta_3 k) - f'_y(x, y + \theta_3 k) \Bigr) k\\
        &= f''_{yx}(x + \theta_4 h, y + \theta_3 k) h k
    \end{aligned}
    $$

    即

    $$
    f''_{xy}(x + \theta_1 h, y + \theta_2 k) = f''_{yx}(x + \theta_4 h, y + \theta_3 k)
    $$

    令 $h \to 0,\, k \to 0$，由于 $f''_{xy}(x, y),\, f''_{yx}(x, y)$ 在点 $(x, y)$ 处连续，故

    $$
    f''_{xy}(x, y) = f''_{yx}(x, y)
    $$

上面的结论可以推广到 $n$ 元函数的偏导数上，只需记为分式形式即可。

## 全微分

!!! info ""
    设函数 $z = f(x, y)$ 在点 $P(x, y)$ 的某邻域内有定义，若函数 $z = f(x, y)$ 在点 $P$ 的全增量

    $$
    \Delta z = f(x + \Delta x, y + \Delta y) - f(x, y)
    $$

    可表示为

    $$
    \Delta z = A \Delta x + B \Delta y + o(\rho)
    $$

    其中 $A,\, B$ 只与 $P$ 有关，而与 $\Delta x,\, \Delta y$ 无关，且 $\rho = \sqrt{(\Delta x)^2 + (\Delta y)^2}$，$o(\rho)$ 是当 $\rho \to 0^{+}$ 时比 $\rho$ 高阶的无穷小，则称**函数 $f(x, y)$ 在点 $(x, y)$ 处可微**，其线性部分 $A \Delta x + B \Delta y$ 称为**函数 $z = f(x, y)$ 在点 $(x, y)$ 处的*全微分***，记作

    $$
    \d z = A \Delta x + B \Delta y
    $$

!!! info ""
    设函数 $z = f(x, y)$ 在 $(x, y)$ 处可微，则函数 $f(x, y)$ 在 $(x, y)$ 处连续。

    ---

    证明：

    $$
    \begin{aligned}
        \lim_{\substack{\Delta x \to 0\\\Delta y \to 0}} \Delta z &= \lim_{\substack{\Delta x \to 0\\\Delta y \to 0}} \left(A \Delta x + B \Delta y + o(\rho)\right)\\
        &= 0
    \end{aligned}
    $$

    即 $f(x, y)$ 在 $(x, y)$ 处连续。

!!! info ""
    设函数 $z = f(x, y)$ 在 $(x, y)$ 处可微，则

    $$
    \d z = \dfrac{\pd z}{\pd x} \d x + \dfrac{\pd z}{\pd y} \d y
    $$

    ---

    证明：

    令 $\Delta y = 0$，得

    $$
    \dfrac{\Delta z}{\Delta x} = A + \dfrac{o(\rho)}{\Delta x}
    $$

    从而

    $$
    \begin{aligned}
        \dfrac{\pd z}{\pd x} &= \lim_{\Delta x \to 0} \dfrac{\Delta z}{\Delta x}\\
        &= A + \lim_{\Delta x \to 0} \dfrac{o(\left\lvert \Delta x \right\rvert)}{\Delta x}\\
        &= A
    \end{aligned}
    $$

    同理可得 $\dfrac{\pd z}{\pd y} = B$，故

    $$
    \begin{aligned}
        \d z &= A \d x + B \d y\\
        &= \dfrac{\pd z}{\pd x} \Delta x + \dfrac{\pd z}{\pd y} \Delta y
    \end{aligned}
    $$

    类似一元函数微分的证明，分别取函数 $f(x, y) = x$ 和 $f(x, y) = y$，可得

    $$
    \d x = \Delta x,\quad \d y = \Delta y
    $$

    从而

    $$
    \d z = \dfrac{\pd z}{\pd x} \d x + \dfrac{\pd z}{\pd y} \d y
    $$

由上面的内容可知，连续和可偏导是可微的**必要条件**，但不是充分条件。

!!! example ""
    设 $f(x, y) = \begin{cases} \dfrac{xy}{\sqrt{x^2 + y^2}}, & (x, y) \ne (0, 0)\\ 0, & (x, y) = (0, 0) \end{cases}$，可以证明 $f(x, y)$ 在 $(0, 0)$ 处连续、可偏导，但不可微。

    设 $x = \rho \cos \theta,\, y = \rho \sin \theta$，从而

    $$
    \begin{aligned}
        \lim_{\substack{x \to 0\\ y \to 0}} f(x, y) &= \lim_{\rho \to 0^{+}} \frac{\rho^2 \cos \theta \sin \theta}{\rho}\\
        &= 0\\
        &= f(0, 0)
    \end{aligned}
    $$

    从而 $f(x, y)$ 在 $(0, 0)$ 处连续。

    $$
    \begin{aligned}
        \dfrac{\pd z}{\pd x}(0, 0) &= \lim\limits_{x \to 0} \dfrac{f(x, 0) - f(0, 0)}{x}\\
        &= \lim\limits_{x \to 0} \dfrac{0}{x}\\
        &= 0
    \end{aligned}
    $$

    $$
    \begin{aligned}
        \dfrac{\pd z}{\pd y}(0, 0) &= \lim\limits_{y \to 0} \dfrac{f(0, y) - f(0, 0)}{y}\\
        &= \lim\limits_{y \to 0} \dfrac{0}{y}\\
        &= 0
    \end{aligned}
    $$

    从而 $f(x, y)$ 在 $(0, 0)$ 处可偏导。

    则全增量（由 $\Delta z = \dfrac{\pd z}{\pd x}\Delta x + \dfrac{\pd z}{\pd y}\Delta y + o(\rho)$，其中 $\rho = \sqrt{(\Delta x)^2 + (\Delta y)^2}$。此处 $\Delta x = x - 0 = x,\, \Delta y = y - 0 = y$）有

    $$
    \begin{aligned}
        \Delta z &= f(x, y) - f(0, 0)\\
        &= x\dfrac{\pd z}{\pd x}(0, 0) + y\dfrac{\pd z}{\pd y}(0, 0) + \omega\\
        &= \omega
    \end{aligned}
    $$

    从而

    $$
    \omega = f(x, y) = \dfrac{xy}{\sqrt{x^2 + y^2}}
    $$

    若 $f(x, y)$ 在 $(0, 0)$ 处可微，则 $\omega$ 应该为 $\rho = \sqrt{x^2 + y^2}$ 的高阶无穷小，但

    $$
    \begin{aligned}
        \dfrac{\omega}{\rho} &= \dfrac{\rho \cos \theta \sin \theta}{ \rho^2}\\
        &= \cos \theta \sin \theta \nrightarrow 0
    \end{aligned}
    $$

    从而 $f(x, y)$ 在 $(0, 0)$ 处不可微。

!!! note ""
    设函数 $z = f(x, y)$ 在点 $(x, y)$ 的某邻域内可偏导，且 $\dfrac{\pd z}{\pd x}$、$\dfrac{\pd z}{\pd y}$ 在点 $(x, y)$ 连续，则 $f(x, y)$ 在点 $(x, y)$ **可微**。（函数可微的<u>充分条件</u>）

    ---

    证明：

    考虑 $z = f(x, y)$ 在点 $(x, y)$ 处的全增量

    $$
    \begin{aligned}
        \Delta z &= f(x + \Delta x, y + \Delta y) - f(x, y)\\
        &= \Bigr(f(x + \Delta x, y + \Delta y) - f(x, y + \Delta y)\Bigr) + \Bigr(f(x, y + \Delta y) - f(x, y)\Bigr)\\
    \end{aligned}
    $$

    $\left\lvert \Delta x \right\rvert,\,  \left\lvert \Delta y \right\rvert$ 充分小时，由一元函数拉格朗日中值定理，存在 $\theta_1,\, \theta_2 \in (0, 1)$，使得

    $$
    \begin{aligned}
        \Delta z = & \Delta x\dfrac{\pd z}{\pd x}(x + \theta_1 \Delta x, y +\Delta y) + \Delta y\dfrac{\pd z}{\pd y}(x, y + \theta_2 \Delta y)\\
    \end{aligned}
    $$

    由于 $\dfrac{\pd z}{\pd x}$、$\dfrac{\pd z}{\pd y}$ 在点 $(x, y)$ 连续，从而

    $$
    \begin{aligned}
        \lim_{\substack{\Delta x \to 0\\ \Delta y \to 0}} \dfrac{\pd z}{\pd x}(x + \theta_1 \Delta x, y +\Delta y) &= \dfrac{\pd z}{\pd x}(x, y)\\
        \lim_{\substack{\Delta x \to 0\\ \Delta y \to 0}} \dfrac{\pd z}{\pd y}(x, y + \theta_2 \Delta y) &= \dfrac{\pd z}{\pd y}(x, y)\\
    \end{aligned}
    $$

    所以

    $$
    \begin{aligned}
        \dfrac{\pd z}{\pd x}(x + \theta_1 \Delta x, y +\Delta y) &= \dfrac{\pd z}{\pd x}(x, y) + \alpha\\
        \dfrac{\pd z}{\pd y}(x, y + \theta_2 \Delta y) &= \dfrac{\pd z}{\pd y}(x, y) + \beta\\
    \end{aligned}
    $$

    其中 $\alpha,\, \beta \to 0\, (\Delta x \to 0,\, \Delta y \to 0)$。

    从而

    $$
    \Delta z = \Delta x\dfrac{\pd z}{\pd x}(x, y) + \Delta y\dfrac{\pd z}{\pd y}(x, y) + \alpha \Delta x + \beta \Delta y
    $$

    $\rho = \sqrt{(\Delta x)^2 + (\Delta y)^2}$，则

    $$
    \begin{aligned}
        0 &\le  \dfrac{\left\lvert \alpha \Delta x + \beta \Delta y \right\rvert}{\rho}\\
        &\le \left\lvert \alpha \right\rvert \dfrac{\left\lvert \Delta x \right\rvert}{\rho} + \left\lvert \beta \right\rvert \dfrac{\left\lvert \Delta y \right\rvert}{\rho}\\
        &\le \left\lvert \alpha \right\rvert + \left\lvert \beta \right\rvert\\
        &\to 0\quad (\Delta x \to 0,\, \Delta y \to 0)
    \end{aligned}
    $$

    夹逼准则知

    $$
    \alpha \Delta x + \beta \Delta y = o(\rho)\quad (\rho \to 0^{+})
    $$

    即

    $$
    \Delta z = \Delta x\dfrac{\pd z}{\pd x}(x, y) + \Delta y\dfrac{\pd z}{\pd y}(x, y) + o(\rho)
    $$

    从而 $f(x, y)$ 在点 $(x, y)$ 可微。

!!! info ""
    若函数 $z = f(x, y)$ 在 $(x, y)$ 的某邻域内可偏导，且 $\dfrac{\pd z}{\pd x}$、$\dfrac{\pd z}{\pd y}$ 在点 $(x, y)$ 连续，则**函数 $z = f(x, y)$ 在点 $(x, y)$ 连续可微**。

    若 $z = f(x, y)$ 在开区域 $G$ 内每一点都连续可微，则称**函数 $z = f(x, y)$ 在 $G$ 上连续可微**。

!!! note ""
    类似可导<u>推不出导函数连续</u>，可微并不代表导函数连续，因此连续可微的概念就与一元函数可导且导函数连续（即「连续可导」）类似。上面的证明和这里的「连续可微」定义一致，因为其实就是「连续可微」。

对于函数

$$
z = f(x, y) = \begin{cases}
    (x^2 + y^2) \sin \dfrac{1}{x^2 + y^2}, & \text{if } (x, y) \neq (0, 0), \\
    0, & \text{if } (x, y) = (0, 0)
\end{cases}
$$

$$
\begin{aligned}
    \dfrac{\pd z}{\pd x}(0, 0) &= \lim\limits_{\Delta x \to 0} \dfrac{f(\Delta x, 0) - f(0, 0)}{\Delta x} \\
    &= \lim\limits_{\Delta x \to 0} \Delta x \sin \dfrac{1}{\Delta x^2}\\
    &= 0
\end{aligned}
$$

同理可得 $\dfrac{\pd z}{\pd y}(0, 0) = 0$

而

$$
\begin{aligned}
    \omega &= \Delta z - \dfrac{\pd z}{\pd x} \Delta x - \dfrac{\pd z}{\pd y} \Delta y \\
    &= \Delta z \\
    &= f(\Delta x, \Delta y) - f(0, 0) \\
    &= (\Delta x^2 + \Delta y^2) \sin \dfrac{1}{\Delta x^2 + \Delta y^2}
\end{aligned}
$$

又

$$
\begin{aligned}
    \lim\limits_{\substack{\Delta x \to 0\\ \Delta y \to 0}} \dfrac{\omega}{\rho} &= \lim\limits_{\substack{\Delta x \to 0\\ \Delta y \to 0}} \sqrt{\Delta x^2 + \Delta y^2} \sin \dfrac{1}{\Delta x^2 + \Delta y^2} \\
    &= 0
\end{aligned}
$$

即 $\omega$ 是 $\rho$ 的高阶无穷小，$\Delta z$ 可以表示成 $A \Delta x + B \Delta y + o(\rho)$ 的形式，因此 $f(x)$ 在 $(0, 0)$ 处可微。

但 $f(x)$ 对 $x$ 的偏导数

$$
\begin{aligned}
    \dfrac{\pd z}{\pd x} &= 2 x \left(\sin \frac{1}{x^{2}+y^{2}}-\frac{1}{x^{2}+y^{2}} \cos \frac{1}{x^{2}+y^{2}}\right)
\end{aligned}
$$

在 $(0, 0)$ 的邻域内无界，从而 $\dfrac{\pd z}{\pd x}$ 在 $(0, 0)$ 处不连续。

由此说明了可微无法推出导函数连续。

二元函数的结论，也可以推广到多元函数，如函数 $z = f(x_1, x_2, \cdots, x_n)$ 的全微分

$$
\d z = \sum_{i=1}^{n} \dfrac{\pd z}{\pd x_i}\d x_i
$$

不再赘述。

目前看来，多元函数有四个性质：可偏导、连续、可微、连续可微。它们大致有下面的关系：

- 可偏导不一定连续，连续也不一定可偏导
- 可微一定可偏导，可微一定连续
- 可偏导、连续不一定可微
- 可微不一定连续可微，连续可微一定可微

!!! info ""
    设函数 $z = f(x, y)$ 在点 $(x, y)$ 处的所有 $n$ 阶偏导数都存在且连续，则函数 $z = f(x, y)$ 在点 $(x, y)$ 处 $n$ 阶可微（即函数 $f(x, y)$ $n$ 阶连续可微），且有

    $$
    \d^n z = \left( \d x \dfrac{\pd }{\pd x} + \d y \dfrac{\pd }{\pd y} \right)^n f(x, y)
    $$

    或者展开有

    $$
    \d^n z = \sum_{k=0}^n \dbinom{n}{k}  \dfrac{\pd^n f}{\pd x^k \pd y^{n - k}} (x, y) \d x^k  \d y^{n - k}
    $$
