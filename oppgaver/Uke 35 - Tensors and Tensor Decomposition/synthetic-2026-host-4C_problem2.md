### **Problem 2** (Kronecker, Khatri–Rao and Hadamard products, 8 points)

Consider the matrices

$$A=\begin{pmatrix}1&2\\ 3&4\end{pmatrix},\qquad B=\begin{pmatrix}1&0\\ 2&1\end{pmatrix},\qquad C=\begin{pmatrix}0&1\\ 1&1\end{pmatrix}.$$

a) Compute the Kronecker product $A\otimes B\in\mathbb{R}^{4\times 4}$, defined blockwise by $A\otimes B=(a_{i,j}B)_{i,j}$.

b) Compute the Khatri–Rao product $A\odot C\in\mathbb{R}^{4\times 2}$, defined columnwise by stacking the Kronecker products of corresponding columns, $A\odot C=\begin{pmatrix}\mathbf{a}_1\otimes\mathbf{c}_1&\mathbf{a}_2\otimes\mathbf{c}_2\end{pmatrix}$.

c) Compute the Hadamard (entrywise) product $A\circ C$ with entries $(A\circ C)_{i,j}=a_{i,j}c_{i,j}$.

d) Verify by direct computation that

$$(A\odot C)^{\top}(A\odot C)=(A^{\top}A)\circ(C^{\top}C).$$

e) In the ALS algorithm for the CP decomposition one repeatedly solves least-squares problems whose normal equations involve the Gram matrix $(C\odot B)^{\top}(C\odot B)$. In view of d), why is this Gram matrix cheap to assemble for large tensors?
