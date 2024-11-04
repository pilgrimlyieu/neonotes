---
layout: post
title: 算法分析基础
date: 2024-09-13 13:54:36
updated: 2024-09-13 16:27:36
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## Correctness of Algorithms

### Definition

When we talk about the **correctness** of an algorithm, we actually mean <u>the correctness with respect to its specification</u>.

Specification expresses the task to be done by the algorithm, which consists of:
- (optional) name of algorithm and list of its arguments
- **Precondition** (or initial condition): it species what is correct input data to the
problem
- **Postcondition** (or final condition): it species what is the desired result of the algorithm)

Example:
- name: $Sort(A)$
- input: An array $A$ of $n$ integers
- output: A permutation of that array $A$ that is sorted (monotonic).

!!! info Total correctness(完全正确性)
    An algorithm is called *totally correct* for the given specification if and only if for <u>any correct input data</u> it:
    1. terminates
    2. returns correct output

Usually, while checking the correctness of an algorithm it is easier to separately:
- Check whether the algorithm stops
- Then checking the remaining part — This remaining part of correctness is called "Partial Correctness" of algorithm

!!! info Partial correctness(部分正确性)
    An algorithm is called *partially correct* if satisfies the following condition: If the algorithm receiving correct input data stops then its result is correct.

    > Note: Partial correctness does not make the algorithm stop.

!!! example ""
    Total correctness:
    - precondition: $x = 1$
    - algorithm: $y \coloneqq x$
    - postcondition: $y = 1$

    ---

    Partial correctness:
    - precondition: $x = 1$
    - algorithm:
    ```python
    while (true)
        x := 0
    ```
    - postcondition: $y = 1$

    ---

    Neither partial nor total correctness:
    - precondition: $x = 1$
    - algorithm: $y \coloneqq x$
    - postcondition: $y = 2$

### The proof of total correctness

A proof of total correctness of an algorithm usually assumes 2 separate steps
1. (to prove that) the algorithm always **terminate** for correct input data
2. (to prove that) the algorithm is **partially correct**.

Different proof methods for them, typically
- **Variants**(变式) for "termination"
- **Invariants**(不变式) for "partial correctness"

> Termination is often much easier to prove.

#### Example: Insertion-Sort

```python
# Procedure: Insertion-Sort(A)
# In: An arrat A of n integers
# Out: A permutation of that array A that is sorted (monotonic)

for i := 2 to A.length
    key := A[i]
    # Insert A[i] into the sorted sequence A[1:i-1]
    j := i - 1
    while j > 0 and A[j] > key
        A[j + 1] := A[j]
        j := j - 1
    A[j + 1] := key
return A
```

Proof the correctness of Insertion-Sort:
1. The algorithm outputs correct result on every instance (partially correct).
2. The algorithm terminates within finite steps on every instance (termination).

##### Step 1: Using loop *invariant* for partial correctness

General rules for loop invariant proofs:
- **Initialization**: It is true prior to the first iteration of the loop.
- **Maintenance**: If it is true before an iteration of the loop, it remains true before the next iteration.
- **Termination**: When the loop terminates, the invariant gives us a useful property that helps show that the algorithm is correct.

The loop invariant of the outer `for` loop: By the end of $i$-th iteration, the elements in subarray `A[1:i]` are sorted order.
- *Initialization*: prior the first iteration(`i=2`): `A[1]` is in sorted order.
- *Maintenance*: Assume by the end of the $i$-th iteration, the elements in subarray `A[1:i]` are in sorted order; then by the end of the $(i+1)$-th iteration, the elements in subarray `A[1:i+1]` are in sorted order.
- *Termination*: After the iteration `i=n`, the loop invariant states that `A` is sorted.

Let the loop invariant mentioned above as $IV_1$. Is there only one loop invariant? The answer is NO!

Here is another loop invariant: By the end of the $i$-th iteration, subarray `A[1:i]` retains all of the original elements in `A[1:i]` in previous iteration. Let this be $IV_2$.

$IV_2$ is weaker than $IV_1$! Since there are more possible `A[1:i]` that satisfy $IV_2$ but not satisfy $IV_1$.

A good (strong) loop invariant must satisfy these three properties *Initialization*, *Maintenance* and *Termination*. Note that $IV_2$ does not satisfy *Termination* property.

!!! note How to find the loop invariant?
    Generally, the answer is: **We don't know**.

    For simple ones, there exists effective techniques.

##### Step 2: Using *variant* for termination

Using loop variant to prove the termination:
- show that some quantity *strictly* decreases.
- it cannot decrease indefinitely (Bounded!)

!!! info Well-ordered set(良序集)
    An ordered set is **well-ordered**(良序) if each and every nonempty subset has a smallest or least element.

「良序」的更多内容见[离散数学笔记](/notes/D-discrete-mathematics/12-partial-order-set#良序)。

A well-ordered set has **no infinite descending** sequences, which can be used to ensure the termination of algorithm.

Loop variant for the inner `while` loop: $j$. For each iteration, $j$ strictly decreases. $j$ is bounded to be larger than $0$.

Loop variant for the outer `for` loop: `A.length - i`. For each iteration, `A.length - i` strictly decreases. `A.length - i` is bounded to be larger than $0$.

!!! note How to find the loop variant?
    Again, generally, the answer is: **We don't know**.

    However, generally speaking, it is very easy to identify. For example, the induction variable of the loop (or some linear transformation of it).

Some other strategies of correctness proof: proof by cases, proof by contrapposition, proof by contraction, etc.

When loops and/or recursions are involved: often (if not always) use mathematical induction.

## Efficiency of Algorithms

### Complexity

!!! info ""
    - **Time complexity**: how much time is needed before halting
    - **Space complexity**: how much memory (usually *excluding* input) is required for successful executed

    Other performance measures:
    - communication bandwidth(通信带宽)
    - energy consumption
    - ...

    > Time complexity is typically more important than others in analysis.

An observation: <u>larger inputs often demands more time</u>. Therefore, Cost of an algorithm should be a function of *input size*, say, $T(n)$.

Given an algorithm and an input, when counting the cost with respect to the RAM model:
- Each <u>memory access</u> takes *constant time*.
- Each <u>"primitive" operation</u> takes *constant time*.
- Compound operations should be decomposed.
- At last, Counting up the number of time units.

Time complexity of Insertion Sort

```python
                                # Cost   # Times
                                # ----   # -----
for i := 2 to A.length          # c1     # n
    key := A[i]                 # c2     # n - 1
    j := i - 1                  # c3     # n - 1
    while j > 0 and A[j] > key  # c4     # sum(t_i), i=2 to n
        A[j + 1] := A[j]        # c5     # sum(t_i - 1), i=2 to n
        j := j - 1              # c6     # sum(t_i - 1), i=2 to n
    A[j + 1] := key             # c7     # n - 1
return A
```

The total cost of the algorithm is

$$
T(n) = c_1n + c_2(n-1) + c_3(n-1) + c_4\sum_{i=2}^{n}t_i + c_5\sum_{i=2}^{n}(t_i-1) + c_6\sum_{i=2}^{n}(t_i-1) + c_7(n-1)
$$

$t_i$ depends on *which* input of size $n$.

The time cost of insert sort varies among inputs. How to fairly evaluate a algorithm?

Enumerate the cost of all the possible inputs? Not possible, since the input space is infinite! We can check the representative inputs, but, what are they?

!!! info Worst, Best and Average case
    - **Worst-case time complexity**: the maximum time cost among all possible inputs of size $n$.
        - $W(n) = \max\limits_{x \in \mathscr{X}_n} T(x)$
    - **Best-case time complexity**: the minimum time cost among all possible inputs of size $n$.
        - $B(n) = \min\limits_{x \in \mathscr{X}_n} T(x)$
    - **Average-case time complexity**: the average time cost among all possible inputs of size $n$.
        - $A(n) = \sum\limits_{x \in \mathscr{X}_n} \Pr(x)T(x) = \mathbb{E}[T(x)]$

    > Note: need assumption of statistics distribution of inputs.

We mainly focus on **worst-case** time complexity.

Exceptions: Some exponential-time algorithms are used widely in practice because the worst-case instances don't arise.

#### Best-case time complexity

Each time $t_i$ is $1$, which means that each time the while loop condition is false at the beginning! Which means that the array is already sorted at the beginning!

$$
B(n) = c_1n + c_2(n-1) + c_3(n-1) + c_4(n-1) + c_7(n-1) = (c_1 + c_2 + c_3 + c_4 + c_7)n - (c_2 + c_3 + c_4 + c_7)
$$

#### Worst-case time complexity

Each time $t_i$ is the largest it can be, which means that each time the while loop condition is true until $j$ is equal to $0$. `A[j] > key` is true every time, which means that the array is reversely sorted at the beginning! So $t_i = i$ every time.

$$
\begin{aligned}
    W(n) &= c_1n + c_2(n-1) + c_3(n-1) + c_4\sum_{i=2}^{n}i + c_5\sum_{i=2}^{n}(i-1) + c_6\sum_{i=2}^{n}(i-1) + c_7(n-1) \\
    &= \dfrac{c_4+c_5+c_6}{2}n^2 + \left(c_1+c_2+c_3+c_7-\dfrac{c_4+c_5+c_6}{2}\right)n - (c_2+c_3+c_4+c_7)
\end{aligned}
$$

#### Average-case time complexity

What about the average case? The elements in the input array are randomly ordered.

Hint: the number of swaps equals the number of inversions!

相当于求随机列表中反序对的期望值，为 $\dbinom{n}{2}\mathbb{E}(I) = \dfrac{1}{2}\dbinom{n}{2}$

## Asymptotic order of growth

### Big $O$ notation

In practice, we usually don't care about the unimportant details in the counted operations.

We need one more simplifying abstraction, which can give us an intuitive feeling of the cost of an algorithm.

The abstractions is: the rate of growth, or order of growth, of the running time that really interests us, therefore, two factors are ignored:
- Constant coefficients are not that important (when $n$ is large)
- Lower-order terms are not that important (when $n$ is large).

!!! info Big $O$ notation(大 $O$ 符号)
    Given a function $g(n)$, we denote by $O(g(n))$ the following set of functions:

    $$
    O(g(n)) = \left\lbrace f(n) \mid \exists c > 0,\, \exists n_0 > 0,\, \forall n \ge n_0\colon 0 \le f(n) \le c \cdot g(n) \right\rbrace
    $$

    **Asymptotic upper bounds**(渐近上界): when we say $f(n)$ is $O(g(n))$, we mean that $f(n)$ grows no faster than a certain rate (is asymptotically at most $g(n)$).

$O(g(n))$ is actually a set of functions, but computer scientists often write $f(n) = O(g(n))$ instead of $f(n) \in O(g(n))$.

Consider $f_1(n) = 5n^3,\, f_2(n) = 3n^2$, we have $f_1(n) = O(n^3),\, f_2(n) = O(n^3)$. But we do not concluded $f_1(n) = f_2(n)$.

Therefore, the worst time complexity of Insertion Sort $W(n) = O(n^2)$, which means that it is asymptotically at most $n^2$.

!!! note multiple variables
    $f(m, n)$ is $O(g(m, n))$ if there exists constants $c > 0,\, m_0 \ge 0,\, n_0 \ge 0$ such that $0 \le f(m, n) \le c \cdot g(m, n)$ for all $m \ge m_0,\, n \ge n_0$.

    Ex. $f(m, n) = 32mn^2 + 17mn + 32n^3$ is both $O(mn^2 + n^3)$ and $O(mn^3)$, but is neither $O(n^3)$ nor $O(mn^2)$.

### Big $\Omega$ notation

!!! info Big $\Omega$ notation(大 $\Omega$ 符号)
    Given a function $g(n)$, we denote by $\Omega(g(n))$ the following set of functions:

    $$
    \Omega(g(n)) = \left\lbrace f(n) \mid \exists c > 0,\, \exists n_0 > 0,\, \forall n \ge n_0\colon f(n) \ge c \cdot g(n) \right\rbrace
    $$

    **Asymptotic lower bounds**(渐近下界): when we say $f(n)$ is $\Omega(g(n))$, we mean that $f(n)$ grows at least as fast as a certain rate (is asymptotically at least $g(n)$).

### Big $\Theta$ notation

!!! info Big $\Theta$ notation(大 $\Theta$ 符号)
    Given a function $g(n)$, we denote by $\Theta(g(n))$ the following set of functions:

    $$
    \Theta(g(n)) = \left\lbrace f(n) \mid \exists c_1 > 0,\, \exists c_2 > 0,\, \exists n_0 > 0,\, \forall n \ge n_0\colon c_1 \cdot g(n) \le f(n) \le c_2 \cdot g(n) \right\rbrace
    $$

    **Asymptotically tight bounds**(渐近紧确界): when we say $f(n)$ is $\Theta(g(n))$, we mean that $f(n)$ grows precisely at a certain rate (is asymptotically equal to $g(n)$).

### Small $o$ and $\omega$ notation

!!! info Small $o$ notation(小 $o$ 符号)
    Given a function $g(n)$, we denote by $o(g(n))$ the following set of functions:

    $$
    o(g(n)) = \left\lbrace f(n) \mid \forall c > 0,\, \exists n_0 > 0,\, \forall n \ge n_0\colon 0 \le f(n) < c \cdot g(n) \right\rbrace
    $$

    $f(n)$ is asymptotically (strictly) smaller than $g(n)$.

!!! info Small $\omega$ notation(小 $\omega$ 符号)
    Given a function $g(n)$, we denote by $\omega(g(n))$ the following set of functions:

    $$
    \omega(g(n)) = \left\lbrace f(n) \mid \forall c > 0,\, \exists n_0 > 0,\, \forall n \ge n_0\colon f(n) > c \cdot g(n) \right\rbrace
    $$

    $f(n)$ is asymptotically (strictly) larger than $g(n)$.

There is no small $\theta$ notation.

### Some properties of asymptotic notations

- **Reflexivity**: $f(n) \in O(f(n))$; but $f(n) \notin o(f(n))$
- **Transitivity**: if $f(n) \in O(g(n))$ and $g(n) \in O(h(n))$, then $f(n) \in O(h(n))$
- **Symmetry**: $f(n) \in \Theta(g(n)) \iff g(n) \in \Theta(f(n))$
- **Transpose symmetry**: $f(n) \in O(g(n)) \iff g(n) \in \Omega(f(n))$

### Asymptotic bounds and limits

If cost functions are complex, it is hard to apply the definitions to get its asymptotic bounds. In this case, it usually easier to apply <u>limit method</u>.

!!! note ""
    1. If $\lim\limits_{n\to \infty } \dfrac{f(n)}{g(n)} = c$ for some constant $0 < c < \infty$, then $f(n)$ is $\Theta(g(n))$.
    2. If $\lim\limits_{n\to \infty } \dfrac{f(n)}{g(n)} = 0$, then $f(n)$ is $O(g(n))$. (a.k.a. $f(n)$ is $o(g(n))$).
    3. If $\lim\limits_{n\to \infty } \dfrac{f(n)}{g(n)} = \infty$, then $f(n)$ is $\Omega(g(n))$. (a.k.a. $f(n)$ is $\omega(g(n))$).

    <!-- {{{ Proof of 1. -->
    <details>
    <summary>Proof of 1.</summary>

    By definition of the limits, for any $\varepsilon > 0$, there exists $n_0$ such that $c - \varepsilon \le  \dfrac{f(n)}{g(n)} \le c + \varepsilon$ for all $n \ge  n_0$.

    Choose $\varepsilon = \dfrac{c}{2} > 0$. Multiplying by $g(n)$ yields $\dfrac{1}{2}c \cdot g(n) \le f(n) \le \dfrac{3}{2} c \cdot g(n)$ for all $n \ge  n_0$.

    Thus, $f(n)$ is $\Theta(g(n))$ by definition, with $c_1 = \dfrac{1}{2}c$ and $c_2 = \dfrac{3}{2} c$.

    </details>
    <!-- }}} -->

Asymptotic bounds for some common functions
- Polynomials: $p(n)$ is $\Theta(n^d)$, where $d$ is the maximum degree of $p(n)$.
- Logarithms: $\log_a n$ is $\Theta(\log_b n)$ for any $a, b > 1$.
    - $\log_a n$ is $O(n^d)$ for every $a > 1, d > 0$.
- Exponentials: $a^n$ is $\Theta(b^n)$ for any $a, b > 1$.
    - $n^d$ is $O(r^n)$ for every $r > 1, d > 0$.
- Factorials: $n!$ is $\Theta(n^n)$, $\log (n!)$ is $\Theta(n \log n)$.
    - Using [Stirling's formula(斯特林公式)](https://zh.wikipedia.org/wiki/斯特林公式): $n! \sim \sqrt{2 \pi n} \left( \dfrac{n}{\e} \right)^n$.

$$
\begin{aligned}
    \text{tractable}&\begin{cases}
        \Theta(1), &\text{constant}\\
        \Theta(\log n), &\text{logarithm}\\
        \Theta(n), &\text{linear}\\
        \Theta(n \log n) &\text{linearithmic}\\
        \Theta(n^c), &\text{polynomial}\\
    \end{cases}\\
    \text{intractable}&\begin{cases}
        \Theta(2^n), &\text{exponential}\\
        \Theta(n!), &\text{factorial}\\
    \end{cases}
\end{aligned}
$$

When considering brute force algorithm to solve one problem, it is usually asymptotically equal to exponential functions.

When an algorithm has a <u>polynomial running time</u>, we say it is **efficient**, and the corresponding problem is so-called **easy** or **tractable**. The algorithm has typically exposes some crucial structure of the problem.

Although, there are exceptions. Some poly-time algorithms in the wild have galactic constants and/or huge exponents. Which would you prefer: $20n^{120}$ or $n^{1+\ln n}$?
