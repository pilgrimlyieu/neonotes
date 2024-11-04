---
layout: post
title: 命题逻辑
date: 2024-02-27 18:33:26
updated: 2024-04-14 16:04:06
description:
draft: false
comments: true
disableNunjucks: true
katex: true
---

!!! memo ""
    目前记得比较乱。

!!! memo ""
    好好好，老师讲 $\LaTeX$，喜。虽然没细谈。

## 命题逻辑

| 布尔运算符 |   名词   |   英文名词   | 英文符号 |                     $\LaTeX$                      |
| :--------: | :------: | :----------: | :------: | :-----------------------------------------------: |
|   **与**   | **合取** | Conjunction  |   AND    |   $p \land q;\; p \mathbin{\&} q;\; p \cdot q$    |
|   **或**   | **析取** | Disjunction  |    OR    |                $p \lor q;\; p + q$                |
|   **非**   | **否定** |   Negation   |   NOT    |          $\lnot p;\; \sim p;\; \bar{p}$           |

!!! note ""
    $\LaTeX$ 正好是 **l**ogical + 对应英文，即分别为 `\land` `\lor` `\lnot`。

除非 $p$，否则没有 $q$：$\lnot p \mathbin{\to} \lnot q$，即 $q \mathbin{\to} p$。从集合的角度，$q \subset p$。$p$ 的发生是 $q$ 的发生的必要条件。

- **推理**（Reasoning）
    - **演绎**（Deduction）
    - **归纳**（Induction）
    - **溯因**/**反绎**（Abduction）

目标是初步理解一下概念：
- 断言（Assertion）
- 命题（Proposition）
- 论证（Argument）
- 有效性（Validity）
- 证明（Proof）
- 定理（Theorem）
- 矛盾（Contradiction）
- 悖论（Paradox）
- 一致性（Consistency）
- 可靠性（Soundness）
- 完备性（Completeness）

!!! info 命题
    **命题**是一个陈述语句，即<u>一个陈述事实的句子</u>。

$3 - x = 5$ 不是命题，$x$ 值不定。

- **形式逻辑**：推理形式与内容的分离
- **符号逻辑**：使推理的形式与内容彻底分离，引入符号语言。
- **数理逻辑**：用符号逻辑作为研究数学问题的基本工具。

### 命题变元

常用小写字母 $p,\, q,\, r$ 等表示**命题变元**，取值范围为 $\{\mathbf{T},\, \mathbf{F}\}$ 或 $\{1,\, 0\}$。

不能用简单的命题表示的命题称为**原子命题**。

### 逻辑连接词

**否定**

| $p$ | $\lnot p$ |
| :-: | :-------: |
| $0$ |  $\bm{1}$ |
| $1$ |  $\bm{0}$ |

**合取**

| $p$ | $q$ | $p \land q$ |
| :-: | :-: | :---------: |
| $0$ | $0$ |   $\bm{0}$  |
| $0$ | $1$ |   $\bm{0}$  |
| $1$ | $0$ |   $\bm{0}$  |
| $1$ | $1$ |   $\bm{1}$  |

**析取**

| $p$ | $q$ | $p \lor q$ |
| :-: | :-: | :--------: |
| $0$ | $0$ |   $\bm{0}$ |
| $0$ | $1$ |   $\bm{1}$ |
| $1$ | $0$ |   $\bm{1}$ |
| $1$ | $1$ |   $\bm{1}$ |

**异或**：$p \oplus q$，当 $p$ 与 $q$ 有不同的真值时为真。

| $p$ | $q$ | $p \oplus q$ |
| :-: | :-: | :---------: |
| $0$ | $0$ |   $\bm{0}$  |
| $0$ | $1$ |   $\bm{1}$  |
| $1$ | $0$ |   $\bm{1}$  |
| $1$ | $1$ |   $\bm{0}$  |

$p \oplus q = (p \lor q) \land \lnot (p \land q)$。

**蕴含**（Implication, Conditional）：$p \mathbin{\to} q$（若 $p$ 则 $q$），当 $p$ 为真时，$q$ 为真。$p$ 称为<u>假设</u>，$q$ 称为<u>结论</u>。

| $p$ | $q$ | $p \mathbin{\to} q$ |
| :-: | :-: | :-------: |
| $0$ | $0$ |   $\bm{1}$ |
| $0$ | $1$ |   $\bm{1}$ |
| $1$ | $0$ |   $\bm{0}$ |
| $1$ | $1$ |   $\bm{1}$ |

$p \mathbin{\to} q = \lnot p \lor q$。

荒谬的前提可以推出任何结论，即对 $p = 0$ 与任意 $q$，$p \mathbin{\to} q = 1$。

- $a$ 仅当 $b$：$a \mathbin{\to} b$
- 不能 $a$ 除非 $b$：$\lnot b \mathbin{\to} \lnot a$

可以从集合的角度进行理解，$p \mathbin{\to} q$ 可以理解为 $S_p \subseteq S_q$。考虑 $p = q = 1$，对 $r \in S_p$ 都有 $r \in S_q$。或者理解成 $p \implies q$。

**双条件**（Biconditional）：$p \mathbin{\leftrightarrow} q$，当 $p$ 与 $q$ 的真值相同时为真。

| $p$ | $q$ | $p \mathbin{\leftrightarrow} q$ |
| :-: | :-: | :------------------: |
| $0$ | $0$ |        $\bm{1}$        |
| $0$ | $1$ |        $\bm{0}$        |
| $1$ | $0$ |        $\bm{0}$        |
| $1$ | $1$ |        $\bm{1}$        |

$p \mathbin{\leftrightarrow} q = (p \mathbin{\to} q) \land (q \mathbin{\to} p)$。

双条件语句为「当且仅当」，可以用 $\mathrm{iff}$（iff and only if）表示。（真正的 $\mathrm{iff}$ 是 $\iff$）

逻辑运算符优先级：

$$
\lnot > \land > \lor > \mathbin{\to} > \mathbin{\leftrightarrow}
$$

也同时约定 $\mathbin{\to}$ 为右结合的，即 $p \mathbin{\to} q \mathbin{\to} r = p \mathbin{\to} (q \mathbin{\to} r)$。

前三者是在编程语言中就了解过了的，符合常识。然而对于复杂命题还是多加括号为好。

### 命题表达式（命题逻辑公式）

命题逻辑的**合式公式**（**W**ell-**F**ormed **F**ormula）：
1. 命题变元 $p_1,\, p_2,\, \cdots$ 是命题表达式
2. 若 $\varphi$ 是命题表达式，则 $\lnot \varphi$ 也是命题表达式
3. 若 $\varphi$ 与 $\psi$ 是命题表达式，则 $(\varphi \land \psi)$、$(\varphi \lor \psi)$、$(\varphi \mathbin{\to} \psi)$、$(\varphi \mathbin{\leftrightarrow} \psi)$ 也是命题表达式
4. 只有**有限次**应用 1-3 的规则得到的表达式才是命题表达式

列出命题表达式真值表，命题变元所有取值组合称为该命题表达式的所有**指派**（Assignment）。

- 真值为真的指派称为**成真指派**（Satisfying Assignment）。
- 真值为假的指派称为**成假指派**（Falsifying Assignment）。

- **永真式**（重言式 Tautology）：对于所有指派，命题表达式的真值都为真。如 $p \lor \lnot p$。
- **矛盾式**（Contradiction）：对于所有指派，命题表达式的真值都为假。如 $p \land \lnot p$。
- **可能式**（Contingency）：既不是永真式也不是矛盾式。如 $p$。

### 语义蕴含（Semantic Entailment）

$\varphi$ **语义蕴含** $\psi$，记作 $\varphi \models \psi$，当且仅当对于任意一个 $\varphi$ 的成真指派，对 $\psi$ 也是成真的。也被称为重言蕴含、逻辑蕴含。

等价的，$\varphi \models \psi$ 当且仅当 $\varphi \mathbin{\to} \psi$ 是重言式。

$\varphi$ 是永真的，记为 $\models \varphi$（$\varphi$ is valid）。例如 $\models p \lor \lnot p$。

### 逻辑等价

$\varphi$ 与 $\psi$ 是**逻辑等价**（重言等价），记作 $\varphi \equiv \psi$，当且仅当对于任意指派，$\varphi$ 与 $\psi$ 的真值相同。

即 $p \mathbin{\leftrightarrow} q$ 是重言式，亦即 $\models p \mathbin{\leftrightarrow} q$。

命题逻辑的推理问题可归结为「判断某个命题逻辑公式是否为重言式」，如：
- $\varphi \models \psi \iff  \varphi \mathbin{\to} \psi$ 是重言式
- $\varphi \equiv \psi \iff  \varphi \mathbin{\leftrightarrow} \psi$ 是重言式
- $\varphi$ 可满足 $\iff$ $\lnot \varphi$ 不是重言式

SAT 问题（The **Sat**isfiability Problem）：判断一个命题逻辑公式是否有成真指派。

### 常用逻辑等价

- **双重否定律**：$p \equiv \lnot \lnot p$
- **幂等律**
    - $p \equiv p \land p$
    - $p \equiv p \lor p$
- **交换律**
    - $p \land q \equiv q \land p$
    - $p \lor q \equiv q \lor p$
- **结合律**
    - $(p \land q) \land r \equiv p \land (q \land r)$
    - $(p \lor q) \lor r \equiv p \lor (q \lor r)$
- **分配律**
    - $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$
    - $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$
- **德摩根律**
    - $\lnot (p \land q) \equiv \lnot p \lor \lnot q$
    - $\lnot (p \lor q) \equiv \lnot p \land \lnot q$
- **吸收律**
    - $p \lor (p \land q) \equiv p$
    - $p \land (p \lor q) \equiv p$
- **支配律**
    - $p \lor \mathbf{T} \equiv \mathbf{T}$
    - $p \land \mathbf{F} \equiv \mathbf{F}$
- **恒等律**
    - $p \lor \mathbf{F} \equiv p$
    - $p \land \mathbf{T} \equiv p$
- **排中律**：$p \lor \lnot p \equiv \mathbf{T}$
- **矛盾律**：$p \land \lnot p \equiv \mathbf{F}$
- **假言易位**：$p \to q \equiv \lnot q \to \lnot p$
- **归谬论**：$(p \to q) \land (p \to \lnot q) \equiv \lnot p$
- 其它
    - $p \to q \equiv \lnot p \lor q$
    - $p \leftrightarrow q \equiv (p \to q) \land (q \to p)$
    - $p \leftrightarrow q \equiv \lnot q \leftrightarrow \lnot p$

### 范式

范式：
- 有限个文字的析取式称为**简单析取式**（基本和）
- 有限个文字的合取式称为**简单合取式**（基本积）
- 由有限个<u>简单合取式</u>构成的析取式称为**析取范式**（DNF, Disjunctive Normal Form）
    - $\cdots \lor (p_1 \land p_2 \land \cdots \land p_n) \lor \cdots$
- 由有限个<u>简单析取式</u>构成的合取式称为**合取范式**（CNF, Conjunctive Normal Form）。
    - $\cdots \land (p_1 \lor p_2 \lor \cdots \lor p_n) \land \cdots$
    - $\models p_1 \lor p_2 \lor \cdots \lor p_n \iff \exist_{i, j},\, p_i \equiv \lnot p_j$

性质：
- 一个文字<u>既是一个析取范式又是一个合取范式</u>
- 一个析取范式为*矛盾式*，当且仅当它的每个简单合取式是*矛盾式*
- 一个合取范式为*重言式*，当且仅当它的每个简单析取式是*重言式*

!!! info ""
    任一命题公式都存在着与之重言等价的析取范式和合取范式。

范式不唯一，从而定义：
- 包含所有命题变元或其否定一次仅一次的*简单合取式*，称为**极小项**
- 包含所有命题变元或其否定一次仅一次的*简单析取式*，称为**极大项**
- 由有限个*极小项*组成的析取范式称为**主析取范式**
- 由有限个*极大项*组成的合取范式称为**主合取范式**。

性质：
- 没有两个不同的极小项是等价的，且<u>每个极小项只有一组真值指派，使该极小项的真值为真</u>，因此可给极小项编码，使极小项为 $\mathbf{T}$ 和那组真值指派为对应的极小项编码。
    - 如极小项 $\neg P \land \neg Q \land \neg R$ 只有在 $P, Q$, $R$ 分别取真值 $0,0,0$ 时才为真，所以有时又可用 $m_{000}\left(m_{0}\right)$ 来表示
    - 又如 $\neg P \land Q \land \neg R$ 也可用 $m_{010}\left(m_{2}\right)$ 来表示。
- 没有两个不同的极大项是等价的，且<u>每个极大项只有一组真值指派，使该极大项的真值为假</u>，因此可给极大项编码，使极大项为 $\mathbf{F}$ 和那组真值指派为对应的极大项编码。
    - 如极大项 $P \lor Q \lor R$ 只有在 $P, Q$, $R$ 分别取真值 $1,1,1$ 时才为真，所以有时又可用 $M_{111}\left(M_{7}\right)$ 来表示
    - 又如 $P \lor \neg Q \lor R$ 也可用 $M_{101}\left(M_{5}\right)$ 来表示。
- 任意两个极小项的合取为矛盾式，任意两个极大项的析取为重言式
    - $m_i \land m_j \equiv \mathbf{F}(i \ne j,\, i, j \in [0, 2^n-1])$
    - $M_i \lor M_j \equiv \mathbf{T}(i \ne j,\, i, j \in [0, 2^n-1])$
- 所有的极小项的析取为重言式，所有的极大项的合取为矛盾式
    - $\bigvee\limits_{i=0}^{2^n-1} m_i \equiv \mathbf{T}$
    - $\bigwedge\limits_{i=0}^{2^n-1} M_i \equiv \mathbf{F}$

!!! info ""
    任何命题公式的主析取范式和主合取范式<u>存在且唯一</u>，即任何命题公式都<u>有且仅有一个</u>与之等价的主合取范式和主析取范式。

### 演绎系统

!!! memo ""
    $\KaTeX$ 写自然演绎让人窒息

!!! info ""
    **希尔伯特式推演系统 $\mathcal{L}$**

    三条公理：
    1. $\mathrm{L_1}\colon \alpha \to (\beta \to \alpha)$
    2. $\mathrm{L_2}\colon (\alpha \to (\beta \to \gamma)) \to ((\alpha \to \beta) \to (\alpha \to \gamma))$
    3. $\mathrm{L_3}\colon (\lnot \alpha \to \lnot \beta) \to (\beta \to \alpha)$

    一条推理规则：
    1. 分离规则：$\left\lbrace \alpha, \alpha \to \beta \right\rbrace \vdash \beta$

采用 Stanisław Jaśkowski 的「自然演绎记法」。

| | 引入（Introduction） | 消去（Elimination） |
| :-: | :-: | :-: |
| 合取 $\land$ | $ \begin{aligned} \varphi\quad \psi\\ \hline \varphi \land \psi \end{aligned} \land \mathrm{i.}$ | $ \begin{aligned} \varphi \nobreak \land \nobreak \psi\\ \hline \varphi \hspace{0.9em}\end{aligned} \nobreak \land \nobreak \mathrm{e}_1. \quad \begin{aligned} \varphi \land \psi\\ \hline \psi \hspace{0.9em} \end{aligned} \nobreak \land \nobreak \mathrm{e}_2.$ |
| 析取 $\lor$ | $ \begin{aligned} \varphi \hspace{0.8em}\\ \hline \varphi \lor \psi \end{aligned} \nobreak \lor \nobreak \mathrm{i}_1. \quad \begin{aligned} \psi \hspace{0.8em}\\ \hline \varphi \lor \psi \end{aligned} \nobreak \lor \nobreak \mathrm{i}_2.$ | $ \begin{aligned} \varphi \lor \psi\quad \boxed{\begin{aligned} &\varphi\\ &\kern{0.2em}\vdots\\ &\chi \end{aligned}}\quad \boxed{\begin{aligned} &\psi\\ &\kern{0.25em}\vdots\\ &\chi \end{aligned}}\\ \hline \chi \hspace{3em}\end{aligned} \; \nobreak \raisebox{-2.3em}{\(\lor \,\nobreak \mathrm{e.}\)} $ |
| 蕴含 $\to$ | $ \begin{aligned} \boxed{\begin{aligned} &\varphi\\ &\kern{0.2em}\vdots\\ &\psi \end{aligned}} \hspace{0.7em}\\ \hline \varphi \to \psi \end{aligned} \nobreak \;\raisebox{-2.3em}{\(\to \nobreak \mathrm{i.}\)} $ | $ \begin{aligned} \varphi\quad \varphi \to \psi\\ \hline \psi \hspace{1.75em}\end{aligned} \nobreak \to \nobreak \mathrm{e.}$ |
| 否定 $\lnot$ | $ \begin{aligned} \boxed{\begin{aligned} &\varphi\\ &\kern{0.25em}\vdots\\ &\bot \end{aligned}}\\ \hline \lnot \varphi \end{aligned} \; \nobreak \raisebox{-2.3em}{\(\lnot \, \nobreak \mathrm{i.}\)} $ | $ \begin{aligned} \varphi\quad \lnot \varphi\\ \hline \bot \hspace{1em}\end{aligned}\; \nobreak \lnot \, \nobreak \mathrm{e.}$ |
| 假值 $\bot$ | Nop | $ \begin{aligned} \bot\\ \hline \varphi \end{aligned} \; \nobreak \bot \, \nobreak \mathrm{e.}$ |
| 双重否定 $\lnot \lnot$ | $ \begin{aligned} \varphi \hspace{0.5em}\\ \hline \lnot \lnot \varphi \end{aligned} \; \nobreak \lnot \lnot \, \nobreak \mathrm{i.}$ | $ \begin{aligned} \lnot \lnot \varphi\\ \hline \varphi \hspace{0.6em}\end{aligned} \; \nobreak \lnot \lnot \, \nobreak \mathrm{e.}$ |

同时有导出规则：
1. 取拒：$\begin{aligned} \varphi \to \psi\quad \lnot \psi\\ \hline \lnot \varphi \hspace{2em} \end{aligned} \; \nobreak \mathrm{MT}$
2. 反证：$\begin{aligned} \boxed{\begin{aligned} \lnot&\varphi\\ &\vdots\\ &\kern{-0.25em}\bot \end{aligned}}\\ \hline \varphi \phantom{a} \end{aligned} \; \nobreak \raisebox{-2.25em}{PBC} $
3. 排中：$\begin{aligned} \vphantom{a}\\ \hline \varphi \lor \lnot\varphi \end{aligned} \; \nobreak \mathrm{LEM}$

论证谬误（下面是错的）：
- $p \to q, q \vdash p$
- $p \to q, \lnot p \vdash \lnot q$

$\phi_{1}, \phi_{2}, \ldots, \phi_{n} \vdash \psi$ is valid iff $\phi_{1}, \phi_{2}, \ldots, \phi_{n} \models \psi$ holds. 前者是基于自然演绎规则的推导，后者是基于真值表的语义蕴涵。

<!-- {{{KaTeX 写自然演绎为何抽象 -->
<details>
<summary>KaTeX 写自然演绎为何抽象</summary>

其实不只是 $\KaTeX$，$\mathrm{MathJax},\, \LaTeX$ 也一样。

小调了下格式，总算能看了。

主要使用了 `\raisebox` `\hspace` `\kern` `\phantom` 等调间距等。

方框内多行怎么做到的呢，用了 `\boxed` 命令与 `aligned` 环境，即

```latex
\boxed{
    \begin{aligned}
        ...
    \end{aligned}
}
```

`\boxed` 里面 `aligned` 环境既使用 `&` 对齐，又使用了 `\kern` 细调间距以对齐。

横线右边的标记怎么跟横线差不多对齐的呢？对于上下都是单行的，直接放在环境外，基本就是对齐的。对于有个 `\boexed` 的，用了 `\raisebox` 命令调低位置，基本使用了 -2.3em。然后呢跟横线的间距，有的比较紧，也不知道原因，用了 `\;` 稍微右移了一下。

排中那里因为没条件，还用 `\phantom` 占了个位。

一开始用了很多 `\phantom` 来代替 `\raisebox` 和 `\hspace`，然而这样调整不够精细。

虽然最后成果挺不错的，但是要是使用 copy-tex 看源码的话，就会发现丑陋不堪，不同地方间距设置的也不一样。

!!! memo ""
    不知怎的，没复制过来。

    先解释一下流程，现在我写笔记一般是在 WSL，一个 Test 文件夹创一个 markdown 文件，一般叫 `a.md`，然后在里面写，写完复制回 Windows 上的笔记文件，然后清空写别的，或者直接 `rm` 掉。

    不知怎的，没复制过来，道法课尾声我去看博客的笔记，很奇怪怎么没对齐，一拖动发现很多 `\phantom`，再一看源文件，心脏骤停，`details` 里面还是「待续」，说明没复制过来，我哼哧哼哧调了好久的格式没了。

    回宿舍后用 Vim `undo` 功能，也不行，毕竟我是移除了文件，最后不匹配了，无法恢复，最多只能看 undohistory，看看能不能找回点什么。

    然后我看寄存器 `:registers`，寄存器 7 存了一部分，但不完整。不过好在我想起来装过 [coc-yank](https://github.com/neoclide/coc-yank)，果然找回来了，太感动了，爱死你了 coc。当然不确定是不是完整的，但是总比没的好。

</details>
<!-- }}} -->
