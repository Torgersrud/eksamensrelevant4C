### **Problem 5** (Rank-1 pieces and a CP fit by least squares, 8 points)

The tensor $\mathbf{Y}\in\mathbb{R}^{2\times 3\times 2}$ is given by its frontal slices

$$Y_{::1}=\begin{pmatrix}3&-1&2\\ 4&2&1\end{pmatrix},\qquad Y_{::2}=\begin{pmatrix}-1&3&-2\\ 2&4&-1\end{pmatrix},$$

and the three factor matrices

$$A=\begin{pmatrix}1&2\\ 3&1\end{pmatrix},\qquad B=\begin{pmatrix}1&1\\ 1&-1\\ 0&1\end{pmatrix},\qquad C=\begin{pmatrix}1&1\\ 1&-1\end{pmatrix},$$

with columns $\mathbf{a}_1,\mathbf{a}_2$; $\mathbf{b}_1,\mathbf{b}_2$; $\mathbf{c}_1,\mathbf{c}_2$.

a) Form the two rank-1 tensors $\mathbf{R}_1=\mathbf{a}_1\circledast\mathbf{b}_1\circledast\mathbf{c}_1$ and
$\mathbf{R}_2=\mathbf{a}_2\circledast\mathbf{b}_2\circledast\mathbf{c}_2$ as pairs of frontal slices, add them, and compare with $\mathbf{Y}$. What does the comparison tell you about $\operatorname{rank}(\mathbf{Y})$?

b) Show that the first slice $Y_{::1}$ has rank $2$ when read as a matrix. Why does that rule out $\operatorname{rank}(\mathbf{Y})=1$, and what is $\operatorname{rank}(\mathbf{Y})$?

c) One ALS step for the CP model fixes $B$ and $C$ and chooses the mode-$1$ factor $A\in\mathbb{R}^{2\times 2}$ so as to minimise $\big\|\mathbf{Y}^{(1)}-A\,(C\odot B)^{\top}\big\|_F$, where $\mathbf{Y}^{(1)}\in\mathbb{R}^{2\times 6}$ is the mode-$1$ matricization: its columns are the fibers $y_{:jk}$, with the second index running fastest. Put $M=C\odot B$; compute $M\in\mathbb{R}^{6\times 2}$ and the Gram matrix $M^{\top}M$, and check $M^{\top}M$ against the Hadamard product $(C^{\top}C)\circ(B^{\top}B)$. Write down the normal equations for $A$ and solve them. Do you recover the matrix $A$ printed above, and what is the residual of the fit?

d) Count the numbers needed to store $\mathbf{Y}$ in full and in the rank-$2$ factor form $[\![A,B,C]\!]$. Does the low-rank form pay off here? State the general inequality for a $d$-way tensor and check it for a rank-$20$ representation of a $120\times 100\times 60$ tensor (give both storages and their ratio).

*Kjeldevarsel: Syntetisk oppgåve — oppgåveforma er tilpassa frå øvingsoppgåver i Ballard & Kolda, «Tensor Decompositions for Data Science» (Cambridge University Press, final draft mars 2025), kap. 3 og 9; ingen tekst eller tal er henta frå utkastet, og definisjonane og formlane oppgåva byggjer på er standardstoff som òg står i den offentleg utgitte rapporten Kolda & Bader, «Tensor Decompositions and Applications», SAND2007-6702 (2007).*
