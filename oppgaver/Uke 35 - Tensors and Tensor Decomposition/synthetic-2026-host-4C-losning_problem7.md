### **Solution to Problem 7** (Mode-$n$ products and multilinear maps, 8 points)

a) Multiplying from the left acts row-wise on every frontal slice, $W_{::k}=PX_{::k}$:

$$W_{::1}=\begin{pmatrix}1&2\\ 0&1\end{pmatrix}\begin{pmatrix}1&0&2\\ 3&1&0\end{pmatrix}=\begin{pmatrix}7&2&2\\ 3&1&0\end{pmatrix},\qquad W_{::2}=\begin{pmatrix}1&2\\ 0&1\end{pmatrix}\begin{pmatrix}2&1&1\\ 0&2&4\end{pmatrix}=\begin{pmatrix}2&5&9\\ 0&2&4\end{pmatrix}.$$

The first row of each slice becomes (row 1) $+\,2\cdot$(row 2); the second row is unchanged. (1 P.)

b) The mode-$3$ product mixes the frontal slices: $V_{::\ell}=\sum_k s_{\ell k}X_{::k}$. Since the first row of $S$ is $(0,1)$ and the second is $(1,1)$,

$$V_{::1}=0\cdot X_{::1}+1\cdot X_{::2}=X_{::2}=\begin{pmatrix}2&1&1\\ 0&2&4\end{pmatrix},\qquad V_{::2}=X_{::1}+X_{::2}=\begin{pmatrix}3&1&3\\ 3&3&4\end{pmatrix}.$$

$V_{::1}$ is $X_{::2}$ unchanged because $s_{11}=0$ kills the first slice. Multiplying out in both orders, with $W$ from a),

$$(\mathbf{X}\times_1 P)\times_3 S=\begin{pmatrix}0&1\\ 1&1\end{pmatrix}\text{-mix of }W_{::1},W_{::2}=\begin{pmatrix}2&5&9\\ 0&2&4\end{pmatrix},\ \begin{pmatrix}9&7&11\\ 3&3&4\end{pmatrix}=(\mathbf{X}\times_3 S)\times_1 P,$$

where the second order mixes the slices first and then applies $P$ row-wise. Mode products along **different** modes commute, $(\mathbf{X}\times_n M)\times_k N=(\mathbf{X}\times_k N)\times_n M$ for $n\neq k$: each acts on a different index, so the order is irrelevant, and the result is the multilinear map with entries $\sum_{i,k}p_{\cdot i}\,s_{\cdot k}\,x_{ijk}$. (2 P.)

c) Applying the three products (in any order, e.g. first $P$ and $S$ as in b), then $Q$ which turns the $3$-mode into a $2$-mode by $Q_{::1}=(1,0,1)$ and $Q_{::2}=(2,1,0)$ acting along the rows),

$$Y_{::1}=\begin{pmatrix}11&9\\ 4&2\end{pmatrix},\qquad Y_{::2}=\begin{pmatrix}20&25\\ 7&9\end{pmatrix}.$$

The unfolding $Y^{(2)}$ has one row per value of mode 2 and columns indexed by the pairs $(i,k)$ with $i$ fastest:

$$Y^{(2)}=\begin{pmatrix}11&4&20&7\\ 9&2&25&9\end{pmatrix}.$$

On the right-hand side, reading the columns of $X^{(2)}$ as $(i,k)$ pairs with $i$ fastest,

$$X^{(2)}=\begin{pmatrix}1&3&2&0\\ 0&1&1&2\\ 2&0&1&4\end{pmatrix},\qquad S\otimes P=\begin{pmatrix}0&0&1&2\\ 0&0&0&1\\ 1&2&1&2\\ 0&1&0&1\end{pmatrix},$$

so $(S\otimes P)^{\top}=\begin{pmatrix}0&0&1&0\\ 0&0&2&1\\ 1&0&1&0\\ 2&1&0&1\end{pmatrix}$ and

$$Q\,X^{(2)}=\begin{pmatrix}1&0&1\\ 2&1&0\end{pmatrix}\begin{pmatrix}1&3&2&0\\ 0&1&1&2\\ 2&0&1&4\end{pmatrix}=\begin{pmatrix}3&3&3&4\\ 2&7&5&2\end{pmatrix},\qquad QX^{(2)}(S\otimes P)^{\top}=\begin{pmatrix}3&3&3&4\\ 2&7&5&2\end{pmatrix}\begin{pmatrix}0&0&1&0\\ 0&0&2&1\\ 1&0&1&0\\ 2&1&0&1\end{pmatrix}=\begin{pmatrix}11&4&20&7\\ 9&2&25&9\end{pmatrix},$$

which is exactly $Y^{(2)}$. The other two factors appear as $S\otimes P$ because the columns of a mode-$2$ unfolding run over $(i,k)$ with $i$ the fastest index, so the matrix acting on the slow index $k$ must sit leftmost in the Kronecker product. (3 P.)

d) Summing squares over the two slices: $\|\mathbf{X}\|_F^2=(1+0+4+9+1+0)+(4+1+1+0+4+16)=15+26=41$.

For $R$, the slices of $\mathbf{X}\times_3 R$ are $R_{::1}\text{-mix}=X_{::1}+X_{::2}=\begin{pmatrix}3&1&3\\ 3&3&4\end{pmatrix}$ and $R_{::2}\text{-mix}=-X_{::1}+X_{::2}=\begin{pmatrix}1&1&-1\\ -3&1&4\end{pmatrix}$, whose squared norms are $9+1+9+9+9+16=53$ and $1+1+1+9+1+16=29$, so $\|\mathbf{X}\times_3 R\|_F^2=53+29=82=2\cdot 41$.

The factor $2$ is forced by $R^{\top}R=\begin{pmatrix}2&0\\ 0&2\end{pmatrix}=2I$: the two rows of $R$ are orthogonal with squared length $2$, so every mode-$3$ fiber $\mathbf{x}_{ij:}$ is mapped to a vector of squared length $2\|\mathbf{x}_{ij:}\|^2$, and summing over all $2\cdot 3$ fibers doubles the total. Replacing $R$ by $R/\sqrt2$, which has orthonormal rows, would give $R^{\top}R=I$ and leave $\|\mathbf{X}\|_F^2=41$ unchanged. For $S$ one computes $S^{\top}S=\begin{pmatrix}1&1\\ 1&2\end{pmatrix}\neq I$, and indeed

$$\|\mathbf{X}\times_3 S\|_F^2=\|X_{::2}\|^2+\|X_{::1}+X_{::2}\|^2=26+53=79\neq 41,$$

so only factors with orthonormal rows (an orthogonal transformation in that mode) preserve the Frobenius norm. (1 P.)

e) A mode-$n$ product on a tensor with $D$ current entries unfolds to $U_nZ^{(n)}$ with $U_n\in\mathbb{R}^{J_n\times I_n}$ and $Z^{(n)}\in\mathbb{R}^{I_n\times(D/I_n)}$, which costs $J_n\,I_n\,\frac{D}{I_n}=J_n D$ multiplications — the input size $I_n$ cancels, so a step costs (number of rows of $U_n$) $\times$ (current number of entries), and after the step $D$ becomes $D\cdot J_n/I_n$. Starting from $D=40\cdot30\cdot20=24\,000$:

$$\begin{array}{c|c|c}\text{order}&\text{steps}&\text{total}\\\hline
1,2,3&96\,000+12\,000+800&108\,800\\
1,3,2&96\,000+4\,800+1\,200&102\,000\\
2,1,3&120\,000+16\,000+800&136\,800\\
2,3,1&120\,000+8\,000+1\,600&129\,600\\
3,1,2&48\,000+9\,600+1\,200&58\,800\\
3,2,1&48\,000+12\,000+1\,600&61\,600
\end{array}$$

The cheapest order is $3,1,2$ with $58\,800$ multiplications, the most expensive is $2,1,3$ with $136\,800$ — more than twice as much. The rule of thumb: since each step costs $J_n$ multiplications per current entry, run the products that **shrink** the tensor early (here modes 1 and 3 divide their mode by $10$) and save the step with the largest $J_n$ ($U_2$, with $5$ rows) for last, when the tensor is at its smallest. (1 P.)
