### **Solution to Problem 3**

**a)** Compute the singular value decomposition of $A$.

**Solution:**

1. $A^{*}A=\begin{pmatrix}9&8\\ 8&9\end{pmatrix}$ has as characteristic polynomial $x^{2}-18x+17=(x-17)(x-1)$. Hence the eigenvalues of $A^{*}A$ are $\lambda_1=17$ and $\lambda_2=1$. The corresponding normalized eigenvectors are $v_1=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ 1\end{pmatrix}$ and $v_2=\frac{1}{\sqrt{2}}\begin{pmatrix}1\\ -1\end{pmatrix}$. Consequently, we have

$$\begin{pmatrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\ \frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}\end{pmatrix}.$$

2. The singular values of $A$ are $\sigma_1=\sqrt{17}$ and $\sigma_2=1$. Thus

$$\Sigma=\begin{pmatrix}\sqrt{17}&0\\ 0&1\\ 0&0\end{pmatrix}.$$

3. The first two columns of $U$ are given by

$$u_1=\frac{1}{\sqrt{17}}\frac{1}{\sqrt{2}}Av_1=\frac{1}{\sqrt{34}}\begin{pmatrix}1&2\\ 2&2\\ 2&1\end{pmatrix}\begin{pmatrix}1\\ 1\end{pmatrix}=\frac{1}{\sqrt{34}}\begin{pmatrix}3\\ 4\\ 3\end{pmatrix}$$

and by

$$u_2=\frac{1}{1}Av_2=\frac{1}{\sqrt{2}}\begin{pmatrix}1&2\\ 2&2\\ 2&1\end{pmatrix}\begin{pmatrix}1\\ -1\end{pmatrix}=\frac{1}{\sqrt{2}}\begin{pmatrix}-1\\ 0\\ 1\end{pmatrix}.$$

Consequently, $U$ has the form

$$\begin{pmatrix}\frac{3}{\sqrt{34}}&\frac{-1}{\sqrt{2}}&x_1\\[3pt] \frac{4}{\sqrt{34}}&0&x_2\\[3pt] \frac{3}{\sqrt{34}}&\frac{1}{\sqrt{2}}&x_3\end{pmatrix}$$

The last column is determined by the assumption that it has to be orthogonal to the first two columns. The choice

$$u_3=\frac{1}{\sqrt{17}}\begin{pmatrix}2\\ -3\\ 2\end{pmatrix}$$

satisfies these conditions, but there are many other ways to complete the first two columns to become an orthonormal basis for $\mathbb{C}^{3}$,

$$\begin{pmatrix}\frac{3}{\sqrt{34}}&\frac{-1}{\sqrt{2}}&\frac{2}{\sqrt{17}}\\[3pt] \frac{4}{\sqrt{34}}&0&\frac{-3}{\sqrt{17}}\\[3pt] \frac{3}{\sqrt{34}}&\frac{1}{\sqrt{2}}&\frac{2}{\sqrt{17}}\end{pmatrix}.$$

4. The SVD of $A$ is

$$\begin{pmatrix}\frac{3}{\sqrt{34}}&\frac{-1}{\sqrt{2}}&\frac{2}{\sqrt{17}}\\[3pt] \frac{4}{\sqrt{34}}&0&\frac{-3}{\sqrt{17}}\\[3pt] \frac{3}{\sqrt{34}}&\frac{1}{\sqrt{2}}&\frac{2}{\sqrt{17}}\end{pmatrix}\begin{pmatrix}\sqrt{17}&0\\ 0&1\\ 0&0\end{pmatrix}\begin{pmatrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\ \frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}\end{pmatrix}.$$

**b)** Use the result of a) to find:
(1) Bases for the following vector spaces: $\ker(A),\ker(A^{*}),\operatorname{ran}(A),\operatorname{ran}(A^{*})$.

**Solution:**

$$\ker(A^{*})=\{u_3\},\ker(A)=\{0\},\operatorname{ran}(A^{*})=\{v_1,v_2\},\operatorname{ran}(A)=\{u_1,u_2\}.$$

(3) The pseudo-inverse of $A$.

**Solution:**

$$A^{\dagger}=\begin{pmatrix}\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\\ \frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}\end{pmatrix}\begin{pmatrix}\frac{1}{\sqrt{17}}&0&0\\ 0&1&0\end{pmatrix}\begin{pmatrix}\frac{3}{\sqrt{34}}&\frac{4}{\sqrt{34}}&\frac{3}{\sqrt{34}}\\[3pt] \frac{-1}{\sqrt{2}}&0&\frac{1}{\sqrt{2}}\\[3pt] \frac{2}{\sqrt{17}}&\frac{-3}{\sqrt{17}}&\frac{2}{\sqrt{17}}\end{pmatrix}.$$

*Kjeldevarsel: Løysingsarket `tma4145eksamen_2016_en_sol-final.pdf` utelèt punkt b)(2) om polardekomposisjon — berre (1) og (3) står att. Wiki-sida for eksamen markerer polardekomposisjonen som ikkje-pensum. Kontrollrekna produkt for (3): $A^{\dagger}=\frac{1}{17}\begin{pmatrix}-7&2&10\\ 10&2&-7\end{pmatrix}$, som stemmer med sympy sitt `pinv(A)`.*

Kildesett: course=TMA4145 term=host year=2016 problem=3 file=tma4145eksamen_2016_en.pdf
