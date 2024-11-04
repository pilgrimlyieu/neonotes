---
layout: post
title: 指令集体系
date: 2024-04-02 18:28:11
updated: 2024-05-30 17:28:28
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 概述

**指令集架构**（Instruction Set Architecture, ISA）
- IA-32(x86)
- MIPS
- RISC-V

**中央处理器**（Central Processing Unit, CPU）
- IA-32 架构（CISC）
- MIPS 架构（RISC）
- RISC-V 架构（RISC）
- ARM 架构（RISC）

指令集体系
- 某台计算机能够执行的机器指令的集合
- 计算机能够执行的操作和每一步操作涉及的数据
    - 运算部件
    - 寄存器、存储器
- 明确了在这台机器上编写软件时所要注意的全部信息
- 规定了程序员使用机器语言编程时的全部信息
- 将高级语言编写的程序翻译为机器语言时，ISA 也为翻译器提供了关于该计算机的信息
- ISA 规定了存储器的组织，寄存器集和指令集，包括操作码，数据类型和寻址模式等

**寄存器**（Register）
- 机器语言和汇编语言不能使用各种类型的变量
- 寄存器变量<u>没有数据类型</u>
- 机器语言和汇编语言的操作对象是*寄存器*
- 好处：寄存器是最快的数据存取单元
- 缺陷：寄存器数量有限，需仔细高效的使用
- MIPS 包括 32 个通用寄存器，字长 32 位，即 $\pu{1 word} = \pu{32 bits} = \pu{4 bytes}$

MIPS 寄存器
- 32 个 32 位通用寄存器 \$0~\$31
- 32 个 32 位单精度浮点寄存器 \$f0~\$f31
- 2 个 32 位乘、商寄存器 Hi 和 Lo
- 1 个程序寄存器 PC
- 无程序状态寄存器

| 通用寄存器 | 助记符    | 释义                           |
| :--------: | :----:    | :---                           |
| 0          | \$zero    | 固定值为 0，硬件置位           |
| 1          | \$at      | 汇编器保留，临时变量           |
| 2~3        | \$v0~\$v1 | 函数调用返回值                 |
| 4~7        | \$a0~\$a3 | 函数调用参数                   |
| 8~15       | \$t0~\$t7 | 暂存寄存器，被调用者按需保存   |
| 16~23      | \$s0~\$s7 | 保存寄存器，调用者保存         |
| 24~25      | \$t8~\$t9 | 暂存寄存器，同上               |
| 26~27      | \$k0~\$k1 | 操作系统保留，中断异常处理     |
| 28         | \$gp      | 全局指针（Global Pointer）     |
| 29         | \$sp      | 栈指针（Stack Pointer）        |
| 30         | \$fp      | 帧指针（Frame Pointer）        |
| 31         | \$ra      | 函数返回地址（Return Address） |

RISV-V 整型寄存器
| Register name | Symbolic name | Description                         | Saved by |
| :-----------: | :-----------: | :----------                         | :------- |
| x0            | Zero          | Always zero                         | -        |
| x1            | ra            | Return address                      | Caller   |
| x2            | sp            | Stack pointer                       | Callee   |
| x3            | gp            | Global pointer                      | -        |
| x4            | tp            | Thread pointer                      | -        |
| x5            | t0            | Temporary/alternate return register | Caller   |
| x6~x7         | t1~t2         | Temporary                           | Caller   |
| x8            | s0/fp         | Saved register/frame pointer        | Callee   |
| x9            | s1            | Saved register                      | Callee   |
| x10~x11       | a0~a1         | Function argument/return value      | Caller   |
| x12~x17       | a2~a7         | Function argument                   | Caller   |
| x18~x27       | s2~s11        | Saved register                      | Callee   |
| x28~x31       | t3~t6         | Temporary                           | Caller   |

寄存器数据存储
- 字长：32 位，4 字节
- 5 位编码识别
- 左边字节称为*高字节*
- 右边字节称为*低字节*
- **大端**（Big Endian）：高位优先
- **小端**（Little Endian）：低位优先
- 存储在每个寄存器中的位数通常是 1 个字（即 32 位）

浮点寄存器
- 用于单精度或双精度计算
- 5 位编码识别
- 单精度浮点数使用 1 个寄存器
- 双精度浮点数使用 2 个寄存器

## MIPS 指令

### 加减法运算

```c
a = b + c;
d = e - f;
```

对应的 MIPS 汇编指令（a, b, c 对应寄存器 \$s0, \$s1, \$s2；d, e, f 对应寄存器 \$s3, \$s4, \$s5）

```assembly
add $s0, $s1, $s2
sub $s3, $s4, $s5
```

另一个例子

```c
a = b + c + d - e;
```

对应的 MIPS 汇编指令

```assembly
add $t0, $s1, $s2   # temp = b    + c
add $t0, $t0, $s3   # temp = temp + d
sub $s0, $t0, $s4   # a    = temp - e
```

和常数相加，如

```c
g += 4; // 4 在内存中
```

对应的 MIPS 汇编指令

```assembly
lw  $t0, 0($s3)    # $s3 = Address(4)
add $s0, $s0, $t0   # g   = g + temp
```

上面的 `0($s3)` 中，`0` 是*偏移量*，`$s3` 是*基址寄存器*。

```c
g += 4; // 4 在指令中
```

对应的 MIPS 汇编指令（加**立即数**，i 即 **i**mmediate）

```assembly
addi $s0, $s0, 4   # g = g + 4
```

### 内存数据访问

```c
g = h + A[8];
```

对应的 MIPS 汇编指令

```assembly
lw  $t0, 32($s3)    # $s3 = Address(A[0])
add $s0, $s1, $t0   # g   = h + A[8]
```

变址寻址：基址寄存器 + 地址偏移量

上面的例子中，$\pu{32 byte} = 8 \times \pu{4 byte}$，因为一个字长为 4 字节。

写内存

```c
A[12] = h + A[8];
```

对应的 MIPS 汇编指令

```assembly
lw  $t0, 32($s3)    # $s3 = Address(A[0])
add $t0, $s2, $t0   # temp = h + A[8]
sw  $t0, 48($s3)    # A[12] = temp
```

### 条件判断

```c
if (a == b) {
    i = 1;
} else {
    i = 2;
}
```

等效 C 代码

```c
if (a == b) goto L1;
i = 2;
goto L2;
L1: i = 1;
L2:
```

等效 MIPS 汇编指令（beq 即 **b**ranch if **eq**ual，j 即 **j**ump）

```assembly
    beq  $s0, $s1, L1
    addi $s3, $zero, 2
    j    L2
L1: addi $s3, $zero, 1
L2:
```

!!! info 跳转
    条件跳转

    ```assembly
    beq reg1, reg2, label
    bne reg1, reg2, label
    ```
    
    无条件跳转

    ```assembly
    j label
    ```

### 指令集

**指令**：
- 操作码（Opcode）：指令的类型
- 操作数（Operand）：指令的参数

指令集是由一组操作码、操作数和寻址模式定义的指令集合。

寻址模式决定了如何计算将要读取/存储的存储单元的地址。

- CISC（Complex Instruction Set Computer）：复杂指令集计算机
    - 指令系统复杂：变长操作码/变长指令字/指令多/寻址方式多/指令格式多
    - 指令周期长：绝大多数指令需要多个时钟周期才能完成
    - 各种指令都能访问存储器：除了专门的存储器读写指令外，运算指令也能访问存储器
    - 采用微程序控制
    - 有专用寄存器
    - 难以进行编译优化来生成高效目标代码
- RISC（Reduced Instruction Set Computer）：精简指令集计算机
    - 简化的指令系统：指令少/寻址方式少/指令格式少/指令长度一致
    - 以 RR（register-to-register）方式工作：除 Load/Store 指令
可访问存储器外，其余指令都只访问寄存器
    - 指令周期短：以流水线方式工作， 因而除 Load/Store 指令外，其他简单指令都只需一个或一个不到的时钟周期就可完成
    - 采用大量通用寄存器，以减少访存次数
    - 采用组合逻辑电路控制，不用或少用微程序控制
    - 采用优化的编译系统，力求有效地支持高级语言程序

### 指令分类

表示一条指令的机器字，称为**指令字**，简称**指令**。

- 按计算机系统的层次结构分类
    - 微指令
    - 机器指令
    - 宏指令
- 按操作数物理位置分类
    - 存储器－存储器（SS）型
    - 寄存器－寄存器（RR）型
    - 寄存器－存储器（RS）型
- 按指令长度分类
    - 定长指令
    - 变长指令
- 按操作数个数分类
    - 四操作数
    - 三操作数
    - 二操作数
    - 单操作数
    - 零操作数
- 按指令功能分类

指令长度：指令中包含二进制代码的位数。

- 指令字越长，地址码长度越长，可直接寻址空间越大
- 指令字越长，占用空间越大，取指令越慢

### 指令寻址方式

- 指令寻址
    - 顺序寻址
    - 跳转寻址
- 操作数寻址
    - 立即寻址
    - 寄存器寻址
    - 间接寻址
    - 基址/变址寻址

#### 指令寻址

- 顺序寻址
    - 程序对应的机器指令序列按先后顺序依次存放
    - 程序执行时从第一条指令开始，逐条取出并顺序依次执行
- 跳转寻址
    - 当程序中出现分支或循环时，就会改变程序的执行顺序
    - 下条指令的地址由指令本身给出

#### 操作数寻址

- 立即寻址：操作数字段是操作数本身。

例如 `MOV $s0, 38H`（将立即数 38H 移动到寄存器 \$s0）

<style>
@media (prefers-color-scheme: dark) {
    img[src$='#invert'] {
        -webkit-filter: invert(1);
        filter: invert(1) hue-rotate(180deg);
        mix-blend-mode: screen;
    }
}
</style>

![](05-instruction-set-architecture/addressing-mode-1.png#invert)

- 寄存器寻址：操作数在 CPU 的内部寄存器中。

例如 `PUSH $s0`（将寄存器 \$s0 的内容压入栈）

![](05-instruction-set-architecture/addressing-mode-2.png#invert)

### MIPS 指令集

- 指令格式
    - R 型指令
    - I 型指令
    - J 型指令
- 无寻址方式，隐藏在了操作码字段 OP 中

R-Type 指令格式（Register）
- op: 操作码
- rs: 源寄存器
- rt: 目的寄存器
- rd: 目的寄存器
- shamt: 移位量
- funct: 功能码

![](05-instruction-set-architecture/mips-r-type.png#invert)

I-Type 指令格式（Immediate）
- op: 操作码
- rs: 源寄存器
- rt: 目的寄存器
- immediate: 立即数

![](05-instruction-set-architecture/mips-i-type.png#invert)

J-Type 指令格式（Jump）
- op: 操作码
- target address: 目标地址（立即数）

![](05-instruction-set-architecture/mips-j-type.png#invert)

#### R-Type 指令

##### ADD

| op(10) | rs  | rt  | rd  | shamt | funct(10) |
|  :-:   | :-: | :-: | :-: |  :-:  |    :-:    |
|   0    | Reg | Reg | Reg |   0   |    32     |

```assembly
ADD rd, rs, rt
```

即 `GPR[rd] <- GPR[rs] + GPR[rt]`[^gpr]。

[^gpr]: GPR 为通用寄存器（**G**eneral **P**urpose **R**egister）。

##### SUB

| op(10) | rs  | rt  | rd  | shamt | funct(10) |
|  :-:   | :-: | :-: | :-: |  :-:  |    :-:    |
|   0    | Reg | Reg | Reg |   0   |    34     |

```assembly
SUB rd, rs, rt
```

即 `GPR[rd] <- GPR[rs] - GPR[rt]`。

##### AND

| op(10) | rs  | rt  | rd  | shamt | funct(10) |
|  :-:   | :-: | :-: | :-: |  :-:  |    :-:    |
|   0    | Reg | Reg | Reg |   0   |    36     |

```assembly
AND rd, rs, rt
```

即 `GPR[rd] <- GPR[rs] and GPR[rt]`。

##### OR

| op(10) | rs  | rt  | rd  | shamt | funct(10) |
|  :-:   | :-: | :-: | :-: |  :-:  |    :-:    |
|   0    | Reg | Reg | Reg |   0   |    37     |

```assembly
OR rd, rs, rt
```

即 `GPR[rd] <- GPR[rs] or GPR[rt]`。

##### SLL(Shift Left Logical)

即**逻辑左移**。

| op(10) | rs  | rt  | rd  | shamt | funct(10) |
|  :-:   | :-: | :-: | :-: |  :-:  |    :-:    |
|   0    |  0  | Reg | Reg |   X   |     0     |

```assembly
SLL rd, rt, shamt
```

即 `GPR[rd] <- GPR[rt] << shamt`。

#### SLT(Set on Less Than)

| op(10) | rs  | rt  | rd  | shamt | funct(10) |
|  :-:   | :-: | :-: | :-: |  :-:  |    :-:    |
|   0    | Reg | Reg | Reg |   0   |    42     |

```assembly
SLT rd, rs, rt
```

即 `GPR[rd] <- (GPR[rs] < GPR[rt])`。若 `GPR[rs] < GPR[rt]`，则 `GPR[rd]` 被置为 1，否则置为 0。

#### JR(Jump Register)

| op(10) | rs  | rt  | rd  | shamt | funct(10) |
|  :-:   | :-: | :-: | :-: |  :-:  |    :-:    |
|   0    | Reg |  0  |  0  |   0   |    9      |

```assembly
JR rs
```

即 `PC <- GPR[rs]`[^pc]。

[^pc]: PC 为程序计数器（**P**rogram **C**ounter）。

程序设计中 rs 应使用除了 31(\$ra) 以外的寄存器。

### I-Type 指令

#### ADDI

| op(10) | rs  | rt  |   immediate   |
|  :-:   | :-: | :-: |      :-:      |
|   8    | Reg | Reg | 16bits 立即数 |

```assembly
ADDI rt, rs, immediate
```

即 `GPR[rt] <- GPR[rs] + immediate`。`immediate` 为*有符号数*。

当结果的二进制补码发生溢出时，rt 不会被修改，结果被丢弃。

> v6 中舍弃了 `ADDI` 指令，使用 `ADDIU` 代替，因为二者在不溢出时行为相同。

#### ANDI

| op(10) | rs  | rt  |   immediate   |
|  :-:   | :-: | :-: |      :-:      |
|   12   | Reg | Reg | 16bits 立即数 |

```assembly
ANDI rt, rs, immediate
```

即 `GPR[rt] <- GPR[rs] and ZeroExtend(immediate)`。`immediate` 被零扩展为 32 位。

#### SLTI

| op(10) | rs  | rt  |   immediate   |
|  :-:   | :-: | :-: |      :-:      |
|   10   | Reg | Reg | 16bits 立即数 |

```assembly
SLTI rt, rs, immediate
```

即 `GPR[rt] <- (GPR[rs] < SignExtend(immediate))`。`immediate` 被符号扩展为 32 位。

#### LW(Load Word)

| op(10) | rs  | rt  |   immediate   |
|  :-:   | :-: | :-: |      :-:      |
|   35   | Reg | Reg | 16bits 立即数 |

```assembly
LW rt, immediate(rs)
```

即 `GPR[rt] <- Memory[GPR[rs] + SignExtend(immediate)]`。将主存（Memory）中 32 位的字取到寄存器 rt 中。

地址由 `GPR[rs] + offset` 确定，rs 寄存器中的值为基址，immediate 16 位立即数为*有符号*偏移量，相加后给出有效地址。

#### LH(Load Halfword)

| op(10) | rs  | rt  |   immediate   |
|  :-:   | :-: | :-: |      :-:      |
|   33   | Reg | Reg | 16bits 立即数 |

```assembly
LH rt, immediate(rs)
```

即 `GPR[rt] <- SignExtend(Memory[GPR[rs] + SignExtend(immediate)])`。将主存中 16 位的半字取到寄存器 rt 中。

#### LUI(Load Upper Immediate)

| op(10) | rs  | rt  |   immediate   |
|  :-:   | :-: | :-: |      :-:      |
|   31   |  0  | Reg | 16bits 立即数 |

```assembly
LUI rt, immediate
```

即 `GPR[rt] <- immediate << 0(16)`。将 16 位立即数取到寄存器 rt 的高 16 位半字中。

实际操作中，是将 16 位立即数左移 16 位，再与 16 个低位的 0 拼接，将拼接后的 32 位数存入寄存器 rt 中。

#### SW(Store Word)

| op(10) | rs  | rt  |   immediate   |
|  :-:   | :-: | :-: |      :-:      |
|   43   | Reg | Reg | 16bits 立即数 |

```assembly
SW rt, immediate(rs)
```

即 `Memory[GPR[rs] + SignExtend(immediate)] <- GPR[rt]`。将寄存器 rt 中低 32 位的字存入主存中。

#### BEQ(Branch on Equal)

| op(10) | rs  | rt  |   immediate   |
|  :-:   | :-: | :-: |      :-:      |
|   4    | Reg | Reg | 16bits 立即数 |

```assembly
BEQ rs, rt, immediate
```

即 `if GPR[rs] == GPR[rt] then branch`。如果寄存器 rs 和 rt 中的值相等，则发生跳转。

跳转地址为 `PC + 4 + (SignExtend(immediate) << 2)`。

则 `BEQ r0, r0, immediate` 为无条件跳转。

使用这样的方式，branch 就为 `PC + 4 * (immediate + 1)`。

#### BNE(Branch on Not Equal)

| op(10) | rs  | rt  |   immediate   |
|  :-:   | :-: | :-: |      :-:      |
|   5    | Reg | Reg | 16bits 立即数 |

```assembly
BNE rs, rt, immediate
```

即 `if GPR[rs] != GPR[rt] then branch`。如果寄存器 rs 和 rt 中的值不相等，则发生跳转。

### J-Type 指令

#### J(Jump)

| op(10) | target address |
|  :-:   |      :-:       |
|   2    | 26bits 立即数  |

```assembly
J target
```

即 `PC <- PC[31:28] || target || 00`。

跳转地址为，26bits 立即数左移两位，与 PC 的高四位拼接。

#### JAL(Jump and Link)

| op(10) | target address |
|  :-:   |      :-:       |
|   3    | 26bits 立即数  |

```assembly
JAL target
```

即 `GPR[31] <- PC + 4` 与 `PC <- PC[31:28] || target || 00`。

将返回地址存入 31(\$ra) 寄存器，再跳转。

### RISC-V 指令集

略。
