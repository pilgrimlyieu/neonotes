---
layout: post
title: 计算机系统概述
date: 2024-09-02 10:38:07
updated: 2024-09-09 10:44:11
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

前略。

## 计算机系统性能评价

### 计算机性能的定义

计算机性能基本指标：
1. 任务提交开始到完成所用的时间（**响应时间**）
2. 单位时间所完成的工作量（**吞吐率**）

比较计算机的性能时，常常用**执行时间**来衡量。完成同样工作量所需时间最短的那台计算机就是性能最好的。

但处理器时间往往被多个程序共享使用，因此用户感觉到的程序执行时间并不是程序真正的执行时间。

通常将*用户感觉到的响应时间*分成
- **用户 CPU 时间**：用来运行用户代码的时间
- **其他时间**：CPU 运行操作系统、等待 I/O 操作完成、CPU 花在其他用户程序的时间

系统性能和 CPU 性能不等价：
- **系统性能**：系统响应时间，与 CPU 外的其他部分也有关系
- **CPU 性能**：用户 CPU 时间

计算机系统的性能主要考虑 CPU 性能，即用户 CPU 时间。

用户 CPU 时间涉及的概念和参数：
- **时钟周期**：计算机产生的同步时钟定时信号(CPU 主脉冲信号)的宽度
- **时钟频率**：主脉冲信号的时钟频率，CPU 时钟周期的倒数
- **CPI**：执行一条指令所需的时钟周期数。对于一条指令，CPI 是确定值；对于一个程序或机器，综合 CPI 是所有指令的平均时钟周期数。

$$
\begin{aligned}
    \text{用户 CPU 时间} &= \text{程序总时钟周期数} \div \text{时钟频率} \\
    &= \text{指令总条数} \times \text{时钟周期}\\
    \text{程序总时钟周期数} &= \text{程序指令总条数} \times \text{CPI}\\
    &= \sum_{i=1}^{n} (\text{CPI}_i \times \text{C}_i)\\
    \text{CPI} &= \sum_{i=1}^{n} (\text{CPI}_i \times \text{F}_i)
\end{aligned}
$$

其中 $\text{CPI}_i, \text{C}_i, \text{F}_i$ 是第 $i$ 类指令的 CPI 、指令条数及其在程序中的出现频率。

$$
\boxed{
        \begin{aligned}
            \text{用户 CPU 时间} &= \text{程序总指令条数} \times \text{CPI} \times \text{时钟周期}\\
            &= \text{程序总指令条数} \times \text{CPI} \div \text{时钟频率}
        \end{aligned}
    }
$$

这三个参数相互制约，提高时钟频率不能保证速度同倍数提高。

### 用指令执行速度进行性能评估

**指令速度计量单位**：平均每秒钟执行多少百万条指令（**MIPS**, Million Instructions Per Second）；因为每条指令执行时间不同，所以 MIPS 总是一个平均值。

因不同机器的指令集不同、程序由不同的指令混合而成、指令使用的频度动态变化等原因，MIPS 不能说明性能的好坏。

**浮点操作速度**：**MFLOPS**(Million Floating-point Operations Per Second)

MFLOPS 与机器相关性大、并不是程序中花时间的部分，用以表示性能也有局限。

### 用基准程序进行性能评估

**基准测试程序**是<u>专门用来进行性能评价的一组程序</u>；在不同机器上运行相同的基准程序比较运行时间来测评性能；基准程序能够反映计机器在运行实际负载时的性能。

缺陷：基准程序的性能与某段短代码密切相关时，会被利用以得到不当的性能评测结果。

**SPEC**(Standard Performance Evaluation Corporation)：引用最广泛也是最全面的基准程序集。

### 综合性能评价

执行时间的规格化：测试机器相对于参考机器的性能。

$$
\text{规格化执行时间} = \dfrac{\text{参考机器执行时间}}{\text{测试机器执行时间}}
$$

根据*算术平均*执行时间能得到总平均执行时间；平均规格化执行时间应该用*几何平均*。

!!! info Amdahl 定律（阿姆达尔定律）
    对系统中某部分（硬件或软件）进行更新所带来的系统性能改进程度，取决于该部分被使用的频率或其执行时间占总执行时间的比例。

    $$
    \begin{aligned}
        \text{改进后的执行时间} &= \dfrac{\text{改进部分执行时间}}{\text{改进部分的改进倍数}} + \text{未改进部分执行时间}\\
        \text{整体改进倍数} &= \dfrac{1}{\frac{\text{改进部分执行时间比例}}{\text{改进部分的改进倍数}} + \text{未改进部分执行时间比例}}
    \end{aligned}
    $$

    即

    $$
    \boxed{p = \dfrac{1}{\frac{t}{n} + 1 - t}}
    $$

    上面的 $p$ 是整体改进倍数，$t$ 是改进部分执行时间比例，$n$ 是改进部分的改进倍数。

## 数据的机器级表示

本节很多内容可见[计算系统基础笔记](/notes/E-fundamentals-of-computing-systems/02-machine-representation-of-data)，不再重复书写。

- 二进制（binary）：$1011 \text{B}$
- 八进制（octal）：$13 \text{O}$
- 十进制（decimal）：$11 \text{D}$ 或 $11$
- 十六进制（hexadecimal）：$\text{BH}$

快速转换法（十进制转二进制）——最近权法：

$$
\left\lbrace\begin{aligned}
    2^{-1} &= 0.5\\
    2^{-2} &= 0.25\\
    2^{-3} &= 0.125\\
    2^{-4} &= 0.0625\\
    2^{-5} &= 0.03125\\
    \vdots\\
    2^{12} &= 4096\\
    2^{13} &= 8192\\
    2^{14} &= 16384\\
    2^{15} &= 32768\\
    2^{16} &= 65536\\
\end{aligned}\right.
$$

|   单词    | 十进制前缀  |    值     |
|    :-:    |     :-:     |    :-:    |
| kilobyte  | $\text{KB}$ |  $10^3$   |
| megabyte  | $\text{MB}$ |  $10^6$   |
| gigabyte  | $\text{GB}$ |  $10^9$   |
| terabyte  | $\text{TB}$ | $10^{12}$ |
| petabyte  | $\text{PB}$ | $10^{15}$ |

IEC 给出了表示二进制信息大小的单位

|   单词   | IEC 定义的二进制前缀 |    值    | 与十进制前缀值差 |
|   :-:    |         :-:          |   :-:    |       :-:        |
| kibibyte |     $\text{KiB}$     | $2^{10}$ |      $2\%$       |
| mebibyte |     $\text{MiB}$     | $2^{20}$ |      $5\%$       |
| gibibyte |     $\text{GiB}$     | $2^{30}$ |      $7\%$       |
| tebibyte |     $\text{TiB}$     | $2^{40}$ |      $10\%$      |
| pebibyte |     $\text{PiB}$     | $2^{50}$ |      $13\%$      |
