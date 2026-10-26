### **Solution to Problem 3**

a) The SVD of $A$ can be written as $A=P\Sigma Q^{T}$ with $P\in\mathbb{R}^{2\times 2}$ orthogonal, $Q\in\mathbb{R}^{4\times 2}$ orthogonal, and $\Sigma\in\mathbb{R}^{2\times 2}$ diagonal with non-negative diagonal entries. Thus

$$AA^{T}=P\Sigma Q^{T}Q\Sigma P^{T}=P\Sigma^{2}P^{T}$$

and thus the columns of $P$ form an orthogonal eigenbasis of $P$ and the diagonal entries of $\Sigma^{2}$ are the eigenvalues of $AA^{T}$.

We now compute

$$AA^{T}=\begin{pmatrix}3&0&6&-6\\ 0&-2&4&4\end{pmatrix}\begin{pmatrix}3&0\\ 0&-2\\ 6&4\\ -6&4\end{pmatrix}=\begin{pmatrix}81&0\\ 0&36\end{pmatrix}.$$

This implies that

$$\Sigma=\begin{pmatrix}9&0\\ 0&6\end{pmatrix}\qquad\text{and}\qquad P=\begin{pmatrix}1&0\\ 0&1\end{pmatrix}.$$

Now we can write

$$Q^{T}=\Sigma^{-1}P^{-1}A=\begin{pmatrix}1/9&0\\ 0&1/6\end{pmatrix}\begin{pmatrix}3&0&6&-6\\ 0&-2&4&4\end{pmatrix}=\begin{pmatrix}1/3&0&2/3&-2/3\\ 0&-1/3&2/3&2/3\end{pmatrix}.$$

The SVD of $A$ is therefore

$$A=P\Sigma Q^{T}=\begin{pmatrix}1&0\\ 0&1\end{pmatrix}\begin{pmatrix}9&0\\ 0&6\end{pmatrix}\begin{pmatrix}1/3&0&2/3&-2/3\\ 0&-1/3&2/3&2/3\end{pmatrix}.$$

b) Here we recall that we can compute $x$ as

$$x=A^{\dagger}b,$$

where $A^{\dagger}$ is the pseudo-inverse of $A$. In this case,

$$A^{\dagger}=Q\Sigma^{-1}P^{T}=\begin{pmatrix}1/3&0\\ 0&-1/3\\ 2/3&2/3\\ -2/3&2/3\end{pmatrix}\begin{pmatrix}1/9&0\\ 0&1/6\end{pmatrix}=\begin{pmatrix}1/27&0\\ 0&-1/18\\ 2/27&1/9\\ -2/27&1/9\end{pmatrix}$$

and thus

$$x=A^{\dagger}b=\begin{pmatrix}1/27&0\\ 0&-1/18\\ 2/27&1/9\\ -2/27&1/9\end{pmatrix}\begin{pmatrix}9\\ 6\end{pmatrix}=\begin{pmatrix}1/3\\ -1/3\\ 4/3\\ 0\end{pmatrix}.$$

*Kjeldevarsel: i fasiten er setninga om eigenbasisen trykt som «the columns of $P$ form an orthogonal eigenbasis of $P$», men kolonnene er eigenbasis for $AA^{T}$ — rekningsgangen går ut frå dette og er elles korrekt.*

Kildesett: course=TMA4145 term=host year=2023 problem=3 points=10 file=lineaere_metoder_h23.pdf
