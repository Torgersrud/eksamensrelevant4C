### **Problem 10** (Tucker decomposition by hand: reconstruction, norms and one HOOI update, 8 points)

A calibration measurement is stored in the tensor $\mathbf{T}\in\mathbb{R}^{3\times 2\times 4}$ with frontal slices

$$T_{::1}=\begin{pmatrix}\tfrac45&\tfrac45\\[2pt] \tfrac25&\tfrac25\\[2pt] \tfrac45&\tfrac45\end{pmatrix},\qquad T_{::2}=\begin{pmatrix}\tfrac{16}{15}&\tfrac{16}{15}\\[2pt] \tfrac8{15}&\tfrac8{15}\\[2pt] \tfrac{16}{15}&\tfrac{16}{15}\end{pmatrix},\qquad T_{::3}=\begin{pmatrix}\tfrac25&\tfrac25\\[2pt] \tfrac15&\tfrac45\\[2pt] \tfrac25&-\tfrac45\end{pmatrix},\qquad T_{::4}=\begin{pmatrix}\tfrac8{15}&\tfrac8{15}\\[2pt] \tfrac4{15}&\tfrac{16}{15}\\[2pt] \tfrac8{15}&-\tfrac{16}{15}\end{pmatrix}.$$

The same data are claimed to live in the Tucker format $\mathbf{T}=\mathbf{G}\times_1 U\times_2 V\times_3 W$, i.e.

$$t_{ijk}=\sum_{p=1}^{2}\sum_{q=1}^{2}\sum_{r=1}^{2} g_{pqr}\,u_{ip}\,v_{jq}\,w_{kr},$$

with the $2\times2\times2$ core given by its frontal slices $G_{::1}=\begin{pmatrix}2&2\\ 0&0\end{pmatrix}$, $G_{::2}=\begin{pmatrix}1&0\\ 0&2\end{pmatrix}$ and the factor matrices

$$U=\frac13\begin{pmatrix}2&1\\ 1&2\\ 2&-2\end{pmatrix}\in\mathbb{R}^{3\times2},\qquad V=I_2,\qquad W=\begin{pmatrix}\tfrac35&0\\[2pt] \tfrac45&0\\[2pt] 0&\tfrac35\\[2pt] 0&\tfrac45\end{pmatrix}\in\mathbb{R}^{4\times2}.$$

a) Check that $U^{\top}U=I_2$ and $W^{\top}W=I_2$. Then reconstruct the slices from the Tucker form using $T_{::k}=\sum_{r} w_{kr}\,U\,G_{::r}\,V^{\top}$: compute $T_{::1}$ and $T_{::3}$ and compare with the measured slices above. (2 P.)

b) Compute the single entry $t_{3,2,4}$ directly from the triple sum and check it against slice $4$. Show that a mode-$n$ product with a matrix that has orthonormal columns leaves the Frobenius norm unchanged (hint: compare the mode-$n$ unfoldings), and conclude $\|\mathbf{T}\|_F^2=\|\mathbf{G}\|_F^2$; give the number. (2 P.)

c) A HOOI sweep updates one factor at a time by an SVD of a Gram matrix of the current fit. For the mode-$1$ update with $V,W$ fixed, the best $3\times2$ factor with orthonormal columns maximises $\operatorname{tr}\!\big(U^{\top}\mathbf{T}^{(1)}\mathbf{T}^{(1)\top}U\big)$ over such $U$. Here

$$\mathbf{T}^{(1)}\mathbf{T}^{(1)\top}=\frac19\begin{pmatrix}40&26&28\\ 26&25&2\\ 28&2&52\end{pmatrix}.$$

Verify that the three vectors $\tfrac13(2,1,2)^{\top}$, $\tfrac13(1,2,-2)^{\top}$, $\tfrac13(-2,2,1)^{\top}$ are eigenvectors with eigenvalues $9$, $4$, $0$. Which $U$ does the HOOI update return, and do you recognise it? What does the zero eigenvalue say about how well the format $\mathbf{G}\times_1 U\times_2 V\times_3 W$ with a $2$-dimensional mode-$1$ factor fits these data? Finally, explain why the Gram is cheap here: use $\mathbf{T}^{(1)}=U\,G^{(1)}(W\odot V)^{\top}$ and the Gram identity for $\odot$ to get $\mathbf{T}^{(1)}\mathbf{T}^{(1)\top}=U\,G^{(1)}G^{(1)\top}U^{\top}$ without ever forming $\mathbf{T}^{(1)}$. (3 P.)

d) Count the numbers the Tucker representation stores here (core plus three factors) and compare with storing all entries of $\mathbf{T}$. Does the format pay off at this size? Repeat the count for a $600\times400\times500$ tensor with core $(2,2,2)$ and the same mode sizes in the factors, and give the ratio. (1 P.)

*Kjeldevarsel: Syntetisk oppgåve — oppgåveforma er tilpassa frå øvingsoppgåver i Ballard & Kolda, «Tensor Decompositions for Data Science» (Cambridge University Press, final draft mars 2025), kap. 4 og 6; ingen tekst eller tal er henta frå utkastet, og Tucker-modellen, modus-produkta og HOOI-oppdateringa er standardstoff som òg står i den offentleg utgitte rapporten Kolda & Bader, «Tensor Decompositions and Applications», SAND2007-6702 (2007).*
