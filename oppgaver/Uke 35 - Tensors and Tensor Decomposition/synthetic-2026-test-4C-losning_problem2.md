### **Solution to Problem 2** (Kronecker, Khatri–Rao and Hadamard products, 8 points)

a) Multiplying each entry of $A$ by the full matrix $B$,

$$A\otimes B=\begin{pmatrix}1\cdot B&2\cdot B\\ 3\cdot B&4\cdot B\end{pmatrix}=\begin{pmatrix}1&0&2&0\\ 2&1&4&2\\ 3&0&4&0\\ 6&3&8&4\end{pmatrix}.$$ (2 P.)

b) With $\mathbf{a}_1=(1,3)^{\top}$, $\mathbf{a}_2=(2,4)^{\top}$, $\mathbf{c}_1=(0,1)^{\top}$, $\mathbf{c}_2=(1,1)^{\top}$,

$$\mathbf{a}_1\otimes\mathbf{c}_1=\begin{pmatrix}1\cdot\mathbf{c}_1\\ 3\cdot\mathbf{c}_1\end{pmatrix}=\begin{pmatrix}0\\ 1\\ 0\\ 3\end{pmatrix},\qquad \mathbf{a}_2\otimes\mathbf{c}_2=\begin{pmatrix}2\\ 2\\ 4\\ 4\end{pmatrix},\qquad A\odot C=\begin{pmatrix}0&2\\ 1&2\\ 0&4\\ 3&4\end{pmatrix}.$$ (2 P.)

c) Entry by entry,

$$A\circ C=\begin{pmatrix}1\cdot 0&2\cdot 1\\ 3\cdot 1&4\cdot 1\end{pmatrix}=\begin{pmatrix}0&2\\ 3&4\end{pmatrix}.$$ (1 P.)

d) From b),

$$(A\odot C)^{\top}(A\odot C)=\begin{pmatrix}0&1&0&3\\ 2&2&4&4\end{pmatrix}\begin{pmatrix}0&2\\ 1&2\\ 0&4\\ 3&4\end{pmatrix}=\begin{pmatrix}10&14\\ 14&40\end{pmatrix},$$

using $0+1+0+9=10$, $0+2+0+12=14$ and $4+4+16+16=40$. On the other side,

$$A^{\top}A=\begin{pmatrix}10&14\\ 14&20\end{pmatrix},\qquad C^{\top}C=\begin{pmatrix}1&1\\ 1&2\end{pmatrix},\qquad (A^{\top}A)\circ(C^{\top}C)=\begin{pmatrix}10&14\\ 14&40\end{pmatrix},$$

and the two matrices agree. (2 P.)

e) The identity says the Gram matrix of the Khatri–Rao product is the Hadamard product of the Gram matrices. Instead of forming $C\odot B$, which has $np$ rows (one entry per data point, huge for real tensors), one only needs the small $r\times r$ Gram matrices $B^{\top}B$ and $C^{\top}C$ and their entrywise product — a cost independent of the tensor size, which is what makes each ALS least-squares step affordable. (1 P.)
