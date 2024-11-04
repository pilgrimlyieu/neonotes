---
layout: post
title: 支持向量机
date: 2024-10-16 09:34:14
updated: 2024-10-23 10:37:01
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 间隔与支持向量

给定训练样本集 $\left\lbrace (\bm{x}_i, y_i) \right\rbrace_{i=1}^m$ ，其中 $\bm{x}_i \in \mathbb{R}^d$ ，$y_i \in \left\lbrace -1, 1 \right\rbrace$ ，分类学习最基本的想法就是基于训练集 $D$ 在样本空间中找到一个划分超平面，将不同类别的样本分开。

如图所示，能将训练样本分开的划分超平面可能有很多：

![](./06-support-vector-machine/different-hyperplanes.png)

直观来说，应当选择对训练样本局部扰动的「容忍」性最好的。换言之，划分超平面所产生的分类结果是最鲁棒的，对未见示例的泛化能力最强。

样本空间中划分超平面可以描述为
$$
\bm{w}^\intercal \bm{x} + b = 0
$$

其中 $\bm{w} = (w_1; w_2; \dots; w_d)$ 为法向量，决定了超平面的方向；$b$ 为位移项，决定了超平面与原点之间的距离。因此划分超平面可以由这两个参数确定，记为 $(\bm{w}, b)$。

样本空间中任一点 $\bm{x}$ 到超平面 $(\bm{w}, b)$ 的距离可写为
$$
r = \frac{\left| \bm{w}^\intercal \bm{x} + b \right|}{\left\| \bm{w} \right\|}
$$

若超平面 $(\bm{w}, b)$ 可以将训练样本正确分类，即对于 $(\bm{x}_i, y_i) \in D$，若 $y_i = +1$，则有 $\bm{w}^\intercal \bm{x}_i + b > 0$；若 $y_i = -1$，则有 $\bm{w}^\intercal \bm{x}_i + b < 0$。令
$$
\begin{cases}
\bm{w}^\intercal \bm{x}_i + b \ge +1, & y_i = +1 \\ 
\bm{w}^\intercal \bm{x}_i + b \le -1, & y_i = -1
\end{cases}
$$

换种写法就是
$$
\begin{equation}
    y_i(\bm{w}^\intercal \bm{x}_i + b) \ge 1, \quad i = 1, 2, \dots, m \label{1}
\end{equation}
$$

如下图所示，距离超平面最近的这几个训练样本点可使上式等号成立，它们被称为**支持向量**（support vector）：

![](./06-support-vector-machine/support-vector-and-margin.png)

两个异类支持向量到超平面的距离之和为
$$
\gamma = \frac{2}{\left\| \bm{w} \right\|}
$$

这被称为**间隔**（margin）。

也就是说，目标是找到具有「最大间隔」（maximum margin）的划分超平面，即找到满足 $\eqref{1}$ 约束的参数 $\bm{w}, b$ 使得 $\gamma$ 最大：
$$
\max_{\bm{w}, b} \frac{2}{\left\| \bm{w} \right\|} \quad \text{s.t.} \quad y_i(\bm{w}^\intercal \bm{x}_i + b) \ge 1, \quad i = 1, 2, \dots, m
$$

显然最大化间隔，只需要最小化 $\left\| \bm{w} \right\|^2$ 即可，因此上述优化问题等价于
$$
\begin{equation}
    \min_{\bm{w}, b} \frac{1}{2} \left\| \bm{w} \right\|^2 \quad \text{s.t.} \quad y_i(\bm{w}^\intercal \bm{x}_i + b) \ge 1, \quad i = 1, 2, \dots, m \label{2}
\end{equation}
$$

这就是**支持向量机**（Support Vector Machine, SVM）的基本型。

## 对偶问题

!!! memo ""
    数学知识待额外补充

### 拉格朗日乘子法

!!! info 拉格朗日乘子法
    最小化 $f(\bm{x})$，其中 $f(\bm{x})$ 为凸函数，约束条件为
    $$
    \begin{cases}
        h_i(\bm{x}) \le 0, & i = 1, 2, \dots, m\\
        g_{j}(\bm{x}) = 0, & j = 1, 2, \dots, n
    \end{cases}
    $$
    
    拉格朗日函数为
    $$
    \mathcal{L}(\bm{x}, \bm{\lambda}, \bm{\mu}) = f(\bm{x}) + \sum_{i=1}^m \lambda_i h_i(\bm{x}) + \sum_{j=1}^n \mu_j g_j(\bm{x})
    $$
    
    对偶问题为
    $$
    \max_{\bm{\lambda}, \bm{\mu}} \inf_{\bm{x}} \mathcal{L}(\bm{x}, \bm{\lambda}, \bm{\mu})\quad \text{s.t.} \quad \lambda_i \ge 0, \quad i = 1, 2, \dots, m
    $$
    
    Karush-Kuhn-Tucker(KKT) 条件为
    1. 稳定性：$\mathcal{L}(\bm{x}, \bm{\lambda}, \bm{\mu})$ 极值点梯度为零
    2. 原问题约束：$h_i(\bm{x}) \le 0,\, g_j(\bm{x}) = 0$
    3. 对偶问题约束：$\lambda_i \ge 0$
    4. 互补松弛：$\lambda_i h_i(\bm{x}) = 0$

    若满足 KKT 条件，则原问题与对偶问题的解相等。

首先引入拉格朗日乘子得到拉格朗日函数
$$
\mathcal{L}(\bm{w}, b, \bm{\alpha}) = \frac{1}{2} \left\| \bm{w} \right\|^2 + \sum_{i=1}^m \alpha_i \left(1 - y_i(\bm{w}^\intercal \bm{x}_i + b) \right)
$$

对 $\bm{w}, b$ 偏导为零得
$$
\left\lbrace\begin{aligned}
    \bm{w} &= \sum_{i=1}^m \alpha_i y_i \bm{x}_i \\ 
    0 &= \sum_{i=1}^m \alpha_i y_i
\end{aligned}\right.
$$

代回拉格朗日函数得到对偶问题
$$
\begin{equation}
    \begin{aligned}
        &\max_{\bm{\alpha}} \sum_{i=1}^m \alpha_i - \frac{1}{2} \sum_{i=1}^m \sum_{j=1}^m \alpha_i \alpha_j y_i y_j \bm{x}_i^\intercal \bm{x}_j \\
        &\text{s.t.} \quad \sum_{i=1}^{m}\alpha_i y_i = 0,\,  \alpha_i \ge 0, \quad i = 1, 2, \dots, m
    \end{aligned} \label{3}
\end{equation}
$$

<!-- {{{ 过程 -->
<details>
<summary>过程</summary>

$$
\begin{aligned}
    \mathcal{L}(\bm{w}, b, \bm{\alpha}) &= \dfrac{1}{2}\bm{w}^\intercal \bm{w} - \sum_{i=1}^{m}\alpha_i y_i\bm{w}^\intercal \bm{x}_i + \sum_{i=1}^{m}\alpha_i - b\sum_{i=1}^{m}\alpha_i y_i \\ 
    &= \dfrac{1}{2}\bm{w}^\intercal \bm{w} - \bm{w}^\intercal \sum_{i=1}^{m}\alpha_i y_i \bm{x}_i + \sum_{i=1}^{m}\alpha_i - 0\\
    &= \dfrac{1}{2}\bm{w}^\intercal \bm{w} - \bm{w}^\intercal \bm{w} + \sum_{i=1}^{m}\alpha_i\\ 
    &= \sum_{i=1}^{m}\alpha_i - \dfrac{1}{2}\bm{w}^\intercal \bm{w}\\ 
    &= \sum_{i=1}^{m}\alpha_i - \dfrac{1}{2}\left(\sum_{i=1}^{m}\alpha_i y_i \bm{x}_i\right)^\intercal \left(\sum_{i=1}^{m}\alpha_i y_i \bm{x}_i\right)\\ 
    &= \sum_{i=1}^{m}\alpha_i - \dfrac{1}{2}\sum_{i=1}^{m}\sum_{j=1}^{m}\alpha_i\alpha_j y_i y_j \bm{x}_i^\intercal \bm{x}_j
\end{aligned}
$$

</details>
<!-- }}} -->

最终模型为
$$
\begin{equation}
    \begin{aligned}
        f(\bm{x}) &= \bm{w}^\intercal \bm{x} + b \\ 
        &= \sum_{i=1}^m \alpha_i y_i \bm{x}_i^\intercal \bm{x} + b \\ 
    \end{aligned} \label{4}
\end{equation}
$$

KKT 条件为
$$
\left\lbrace\begin{aligned}
    &\alpha_i \ge 0 \\ 
    &y_i f(\bm{x}_i) - 1 \ge 0 \\ 
    &\alpha_i (y_i f(\bm{x}_i) - 1) = 0
\end{aligned}\right.
$$

可以看出一定有 $\alpha_i = 0$ 或 $y_i f(\bm{x}_i) = 1$。

- 若 $\alpha_i = 0$，则该样本压根不会出现在模型当中，不会对 $f(\bm{x})$ 有任何影响。
- 若 $\alpha_i > 0$，则一定有 $y_i f(\bm{x}_i) = 1$，即对应的样本点位于最大间隔边界上，是一个支持向量。

因此得到了支持向量机一个重要性质——解的*稀疏性*：训练完成后，大部分的训练样本都不需要保留，最终模型仅与支持向量有关。

### SMO 算法

求解 $\eqref{3}$ 可以使用 SMO (Sequential Minimal Optimization) 算法。

基本思路：不断执行如下两个步骤直至收敛：
1. 选取一对需更新的变量 $a_i, a_{j}$
2. 固定 $a_i, a_{j}$ 以外的参数，求解对偶问题更新 $a_i, a_{j}$

仅考虑 $a_i, a_{j}$ 时，对偶问题的约束
$$
0 = \sum_{i=1}^{m}\alpha_i y_i
$$

变为
$$
\alpha_i y_i + \alpha_j y_j = c,\quad \alpha_i, \alpha_j \ge 0
$$

其中 $c = -\displaystyle \sum_{k \neq i, j} \alpha_k y_k$ 是使得约束条件成立的常数。

选取的 $a_i, a_{j}$ 有一个不满足 $\eqref{3}$ 时，目标函数就会在迭代后减小。直观来看，KKT 条件 $\eqref{3}$ 违背程度越大，变量更新后导致的目标函数值的减幅越大。因此 SMO 先选取违背 $\eqref{3}$ 程度最大的变量，第二个变量应选择一个使目标函数减小最快的变量。

不过这样比较各变量对应的目标函数减幅的复杂度过高，SMO 采用了一个启发式：使选取的两变量所对应样本之间的间隔最大。

一种直观的解释是，这样的两个变量有很大的差别，与对两个相似的变量进行更新相比，对它们进行更新会带给目标函数值更大的变化。

消去 $\eqref{3}$ 中的 $a_{j}$，则得到一个关于 $a_i$ 的单变量二次规划问题，仅有的约束是 $\alpha_i \ge 0$，这样的二次规划问题有闭式解。

对于偏移项 $b$，对任意支持向量 $(\bm{x}_s, y_s)$ 都有 $y_s f(\bm{x}_s) = 1$，即
$$
y_s \left( \sum_{i \in S} \alpha_i y_i \bm{x}_i^\intercal \bm{x}_s + b \right) = 1
$$

其中 $S = \left\lbrace i \mid a_i > 0, i = 1, 2, \dots, m \right\rbrace$ 为所有支持向量的下标集。

理论上可选取任意支持向量并通过上式获得 $b$，但现实任务中常采用一种更鲁棒的做法，即使用所有支持向量求解的平均值
$$
b = \frac{1}{\left| S \right|} \sum_{s \in S} \left( y_s - \sum_{i \in S} \alpha_i y_i \bm{x}_i^\intercal \bm{x}_s \right)
$$

## 核函数

前面的讨论中，假设了训练样本是线性可分的，即存在一个划分超平面能够将训练样本正确分类。但实际任务中，训练样本可能是线性不可分的。如下图的「异或问题」：

![](./06-support-vector-machine/xor-problem-and-nonlinear-map.png)

对这样的问题，可将样本从原始空间映射到一个更高维的特征空间，使得在这个特征空间中样本是线性可分的。

上图中，若将原始的二维空间映射到一个合适的三维空间，就能找到一个合适的划分超平面。

若原始空间是有限维，即属性数有限，那么一定存在一个高维特征空间使样本线性可分。

令 $\phi(\bm{x})$ 表示将 $\bm{x}$ 映射后的特征向量，于是特征空间中划分超平面所对应的模型可表示为
$$
f(\bm{x}) = \bm{w}^\intercal \phi(\bm{x}) + b
$$

其中 $\bm{w}, b$ 是模型参数。

类似地有对偶问题
$$
\begin{aligned}
    &\max_{\bm{\alpha}} \sum_{i=1}^m \alpha_i - \frac{1}{2} \sum_{i=1}^m \sum_{j=1}^m \alpha_i \alpha_j y_i y_j \phi(\bm{x}_i)^\intercal \phi(\bm{x}_j) \\
    &\text{s.t.} \quad \sum_{i=1}^{m}\alpha_i y_i = 0,\,  \alpha_i \ge 0, \quad i = 1, 2, \dots, m
\end{aligned}
$$

求解上式涉及到计算 $\phi(\bm{x}_i)^\intercal \phi(\bm{x}_{j})$，是样本 $\bm{x}_i, \bm{x}_{j}$ 映射到特征空间之后的内积。由于特征空间的维数可能很高，甚至是无穷维，因此直接计算是很困难的，需要避开这个障碍。

可以设想一个这样的函数
$$
\kappa(\bm{x}_i, \bm{x}_{j}) = \phi(\bm{x}_i)^\intercal \phi(\bm{x}_{j})
$$

即 $\bm{x}_i, \bm{x}_{j}$ 在特征空间的内积等于它们在原始样本空间中通过函数 $\kappa$ 计算的结果。于是可重写对偶问题为
$$
\begin{equation}
    \begin{aligned}
        &\max_{\bm{\alpha}} \sum_{i=1}^m \alpha_i - \frac{1}{2} \sum_{i=1}^m \sum_{j=1}^m \alpha_i \alpha_j y_i y_j \kappa(\bm{x}_i, \bm{x}_j) \\
        &\text{s.t.} \quad \sum_{i=1}^{m}\alpha_i y_i = 0,\,  \alpha_i \ge 0, \quad i = 1, 2, \dots, m
    \end{aligned} \label{5}
\end{equation}
$$

这种方法称为**核技巧**（kernel trick），函数 $\kappa$ 称为**核函数**（kernel function）。

$\eqref{5}$ 显示出模型最优解可通过训练样本的核函数展开，这一展式亦称为**支持向量展式**（support vector expansion）。

若已知映射 $\phi$ 的具体形式，则可写出核函数 $\kappa$。但现实中通常不知道 $\phi$ 的形式，核函数是否一定存在？什么样的函数能做核函数？

!!! note 核函数定理
    令 $\mathcal{X}$ 为输入空间，$\kappa$ 是定义在 $\mathcal{X} \times \mathcal{X}$ 上的对称函数，则 $\kappa$ 是核函数当且仅当对于任意数据集 $D = \left\lbrace \bm{x}_1, \bm{x}_2, \dots, \bm{x}_m \right\rbrace$，「核矩阵」（kernel matrix）$\bm{K} = [\kappa(\bm{x}_i, \bm{x}_{j})]_{m}$ 是半正定的。

也就是说，只要一个对称函数所对应的核矩阵半正定，就能作为核函数使用。实际上对于一个半正定矩阵，总能找到一个与之对应的映射 $\phi$。换言之，任意一个核函数都隐式地定义了一个称为「再生核希尔伯特空间」（reproducing kernel Hilbert space, RKHS）的特征空间。

特征空间的好坏对于支持向量机的性能至关重要，核函数的选择就成为了支持向量机的最大变数。

几种常用的核函数

| 名称 | 表达式 $\kappa(\bm{x}_i, \bm{x}_{j})$ | 参数 |
| :- | :- | :- |
| 线性核 | $\bm{x}_i^\intercal \bm{x}_{j}$ | - |
| 多项式核 | $(\bm{x}_i^\intercal \bm{x}_{j})^d$ | $d \ge 1$ 为多项式的次数 |
|| 高斯核（RBF 核） | $\exp\left( -\frac{\left\lVert \bm{x}_i - \bm{x}_{j} \right\rVert^2}{2\sigma^2} \right)$ | $\sigma > 0$ 为高斯核的带宽（width） |
| 拉普拉斯核 | $\exp\left( -\frac{\left\lVert \bm{x}_i - \bm{x}_{j} \right\rVert}{\sigma} \right)$ | $\sigma > 0$ |
| Sigmoid 核 | $\tanh(\beta \bm{x}_i^\intercal \bm{x}_{j} + \theta)$ | $\beta > 0, \theta < 0$ |

还可以通过函数组合得到
- 若 $\kappa_1, \kappa_2$ 是核函数，则对于任意正数 $\gamma_1, \gamma_2$，其线性组合 $\gamma_1 \kappa_1 + \gamma_2 \kappa_2$ 也是核函数
- 若 $\kappa_1, \kappa_2$ 是核函数，则它们的直积 $\kappa_1 \otimes \kappa_2(\bm{x}, \bm{z}) = \kappa_1(\bm{x}, \bm{z}) \kappa_2(\bm{x}, \bm{z})$ 也是核函数
- 若 $\kappa_1$ 是核函数，则对于任意函数 $g(\bm{x})$，$\kappa(\bm{x}, \bm{z}) = g(\bm{x}) \kappa_1(\bm{x}, \bm{z}) g(\bm{z})$ 也是核函数

## 软间隔与正则化

现实任务中，往往很难确定合适的核函数使得训练样本在特征空间中线性可分。即使找到了某个核函数，也很难断定是否是由于过拟合所造成的。

缓解该问题的一个办法是允许向量机在一些样本上出错，为此需要引入**软间隔**（soft margin）的概念，如下图所示：

![](./06-support-vector-machine/soft-margin.png)

前面介绍的支持向量机形式要求所有样本满足约束 $\eqref{1}$，即所有样本必须划分正确，这称为**硬间隔**（hard margin），而软间隔则允许某些样本不满足约束 $\eqref{1}$。

但与此同时，最大化间隔的同时，不满足约束的样本应尽可能的少，于是优化目标可写为
$$
\begin{equation}
    \min_{\bm{w}, b, \bm{\xi}} \frac{1}{2} \left\| \bm{w} \right\|^2 + C \sum_{i=1}^m \ell_{0 / 1} (y_i(\bm{w}^\intercal \bm{x}_i + b) - 1) \label{6}
\end{equation}
$$

其中 $C > 0$ 是一个常数，$\ell_{0 / 1}$ 是「0/1 损失函数」：
$$
\ell_{0 / 1}(z)\begin{cases}
    1, & z < 0 \\ 
    0, & z \ge 0
\end{cases}
$$

$C$ 为无穷大时，迫使所有样本满足约束，此时为硬间隔；$C$ 为有限值时，允许一些样本不满足约束，此时为软间隔。

然而 $\ell_{0 / 1}$ 数学性质不好，通常使用其他函数替代，称为*替代损失*（surrogate loss），例如
- hinge 损失：$\ell_{\text{hinge}}(z) = \max(0, 1 - z)$
- 指数损失（exponential loss）：$\ell_{\text{exp}}(z) = \exp(-z)$
- 对率损失（logistic loss）：$\ell_{\text{log}}(z) = \log(1 + \exp(-z))$

![](./06-support-vector-machine/surrogate-loss.png)

下面采用了 hinge 损失，虽然没有显式写出。

引入**松弛变量**（slack variables）$\xi_i \ge 0$，则 $\eqref{6}$ 可写为
$$
\begin{equation}
    \begin{aligned}
        &\min_{\bm{w}, b, \bm{\xi}} \frac{1}{2} \left\| \bm{w} \right\|^2 + C \sum_{i=1}^m \xi_i\\
        &\text{s.t.} \quad y_i(\bm{w}^\intercal \bm{x}_i + b) \ge 1 - \xi_i, \quad \xi_i \ge 0, \quad i = 1, 2, \dots, m
    \end{aligned} \label{7}
\end{equation}
$$
这就是常用的「软间隔支持向量机」。

式 $\eqref{7}$ 每个样本都有一个对应的松弛变量，用以<u>表征该样本不满足约束 $\eqref{1}$ 的程度</u>。

类似 $\eqref{2}$，这仍是一个二次规划问题，同样使用拉格朗日乘子法得到拉格朗日函数
$$
\begin{aligned}
    \mathcal{L}(\bm{w}, b, \bm{\alpha}, \bm{\xi}, \bm{\mu}) &= \dfrac{1}{2} \left\lVert \bm{w} \right\rVert^2 + C \sum_{i=1}^{m}\xi_i\\
    &\phantom{=} + \sum_{i=1}^{m}\alpha_i(1 - \xi_i - y_i(\bm{w}^\intercal \bm{x}_i + b)) - \sum_{i=1}^{m}\mu_i \xi_i
\end{aligned}
$$

其中 $\alpha_i, \mu_i \ge 0$ 是拉格朗日乘子。

对 $\bm{w}, b, \xi_i$ 求偏导数为零，得
$$
\left\lbrace\begin{aligned}
    \bm{w} &= \sum_{i=1}^{m}\alpha_i y_i \bm{x}_i \\ 
    0 &= \sum_{i=1}^{m}\alpha_i y_i \\ 
    C &= \alpha_i + \mu_i
\end{aligned}\right.
$$

将上面三个式子代入拉格朗日函数可得对偶问题
$$
\begin{equation}
    \begin{aligned}
        &\max_{\bm{\alpha}} \sum_{i=1}^{m}\alpha_i - \dfrac{1}{2}\sum_{i=1}^{m}\sum_{j=1}^{m}\alpha_i\alpha_j y_i y_j \bm{x}_i^\intercal \bm{x}_j\\
        &\text{s.t.} \quad \sum_{i=1}^{m}\alpha_i y_i = 0,\, 0 \le \alpha_i \le C, \quad i = 1, 2, \dots, m
    \end{aligned} \label{8}
\end{equation}
$$

对照原对偶问题，二者唯一的差别是对于对偶变量的约束不同：原问题是 $0 \le \alpha_i$，而这里是 $0 \le \alpha_i \le C$。于是可以采用同样的算法求解 $\eqref{8}$。引入核函数后能得到与式 $\eqref{5}$ 相同的支持向量展式。

类似的，对软间隔支持向量机，KKT 条件要求
$$
\left\lbrace\begin{aligned}
    &\alpha_i, \mu_i \ge 0\\
    &y_i f(\bm{x}_i) - 1 + \xi_i \ge 0\\
    &\alpha_i (y_i f(\bm{x}_i) - 1 + \xi_i) = 0\\ 
    &\xi_i \ge 0,\, \mu_i \xi_i = 0
\end{aligned}\right.
$$

于是对于任意训练样本 $(\bm{x}_i, y_i)$，总有 $\alpha_i = 0$ 或 $y_i f(\bm{x}_i) = 1 - \xi_i$。

- 若 $\alpha_i = 0$，则该样本不会对 $f(\bm{x})$ 有任何影响。
- 若 $\alpha_i > 0$，则必有 $y_i f(\bm{x}_i) = 1 - \xi_i$，即该样本是支持向量：
    - 若 $\alpha_i < C$，由上面的偏导结果有 $\mu_i > 0$，进而 $\xi_i = 0$，即此时该样本恰在最大间隔边界上。
    - 若 $\alpha_i = C$，则有 $\mu_i = 0$，此时：
        - 若 $\xi_i \le 1$，则该样本落在最大间隔内部。
        - 若 $\xi_i > 1$，则该样本被错误分类。

由此可得，软间隔支持向量机最终模型仅与支持向量有关，即通过 hinge 损失函数仍保持了*稀疏性*。

将 $\eqref{6}$ 的 0/1 损失函数换成别的替代损失函数以得到其他学习模型，这些模型的性质与所用的替代函数直接相关。

但是这些模型都有一个共性：优化目标中的第一项用来描述划分超平面的「间隔大小」，另一项用来表述训练集上的误差，可写为更一般的形式
$$
\min_f \textcolor{ff0099}{\Omega(f)} + C \textcolor{05aa94}{\sum_{i=1}^{m} \ell(f(\bm{x}_i), y_i)} 
$$

- 红色部分，即 $\Omega(f)$ 称为**结构风险**（structural risk），用以描述模型 $f$ 的某些性质
- 蓝色部分，即 $\sum_{i=1}^m\ell(f(\bm{x}_i), y_i)$ 称为**经验风险**（empirical risk），用以描述模型与训练数据的契合程度。

!!! memo ""
    【待补充】
    根据课件与教材。

## 支持向量回归

现在考虑回归问题。给定训练样本 $D = \left\lbrace (\bm{x}_i, y_i) \right\rbrace_{i=1}^m,\, y_i \in \R$，希望学得一个形如 $f(\bm{x}) = \bm{w}^\intercal \bm{x} + b$ 的回归模型，使得 $f(\bm{x})$ 与 $y$ 尽可能接近。而 $\bm{w}, b$ 是待确定的模型参数。

对样本 $(\bm{x}, y)$，传统回归模型通常直接基于模型输出 $f(\bm{x})$ 与真实输出 $y$ 之间的差别来计算损失，当且仅当 $f(\bm{x}) = y$ 时损失才为零。

支持向量回归（Support Vector Regression, SVR）则假设我们能「容忍」$f(\bm{x})$ 与 $y$ 之间最多有 $\epsilon$ 的偏差，即当 $\left| f(\bm{x}) - y \right| \ge \epsilon$ 时才计算损失。

这就相当于以 $f(\bm{x})$ 为中心，构建了一个宽度为 $2\epsilon$ 的间隔带，若训练样本落入此间隔带，则认为是被预测正确的：

![](./06-support-vector-machine/support-vector-regression.png)

于是 SVR 问题可形式化为
$$
\begin{equation}
        \min_{\bm{w}, b} \frac{1}{2} \left\lVert \bm{w} \right\rVert^2 + C \sum_{i=1}^{m}\ell_{\epsilon}(y_i - f(\bm{x}_i)) \label{9}
\end{equation}
$$
其中 $C$ 为正则化常数，$\ell_{\epsilon}$ 是$\epsilon$-不敏感损失（$\epsilon$-insensitive loss）函数：
$$
\ell_{\epsilon}(z)\begin{cases}
    0, & \left| z \right| \le \epsilon \\ 
    \left| z \right| - \epsilon, & \left| z \right| > \epsilon
\end{cases}
$$

![](./06-support-vector-machine/epsilon-insensitive-loss.png)

引入松弛变量 $\xi_i, \hat{\xi}_i$，则 $\eqref{9}$ 可写为
$$
\begin{equation}
    \begin{aligned}
        &\min_{\bm{w}, b, \bm{\xi}, \bm{\hat{\xi}}} \frac{1}{2} \left\lVert \bm{w} \right\rVert^2 + C \sum_{i=1}^{m}(\xi_i + \hat{\xi}_i)\\
        &\text{s.t.} f(\bm{x}_i) - y_i \le \epsilon + \xi_i, \quad y_i - f(\bm{x}_i) \le \epsilon + \hat{\xi}_i, \quad \xi_i, \hat{\xi}_i \ge 0
    \end{aligned} \label{10}
\end{equation}
$$

引入拉格朗日乘子 $\mu_i, \hat{\mu}_i, \alpha_i, \hat{\alpha}_i \ge 0$，拉格朗日函数
$$
\begin{aligned}
    \mathcal{L}(\bm{w}, b, \bm{\xi}, \bm{\hat{\xi}}, \bm{\mu}, \bm{\hat{\mu}}, \bm{\alpha}, \bm{\hat{\alpha}}) &= \dfrac{1}{2}\left\lVert \bm{w} \right\rVert^2 + C\sum_{i=1}^{m}(\xi_i + \hat{\xi}_i) - \sum_{i=1}^{m}\mu_i\xi_i - \sum_{i=1}^{m}\hat{\mu}_i\hat{\xi}_i\\ 
    &\phantom{=} + \sum_{i=1}^{m}\alpha_i(f(\bm{x}_i) - y_i - \epsilon - \xi_i) + \sum_{i=1}^{m}\hat{\alpha}_i(y_i - f(\bm{x}_i) - \epsilon - \hat{\xi}_i)
\end{aligned}
$$

对 $\bm{w}, b, \xi_i, \hat{\xi}_i$ 求偏导数为零，得
$$
\left\lbrace\begin{aligned}
    \bm{w} &= \sum_{i=1}^{m}(\alpha_i - \hat{\alpha}_i)\bm{x}_i \\ 
    0 &= \sum_{i=1}^{m}(\alpha_i - \hat{\alpha}_i) \\ 
    C &= \alpha_i + \mu_i\\
    C &= \hat{\alpha}_i + \hat{\mu}_i
\end{aligned}\right.
$$

将上面四个式子代入拉格朗日函数可得对偶问题
$$
\begin{equation}
    \begin{aligned}
        &\max_{\bm{\alpha}, \bm{\hat{\alpha}}} \sum_{i=1}^{m}[y_i(\hat{\alpha}_i - \alpha_i) - \epsilon(\hat{\alpha}_i + \alpha_i)] - \dfrac{1}{2}\sum_{i=1}^{m}\sum_{j=1}^{m}(\hat{\alpha}_i - \alpha_i)(\hat{\alpha}_j - \alpha_j)\bm{x}_i^\intercal \bm{x}_j\\ 
        &\text{s.t.} \quad \sum_{i=1}^{m}(\hat{\alpha}_i - \alpha_i) = 0,\, 0 \le \alpha_i, \hat{\alpha}_i \le C, \quad i = 1, 2, \dots, m
    \end{aligned} \label{11}
\end{equation}
$$

KKT 条件为
$$
\left\lbrace\begin{aligned}
    &\alpha_i (f(\bm{x}_i) - y_i - \epsilon - \xi_i) = 0\\ 
    &\hat{\alpha}_i (y_i - f(\bm{x}_i) - \epsilon - \hat{\xi}_i) = 0\\ 
    &\alpha_i \hat{\alpha}_i = 0,\, \xi_i \hat{\xi}_i = 0\\ 
    &(C - \alpha_i)\xi_i = 0,\, (C - \hat{\alpha}_i)\hat{\xi}_i = 0
\end{aligned}\right.
$$

!!! memo ""
    【待补充】

## 核方法

给定训练样本 $\left\lbrace (\bm{x}_i, y_i) \right\rbrace_{i=1}^m$，若不考虑偏移项 $b$，无论是 SVM 还是 SVR，学得模型总能表示为核函数 $\kappa(\bm{x}, \bm{x}_i)$ 的线性组合。

!!! info 表示定理（Representer 定理）
    令 $\mathbb{H}$ 为核函数 $\kappa$ 对应的再生核希尔伯特空间，$\left\lVert h \right\rVert_{\mathbb{H}}$ 表示 $\mathbb{H}$ 空间中关于 $h$ 的范数，对于任意单调递增函数 $\Omega\colon [0, \infty ] \to \R$ 和任意非负损失函数 $\ell\colon \R^m \to [0, \infty ]$，优化问题
    $$
    \min_{h \in \mathbb{H}} F(h) = \Omega(\left\lVert h \right\rVert_{\mathbb{H}}) + \ell(h(\bm{x}_1), \dots, h(\bm{x}_m))
    $$
    的解总能表示为
    $$
    h^{*}(\bm{x}) = \sum_{i=1}^{m}\alpha_i \kappa(\bm{x}, \bm{x}_i)
    $$

表示定理对于损失函数没有限制，对正则化项 $\Omega$ 仅要求单调递增，甚至不要求 $\Omega$ 是凸函数。因此对于一般的损失函数和正则化项，上面的优化问题的解都能表示为核函数的线性组合。

人们发展出一系列基于核函数的学习方法，统称为「核方法」（kernel methods）。最常见的是通过「核化」（即引入核函数）来将线性学习器拓展为非线性学习器。
