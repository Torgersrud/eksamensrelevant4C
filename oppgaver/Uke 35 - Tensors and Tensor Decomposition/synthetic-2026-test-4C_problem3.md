### **Problem 3** (Matricization and k-mode products, 10 points)

The tensor $\mathbf{X}\in\mathbb{R}^{2\times 2\times 2}$ is given by its frontal slices

$$X_{::1}=\begin{pmatrix}1&2\\ 3&4\end{pmatrix},\qquad X_{::2}=\begin{pmatrix}5&6\\ 7&8\end{pmatrix}.$$

Recall the mode-$m$ matricization $\mathbf{X}^{(m)}\in\mathbb{R}^{n_m\times(n\cdot n/n_m)}$ from the lectures: the entry $x_{i_1,i_2,i_3}$ becomes $a_{i_m,j}$ with $j=1+\sum_{k\neq m}(i_k-1)\prod_{l\neq m,\,l<k}n_l$, i.e. the remaining indices run through their values in order, first index fastest.

a) Write down the three matricizations $\mathbf{X}^{(1)}$, $\mathbf{X}^{(2)}$ and $\mathbf{X}^{(3)}$.

b) For a matrix $M\in\mathbb{R}^{m\times n_3}$ the mode-3 product $Y=\mathbf{X}\times_3 M$ is defined by $y_{i,j,l}=\sum_{k}x_{i,j,k}\,m_{l,k}$, equivalently $Y^{(3)}=MX^{(3)}$. Compute $Y=\mathbf{X}\times_3 M$ for $M=\begin{pmatrix}1&0\\ 1&1\end{pmatrix}$ as its two frontal slices, and verify $Y^{(3)}=MX^{(3)}$ with your answer from a).

c) Compute $Z=\mathbf{X}\times_2\mathbf{v}$ for the row vector $\mathbf{v}^{\top}=(1,-1)$, a $2\times 2$ matrix with entries $z_{i,k}=\sum_j x_{i,j,k}v_j$. What does $Z$ compute column by column?

d) Recall the relation between the CP form and matricizations: for $\mathbf{X}=[\![A,B,C]\!]$ one has $\mathbf{X}^{(1)}=A(C\odot B)^{\top}$. For

$$A=\begin{pmatrix}1&0\\ 1&1\end{pmatrix},\qquad B=\begin{pmatrix}1&1\\ 1&2\end{pmatrix},\qquad C=\begin{pmatrix}1&0\\ 0&1\end{pmatrix},$$

compute $\mathbf{X}^{(1)}$ using this relation, without writing out the tensor $\mathbf{X}$ itself.
