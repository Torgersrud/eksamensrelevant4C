### **Solution to Problem 1** (Tensor notation, outer products and rank, 8 points)

a) $\mathbf{X}$ is a $3$-tensor (order $3$) with dimensions $2\times 2\times 2$ and $2\cdot 2\cdot 2=8$ entries. (1 P.)

The column fibers are obtained by fixing the second and third indices and running through the first: $x_{:jk}=(x_{1,j,k},x_{2,j,k})^{\top}\in\mathbb{R}^{2}$. Reading the entries off the slices,

$$x_{:11}=\begin{pmatrix}1\\ 0\end{pmatrix},\quad x_{:21}=\begin{pmatrix}1\\ 0\end{pmatrix},\quad x_{:12}=\begin{pmatrix}0\\ 1\end{pmatrix},\quad x_{:22}=\begin{pmatrix}0\\ 2\end{pmatrix}.$$ (1 P.)

b) Here the columns are $\mathbf{a}_1=\mathbf{c}_1=(1,0)^{\top}$, $\mathbf{a}_2=\mathbf{c}_2=(0,1)^{\top}$, $\mathbf{b}_1=(1,1)^{\top}$, $\mathbf{b}_2=(1,2)^{\top}$, and since $c_{k,1}=\begin{cases}1&k=1\\ 0&k=2\end{cases}$ and $c_{k,2}=\begin{cases}0&k=1\\ 1&k=2\end{cases}$ the sum collapses in each frontal slice:

$$X_{::1}=\mathbf{a}_1\mathbf{b}_1^{\top}=\begin{pmatrix}1\\ 0\end{pmatrix}\begin{pmatrix}1&1\end{pmatrix}=\begin{pmatrix}1&1\\ 0&0\end{pmatrix},\qquad X_{::2}=\mathbf{a}_2\mathbf{b}_2^{\top}=\begin{pmatrix}0\\ 1\end{pmatrix}\begin{pmatrix}1&2\end{pmatrix}=\begin{pmatrix}0&0\\ 1&2\end{pmatrix},$$

which are exactly the given slices, so $x_{i,j,k}=\sum_{s=1}^{2}a_{i,s}b_{j,s}c_{k,s}$. (One may equally check the eight entries one by one, e.g. $x_{2,2,2}=a_{2,1}b_{2,1}c_{2,1}+a_{2,2}b_{2,2}c_{2,2}=0\cdot 1\cdot 0+1\cdot 2\cdot 1=2$.) (2 P.)

c) $[\![A,B,C]\!]=\mathbf{a}_1\circledast\mathbf{b}_1\circledast\mathbf{c}_1+\mathbf{a}_2\circledast\mathbf{b}_2\circledast\mathbf{c}_2$ is a sum of two rank-1 tensors, so $\operatorname{rank}(\mathbf{X})\leq 2$. (1 P.)

If $\mathbf{X}=\mathbf{a}\circledast\mathbf{b}\circledast\mathbf{c}$ were rank-1, then every frontal slice would be a multiple of the same matrix $\mathbf{a}\mathbf{b}^{\top}$, namely $X_{::k}=c_k\,\mathbf{a}\mathbf{b}^{\top}$. The two given slices are both non-zero, so they would have to be scalar multiples of each other — but $X_{::2}=\lambda X_{::1}$ would require $1=\lambda\cdot 0$, impossible. Hence $\mathbf{X}$ has rank exactly $2$. (1 P.)

d) (i) All entries: $mnp$ numbers. (ii) Factor matrices: $rm+rn+rp=r(m+n+p)$ numbers. (1 P.)

The representation $[\![A,B,C]\!]$ saves storage when $r(m+n+p)<mnp$. For $m=n=100$, $p=25$, $r=10$ we compare $100\cdot 100\cdot 25=250\,000$ entries against $10\cdot(100+100+25)=2\,250$ numbers, a saving of $247\,750$ numbers (less than one percent of the full storage). (1 P.)
