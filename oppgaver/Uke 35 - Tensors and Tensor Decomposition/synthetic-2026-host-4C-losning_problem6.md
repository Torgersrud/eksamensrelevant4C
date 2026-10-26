### **Solution to Problem 6** (When is a CP decomposition unique? Scaling, permutation and a degenerate tensor, 8 points)

a) The slices of $\mathbf{X}=[\![A,B,C]\!]$ are $X_{::k}=\sum_r \mathbf{a}_r\mathbf{b}_r^{\top}c_{k,r}$, and here $C=I$ picks out one component per slice:

$$X_{::1}=\mathbf{a}_1\mathbf{b}_1^{\top}=\begin{pmatrix}3\\4\end{pmatrix}\begin{pmatrix}4&3\end{pmatrix}=\begin{pmatrix}12&9\\ 16&12\end{pmatrix},\qquad
X_{::2}=\mathbf{a}_2\mathbf{b}_2^{\top}=\begin{pmatrix}5\\12\end{pmatrix}\begin{pmatrix}12&5\end{pmatrix}=\begin{pmatrix}60&25\\ 144&60\end{pmatrix}.$$

Swapping columns means multiplying the factor matrices on the right by $\Pi=\begin{pmatrix}0&1\\1&0\end{pmatrix}$:

$$A\Pi=\begin{pmatrix}5&3\\ 12&4\end{pmatrix},\quad B\Pi=\begin{pmatrix}12&4\\ 5&3\end{pmatrix},\quad C\Pi=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}.$$

Now component $1$ of the new set is $(\mathbf{a}_2,\mathbf{b}_2,\mathbf{c}_2)$, whose mode-$3$ vector is $\mathbf{e}_2$, so it lands in slice $2$ with the value $\mathbf{a}_2\mathbf{b}_2^{\top}$, and component $2$ lands in slice $1$ with $\mathbf{a}_1\mathbf{b}_1^{\top}$. The two slices come out exactly as before, so $[\![A\Pi,B\Pi,C\Pi]\!]=\mathbf{X}$.

The scaling gives

$$\tilde A=\begin{pmatrix}3\cdot 3&5\\ 3\cdot 4&12\end{pmatrix}=\begin{pmatrix}9&5\\ 12&12\end{pmatrix},\quad
\tilde B=\begin{pmatrix}5\cdot 4&12\\ 5\cdot 3&5\end{pmatrix}=\begin{pmatrix}20&12\\ 15&5\end{pmatrix},\quad
\tilde C=\begin{pmatrix}\tfrac1{15}&0\\ 0&1\end{pmatrix},$$

and its first slice is $3\cdot 5\cdot\tfrac1{15}\,\mathbf{a}_1\mathbf{b}_1^{\top}=\mathbf{a}_1\mathbf{b}_1^{\top}$, its second $1\cdot1\cdot1\,\mathbf{a}_2\mathbf{b}_2^{\top}$ — the same $\mathbf{X}$ again.

The two indeterminacies are, for a rank-$r$ decomposition $\mathbf{X}=\sum_{s=1}^r\mathbf{a}_s\circledast\mathbf{b}_s\circledast\mathbf{c}_s$:

* **permutation:** $[\![A,B,C]\!]=[\![A\Pi,B\Pi,C\Pi]\!]$ for any $r\times r$ permutation matrix $\Pi$ — the components may be listed in any order;
* **scaling:** $\mathbf{a}_s\circledast\mathbf{b}_s\circledast\mathbf{c}_s=(\alpha_s\mathbf{a}_s)\circledast(\beta_s\mathbf{b}_s)\circledast(\gamma_s\mathbf{c}_s)$ whenever $\alpha_s\beta_s\gamma_s=1$, so the size of a component may be moved freely between its three factor vectors. (2 P.)

b) $|\mathbf{a}_1|=|(3,4)|=5$, $|\mathbf{b}_1|=|(4,3)|=5$, $|\mathbf{c}_1|=1$, and $|\mathbf{a}_2|=|(5,12)|=13$, $|\mathbf{b}_2|=|(12,5)|=13$, $|\mathbf{c}_2|=1$, so

$$\lambda_1=5\cdot 5\cdot 1=25,\qquad \lambda_2=13\cdot13\cdot1=169,$$

$$\hat{\mathbf{a}}_1=\tfrac15\begin{pmatrix}3\\4\end{pmatrix},\ \hat{\mathbf{b}}_1=\tfrac15\begin{pmatrix}4\\3\end{pmatrix},\ \hat{\mathbf{c}}_1=\begin{pmatrix}1\\0\end{pmatrix},\qquad
\hat{\mathbf{a}}_2=\tfrac1{13}\begin{pmatrix}5\\12\end{pmatrix},\ \hat{\mathbf{b}}_2=\tfrac1{13}\begin{pmatrix}12\\5\end{pmatrix},\ \hat{\mathbf{c}}_2=\begin{pmatrix}0\\1\end{pmatrix}.$$

Check of slice $1$: only $\hat{\mathbf{c}}_1$ has a non-zero first entry, so $X_{::1}=\lambda_1\hat{\mathbf{a}}_1\hat{\mathbf{b}}_1^{\top}=\tfrac{25}{25}\begin{pmatrix}3\\4\end{pmatrix}\begin{pmatrix}4&3\end{pmatrix}=\begin{pmatrix}12&9\\16&12\end{pmatrix}$, and likewise $X_{::2}=\tfrac{169}{169}\begin{pmatrix}5\\12\end{pmatrix}\begin{pmatrix}12&5\end{pmatrix}=\begin{pmatrix}60&25\\144&60\end{pmatrix}$ — the slices from a). With unit-length factors the only remaining freedom is the ordering of the components, because any rescaling that keeps all three vectors of length $1$ must use $|\alpha_r|=|\beta_r|=|\gamma_r|=1$. (2 P.)

c) Both factorisations have $C_0=\tilde C=\begin{pmatrix}1&1\\3&3\end{pmatrix}$, i.e. both components carry the *same* mode-$3$ vector $\mathbf{c}=(1,3)^{\top}$, so slice $1$ is $\sum_s\mathbf{a}_s\mathbf{b}_s^{\top}=AB^{\top}$ and slice $2$ is $3$ times the same matrix. For the first factorisation

$$A_0B_0^{\top}=\begin{pmatrix}1&0\\0&1\end{pmatrix}\begin{pmatrix}1&2\\1&3\end{pmatrix}=\begin{pmatrix}1&2\\1&3\end{pmatrix},$$

and for the second

$$\tilde A\tilde B^{\top}=\begin{pmatrix}1&1\\0&1\end{pmatrix}\begin{pmatrix}0&-1\\1&3\end{pmatrix}=\begin{pmatrix}1&2\\1&3\end{pmatrix},$$

the same matrix, so both produce $(X_0)_{::1}=\begin{pmatrix}1&2\\1&3\end{pmatrix}$ and $(X_0)_{::2}=\begin{pmatrix}3&6\\3&9\end{pmatrix}$. (1 P.)

The mode-$1$ unfolding is $\mathbf{X}_0^{(1)}=\begin{pmatrix}1&2&3&6\\ 1&3&3&9\end{pmatrix}$, which has rank $2$ (its first two columns are independent), and $\operatorname{rank}(\mathbf{X}_0^{(1)})\le\operatorname{rank}(\mathbf{X}_0)$ always, so $\operatorname{rank}(\mathbf{X}_0)\ge2$; the two displayed factorisations show $\operatorname{rank}(\mathbf{X}_0)\le2$. Hence $\operatorname{rank}(\mathbf{X}_0)=2$. (1 P.)

The two factorisations are not the same component list in disguise: the mode-$1$ directions in the first are $\mathbf{e}_1=(1,0)^{\top}$ and $\mathbf{e}_2=(0,1)^{\top}$, while the second uses $(1,0)^{\top}$ and $(1,1)^{\top}$, and $(1,1)^{\top}$ is parallel to neither $\mathbf{e}_1$ nor $\mathbf{e}_2$. Permuting reorders the list and rescaling only stretches the vectors, so no combination of the two indeterminacies in a) turns one into the other — the rank-$2$ decomposition of $\mathbf{X}_0$ is genuinely non-unique.

The mechanism is the rank deficiency of $C_0$: both components have the same mode-$3$ direction, so the tensor cannot separate them and only "sees" the matrix $M=\sum_s\mathbf{a}_s\mathbf{b}_s^{\top}$. But a rank-$2$ matrix has infinitely many rank-$2$ factorisations: for any invertible $2\times2$ matrix $T$, $AB^{\top}=(AT)(BT^{-\top})^{\top}$, and here $T=\begin{pmatrix}1&1\\0&1\end{pmatrix}$, $T^{-\top}=\begin{pmatrix}1&0\\-1&1\end{pmatrix}$ is exactly the step from $(A_0,B_0)$ to $(\tilde A,\tilde B)$. As long as the mode-$3$ factors are dependent, the CP components can be mixed inside the span without changing $\mathbf{X}_0$. (1 P.)

d) $A$ and $B$ are both invertible ($3\cdot12-5\cdot 4=16$ and $4\cdot5-12\cdot3=-16$, neither zero) and so is $C$, and a $2\times2$ factor matrix with independent columns has $k=2$. Thus

$$k_A+k_B+k_C=2+2+2=6\ge 2\cdot 2+2=6,$$

so Kruskal's condition holds for $\mathbf{X}=[\![A,B,C]\!]$: its rank-$2$ decomposition is unique apart from permutation and scaling — which is what a) and b) show by exhibiting only those two kinds of alternatives.

For $\mathbf{X}_0$ the two columns of $C_0$ are equal, so the largest set of mutually independent columns there has size $1$: $k_{C_0}=1$, and

$$k_{A_0}+k_{B_0}+k_{C_0}=2+2+1=5<6 .$$

The condition fails, and c) shows the failure is real: the same tensor has two rank-$2$ decompositions that differ by more than permutation and scaling. The condition is only sufficient, not necessary, but when a mode is rank deficient the uniqueness is exactly what is lost. (1 P.)
