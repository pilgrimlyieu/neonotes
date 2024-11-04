---
layout: post
title: 编程语言概述
date: 2024-02-27 07:40:46
updated: 2024-03-04 12:38:20
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 编程语言概述

**计算机语言** ≠ **编程语言**。如 markdown, HTML, XML 等是标记语言，不是编程语言。

- 命令式（Imperative）
    - 过程式（Procedure）
    - 面向对象（Object-Oriented）
- 声明式（Declarative）
    - 函数式（Functional）
    - 逻辑式（Logic）

### 命令式编程

- How: 具体指明程序要做哪些步骤，一般支持如下几种语句：
    1. 运算语句
    2. 循环
    3. 条件分支
    4. 无条件分支（`goto` in C）

#### 面向对象

- 目标：程序更加模块化和可维护

### 声明式编程

- What: 表达想要计算的逻辑，而不需要给出具体步骤。

#### 函数式

命令式（C）

```c
int factorial(int n) {
    int f = 1;
    for (; n > 0; n--) {
        f *= n;
    }
    return f;
}
```

函数式（Lisp）

```lisp
(define (factorial n)
  (if (= n 0)
      1
      (* n (factorial (- n 1)))))
```

#### 逻辑式

证明即程序（Curry-Howard isomorphism）。

Prolog

```prolog
// 0! = 1
factorial(0, 1).
// N! = F <== (N-1)! = G, F = N * G
factorial(N, F) :- M is N - 1, factorial(M, G), F is N * G.
```

### 实现方式

- **编译**（Compiling）：把整个程序源代码翻译成另一种代码（机器码），然后等待被执行，发生在运行之前，产物是「另一份代码」。
- **解释**（Interpretation）：把程序源代码一行一行翻译然后执行，发生在运行时，产物是「执行结果」。
