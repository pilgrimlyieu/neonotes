---
layout: post
title: 引入
date: 2024-09-06 14:38:39
updated: 2024-09-06 14:38:39
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

!!! tip ""
    课件用的是英文，因此复制过来的部分大部分保留英文。而我英文不好，表达不清意思，因此自己写的部分大部分还是沿用中文。

## Introduction

In computer science, an **algorithm** is any *well-defined* computational <u>procedure</u> that takes some value(s) as *input* and produces some value(s) as *output*.

A particular input of a problem is an **instance** of that problem.

A **data structure** is a way to <u>store and organize data</u> in order to facilitate *access* and *modifications*.

## Pseudocode

We'll typically describe algorithms as procedures written in a **pseudocode**(伪代码).
- Independent of specific c languages, but uses structural conventions of a normal programming language (like C, Java, C++)
- Intended for human reading rather than machine reading (omit nonessential details and easier to understand)

Some conventions:
- Give a *valid name* for the pseudocode procedure, specify the *input* and *output* variables' *names* (as well as the *types*) at the beginning.
- Use proper Indentation for every statement in a block structure.
- For a flow control statements use **if-else**. Always end an **if** statement with an **end-if**. Both **if**, **else** and **end-if** should be aligned vertically in same line.
- Use `<-` or `:=` operator for assignment statements, Use `=` for equality check.
- Array elements can be represented by specifying the array name followed by the index in square brackets. For example, `A[i]` indicates the $i$-th element of the array `A`.
- For looping or iteration use **for** or **while** statements. Always end a **for** loop with **end-for** and a **while** with **end-while**.

### Integer Multiplication

An example of the Grade-School Algorithm for Multiplication of two numbers:

```pseudo
Procedure GradeMult(x, y)
In: two n-bit positive integers x, y
Out: the product p := x * y

A := split x into an array of its digits // e.g., 1235 -> [1, 2, 3, 5]
B := split y into an array of its digits
product := [1...2n]
for i := 1 to n:
    carry := 0
    for j := 1 to n:
        temp := product[i + j - 1] + carry + A[i] * B[j] 
        carry := temp / 10
        product[i + j - 1] := temp mod 10
    end for
    product[i + n] := carry
end for
p := concatenate product into a single number
return p
```

- at most $n^2$ multiplications
- at most $n^2$ additions (for carries)
- add $n$ different $2n$-digit numbers ($2n^2$ additions)

At most $4n^2$ single digit operations.

### Recursion

使用递归的方法可以减少乘法的次数。

将 $n$ 位数 $x, y$ 分为两部分（无法均分则补 $0$）：

$$
\left\lbrace\begin{aligned}
    x &= 10^{n/2}a + b \\
    y &= 10^{n/2}c + d
\end{aligned}\right.
$$

于是

$$
\begin{aligned}
    x \times y &= (10^{n/2}a + b) \times (10^{n/2}c + d) \\
    &= 10^n \times (a \times c) + 10^{n/2} \times (a \times d + b \times c) + b \times d
\end{aligned}
$$

因此可以用四个更小的乘法来计算 $x \times y$。

### Karatsuba Algorithm

我们可以在没有 $a \times c$ 与 $b \times d$ 的情况下得到 $a \times d + b \times c$。

注意到

$$
a \times d + b \times c = (a + b) \times (c + d) - a \times c - b \times d
$$

只需计算 $(a + b) \times (c + d)$，因此就比上面的方法少了一次乘法。

### Schönhage-Strassen Algorithm\*

Convolution(卷积) of $[1, 2, 3]$ and $[3, 2, 1]$:

|     | $1$ | $2$ | $3$ |
| :-: | :-: | :-: | :-: |
| $3$ | $3$ | $6$ | $9$ |
| $2$ | $2$ | $4$ | $6$ |
| $1$ | $1$ | $2$ | $3$ |

可以看作是多项式相乘 $(x^2 + 2x + 3)(3x^2 + 2x + 1)$，然后求系数。

系数可以通过反对角线求和得到。

Schönhage-Strassen 算法：
- 给出 $A = (a_1, a_2, \cdots, a_n),\, B = (b_1, b_2, \cdots, b_n)$，要求得 $A$ 与 $B$ 的卷积 $C = (c_1, c_2, \cdots, c_{2n-1})$；
- 令 $h(x) = c_{2n-1} + c_{2n-2}x + \cdots + c_1x^{2n-2}$；
- 取样 $2n-1$ 个点，得到 $c_1, \cdots, c_{2n-1}$，从而可以通过解线性方程得到 $h(x)$；
- 若取样点是一组复数（$n$ 次单位根），线性方程可以通过*快速傅立叶*（Fast Fourier Transform, FFT）很快地解决。
