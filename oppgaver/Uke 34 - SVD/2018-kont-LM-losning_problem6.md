### **Solution to Problem 6**

a) *Note that there are several possible singular value decompositions $A=U\Sigma V^{*}$. Only the matrix $\Sigma$ is uniquely defined. All correct SVDs are of course equally good answers.*

Seeking a singular value decomposition of $A$, we first find

$$A^{*}A=\begin{bmatrix}5&0&-3\\ 0&0&0\\ -3&0&5\end{bmatrix}.$$

The positive eigenvalues of this matrix are $\sigma_1^2=8$ and $\sigma_2^2=2$. The final eigenvalue is $\sigma_3^2=0$. Since $A^{*}A$ is self-adjoint, the corresponding eigenvectors are necessarily orthogonal. These are:

$$A^{*}Av_1=8v_1\ \ \Rightarrow\ \ v_1=\begin{pmatrix}\frac{1}{\sqrt{2}}\\[2pt] 0\\[2pt] -\frac{1}{\sqrt{2}}\end{pmatrix}$$

$$A^{*}Av_2=2v_2\ \ \Rightarrow\ \ v_2=\begin{pmatrix}\frac{1}{\sqrt{2}}\\[2pt] 0\\[2pt] \frac{1}{\sqrt{2}}\end{pmatrix}$$

$$A^{*}Av_3=0v_3\ \ \Rightarrow\ \ v_3=\begin{pmatrix}0\\ 1\\ 0\end{pmatrix}$$

All eigenvectors above are normalized to length one. We thus get

$$\Sigma=\begin{bmatrix}\sqrt{8}&0&0\\ 0&\sqrt{2}&0\end{bmatrix}\quad\text{and }\quad V=\begin{bmatrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\\[3pt] 0&0&1\\[3pt] -\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\end{bmatrix}.\tag{1}$$

Finally, we find the matrix $U$. Its first column $u_1$ is given by

$$u_1=\frac{1}{\sigma_1}Av_1=\frac{1}{\sqrt{8}}\begin{pmatrix}0\\ 2\sqrt{2}\end{pmatrix}=\begin{pmatrix}0\\ 1\end{pmatrix},$$

and its second column $u_2$ by

$$u_2=\frac{1}{\sigma_2}Av_2=\frac{1}{\sqrt{2}}\begin{pmatrix}\sqrt{2}\\ 0\end{pmatrix}=\begin{pmatrix}1\\ 0\end{pmatrix}.$$

We get

$$U=\begin{bmatrix}0&1\\ 1&0\end{bmatrix},\tag{2}$$

and thus we have the singular value decomposition $A=U\Sigma V^{*}$, with $U$ given in (2) and $\Sigma$ and $V$ given in (1) (note again that only $\Sigma$ is unique).

b) The pseudoinverse $A^{+}$ of $A$ is given by $A^{+}=V\Sigma^{+}U^{*}$, where

$$\Sigma^{+}=\begin{bmatrix}\frac{1}{\sqrt{8}}&0\\[3pt] 0&\frac{1}{\sqrt{2}}\\[3pt] 0&0\end{bmatrix}.$$

We get

$$A^{+}=\begin{bmatrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\\[3pt] 0&0&1\\[3pt] -\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\end{bmatrix}\begin{bmatrix}\frac{1}{\sqrt{8}}&0\\[3pt] 0&\frac{1}{\sqrt{2}}\\[3pt] 0&0\end{bmatrix}\begin{bmatrix}0&1\\ 1&0\end{bmatrix}=\begin{bmatrix}\frac{1}{2}&\frac{1}{4}\\[3pt] 0&0\\[3pt] \frac{1}{2}&-\frac{1}{4}\end{bmatrix}.$$

The minimal norm solution of the system

$$x_1+0x_2+x_3=1$$
$$2x_1+0x_2-2x_3=4$$

is thus given by

$$\begin{pmatrix}x_1\\ x_2\\ x_3\end{pmatrix}=A^{+}\begin{pmatrix}1\\ 4\end{pmatrix}=\begin{bmatrix}\frac{1}{2}&\frac{1}{4}\\[3pt] 0&0\\[3pt] \frac{1}{2}&-\frac{1}{4}\end{bmatrix}\begin{pmatrix}1\\ 4\end{pmatrix}=\begin{pmatrix}\frac{3}{2}\\[2pt] 0\\[2pt] -\frac{1}{2}\end{pmatrix}.$$

Kildesett: course=TMA4145 term=kont year=2018 problem=6 file=tma4145_english.pdf
