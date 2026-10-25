### **Solution to Problem 1**

**Solution.**

a) Given an $m\times n$-matrix $A$ with rank $r$, the singular value decomposition states that we can find a unitary $m\times m$ matrix U, a unitary $n\times n$ matrix $V$ and a diagonal $m\times n$ matrix $\Sigma$ such that

$$A=U\Sigma V^{*}.$$

$\Sigma$ has the singular values $\sigma_1,\sigma_2,...,\sigma_r$ of $A$ (i.e. the square roots of the eigenvalues of either $A^{*}A$ or $AA^{*}$) in the first $r$ entries of the diagonal and zeros elsewhere.

b) Recall that the singular values of $A$ are the eigenvalues of $A^{*}A$, or equivalently of $AA^{*}$. We will use $A^{*}A$. First note that

$$A^{*}=\begin{pmatrix}1&-1&0\\ 0&1&1\\ -1&0&1\end{pmatrix},$$

and then calculate that

$$A^{*}A=\begin{pmatrix}2&-1&-1\\ -1&2&1\\ -1&1&2\end{pmatrix}.$$

**Finding $\Sigma$**
To find the eigenvalues $\lambda_i=\sigma_i^2$ of $A^{*}A$ we need to solve $\det(A^{*}A-\lambda I)=0$ for $\lambda$. Written out, this equation is

$$\lambda^{3}-6\lambda^{2}+9\lambda-4=0.$$

The roots of this polynomial are $4,1$ and $1$: by trial and error, one finds that $1$ is a root. By dividing the polynomial $\lambda^{3}-6\lambda^{2}+9\lambda-4$ by $\lambda-1$ we get

$$\frac{\lambda^{3}-6\lambda^{2}+9\lambda-4}{\lambda-1}=\lambda^{2}-5\lambda+4,$$

and this quadratic polynomial has roots $1$ and $4$, which one can find either by inspection or by using the quadratic formula. Therefore the singular values of $A$ are $\sqrt{4}=2,1$ and $1$, so

$$\Sigma=\begin{pmatrix}2&0&0\\ 0&1&0\\ 0&0&1\end{pmatrix}.$$

**Finding $V$:** To find $V$, we need the eigenvectors of $A^{*}A$. We start with $\lambda=4$. The eigenvectors form the solution space for $A-4I=0$, and solving this equation by row reduction gives us the normalized eigenvector

$$v_1=\frac{1}{\sqrt{3}}\begin{pmatrix}1\\ -1\\ -1\end{pmatrix}.$$

A similar calculation for $\lambda=1$ leads to the orthonormal eigenvectors

$$v_2=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ 1\\ 0\end{pmatrix}\qquad v_3=\frac{1}{\sqrt{6}}\begin{pmatrix}1\\ -1\\ 2\end{pmatrix}.$$

The two eigenvectors you first find for $\lambda=1$ might not be orthogonal. In that case you will need to use the Gram-Schmidt method to produce an orthogonal pair of eigenvectors. In conclusion:

$$V=\begin{pmatrix}\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{6}}\\[3pt] -\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{6}}\\[3pt] -\frac{1}{\sqrt{3}}&0&\frac{2}{\sqrt{6}}\end{pmatrix}.$$

**Finding $U$:** The columns $u_1,u_2,u_3$ of $U$ are obtained by $u_i=\frac{1}{\sigma_i}Av_i$, where $\sigma_i$ are the singular values of $A$. By calculating these matrix products we find that

$$u_1=\frac{1}{\sqrt{3}}\begin{pmatrix}1\\ -1\\ -1\end{pmatrix}\qquad u_2=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ 0\\ 1\end{pmatrix}\qquad u_3=\frac{1}{\sqrt{6}}\begin{pmatrix}-1\\ -2\\ 1\end{pmatrix}.$$

Hence

$$U=\begin{pmatrix}\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{6}}\\[3pt] -\frac{1}{\sqrt{3}}&0&-\frac{2}{\sqrt{6}}\\[3pt] -\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{6}}\end{pmatrix}.$$

The singular value decomposition of $A$ is

$$A=U\Sigma V^{*}=\begin{pmatrix}\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{6}}\\[3pt] -\frac{1}{\sqrt{3}}&0&-\frac{2}{\sqrt{6}}\\[3pt] -\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{6}}\end{pmatrix}\begin{pmatrix}2&0&0\\ 0&1&0\\ 0&0&1\end{pmatrix}\begin{pmatrix}\frac{1}{\sqrt{3}}&-\frac{1}{\sqrt{3}}&-\frac{1}{\sqrt{3}}\\[3pt] \frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\\[3pt] \frac{1}{\sqrt{6}}&-\frac{1}{\sqrt{6}}&\frac{2}{\sqrt{6}}\end{pmatrix}.$$

Finally, we use this to express the inverse of $A$. We know that $A=U\Sigma V^{*}$, hence $A^{-1}=(V^{*})^{-1}\Sigma^{-1}U^{-1}$. Luckily, the inverses of the the building blocks of the SVD are easy to find. $U$ and $V^{*}$ are unitary, so their inverses are $U^{*}$ and $(V^{*})^{*}=V$. $\Sigma$ is diagonal, so its inverse is obtained by taking the inverse of the diagonal elements. This means that

$$A^{-1}=(V^{*})^{-1}\Sigma^{-1}U^{-1}=V\Sigma^{-1}U^{*}=\begin{pmatrix}\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{6}}\\[3pt] -\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{6}}\\[3pt] -\frac{1}{\sqrt{3}}&0&\frac{2}{\sqrt{6}}\end{pmatrix}\begin{pmatrix}\frac{1}{2}&0&0\\[3pt] 0&1&0\\[3pt] 0&0&1\end{pmatrix}\begin{pmatrix}\frac{1}{\sqrt{3}}&-\frac{1}{\sqrt{3}}&-\frac{1}{\sqrt{3}}\\[3pt] \frac{1}{\sqrt{2}}&0&\frac{1}{\sqrt{2}}\\[3pt] -\frac{1}{\sqrt{6}}&-\frac{2}{\sqrt{6}}&\frac{1}{\sqrt{6}}\end{pmatrix}.$$

Kildesett: course=TMA4145 term=kont year=2017 problem=1 file=exam_2018_konte_en.pdf
