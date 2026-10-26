### **Solution to Problem 12** (Tucker versus CP: truncations and error bookkeeping on a small tensor, 8 points)

a) The integer columns of $U$ are $(2,1,2)$, $(1,2,-2)$, $(2,-2,-1)$, each of length $\sqrt9=3$ (so the columns of $U$ are unit), and their pairwise dot products are $2+2-4=0$, $4-2-2=0$, $2-4+2=0$; the columns $(1,2)$, $(2,-1)$ of $V$ have length $\sqrt5$ and dot product $2-2=0$; likewise $(1,1)\cdot(1,-1)=0$ with length $\sqrt2$ in $W$. So all three factor sets are orthonormal. Each $\boldsymbol\varphi_r$ is a tensor product of unit vectors, hence unit; and

$$\langle\boldsymbol\varphi_1,\boldsymbol\varphi_2\rangle=(\mathbf{u}_1\cdot\mathbf{u}_2)(\mathbf{v}_1\cdot\mathbf{v}_2)(\mathbf{w}_1\cdot\mathbf{w}_2)=0,\quad
\langle\boldsymbol\varphi_1,\boldsymbol\varphi_3\rangle=(\mathbf{u}_1\cdot\mathbf{u}_3)\cdot1\cdot(\mathbf{w}_1\cdot\mathbf{w}_2)=0,\quad
\langle\boldsymbol\varphi_2,\boldsymbol\varphi_3\rangle=(\mathbf{u}_2\cdot\mathbf{u}_3)(\mathbf{v}_2\cdot\mathbf{v}_1)\cdot1=0 .$$

Pythagoras then gives $\|\mathbf{T}\|_F^2=6^2+3^2+2^2=49$ (equally $\|\mathbf{G}\|_F^2$ by orthonormal mode products, Problem 10 b)). (2 P.)

b) With the first remaining index fastest,

$$G^{(1)}=\begin{pmatrix}6&0&0&0\\ 0&0&0&3\\ 0&0&2&0\end{pmatrix},\quad
G^{(2)}=\begin{pmatrix}6&0&0&0&0&2\\ 0&0&0&0&3&0\end{pmatrix},\quad
G^{(3)}=\begin{pmatrix}6&0&0&0&0&0\\ 0&0&2&0&3&0\end{pmatrix},$$

each of rank $2$: the multilinear rank of $\mathbf{G}$ is $(2,2,2)$, and multiplying by the invertible (orthogonal) factors does not change unfolding ranks, so $\mathbf{T}$ has multilinear rank $(2,2,2)$ too. Further $G^{(1)}G^{(1)\top}=\operatorname{diag}(36,9,4)$. Since $\mathbf{T}^{(1)}=U\,G^{(1)}(W\odot V)^{\top}$ and $(W\odot V)^{\top}(W\odot V)=(W^{\top}W)\circ(V^{\top}V)=I_2\circ I_2=I_2$, the Gram of $\mathbf{T}^{(1)}\mathbf{T}^{(1)\top}=U\operatorname{diag}(36,9,4)U^{\top}$ has eigenvalues $36,9,4$, so the singular values of $\mathbf{T}^{(1)}$ are $\sigma_1=6$, $\sigma_2=3$, $\sigma_3=2$. (2 P.)

c) Dropping the $u_3$ direction kills exactly $2\boldsymbol\varphi_3$, a term orthogonal to the others, so

$$\|\mathbf{T}-\widehat{\mathbf{T}}\|_F^2=\|2\boldsymbol\varphi_3\|_F^2=4,\qquad \|\mathbf{T}-\widehat{\mathbf{T}}\|_F=2,\qquad \text{relative error } \frac{2}{\|\mathbf{T}\|_F}=\frac{2}{7}.$$

Optimality: every tensor $\mathbf{X}$ that has a core $(2,2,2)$ with $2$-column factors satisfies $\operatorname{rank}X^{(1)}\le2$, so its unfolding is at least as far from $\mathbf{T}^{(1)}$ as the best matrix of rank $\le2$; by Eckart–Young that best matrix is $\widehat{\mathbf{T}}^{(1)}$ (keep $\sigma_1,\sigma_2$, drop $\sigma_3$) with error $\sigma_3=2$. Since $\widehat{\mathbf{T}}$ itself is a core-$(2,2,2)$ tensor attaining this bound over the larger class $\{\operatorname{rank}X^{(1)}\le2\}$, it is the best rank-$(2,2,2)$ approximation. Storage: the truncated format keeps a core $2\cdot2\cdot2=8$, $\widehat U$ of size $3\times2=6$, $V$ $4$, $W$ $4$: $22$ numbers — fewer than the untruncated $12+9+4+4=29$, but still more than the $12$ raw entries (a $3\times2\times2$ tensor is too small for any format to pay off). (2 P.)

d) As a CP sum $\mathbf{T}=\sum_r\lambda_r\,\mathbf{p}_r\circledast\mathbf{q}_r\circledast\mathbf{s}_r$ with the three orthonormal triples above, the format stores $3(3+2+2)=21$ numbers — cheaper than the Tucker $29$. For the rank-$1$ claim, write a unit rank-$1$ tensor in the three orthonormal bases: with $\|\boldsymbol\alpha\|=\|\boldsymbol\beta\|=\|\boldsymbol\gamma\|=1$,

$$\langle\mathbf{T},\mathbf{z}\rangle=6\alpha_1\beta_1\gamma_1+3\alpha_2\beta_2\gamma_2+2\alpha_3\beta_1\gamma_2 .$$

Cauchy–Schwarz on the pair $(\alpha_1,\alpha_3)$ against $(6\gamma_1,2\gamma_2)$ gives $|6\alpha_1\gamma_1+2\alpha_3\gamma_2|\le\sqrt{\alpha_1^2+\alpha_3^2}\sqrt{36\gamma_1^2+4\gamma_2^2}\le6s$ with $s=\sqrt{\alpha_1^2+\alpha_3^2}$ (since $\gamma_1^2+\gamma_2^2\le1$); with $t=|\alpha_2|$ (so $s^2+t^2\le1$) and Cauchy–Schwarz in $(\beta_1,\beta_2)$,

$$|\langle\mathbf{T},\mathbf{z}\rangle|\le 6s\beta_1+3t\beta_2\le\sqrt{36s^2+9t^2}\sqrt{\beta_1^2+\beta_2^2}\le\sqrt{36(s^2+t^2)}=6 .$$

For a fixed unit direction $\mathbf{z}$ the best scaled rank-$1$ fit is $\langle\mathbf{T},\mathbf{z}\rangle\mathbf{z}$ with squared error $\|\mathbf{T}\|_F^2-\langle\mathbf{T},\mathbf{z}\rangle^2\ge49-36=13$, and equality holds at $\mathbf{z}=\boldsymbol\varphi_1$: the best rank-$1$ CP approximation is $6\,\boldsymbol\varphi_1$ with error $\sqrt{13}\approx3.6$ (relative $\sqrt{13}/7\approx52\%$). So the books read very differently: dropping one mode-$1$ direction (a core $(2,2,2)$ truncation) keeps six components' worth of structure for error $2$, while collapsing to a single CP term costs $\sqrt{13}$. At scale the format comparison flips the storage ranking of part c): for a $400\times300\times200$ tensor, rank-$3$ CP stores $3\cdot900=2\,700$ numbers while Tucker with core $(3,2,2)$ stores $12+3\cdot400+2\cdot300+2\cdot200=2\,212$ — the small unbalanced core makes Tucker the cheaper of the two (against $24\,000\,000$ raw entries: factors $\approx8\,900$ and $\approx10\,850$), even though CP won on the $3\times2\times2$ case. (2 P.)
