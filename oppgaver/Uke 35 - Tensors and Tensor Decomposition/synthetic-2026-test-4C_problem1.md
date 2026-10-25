### **Problem 1** (Tensor notation, outer products and rank, 8 points)

The 3-tensor $\mathbf{X}\in\mathbb{R}^{2\times 2\times 2}$ is given by its two frontal slices

$$X_{::1}=\begin{pmatrix}1&1\\ 0&0\end{pmatrix},\qquad X_{::2}=\begin{pmatrix}0&0\\ 1&2\end{pmatrix},$$

i.e. $x_{i,j,1}$ and $x_{i,j,2}$ are the entries in position $(i,j)$ of $X_{::1}$ and $X_{::2}$ respectively.

a) State the order and the dimensions of $\mathbf{X}$ and the number of entries it has. Say what the column fibers $x_{:jk}\in\mathbb{R}^{2}$ of $\mathbf{X}$ are and list all four of them.

b) For matrices $A\in\mathbb{R}^{m\times r}$, $B\in\mathbb{R}^{n\times r}$, $C\in\mathbb{R}^{p\times r}$ the tensor $[\![A,B,C]\!]$ has entries $x_{i,j,k}=\sum_{s=1}^{r}a_{i,s}b_{j,s}c_{k,s}$. Show that the given $\mathbf{X}$ equals $[\![A,B,C]\!]$ for

$$A=\begin{pmatrix}1&0\\ 0&1\end{pmatrix},\qquad B=\begin{pmatrix}1&1\\ 1&2\end{pmatrix},\qquad C=\begin{pmatrix}1&0\\ 0&1\end{pmatrix}.$$

c) The rank of a tensor is the smallest number of rank-1 tensors (outer products $\mathbf{a}\circledast\mathbf{b}\circledast\mathbf{c}$ with entries $a_ib_jc_k$) that sum to it. From b), what is an upper bound for the rank of $\mathbf{X}$? Argue that $\mathbf{X}$ itself is not a rank-1 tensor and state its rank.

d) For $\mathbf{X}\in\mathbb{R}^{m\times n\times p}$: how many numbers do we store if we keep (i) all entries of $\mathbf{X}$, (ii) a rank-$r$ representation $[\![A,B,C]\!]$ via the three factor matrices? What inequality between $r$, $m$, $n$, $p$ must hold for (ii) to save storage, and how many numbers does a rank-$10$ representation of a $100\times 100\times 25$ tensor save against storing all entries?
