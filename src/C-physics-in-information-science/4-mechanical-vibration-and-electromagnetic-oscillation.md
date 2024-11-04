---
layout: post
title: 机械振动和电磁振荡
date: 2023-12-15 20:58:33
updated: 2023-12-15 20:58:33
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 谐振动

!!! info ""
    如果物体受力的大小与物体对其平衡位置的位移成正比而方向相反，即

    $$
    F = -kx
    $$

    或

    $$
    \dfrac{\d^2 x}{\d t^2} + \omega^2 x = 0
    $$

    则称物体做**谐振动**，其中 $\omega = \sqrt{\dfrac{k}{m}}$ 称为**谐振动的角频率**，$T = \dfrac{2\pi}{\omega}$ 称为**谐振动的周期**。

    通解为

    $$
    \boxed{
            x = A \cos(\omega t + \phi_0)
        }
    $$

    也可写作

    $$
    x = A \e^{\i (\omega t + \phi_0)}
    $$

    有

    $$
    \left\lbrace\begin{aligned}
        A &= \sqrt{x_0^2 + \left(\dfrac{v_0}{\omega}\right)^2} \\
        \phi_0 &= \arctan \left(- \dfrac{v_0}{\omega x_0} \right)
    \end{aligned}\right.
    $$


!!! note 谐振波的能量
    $$
    \boxed{E = \dfrac{1}{2} k A^2}
    $$

## 阻尼振动

!!! info ""
    若阻力与速度成正比，即

    $$
    F_{\mathrm{f}} = - \gamma \dfrac{\d x}{\d t}
    $$

    则称物体做**阻尼振动**，其中 $\gamma$ 称为*阻力系数*。

    物体运动方程为

    $$
    m \dfrac{\d^2 x}{\d t^2} = -k x - \gamma \dfrac{\d x}{\d t}
    $$

    令

    $$
    \delta = \dfrac{\gamma}{2m}
    $$

    为**阻尼系数**，则微分方程通解为

    $$
    \boxed{
            x = A \e^{-\delta t} \cos(\omega' t + \phi_0')
        }
    $$

    其中

    $$
    \omega' = \sqrt{\omega^2 - \delta^2}
    $$

    则

    $$
    T = \dfrac{2\pi}{\omega'} = \dfrac{2\pi}{\sqrt{\omega^2 - \delta^2}}
    $$

## 受迫振动

!!! info ""
    假设驱动力

    $$
    F_{\mathrm{d}} = F_0 \cos \omega_{\mathrm{d}} t
    $$

    其中 $F_0$ 为驱动力的最大值，$\omega_{\mathrm{d}}$ 为驱动力的角频率，则物体运动方程为

    $$
    m \dfrac{\d^2 x}{\d t^2} = -k x - \gamma \dfrac{\d x}{\d t} + F_0 \cos \omega_{\mathrm{d}} t
    $$

    或

    $$
    \dfrac{\d^2 x}{\d t^2} + 2 \delta \dfrac{\d x}{\d t} + \omega_0^2 x = \dfrac{F_0}{m} \cos \omega_{\mathrm{d}} t
    $$

    阻尼较小时，解为

    $$
    x = A_0 \e^{-\delta t} \cos(\sqrt{w_0^2 - \delta^2} t + \phi_0') + A \cos(\omega_{\mathrm{d}} t + \phi)
    $$

    稳定后

    $$
    x = A \cos(\omega_{\mathrm{d}} t + \phi)
    $$

!!! note ""
    1. 受迫振动的角频率不是振子的固有角频率，而是**驱动力的角频率**。
    2. 受迫振动的振幅<u>不是决定于振子的初始状态</u>，而是依赖于振子的性质、阻尼的大小和驱动力的特征。
    3. 相位是稳态受振动的位移和驱动力的相位差，这也<u>与初始条件无关</u>。

    有

    $$
    \begin{aligned}
        A &= \dfrac{F_0}{m \sqrt{(\omega_0^2 - \omega_{\mathrm{d}}^2)^2 + (2 \delta \omega_{\mathrm{d}})^2}} \\
        \tan \phi &= \dfrac{2 \delta \omega_{\mathrm{d}}}{\omega_{\mathrm{d}}^2 - \omega_{0}^2}
    \end{aligned}
    $$

    稳定时

    $$
    v = \dfrac{\d x}{\d t} = v_{\mathrm{m}} \cos\left(\omega_{\mathrm{d}} t + \phi + \dfrac{\pi}{2}\right)
    $$

    其中

    $$
    v_{\mathrm{m}} = \omega_{\mathrm{d}} A
    $$

## 共振

位移振幅最大时，令 $\dfrac{\d A}{\d \omega_{\mathrm{d}}} = 0$，有共振角频率

$$
\omega' = \sqrt{\omega_0^2 - 2 \delta^2}
$$

速度共振，令 $\dfrac{\d v_{\mathrm{m}}}{\d \omega_{\mathrm{d}}} = 0$，有共振角频率

$$
\omega' = \omega_0
$$

## 电磁振动

!!! info ""
    无阻尼 LC 振荡电路自由振荡频率和周期分别为

    $$
    \nu = \dfrac{\omega}{2 \pi} = \frac{1}{2\pi\sqrt{LC}}
    $$

    $$
    T = 2\pi\sqrt{LC}
    $$

!!! note ""
    **电流振幅**表示电流最大值，有

    $$
    I_0 = \omega Q_0
    $$

    其中 $Q_0$ 为电荷振幅，表示电荷最大值。

!!! note ""
    总能量

    $$
    W = \dfrac{Q_0^2}{2 C}
    $$

!!! info ""
    $\omega_{\mathrm{d}} = \dfrac{1}{\sqrt{LC}}$ 时，电路中的电流振幅最大。

    即外加电动势的频率和自由振荡的固有频率相等时，电路中的电流振幅最大，值为 $\dfrac{\mathscr{E}_0}{R}$。这种在周期性电动势作用下，电路中电流振幅最大的现象称为**电共振**。

    此时电流与外加电动势相位差 $\phi' = 0$。

!!! note 力电类比
    |           机械振动            |     电磁振动（串联电路）      |
    |           :------:            |     :------------------:      |
    |           位移 $x$            |           电荷 $q$            |
    |           速度 $v$            |           电流 $i$            |
    |           质量 $m$            |           电感 $L$            |
    |         劲度系数 $k$          |    电容倒数 $\dfrac{1}{C}$    |
    |       阻力系数 $\gamma$       |           电阻 $R$            |
    |    驱动力 $F_{\mathrm{d}}$    |     电动势 $\mathscr{E}$      |
    | 弹性势能 $\dfrac{1}{2} k x^2$ | 电场能量 $\dfrac{1}{2} C q^2$ |
    |   动能 $\dfrac{1}{2} m v^2$   | 磁场能量 $\dfrac{1}{2} L i^2$ |
