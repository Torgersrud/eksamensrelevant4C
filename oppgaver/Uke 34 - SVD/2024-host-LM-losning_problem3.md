### **Solution to Problem 3**

a) The SVD of $A$ can be written as $A=P\Sigma Q^{T}$ with $P\in\mathbb{R}^{3\times 2}$ orthogonal, $Q\in\mathbb{R}^{2\times 2}$ orthogonal, and $\Sigma\in\mathbb{R}^{2\times 2}$ diagonal with non-negative diagonal entries. Thus

$$A^{T}A=Q\Sigma P^{T}P\Sigma Q^{T}=Q\Sigma^{2}Q^{T}$$

and thus the columns of $Q$ form an orthogonal eigenbasis of $Q$ and the diagonal entries of $\Sigma^{2}$ are the eigenvalues of $A^{T}A$. We now compute

$$A^{T}A=\begin{pmatrix}2&5&4\\ 6&3&0\end{pmatrix}\begin{pmatrix}2&6\\ 5&3\\ 4&0\end{pmatrix}=\begin{pmatrix}45&27\\ 27&45\end{pmatrix}.$$

We see that $q_1=(1,1)^{T}$ is an eigenvector of $A^{T}A$ for the eigenvalue $72=(6\sqrt{2})^{2}$. Since the eigenvectors of $A^{T}A$ are orthogonal, $q_2=(1,-1)^{T}$ is another eigenvector, namely for the eigenvalue $18=(3\sqrt{2})^{2}$. This implies that

$$\Sigma=\begin{pmatrix}6\sqrt{2}&0\\ 0&3\sqrt{2}\end{pmatrix}\qquad\text{and}\qquad Q=\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\ 1&-1\end{pmatrix}.$$

Now we can write

$$P=AQ^{-T}\Sigma^{-1}=AQ\Sigma^{-1}=\begin{pmatrix}2&6\\ 5&3\\ 4&0\end{pmatrix}\begin{pmatrix}1&1\\ 1&-1\end{pmatrix}\begin{pmatrix}1/12&0\\ 0&1/6\end{pmatrix}=\begin{pmatrix}8&-4\\ 8&2\\ 4&4\end{pmatrix}\begin{pmatrix}1/12&0\\ 0&1/6\end{pmatrix}=\frac{1}{3}\begin{pmatrix}2&-2\\ 2&1\\ 1&2\end{pmatrix}.$$

The SVD of $A$ is therefore

$$A=P\Sigma Q^{T}=\frac{1}{3}\begin{pmatrix}2&-2\\ 2&1\\ 1&2\end{pmatrix}\begin{pmatrix}6\sqrt{2}&0\\ 0&3\sqrt{2}\end{pmatrix}\frac{1}{\sqrt{2}}\begin{pmatrix}1&1\\ 1&-1\end{pmatrix}.$$

b) Here we recall that we can compute $x$ as

$$x=A^{\dagger}b,$$

where $A^{\dagger}$ is the pseudo-inverse of $A$. In this case,

$$A^{\dagger}=Q\Sigma^{-1}P^{T}=\frac{1}{3}\begin{pmatrix}1&1\\ 1&-1\end{pmatrix}\begin{pmatrix}1/12&0\\ 0&1/6\end{pmatrix}\begin{pmatrix}2&2&1\\ -2&1&2\end{pmatrix}=\frac{1}{36}\begin{pmatrix}-2&4&5\\ 6&0&-3\end{pmatrix}$$

and thus

$$x=A^{\dagger}b=\frac{1}{36}\begin{pmatrix}-2&4&5\\ 6&0&-3\end{pmatrix}\begin{pmatrix}1\\ 1\\ 2\end{pmatrix}=\frac{1}{3}\begin{pmatrix}1\\ 0\end{pmatrix}.$$

*If you were unable to compute the SVD in part a) and have relied on the given (wrong) decomposition, you should instead have ended up with the results*

$$B^{\dagger}=\frac{1}{30}\begin{pmatrix}14&-10&19\\ 2&20&-8\end{pmatrix}\qquad\text{and}\qquad x=B^{\dagger}b=\frac{1}{5}\begin{pmatrix}7\\ 1\end{pmatrix}.$$

*Kjeldevarsel: i fasiten er setninga om eigenbasisen trykt som «the columns of $Q$ form an orthogonal eigenbasis of $Q$», men kolonnene er eigenbasis for $A^{T}A$ — rekningsgangen går ut frå dette og er elles korrekt (alle matrisene er kontrollreikna: $P\Sigma Q^{T}=A$, $A^{\dagger}b=\frac13(1,0)^{T}$).*

Kildesett: course=TMA4145 term=host year=2024 problem=3 points=10 file=lineaere_metoder_h24.pdf
