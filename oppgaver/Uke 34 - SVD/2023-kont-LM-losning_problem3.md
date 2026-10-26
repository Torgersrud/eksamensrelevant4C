### **Solution to Problem 3**

a) We compute

$$AA^{T}=\begin{pmatrix}20&8&-2\\ 10&19&14\end{pmatrix}\begin{pmatrix}20&10\\ 8&19\\ -2&14\end{pmatrix}=\begin{pmatrix}468&324\\ 324&657\end{pmatrix}.$$

The characteristic polynomial of this matrix is

$$p(\lambda)=(\lambda-468)(\lambda-657)-324^{2}=\lambda^{2}-1125\lambda+202500.$$

The corresponding eigenvalues are therefore

$$\frac{1125\pm\sqrt{1125^{2}-4*202500}}{2}=\frac{1125\pm 675}{2}=\begin{cases}900,\\ 225.\end{cases}$$

The singular values of $A$ are therefore $\sigma_1=30$ and $\sigma_2=15$.

We next find an orthogonal eigenbasis of $AA^{T}$. We start by computing an eigenvector of $AA^{T}$ for the eigenvalue $\lambda_1=900$. We have that

$$900\,\mathrm{Id}-A=\begin{pmatrix}432&-324\\ -324&243\end{pmatrix}=27\begin{pmatrix}16&-12\\ -12&9\end{pmatrix}$$

From this, we see that an eigenvector of $A$ is the vector $\begin{pmatrix}3\\ 4\end{pmatrix}$, which we can normalise to $u_1=\frac{1}{5}\begin{pmatrix}3\\ 4\end{pmatrix}$. We can complete this vector with $u_2=\frac{1}{5}\begin{pmatrix}4\\ -3\end{pmatrix}$ to an orthonormal eigenbasis of $AA^{T}$. Thus

$$U=\frac{1}{5}\begin{pmatrix}3&4\\ 4&-3\end{pmatrix}$$

and

$$\Sigma=\begin{pmatrix}30&0\\ 0&15\end{pmatrix}$$

are the first two ingredients of the singular value decomposition $A=U\Sigma V^{T}$ of $A$. We then can compute

$$V^{T}=\Sigma^{-1}U^{-1}A=\Sigma^{-1}U^{T}A=\frac{1}{30}\begin{pmatrix}1&0\\ 0&2\end{pmatrix}\frac{1}{5}\begin{pmatrix}3&4\\ 4&-3\end{pmatrix}\begin{pmatrix}20&8&-2\\ 10&19&14\end{pmatrix}$$

$$=\frac{1}{150}\begin{pmatrix}3&4\\ 8&-6\end{pmatrix}\begin{pmatrix}20&8&-2\\ 10&19&14\end{pmatrix}=\frac{1}{150}\begin{pmatrix}100&100&50\\ 100&-50&-100\end{pmatrix}=\frac{1}{3}\begin{pmatrix}2&2&1\\ 2&-1&-2\end{pmatrix}.$$

b) Here we recall that we can compute $x$ as

$$x=A^{\dagger}b,$$

where $A^{\dagger}$ is the pseudoinverse of $A$, which in this case is $A^{\dagger}=V\Sigma^{-1}U^{T}$. We compute

$$A^{\dagger}=V\Sigma^{-1}U^{T}=\frac{1}{3}\begin{pmatrix}2&2\\ 2&-1\\ 1&-2\end{pmatrix}\frac{1}{150}\begin{pmatrix}3&4\\ 8&-6\end{pmatrix}=\frac{1}{450}\begin{pmatrix}22&-4\\ -2&14\\ -13&16\end{pmatrix}.$$

Thus

$$x=A^{\dagger}b=\frac{1}{450}\begin{pmatrix}22&-4\\ -2&14\\ -13&16\end{pmatrix}\begin{pmatrix}12\\ -9\end{pmatrix}=\frac{1}{450}\begin{pmatrix}300\\ -150\\ -300\end{pmatrix}=\frac{1}{3}\begin{pmatrix}2\\ -1\\ -2\end{pmatrix}.$$

*If you were unable to compute the SVD in part a) and have relied on the given (wrong) decomposition, you should instead have ended up with the results*

$$A^{\dagger}=\frac{1}{70}\begin{pmatrix}36&2\\ -24&57\\ 26&-18\end{pmatrix}\qquad\text{and}\qquad x=A^{\dagger}b=\frac{1}{70}\begin{pmatrix}414\\ -801\\ 474\end{pmatrix}.$$

*Kjeldevarsel: i fasiten er utrekninga for eigenvektoren trykt som «$900\,\mathrm{Id}-A$» og eigenvektoren som «an eigenvector of $A$», men tala $432$, $-324$ og $243$ svarer til $900\,\mathrm{Id}-AA^{T}$ og vektoren er eigenvektor for $AA^{T}$ ($A$ er $2\times 3$); rekningsgangen elles er konsistent med $AA^{T}$ og alle matrisene er kontrollreikna ($U\Sigma V^{T}=A$, $A^{\dagger}b=\frac13(2,-1,-2)^{T}$ og $A\cdot\frac13(2,-1,-2)^{T}=b$).*

Kildesett: course=TMA4145 term=kont year=2023 problem=3 points=10 file=lineaere_metoder_h23_kont.pdf
