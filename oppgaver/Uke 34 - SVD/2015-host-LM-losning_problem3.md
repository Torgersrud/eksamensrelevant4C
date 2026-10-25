### **Solution to Problem 3**

**a)** Recall $A^{*}$ is defined to be the complex-transpose of a matrix $A$. Hence

$$A^{*}=\begin{pmatrix}1&1&-1\\ 1&-1&0\\ 1&0&1\end{pmatrix}\ \text{ and so we get that }\ A^{*}A=\begin{pmatrix}3&0&0\\ 0&2&1\\ 0&1&2\end{pmatrix}.$$

The characteristic polynomial for $A^{*}A$ is given by

$$\det\begin{pmatrix}3-\lambda&0&0\\ 0&2-\lambda&1\\ 0&1&2-\lambda\end{pmatrix}=(3-\lambda)\big[(2-\lambda)(2-\lambda)-1\big]=(3-\lambda)(\lambda-3)(\lambda-1)$$

Hence the eigenvalues are $\lambda_1=1$ with algo.-multiplicity 1 and $\lambda_2=3$ with algo.-multiplicity 2.

$(\cdot)$ Eigenvectors for $\lambda_1=1$ satisfy $\begin{pmatrix}2&0&0\\ 0&1&1\\ 0&1&1\end{pmatrix}\begin{pmatrix}x_1\\ x_2\\ x_3\end{pmatrix}=0$

$$\leadsto v_1=\begin{pmatrix}0\\ 1\\ -1\end{pmatrix}.$$

$(\cdot)$ Eigenvectors for $\lambda_2=3$: $\begin{pmatrix}0&0&0\\ 0&-1&1\\ 0&1&-1\end{pmatrix}\begin{pmatrix}x_1\\ x_2\\ x_3\end{pmatrix}=0$

$$\leadsto\begin{pmatrix}0\\ 1\\ 1\end{pmatrix}=v_2$$

Since the algo.-multiplicity is 2 we have to deal again with generalized eigenvectors, i.e. elements in the kernel of $(A^{*}A-3I)^{2}$.

$(A^{*}A-3I)^{2}=\begin{pmatrix}0&0&0\\ 0&2&-2\\ 0&-2&2\end{pmatrix}\leadsto v_3=\begin{pmatrix}1\\ 0\\ 0\end{pmatrix}\ \left(\text{or }\begin{pmatrix}1\\ 1\\ 1\end{pmatrix}\right)$

**b)** We have to find unitary matrices $U$ and $V$ s.t. $A=U\Sigma V^{*}$ where $\Sigma$ is a diagonal matrix containing the singular values of $A$, which are the square roots of the eigenvalues of $A^{*}A$. In our case, $\sigma_1=\sigma_2=\sqrt{3}$ and $\sigma_3=1\leadsto\Sigma=\begin{pmatrix}\sqrt{3}&0&0\\ 0&\sqrt{3}&0\\ 0&0&1\end{pmatrix}$.

$(\cdot)$ $V$ consists of the normalized eigenvectors of $A^{*}A$, which by Part a) are given by $v_1=\begin{pmatrix}1\\ 0\\ 0\end{pmatrix}$, $v_2=\dfrac{1}{\sqrt{2}}\begin{pmatrix}0\\ 1\\ 1\end{pmatrix}$, $v_3=\dfrac{1}{\sqrt{2}}\begin{pmatrix}0\\ -1\\ 1\end{pmatrix}$ $\leadsto V=\begin{pmatrix}1&0&0\\ 0&\frac{1}{\sqrt{2}}&-\frac{1}{\sqrt{2}}\\ 0&\frac{1}{\sqrt{2}}&\frac{1}{\sqrt{2}}\end{pmatrix}$.

$(\cdot)$ The columns of $U=(u_1|u_2|u_3)$ are given by $u_i=\dfrac{1}{\sigma_i}Av_i$, $i=1,2,3$.

$$\leadsto u_2=\frac{1}{\sqrt{6}}\begin{pmatrix}2\\ -1\\ 1\end{pmatrix},\ u_3=\frac{1}{\sqrt{2}}\begin{pmatrix}0\\ 1\\ 1\end{pmatrix},\ u_1=\frac{1}{\sqrt{3}}\begin{pmatrix}1\\ 1\\ -1\end{pmatrix}$$

$$\leadsto U=\begin{pmatrix}\frac{1}{\sqrt{3}}&\sqrt{\frac{2}{3}}&0\\[3pt] \frac{1}{\sqrt{3}}&-\frac{1}{\sqrt{6}}&\frac{1}{\sqrt{2}}\\[3pt] \frac{1}{\sqrt{3}}&\frac{1}{\sqrt{6}}&\frac{1}{\sqrt{2}}\end{pmatrix}.\quad\blacksquare$$

*Kjeldevarsel: Løysinga i `solutionstma4145-dec2015.pdf` (hand skriven, side 4–5 av 11) har pluss-teikn på plass (3,1) i den siste U-matrisa, men ei linje ovanfor står $u_1=\frac{1}{\sqrt{3}}(1,1,-1)^{T}$. Med pluss-teikn blir $U\Sigma V^{*}=\begin{pmatrix}1&1&1\\ 1&-1&0\\ 1&0&1\end{pmatrix}$, som ikkje er $A$; med minusteikn $\left(-\frac{1}{\sqrt{3}}\right)$ blir $U\Sigma V^{*}=A$ (kontrollrekna). Teksten over fylgjer handskrifta som det står.*

Kildesett: course=TMA4145 term=host year=2015 problem=3 file=tma4145-eksamen-english.pdf
