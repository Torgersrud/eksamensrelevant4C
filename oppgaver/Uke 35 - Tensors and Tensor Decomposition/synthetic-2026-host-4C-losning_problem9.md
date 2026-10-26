### **Solution to Problem 9** (Kronecker and Khatri–Rao products at work: mixed products, Grams and selections, 8 points)

a) Block by block, $A\otimes B=(a_{ij}B)$ with $a_{11}=1$, $a_{12}=2$, $a_{21}=0$, $a_{22}=1$:

$$A\otimes B=\begin{pmatrix}1&0&2&0\\ 2&1&4&2\\ 0&3&0&6\\ 0&0&1&0\\ 0&0&2&1\\ 0&0&0&3\end{pmatrix},\qquad C\otimes D=\begin{pmatrix}0&2&0&1\\ 2&4&1&2\\ 0&1&0&0\\ 1&2&0&0\end{pmatrix}.$$

Multiplying the $6\times4$ by the $4\times4$ matrix,

$$(A\otimes B)(C\otimes D)=\begin{pmatrix}0&4&0&1\\ 4&16&1&4\\ 12&24&3&6\\ 0&1&0&0\\ 1&4&0&0\\ 3&6&0&0\end{pmatrix}.$$

On the other side, $AC=\begin{pmatrix}1&2\\ 0&1\end{pmatrix}\begin{pmatrix}2&1\\ 1&0\end{pmatrix}=\begin{pmatrix}4&1\\ 1&0\end{pmatrix}$ and $BD=\begin{pmatrix}1&0\\ 2&1\\ 0&3\end{pmatrix}\begin{pmatrix}0&1\\ 1&2\end{pmatrix}=\begin{pmatrix}0&1\\ 1&4\\ 3&6\end{pmatrix}$, so

$$(AC)\otimes(BD)=\begin{pmatrix}4\cdot BD & 1\cdot BD\\ 1\cdot BD & 0\cdot BD\end{pmatrix}=\begin{pmatrix}0&4&0&1\\ 4&16&1&4\\ 12&24&3&6\\ 0&1&0&0\\ 1&4&0&0\\ 3&6&0&0\end{pmatrix}.$$

The two computations agree. The general law is the **mixed-product property**

$$(A\otimes B)(C\otimes D)=(AC)\otimes(BD),$$

and it holds whenever $A$ and $C$, and $B$ and $D$, are multiplyable in that order: for $A\in\mathbb{R}^{m\times n}$, $C\in\mathbb{R}^{n\times r}$, $B\in\mathbb{R}^{p\times q}$, $D\in\mathbb{R}^{q\times s}$ both sides are $mp\times rs$. (2 P.)

b) Column $r$ of $A\odot B$ is $\mathbf{a}_r\otimes\mathbf{b}_r$:

$$A\odot B=\begin{pmatrix}1&0\\ 2&2\\ 0&6\\ 0&0\\ 0&1\\ 0&3\end{pmatrix},\qquad (A\odot B)^{\top}(A\odot B)=\begin{pmatrix}5&4\\ 4&50\end{pmatrix}.$$

The factor Grams are $A^{\top}A=\begin{pmatrix}1&2\\ 2&5\end{pmatrix}$ (columns $(1,0)$, $(2,1)$: $\|\mathbf{a}_1\|^2=1$, $\mathbf{a}_1\cdot\mathbf{a}_2=2$, $\|\mathbf{a}_2\|^2=5$) and $B^{\top}B=\begin{pmatrix}5&2\\ 2&10\end{pmatrix}$, so the Hadamard product gives

$$(A^{\top}A)\circ(B^{\top}B)=\begin{pmatrix}1\cdot5&2\cdot2\\ 2\cdot2&5\cdot10\end{pmatrix}=\begin{pmatrix}5&4\\ 4&50\end{pmatrix}=(A\odot B)^{\top}(A\odot B).$$

Entrywise the identity reads $(\mathbf{a}_s\otimes\mathbf{b}_s)\cdot(\mathbf{a}_t\otimes\mathbf{b}_t)=(\mathbf{a}_s\cdot\mathbf{a}_t)(\mathbf{b}_s\cdot\mathbf{b}_t)$; e.g. the off-diagonal entry is $(\mathbf{a}_1\cdot\mathbf{a}_2)(\mathbf{b}_1\cdot\mathbf{b}_2)=2\cdot2=4$, and $\|\mathbf{a}_1\otimes\mathbf{b}_1\|^2=1\cdot5=5$, $\|\mathbf{a}_2\otimes\mathbf{b}_2\|^2=5\cdot10=50$ ✓. A nonzero off-diagonal entry means the two rank-$1$ components are *not* orthogonal — the design matrix $C\odot B$ of the ALS least-squares problem is column-correlated, so the components compete for the same part of the data. In Problem 5 c) the factor columns were pairwise orthogonal (both Grams diagonal), which made $M^{\top}M$ diagonal and the mode-$1$ solve trivial; here the $2\times2$ system $\begin{pmatrix}5&4\\ 4&50\end{pmatrix}$ is genuinely coupled. (2 P.)

c) Working columnwise (the $12$-vectors stack $i$ fastest, then $j$, then $k$), with columns $\mathbf{a}_r\in\mathbb{R}^2$, $\mathbf{b}_r\in\mathbb{R}^3$, $\mathbf{c}_r\in\mathbb{R}^2$:

$$(C\odot B)\odot A=\Big((\mathbf{c}_1\otimes\mathbf{b}_1)\otimes\mathbf{a}_1\ \ (\mathbf{c}_2\otimes\mathbf{b}_2)\otimes\mathbf{a}_2\Big),\qquad C\odot(B\odot A)=\Big(\mathbf{c}_1\otimes(\mathbf{b}_1\otimes\mathbf{a}_1)\ \ \mathbf{c}_2\otimes(\mathbf{b}_2\otimes\mathbf{a}_2)\Big).$$

Column $1$: $\mathbf{c}_1\otimes\mathbf{b}_1\otimes\mathbf{a}_1=(2,1)^{\top}\otimes(1,2,0)^{\top}\otimes(1,0)^{\top}=(2,0,4,0,0,0,\;1,0,2,0,0,0)^{\top}$, and both groupings produce this same vector; column $2$: $\mathbf{c}_2\otimes\mathbf{b}_2\otimes\mathbf{a}_2=(1,0)^{\top}\otimes(0,1,3)^{\top}\otimes(2,1)^{\top}=(0,0,2,1,6,3,\;0,0,0,0,0,0)^{\top}$, again identically for both groupings — the Khatri–Rao product is associative. These columns are exactly $\operatorname{vec}(\mathbf{a}_r\circledast\mathbf{b}_r\circledast\mathbf{c}_r)$: e.g. the rank-$1$ tensor $\mathbf{a}_1\circledast\mathbf{b}_1\circledast\mathbf{c}_1$ has its only nonzero entries at $(i,j,k)=(1,1,1),(1,2,1),(1,1,2),(1,2,2)$ with values $2,4,1,2$, which in $i$-fastest order land in positions $1,3,7,9$ — the support of column $1$ above. This is the mechanism of $\mathbf{X}^{(1)}=A(C\odot B)^{\top}$: column $r$ of $C\odot B$ is the unfolded rank-$1$ piece $(k,j)$-wise, so multiplying by $A$ recombines the unfolded rank-$1$ tensors with the mixing weights $\mathbf{a}_{\cdot r}$, which is exactly what the CP sum $\sum_r\mathbf{a}_r\circledast\mathbf{b}_r\circledast\mathbf{c}_r$ does. (2 P.)

d) $\mathbf{a}_1\otimes\mathbf{b}_1$ is column $1$ of $A\otimes B$ and $\mathbf{a}_2\otimes\mathbf{b}_2$ is column $4$: block column $j$ of $A\otimes B$ holds $\big(\text{col}_j(A)\big)\otimes B$'s pieces — its columns are $\mathbf{a}_j\otimes(\text{col of }B)$ — so the diagonal block $(j,r=j)$ column is $\mathbf{a}_j\otimes\mathbf{b}_j$. With $p$ rows in $B$ and $n$ columns each, column $r$ of $M\odot N$ is column $(r-1)p+r$ of $M\otimes N$: only $n$ of the $n^2$ block columns are used. Sizes: $M\otimes N$ has $(mp)(n^2)=mp\,n^2$ entries against $mp\,n$ for $M\odot N$ — a waste factor of $n$; for $m=200$, $p=300$, $n=8$ that is $600\times64=38\,400$ entries against $600\times8=4\,800$, i.e. $8$ times as many numbers for products that are then discarded. An ALS implementation needs neither product explicitly: the normal equations only ask for $(C\odot B)^{\top}(C\odot B)=(C^{\top}C)\circ(B^{\top}B)$, assembled from two $r\times r$ Grams (b)), and right-hand sides like $\mathbf{Y}^{(1)}(C\odot B)$ are evaluated as unfoldings/contractions without ever materialising the Khatri–Rao matrix. (2 P.)
