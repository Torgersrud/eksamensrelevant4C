### **Solution to Problem 2**

**a.** We have

$$A^{\top}A=\begin{bmatrix}2&0&2\\ 0&2&0\\ 2&0&2\end{bmatrix}=2\begin{bmatrix}1&0&1\\ 0&1&0\\ 1&0&1\end{bmatrix},$$

with characteristic polynomial $-\lambda(\lambda-2)(\lambda-4)$: the eigenvalues are $\lambda_1=4$, $\lambda_2=2$, $\lambda_3=0$, so the singular values are $\sigma_1=2$ and $\sigma_2=\sqrt2$. Orthonormal eigenvectors are

$$v_1=\frac1{\sqrt2}\begin{bmatrix}1\\ 0\\ 1\end{bmatrix},\qquad v_2=\begin{bmatrix}0\\ 1\\ 0\end{bmatrix},\qquad v_3=\frac1{\sqrt2}\begin{bmatrix}1\\ 0\\ -1\end{bmatrix},$$

and we collect them in the orthogonal matrix

$$V=\frac1{\sqrt2}\begin{bmatrix}1&0&1\\ 0&\sqrt2&0\\ 1&0&-1\end{bmatrix}.$$

For the left singular vectors we get

$$u_1=\frac1{\sigma_1}Av_1=\frac1{\sqrt2}\begin{bmatrix}1\\ 0\\ 1\\ 0\end{bmatrix},\qquad u_2=\frac1{\sigma_2}Av_2=\frac1{\sqrt2}\begin{bmatrix}0\\ 1\\ 0\\ 1\end{bmatrix}.$$

To extend $u_1,u_2$ to an orthonormal basis of $\mathbb{R}^4$ we solve $Bx=0$ where

$$B=\begin{bmatrix}1&0&1&0\\ 0&1&0&1\end{bmatrix},$$

i.e. the general solution is $u=s\,(1,0,-1,0)^{\top}+t\,(0,1,0,-1)^{\top}$. The two directions are orthogonal, and after normalizing we may take

$$U=\frac1{\sqrt2}\begin{bmatrix}1&0&1&0\\ 0&1&0&1\\ 1&0&-1&0\\ 0&1&0&-1\end{bmatrix},\qquad
\Sigma=\begin{bmatrix}2&0&0\\ 0&\sqrt2&0\\ 0&0&0\\ 0&0&0\end{bmatrix}.$$

Then $U$ and $V$ are orthogonal and $A=U\Sigma V^{\top}$ is a singular value decomposition of $A$.

**b.** From $A^{+}=V\Sigma^{+}U^{\top}$, where

$$\Sigma^{+}=\begin{bmatrix}1/2&0&0&0\\ 0&1/\sqrt2&0&0\\ 0&0&0&0\end{bmatrix},$$

we find

$$A^{+}=\frac12\begin{bmatrix}1&0&1\\ 0&\sqrt2&0\\ 1&0&-1\end{bmatrix}
\begin{bmatrix}1/2&0&0&0\\ 0&1/\sqrt2&0&0\\ 0&0&0&0\end{bmatrix}
\cdot\frac1{\sqrt2}\begin{bmatrix}1&0&1&0\\ 0&1&0&1\\ 1&0&-1&0\\ 0&1&0&-1\end{bmatrix}
=\frac14\begin{bmatrix}1&0&1&0\\ 0&2&0&2\\ 1&0&1&0\end{bmatrix}.$$

(Check: $AA^{+}A=A$. Note that $A$ does not have full column rank — its third column equals its first — so $A^{+}A\neq I$, as expected: $A^{+}A$ is the orthogonal projection of $\mathbb{R}^{3}$ onto the row space of $A$.)

Kildesett: course=TMA4145 term=host year=2007 problem=2 file=tma4145eksh07en.pdf
