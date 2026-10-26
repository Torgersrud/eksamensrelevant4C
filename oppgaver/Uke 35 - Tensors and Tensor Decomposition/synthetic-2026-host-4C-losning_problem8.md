### **Solution to Problem 8** (Unfolding identities for rank-one, CP and multilinear maps, 8 points)

a) The slices of a rank-one tensor are $\mathbf{a}\mathbf{b}^{\top}$ scaled by the corresponding entry of $\mathbf{c}$. With

$$\mathbf{a}\mathbf{b}^{\top}=\begin{pmatrix}1&0&-1\\ 2&0&-2\end{pmatrix},\qquad c_1=2,\ c_2=1,$$

the slices are $X_{::1}=\begin{pmatrix}2&0&-2\\ 4&0&-4\end{pmatrix}$ and $X_{::2}=\begin{pmatrix}1&0&-1\\ 2&0&-2\end{pmatrix}$. Reading the unfoldings with the first remaining index fastest:

$$\mathbf{X}^{(1)}=\begin{pmatrix}2&0&-2&1&0&-1\\ 4&0&-4&2&0&-2\end{pmatrix},\quad \mathbf{X}^{(2)}=\begin{pmatrix}2&4&1&2\\ 0&0&0&0\\ -2&-4&-1&-2\end{pmatrix},\quad \mathbf{X}^{(3)}=\begin{pmatrix}2&4&0&0&-2&-4\\ 1&2&0&0&-1&-2\end{pmatrix}.$$

The three Kronecker products (left factor = slowest remaining index) are

$$\mathbf{c}\otimes\mathbf{b}=\begin{pmatrix}2\\0\\-2\\1\\0\\-1\end{pmatrix},\qquad \mathbf{c}\otimes\mathbf{a}=\begin{pmatrix}2\\4\\1\\2\end{pmatrix},\qquad \mathbf{b}\otimes\mathbf{a}=\begin{pmatrix}1\\2\\0\\0\\-1\\-2\end{pmatrix},$$

and the outer products give exactly the unfoldings above: $\mathbf{a}(\mathbf{c}\otimes\mathbf{b})^{\top}$ has first row $\mathbf{c}\otimes\mathbf{b}$ and second row twice that, matching $\mathbf{X}^{(1)}$; $\mathbf{b}(\mathbf{c}\otimes\mathbf{a})^{\top}$ has rows $1$, $0$, $-1$ times $(2,4,1,2)$, matching $\mathbf{X}^{(2)}$; $\mathbf{c}(\mathbf{b}\otimes\mathbf{a})^{\top}$ has rows $2$ and $1$ times $(1,2,0,0,-1,-2)$, matching $\mathbf{X}^{(3)}$. (This is no coincidence: in a rank-one tensor every column of $\mathbf{X}^{(1)}$ is a multiple of $\mathbf{a}$, and the multipliers run over $(\mathbf{c}\otimes\mathbf{b})$ in the column order of the unfolding.) (2 P.)

For the norm, $\|\mathbf{X}\|_F^2=(4+4+16+16)+(1+1+4+4)=40+10=50$, and $\|\mathbf{a}\|^2\|\mathbf{b}\|^2\|\mathbf{c}\|^2=5\cdot 2\cdot 5=50$ — the entries of $\mathbf{X}$ are all products $a_ib_jc_k$, so the sum of squares factors. (1 P.)

b) Each slice is $X_{::k}=\sum_r c_{kr}\,\mathbf{a}_r\mathbf{b}_r^{\top}$ with $\mathbf{a}_1\mathbf{b}_1^{\top}=\begin{pmatrix}1&0&1\\ 0&0&0\end{pmatrix}$ and $\mathbf{a}_2\mathbf{b}_2^{\top}=\begin{pmatrix}2&4&0\\ 1&2&0\end{pmatrix}$. The rows of $C$ are $\mathbf{c}_1^{\top}=(1,0)$ and $\mathbf{c}_2^{\top}=(1,1)$, so

$$X_{::1}=\begin{pmatrix}1&0&1\\ 0&0&0\end{pmatrix},\qquad X_{::2}=\mathbf{a}_1\mathbf{b}_1^{\top}+\mathbf{a}_2\mathbf{b}_2^{\top}=\begin{pmatrix}3&4&1\\ 1&2&0\end{pmatrix}.$$

The columns of $B\odot A$ are $\mathbf{b}_r\otimes\mathbf{a}_r$ (with $\mathbf{a}$ the fast index):

$$B\odot A=\begin{pmatrix}1&2\\ 0&1\\ 0&4\\ 0&2\\ 1&0\\ 0&0\end{pmatrix},\qquad (B\odot A)^{\top}=\begin{pmatrix}1&0&0&0&1&0\\ 2&1&4&2&0&0\end{pmatrix}.$$

Reading the slices first index fastest, $\mathbf{X}^{(3)}=\begin{pmatrix}1&0&0&0&1&0\\ 3&1&4&2&1&0\end{pmatrix}$, and on the other side

$$C\,(B\odot A)^{\top}=\begin{pmatrix}1&0\\ 1&1\end{pmatrix}\begin{pmatrix}1&0&0&0&1&0\\ 2&1&4&2&0&0\end{pmatrix}=\begin{pmatrix}1&0&0&0&1&0\\ 3&1&4&2&1&0\end{pmatrix}=\mathbf{X}^{(3)}.$$ (3 P.)

c) The slices of $Y=\mathbf{X}\times_1 P\times_2 Q\times_3 S$ come out as

$$Y_{::1}=\begin{pmatrix}6&13\\ 6&12\end{pmatrix},\qquad Y_{::2}=\begin{pmatrix}1&4\\ 0&2\end{pmatrix},$$

so with $i$ fastest, then $j$, then $k$,

$$\operatorname{vec}(\mathbf{X})=(1,0,2,1,1,3,0,1)^{\top},\qquad \operatorname{vec}(Y)=(6,6,13,12,1,0,4,2)^{\top}.$$

The big Kronecker product is the $8\times 8$ matrix

$$S\otimes Q\otimes P=\begin{pmatrix}2&2&0&0&1&1&0&0\\ 0&4&0&0&0&2&0&0\\ 2&2&2&2&1&1&1&1\\ 0&4&0&4&0&2&0&2\\ 1&1&0&0&0&0&0&0\\ 0&2&0&0&0&0&0&0\\ 1&1&1&1&0&0&0&0\\ 0&2&0&2&0&0&0&0\end{pmatrix},$$

and multiplying, entry by entry (e.g. the third entry is $2\cdot1+2\cdot0+2\cdot2+2\cdot1+1\cdot1+1\cdot3+1\cdot0+1\cdot1=13$),

$$(S\otimes Q\otimes P)\operatorname{vec}(\mathbf{X})=(6,6,13,12,1,0,4,2)^{\top}=\operatorname{vec}(Y),$$

as claimed: a multilinear map is a linear map on the vectorized tensor, with the mode-$3$ matrix leftmost because $k$ is the slowest stacking index. (1 P.)

For the size count: $S\otimes Q\otimes P$ has $8\cdot 8=64$ entries, while $P$, $Q$ and $S$ together store only $4+4+4=12$ numbers. Forming the Kronecker product explicitly multiplies the memory and work by roughly $5\times$ here — and in general the dense matrix has $\big(\prod_m n_m\big)^2$ entries against $\sum_m n_m^2$ (or $\sum_m n_m r_m$ in a low-rank map) in the factors. That is why implementations never build $S\otimes Q\otimes P$: they apply the three small mode-$n$ products one mode at a time, which is exactly what makes multilinear computations on tensors feasible. (1 P.)
