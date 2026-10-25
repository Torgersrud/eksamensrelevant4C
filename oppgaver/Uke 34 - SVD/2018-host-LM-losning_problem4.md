### **Solution to Problem 4**

a) *Note that there are many possible singular value decompositions $A=U\Sigma V^{*}$. Only the matrix $\Sigma$ is uniquely defined. All correct SVDs are of course equally good answers.*

Seeking a singular value decomposition of $A$, we first find

$$A^{*}A=\begin{bmatrix}9&9\\ 9&9\end{bmatrix}.$$

This matrix has one positive eigenvalue $\sigma_1^2=18$, and one eigenvalue $\sigma_2^2=0$. The eigenvectors corresponding to these eigenvalues are $v_1$ and $v_2$ satisfying

$$A^{*}Av_1=18v_1\ \ \Rightarrow\ \ v_1=\begin{pmatrix}\frac{1}{\sqrt{2}}\\[2pt] \frac{1}{\sqrt{2}}\end{pmatrix}$$

and

$$A^{*}Av_2=0\ \ \Rightarrow\ \ v_2=\begin{pmatrix}\frac{1}{\sqrt{2}}\\[2pt] -\frac{1}{\sqrt{2}}\end{pmatrix},$$

where both eigenvectors are normalized to length one. We thus have

$$\Sigma=\begin{bmatrix}3\sqrt{2}&0\\ 0&0\\ 0&0\end{bmatrix}\quad\text{and}\quad V=\begin{bmatrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\[2pt] \frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}\end{bmatrix}.\tag{3}$$

Finally, we find the matrix $U$. Its first column is $u_1$ given by

$$u_1=\frac{1}{\sigma_1}Av_1=\frac{1}{3\sqrt{2}}\begin{pmatrix}2\sqrt{2}\\ 2\sqrt{2}\\ -\sqrt{2}\end{pmatrix}=\begin{pmatrix}\frac{2}{3}\\[2pt] \frac{2}{3}\\[2pt] -\frac{1}{3}\end{pmatrix}.$$

We can now complete the matrix $U$ by choosing any two orthonormal vectors orthogonal to $u_1$. For $w\in\mathbb{C}^3$, we have that

$$\langle u_1,w\rangle=0\ \ \Rightarrow\ \ w=\begin{pmatrix}-s+t\\ s\\ 2t\end{pmatrix},\quad s,t\in\mathbb{C}.$$

We see that by choosing (for example) $(s=1,t=0)$ and $(s=1,t=2)$, we find the orthogonal vectors

$$\tilde{u}_2=\begin{pmatrix}-1\\ 1\\ 0\end{pmatrix}\quad\text{and }\tilde{u}_3=\begin{pmatrix}1\\ 1\\ 4\end{pmatrix}.$$

Letting $u_2=\tilde{u}_2/\lVert\tilde{u}_2\rVert$ and $u_3=\tilde{u}_3/\lVert\tilde{u}_3\rVert$, we finally get

$$U=\begin{bmatrix}\frac{2}{3}&-\frac{1}{\sqrt{2}}&\frac{1}{3\sqrt{2}}\\[3pt] \frac{2}{3}&\frac{1}{\sqrt{2}}&\frac{1}{3\sqrt{2}}\\[3pt] -\frac{1}{3}&0&\frac{4}{3\sqrt{2}}\end{bmatrix}.\tag{4}$$

We thus have the singular value decomposition $A=U\Sigma V^{*}$, with $U$ given in (4) and $\Sigma$ and $V$ given in (3) (note that only $\Sigma$ is unique).

b) The pseudoinverse $A^{+}$ of $A$ is given by $A^{+}=V\Sigma^{+}U^{*}$, where

$$\Sigma^{+}=\begin{bmatrix}\frac{1}{3\sqrt{2}}&0&0\\[2pt] 0&0&0\end{bmatrix}.$$

We get

$$A^{+}=\begin{bmatrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\[2pt] \frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}\end{bmatrix}\begin{bmatrix}\frac{1}{3\sqrt{2}}&0&0\\[2pt] 0&0&0\end{bmatrix}\begin{bmatrix}\frac{2}{3}&\frac{2}{3}&-\frac{1}{3}\\[3pt] -\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\\[3pt] \frac{1}{3\sqrt{2}}&\frac{1}{3\sqrt{2}}&\frac{4}{3\sqrt{2}}\end{bmatrix}=\frac{1}{18}\begin{bmatrix}2&2&-1\\ 2&2&-1\end{bmatrix}$$

The best approximation to a solution of the inconsistent system

$$2x_1+2x_2=3$$
$$2x_1+2x_2=4$$
$$-x_1-x_2=-4$$

is thus given by

$$z=A^{+}\begin{pmatrix}3\\ 4\\ -4\end{pmatrix}=\frac{1}{18}\begin{bmatrix}2&2&-1\\ 2&2&-1\end{bmatrix}\begin{pmatrix}3\\ 4\\ -4\end{pmatrix}=\begin{pmatrix}1\\ 1\end{pmatrix}.$$

Kildesett: course=TMA4145 term=host year=2018 problem=4 file=tma4145eksh18en.pdf
