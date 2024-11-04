---
layout: post
title: 气体动理论
date: 2023-10-31 14:50:41
updated: 2023-11-01 17:21:15
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 气体动理论

### 一些概念

#### 平衡态

!!! info 平衡态
    在不受外界影响的条件下，系统的宏观性质不随时间变化的状态。


- 气体处于热平衡、力学平衡与化学平衡
- 微观物理量会继续变化，所以为*热动平衡状态*

注意：如果将一根金属棒的两端分别放在沸水和冰水混合物中，经过一段时间，虽然棒上各处温度不随时间而变化，但这种状态不是平衡态，而是**定常态**，因为金属棒与外界有能量交换。

!!! info 准静态过程（平衡过程）
    当气体从一个状态变化到另一个状态，如果过程进展十分缓慢，使得经历的一系列中间状态都无限接近平衡状态。

#### 状态参量

!!! info 状态参量
    为了描述系统的平衡状态，常采用一些物理量来表示物体的有关特性，这些描述状态的变量，叫做**状态参量**。

在热力学中通常把描写均匀系的变量分为两类，

!!! info 广延量
    与总质量成比例的。

    如*体积*、*内能*、*熵*、*焓*等。

!!! info 强度量
    代表物质的内在性质，与总质量无关的。

    如*温度*、*压强*、*密度*等。

广延量和强度量可以用一个齐次函数来表示。一个广延量应是广延量的一次齐次函数，而一个强度量应是广延量的零次齐次函数。

对于多元均匀系，其体积

$$
V = V\left( T, p, N_1 , \cdots , N_k \right)
$$

若各组元的分子数同时增加 $\lambda$ 倍而总体积亦增加 $\lambda$ 倍，即 $V' = V\left( T, p, \lambda N_1, \cdots, \lambda N_k \right)=\lambda V\left( T, p, N_1, \cdots, N_k \right)$，则 $V$ 为广延量。

#### 孤立系 闭系 开系

- **孤立系**：系统与外界没有能量交换和物质交换
- **闭系**：有能量交换，但是没有物质交换
- **开系**：有能量交换和物质交换

### 理想气体物态方程

$$
pV = \dfrac{m}{M}RT
$$

其中 $R$ 为**普适气体常量**，

$$
R = \pu{8.31 J . mol-1 . K-1}
$$

### 压强

设长方体容器边长分别为 $l_x, l_y, l_z$，有 $N$ 个同类气体分子，分子数密度为 $n = \dfrac{N}{l_x l_y l_z}$，分子质量为 $m_0$。

考虑其中一个分子 $i$，速度为 $\vec{v}_i$。

分子一次撞到 $x$ 面给器壁的冲量为 $2m_0 v_{ix}$。

单位时间内，分子与 $x$ 面碰撞的次数为 $\dfrac{v_{ix}}{2l_x}$。（因 $x$ 方向上路程为 $2l_x$）。

则单位时间内该分子给予 $x$ 面的冲量为 $2m_0v_{ix} \cdot \dfrac{v_{ix}}{2l_x}$。

单位时间内所有分子给予 $x$ 面的冲量（即平均力）为

$$
\bar{F}= \sum_{i=1}^N 2m_0v_{ix} \cdot \dfrac{v_{ix}}{2l_x} = \dfrac{m_0}{l_x} \sum_{i=1}^N v_{ix}^2
$$

压强为

$$
\begin{aligned}
    p &= \dfrac{\bar{F}}{l_y l_z}\\
    &= \dfrac{m_0}{l_x l_y l_z} \sum_{i=1}^N v_{ix}^2\\
    &= \dfrac{Nm_0}{l_x l_y l_z} \cdot \dfrac{1}{N} \sum_{i=1}^N v_{ix}^2\\
    &= n m_0 \bar{v}_x^2
\end{aligned}
$$

!!! tip ""
    这里的 $\bar{v}_x^2$（`\bar{v}_x^2`）指的其实是 $\bar{v^2_x}$（`\bar{v^2_x}`），即速度平方的平均，而非平均速度 $\bar{v}$ 的平方。

    只不过我觉得后者不好看，因此用前者。再次特地说明，以免引起误解。

而 $\bar{v}_x^2$ 为 $x$ 方向上分子速度的平均值，即有 $\bar{v}_x^2 + \bar{v}_y^2 + \bar{v}_z^2 = \bar{v}^2$。

!!! tip ""
    有了上面这个提示，我们可以知道对任意一个子速度 $v_i$，可以分解为 $v_{ix}, v_{iy}, v_{iz}$，且有 $v_i^2=v_{ix}^2 + v_{iy}^2 + v_{iz}^2$，累加后平均，则有上面的结论。

根据统计规律，有 $\bar{v}_x^2 = \bar{v}_y^2 = \bar{v}_z^2 = \dfrac{1}{3}\bar{v}^2$。

而分子平均动能 $\bar{\varepsilon}_k=\dfrac{1}{2}m_0\bar{v}^2$，代入得

$$
\boxed{p = \dfrac{2}{3}n\bar{\varepsilon}_k}
$$

### 温度的本质和统计意义

理想气体物态方程变换得

$$
p = \dfrac{N}{V} \dfrac{R}{N_A} T
$$

称 $k = \dfrac{R}{N_A}$ 为**玻尔兹曼常数**，其值为

$$
k = \pu{1.38e-23 J . K-1}
$$

则

$$
\boxed{p = nkT}
$$

得温度公式

$$
\boxed{\bar{\varepsilon}_k = \dfrac{3}{2}kT}
$$

即<u>气体温度是气体分子平均动能的量度</u>。

### 气体分子的方均根速率

气体分子的方均根速率为

$$
v_{\mathrm{rms}}=\sqrt{\bar{v}^2}=\sqrt{\dfrac{3kT}{m_0}}=\sqrt{\dfrac{3RT}{M}}
$$

### 分子的自由度

!!! info 自由度
    **自由度**是指物理学当中描述一个物理状态，独立对物理状态结果产生影响的变量的数量。

*单原子分子*有 $3$ 个自由度，因为描述其位置需要三个坐标。

*双原子分子*如果分子间相对位置保持不变，则可以用 $5$ 个变量描述。质心的位置需要 $3$ 个变量，连线的方位需要 $2$ 个变量。

因此*双原子分子*有 $5$ 个自由度。其中 $3$ 个为**平动自由度**，$2$ 个为**转动自由度**。

*三原子及多原子分子*如果分子间相对位置保持不变，则整个分子就是**自由刚体**，其自由度为 $6$。其中 $3$ 个为**平动自由度**，$3$ 个为**转动自由度**。

!!! tip ""
    这里自由度的概念我还有点模糊，不过问题应该不大。

原子间距离不变的分子一般称为**刚性分子**。双原子分子和多原子分子一般不是完全刚性的，分子内部会出现振动，因此还有**振动自由度**。常温下可以不予考虑。

!!! tip ""
    高温下不可忽略！

### 能量按自由度均分定理

在不考虑转动的情况下，可以认为分子动能 $\bar{\varepsilon}_k=\dfrac{3}{2}kT$ 均分在三个平动自由度上。

考虑转动，平动和转动，及各个转动自由度间可以进行能量交换，因此各个自由度平均动能都应该相等。由此有

!!! info 能量按自由度均分定理
    在热平衡状态下，每个自由度所对应的平均动能为 $\dfrac{1}{2}kT$。

即如果气体分子共有 $i$ 个自由度，则其平均总动能为

$$
\boxed{\bar{\varepsilon}_k = \dfrac{i}{2}kT}
$$

!!! quote ""
    如果气体分子不是刚性的，那么，除上述平动与转动自由度以外，还存在着振动自由度。对应于每一个振动自由度，每个分子除有 $\dfrac{1}{2} k T$ 的平均振动动能外，还具有 $\dfrac{1}{2} k T$ 的平均弹性势能，所以，在每一振动自由度上将分配到量值为 $k T$ 的平均能量。

    以上选自课本，~~考试应该不考~~。

综上，质量为 $m$ 的理想气体的内能为

$$
\boxed{E = \dfrac{m}{M}\dfrac{i}{2}RT}
$$

一定量的理想气体的内能完全决定于分子运动的自由度 $i$ 和气体的热力学温度 $T$，而与气体的体积和压强无关。

或者说，<u>理想气体的内能只是温度的单值函数</u>。

因此，内能是理想气体的*状态量*，与变化路径无关。

### 气体分子速率分布函数

设速率处在 $v \sim v + \Delta v$ 之间的分子数为 $\Delta N$，则其在总分子数 $N$ 中所占的比例为 $\dfrac{\Delta N}{N}$。

当 $\Delta v \to 0$ 时，有 $\dfrac{\Delta N}{N} \propto \Delta v$，且分布与 $v$ 有关。

由此定义

$$
f(v) = \lim_{\Delta v \to 0} \dfrac{\Delta N}{N \Delta v}=\dfrac{\d N}{N\d v}
$$

为**分子速率分布函数**，描述在速率 $v$ 附近单位速率区间内分子数占总分子数的比例。

对于单个分子，它表示分子速率在 $v$ 附近单位速率区间内的概率。因此也称为分子速率分布的概率密度。

则速率处在 $v_1 \sim v_2$ 区间的分子数为

$$
\Delta N = \int_{v_1}^{v_2} N f(v) \d v
$$

对于所有分子，有

$$
N = \int_0^\infty N f(v) \d v
$$

即

$$
\int_0^\infty f(v) \d v = 1
$$

这称为**归一化条件**，是概率分布函数的基本性质。

!!! info 速率平均值
    $$
    \begin{aligned}
        \bar{v} &= \dfrac{\displaystyle \int_{0}^{\infty}v\d N}{N}\\
        &= \dfrac{\displaystyle \int_{0}^{\infty}v \cdot Nf(v)\d v}{N}\\
        &= \int_{0}^{\infty}vf(v)\d v
    \end{aligned}
    $$

!!! info 速率平方平均值
    $$
    \begin{aligned}
        \bar{v}^2 &= \dfrac{\displaystyle \int_{0}^{\infty}v^2\d N}{N}\\
        &= \dfrac{\displaystyle \int_{0}^{\infty}v^2 \cdot Nf(v)\d v}{N}\\
        &= \int_{0}^{\infty}v^2f(v)\d v
    \end{aligned}
    $$

### 麦克斯韦速率分布律

!!! info 麦克斯韦速率分布律
    $$
    f(v) = 4\pi \left( \dfrac{m_0}{2\pi kT} \right)^{\frac{3}{2}} \exp \left( -\dfrac{m_0 v^2}{2kT} \right) v^2
    $$

$m_0$ 为每个分子的质量，$k$ 为玻尔兹曼常数，$T$ 为气体的热力学温度。

!!! info 最概然速率
    麦克斯韦速率分布曲线的最大值对应的速率称为**最概然速率**。
    $$
    \begin{aligned}
        \dfrac{\d f(v)}{\d v} \as_{v=v_{\mathrm{p}}} = 0 &\implies\\
         4 \pi \left( \dfrac{m_0}{2\pi kT} \right)^{\frac{3}{2}} \exp &\left( -\dfrac{m_0 v_{\mathrm{p}}^2}{2kT} \right) \left[ 2v_{\mathrm{p}} - \dfrac{m_0 v_{\mathrm{p}}^3}{kT} \right] = 0\\
        &\implies v_{\mathrm{p}} = \sqrt{\dfrac{2kT}{m_0}}\\
        &\implies \boxed{v_{\mathrm{p}} = \sqrt{\dfrac{2RT}{M}}}
    \end{aligned}
    $$

!!! info 平均速率
    $$
    \begin{aligned}
        \bar{v}&= \int_{0}^{\infty}vf(v)\d v \\
        &= \sqrt{\dfrac{8kT}{\pi m_0}}\\
        &= \boxed{\sqrt{\dfrac{8RT}{\pi M}}}
    \end{aligned}
    $$

    证明：

    记 $b=\dfrac{m_0}{2kT}$，则 $f(v) = 4\pi^{-\frac{1}{2}} b^{\frac{3}{2}} \exp(-bv^2) v^2$。

    则

    $$
    \begin{aligned}
        \bar{v} &= \int_{0}^{\infty}vf(v)\d v\\
            &= 4\pi^{-\frac{1}{2}} b^{\frac{3}{2}} \int_{0}^{\infty}v^3 \exp(-bv^2) \d v\\
            &= 2\pi^{-\frac{1}{2}} b^{-\frac{1}{2}} \int_{0}^{-\infty}(-bv^2) \exp(-bv^2)\d (-bv^2)\\
            &= 2\pi^{-\frac{1}{2}} b^{-\frac{1}{2}} \int_{1}^{0}(-bv^2) \d \exp(-bv^2)\\
            &= 2\pi^{-\frac{1}{2}} b^{-\frac{1}{2}} \left[ -bv^2 \exp(-bv^2) \as^{\infty }_{v=0} - \int_{0}^{-\infty}\exp(-bv^2)\d (-bv^2)\right]\\
            &= 2\pi^{-\frac{1}{2}} b^{-\frac{1}{2}} \left[ 0 - \exp(-bv^2) \as^{\infty }_{v=0}\right]\\
            &= 2\pi^{-\frac{1}{2}} b^{-\frac{1}{2}}\\
            &= \sqrt{\dfrac{8kT}{\pi m_0}}\\
    \end{aligned}
    $$

!!! info 方均根速率
    $$
    \bar{v}^2 = \int_{0}^{\infty}v^2f(v)\d v = \dfrac{3kT}{m_0}
    $$

    $$
    \begin{aligned}
        v_{\mathrm{rms}} &= \sqrt{\bar{v}^2}\\
        &= \sqrt{\dfrac{3kT}{m_0}}\\
        &= \boxed{\sqrt{\dfrac{3RT}{M}}}
    \end{aligned}
    $$

    证明：

    记 $b=\dfrac{m_0}{2kT}$，则 $f(v) = 4\pi^{-\frac{1}{2}} b^{\frac{3}{2}} \exp(-bv^2) v^2$。

    则

    $$
    \begin{aligned}
        \bar{v}^2 &= \int_{0}^{\infty}v^2f(v)\d v\\
            &= 4\pi^{-\frac{1}{2}} b^{\frac{3}{2}} \int_{0}^{\infty}v^4 \exp(-bv^2) \d v\\
            &= -4\pi^{-\frac{1}{2}} b^{\frac{1}{2}} \int_{0}^{\infty}v^3\d \exp(-bv^2)\\
            &= -4\pi^{-\frac{1}{2}} b^{\frac{1}{2}} \left[ v^3 \exp(-bv^2) \as^{\infty }_{v=0} - \int_{0}^{\infty}3v^2\exp(-bv^2)\d v\right]\\
            &= -4\pi^{-\frac{1}{2}} b^{\frac{1}{2}} \left[ 0 - \int_{0}^{\infty}3v^2\exp(-bv^2)\d v\right]\\
            &= -6\pi^{-\frac{1}{2}} b^{-\frac{1}{2}} \int_{1}^{0}v\d \exp(-bv^2)\\
            &= -6\pi^{-\frac{1}{2}} b^{-\frac{1}{2}} \left[ v \exp(-bv^2)\as_{v=0}^{\infty } - \int_{0}^{\infty}\exp(-bv^2)\d v \right]\\
            &= -6\pi^{-\frac{1}{2}} b^{-\frac{1}{2}} \left[ 0 - \int_{0}^{\infty}\exp(-bv^2)\d v \right]\\
            &= 6\pi^{-\frac{1}{2}} b^{-\frac{1}{2}} \int_{0}^{\infty}\exp(-bv^2)\d v\\
    \end{aligned}
    $$

    完蛋了，我忘记老师的做法了。这个积分是正态分布的那个积分，我记得要用什么换元然后一个二重积分，我当然还不会。等我会想起老师的做法再说吧。

$k$ 为玻尔兹曼常量，$R$ 为普适气体常量，$M$ 为气体摩尔质量。

三个速率大小关系

$$
\boxed{v_{\mathrm{rms}} > \bar{v} > v_{\mathrm{p}}}
$$

### 分子碰撞和平均自由程

#### 分子碰撞截面

我不想加图片，就直接口述了。

A 分子视为静止，B 分子束向 A 分子平行发射运动。接近 A 分子时 B 分子的运动方向会发生偏转，当 B 分子偏折角开始变为 $0$ 时的 A、B 分子间的距离称为**分子有效直径** $d$。

!!! tip ""
    为啥叫直径啊。。。不应该是半径吗？

圆面积 $S=\pi d^2$ 称为**分子碰撞截面**。

对于有效直径为 $d_1,\, d_2$ 的两刚球分子[^1]间的碰撞，其碰撞截面为 $S=\pi (d_1+d_2)^2$。

!!! tip ""
    这个我要再研究一下。

#### 分子平均碰撞频率 平均自由程

单位时间内（$\pu{1s}$）内一个分子和其它分子碰撞碰撞的平均次数称为**分子平均碰撞频率**，记为 $\bar{Z}$。

每两次连续碰撞间一个分子自由运动的平均路程称为**平均自由程**，记为 $\bar{\lambda}$。

#### 平均自由程公式

设单位体积内分子数为 $n$，分子平均相对速率 $\bar{v}_{\mathrm{r}}$，分子算术平均速率 $\bar{v}$。

!!! tip ""
    根据*麦克斯韦速率分布和式*，有

    $$
    \bar{v}_{\mathrm{r}} = \sqrt{2}\bar{v}
    $$

    这个我要再想一想。

而 $p=nkT$，则有

$$
\begin{aligned}
    \bar{Z} &= \pi d^2 \bar{v}_{\mathrm{r}} n\\
    &= \sqrt{2} \pi d^2 \bar{v} n\\
    &= \dfrac{4 \pi d^2 p }{\sqrt{\pi m_0 k T}}
\end{aligned}
$$

$$
\begin{aligned}
    \bar{\lambda} &= \dfrac{\bar{v}}{\bar{Z}}\\
    &= \dfrac{1}{\sqrt{2}\pi d^2 n}\\
    &= \dfrac{kT}{\sqrt{2}\pi d^2 p}
\end{aligned}
$$

!!! quote ""
    应该注意，分子并不是真正的球体。当分子相距极近时，它们之间的相互作用力是斥力。

    分子间的相互斥力开始起显著作用时，两分子质心间的最小距离的平均值就是 $d$，所以 $d$ 叫做分子的有效直径。

    实验证明，气体密度一定时，分子的有效直径将随速度的增加而减小，所以当 $T$ 与 $p$ 的比值一定，$\bar{\lambda}$ 将随温度的升高而略有增加。

[^1]: 刚性球形分子？
