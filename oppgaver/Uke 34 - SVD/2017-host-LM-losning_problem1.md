### **Solution to Problem 1**

a) (1) Find the singular value decomposition for the matrix

$$A=\begin{pmatrix}1&1&-1\\ 1&1&-1\end{pmatrix}.$$

**Solution:** Let us compute the singular values of $A$. Recall these are the non-zero eigenvalues of the selfadjoint matrix $AA^{*}=\begin{pmatrix}3&3\\ 3&3\end{pmatrix}$ or $A^{*}A=\begin{pmatrix}2&2&-2\\ 2&2&-2\\ -2&-2&2\end{pmatrix}$. In the first case we get a $2\times 2$-matrix and in the second case we get a $3\times 3$-matrix, so we use $AA^{*}$ for the computation of the singular values. The eigenvalues of $\begin{pmatrix}3&3\\ 3&3\end{pmatrix}$ are $6$ and $0$. For those, who have decided to use $A^{*}A$: the eigenvalues are $6,0,0$. Hence $\sigma_1=\sqrt{6}$ is the only singular value of $A$, which fits very well with the fact that $A$ has rank one.

Consequently $\Sigma$ is given by

$$\Sigma=\begin{pmatrix}\sqrt{6}&0&0\\ 0&0&0\end{pmatrix}.$$

Let us look at the eigenvectors of $A^{*}A$. A little bit of computation yields

$$v_1=\frac{1}{\sqrt{3}}\begin{pmatrix}1\\ 1\\ -1\end{pmatrix},\ v_2=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ -1\\ 0\end{pmatrix},\ v_3=\frac{1}{\sqrt{6}}\begin{pmatrix}1\\ 1\\ 2\end{pmatrix}.$$

The set $\{v_1,v_2,v_3\}$ is an orthonormal basis of $\mathbb{R}^3$ and yield the columns of $V$:

$$V=\begin{pmatrix}\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{6}}\\[3pt] \frac{1}{\sqrt{3}}&-\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{6}}\\[3pt] -\frac{1}{\sqrt{3}}&0&\frac{2}{\sqrt{6}}\end{pmatrix}.$$

Now we get the columns of $U$, which is an orthonormal basis for $\mathbb{R}^2$, by

$$u_1=\frac{1}{\sigma_1}Av_1=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ 1\end{pmatrix}$$

and choosing another vector orthogonal to $v_1$, such as $u_2=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ -1\end{pmatrix}$

and thus

$$U=\begin{pmatrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\[3pt] \frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}\end{pmatrix}.$$

Hence $A=U\Sigma V^{*}=\begin{pmatrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\[3pt] \frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}\end{pmatrix}\begin{pmatrix}\sqrt{6}&0&0\\ 0&0&0\end{pmatrix}\begin{pmatrix}\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{3}}&-\frac{1}{\sqrt{3}}\\[3pt] \frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}&0\\[3pt] \frac{1}{\sqrt{6}}&\frac{1}{\sqrt{6}}&\frac{2}{\sqrt{6}}\end{pmatrix}$.

(2) The linear system:

$$x_1+x_2-x_3=1$$
$$x_1+x_2-x_3=1$$

has infinitely many solutions. Determine the one with the minimal Euclidean norm $\lVert.\rVert_2$.

The linear system

$$x_1+x_2-x_3=1$$
$$x_1+x_2-x_3=2$$

has no solution. Determine the least squares solution of the linear system.

Hint: The pseudoinverse of the matrix related to the linear system might be useful.

**Solution:** We first compute the pseudoinverse of $A$: The pseudoinverse in terms of the SVD is given by $A^{+}=V\Sigma^{+}U^{*}$, which gives

$$A^{+}=\begin{pmatrix}\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{3}}&\frac{1}{\sqrt{3}}\\[3pt] \frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}&0\\[3pt] -\frac{1}{\sqrt{6}}&\frac{1}{\sqrt{6}}&\frac{2}{\sqrt{6}}\end{pmatrix}\begin{pmatrix}\frac{1}{\sqrt{6}}&0\\[3pt] 0&0\\[3pt] 0&0\end{pmatrix}\begin{pmatrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\[3pt] \frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}\end{pmatrix}=\frac{1}{6}\begin{pmatrix}1&1\\ 1&1\\ -1&-1\end{pmatrix}.$$

The system

$$x_1+x_2-x_3=1$$
$$x_1+x_2-x_3=1$$

has infinitely many solutions and we have learned that $A^{+}\begin{pmatrix}1\\ 1\end{pmatrix}=\frac{1}{3}\begin{pmatrix}1\\ 1\\ -1\end{pmatrix}$ is the solution of minimal $\lVert.\rVert_2$-norm. The system

$$x_1+x_2-x_3=1$$
$$x_1+x_2-x_3=2$$

has no solution, but $A^{+}\begin{pmatrix}1\\ 2\end{pmatrix}=\frac{1}{2}\begin{pmatrix}1\\ 1\\ -1\end{pmatrix}$ is the best approximation to a solution having minimal norm.

b) Given a $n\times n$-matrix $A$ of rank $n$. Prove that $A$ has a polar decomposition using the singular value decomposition of $A$. Hence, show that there exist an $n\times n$ unitary matrix $W$ and a positive definite $n\times n$ matrix $P$ such that $A=WP$.

**Solution:** The SVD decomposition gives us unitary $n\times n$ matrices $U$ and $V$ such that

$$A=U\Sigma V^{*}=UV^{*}V\Sigma V^{*}.$$

Note that $UV^{*}$ is unitary as a product of two unitary matrices and $V\Sigma V^{*}$ is positive definite, since $\Sigma$ is positive definite. Hence $V\Sigma V^{*}$ is the replacement of the length of a complex number and $UV^{*}$ the one for the phase factor.

Kildesett: course=TMA4145 term=host year=2017 problem=1 file=exam_2017_en.pdf
