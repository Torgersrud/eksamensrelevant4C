### **Problem 8** (Unfolding identities for rank-one, CP and multilinear maps, 8 points)

Throughout, use the matricization convention of Problem 3: in $\mathbf{X}^{(m)}$ the columns run over the remaining indices with the **first** remaining index fastest, and the Kronecker product $A\otimes B$ is the block matrix with blocks $a_{ij}B$.

a) Let $\mathbf{a}=(1,2)^{\top}$, $\mathbf{b}=(1,0,-1)^{\top}$, $\mathbf{c}=(2,1)^{\top}$ and $\mathbf{X}=\mathbf{a}\circ\mathbf{b}\circ\mathbf{c}\in\mathbb{R}^{2\times 3\times 2}$. Write out the two frontal slices of $\mathbf{X}$ and the three unfoldings $\mathbf{X}^{(1)}$, $\mathbf{X}^{(2)}$, $\mathbf{X}^{(3)}$, and verify on your numbers that for a rank-one tensor

$$\mathbf{X}^{(1)}=\mathbf{a}\,(\mathbf{c}\otimes\mathbf{b})^{\top},\qquad \mathbf{X}^{(2)}=\mathbf{b}\,(\mathbf{c}\otimes\mathbf{a})^{\top},\qquad \mathbf{X}^{(3)}=\mathbf{c}\,(\mathbf{b}\otimes\mathbf{a})^{\top}.$$

Also compute $\|\mathbf{X}\|_F^2$ and check it against the product $\|\mathbf{a}\|^2\|\mathbf{b}\|^2\|\mathbf{c}\|^2$. (3 P.)

b) Let $\mathbf{X}=[\![A,B,C]\!]\in\mathbb{R}^{2\times 3\times 2}$ with

$$A=\begin{pmatrix}1&2\\ 0&1\end{pmatrix},\qquad B=\begin{pmatrix}1&1\\ 0&2\\ 1&0\end{pmatrix},\qquad C=\begin{pmatrix}1&0\\ 1&1\end{pmatrix}.$$

Compute the two frontal slices of $\mathbf{X}$, form the Khatri-Rao product $B\odot A$ (columns $\mathbf{b}_r\otimes\mathbf{a}_r$), and verify the mode-$3$ matricization identity $\mathbf{X}^{(3)}=C\,(B\odot A)^{\top}$ by computing both sides. (3 P.)

c) For a $3$-tensor $\mathbf{T}$ write $\operatorname{vec}(\mathbf{T})$ for the long column vector that stacks the entries $t_{ijk}$ with $i$ fastest, then $j$, then $k$ last. Let $\mathbf{X}\in\mathbb{R}^{2\times 2\times 2}$ have frontal slices

$$X_{::1}=\begin{pmatrix}1&2\\ 0&1\end{pmatrix},\qquad X_{::2}=\begin{pmatrix}1&0\\ 3&1\end{pmatrix},$$

and let $Y=\mathbf{X}\times_1 P\times_2 Q\times_3 S$ with $P=\begin{pmatrix}1&1\\ 0&2\end{pmatrix}$, $Q=\begin{pmatrix}1&0\\ 1&1\end{pmatrix}$, $S=\begin{pmatrix}2&1\\ 1&0\end{pmatrix}$. Compute the slices of $Y$ and the vector $\operatorname{vec}(Y)$, and verify

$$\operatorname{vec}(Y)=(S\otimes Q\otimes P)\,\operatorname{vec}(\mathbf{X})$$

by forming $S\otimes Q\otimes P$ and multiplying. Compare the number of entries of $S\otimes Q\otimes P$ with the number of entries of $P$, $Q$ and $S$ put together, and say what this means for implementing multilinear maps. (2 P.)

*Kjeldevarsel: Syntetisk oppgåve — oppgåveforma er tilpassa frå øvingsoppgåver i Ballard & Kolda, «Tensor Decompositions for Data Science» (Cambridge University Press, final draft mars 2025), kap. 2–3; ingen tekst eller tal er henta frå utkastet, og definisjonane og formlane oppgåva byggjer på er standardstoff som òg står i den offentleg utgitte rapporten Kolda & Bader, «Tensor Decompositions and Applications», SAND2007-6702 (2007).*
