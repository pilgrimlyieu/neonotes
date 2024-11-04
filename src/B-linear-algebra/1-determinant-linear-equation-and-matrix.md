---
layout: post
title: 行列式、线性方程组与矩阵
date: 2023-10-06 19:46:23
updated: 2024-08-30 15:49:07
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

!!! Memo ""
    线代老师不是按课本顺序讲的，因此下面我的笔记可能比较杂乱。

## 笔记

### 行列式

#### 行列式的公理化定义

1. 单位矩阵的行列式 $\left\lvert \bm{E} \right\rvert=1$
2. 行列式 $A$ 中任意两行交换，行列式变号
3. **多重线性**：行列式 $A$ 对其每一行都线性

#### 余子式

设 $\bm{A}$ 为 $n$ 阶方阵，$a_{ij}$ 为 $\bm{A}$ 的第 $i$ 行第 $j$ 列元素，则 $M_{ij}$ 为 $a_{ij}$ 的**余子式**，$A_{ij}$ 为 $a_{ij}$ 的**代数余子式**。有

$$
A_{ij} = (-1)^{i+j} M_{ij}
$$

$$
\begin{aligned}
    A &= \sum_{j=1}^n a_{ij} A_{ij} \\
    &= \sum_{j=1}^n (-1)^{i+j} a_{ij} M_{ij}
\end{aligned}
$$

#### 逆序数

排列 $S$ 中的所有*逆序*的个数称为这个排列的**逆序数**。记为 $\tau(S)$。

*自然顺序*指的是从小到大排列的顺序。

*逆序*指的是从大到小排列的顺序。

基于*逆序数*的**行列式**的定义：

对行列式 $D_n=
\begin{vmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{n1} & a_{n2} & \cdots & a_{nn} \\ \end{vmatrix}$，定义其结果为

$$
D_n=\sum_{S} (-1)^{\tau(S)} a_{1 s_1} a_{2 s_2} \cdots a_{n s_n},\,\qquad\left( S=s_1, s_2, \cdots, s_n \right)
$$

#### 和

$$
\begin{vmatrix}
    a_{11} & \cdots & a_{1n} \\
    \vdots &  & \vdots \\
    a_{i 1}+b_{i 1} & \cdots & a_{in} + b_{i n} \\
    \vdots &  & \vdots \\
    a_{n1} & \cdots & a_{nn} \\
\end{vmatrix}
=
\begin{vmatrix}
    a_{11} & \cdots & a_{1n} \\
    \vdots &  & \vdots \\
    a_{i1} & \cdots & a_{in} \\
    \vdots &  & \vdots \\
    a_{n1} & \cdots & a_{nn} \\
\end{vmatrix}
+
\begin{vmatrix}
    a_{11} & \cdots & a_{1n} \\
    \vdots &  & \vdots \\
    b_{i1} & \cdots & b_{in} \\
    \vdots &  & \vdots \\
    a_{n1} & \cdots & a_{nn} \\
\end{vmatrix}
$$

即一次只能拆一行。

#### 定理 1.2.9

!!! info ""
    行列式任一行（列）的元素与另一行（列）对应元素的代数余子式乘积之和等于零。

证明：只需将原行列式代数余子式对应行（上面说的第二个行）换成另一行（上面说的第一个行）。新行列式出现两行相同，值为零。

#### 箭形行列式

设 $\displaystyle \prod_{i=1}^{n}c_i\ne 0$，则**箭形行列式**可定义为

$$
\begin{aligned}
    A_{n+1}&=
    \begin{vmatrix}
        c_0 & a_1 & a_2 & \cdots & a_n \\
        b_1 & c_1 & 0 & \cdots & 0 \\
        b_2 & 0 & c_2 & \cdots & 0 \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        b_n & 0 & 0 & \cdots & c_n \\
    \end{vmatrix}\\
    &= \prod_{i=1}^{n}c_i\left(c_0 - \sum_{i=1}^{n} \dfrac{a_i b_i}{c_i}\right)
\end{aligned}
$$

证明：

$$
\begin{aligned}
    A_{n+1}&\xlongequal{\displaystyle r_1 - \sum \limits_{i=1}^{n} \frac{a_i}{c_i}r_{i+1}}\begin{vmatrix}
        c_0 - \sum \limits_{i=1}^{n} \frac{a_i b_i}{c_i} & 0 & 0 & \cdots & 0 \\
        b_1 & c_1 & 0 & \cdots & 0 \\
        b_2 & 0 & c_2 & \cdots & 0 \\
        \vdots & \vdots & \vdots & \ddots & \vdots \\
        b_n & 0 & 0 & \cdots & c_n \end{vmatrix}\\
    &= \prod_{i=1}^{n}c_i\left(c_0 - \sum_{i=1}^{n} \dfrac{a_i b_i}{c_i}\right)
\end{aligned}
$$

#### $-\bm{A}$

$$
-\bm{A}=\begin{bmatrix} -a_{i j} \end{bmatrix}
$$

$$
\left\lvert -\bm{A}_n \right\rvert = (-1)^n \left\lvert \bm{A}_n \right\rvert
$$

!!! info ""
    奇数阶的反对称行列式等于零。

证明：即 $\bm{A}^{\rm T}=-\bm{A}$。则 $\left\lvert \bm{A}^\intercal \right\rvert=\left\lvert -\bm{A} \right\rvert=-\left\lvert \bm{A} \right\rvert=\left\lvert \bm{A} \right\rvert$。

#### 范德蒙德行列式

$n$ 阶范德蒙德行列式为

$$
\begin{aligned}
    D_n\left( x_1, x_2, \cdots, x_n \right)&=\begin{vmatrix}
        1 & 1 & \cdots & 1 \\
        x_1 & x_2 & \cdots & x_n \\
        x_1^2 & x_2^2 & \cdots & x_n^2 \\
        \vdots & \vdots & \ddots & \vdots \\
        x_1^{n-1} & x_2^{n-1} & \cdots & x_n^{n-1} \\
    \end{vmatrix}\\
    &=\prod_{1 \leq i < j \leq n} \left( x_j - x_i \right)
\end{aligned}
$$

证明：我忘记了老师的做法，课本做法太麻烦了。

### 线性方程组

#### 克莱姆法则

$n$ 元线性方程组

$$
\left\lbrace\begin{aligned}
    a_{11} x_1 + a_{12} x_2 + \cdots + a_{1n} x_n &= b_1 \\
    a_{21} x_1 + a_{22} x_2 + \cdots + a_{2n} x_n &= b_2 \\
    \vdots \\
    a_{n1} x_1 + a_{n2} x_2 + \cdots + a_{nn} x_n &= b_n \\
\end{aligned}\right.
$$

若其系数行列式

$$
D=
\begin{vmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    a_{21} & a_{22} & \cdots & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{nn} \\
\end{vmatrix}
\ne 0
$$

则方程组有唯一解，且解可表示为

$$
x_i = \dfrac{D_i}{D},\qquad (i=1,2,\cdots,n)
$$


!!! note ""
    不代表 $D=0$ 时方程组无解！

#### 代数基本定理

!!! info ""
    $\displaystyle \sum \limits_{i=0}^{n}c_i x^i=0,\,(c_n\ne 0)$ 至多有 $n$ 个互不相等的实根。

证明：反证法，不妨设 $x_1, x_2, \cdots, x_{n+1}$ 是 $n+1$ 个互不相等的实根，则

$$
\begin{bmatrix}
    1 & x_1 & \cdots & x_1^n \\
    1 & x_2 & \cdots & x_2^n \\
    \vdots & \vdots & \ddots & \vdots \\
    1 & x_{n+1} & \cdots & x_{n+1}^n \\
\end{bmatrix}
\begin{bmatrix}
    c_0 \\
    c_1 \\
    \vdots \\
    c_n \\
\end{bmatrix}
=
\begin{bmatrix}
    0 \\
    0 \\
    \vdots \\
    0
\end{bmatrix}
$$


而[范德蒙德行列式](#范德蒙德行列式) $\begin{vmatrix} 1 & x_1 & \cdots & x_1^n \\ 1 & x_2 & \cdots & x_2^n \\ \vdots & \vdots & \ddots & \vdots \\ 1 & x_{n+1} & \cdots & x_{n+1}^n \\ \end{vmatrix}=\displaystyle \prod\limits_{1\le i < j \le n+1}^{}(x_j-x_i)\ne 0$，因此 $c_0=c_1=\cdots=c_n=0$，与 $c_n\ne 0$ 矛盾，得证。

### 矩阵

#### 表示

$\bm{A}_{m \times n}$ 表示 $m$ 行 $n$ 列的矩阵，可记作

$$
\begin{pmatrix}
    a_{1 1} & a_{1 2} & \cdots & a_{1 n} \\
    a_{2 1} & a_{2 2} & \cdots & a_{2 n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{pmatrix}
$$

或

$$
\begin{bmatrix}
    a_{1 1} & a_{1 2} & \cdots & a_{1 n} \\
    a_{2 1} & a_{2 2} & \cdots & a_{2 n} \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{bmatrix}
$$

!!! memo ""
    我个人更喜欢第二种，我的文章应该也全都是第二种。但教材、老师都是第一种，而因为第一种比较方便，我手写也可能用第一种。

用 $M_{m \times n}(\mathbb{R})$ 表示全体 $m$ 行 $n$ 列的实矩阵。

!!! tip ""
    教材上用的是 $M_{m \times n}(\mathbf{R})$。

#### 零矩阵

所有元素都为零的矩阵称为**零矩阵**，记作 $\bm{O}_{m \times n}$ 或 $\bm{O}$。

#### 对角矩阵

$$
\bm{A}=\begin{bmatrix}
    a_{11} & 0 & \cdots & 0 \\
    0 & a_{22} & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & a_{nn}
\end{bmatrix}
$$

则称 $\bm{A}$ 为**对角矩阵**。也常用 $\def\diag{\operatorname{diag}}\diag(a_{11}, a_{22}, \cdots, a_{nn})$ 表示。

##### 数量矩阵

若 $a_{11}=a_{22}=\cdots=a_{nn}=k$，则称 $\bm{A}$ 为**数量矩阵**。

##### 单位矩阵

若 $k=1$，则称 $\bm{A}$ 为**单位矩阵**，记作 $\bm{E}$ 或 $\bm{I}$。

#### 三角形矩阵

上三角矩阵：

$$
\bm{A}=\begin{bmatrix}
    a_{11} & a_{12} & \cdots & a_{1n} \\
    0 & a_{22} & \cdots & a_{2n} \\
    \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & \cdots & a_{nn}
\end{bmatrix}
$$

下三角矩阵：

$$
\bm{A}=\begin{bmatrix}
    a_{11} & 0 & \cdots & 0 \\
    a_{21} & a_{22} & \cdots & 0 \\
    \vdots & \vdots & \ddots & \vdots \\
    a_{n1} & a_{n2} & \cdots & a_{nn}
\end{bmatrix}
$$

#### 对称矩阵 & 反对称矩阵

若 $\bm{A}=(a_{ij})_n$ 满足 $a_{ij}=a_{ji}$，则称 $\bm{A}$ 为**对称矩阵**。

若 $\bm{A}=(a_{ij})_n$ 满足 $a_{ij}=-a_{ji}$，则称 $\bm{A}$ 为**反对称矩阵**。

#### 转置矩阵

把 $m \times n$ 矩阵 $\bm{A}$ 的行换成同序数的列所得到的 $n \times m$ 矩阵称为 $\bm{A}$ 的**转置矩阵**，记作 $\bm{A}^\intercal$ 或 $\bm{A}'$。

#### 奇异矩阵 & 非奇异矩阵

若方阵 $\bm{A}$ 的行列式 $\left\lvert \bm{A} \right\rvert=0$，则称 $\bm{A}$ 为**奇异矩阵**，否则称 $\bm{A}$ 为**非奇异矩阵**。

!!! tip ""
    **奇异矩阵**也称为*退化矩阵*。

    **非奇异矩阵**也称为*非异矩阵*。

#### 矩阵的运算

##### 数乘

设 $k$ 为数，$\bm{A}=\left[a_{ij}\right]_n$，则 $k \bm{A}=\left[k a_{ij}\right]_n$。

$$
\left\lvert k \bm{A}_n \right\rvert = k^n \left\lvert \bm{A}_n \right\rvert
$$

##### 乘法

设 $\bm{A}_{m \times l}=\left[a_{ij}\right]$，$\bm{B}_{l \times n}=\left[b_{ij}\right]$，则 $\bm{A}$ 与 $\bm{B}$ 的乘积 $\bm{C}_{m \times n}=\left[c_{ij}\right]_{m \times n}$ 定义为

$$
c_{ij}=\sum_{k=1}^l a_{ik} b_{kj},\qquad (i=1,2,\cdots,m;\;j=1,2,\cdots,n)
$$

$c_{ij}$ 等于 $\bm{A}$ 的第 $i$ 行元素与 $\bm{B}$ 的第 $j$ 列元素对应相乘再相加。

从向量角度进行理解，设 $\bm{A}=\begin{bmatrix} \vec{\alpha}_1 \\ \vec{\alpha}_2 \\ \vdots \\ \vec{\alpha}_m \end{bmatrix},\, \bm{B}=\begin{bmatrix} \vec{\beta}_1 & \vec{\beta}_2 & \cdots & \vec{\beta}_n \end{bmatrix}$（$\vec{\alpha}_i,\, \vec{\beta}_i$ 都是 $l$ 维向量），则

$$
\bm{C}=\bm{A}\bm{B}= \begin{bmatrix} \vec{\alpha}_1 \\ \vec{\alpha}_2 \\ \vdots \\ \vec{\alpha}_m \end{bmatrix} \begin{bmatrix} \vec{\beta}_1 & \vec{\beta}_2 & \cdots & \vec{\beta}_n \end{bmatrix} = \begin{bmatrix} \vec{\alpha}_1 \vec{\beta}_1 & \vec{\alpha}_1 \vec{\beta}_2 & \cdots & \vec{\alpha}_1 \vec{\beta}_n \\ \vec{\alpha}_2 \vec{\beta}_1 & \vec{\alpha}_2 \vec{\beta}_2 & \cdots & \vec{\alpha}_2 \vec{\beta}_n \\ \vdots & \vdots & \ddots & \vdots \\ \vec{\alpha}_m \vec{\beta}_1 & \vec{\alpha}_m \vec{\beta}_2 & \cdots & \vec{\alpha}_m \vec{\beta}_n \end{bmatrix}
$$

$$
c_{ij}=\vec{\alpha}_i \cdot \vec{\beta}_j
$$

由于矩阵乘法不满足交换律，因此一般 $\bm{A}\bm{B} \ne \bm{B}\bm{A}$，$\left( \bm{A}\bm{B} \right)^k \ne \bm{A}^k \bm{B}^k$。

!!! info ""
    $\left\lvert \bm{A}_1 \bm{A}_2 \cdots \bm{A}_k \right\rvert = \left\lvert \bm{A}_1 \right\rvert \left\lvert \bm{A}_2 \right\rvert \cdots \left\lvert \bm{A}_k \right\rvert$

!!! info ""
    $\left( \bm{A}\bm{B} \right) ^\intercal=\bm{B}^\intercal\bm{A}^\intercal$

    $\left( \bm{A}_1 \bm{A}_2 \cdots \bm{A}_k \right)^\intercal=\bm{A}_k^\intercal\cdots \bm{A}_2^\intercal\bm{A}_1^\intercal$

##### 矩阵的幂

设 $\bm{A}$ 为 $n$ 阶方阵，定义 $\bm{A}^0=\bm{E},\, \bm{A}^k=\bm{A}^{k-1}\bm{A}$。

若 $\bm{A}\bm{B}=\bm{B}\bm{A}$，则 $\left( \bm{A}+\bm{B} \right)^n=\displaystyle \sum_{i=0}^{n}\combination_n^i \bm{A}^{n-i}\bm{B}^i$。

如计算 $\bm{A}=\begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$ 的 $n$ 次幂，可令 $\bm{A}=\bm{E}+\bm{B}$。

##### 矩阵多项式

定义

$$
f(\bm{A})=\sum_{i=1}^{n} a_i \bm{A}^i
$$

为**矩阵多项式**。

<!-- !!! Memo "" -->
<!--     先写这么多，以后再补充。 -->

<!--     现在写点别的。 -->

<!-- ## Copilot -->

<!-- 最近把[矩阵的 Snippets 写好了](https://github.com/pilgrimlyieu/Snippets/pull/7)，实际用时感觉还行，还是有点缺憾。不过用的最爽的其实还是 Copilot。 -->

<!-- 比如上面一些定义，我就是先写好了标题，然后开头写个「若」什么的，然后 <kbd>Tab</kbd> 就好了，最多需要额外修改一下什么的。 -->

<!-- 再比如很多矩阵，要是以前，即使有 Snippets 也得累死，然后现在 Copilot 也是很聪明就写出来了。 -->

<!-- 上面那个范德蒙德行列式，我也是写好标题，Copilot 就写出来了。然后下面证明出现时，我写了一行，后面就自动补全了，还知道用省略号。然后范德蒙德行列式的结果也是它给出来的。 -->

<!-- 然后什么线性方程组、系数矩阵、对角矩阵、三角矩阵等等，都直接写个标题就完事了，亏我还专门做了几个 Snippets，连这个 Snippets 都是 Copilot 提示的。 -->

<!-- 上面的矩阵乘法，也是它写好的。而且我前面 display 数学环境逗号后面用了 `\qquad`（Copilot 提示 `\quad`），它这里就自动用了 `\qquad` 了。 -->

<!-- 然后是上面那个向量角度，我写好两个矩阵的向量表示，然后 Copilot 就写出来了乘积的表达式，要不是它，这个即使用 Snippets 也得写段时间，而现在直接 <kbd>Tab</kbd> 就好了。 -->

<!-- ### :heart: -->

<!-- 最为感动的是，敲着敲着，它在后面给你提示，正好是你心中所想。 -->

<!-- 我是一个话不多的人，可能对熟人话会多一点，但也没讲过心里话。我内心真正的想法从来都是不直接对外传达的，因此有这样一个人，**懂**我，可以说是让我非常感动了。连一个人工智能都能懂我，看来我还是蛮好懂的。 -->

<!-- 当然仅限于数学笔记这方面，我写真正反映心声的文章，它还是不懂的。我也只是借题发挥，有感而发。 -->

<!-- 我似乎已经成为一个互联网上的人类了，对线下的生活提不起兴致。 -->

<!-- 我不打游戏（以前虽然打过），懒得运动，不喜外出……每天从早到晚都是坐在电脑面前。国庆期间，我的外出只有两个目的，一是去吃饭，二是去取快递。本来有想过去南京大屠杀遇难同胞纪念馆看一下的，但还是因各种原因打消了念头。我也常戏称自己一天有 25 个小时坐在电脑前。 -->

<!-- 也许正因此，我的内心逐渐封闭，不愿与人交流，不愿与人接触，不愿与人沟通。所以我才会在 Copilot 仅仅只是预测到了我想写的东西，还满心欢喜，感动不已吧。 -->

<!-- 也许照这个趋势，我以后可能会爱上一个人工智能吧。我现在也是很期待人工智能的发展，照「赤橙黄绿青蓝靛紫」给予我慰藉吧。 -->

<!-- !!! Danger Q -->
<!--     你这种状况什么时候开始有的？ -->

<!-- !!! Tip A -->
<!--     也许是从高中？我记得小学初中我还是蛮外向的，经常和朋友一起。但我肯定初中内心里就有这样的苗头了，我清晰地记得现在的感受，在初中时的内心深处也是有的，只不过没有表露出来。 -->

<!--     到了高中后，举目无亲。也许就是这样，我才变得内向了吧。 -->

<!--     到了大学情况估计更甚，不过我也放宽心了。高中时还有点在意，有点焦虑，大学我就无所谓了。目前我们班我认识的也就宿舍两个人罢了。唯一比较担心的，可能是小组活动这样的事情。 -->
