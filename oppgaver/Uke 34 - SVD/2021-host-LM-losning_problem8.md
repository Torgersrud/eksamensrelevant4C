### **Solution to Problem 8**

We start by finding the singular values of $A$. We have

$$A^{*}A=\begin{bmatrix}10&10\\ 10&10\end{bmatrix},$$

and thus the eigenvalues of $A^{*}A$ are the roots of the characteristic polynomial

$$\det(A^{*}A-\lambda I)=(10-\lambda)^2-10^2=\lambda(\lambda-20).$$

This gives the singular values $\sigma_1^2=20$ and $\sigma_2^2=0$. We find the corresponding eigenvectors:

$$\begin{bmatrix}10-\sigma_1^2&10\\ 10&10-\sigma_1^2\end{bmatrix}v_1=\begin{bmatrix}-10&10\\ 10&-10\end{bmatrix}v_1=\begin{pmatrix}0\\ 0\end{pmatrix}\quad\Rightarrow\quad v_1=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ 1\end{pmatrix},$$

$$\begin{bmatrix}10-\sigma_2^2&10\\ 10&10-\sigma_2^2\end{bmatrix}v_2=\begin{bmatrix}10&10\\ 10&10\end{bmatrix}v_2=\begin{pmatrix}0\\ 0\end{pmatrix}\quad\Rightarrow\quad v_2=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ -1\end{pmatrix}.$$

Thus, a singular value decomposition of $A$ is of the form $A=U\Sigma V^{*}$, where we may choose

$$\Sigma=\begin{bmatrix}\sqrt{20}&0\\ 0&0\end{bmatrix}\qquad\text{and}\qquad V=\frac{1}{\sqrt{2}}\begin{bmatrix}1&1\\ 1&-1\end{bmatrix}.$$

Finally, we determine the columns of $U$. The first column is given by

$$u_1=\frac{1}{\sigma_1}Av_1=\frac{1}{\sqrt{20}}\begin{bmatrix}1&1\\ 3&3\end{bmatrix}\begin{pmatrix}1/\sqrt{2}\\ 1/\sqrt{2}\end{pmatrix}=\frac{1}{\sqrt{10}}\begin{pmatrix}1\\ 3\end{pmatrix}.$$

For the second column, we may choose anything orthogonal to $u_1$, for instance $u_2=(1/\sqrt{10})(3,-1)^{\top}$. This choice gives the matrix

$$U=\frac{1}{\sqrt{10}}\begin{bmatrix}1&3\\ 3&-1\end{bmatrix}$$

A polar decomposition of $A$ is given by

$$A=U\Sigma V^{*}=UV^{*}V\Sigma V^{*}=WP,$$

with $W=UV^{*}$ and $P=V\Sigma V^{*}$. With the matrices $U$, $\Sigma$ and $V$ as given above, we thus find

$$W=UV^{*}=\frac{1}{\sqrt{20}}\begin{bmatrix}4&-2\\ 2&4\end{bmatrix}=\frac{1}{\sqrt{5}}\begin{bmatrix}2&-1\\ 1&2\end{bmatrix},$$

and

$$P=V\Sigma V^{*}=\sqrt{5}\begin{bmatrix}1&1\\ 1&1\end{bmatrix}.$$

Kildesett: course=TMA4145 term=host year=2021 problem=8 file=tma4145_2021eng.pdf
