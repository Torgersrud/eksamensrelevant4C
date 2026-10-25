### **Solution to Problem 3**

Write $A=QR$ with

$$Q=\begin{bmatrix}1/2&1/2&1/2&1/2\\ 1/2&-1/2&1/2&-1/2\\ 1/2&1/2&-1/2&-1/2\\ 1/2&-1/2&-1/2&1/2\end{bmatrix},\qquad R=\begin{bmatrix}8&-6&0\\ 0&0&5\\ 0&0&0\\ 0&0&0\end{bmatrix}.$$

The columns of $Q$ are orthonormal (all entries are $\pm 1/2$ and distinct columns agree in exactly two positions and disagree in the other two), so $Q^{\top}Q=I$.

**1.** Since $A=QR$ and $Q^{\top}Q=I$,

$$A^{\top}A=(QR)^{\top}(QR)=R^{\top}Q^{\top}QR=R^{\top}R.$$

Multiplying out:

$$R^{\top}R=\begin{bmatrix}64&-48&0\\ -48&36&0\\ 0&0&25\end{bmatrix}.$$

**2.** The vector $\begin{bmatrix}0\\0\\1\end{bmatrix}$ is an eigenvector with eigenvalue $25$. Since $R$ is not injective (its third column is a multiple of its first), $R^{\top}R$ has eigenvalue $0$; looking for its null space gives the eigenvector $\begin{bmatrix}3/5\\4/5\\0\end{bmatrix}$. The third basis vector must be orthogonal to these two, so it is $\begin{bmatrix}4/5\\-3/5\\0\end{bmatrix}$; a direct check gives $R^{\top}R\,(4/5,-3/5,0)^{\top}=(80,-60,0)^{\top}$, so its eigenvalue is $100$. An orthonormal eigenbasis is therefore

$$\left\{\begin{bmatrix}4/5\\-3/5\\0\end{bmatrix},\begin{bmatrix}0\\0\\1\end{bmatrix},\begin{bmatrix}3/5\\4/5\\0\end{bmatrix}\right\}$$

with eigenvalues $100$, $25$ and $0$ respectively.

**3.** Applying $R$ to these basis vectors in the order above gives

$$R\begin{bmatrix}4/5\\-3/5\\0\end{bmatrix}=\begin{bmatrix}10\\0\\0\\0\end{bmatrix},\quad R\begin{bmatrix}0\\0\\1\end{bmatrix}=\begin{bmatrix}0\\5\\0\\0\end{bmatrix},\quad R\begin{bmatrix}3/5\\4/5\\0\end{bmatrix}=\begin{bmatrix}0\\0\\0\\0\end{bmatrix},$$

so we can take the standard basis of $\mathbb{R}^{4}$ as the left singular vectors and write

$$R=\begin{bmatrix}10&0&0\\ 0&5&0\\ 0&0&0\\ 0&0&0\end{bmatrix}\begin{bmatrix}4/5&-3/5&0\\ 0&0&1\\ 3/5&4/5&0\end{bmatrix}.$$

This is a singular value decomposition $R=U\Sigma V^{\top}$ with $U$ the $4\times 4$ identity matrix (the two zero rows of $\Sigma$ allow any completion of the left singular vectors), $\Sigma=\operatorname{diag}(10,5,0)$ of size $4\times 3$, and

$$V^{\top}=\begin{bmatrix}4/5&-3/5&0\\ 0&0&1\\ 3/5&4/5&0\end{bmatrix}.$$

Since $A=QR$, a singular value decomposition of $A$ is thus

$$A=\underbrace{\begin{bmatrix}1/2&1/2&1/2&1/2\\ 1/2&-1/2&1/2&-1/2\\ 1/2&1/2&-1/2&-1/2\\ 1/2&-1/2&-1/2&1/2\end{bmatrix}}_{U}\underbrace{\begin{bmatrix}10&0&0\\ 0&5&0\\ 0&0&0\\ 0&0&0\end{bmatrix}}_{\Sigma}\underbrace{\begin{bmatrix}4/5&-3/5&0\\ 0&0&1\\ 3/5&4/5&0\end{bmatrix}}_{V^{\top}}.$$

*Kjeldevarsel: i fasiten er matrisa $R^{\top}R$ under punkt 1 trykt med $(2,2)$-innhald $64$, men $(-6)\cdot(-6)=36$ — den rette matrisa er $\begin{bmatrix}64&-48&0\\ -48&36&0\\ 0&0&25\end{bmatrix}$ (kontrollrekna med sympy). Eigenvektorane, eigenverdiane og SVD-en i resten av fasiten er konsistente med den rette matrisa og er rette.*

Kildesett: course=TMA4145 term=host year=2009 problem=3 file=tma4145eksh09en.pdf
