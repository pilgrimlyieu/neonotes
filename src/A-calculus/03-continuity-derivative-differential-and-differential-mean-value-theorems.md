---
layout: post
title: 连续性、导数、微分与微分中值定理
date: 2023-11-16 09:46:22
updated: 2024-04-30 17:51:02
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 函数与连续性

### 函数的间断性

!!! info 间断点
    若以下条件至少有一个不成立，则称 $x_0$ 为函数 $f(x)$ 的间断点：
    1. $f(x)$ 在 $x_0$ 处有定义。
    2. $\lim\limits_{x \to x_0} f(x)$ 存在。
    3. $\lim\limits_{x \to x_0} f(x) = f(x_0)$。

1. 若 $f_{-}(x_0)$ 与 $f_{+}(x_0)$ 均存在，则称此类间断点为**第一类间断点**。
    1. 若 $f_{-}(x_0) \neq f_{+}(x_0)$，则称此类间断点为**跳跃间断点**。
    2. 若 $f_{-}(x_0) = f_{+}(x_0)$，则称此类间断点为**可去间断点**
2. 若 $f_{-}(x_0)$ 与 $f_{+}(x_0)$ 有一个不存在，则称此类间断点为**第二类间断点**。
    1. 若 $f_{-}(x_0)$ 与 $f_{+}(x_0)$ 均不存在，则称此类间断点为**无穷间断点**。
    2. 若 $f(x)$ 在 $x\to x_0$ 时不断变化，则称此类间断点为**振荡间断点**。

### 闭区间连续函数性质

!!! info 零点定理
    若 $f(x)$ 在 $[a,b]$ 上连续，且 $f(a) \cdot f(b) < 0$，则存在 $\xi \in (a,b)$，使得 $f(\xi) = 0$。

由此可得**介值定理**：

!!! info 介值定理
    若 $f(x)$ 在 $[a,b]$ 上连续，且 $f(a) \ne  f(b)$，则对于任意 $\eta \in \left(f(a),f(b)\right)$ 或 $\eta \in \left( f(b), f(a) \right) $ ，存在 $\xi \in (a,b)$，使得 $f(\xi) = \eta$。

!!! info 有界性定理
    若 $f(x)$ 在 $[a,b]$ 上连续，则 $f(x)$ 在 $[a,b]$ 上有界。

!!! info 最值定理
    若 $f(x)$ 在 $[a,b]$ 上连续，则 $f(x)$ 在 $[a,b]$ 上必有最大值和最小值。

## 导数

### 定义

!!! info ""
    若

    $$
    \lim\limits_{\Delta x \to 0} \frac{\Delta y}{\Delta x} = \lim\limits_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}
    $$

    存在，则称 $f(x)$ 在 $x_0$ 处可导，记为 $f'(x_0)$，称 $f'(x_0)$ 为 $f(x)$ 在 $x_0$ 处的导数。

    该极限也可写为

    $$
    \lim\limits_{x \to x_0} \frac{f(x) - f(x_0)}{x - x_0}
    $$

!!! note 导数的几种记号
    具体值：
    1. $f'(x_0)$
    2. $\dfrac{\d f(x)}{\d x}\as_{x=x_0}$
    3. $\dfrac{\d y}{\d x}\as_{x=x_0}$

    导函数：
    1. $f'(x)$
    2. $y'$
    3. $\dfrac{\d f(x)}{\d x}$
    4. $\dfrac{\d y}{\d x}$


### 增量公式

若 $f(x)$ 在 $x_0$ 处可导，则

$$
f(x_0 + \Delta x) - f(x_0) = f'(x_0) \Delta x + o(\Delta x)
$$

### 可导与连续的关系

!!! note ""
    **可导**<u>一定</u>**连续**，但**连续**<u>不一定</u>**可导**。

!!! memo ""
    想起一个图，一排共享单车倒下的样子，即「可『倒』一定连续，但连续不一定可『倒』」。

### 反函数求导

谨记

$$
\dfrac{\d x}{\d y} = \dfrac{1}{\dfrac{\d y}{\d x}}
$$

即可。

需要特别注意是，还可写成

$$
(f^{-1})'(x) = \dfrac{1}{f'(y)} = \dfrac{1}{f'(f^{-1}(x))}
$$

要注意第二个式子里的 $y$。

### 链式法则

谨记

$$
\dfrac{\d y}{\d x} = \dfrac{\d y}{\d u} \cdot \dfrac{\d u}{\d x}
$$

即可。非常简单。

利用 Chain Rule，有时候可以利用「对数求导法」简化分式求导。

例如 $y = \sqrt{\dfrac{(x-1)(x-2)}{(x-3)(x-4)}}$，则有

$$
\begin{aligned}
    \ln y &= \dfrac{1}{2} \ln \dfrac{(x-1)(x-2)}{(x-3)(x-4)}\\
    &= \dfrac{1}{2} \left( \ln (x-1) + \ln (x-2) - \ln (x-3) - \ln (x-4) \right)\\
\end{aligned}
$$

从而

$$
\d \ln y = \dfrac{1}{2} \left( \dfrac{1}{x-1} + \dfrac{1}{x-2} - \dfrac{1}{x-3} - \dfrac{1}{x-4} \right) \d x
$$

而 $\d \ln y = \dfrac{\d y}{y}$，即有

$$
\begin{aligned}
    y' &= \dfrac{\d y}{\d x} = \dfrac{y}{2} \left( \dfrac{1}{x-1} + \dfrac{1}{x-2} - \dfrac{1}{x-3} - \dfrac{1}{x-4} \right)\\
    &= \dfrac{1}{2} \sqrt{\dfrac{(x-1)(x-2)}{(x-3)(x-4)}} \left( \dfrac{1}{x-1} + \dfrac{1}{x-2} - \dfrac{1}{x-3} - \dfrac{1}{x-4} \right)
\end{aligned}
$$

### 常见函数的导数

| 函数 | 导数 | 注意 |
| :--: | :--: | :--: |
| $C$ | $0$ | - |
| $x^n$ | $nx^{n-1}$ | - |
| $a^x$ | $a^x \ln a$ | $a > 0$ 且 $a \neq 1$ |
| $\log_a x$ | $\dfrac{1}{x \ln a}$ | $a > 0$ 且 $a \neq 1$ |
| $\sin x$ | $\cos x$ | - |
| $\cos x$ | $-\sin x$ | - |
| $\tan x$ | $\sec^2 x$ | - |
| $\cot x$ | $-\csc^2 x$ | 不熟 |
| $\sec x$ | $\sec x \tan x$ | 不熟 |
| $\csc x$ | $-\csc x \cot x$ | 不熟 |
| $\arcsin x$ | $\dfrac{1}{\sqrt{1-x^2}}$ | - |
| $\arccos x$ | $-\dfrac{1}{\sqrt{1-x^2}}$ | - |
| $\arctan x$ | $\dfrac{1}{1+x^2}$ | - |
| $\arccot x$ | $-\dfrac{1}{1+x^2}$ | - |
| $\sinh x$ | $\cosh x$ | - |
| $\cosh x$ | $\sinh x$ | 不熟 |
| $\tanh x$ | $\dfrac{1}{\cosh^2 x}$ | - |
| $\coth x$ | $-\dfrac{1}{\sinh^2 x}$ | 不熟 |
| $\arsinh x$ | $\dfrac{1}{\sqrt{1+x^2}}$ | 不熟 |
| $\arcosh x$ | $\dfrac{1}{\sqrt{x^2-1}}$ | 不熟 |
| $\artanh x$ | $\dfrac{1}{1-x^2}$ | 不熟 |
| $\arcoth x$ | $\dfrac{1}{1-x^2}$ | 不熟 |

补充一下双曲三角函数的定义：

$$
\left\lbrace\begin{aligned}
    \sinh x &= \dfrac{\e^x - \e^{-x}}{2}\\
    \cosh x &= \dfrac{\e^x + \e^{-x}}{2}\\
\end{aligned}\right.
$$

### 高阶导数

$n$ 阶导数记为 $f^{(n)}(x)$ 或 $\dfrac{\d^n y}{\d x^n}$。

其中 $\d x^n$ 意思是 $(\d x)^n$，而非 $\d (x^n)$，只是为了~~偷懒~~方便，不用写括号。

而 $\d^n y = \overbrace{\d \cdots \d}^{n} y$。

根据高阶导数的定义（虽然我没写出来），有

$$
\begin{aligned}
    y^{(n)} &= \dfrac{\d y^{(n-1)}}{\d x}\\
\end{aligned}
$$

解这个递推即有 $y^{(n)} = \dfrac{\d^n y}{\d x^n}$。

### 莱布尼茨公式

类似二项式定理，有

$$
\begin{aligned}
    (uv)^{(n)} &= \sum_{k=0}^n \binom{n}{k} u^{(k)} v^{(n-k)}\\
\end{aligned}
$$

## 微分

### 定义

$$
\d f(x) = f'(x) \d x
$$

为了使这个定义易于理解，我抄一下书：

若可以将 $f(x)$ 增量 $\Delta y$ 表示为 $A(x)\Delta x + o(\Delta x)$，我们就可以有 $\Delta y$ 与 $\Delta x$ 的关系，去掉高阶无穷小，即有增量的商，在自变量 $x$ 增量趋于 $0$ 时，则可以将上的极限视为函数 $f(x)$ 在 $x$ 的导数。

由此我们记 $\d y = A(x) \Delta x$，视为 $y$ 的微分，也可以记为 $\d f(x)$。

现在有几种表示极小的符号：

1. $\Delta$：增量。
2. $\d$：微分，增量的极限。
3. $\delta$：物理那边用的比较多，有机会的话在那边写。数学这边我只记得一个极限的定义，表示一个小正数。
4. $\varepsilon$：似乎只在极限定义见过。表示任意小的正数。

根据导数的定义，有

$$
\begin{aligned}
    y' &= \lim\limits_{\Delta x \to 0} \frac{\Delta y}{\Delta x}\\
    &= \lim\limits_{\Delta x \to 0} \frac{A(x) \Delta x + o(\Delta x)}{\Delta x}\\
    &= \lim\limits_{\Delta x \to 0} A(x) + \lim\limits_{\Delta x \to 0} \frac{o(\Delta x)}{\Delta x}\\
    &= A(x)
\end{aligned}
$$

从而有

$$
\d y = y' \d x
$$

也即

$$
\boxed{\dfrac{\d y}{\d x} = y'}
$$

这也是导数别称**微商**的原因。

略去高阶无穷小，有

$$
f(x + \Delta x) \approx f(x) + f'(x) \Delta x
$$

### 莱布尼茨公式

同样有莱布尼茨公式

$$
\d^n (uv) = \sum_{k=0}^n \binom{n}{k} \d^k u \d^{n-k} v
$$

## 微分中值定理

### Fermat 引理（费马引理）

!!! info Fermat 引理
    若 $f(x)$ 在 $x_0$ 某个邻域 $U = N_{\delta}(x_0)$ 有定义，且在 $x_0$ 可导，并有 $f(x)$ 在 $x_0$ 处取得极值，则 $f'(x_0) = 0$。

证明：

根据导数的定义有 $f'_{-}(x_0)$ 与 $f'_{+}(x_0)$ 均存在，且 $f'_{-}(x_0) = f'_{+}(x_0)$。然而由极值的条件知两极限异号，从而 $f'(x_0) = 0$。

### Rolle 定理（洛尔定理/罗尔定理）

!!! info Rolle 定理
    若 $f(x)$ 满足：
    1. 在 $[a,b]$ 上连续
    2. 在 $(a,b)$ 内可导
    3. $f(a) = f(b)$

    则存在 $\xi \in (a,b)$，使得 $f'(\xi) = 0$。

### Lagrange 中值定理（拉格朗日中值定理）

!!! info Lagrange 中值定理
    若 $f(x)$ 满足：
    1. 在 $[a,b]$ 上连续
    2. 在 $(a,b)$ 内可导

    则存在 $\xi \in (a,b)$，使得 $f'(\xi) = \dfrac{f(b) - f(a)}{b - a}$。

证明：

作辅助函数 $\varphi(x) = f(x) - \dfrac{f(b) - f(a)}{b - a} (x - a)$。

则 $\varphi(x)$ 满足 Rolle 定理，也即存在 $\xi \in (a,b)$，使得 $\varphi'(\xi) = 0$，从而有 $f'(\xi) = \dfrac{f(b) - f(a)}{b - a}$。

若记 $a = x_0,\, b = x_0 + \Delta x$，则有 $\xi = x_0 + \theta \Delta x$，其中 $\theta \in (0,1)$。

从而可以将 Lagrange 中值定理写为**有限增量形式**：

$$
f(x_0 + \Delta x) = f(x_0) + f'(x_0 + \theta \Delta x) \Delta x
$$

### Cauchy 中值定理（柯西中值定理）

!!! info Cauchy 中值定理
    若 $f(x)$ 与 $g(x)$ 满足：
    1. 在 $[a,b]$ 上连续
    2. 在 $(a,b)$ 内可导
    3. $g'(x) \neq 0$ 在 $(a,b)$ 内恒成立

    则存在 $\xi \in (a,b)$，使得 $\dfrac{f'(\xi)}{g'(\xi)} = \dfrac{f(b) - f(a)}{g(b) - g(a)}$。

证明：

对 $g(x)$ 运用 Lagrange 中值定理有 $g(b) - g(a) = g'(\eta)(b - a)\ne 0$，其中 $\eta \in (a,b)$。

由此可作辅助函数 $\varphi(x) = f(x) - \dfrac{f(b) - f(a)}{g(b) - g(a)} (g(x) - g(a))$。

则 $\varphi(x)$ 满足 Rolle 定理，也即存在 $\xi \in (a,b)$，使得 $\varphi'(\xi) = 0$，从而有 $\dfrac{f'(\xi)}{g'(\xi)} = \dfrac{f(b) - f(a)}{g(b) - g(a)}$。

可以看出，Rolle 定理是 Lagrange 中值定理的特例，而 Lagrange 中值定理是 Cauchy 中值定理的特例。

### L'Hospital 法则（洛必达法则）

即所谓「萝卜头法则」，具体略~~懒得敲了~~。

### Taylor 公式（泰勒公式）

!!! info Taylor 公式
    若 $f(x)$ 在 $x_0$ 的某个邻域 $U = N_{\delta}(x_0)$ 内有 $n$ 阶导数，则 $x\to x_0$ 时有

    $$
    \begin{aligned}
        f(x) &= \sum_{k=0}^n \dfrac{f^{(k)}(x_0)}{k!} (x - x_0)^k + o((x - x_0)^n)\\
    \end{aligned}
    $$

称 $R_n(x) = o((x-x_0)^n)$ 为 Peano 余项（**皮亚诺余项**）。

多展开一项，为 $\dfrac{f^{(n + 1)}(x_0)}{(n + 1)!}(x - x_0)^{n+1}$，将其改写为 $\dfrac{f^{(n + 1)}(\xi)}{(n + 1)!}(x - x_0)^{n+1}$，记为 $R_n(x)$，其中 $\xi$ 介于 $x$ 与 $x_0$ 之间，称为 Lagrange 余项（**拉格朗日余项**）。

可以证明

!!! info 带 Lagrange 余项的 Taylor 公式
    若 $f(x)$ 在 $x_0$ 的某个邻域 $U = N_{\delta}(x_0)$ 内有 $n + 1$ 阶导数，则 $x\to x_0$ 时有

    $$
    \begin{aligned}
        f(x) &= \sum_{k=0}^n \dfrac{f^{(k)}(x_0)}{k!} (x - x_0)^k + R_n(x)
    \end{aligned}
    $$

    其中 $R_n(x) = \dfrac{f^{(n + 1)}(\xi)}{(n + 1)!}(x - x_0)^{n+1}$，$\xi$ 介于 $x$ 与 $x_0$ 之间。

    证明：

    $R_n(x_0) = 0$，柯西中值定理有

    $$
    \dfrac{R_n(x)}{(x-x_0)^{n+1}} = \dfrac{R_n(x) - R_n(x_0)}{(x - x_0)^{n+1} - 0} =\dfrac{1}{n+1} \dfrac{R_n'(\xi_1)}{(\xi_1 - x_0)^n}
    $$

    其中 $\xi_1$ 介于 $x$ 与 $x_0$ 之间。

    反复使用柯西中值定理，有

    $$
    \begin{aligned}
        \dfrac{R_n(x)}{(x-x_0)^{n+1}} &= \dfrac{1}{(n+1)!} \dfrac{R_n^{(n)}(\xi_n)}{(\xi_n - x_0)}\\
        &= \dfrac{1}{(n+1)!} \dfrac{R_n^{(n)}(\xi_n) - R_n^{(n)}(x_0)}{(\xi_n - x_0) - 0}\\
        &= \dfrac{1}{(n+1)!} \dfrac{R_n^{(n+1)}(\xi_{n+1})}{1}\\
        &= \dfrac{R_n^{(n+1)}(\xi_{n+1})}{(n+1)!}\\
    \end{aligned}
    $$

    且有 $R_n^{(n+1)}(\xi_{n+1}) = f^{(n+1)}(\xi_{n+1})$，

    而 $\xi_{n+1}$ 介于 $x$ 与 $x_0$ 之间，不妨记其为 $\xi$，从而有 $R_n(x) = \dfrac{f^{(n + 1)}(\xi)}{(n + 1)!}(x - x_0)^{n+1}$。

特别地，若 $x_0 = 0$，Taylor 公式可写作

!!! info Maclaurin 公式（麦克劳林公式）
    $$
    \begin{aligned}
        f(x) &= \sum_{k=0}^n \dfrac{f^{(k)}(0)}{k!} x^k + R_n(x)\\
        &= \sum_{k=0}^n \dfrac{f^{(k)}(0)}{k!} x^k + \dfrac{f^{(n + 1)}(\theta x)}{(n + 1)!} x^{n+1}\\
    \end{aligned}
    $$

    其中 $\theta \in (0,1)$。


下面给出常见函数的 Maclaurin 公式（顺便试一试 OCRC）：

$$
\begin{aligned}
    \e^x &= \sum_{k=0}^{n} \frac{x^{k}}{k !} + \frac{\e^{\theta x}}{(n + 1)!} x^{n+1}\\
    \sin x &= \sum_{k=0}^{n} \frac{(-1)^{k}}{(2 k+1) !} x^{2 k+1} + \frac{\sin \left(\theta x + \frac{2m + 3}{2}\pi\right)}{(2n + 3)!} x^{2n+3}\\
    \cos x &= \sum_{k=0}^{n} \frac{(-1)^{k}}{(2 k) !} x^{2 k} + \frac{\cos \left(\theta x + \left(m+1\right)\pi\right)}{(2n + 2)!} x^{2n+2}\\
    \ln (1+x) &= \sum_{k=1}^{n} \frac{(-1)^{k-1}}{k} x^{k} + \frac{(-1)^{n}}{(n + 1)(1 + \theta x)^{n+1}} x^{n+1}\\
    (1+x)^{\alpha} &= \sum_{k=0}^{n} \binom{\alpha}{k} x^{k} + \frac{\alpha(\alpha - 1) \cdots (\alpha - n)}{(n + 1)!} (1 + \theta x)^{\alpha - n - 1} x^{n+1}\\
\end{aligned}
$$


!!! memo ""
    好吧，只用了一次 OCRC，维基给的不是我想要的，最后还是 Copilot 弄的。

以上为通项，并不显著，下面展开几项：

$$
\begin{aligned}
    \e^x &= 1 + x + \frac{x^2}{2} + \frac{x^3}{6} + \cdots + R_n(x)\\
    \sin x &= x - \frac{x^3}{6} + \frac{x^5}{120} - \cdots + R_n(x)\\
    \cos x &= 1 - \frac{x^2}{2} + \frac{x^4}{24} - \cdots + R_n(x)\\
    \ln (1+x) &= x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots + R_n(x)\\
    (1+x)^{\alpha} &= 1 + \alpha x + \frac{\alpha(\alpha - 1)}{2} x^2 + \frac{\alpha(\alpha - 1)(\alpha - 2)}{6} x^3 + \cdots + R_n(x)\\
\end{aligned}
$$

附带上几个可能会用到的

$$
\begin{aligned}
    \dfrac{1}{1 - x} &= 1 + x + x^2 + \cdots + R_n(x)\\
    \tan x &= x + \dfrac{x^3}{3} + \dfrac{2x^5}{15} + \cdots + R_n(x)\\
    \arcsin x &= x + \dfrac{x^3}{6} + \dfrac{3x^5}{40} + \cdots + R_n(x)\\
    \arctan x &= x - \dfrac{x^3}{3} + \dfrac{x^5}{5} - \cdots + R_n(x)
\end{aligned}
$$

### 导数的应用

#### 极值点

**可疑极值点**：若 $f(x)$ 在 $x_0$ 处可导，且 $f'(x_0) = 0$ 或 $f'(x_0)$ 不存在，则称 $x_0$ 为 $f(x)$ 的可疑极值点。

极值点一定是可疑极值点，但可疑极值点不一定是极值点。

#### 凹凸性

若 $f(x)$ 在 $x_0$ 处二阶可导，则有

1. 若 $f''(x_0) > 0$，则 $f(x)$ 在 $x_0$ 处**上凹**（凹）
2. 若 $f''(x_0) < 0$，则 $f(x)$ 在 $x_0$ 处**下凹**（凸）

函数的形状与括号内汉字一致。

凹凸性的几何含义：

1. 若 $f''(x_0) > 0$，则 $f(x)$ 在 $x_0$ 处的图像位于其切线的上方
2. 若 $f''(x_0) < 0$，则 $f(x)$ 在 $x_0$ 处的图像位于其切线的下方

从而定义**拐点**：若 $f(x)$ 在 $x_0$ 处连续，若 $f(x)$ 在 $x_0$ 的左右邻域凹凸性相异，则称 $x_0$ 为 $f(x)$ 的**拐点**。

与极值点的判定类似，$f''(x_0) = 0$ 未必就是拐点。

若 $f''(x_0) = 0$ 或不存在，且 $f''(x)$ 在 $x_0$ 的左右邻域内异号，则 $x_0$ 为 $f(x)$ 的拐点。

#### 函数的渐近线

水平和铅直渐近线比较好判断，下面主要看斜渐近线。

!!! memo ""
    课本上用的是 $l\colon y = ax + b$ 作为直线方程。不过我为了依照 lf 所说的「初恋方程」，使用 $l\colon y = kx + b$ 作为直线方程。

显然有

$$
\lim\limits_{x \to +\infty} \left( f(x) - (kx + b) \right) = 0
$$

由此得 $\lim\limits_{x \to +\infty } \dfrac{f(x) - kx - b}{x} = 0$，

从而 $\lim\limits_{x \to +\infty } \dfrac{f(x)}{x} = k$。

那么有 $\lim\limits_{x \to +\infty } \left(f(x) - kx\right) = b$

也就是说，如果这两个极限存在，那么斜渐近线就随之确定了：

$$
\left\lbrace\begin{aligned}
    k &= \lim\limits_{x \to +\infty } \dfrac{f(x)}{x}\\
    b &= \lim\limits_{x \to +\infty } \left(f(x) - kx\right)
\end{aligned}\right.
$$
