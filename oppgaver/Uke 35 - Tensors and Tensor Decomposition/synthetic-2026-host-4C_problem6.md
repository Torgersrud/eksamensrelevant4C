### **Problem 6** (When is a CP decomposition unique? Scaling, permutation and a degenerate tensor, 8 points)

Let

$$A=\begin{pmatrix}3&5\\ 4&12\end{pmatrix},\qquad B=\begin{pmatrix}4&12\\ 3&5\end{pmatrix},\qquad C=\begin{pmatrix}1&0\\ 0&1\end{pmatrix},\qquad
X=[\![A,B,C]\!]\in\mathbb{R}^{2\times 2\times 2}.$$

a) Write out the two frontal slices of $\mathbf{X}$. Now swap the two columns in all three factor matrices, and separately scale them by
$\alpha=(3,1)$, $\beta=(5,1)$, $\gamma=(1/15,1)$, i.e. replace $(\mathbf{a}_r,\mathbf{b}_r,\mathbf{c}_r)$ by $(\alpha_r\mathbf{a}_r,\beta_r\mathbf{b}_r,\gamma_r\mathbf{c}_r)$. Recompute the frontal slices for both new factor sets and compare with $\mathbf{X}$. Name the two indeterminacies of the CP decomposition that these two examples illustrate, and state each of them in general form for a rank-$r$ decomposition.

b) In the scaling example above the three scaling triples satisfy $\alpha_r\beta_r\gamma_r=1$. The usual way to fix the scaling freedom completely is to put all the size into a weight: write $\mathbf{X}$ in the form

$$\mathbf{X}=\sum_{r=1}^{2}\lambda_r\,\hat{\mathbf{a}}_r\circledast\hat{\mathbf{b}}_r\circledast\hat{\mathbf{c}}_r,\qquad
\|\hat{\mathbf{a}}_r\|=\|\hat{\mathbf{b}}_r\|=\|\hat{\mathbf{c}}_r\|=1,$$

by computing $\lambda_1,\lambda_2$ and the six unit vectors. Check that your weighted sum reproduces the slices you found in a).

c) Consider instead the tensor $\mathbf{X}_0\in\mathbb{R}^{2\times 2\times 2}$ given by

$$(X_0)_{::1}=\begin{pmatrix}1&2\\ 1&3\end{pmatrix},\qquad (X_0)_{::2}=\begin{pmatrix}3&6\\ 3&9\end{pmatrix},$$

and the two rank-$2$ factorisations of it

$$A_0=\begin{pmatrix}1&0\\ 0&1\end{pmatrix},\ B_0=\begin{pmatrix}1&1\\ 2&3\end{pmatrix},\ C_0=\begin{pmatrix}1&1\\ 3&3\end{pmatrix}
\qquad\text{and}\qquad
\tilde A=\begin{pmatrix}1&1\\ 0&1\end{pmatrix},\ \tilde B=\begin{pmatrix}0&1\\ -1&3\end{pmatrix},\ \tilde C=C_0 .$$

Verify that both factorisations represent $\mathbf{X}_0$, argue that $\operatorname{rank}(\mathbf{X}_0)=2$, and explain why the second factorisation is *not* obtained from the first by permuting or rescaling columns. What is it about $C_0$ that makes this extra freedom possible?

d) The *$k$-rank* $k_M$ of a matrix $M$ is the largest integer $k$ such that every choice of $k$ columns of $M$ is linearly independent. Kruskal's condition says that a rank-$r$ CP decomposition is unique (up to the two indeterminacies in a)) if $k_A+k_B+k_C\ge 2r+2$. Compute the three $k$-ranks for the factorisations in a) and in c) and decide in which of the two cases Kruskal's condition guarantees uniqueness.

*Kjeldevarsel: Syntetisk oppgåve — oppgåveforma er tilpassa frå øvingsoppgåver i Ballard & Kolda, «Tensor Decompositions for Data Science» (Cambridge University Press, final draft mars 2025), kap. 9; ingen tekst eller tal er henta frå utkastet, og omgrepet k-rang og Kruskal-vilkåret er standardstoff som står i den offentleg utgitte rapporten Kolda & Bader, «Tensor Decompositions and Applications», SAND2007-6702 (2007), avsnitt 3.2.*
