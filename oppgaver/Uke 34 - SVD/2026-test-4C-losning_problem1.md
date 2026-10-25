### **Solution to Problem 1** (Moore-Penrose inverse, 10 points)

a) We use the smaller matrix $A^{\top}A\in\mathbb{R}^{2\times 2}$,

$$A^{\top}A=\begin{pmatrix}27&6\\ 6&18\end{pmatrix}$$

with characteristic polynomial

$$\det(A^{\top}A-\lambda\,\mathrm{I}_{2\times 2})=(27-\lambda)(18-\lambda)-36=\lambda^{2}-45\lambda+450.$$

Its zeros are $\lambda_{1,2}=\frac{45\pm\sqrt{2025-1800}}{2}=\frac{45\pm 15}{2}$, i. e. $\lambda_1=30$ and $\lambda_2=15$, so the singular values are $\sigma_1=\sqrt{30}$ and $\sigma_2=\sqrt{15}$ and (1 P.)

$$\Sigma=\begin{pmatrix}\sqrt{30}&0\\ 0&\sqrt{15}\end{pmatrix}.$$

For the eigenvectors of $A^{\top}A$ we consider

$$A^{\top}A-30\,\mathrm{I}_{2\times 2}=\begin{pmatrix}-3&6\\ 6&-12\end{pmatrix}\quad\text{and}\quad A^{\top}A-15\,\mathrm{I}_{2\times 2}=\begin{pmatrix}12&6\\ 6&3\end{pmatrix}.$$

In the first matrix twice the first column plus the second column is zero, in the second matrix twice the second column minus the first column is zero, hence (2 P.)

$$\mathbf{v}_1=\frac{1}{\sqrt{5}}\begin{pmatrix}2\\ 1\end{pmatrix},\quad \mathbf{v}_2=\frac{1}{\sqrt{5}}\begin{pmatrix}-1\\ 2\end{pmatrix},\quad\text{and}\quad V=\frac{1}{\sqrt{5}}\begin{pmatrix}2&-1\\ 1&2\end{pmatrix}.$$

From $A=U\Sigma V^{\top}$ we obtain (1 P.)

$$U=AV\Sigma^{-1}=\frac{1}{\sqrt{5}}\begin{pmatrix}-5&5\\ 0&-5\\ 5&5\\ 10&0\end{pmatrix}\begin{pmatrix}\frac{1}{\sqrt{30}}&0\\ 0&\frac{1}{\sqrt{15}}\end{pmatrix}=\frac{1}{\sqrt{6}}\begin{pmatrix}-1&\sqrt{2}\\ 0&-\sqrt{2}\\ 1&\sqrt{2}\\ 2&0\end{pmatrix},$$

i. e. $\mathbf{u}_1=\frac{1}{\sqrt{6}}(-1,0,1,2)^{\top}$ and $\mathbf{u}_2=\frac{1}{\sqrt{3}}(1,-1,1,0)^{\top}$. The reduced SVD of $A$ reads

$$A=U\Sigma V^{\top}=\frac{1}{\sqrt{6}}\begin{pmatrix}-1&\sqrt{2}\\ 0&-\sqrt{2}\\ 1&\sqrt{2}\\ 2&0\end{pmatrix}\begin{pmatrix}\sqrt{30}&0\\ 0&\sqrt{15}\end{pmatrix}\frac{1}{\sqrt{5}}\begin{pmatrix}2&1\\ -1&2\end{pmatrix}.$$

b) There are two ways to see this. Either of them gives the points. (2 P.)

*Using the SVD from the first part.* By definition we have

$$A^{\dagger}=V\Sigma^{-1}U^{\top}=\frac{1}{\sigma_1}\mathbf{v}_1\mathbf{u}_1^{\top}+\frac{1}{\sigma_2}\mathbf{v}_2\mathbf{u}_2^{\top},$$

where the two terms are

$$\frac{1}{\sqrt{30}}\mathbf{v}_1\mathbf{u}_1^{\top}=\frac{1}{30}\begin{pmatrix}-2&0&2&4\\ -1&0&1&2\end{pmatrix}\quad\text{and}\quad\frac{1}{\sqrt{15}}\mathbf{v}_2\mathbf{u}_2^{\top}=\frac{1}{15}\begin{pmatrix}-1&1&-1&0\\ 2&-2&2&0\end{pmatrix}.$$

With the common denominator $30$ their sum is

$$A^{\dagger}=\frac{1}{30}\left(\begin{pmatrix}-2&0&2&4\\ -1&0&1&2\end{pmatrix}+\begin{pmatrix}-2&2&-2&0\\ 4&-4&4&0\end{pmatrix}\right)=\frac{1}{30}\begin{pmatrix}-4&2&0&4\\ 3&-4&5&2\end{pmatrix}.$$

*Checking the properties of the Moore-Penrose inverse.* Denote the given matrix by $B$. Since $A$ has full rank, it suffices to check the two properties

$$ABA=A\qquad\text{and}\qquad(AB)^{\top}=AB$$

of the Moore-Penrose inverse. We compute

$$BA=\frac{1}{30}\begin{pmatrix}-4&2&0&4\\ 3&-4&5&2\end{pmatrix}\begin{pmatrix}-3&1\\ 1&-2\\ 1&3\\ 4&2\end{pmatrix}=\frac{1}{30}\begin{pmatrix}30&0\\ 0&30\end{pmatrix}=\mathrm{I}_{2\times 2},$$

hence $ABA=A$, and

$$AB=\frac{1}{6}\begin{pmatrix}3&-2&1&-2\\ -2&2&-2&0\\ 1&-2&3&2\\ -2&0&2&4\end{pmatrix},$$

which is symmetric. Hence $B=A^{\dagger}$. Note that in general also $BAB=B$ and $(BA)^{\top}=BA$ are necessary; here they follow from $BA=\mathrm{I}_{2\times 2}$.

c) Since $A$ has full rank, the vector of smallest error is $\mathbf{x}=A^{\dagger}\mathbf{b}$. We obtain

$$\mathbf{x}=A^{\dagger}\mathbf{b}=\frac{1}{30}\begin{pmatrix}-4&2&0&4\\ 3&-4&5&2\end{pmatrix}\begin{pmatrix}3\\ -3\\ 3\\ -3\end{pmatrix}=\frac{1}{30}\begin{pmatrix}-30\\ 30\end{pmatrix}=\begin{pmatrix}-1\\ 1\end{pmatrix}.$$

For the error we have

$$A\mathbf{x}-\mathbf{b}=\begin{pmatrix}4\\ -3\\ 2\\ -2\end{pmatrix}-\begin{pmatrix}3\\ -3\\ 3\\ -3\end{pmatrix}=\begin{pmatrix}1\\ 0\\ -1\\ 1\end{pmatrix},$$

so the error is $\|A\mathbf{x}-\mathbf{b}\|_2=\sqrt{1+0+1+1}=\sqrt{3}$. (2 P.)

d) Transposing the SVD yields the reduced SVD $A^{\top}=V\Sigma U^{\top}$, with the roles of $U$ and $V$ switched. Hence

$$(A^{\top})^{\dagger}=U\Sigma^{-1}V^{\top}=\left(V\Sigma^{-1}U^{\top}\right)^{\top}=(A^{\dagger})^{\top}=\frac{1}{30}\begin{pmatrix}-4&3\\ 2&-4\\ 0&5\\ 4&2\end{pmatrix}.$$

For the given $\mathbf{c}$ we obtain

$$\mathbf{y}=(A^{\top})^{\dagger}\mathbf{c}=\frac{1}{30}\begin{pmatrix}-4&3\\ 2&-4\\ 0&5\\ 4&2\end{pmatrix}\begin{pmatrix}-3\\ 6\end{pmatrix}=\frac{1}{30}\begin{pmatrix}30\\ -30\\ 30\\ 0\end{pmatrix}=\begin{pmatrix}1\\ -1\\ 1\\ 0\end{pmatrix}.$$

Since $A^{\top}\in\mathbb{R}^{2\times 4}$ has full rank, the system $A^{\top}\mathbf{y}=\mathbf{c}$ has infinitely many solutions. The vector $\mathbf{y}$ is one of them, since $A^{\top}(A^{\top})^{\dagger}=(A^{\dagger}A)^{\top}=\mathrm{I}_{2\times 2}$, namely the one of smallest norm, $\|\mathbf{y}\|_2=\sqrt{3}$. (2 P.)

Kildesett: course=TMA4432 term=test year=2026 problem=1 points=10 file=test-exam-math4c_web.pdf
