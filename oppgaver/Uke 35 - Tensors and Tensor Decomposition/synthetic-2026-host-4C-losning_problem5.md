### **Solution to Problem 5** (Rank-1 pieces and a CP fit by least squares, 8 points)

a) The outer product $\mathbf{a}\circledast\mathbf{b}\circledast\mathbf{c}$ has frontal slices $c_k\,\mathbf{a}\mathbf{b}^{\top}$, so with $\mathbf{a}_1=(1,3)^{\top}$, $\mathbf{b}_1=(1,1,0)^{\top}$, $\mathbf{c}_1=(1,1)^{\top}$:

$$(R_1)_{::1}=1\cdot\mathbf{a}_1\mathbf{b}_1^{\top}=\begin{pmatrix}1\\3\end{pmatrix}\begin{pmatrix}1&1&0\end{pmatrix}=\begin{pmatrix}1&1&0\\ 3&3&0\end{pmatrix},\qquad
(R_1)_{::2}=1\cdot\mathbf{a}_1\mathbf{b}_1^{\top}=\begin{pmatrix}1&1&0\\ 3&3&0\end{pmatrix},$$

and with $\mathbf{a}_2=(2,1)^{\top}$, $\mathbf{b}_2=(1,-1,1)^{\top}$, $\mathbf{c}_2=(1,-1)^{\top}$:

$$(R_2)_{::1}=1\cdot\mathbf{a}_2\mathbf{b}_2^{\top}=\begin{pmatrix}2&-2&2\\ 1&-1&1\end{pmatrix},\qquad
(R_2)_{::2}=(-1)\cdot\mathbf{a}_2\mathbf{b}_2^{\top}=\begin{pmatrix}-2&2&-2\\ -1&1&-1\end{pmatrix}.$$

Adding slice by slice gives

$$R_1+R_2\ \text{slice }1=\begin{pmatrix}3&-1&2\\ 4&2&1\end{pmatrix},\qquad
R_1+R_2\ \text{slice }2=\begin{pmatrix}-1&3&-2\\ 2&4&-1\end{pmatrix},$$

which are exactly $Y_{::1}$ and $Y_{::2}$. Hence $\mathbf{Y}=[\![A,B,C]\!]$ is a sum of two rank-1 tensors, and
$\operatorname{rank}(\mathbf{Y})\le 2$. (2 P.)

b) The columns $1$ and $2$ of $Y_{::1}$ span a $2\times 2$ minor with determinant $3\cdot 2-(-1)\cdot 4=10\neq 0$, so $Y_{::1}$ has matrix rank $2$. If $\mathbf{Y}$ were rank $1$, say $\mathbf{Y}=\mathbf{a}\circledast\mathbf{b}\circledast\mathbf{c}$, every frontal slice would be $c_k\mathbf{a}\mathbf{b}^{\top}$, a matrix of rank at most $1$; a slice of rank $2$ is therefore impossible, so $\operatorname{rank}(\mathbf{Y})\neq 1$. Together with a), $\operatorname{rank}(\mathbf{Y})=2$. (1 P.)

c) The Khatri–Rao product stacks the Kronecker products of corresponding columns, $M=C\odot B=\begin{pmatrix}\mathbf{c}_1\otimes\mathbf{b}_1&\mathbf{c}_2\otimes\mathbf{b}_2\end{pmatrix}$:

$$M=\begin{pmatrix}1&1\\ 1&-1\\ 0&1\\ 1&-1\\ 1&1\\ 0&-1\end{pmatrix},\qquad
M^{\top}M=\begin{pmatrix}4&0\\ 0&6\end{pmatrix}.$$

The two factors give the same Gram matrix through the Hadamard identity: $C^{\top}C=\begin{pmatrix}2&0\\0&2\end{pmatrix}$ (the columns of $C$ are orthogonal of squared length $2$) and $B^{\top}B=\begin{pmatrix}2&0\\0&3\end{pmatrix}$ (orthogonal too, $\mathbf{b}_1\cdot\mathbf{b}_2=1-1+0=0$), so

$$(C^{\top}C)\circ(B^{\top}B)=\begin{pmatrix}2\cdot2&0\\0&2\cdot3\end{pmatrix}=\begin{pmatrix}4&0\\0&6\end{pmatrix}=M^{\top}M.$$

The mode-$1$ matricization collects the fibers $y_{:jk}$ as columns, second index first:

$$\mathbf{Y}^{(1)}=\begin{pmatrix}3&-1&2&-1&3&-2\\ 4&2&1&2&4&-1\end{pmatrix},\qquad
\mathbf{Y}^{(1)}M=\begin{pmatrix}4&12\\ 12&6\end{pmatrix}.$$

Because the objective is a sum of squares over the rows of $A$, each row of $A$ solves an ordinary least-squares problem, and the normal equations are

$$A\,M^{\top}M=\mathbf{Y}^{(1)}M\qquad\Longrightarrow\qquad
A=\mathbf{Y}^{(1)}M\,(M^{\top}M)^{-1}=\begin{pmatrix}4&12\\ 12&6\end{pmatrix}\begin{pmatrix}\tfrac14&0\\[2pt] 0&\tfrac16\end{pmatrix}=\begin{pmatrix}1&2\\ 3&1\end{pmatrix}.$$

(The Gram matrix is invertible — its diagonal entries are $|c_s|^2|b_s|^2>0$ — so the minimiser is unique.) This is exactly the matrix $A$ given in the problem. Multiplying back,

$$A M^{\top}=\begin{pmatrix}1&2\\ 3&1\end{pmatrix}\begin{pmatrix}1&1&0&1&1&0\\ 1&-1&1&-1&1&-1\end{pmatrix}=\begin{pmatrix}3&-1&2&-1&3&-2\\ 4&2&1&2&4&-1\end{pmatrix}=\mathbf{Y}^{(1)},$$

so the residual $\big\|\mathbf{Y}^{(1)}-A(C\odot B)^{\top}\big\|_F=0$: the ALS step does not have to approximate anything, it recovers the exact rank-$2$ representation found in a). (3 P.)

d) Full storage: $2\cdot 3\cdot 2=12$ entries. Rank-$2$ factor storage: $2(2+3+2)=14$ numbers — the CP form is *larger* than the tensor itself, so it does not pay off for a cube this small. In general, for an $n_1\times\cdots\times n_d$ tensor at rank $r$,

$$\text{factors save storage}\quad\Longleftrightarrow\quad r\,(n_1+\cdots+n_d)<n_1\cdots n_d .$$

For a $120\times 100\times 60$ tensor at rank $20$: $120\cdot100\cdot 60=720\,000$ entries against
$20(120+100+60)=20\cdot 280=5\,600$ numbers, a ratio of $720\,000/5\,600=900/7\approx 129$ — the factor form uses less than one percent of the full storage. (2 P.)
