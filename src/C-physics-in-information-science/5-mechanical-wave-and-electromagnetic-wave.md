---
layout: post
title: 机械波和电磁波
date: 2023-12-15 20:58:33
updated: 2023-12-15 20:58:33
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 机械波

### 平面波波动方程

!!! info 平面波波动方程
    $$
    \boxed{
            \dfrac{\pd^2 y}{\pd x^2} = \dfrac{1}{v^2} \dfrac{\pd^2 y}{\pd t^2}
        }
    $$

    符合这个方程的物质运动，为以 $v$ 为传播速度的波动过程。

## 电磁波

振荡偶极子电矩

$$
p_{\mathrm{e}} = p_0 \cos \omega t
$$

$p_0$ 为电矩的振幅，$\omega$ 为振荡角频率。

!!! note 电磁波性质
    1. 电磁波是一种*横波*
    2. 电磁波具有*偏振性*
    3. $\bm{E}$ 与 $\bm{H}$ 同相位
    4. $\sqrt{\varepsilon} E = \sqrt{\mu} H$（$E = v B$）
    5. 电磁波在介质传播速度 $v = \dfrac{1}{\sqrt{\varepsilon \mu}}$（$c = \dfrac{1}{\sqrt{\varepsilon_0 \mu_0}}$）

!!! info 坡印廷矢量
    $$
    \bm{S} = \bm{E} \boldsymbol{\times} \bm{H}
    $$

    $\bm{S}$ 为能流密度矢量，也称为**坡印廷矢量**，单位为 $\pu{W/m^2}$。

    $$
    \boxed{
            \bar{S} = \dfrac{1}{2} \varepsilon_0 c E_0^2
        }
    $$

    $$
    \boxed{
            \bar{S} = \dfrac{1}{2} \mu_0 c H_0^2
        }
    $$
