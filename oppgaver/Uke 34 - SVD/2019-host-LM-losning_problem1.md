### **Solution to Problem 1**

a) We provide examples of matrices $U,\Sigma,V$ such that $A=U\Sigma V^{*}$.

$$A^{*}A=\begin{pmatrix}2&2&0\\ 2&2&0\\ 0&0&2\end{pmatrix}\qquad\text{and}\qquad AA^{*}=\begin{pmatrix}3&-1\\ -1&3\end{pmatrix},$$

singular values: $\sigma_1=2$, $\sigma_2=\sqrt{2}$ and $\sigma_3=0$

$$\Sigma=\begin{pmatrix}2&0&0\\ 0&\sqrt{2}&0\end{pmatrix}$$

Eigenvector $v_1$ of $A^{*}A$ for eigenvalue $2$: $v_1=\begin{pmatrix}1\\ 1\\ 0\end{pmatrix}$.

Eigenvector $v_2$ of $A^{*}A$ for eigenvalue $2$: $v_2=\begin{pmatrix}0\\ 0\\ 1\end{pmatrix}$.

Eigenvector $v_1$ of $A^{*}A$ for eigenvalue $0$: $v_3=\begin{pmatrix}-1\\ 1\\ 0\end{pmatrix}$.

$$V=\frac{1}{\sqrt{2}}\begin{pmatrix}1&0&-1\\ 1&0&1\\ 0&\sqrt{2}&0\end{pmatrix}.$$

$u_1=\frac{1}{\sigma_1}Av_1=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ -1\end{pmatrix}$ and $u_2=\frac{1}{\sigma_2}Av_2=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ 1\end{pmatrix}$

$$U=\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\ -1&1\end{pmatrix}.$$

b) Pseudoinverse $A^{+}=V^{*}\Sigma^{+}U$ is $\frac{1}{4}\begin{pmatrix}1&-1\\ 1&-1\\ 2&2\end{pmatrix}$ for $\Sigma^{+}=\begin{pmatrix}1/2&0\\ 0&1/\sqrt{2}\\ 0&0\end{pmatrix}$ and hence $x^{+}=A^{+}b=\begin{pmatrix}1/2\\ 1/2\\ 0\end{pmatrix}$ for $b=\begin{pmatrix}1\\ -1\end{pmatrix}$.

Kildesett: course=TMA4145 term=host year=2019 problem=1 file=tma4105eksamen-engelsk.pdf
