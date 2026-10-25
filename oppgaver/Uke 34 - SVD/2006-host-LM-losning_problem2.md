### **Solution to Problem 2**

We have

$$A^{\top}A=\begin{bmatrix}2&1\\ 1&2\end{bmatrix},$$

with eigenvalues $\lambda_1=3$, $\lambda_2=1$ and orthonormal eigenvectors

$$v_1=\frac1{\sqrt2}\begin{bmatrix}1\\ 1\end{bmatrix},\qquad v_2=\frac1{\sqrt2}\begin{bmatrix}1\\ -1\end{bmatrix},$$

so the singular values are $\sigma_1=\sqrt3$ and $\sigma_2=1$. Next

$$u_1=\frac1{\sigma_1}Av_1=\frac1{\sqrt6}\begin{bmatrix}1\\ 2\\ 1\end{bmatrix},\qquad
u_2=\frac1{\sigma_2}Av_2=\frac1{\sqrt2}\begin{bmatrix}1\\ 0\\ -1\end{bmatrix}.$$

To complete to an orthonormal basis of $\mathbb{R}^3$ we solve $Bx=0$ where $B$ has rows $u_1^{\top},u_2^{\top}$, which gives the direction $(1,-1,1)$, so we let

$$u_3=\frac1{\sqrt3}\begin{bmatrix}1\\ -1\\ 1\end{bmatrix}.$$

Then with

$$U=\begin{bmatrix}1/\sqrt6&1/\sqrt2&1/\sqrt3\\ 2/\sqrt6&0&-1/\sqrt3\\ 1/\sqrt6&-1/\sqrt2&1/\sqrt3\end{bmatrix},\qquad
\Sigma=\begin{bmatrix}\sqrt3&0\\ 0&1\\ 0&0\end{bmatrix},\qquad
V=\frac1{\sqrt2}\begin{bmatrix}1&1\\ 1&-1\end{bmatrix},$$

we have $U$, $V$ orthogonal and $A=U\Sigma V^{\top}$, a singular value decomposition of $A$.

The pseudo-inverse is $A^{+}=V\Sigma^{+}U^{\top}$ with $\Sigma^{+}=\begin{bmatrix}1/\sqrt3&0&0\\ 0&1&0\end{bmatrix}$:

$$A^{+}=\frac13\begin{bmatrix}2&1&-1\\ -1&1&2\end{bmatrix}.$$

Since $A$ has full column rank, the least squares solution is unique and equals

$$\hat x=A^{+}\begin{bmatrix}2\\ 1\\ 2\end{bmatrix}=\begin{bmatrix}1\\ 1\end{bmatrix}.$$

(Check: $A^{\top}A\hat x=(3,3)^{\top}=A^{\top}b$, so $\hat x$ does solve the normal equations.)

*Kjeldevarsel: i fasiten er midtmatrien i formelen $A^{+}=V\Sigma^{+}U^{T}$ trykt som $\begin{bmatrix}\sqrt3&0&0\\ 0&1&0\end{bmatrix}$, men $\Sigma^{+}$ skal ha resiproke singularverdiar: $\begin{bmatrix}1/\sqrt3&0&0\\ 0&1&0\end{bmatrix}$. Med den trykte midtmatrien blir produktet $\begin{bmatrix}1&1&0\\ 0&1&1\end{bmatrix}$, som ikkje er pseudoinversen; den utrekna sluttmatrisa $A^{+}=\frac13\begin{bmatrix}2&1&-1\\ -1&1&2\end{bmatrix}$ og $\hat x=(1,1)$ i fasiten er derimot rette (kontrollrekna med sympy).*

Kildesett: course=TMA4145 term=host year=2006 problem=2 file=tma4145eksh06en.pdf
