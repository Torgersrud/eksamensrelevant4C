### **Solution to Problem 4**

There are two basic methods to solve this: either find an orthonormal basis for $W$ and use the projection formula or use the method of least–squares. Both begin in the same way.

The subspace $W$ is described in the question as the null space of a matrix. We need to describe it as the image of a matrix, or find a basis for it. To do this, we run Gaussian Elimination on the matrix in the question. The resulting row reduced form is:

$$\begin{bmatrix}1&-1&0&-2\\ 0&0&1&-1\\ 0&0&0&0\\ 0&0&0&0\end{bmatrix}$$

A basis for the null space is thus:

$$\left\{\begin{bmatrix}2\\ 0\\ 1\\ 1\end{bmatrix},\begin{bmatrix}1\\ 1\\ 0\\ 0\end{bmatrix}\right\}$$

and so $W$ is the image of the matrix

$$\begin{bmatrix}2&1\\ 0&1\\ 1&0\\ 1&0\end{bmatrix}$$

At this point, we could orthonormalise the basis or use the method of leastsquares using the matrix. Swapping and then orthonormalising leads to the vectors

$$\left\{\frac{1}{\sqrt{2}}\begin{bmatrix}1\\ 1\\ 0\\ 0\end{bmatrix},\frac{1}{2}\begin{bmatrix}1\\ -1\\ 1\\ 1\end{bmatrix}\right\}$$

(the swap is to get a “nice” orthonormal basis). Then our closest point is:

$$\left\langle\frac{1}{\sqrt{2}}\begin{bmatrix}1\\ 1\\ 0\\ 0\end{bmatrix},\begin{bmatrix}7\\ -5\\ -1\\ -3\end{bmatrix}\right\rangle\frac{1}{\sqrt{2}}\begin{bmatrix}1\\ 1\\ 0\\ 0\end{bmatrix}+\left\langle\frac{1}{2}\begin{bmatrix}1\\ -1\\ 1\\ 1\end{bmatrix},\begin{bmatrix}7\\ -5\\ -1\\ -3\end{bmatrix}\right\rangle\frac{1}{2}\begin{bmatrix}1\\ -1\\ 1\\ 1\end{bmatrix}=\frac{1}{2}2\begin{bmatrix}1\\ 1\\ 0\\ 0\end{bmatrix}+\frac{1}{4}8\begin{bmatrix}1\\ -1\\ 1\\ 1\end{bmatrix}=\begin{bmatrix}3\\ -1\\ 2\\ 2\end{bmatrix}$$

Proceeding via least–squares, we solve $A^{T}Ax=A^{T}b$ where $A$ is the matrix whose image is $W$ and $b$ is the vector in the question. This leads us to:

$$\begin{bmatrix}6&2\\ 2&2\end{bmatrix}\begin{bmatrix}x\\ y\end{bmatrix}=\begin{bmatrix}10\\ 2\end{bmatrix}$$

The appropriate Gaussian Elimination leads to the solution $\begin{bmatrix}2\\ -1\end{bmatrix}$. Applying $A$ yields the closest point as:

$$\begin{bmatrix}3\\ -1\\ 2\\ 2\end{bmatrix}$$

as before.

Kildesett: course=TMA4145 term=host year=2010 problem=4 file=tma4145eksh10en.pdf
