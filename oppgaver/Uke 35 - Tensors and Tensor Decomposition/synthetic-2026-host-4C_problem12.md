### **Problem 12** (Tucker versus CP: truncations and error bookkeeping on a small tensor, 8 points)

A small tensor $\mathbf{T}\in\mathbb{R}^{3\times2\times2}$ is given in Tucker form $\mathbf{T}=\mathbf{G}\times_1U\times_2V\times_3W$. The core $\mathbf{G}\in\mathbb{R}^{3\times2\times2}$ has exactly three nonzero entries,

$$g_{111}=6,\qquad g_{222}=3,\qquad g_{312}=2,$$

and the factors are the orthogonal-type matrices

$$U=\frac13\begin{pmatrix}2&1&2\\ 1&2&-2\\ 2&-2&-1\end{pmatrix},\qquad V=\frac1{\sqrt5}\begin{pmatrix}1&2\\ 2&-1\end{pmatrix},\qquad W=\frac1{\sqrt2}\begin{pmatrix}1&1\\ 1&-1\end{pmatrix},$$

with columns $\mathbf{u}_1,\mathbf{u}_2,\mathbf{u}_3$; $\mathbf{v}_1,\mathbf{v}_2$; $\mathbf{w}_1,\mathbf{w}_2$, so that $\mathbf{T}=6\,\boldsymbol\varphi_1+3\,\boldsymbol\varphi_2+2\,\boldsymbol\varphi_3$ with $\boldsymbol\varphi_1=\mathbf{u}_1\circledast\mathbf{v}_1\circledast\mathbf{w}_1$, $\boldsymbol\varphi_2=\mathbf{u}_2\circledast\mathbf{v}_2\circledast\mathbf{w}_2$, $\boldsymbol\varphi_3=\mathbf{u}_3\circledast\mathbf{v}_1\circledast\mathbf{w}_2$.

a) Check from the integer columns that the columns of $U$, $V$ and $W$ are orthonormal in their own spaces. Using $\langle \mathbf{a}\circledast\mathbf{b}\circledast\mathbf{c},\,\mathbf{a}'\circledast\mathbf{b}'\circledast\mathbf{c}'\rangle=(\mathbf{a}\cdot\mathbf{a}')(\mathbf{b}\cdot\mathbf{b}')(\mathbf{c}\cdot\mathbf{c}')$, show that $\boldsymbol\varphi_1,\boldsymbol\varphi_2,\boldsymbol\varphi_3$ are unit tensors that are pairwise orthogonal, and conclude $\|\mathbf{T}\|_F^2=49$. (2 P.)

b) Write out the three unfoldings $G^{(1)}$, $G^{(2)}$, $G^{(3)}$ (the Problem-3 convention: first remaining index fastest) and read off the multilinear rank of $\mathbf{G}$ — and hence of $\mathbf{T}$. Compute $G^{(1)}G^{(1)\top}$, and use $\mathbf{T}^{(1)}=U\,G^{(1)}(W\odot V)^{\top}$ together with $(W\odot V)^{\top}(W\odot V)=(W^{\top}W)\circ(V^{\top}V)$ to find the three singular values of $\mathbf{T}^{(1)}$. (2 P.)

c) Truncate in mode $1$: keep the two leading singular directions and drop the rest, giving $\widehat{\mathbf{T}}=6\,\boldsymbol\varphi_1+3\,\boldsymbol\varphi_2$. State its Frobenius error and relative error, explain via the Eckart–Young theorem why $\widehat{\mathbf{T}}$ is not merely *a* core-$(2,2,2)$ approximation but the **best** one, and count the storage of the truncated format ($2\times2\times2$ core, $U$ shortened to $3\times2$) against the untruncated Tucker format and the $12$ raw entries. (2 P.)

d) Read the same tensor as a weighted rank-$3$ CP decomposition and count its storage. The best rank-$1$ CP approximation of $\mathbf{T}$ is $6\,\boldsymbol\varphi_1$: justify this by showing $\big|\langle \mathbf{T},\mathbf{z}\rangle\big|\le6$ for every unit rank-$1$ tensor $\mathbf{z}=\boldsymbol\alpha\circledast\boldsymbol\beta\circledast\boldsymbol\gamma$, written in the three orthonormal bases $\{\mathbf{u}_i\},\{\mathbf{v}_j\},\{\mathbf{w}_k\}$ (hint: $\langle\mathbf{T},\mathbf{z}\rangle=6\alpha_1\beta_1\gamma_1+3\alpha_2\beta_2\gamma_2+2\alpha_3\beta_1\gamma_2$, then Cauchy–Schwarz twice, using $\beta_1^2+\beta_2^2=1$ and $36s^2+9t^2\le36$ for $s^2+t^2\le1$). Give the resulting rank-$1$ error and compare the two truncation stories (mode truncation error vs best rank-$1$ CP error) and the two formats at scale, for a $400\times300\times200$ tensor in rank-$3$ CP versus Tucker core $(3,2,2)$. (2 P.)

*Kjeldevarsel: Syntetisk oppgåve — oppgåveforma er tilpassa frå øvingsoppgåver i Ballard & Kolda, «Tensor Decompositions for Data Science» (Cambridge University Press, final draft mars 2025), kap. 5–6 og 9; ingen tekst eller tal er henta frå utkastet, og Eckart–Young for modus-unfoldingar og lagringstal for CP og Tucker er standardstoff som òg står i den offentleg utgitte rapporten Kolda & Bader, «Tensor Decompositions and Applications», SAND2007-6702 (2007).*
