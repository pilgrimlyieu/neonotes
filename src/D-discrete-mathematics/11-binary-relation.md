---
layout: post
title: 二元关系
date: 2024-04-16 10:09:54
updated: 2024-05-01 22:24:40
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 关系

### 定义

见 [05-函数及其运算](./05-function-and-its-operation#关系)。

令 $R \subseteq A \times B$，则 $(a, b) \in R$ 可记作 $aRb$，$(a, b) \notin R$ 可记作 $a \cancel{R} b$。

设 $R$ 是 $A$ 到 $B$ 的一个关系：
- $R$ 的**定义域**（Domain）：$\operatorname{Dom}R = \{a \in A \mid \exists b \in B,\,  aRb\}$
- $R$ 的**值域**（Range）：$\operatorname{Ran}R = \{b \in B \mid \exists a \in A,\,  aRb\}$
- $R$ 的**域**（Field）：$\operatorname{Fld}R = \operatorname{Dom}R \cup \operatorname{Ran}R$

|                             关系 $R \subseteq A \times B$                             |                    有向图 $(V_D, E_D)$                 |
|                                          :-:                                          |                                  :-:                         |
|                                     $A, B$ 是集合                                     |             顶点集 $V_D = A \cup B$               |
|                                      有序对集合                                       | 有向边集 $E_D = \{(a, b) \mid aRb\}$        |
|                                    $(x, y) \in R$                                     |                  从 $x$ 到 $y$ 有一条边               |
| 若 $A = B$，$R$ 中存在序列：$(x_1, x_2),\, (x_2, x_3),\,  \cdots,\, (x_{n-1}, x_n)$ |             图 $D$ 中存在从 $x_1$ 到 $x_n$ 的长度为 $n-1$ 通路 |

### 运算

设 $R$ 为从 $A$ 到 $B$ 的关系：
- $R \uparrow S = \{(a, b) \mid a \in S \land aRb\}$
    - $R \uparrow S \subseteq R$ 
- $R[S] = \{b \mid \exists a \in S,\, aRb\} = \operatorname{Ran} (R \uparrow S)$
    - $R[S] \subseteq \operatorname{Ran}R$
- $R^{-1} = \{(b, a) \mid aRb\}$
    - $R^{-1}$ 是从 $B$ 到 $A$ 的关系
    - $\left(R^{-1}\right)^{-1} = R$
    - $\left(R_1 \cup R_2\right)^{-1} = R_1^{-1} \cup R_2^{-1}$ 

设 $R_1 \subseteq A \times B,\, R_2 \subset B \times C$，则 $R_1, R_2$ 的复合记为 $R_2 \circ R_1$，定义为：$R_2 \circ R_1 = \{(a, c) \in A \times C \mid \exists b \in B,\, aR_1b \land bR_2c\}$。
- $R_3 \circ (R_2 \circ R_1) = (R_3 \circ R_2) \circ R_1$
- $\left(R_2 \circ R_1\right)^{-1} = R_1^{-1} \circ R_2^{-1}$

对 $F \subseteq A \times B, G \subseteq B \times C, H \subseteq B \times C$，跟函数类似，有：
- $(G \cup H) \circ F = (G \circ F) \cup (H \circ F)$
- $(G \cap H) \circ F \subseteq (G \circ F) \cap (H \circ F)$

### 矩阵算法

对同阶零一矩阵 $\bm{M}_1, \bm{M}_2$，有
- $\bm{C} = \bm{M}_1 \land \bm{M}_2$：$c_{ij} = m^1_{ij} \land m^2_{ij}$
- $\bm{C} = \bm{M}_1 \lor \bm{M}_2$：$c_{ij} = m^1_{ij} \lor m^2_{ij}$

对 $r \times s, s \times t$ 的零一矩阵 $\bm{M}_1, \bm{M}_2$，有
- $r \times t$ 矩阵 $\bm{C} = \bm{M}_1 \odot \bm{M}_2$：$c_{ij} = \displaystyle \bigvee_{k=1}^s m^1_{ik} \land m^2_{kj}$

对于关系 $R_1, R_2$，有
- $\bm{M}_{R_1 \cap R_2} = \bm{M}_{R_1} \land \bm{M}_{R_2}$
- $\bm{M}_{R_1 \cup R_2} = \bm{M}_{R_1} \lor \bm{M}_{R_2}$
- $\bm{M}_{R_2 \circ R_1} = \bm{M}_{R_1} \odot \bm{M}_{R_2}$

### 性质

集合 $S$ 上的关系 $R$：
- **自反性**（Reflexivity）：$\forall s \in S,\, sRs$（$\iff I_S \subseteq R$）
- **反自反性**（Irreflexivity）：$\forall s \in S,\, s \cancel{R} s$（也是任意，所以不是自反的否定）
- **对称性**（Symmetry）：$aRb \models bRa$（$\iff R^{-1} = R$，空关系也是对称关系）
- **反对称性**（Antisymmetry）：$aRb, bRa \models a = b$（对称与反对称可以同时成立）
- **不对称性**（Asymmetric）：$a R b \models \lnot (b R a)$（反对称的反自反关系）
- **非对称性**（Asymmetry）：$aRb \models b\cancel{R}a$
- **传递性**（Transitivity）：$aRb, bRc \models aRc$（$\iff R \circ R \subseteq R$，空关系也是传递关系）

关系复合有结合律，则记 $R^n = \overbrace{R \circ R \circ \cdots \circ R}^{n}$，$n \in \Z^{+}$。

有 $(a, b) \in R^n$ 当且仅当存在 $t_1, t_2, \cdots, t_{n-1} \in S$ 使得 $aRt_1, t_1Rt_2, \cdots, t_{n-1}Rb$。

|        | $=$ | $\le $ | $<$ | $\mid$ | $\equiv$ | $\empty $ |   $E$ |
|  :-:   | :-: |  :-:   | :-: |  :-:   |   :-:    |    :-:    | :-: |
|  自反  |  √  |   √    |  ×  |   √    |    √     |     ×     |        √  |
| 反自反 |  ×  |   ×    |  √  |   ×    |    ×     |     √     |        ×  |
|  对称  |  √  |   ×    |  ×  |   ×    |    √     |     √     |        √  |
| 反对称 |  √  |   √    |  √  |   √    |    ×     |     √     |        ×  |
|  传递  |  √  |   √    |  √  |   √    |    √     |     √     |        √  |

关系运算与性质的保持：

|                 | 自反 | 反自反 | 对称 | 反对称 | 传递 |
|       :-:       | :-:  |  :-:   | :-:  |  :-:   | :-:  |
|    $R^{-1}$     |  √   |   √    |  √   |   √    |  √   |
| $R_1 \cap R_2$  |  √   |   √    |  √   |   √    |  √   |
| $R_1 \cup R_2$  |  √   |   √    |  √   |   ×    |  ×   |
| $R_1 \circ R_2$ |  √   |   ×    |  ×   |   ×    |  ×   |

表示形式：

|          | 集合表达式                    | 关系矩阵                                           | 关系图                                                                        |
| :-       | :-                            | :-                                                 | :-                                                                            |
| 自反性   | $I_A \subseteq R$             | 主对角线全是 $1$                                   | 每个顶点都有环                                                                |
| 反自反性 | $I_A \cap R = \empty$         | 主对角线全是 $0$                                   | 每个顶点都没有环                                                              |
| 对称性   | $R = R^{-1}$                  | 是对称矩阵                                         | 如果两个顶点之间有边，那么是一对方向相反的边（即无单边）                      |
| 反对称性 | $R \cap R^{-1} \subseteq I_A$ | 若 $r_{ij} = 1$ 且 $i \ne j$ 则 $r_{ji} = 0$       | 如果两个顶点之间有边，那么是一条有向边（即无双向边）                          |
| 传递性   | $R \circ R \subseteq R$       | 对 $M^2$ 中 $1$ 所在的位置，$M$ 中对应位置也是 $1$ | 如果顶点 $x_i$ 到 $x_j$ 有边，$x_j$ 到 $x_k$ 有边，那么 $x_i$ 到 $x_k$ 也有边 |

设 $R$ 为 $A$ 上关系，$A = \left\lbrace a_1, \cdots, a_n \right\rbrace$，其中 $\bm{M}$ 为 $R$ 的关系矩阵：
- $R$ 自反 $\iff \displaystyle \prod_{i=1}^{n} m_{ii} = 1$
- $R$ 反自反 $\iff \displaystyle \sum_{i=1}^{n} m_{ii} = 0$
- $R$ 对称 $\iff \bm{M} = \bm{M}^\intercal$
- $R$ 反对称 $\iff \forall i, j,\,  i \ne j \implies m_{ij} \cdot m_{ji} = 0$
    - 同阶矩阵 $\bm{A} \le \bm{B}$ 表示 $\forall i, j,\,  a_{ij} \le b_{ij}$
- $R$ 传递 $\iff \bm{M} \odot \bm{M} \le \bm{M}$
    - 即 $\bm{M} \odot \bm{M} = \bm{M} \implies R$ 传递，但反之不然

## 关系闭包

!!! info ""
    设 $R$ 是集合 $A$ 上的关系，$\mathfrak{P}$ 是给定的某种性质（如：自反、对称、传递），满足下列所有条件的关系 $R_{1}$ 称为 $R$ 的关于 $\mathfrak{P}$ 的闭包:
    - $R \subseteq R_{1}$
    - $R_{1}$ 满足性质 $\mathfrak{P}$
    - 若存在集合 $A$ 上满足性质 $\mathfrak{P}$ 的关系 $R'$ 且 $R \subseteq R'$，则 $R_1 \subset R'$。

特殊闭包：
- 自反闭包：$r(R) = R \cup I_A$
- 对称闭包：$s(R) = R \cup R^{-1}$
- 传递闭包：$t(R) = R^{*}$

!!! info ""
    设 $R$ 是集合 $A$ 上的关系，定义 $A$ 上的 **$R$ 连通关系 $R^{*}$** 为：

    对任意 $a, b \in A$，$a R^{*} b$ 当且仅当 $(a, b) \in R \lor \exists t_1, \cdots, t_k \in A,\, (a, t_1) \in R, \cdots, (t_k, b) \in R$（即从 $a$ 到 $b$ 存在长度至少为 $1$ 的通路）

    于是

    $$
    R^{*} = \bigcup_{k=1}^{\infty} R^{k}
    $$

- $r\bigl(s(R)\bigr) = s\bigl(r(R)\bigr)$，可记为 $rs(R)$。
- $s\bigl(t(R)\bigr) \subseteq t\bigl(s(R)\bigr)$，可记为 $st(R) \subseteq ts(R)$（证明通过闭包的定义）。

### 闭包的存在性

关于性质 $\mathfrak{P}$ 的闭包是否存在？

令 $R' = \bigcap \left\lbrace X \mid R \subseteq X \land X \text{ 有性质 } \mathfrak{P} \right\rbrace$，则闭包 $R_1$ 存在当且仅当 $R'$ 存在，也即 $\left\lbrace X \mid R \subseteq X \land X \text{ 有性质 } \mathfrak{P} \right\rbrace$ 非空。

### 闭包的计算

自反闭包和对称闭包显然，而传递闭包理论上存在（根据上面的定义）。

对有限集合 $A$，若 $|A| = n$，则有 $A$ 上传递闭包

$$
t(R) = \bigcup_{k=1}^{n} R^{k}
$$

!!! note ""
    也许会因为上面的定义而认为是 $\displaystyle \bigcup_{i=1}^{n-1}R^k$，但额外考虑 $(1, n), \cdots, (n, 1)$，则有 $(1, 1)$ 有长度为 $n$ 的通路（因为是从长度为 $1$ 的通路，如 $(1, 2)$ 开始计算的）。

矩阵乘法计算传递闭包

$$
\bm{M}_{t(R)} = \bm{M} \lor \bm{M}^2 \lor \cdots \lor \bm{M}^n
$$

运算量为 $2n^3(n - 1)$。

### Warshall 算法

!!! info ""
    将 $n$ 个顶点用 $n$ 个正整数 $1, \cdots, n$ 进行标号，设 $D_{i, j, k}$ 为从 $i$ 到 $j$ 的通路中只经过 $1, \cdots, k$ 的顶点的最短通路的长度。
    
    若最短路径经过 $k$，则
    
    $$
    D_{i, j, k} = D_{i, k, k - 1} + D_{k, j, k - 1}
    $$
    
    否则
    
    $$
    D_{i, j, k} = D_{i, j, k - 1}
    $$
    
    因而有
    
    $$
    D_{i, j, k} = \min \left\lbrace D_{i, j, k - 1}, D_{i, k, k - 1} + D_{k, j, k - 1} \right\rbrace
    $$

考虑回传递闭包，设 $\bm{R}^{(k)}_{ij}$ 为从 $i$ 到 $j$ 的通路中只经过 $1, \cdots, k$ 的顶点的通路，则可以写出

$$
\bm{R}^{(k)}_{ij} = \bm{R}^{(k - 1)}_{ij} \lor \left( \bm{R}^{(k - 1)}_{ik} \land \bm{R}^{(k - 1)}_{kj} \right)
$$

Warshall 算法高效的根源在于可以直接利用上一步计算结果中的有效信息简化当前步的计算过程。

运算量为 $2n^3$。

## 等价关系

!!! info ""
    设 $R$ 是非空集合 $A$ 上的二元关系，若 $R$ 有如下性质：
    - 自反性
    - 对称性
    - 传递性

    则称 $R$ 是 $A$ 上的**等价关系**。

!!! info ""
    设 $R$ 是非空集合 $A$ 上的等价关系，对于任意 $a \in A$，**$a$ 的等价类**定义为

    $$
    [a]_R = \{b \in A \mid aRb\}
    $$

    $a$ 称为这个等价类的**代表元素**。

    显然若 $aRb$，则 $[a]_R = [b]_R$。

!!! info ""
    设 $R$ 是非空集合 $A$ 上的等价关系，$A$ 的所有等价类构成的集合称为 $A$ 关于 $R$ 的**商集**，记作 $A/R$。

    $A/R$ 的元素是 $A$ 的等价类。

!!! info ""
    集合 $A$ 的**划分 $\pi$**（partition）是 $A$ 的一组非空子集的集合，即 $\pi \in \mathcal{P}(A)$ 且满足：
    1. 对任意 $a \in A$，则存在某个 $A_i \in \pi$ 使得 $a \in A_i$。即 $\displaystyle \bigcup_{A_i \in \pi} A_i = A$。
    2. 对任意 $A_i, A_j \in \pi$ 且 $i \ne j$，则 $A_i \cap A_j = \empty$。

则商集 $A/R$ 是 $A$ 的一个划分。即有公共元素的任意两个等价类必相等。

设 $R(a)$ 是由 $R$ 所诱导的，关于 $a \in A$ 的等价类，即 $R(a) = [a]_R$。

不妨设 $R(a) \cap R(b) \ne \empty$，设 $c$ 是一个公共元素，从而有 $aRc, bRc$。

任意 $x \in R(a), aRx$，传递性和对称性有 $cRx$，再由 $bRc$ 有 $bRx$，即 $x \in R(b)$。从而 $R(a) \subseteq R(b)$。

同理可证 $R(b) \subseteq R(a)$，从而 $R(a) = R(b)$。

于是可以通过划分定义等价关系。

!!! info ""
    给定 $A$ 上一个划分 $\pi$，定义 $A$ 上的等价关系 $R$：

    $$
    aRb \iff \exists A_i \in \pi, a, b \in A_i
    $$
