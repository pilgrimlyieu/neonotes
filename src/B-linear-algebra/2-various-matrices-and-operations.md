---
layout: post
title: 各式各样的矩阵及矩阵运算
date: 2023-11-05 12:26:17
updated: 2024-04-30 17:51:37
description: 《线性代数》笔记
draft: false
comments: true
disableNunjucks: true
katex: true
---

## 笔记

### 分块矩阵

#### 乘法

若 $\bm{A} = \begin{bmatrix} \bm{A}_{11} & \bm{A}_{12} & \cdots & \bm{A}_{1s} \\ \bm{A}_{21} & \bm{A}_{22} & \cdots & \bm{A}_{2s} \\ \vdots & \vdots & \ddots & \vdots \\ \bm{A}_{r1} & \bm{A}_{r2} & \cdots & \bm{A}_{rs} \\ \end{bmatrix}$，$\bm{B} = \begin{bmatrix} \bm{B}_{11} & \bm{B}_{12} & \cdots & \bm{B}_{1t} \\ \bm{B}_{21} & \bm{B}_{22} & \cdots & \bm{B}_{2t} \\ \vdots & \vdots & \ddots & \vdots \\ \bm{B}_{s1} & \bm{B}_{s2} & \cdots & \bm{B}_{st} \\ \end{bmatrix}$，则 $\bm{C}=\bm{A}\bm{B}=(\bm{C}_{kl})_{r \times t}$，其中

$$
\bm{C}_{kl} = \bm{A}_{k1}\bm{B}_{1l} + \bm{A}_{k2}\bm{B}_{2l} + \cdots + \bm{A}_{ks}\bm{B}_{sl} = \sum_{i=1}^s \bm{A}_{ki}\bm{B}_{il}
$$

若 $\bm{A} = \begin{bmatrix} \bm{A}_{11} & \bm{O} & \cdots & \bm{O} \\ \bm{A}_{21} & \bm{A}_{22} & \cdots & \bm{O} \\ \vdots & \vdots & \ddots & \vdots \\ \bm{A}_{n1} & \bm{A}_{n2} & \cdots & \bm{A}_{nn} \\ \end{bmatrix}$，则

$$
\left\lvert \bm{A}_{n \times n} \right\rvert = \left\lvert \bm{A}_{11} \right\rvert \left\lvert \bm{A}_{22} \right\rvert \cdots \left\lvert \bm{A}_{nn} \right\rvert = \prod_{i=1}^n \left\lvert \bm{A}_{ii} \right\rvert
$$

证明：

对 $\bm{A}$ 进行变换得 $\bm{A} = \begin{bmatrix} \bm{B}_{11} & \bm{O} & \cdots & \bm{O} \\ \bm{B}_{21} & \bm{B}_{22} & \cdots & \bm{O} \\ \vdots & \vdots & \ddots & \vdots \\ \bm{B}_{n1} & \bm{B}_{n2} & \cdots & \bm{B}_{nn} \\ \end{bmatrix}$，其中 $\bm{B}_{ii}$ 为下三角矩阵。

则 $\left\lvert \bm{A} \right\rvert =  \left\lvert \bm{B}_{11} \right\rvert \left\lvert \bm{B}_{22} \right\rvert \cdots \left\lvert \bm{B}_{nn} \right\rvert$，而 $\left\lvert \bm{A}_{ij} \right\rvert = \left\lvert \bm{B}_{ij} \right\rvert$，从而得证。

!!! tip ""
    这里的变换可不是瞎变换。

    具体而言，对对角线上某个矩阵 $A_{ii}$，对其进行行变换和列变换，会分别带动 $A_{i 1},\, \cdots ,\, A_{i, i-1}$ 和 $A_{i + 1, i},\, \cdots ,\, A_{ni}$（当然还有零矩阵，只不过变换对它们没有影响），只不过因为它们在三角形里面，所以没有影响。

#### 转置

若 $\bm{A} = \begin{bmatrix} \bm{A}_{11} & \bm{A}_{12} & \cdots & \bm{A}_{1s} \\ \bm{A}_{21} & \bm{A}_{22} & \cdots & \bm{A}_{2s} \\ \vdots & \vdots & \ddots & \vdots \\ \bm{A}_{r1} & \bm{A}_{r2} & \cdots & \bm{A}_{rs} \\ \end{bmatrix}$，则 $\bm{A}^{\intercal} = \begin{bmatrix} \bm{A}_{11}^{\intercal} & \bm{A}_{21}^{\intercal} & \cdots & \bm{A}_{r1}^{\intercal} \\ \bm{A}_{12}^{\intercal} & \bm{A}_{22}^{\intercal} & \cdots & \bm{A}_{r2}^{\intercal} \\ \vdots & \vdots & \ddots & \vdots \\ \bm{A}_{1s}^{\intercal} & \bm{A}_{2s}^{\intercal} & \cdots & \bm{A}_{rs}^{\intercal} \\ \end{bmatrix}$。

### 初等变换

1. **对调变换**：交换矩阵的两行（列），记为 $r_i \leftrightarrow r_j$（$c_i \leftrightarrow c_j$）。
2. **数乘变换**：把矩阵的某一行（列）乘以一个*非零常数* $k$，记为 $k r_i$（$k c_i$）。
3. **倍加变换**：把矩阵的某一行（列）的 $k$ 倍加到另一行（列）上，记为 $r_i + k r_j$（$c_i + k c_j$）。

单位矩阵 $\bm{E}$ 经过<u>一次初等变换</u>得到的矩阵称为**初等矩阵**。

1. **初等对调矩阵**：$\bm{E}(i, j)$
2. **初等倍乘矩阵**：$\bm{E}(i(k))$
3. **初等倍加矩阵**：$\bm{E}(i, j(k))$

!!! memo ""
    上面是「数乘」，这里又是「倍加」。。。

!!! info ""
    $$
    E(i, j(k)) = \left[ E(j, i(k)) \right]^\intercal
    $$

若矩阵 $\bm{A}$ 经过有限次初等变换得到矩阵 $\bm{B}$，则称 $\bm{A}$ 和 $\bm{B}$ **等价**，记为 $\bm{A} \to \bm{B}$。

显然，$\bm{A} \to \bm{B} \iff \bm{B} \to \bm{A}$。


### 梯形矩阵

!!! info 行梯形矩阵
    1. 若有零行，则零行在最下方。
    2. 从第一行起，每行第一个非零元素（主元）所在的列号逐行递增。

!!! info 行简化梯形矩阵
    1. 为行梯形矩阵。
    2. 主元为 $1$，且主元所在列的其他元素都为 $0$。

同理可定义*列梯形矩阵*和*列简化梯形矩阵*。

!!! info 标准形矩阵
    既为行简化梯形矩阵，又为列简化梯形矩阵。

    可记作

    $$
    \begin{bmatrix} \bm{E} & \bm{O} \\ \bm{O} & \bm{O} \end{bmatrix}
    $$

可知，解线性方程组时，将系数矩阵变为增广矩阵，原系数矩阵变为上三角矩阵时，增广矩阵即为行梯形矩阵；原系数矩阵变为单位矩阵时，即为行简化梯形矩阵。

!!! info 定理
    1. 对矩阵 $\bm{A}$ 进行有限次初等行变化，可以得到行简化梯形矩阵。
    2. 对矩阵 $\bm{A}$ 进行有限次初等列变化，可以得到列简化梯形矩阵。
    3. 对矩阵 $\bm{A}$ 进行有限次初等行变化和初等列变化，可以得到标准形矩阵。

### 伴随矩阵 & 逆矩阵

#### 伴随矩阵

!!! info 伴随矩阵
    设 $\bm{A} = \left[ a_{ij} \right]_n $ 为 $n$ 阶方阵，$A_{ij}$ 是 $a_{ij}$ 的代数余子式，则

    $$
    \bm{A}^* = \left[ A_{ij} \right]_n^\intercal
    $$

    称为 $\bm{A}$ 的**伴随矩阵**。

    易得

    $$
    \bm{A} \bm{A}^* = \bm{A}^* \bm{A} = \left\lvert \bm{A} \right\rvert \bm{E}
    $$

由此，我们可知 $\bm{A}^{-1}=\dfrac{\bm{A}^{*}}{\left\lvert A \right\rvert}$（$\bm{A}$ 可逆时）。

!!! note ""
    $$
    \left\lvert \bm{A}^{*} \right\rvert = \left\lvert \bm{A} \right\rvert^{n-1}
    $$

    证明：
    $$
    \begin{aligned}
        \left\lvert \bm{A}^{*} \right\rvert &= \left\lvert \left\lvert \bm{A} \right\rvert \bm{A}^{-1} \right\rvert \\
        &= \left\lvert \bm{A} \right\rvert^n \left\lvert \bm{A} \right\rvert^{-1} \\
        &= \left\lvert \bm{A} \right\rvert^{n-1}
    \end{aligned}
    $$

!!! note ""
    $$
    \left( \bm{A} \bm{B} \right)^{*} = \bm{B}^{*} \bm{A}^{*}
    $$

#### 逆矩阵

对 $n$ 阶方阵 $\bm{A}$，若存在 $n$ 阶方阵 $\bm{B}$，使 $\bm{A} \bm{B} = \bm{B} \bm{A} = \bm{E}$，则称 $\bm{A}$ 为**可逆矩阵**，$\bm{B}$ 为 $\bm{A}$ 的**逆矩阵**，记为 $\bm{A}^{-1}$。

证明一下若存在 $\bm{A} \bm{B} = \bm{C} \bm{A} = \bm{E}$，则 $\bm{B} = \bm{C}$。

$$
\begin{aligned}
    \bm{A} \bm{B} = \bm{C} \bm{A} = \bm{E} &\implies \bm{C} \bm{A} \bm{B} = \bm{C} \bm{E} \\
    &\implies (\bm{C} \bm{A}) \bm{B} = \bm{C} \\
    &\implies \bm{E} \bm{B} = \bm{C}\\
    &\implies \bm{B} = \bm{C}
\end{aligned}
$$

!!! note 逆矩阵的性质
    以下均假设 $\bm{A},\, \bm{B}$ 可逆。

    1. $\left( \bm{A}^{-1} \right)^{-1} = \bm{A}$
    2. $\left\lvert \bm{A}^{-1} \right\rvert = \left\lvert \bm{A} \right\rvert^{-1}$
    3. 若 $k\ne 0$，$\left( k \bm{A} \right)^{-1} = k^{-1} \bm{A}^{-1}$
    4. $\left( \bm{A}^\intercal \right)^{-1} = \left( \bm{A}^{-1} \right)^\intercal$
    5. $\left( \bm{A} \bm{B} \right)^{-1} = \bm{B}^{-1} \bm{A}^{-1}$

!!! note 初等矩阵的逆
    1. $\bm{E}^{-1}(i, j) = \bm{E}(i, j)$
    2. $\bm{E}^{-1}(i(k)) = \bm{E}(i(\frac{1}{k}))$
    3. $\bm{E}^{-1}(i, j(k)) = \bm{E}(i, j(-k))$

从而有

$$
\newcommand\iddots{\mathinner{\kern{1.2mu}\raisebox{2mu}{.}\kern{3mu}\raisebox{7.4mu}{.}\kern{3mu}\raisebox{12.8mu}{.}\kern{1.2mu}}}
\begin{aligned}
    \begin{bmatrix}
        \lambda_1 &   &   &   \\
          & \lambda_2 &   &   \\
          &   & \ddots &   \\
          &   &   & \lambda_n
    \end{bmatrix}^{-1}
    &=
    \begin{bmatrix}
        \lambda_1^{-1} &   &   &   \\
         & \lambda_2^{-1} &   &   \\
         &   & \ddots &   \\
         &   &   & \lambda_n^{-1}
    \end{bmatrix} \\
    \begin{bmatrix}
          &   &   & \lambda_1 \\
          &   & \lambda_2 &   \\
          & \iddots &   &   \\
        \lambda_n &   &   &
    \end{bmatrix}^{-1}
    &=
    \begin{bmatrix}
          &   &   & \lambda_n^{-1} \\
          &   & \iddots &   \\
          &   \lambda_2^{-1} &   &   \\
        \lambda_1^{-1} &   &   &
    \end{bmatrix}
\end{aligned}
$$

对一般的 $2 \times 2$ 矩阵，有

$$
\begin{bmatrix}
    a & b \\
    c & d
\end{bmatrix}^{-1} =
\dfrac{\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}}{ad-bc} = \dfrac{\begin{bmatrix} d & -b \\ -c & a \end{bmatrix}}{\begin{vmatrix} d & -b \\ -c & a \end{vmatrix}}
$$


!!! memo ""
    $\KaTeX$ 不支持 `\iddots`，参考 [StackExchange](https://math.meta.stackexchange.com/a/23276/1064518)，*稍*加修改：

    ```latex
    \newcommand\iddots{\mathinner{\kern{1.2mu}\raisebox{2mu}{.}\kern{3mu}\raisebox{7.4mu}{.}\kern{3mu}\raisebox{12.8mu}{.}\kern{1.2mu}}}
    ```
    原本是稍加修改，最后不满意效果，自己又调间距调了一个小时。

    想到高二时，调电子轨道表达式（是叫这个名字吧？）的 macro 的间距也是调了很久，最后没能弄出一个满意的效果，就勉强用着了。

    前阵子还试过重新调，结果还是没能令我满意，而且缩放还会改效果。

    这个矩阵的省略号，最后勉强算是和镜像重合了，见 [issue](https://github.com/KaTeX/KaTeX/issues/1223#issuecomment-1793610796) 的图。调过程中发现矩阵两侧高度不同，不管是正常还是我调的，而且位置也会影响，着实闹心。

    到此打住。

### 杂项

#### 零幂矩阵

!!! info 零幂矩阵
    若 $\exist_{k \in \N},\, \bm{J}^k = \bm{O}$，则称 $\bm{J}$ 为**幂零矩阵**。

    显然零幂矩阵是奇异矩阵。

    且有

    $$
    \left( \bm{E} - \bm{J} \right)^{-1} = \sum_{i=0}^{k - 1} \bm{J}^i
    $$

    证明：

    $$
    \begin{aligned}
        \left( \bm{E} - \bm{J} \right) \sum_{i=0}^{k - 1} \bm{J}^i &= \sum_{i=0}^{k - 1} \bm{J}^i - \sum_{i=1}^{k} \bm{J}^i \\
        &= \bm{J}^0 - \bm{J}^k \\
        &= \bm{E}
    \end{aligned}
    $$

#### 矩阵多项式

设 $f(x) = \displaystyle \sum_{i=0}^{n} a_i x^i$，$f(\bm{A}) = \bm{O}$，则 $f(t) \ne 0 \implies \bm{A} - t \bm{E}$ 可逆。

证明：

$f(\bm{A}) = \bm{O}$ 可得

$$
\left( \bm{A} - t \bm{E} \right)\left[ \sum_{i=1}^{n}\left( \sum_{j=i}^{n} t^{j - i}a_j \right)\bm{A}^{i - 1}  \right] + \bm{E} \sum_{k=0}^{n}t^k a_k = \bm{O}
$$

这起码是我一个月以前写的了，显然是跳步了，我也懒得检验或解释了。


总而言之，这一步就是将矩阵多项式提个公因式 $\bm{A} - t \bm{E}$。

!!! tip ""
    还是解释一下吧。$\bm{E}$ 可以看作 $\bm{A}^0$，从而可以看作是把多项式提出一个 $ax + b$ 的因式，外带一个常数项。

    例如 $x^4 + 8x^3 + 3x^2 + 6x + 2$，打算提出一个 $x + 1$，则形式应该为 $(x + 1)(ax^3 + bx^2 + cx + d) + e$。

    显然 $a = 1$，那么三次项就有了一个 $ax^3 = x^3$，还差 $8x^3 - x^3 = 7x^3$，由 $bx^2 \cdot  x$ 提供，则 $b = 7$。

    同理，$c = -4$，$d = 10$，$e = -8$。

    也即 $x^4 + 8x^3 + 3x^2 + 6x + 2 = (x + 1)(x^3 + 7x^2 - 4x + 10) - 8$。

随即若 $f(t) = \displaystyle \sum_{k=0}^{n} t^k a_k \ne 0$，则有

$$
\left( \bm{A} - t \bm{E} \right)^{-1} = - \dfrac{1}{f(t)} \sum_{i=1}^{n}\left( \sum_{j=i}^{n} t^{j - i}a_j \right)\bm{A}^{i - 1}
$$

!!! tip ""
    这个命题不满足等价。也即 $\bm{A} - t \bm{E}$ 可逆 $\nimplies  f(t) \ne 0$。

    例如 $f(x) = x^2 - 3x + 2$，$\bm{A} = 2 \bm{E}$ 满足 $f(\bm{A}) = \bm{O}$，而且 $t = 1$  时 $\bm{A} - t \bm{E} = \bm{E}$ 可逆，但 $f(1) = 0$。

!!! memo ""
    上面这个 tip 用了我自己一个宏来表示「无法推出」，定义为 `\mathbin{\kern13mu\not\kern-13mu\implies}`，然而导致博文后面的内容都无法显示，原因不明。

    上一次出现这个问题还是因为我用了 `\fcolorbox`，我以为是里面的 `$ ... $` 的问题，把 `\fcolorbox` 换成了 `\boxed` 就解决了，不过就没了人教版教科书那样定理的颜色边框。而这次比较神奇。

    `\mathbin` 出自 [Class Assignment](https://katex.org/docs/supported.html#style-color-size-and-font)，意思是指明这个为 binary，也即「二元运算符」。看来是不可以在里面使用 [Spacing](https://katex.org/docs/supported.html#overlap-and-spacing)，我大致试了几个都不行。然而有例外，比如 `\par` 的定义是 `\mathbin{/\kern-5mu/}`，但是可以正常显示，如 $\mathbin{/\kern-5mu/}$（这个用的不是宏，而是直接输入）。于是我猜测是不可以同时有 `\not`。

    真糟心，于是我只好把 Blog 的 `\mathbin` 全删了。

#### 矩阵的分解

设 $\bm{A}$ 为 $m \times n$ 矩阵，$\rank(\bm{A}) = r$，则存在 $m$ 阶可逆矩阵 $\bm{P}$ 和 $n$ 阶可逆矩阵 $\bm{Q}$，使 $\bm{A} = \bm{P} \bm{\Lambda} \bm{Q}$，其中

$$
\bm{\Lambda} = \begin{bmatrix}
    \bm{E}_r & \bm{O} \\
    \bm{O} & \bm{O}
\end{bmatrix}
$$

## 后记

这是本篇博文唯一一个二级标题，正文的二级标题我不知道怎么取，就干脆不要二级标题了（正文我一般不用一级标题，一级标题我一般默认为标题，除了「记事板」，一级标题作为年份）。

!!! memo 2023 年国家公祭日记
    重新整理博客结构时，为了使目录不要太抽象，补了一个二级标题「笔记」在上面。

这篇看起来好像没啥特别的。实际上就内容而言确实，但是却特殊在本篇内容是我完全在 WSL 上完成的。

效率有提高吗？似乎没有，预览速度感觉差不多，也是内容一多就卡；UltiSnips 一开始的 Tabstop 似乎流畅了一点，也不知道是不是错觉，只不过到后面写多了还是会出现 Tabstop 迟滞、乱跳的现象。

不过我敢肯定写 $\LaTeX$ 效率绝对是会快一点的。其一，我自己也测试过了，WSL 的 $\LaTeX$ 编译速度比 Windows 快多了；其二，写 $\LaTeX$ coc 会给补全提示，WSL 下补全菜单性能比 Windows 好多了，Windows 下遍历选项延迟非常明显，而 WSL 流畅多了。

WSL 还有点不同就是我开了 conceal，gVim 我是关着的，因为不知道为什么，一些字符无法显示，WSL 因为在终端就没问题。

效率下降的点也是有的。由于我的 `WSLVim.ahk` 的缺陷，我无法区分单独的 `r` 模式与 Normal 模式，导致如果简单替换一个汉字，WSL 还是得切语言，而且换完后还得切回来，这点确实是 gVim 比较厉害的。

至于双拼，大概现在只比以前全拼慢一点了吧，多熟练熟练。不过非常气愤的是 `f: en` `g: eng` `h: ang` `j: an` 这四个韵母是我比较早就记住了的，但是呢还是老是打错（不是因为分不清楚，我普通话还算可以的吧，大部分我还是分得清楚的，主要是要打时老是要停下来想一想）。

还有一点，Windows 终端下新版输入法，我双拼如果打了很长还没选，发现前面打错了，左右键移动看不到光标的移动，导致我只能盲猜，或者删了重打。我估计全拼也有这个问题，只不过双拼格外严重，因为我开了自动展开，导致我删错一个，后面就模样大变了，我也猜不出删了哪个。

由于后面的笔记与本篇关联性稍有下降（这篇主要是杂七杂八的定义和犄角旮旯的笔记，后面大的要来了，秩有一堆东西，还有高斯消元法什么的），再加上本篇内容也比较长了，要是要预览就得注释一部分了，所以我就另开了一篇。

如图所示，便是我写笔记的布局了。

![](2-various-matrices-and-operations/layout.png)

开两个浏览器，一个大概 2/3 屏预览，一个全屏查资料（比如我现在开着的就是 $\KaTeX$ 函数大全，查一些可能忘记了的命令。

WSL 运行在 Windows Terminal 上，大概占 1/3 屏。

开个 `_posts` 文件夹，或是方便打开 gVim 或是看看以前的博文，或是弄些图片，或是给 `_imagecompression.py` 加个新文件夹什么的。

写完后，一般流程就是 <kbd>Win</kbd> + <kbd>T</kbd> 打开终端（也可以在 WSL 那里 <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>3</kbd>，只不过就会有 UAC 了），然后直接一个 `bpb`（blog publish），或者有时候想看看在博客的效果，用 `blk`（blog look）。

然后 <kbd>Win</kbd> + <kbd>R</kbd> 输入 `code` 回车，打开 Blog 项目，commit 更新的内容，然后 push。

有时候开个小差，也可以用第二个浏览器去看点别的内容，或者打开 QQ 微信看看。

目前我对这套流程还是挺满意的，写笔记成为一个享受。~~然而今日午睡起来后，又玩手机玩了一个多小时才下床继续写~~。

可能会发现最近的笔记逻辑性比较差，不仅少了些必要的证明，也少了很多我个人的见解，因为我课本笔记都随便记的，这里一块那里一块，加上老师不是按课本讲的（课本那定义一个比一个抽象，像行列式、秩），而且已经过去蛮长时间了，我也记不清楚了，所以就只能这样了。

这便是临时抱佛脚的恶果吗。
