### **Solution to Problem 3**

a) The SVD of $A$ can be written as $A=P\Sigma Q^{T}$ with $P\in\mathbb{R}^{3\times 2}$ orthogonal, $Q\in\mathbb{R}^{2\times 2}$ orthogonal, and $\Sigma\in\mathbb{R}^{2\times 2}$ diagonal with non-negative diagonal entries. Thus

$$A^{T}A=Q\Sigma P^{T}P\Sigma Q^{T}=Q\Sigma^{2}Q^{T}$$

and thus the columns of $Q$ form an orthogonal eigenbasis of $Q$ and the diagonal entries of $\Sigma^{2}$ are the eigenvalues of $A^{T}A$. We now compute

$$A^{T}A=\begin{pmatrix}4&3&0\\ 3&-4&12\end{pmatrix}\begin{pmatrix}4&3\\ 3&-4\\ 0&12\end{pmatrix}=\begin{pmatrix}25&0\\ 0&169\end{pmatrix}.$$

We see that $q_1=(1,0)^{T}$ is an eigenvector of $A^{T}A$ for the eigenvalue $25=5^{2}$ and that $q_2=(0,1)^{T}$ is an eigenvector of $A^{T}A$ for the eigenvalue $169=13^{2}$. This implies that

$$\Sigma=\begin{pmatrix}5&0\\ 0&13\end{pmatrix}\qquad\text{and}\qquad Q=\begin{pmatrix}1&0\\ 0&1\end{pmatrix}.$$

Now we can write

$$P=AQ^{-T}\Sigma^{-1}=AQ\Sigma^{-1}=\begin{pmatrix}4&3\\ 3&-4\\ 0&12\end{pmatrix}\begin{pmatrix}1&0\\ 0&1\end{pmatrix}\begin{pmatrix}1/5&0\\ 0&1/13\end{pmatrix}=\begin{pmatrix}4/5&3/13\\ 3/5&-4/13\\ 0&12/13\end{pmatrix}.$$

The SVD of $A$ is therefore

$$A=P\Sigma Q^{T}=\begin{pmatrix}4/5&3/13\\ 3/5&-4/13\\ 0&12/13\end{pmatrix}\begin{pmatrix}5&0\\ 0&13\end{pmatrix}\begin{pmatrix}1&0\\ 0&1\end{pmatrix}.$$

(To be more precise, the diagonal entries should be ordered from largest to smallest value.)

b) Here we recall that we can compute $x$ as

$$x=A^{\dagger}b,$$

where $A^{\dagger}$ is the pseudo-inverse of $A$. In this case,

$$A^{\dagger}=Q\Sigma^{-1}P^{T}=\begin{pmatrix}1&0\\ 0&1\end{pmatrix}\cdot\begin{pmatrix}1/5&0\\ 0&1/13\end{pmatrix}\begin{pmatrix}4/5&3/5&0\\ 3/13&-4/13&12/13\end{pmatrix}=\begin{pmatrix}4/25&3/25&0\\ 3/169&-4/169&12/169\end{pmatrix}$$

and thus

$$x=A^{\dagger}b=\begin{pmatrix}4/25&3/25&0\\ 3/169&-4/169&12/169\end{pmatrix}\begin{pmatrix}12\\ -6\\ 5\end{pmatrix}=\begin{pmatrix}6/5\\ 120/169\end{pmatrix}.$$

*If you were unable to compute the SVD in part a) and have relied on the given (wrong) decomposition, you should instead have ended up with the results*

$$B^{\dagger}=\frac{1}{30}\begin{pmatrix}-10&19&14\\ -20&8&2\end{pmatrix}\qquad\text{and}\qquad x=B^{\dagger}b=-\frac{1}{15}\begin{pmatrix}82\\ 149\end{pmatrix}.$$

*Kjeldevarsel: i fasiten er setninga om eigenbasisen trykt som «the columns of $Q$ form an orthogonal eigenbasis of $Q$», men kolonnene er eigenbasis for $A^{T}A$; i reserve-svaret er $(2,3)$-leddet i $B^{\dagger}$ trykt som $2$, men skal vere $-2$ — det er berre $-\frac{1}{15}(82,149)^{T}$ som følgjer av $B=U\Sigma V^{T}$, og dette resultatet er konsistent med $-2$; elles er alle matrisene kontrollreikna ($P\Sigma Q^{T}=A$, $A^{\dagger}b=(6/5,\,120/169)^{T}$, $B^{\dagger}$ med $-2$ gir $x=B^{\dagger}b=-\frac{1}{15}(82,149)^{T}$).*

Kildesett: course=TMA4145 term=kont year=2024 problem=3 points=10 file=lineaere_metoder_h24_kont.pdf
