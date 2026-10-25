### **Solution to Problem 6**

**a)** The matrix $A$ is normal if $A^{*}A=AA^{*}$, where $A^{*}=\overline{A}^{\top}=A^{\top}$. Here we have

$$A^{*}A=\begin{bmatrix}1&2\\ 1&-2\end{bmatrix}\begin{bmatrix}1&1\\ 2&-2\end{bmatrix}=\begin{bmatrix}5&-3\\ -3&5\end{bmatrix},$$

whereas

$$AA^{*}=\begin{bmatrix}1&1\\ 2&-2\end{bmatrix}\begin{bmatrix}1&2\\ 1&-2\end{bmatrix}=\begin{bmatrix}2&0\\ 0&8\end{bmatrix},$$

so $A$ is *not* normal.

The singular values $\sigma_i$ of $A$ are the square roots of the eigenvalues $\sigma_i^2$ of the matrix $A^{*}A$, or equivalently $AA^{*}$. From the calculations above, we see directly that

$$\sigma_1=\sqrt{8}=2\sqrt{2}\ \quad\text{and}\quad\sigma_2=\sqrt{2}.$$

Finally, the operator norm $\|A\|$ equals the maximal singular value of $A$, so

$$\|A\|=2\sqrt{2}.$$

**b)** The singular value decomposition of $A$ is given by

$$A=U\Sigma V^{*},$$

where

$$\Sigma=\begin{bmatrix}\sigma_1&0\\ 0&\sigma_2\end{bmatrix}=\begin{bmatrix}2\sqrt{2}&0\\ 0&\sqrt{2}\end{bmatrix},$$

and $U$ and $V$ are $(2\times 2)$ unitary matrices. The columns of $V$ are the normalized eigenvectors of $A^{*}A$ corresponding to the eigenvalues $\sigma_1^2$ and $\sigma_2^2$. We find

$$A^{*}Av_1=\sigma_1^2v_1\quad\Rightarrow\quad v_1=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ -1\end{pmatrix},$$

and

$$A^{*}Av_2=\sigma_2^2v_2\quad\Rightarrow\quad v_2=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ 1\end{pmatrix},$$

and thus

$$V=\begin{bmatrix}1/\sqrt{2}&1/\sqrt{2}\\ -1/\sqrt{2}&1/\sqrt{2}\end{bmatrix}.$$

Finally, the columns of $U$ are given by $Av_1/\sigma_1$ and $Av_2/\sigma_2$. We have

$$\frac{1}{\sigma_1}Av_1=\frac{1}{2\sqrt{2}}\begin{bmatrix}1&1\\ 2&-2\end{bmatrix}\begin{pmatrix}1/\sqrt{2}\\ -1/\sqrt{2}\end{pmatrix}=\begin{pmatrix}0\\ 1\end{pmatrix},$$

and

$$\frac{1}{\sigma_2}Av_2=\frac{1}{\sqrt{2}}\begin{bmatrix}1&1\\ 2&-2\end{bmatrix}\begin{pmatrix}1/\sqrt{2}\\ 1/\sqrt{2}\end{pmatrix}=\begin{pmatrix}1\\ 0\end{pmatrix},$$

and thus

$$U=\begin{bmatrix}0&1\\ 1&0\end{bmatrix}.$$

Summarized, we have $A=U\Sigma V^{*}$, where

$$U=\begin{bmatrix}0&1\\ 1&0\end{bmatrix},\quad\Sigma=\begin{bmatrix}2\sqrt{2}&0\\ 0&\sqrt{2}\end{bmatrix},\quad\text{and}\quad V=\begin{bmatrix}1/\sqrt{2}&1/\sqrt{2}\\ -1/\sqrt{2}&1/\sqrt{2}\end{bmatrix}.$$

(Note that this factorization is not unique.)

**c)** We have that

$$A=U\Sigma V^{*}=UV^{*}V\Sigma V^{*}=WP,$$

where $W=UV^{*}$ is unitary and $P=V\Sigma V^{*}$ is positive semi-definite. This is the polar decomposition of $A$. Using the matrices we found in **b)** we find that

$$W=UV^{*}=\begin{bmatrix}0&1\\ 1&0\end{bmatrix}\begin{bmatrix}1/\sqrt{2}&-1/\sqrt{2}\\ 1/\sqrt{2}&1/\sqrt{2}\end{bmatrix}=\begin{bmatrix}1/\sqrt{2}&1/\sqrt{2}\\ 1/\sqrt{2}&-1/\sqrt{2}\end{bmatrix},$$

and

$$P=V\Sigma V^{*}=\begin{bmatrix}1/\sqrt{2}&1/\sqrt{2}\\ -1/\sqrt{2}&1/\sqrt{2}\end{bmatrix}\begin{bmatrix}2\sqrt{2}&0\\ 0&\sqrt{2}\end{bmatrix}\begin{bmatrix}1/\sqrt{2}&-1/\sqrt{2}\\ 1/\sqrt{2}&1/\sqrt{2}\end{bmatrix}=\frac{1}{\sqrt{2}}\begin{bmatrix}3&-1\\ -1&3\end{bmatrix}.$$

(Note that this factorization *is* unique, since $A$ is invertible.)

Kildesett: course=TMA4145 term=host year=2020 problem=6 file=tma4145english_cut.pdf
