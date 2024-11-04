---
layout: post
title: 中央处理器（CPU）
date: 2024-04-16 18:13:29
updated: 2024-05-30 17:29:03
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 概述

主要组成部分：
- 控制信号
- 数据通路

- 控制信号
    - 由控制器生成，负责
        - 程序控制:  程序中指令执行顺序控制
        - 操作控制:  将机器指令翻译成执行部件所需操作控制信号
        - 时序控制:  控制操作信号的产生时间、持续时间
        - 异常控制:  异常处理，外设交互
    - 控制器将机器指令译码并生成指令的执行部件所需的控制信号，控制信号按序送至各执行部件控点，引起逻辑门开闭，建立正确的数据通路，从而完成指令功能
    - 控制信号可以由软件或硬件实现（微程序控制器、硬布线控制器）
- 数据通路
    - 运算部件
    - 存储部件

CPU 中主要寄存器类型：
- PC(Program Counter)：指令计数器
- IR(Instruction Register)：指令寄存器
- AR(Address Register)：地址寄存器
- DR(Data Register)：数据缓冲寄存器
- AC(Accumulator)：累加寄存器
- PSW(Program Status Word)：程序状态字
    - EFLAGS in x86, MIPS 中无

数据通路的寄存器传输表示（RTL, ~~Right To Left~~ Register Transfer Level）。

<style>
@media (prefers-color-scheme: dark) {
    img[src$='#invert'] {
        -webkit-filter: invert(1) hue-rotate(180deg);
        filter: invert(1) hue-rotate(180deg);
        mix-blend-mode: screen;
    }
}
</style>

![](06-cpu/rtl.png#invert)

- 时钟触发前输入须稳定一段*建立时间*（Setup Time）
- 时钟触发后输出需稳定一段*保持时间*（Hold Time）
- 时钟触发到输出稳定的时间*触发器延迟*（Clock-to-Q Delay, Clk_to_Q）

![](06-cpu/rtl-timing.png#invert)

![](06-cpu/min-clock-period.png#invert)

单总线 CPU 示例
- 主要部件都连接在总线上
- 各部件间通过总线传递数据和控制信号

![](06-cpu/single-bus-cpu.png#invert)

| 控制信号 | 作用说明 |
| :-: | :- |
| $\mathrm{IR_{out}, PC_{out}, \cdots, R 1_{out}}$ | 控制三态门将寄存器值输出到总线 |
| $\mathrm{IR_{in}, PC_{in}, \cdots, R 1_{in}}$ | 控制寄存器使能端将总线数据锁存（时钟驱动） |
| $\mathrm{+1, ADD, SUB}$ | 运算控制信号 |
| $\mathrm{Write, Read}$ | 内存读写控制信号（时钟驱动） |

图中 ID 即为 Instruction Decoder，指令译码器。

## MIPS32 单总线 CPU

指令执行一般流程：取指令、执行指令反复循环。

![](06-cpu/instruction-execution.png#invert)

- 时钟周期（节拍脉冲/震荡周期）：完成一次简单的操作的时间
- 机器周期（CPU 周期）：完成一次较为复杂的操作的时间
- 指令周期：从主存取一条指令并执行的时间

![](06-cpu/period.png#invert)

- 定长指令周期：同步控制
    - 机器周期数固定，节拍数固定，按机器周期同步， MIPS 单周期 CPU
- 变长指令周期：异步控制
    - 机器周期数可变，节拍数可变，按时钟周期同步， MIPS 多周期 CPU

!!! memo ""
    指令周期数据通路原理图不记了，听天书……

> 中间省略较多天书

## CPU 性能评价

CPI(Cycles Per Instruction) 是 CPU 性能评价的一个重要指标，它表示完成一条指令所需的时钟周期数。

对于单周期处理器，CPI = 1。

CPI 越小，CPU 性能越好。

计算机的性能除 CPI 外，还取决于时钟周期的宽度。单周期处理器的时钟宽度为*最复杂指令的执行时间*。

- 对于某一条特定的指令而言，其 CPI 是一个确定的值
- 对于某一个程序或一台机器而言，其 CPI 是一个平均值，表示该程序或该机器指令集中每条指令执行时<u>平均</u>需要多少时钟周期

两种性能评价方式：
- 执行任务需要的时间
    - 响应时间（Response Time）：从任务提交到任务完成所经历的时间
    - 执行时间（Execution Time）：CPU 执行任务所需的时间
    - 等待时间/时延（Latency）：任务在系统中等待的时间
- 一段时间内能够执行的任务数量
    - 吞吐量（Throughput）：单位时间内完成的任务数量
    - 带宽（Bandwidth）：单位时间内传输的数据量
