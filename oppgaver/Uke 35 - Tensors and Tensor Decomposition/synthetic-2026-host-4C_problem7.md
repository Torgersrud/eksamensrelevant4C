### **Problem 7** (Mode-$n$ products and multilinear maps, 8 points)

A tensor $\mathbf{X}\in\mathbb{R}^{2\times 3\times 2}$ is given by its two frontal slices

$$X_{::1}=\begin{pmatrix}1&0&2\\ 3&1&0\end{pmatrix},\qquad X_{::2}=\begin{pmatrix}2&1&1\\ 0&2&4\end{pmatrix}.$$

Recall the mode-$n$ product: $Y=\mathbf{X}\times_n M$ has entries $y_{\dots\ell\dots}=\sum_k x_{\dots k\dots}\,m_{\ell k}$, equivalently $Y^{(n)}=MX^{(n)}$, where $M\in\mathbb{R}^{\ell\times n_n}$. Consider the three matrices

$$P=\begin{pmatrix}1&2\\ 0&1\end{pmatrix},\qquad Q=\begin{pmatrix}1&0&1\\ 2&1&0\end{pmatrix},\qquad S=\begin{pmatrix}0&1\\ 1&1\end{pmatrix},$$

where $P$ is $2\times 2$, $Q$ is $2\times 3$ and $S$ is $2\times 2$.

a) Compute $W=\mathbf{X}\times_1 P$ as its two frontal slices. (1 P.)

b) Compute $V=\mathbf{X}\times_3 S$ as its two frontal slices. One of the slices of $V$ is one of the slices of $\mathbf{X}$ unchanged — which one, and why? Compute $(\mathbf{X}\times_1 P)\times_3 S$ and $(\mathbf{X}\times_3 S)\times_1 P$ and state the general rule that explains why the two answers agree. (2 P.)

c) Let $Y=\mathbf{X}\times_1 P\times_2 Q\times_3 S\in\mathbb{R}^{2\times 2\times 2}$. Compute the two frontal slices of $Y$, and verify the mode-$2$ unfolding identity

$$Y^{(2)}=Q\,X^{(2)}\,(S\otimes P)^{\top}$$

by writing out all three matrices on the right-hand side and multiplying them out. (3 P.)

d) Write $\|\mathbf{T}\|_F^2=\sum t_{ijk}^2$ for the squared Frobenius norm, and let $R=\begin{pmatrix}1&1\\ -1&1\end{pmatrix}$. Compute $\|\mathbf{X}\|_F^2$, $\|\mathbf{X}\times_3 R\|_F^2$ and $\|\mathbf{X}\times_3 S\|_F^2$. Explain why the second answer equals a clean multiple of the first, why the third one does not, and what property the third factor would need for the norm to come out unchanged. (1 P.)

e) A streaming pipeline applies three mode products to a tensor $Z\in\mathbb{R}^{40\times 30\times 20}$: $U_1\in\mathbb{R}^{4\times 40}$, $U_2\in\mathbb{R}^{5\times 30}$ and $U_3\in\mathbb{R}^{2\times 20}$, giving $Z\times_1 U_1\times_2 U_2\times_3 U_3$. Counting one scalar multiplication per multiply-add in the matrix product $Y^{(n)}=U_n Z^{(n)}$ (so a $(J\times I)$ matrix times an $(I\times K)$ matrix costs $JIK$ multiplications), give the total number of multiplications for each of the six possible orders of the three products, and identify the cheapest order. State the rule of thumb about when an order is cheap. (1 P.)

*Kjeldevarsel: Syntetisk oppgåve — oppgåveforma er tilpassa frå øvingsoppgåver i Ballard & Kolda, «Tensor Decompositions for Data Science» (Cambridge University Press, final draft mars 2025), kap. 2; ingen tekst eller tal er henta frå utkastet, og definisjonane og formlane oppgåva byggjer på er standardstoff som òg står i den offentleg utgitte rapporten Kolda & Bader, «Tensor Decompositions and Applications», SAND2007-6702 (2007).*
