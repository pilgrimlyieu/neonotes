---
layout: post
title: 分析力学初步
date: 2023-10-17 15:11:57
updated: 2023-10-17 18:01:12
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 分析力学

!!! memo ""
    我也不知道分析力学跟信物有什么关系。

    总感觉信物上着跟没上没啥区别，除了做作业。没感觉我学到了什么，但又讲了很多。期中前看能不能把分析力学以前的知识点整理一下。

参考[知乎 - 你的小睿子 - 从零学分析力学（拉格朗日力学篇）](https://zhuanlan.zhihu.com/p/156760739)。

### 一些概念

!!! info 虚位移
    在时间和空间位置确定的情况下，**虚位移**是符合约束条件的任意无穷小位移，用 $\delta \vec{r}$ 表示。

由此定义，虚位移所需时间为 $0$。

同理可定义*虚功*。

!!! quote ""
    而质点的速度必定在质点位置处的切平面内，故质点的虚位移也在切平面内，这说明质点的虚位移和所受约束力相互垂直，所以<u>约束力所做虚功为零</u>。

对于上面的这个结论，考虑这样一个情景：两个可看作质点的小球在光滑平面上运动，小球之间存在一根质量可忽略的刚性杆。

这个时候小球所受的约束力就有两个，一是平面的支持力，二是杆对小球的作用力。

由上面我们知道「支持力做的虚功为零」，但杆的作用力与虚位移不垂直，虚功不为零。

对这个情景推导一下：

刚性杆的约束方程可表述为

$$
\left( \vec{r}_1 - \vec{r}_2 \right)^2 = l^2
$$

微分得

$$
\d \left( \vec{r}_1 - \vec{r}_2 \right)^2 = \d l^2 =0
$$

而

$$
\begin{aligned}
    \d \left( \vec{r}_1 - \vec{r}_2 \right)^2 &= 2\left( \vec{r}_1 - \vec{r}_2 \right) \d \left( \vec{r}_1 - \vec{r}_2 \right) \\
    &= 2\left( \vec{r}_1 - \vec{r}_2 \right) \left( \d \vec{r}_1 - \d \vec{r}_2 \right) \\
\end{aligned}
$$

由「牛顿第三定律」知刚性杆对小球的作用力是*等大反向*的，而且*和两小球连线共线*。

由此可设 $\vec{N}_1=-\vec{N}_2=\lambda\left( \vec{r}_1 - \vec{r}_2 \right) $。

虚功

$$
\begin{aligned}
    \delta W &= \vec{N}_1 \cdot \delta \vec{r}_1 + \vec{N}_2 \cdot \delta \vec{r}_2 \\
    &= \lambda\left( \vec{r}_1 - \vec{r}_2 \right) \cdot \delta \vec{r}_1 - \lambda\left( \vec{r}_1 - \vec{r}_2 \right) \cdot \delta \vec{r}_2 \\
    &= \lambda\left( \vec{r}_1 - \vec{r}_2 \right) \cdot \left( \delta \vec{r}_1 - \delta \vec{r}_2 \right) \\
    &=0
\end{aligned}
$$

然而这不代表「三个及以上质点的系统，约束力的总虚功也一定为零」。

不过可以进行新定义：

!!! info 理想约束
    将约束力的总虚功为零的约束称为**理想约束**。

由此可得理想约束下的约束力的总虚功为 $0$。

同时可得，**力学系统所受理想约束力的总虚功为零**。

一般来说，光滑没有摩擦力就是理想约束。

!!! memo ""
    是有点循环论证的意思。

### 达朗贝尔原理

牛顿第二定律得

$$
\vec{F} + \vec{N} = m\ddot{\vec{r}}
$$

其中 $\vec{F}$ 是质点所受的*主动力*，$\vec{N}$ 是质点所受的*理想约束力*。

两边同乘 $\delta \vec{r}$ 得

$$
\vec{F} \cdot \delta \vec{r} + \vec{N} \cdot \delta \vec{r} = m\ddot{\vec{r}} \cdot \delta \vec{r}
$$

理想约束得 $\vec{N}\cdot \delta \vec{r}=0$，所以

$$
\left( \vec{F} - m\ddot{\vec{r}} \right) \cdot \delta \vec{r} = 0
$$

其中 $-m\ddot{\vec{r}}$ 称为*惯性力*。

对多个质点的系统，一样有成立，由此得

!!! info 达朗贝尔原理
    $$
    \displaystyle \sum_{i=1}^{n}\left( \vec{F}_i - m_i\ddot{\vec{r}}_i \right) \cdot \delta \vec{r}_i = 0
    $$

无约束条件下，质点相互无影响，$\delta \vec{r}_i$ 相互独立且不为 $0$，由此有 $\displaystyle \sum_{i=1}^{n}\left(\vec{F}_i-m_i\ddot{\vec{r}}_i\right)=\vec{0}$，即 $\vec{F}=m\ddot{\vec{r}}$，这就是*牛顿第二定律*了。

!!! memo ""
    为何为 $0$ 还需想一想。

达朗贝尔原理一特殊情况：系统处于<u>平衡态</u>，即 $\ddot{\vec{r}}_i=\vec{0}$，此时达朗贝尔原理变为

!!! info 虚功原理
    $$
    \displaystyle \sum_{i=1}^{n}\vec{F}_i \cdot \delta \vec{r}_i = 0
    $$

### 广义坐标

描述平面内任意两个质点组成的系统需要至少四个量 $x_1, x_2, y_1, y_2$，则称这个系统的**自由度**为 $4$。

当用两根刚性杆分别连接坐标原点和第一个质点及两个质点时，$y_1, y_2$ 就可由 $x_1, x_2$ 确定，此时系统的自由度为 $2$。

由此我们可以推出，对于空间中 $n$ 个质点的系统，有 $p$ 个约束力，则该系统的自由度为 $s=3n-p$。

那我们就可以用 $s$ 个量来描述这个系统，这 $s$ 个量就是**广义坐标**，记作 $q_1, q_2, \cdots, q_{s}$。

从广义坐标的定义可以知道，$s$ 个广义坐标彼此独立，互不关联。

这样我们就能去掉达朗贝尔原理中的 $\delta \vec{r}_i$。

### 拉格朗日方程

原来的 $n$ 个坐标是 $q_1,\, q_2,\, \cdots ,\, q_s,\, t$ 的函数，记为 $\vec{r}_i=\vec{r}_i(q_1,\, q_2 ,\, \cdots ,\, q_s,\, t)$，其中 $i=1,\, 2,\, \cdots ,\, n$。

由*全微分*

$$
\d \vec{r}_i=\sum_{\alpha=1}^{s}\frac{\partial \vec{r}_i}{\partial q_\alpha}\d q_\alpha+\frac{\partial \vec{r}_i}{\partial t}\d t
$$

!!! memo ""
    全微分我还不知道，但似乎也没啥问题。

用 $\delta$ 代替 $\d$，并考虑到 $\delta t=0$，则有

$$
\delta \vec{r}_i=\sum_{\alpha=1}^{s}\frac{\partial \vec{r}_i}{\partial q_\alpha}\delta q_\alpha
$$

!!! tip ""
    据称，$\delta$ 与 $\d$ 运算法则相同，我暂时还不知道二者区别。

    由*虚位移*的定义知，$\delta t=0$。

代入达朗贝尔原理得

$$
\sum_{i=1}^{n}\left(\left( \vec{F}_i-m_i\ddot{\vec{r}}_i \right) \cdot \sum_{\alpha=1}^{s}\frac{\partial \vec{r}_i}{\partial q_\alpha}\delta q_\alpha\right)=0
$$

提出 $\delta q_\alpha$，而我们知道 $\delta q_\alpha$ 是相互独立的，因此括号里的乘数为 $0$，有

$$
\sum_{i=1}^{n}\left( \vec{F}_i-m_i\ddot{\vec{r}}_i \right) \cdot \frac{\partial \vec{r}_i}{\partial q_\alpha}=0
$$

方程两项分别进行考虑：

第一项，定义 $Q_{\alpha}= \displaystyle \sum_{i=1}^{n}\vec{F}_i \cdot \frac{\partial \vec{r}_i}{\partial q_\alpha}$，称为**广义力**。

广义力与广义坐标有关，检查量纲也发现是正确的。

第二项是 $\displaystyle \sum_{i=1}^{n}m_i\ddot{\vec{r}}_i \cdot \frac{\partial \vec{r}_i}{\partial q_\alpha}$，涉及到在笛卡尔坐标系的加速度 $\ddot{\vec{r}}_i$，需要进行转换。

考虑体系总动能 $T$

$$
T=\sum_{i=1}^{n}\dfrac{1}{2}m_i\dot{\vec{r}}{}_i^2
$$

由*导数的乘法运算* $(uv)'=uv' + u' v$ 知

$$
\displaystyle \sum_{i=1}^{n}m_i\ddot{\vec{r}}_i \cdot \frac{\partial \vec{r}_i}{\partial q_\alpha} = \frac{\d}{\d t}\left( \sum_{i=1}^{n}m_i\dot{\vec{r}}_i \cdot \frac{\partial \vec{r}_i}{\partial q_\alpha} \right) - \sum_{i=1}^{n}m_i\dot{\vec{r}}_i \cdot \frac{\d}{\d t} \frac{\partial \vec{r}_i}{\partial q_\alpha}
$$

这里需要详细说一下，毕竟 $u$ 和 $v$ 可能并不明显。

$u$ 是 $\dfrac{\partial \vec{r}_i}{\partial q_\alpha}$，$v$ 是 $m_i \dot{\vec{r}}_i$。

因此上面的式子实际上就是

$$
uv' = (uv)' - u' v
$$

然后运用**拉格朗日关系**

!!! info 拉格朗日关系
    $$
    \dfrac{\pd \vec{r}_i}{\pd q_\alpha}=\dfrac{\pd \dot{\vec{r}}_i}{\pd \dot{q}_\alpha}
    $$
    $$
    \frac{\d}{\d t} \frac{\partial \vec{r}_i}{\partial q_\alpha} = \frac{\partial }{\partial q_\alpha} \dfrac{\d \vec{r}_i}{\d t}= \frac{\partial \dot{\vec{r}}_i}{\partial q_\alpha}
    $$

!!! memo ""
    先用着，证明晚点看，晚点写。

得

$$
\begin{aligned}
    \displaystyle \sum_{i=1}^{n}m_i\ddot{\vec{r}}_i \cdot \frac{\partial \vec{r}_i}{\partial q_\alpha} &= \frac{\d}{\d t}\left( \sum_{i=1}^{n}m_i\dot{\vec{r}}_i \cdot \frac{\partial \dot{\vec{r}}_i}{\partial \dot{q}_\alpha} \right) - \sum_{i=1}^{n}m_i\dot{\vec{r}}_i \cdot \frac{\partial \dot{\vec{r}}_i}{\partial q_\alpha}\\
    &= \frac{\d}{\d t}\dfrac{\pd }{\pd \dot{q}_\alpha}\left( \sum_{i=1}^{n} \dfrac{1}{2} m_i \dot{\vec{r}}{}_i^2 \right) - \dfrac{\pd }{\pd q_\alpha}\left( \sum_{i=1}^{n} \dfrac{1}{2} m_i \dot{\vec{r}}{}_i^2 \right)\\
    &= \frac{\d}{\d t}\dfrac{\pd T}{\pd \dot{q}_\alpha} - \dfrac{\pd T}{\pd q_\alpha}
\end{aligned}
$$

第二个等号的原理是

$$
\dot{\vec{r}}_i \pd \dot{\vec{r}}_i = \frac{1}{2} \pd \dot{\vec{r}}{}_i^2
$$

简单的微分运算，只不过塞在一大块里，可能看起来很复杂。

因此式子化简为

!!! info 一般情况下的拉格朗日方程
    $$
    \frac{\d}{\d t}\dfrac{\pd T}{\pd \dot{q}_\alpha} - \dfrac{\pd T}{\pd q_\alpha} = Q_\alpha
    $$

解释一下其中的量：

- $T$ 是体系的**总动能**
- $q_\alpha$ 是**广义坐标**
- $\dot{q}_\alpha$ 是**广义速度**
- $Q_\alpha$ 是**广义力**

同时定义**广义动量** $P_\alpha=\dfrac{\pd T}{\pd \dot{q}_\alpha}$。

验证一下：令 $T=\dfrac{1}{2}mv^2,\, \dot{q}_\alpha=v$ 得 $P_\alpha=mv$，符合动量的定义。

在笛卡尔坐标系下，取 $T=\dfrac{1}{2}mv^2,\,\dot{q}_\alpha=v$，动能与广义坐标无关，与广义坐标的导数，也即广义速度有关。

此时拉格朗日方程化为 $m\ddot{\vec{r}}=\vec{F}$，即*牛顿第二定律*。

考虑力学系统中所受的主动力全为**保守力**的情况：

!!! info 保守力
    做的功与路径无关，仅与起点和终点有关的作用力称为**保守力**。

主动力全为保守力，力学系统存在势能 $U$，且只与 $\vec{r}_i$ 有关，即 $U=U(\vec{r}_1,\, \vec{r}_2,\, \cdots ,\, \vec{r}_n)$。

引入势能后，力可以用势能进行表示，即 $\vec{F}_i=-\dfrac{\pd U}{\pd \vec{r}_i}$。

!!! tip ""
    负号我猜测是因为，如果力为正，那么势能减小，偏导就为负。

    比如重力做功，那么重力势能就会减小。

则广义力 $Q_\alpha=\displaystyle \sum_{i=1}^{n}\vec{F}_i \cdot \frac{\partial \vec{r}_i}{\partial q_\alpha}=-\sum_{i=1}^{n}\frac{\pd U}{\pd \vec{r}_i} \cdot \frac{\partial \vec{r}_i}{\partial q_\alpha}=-\frac{\pd U}{\pd q_\alpha}$。

代入拉格朗日方程得

$$
\frac{\d}{\d t}\dfrac{\pd T}{\pd \dot{q}_\alpha} - \dfrac{\pd T}{\pd q_\alpha} = -\frac{\pd U}{\pd q_\alpha} \implies \frac{\d}{\d t}\dfrac{\pd T}{\pd \dot{q}_\alpha} - \dfrac{\pd (T-U)}{\pd q_\alpha} = 0
$$

而势能 $U$ 与广义速度 $\dot{q}_\alpha$ 无关，因此 $\dfrac{\pd U}{\pd \dot{q}_\alpha}=0$，有

$$
\frac{\d}{\d t}\dfrac{\pd (T-U)}{\pd \dot{q}_\alpha} - \dfrac{\pd (T-U)}{\pd q_\alpha} = 0
$$

定义**拉格朗日函数** $L=T-U$，则有

!!! info 保守体系的拉格朗日方程
    $$
    \frac{\d}{\d t}\dfrac{\pd L}{\pd \dot{q}_\alpha} - \dfrac{\pd L}{\pd q_\alpha} = 0
    $$

> 更准确的说，这是**保守体系下完整系统的拉格朗日方程**。

!!! memo ""
    完整约束和不完整约束的部分我先跳过。

    下面将讲最速降线、泛函和变分，而我还没看明白，所以本篇内容先到这里。

    本篇内容（至此）全在 CPL 课上完成。非常感谢知乎文章的作者，与 Copilot 的鼎力支持（好多公式都是 Copilot 写的）。
