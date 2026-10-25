### **Solution to Problem 7** (Discrete Fourier Transform, 8 points)

a) By definition we have $\mathcal{F}_N=\left(\mathrm{e}^{-2\pi\mathrm{i}jk/N}\right)_{j,k=0}^{N-1}$. (1 P.)

In this problem this leads to the Fourier matrix (1 P.)

$$\mathcal{F}_4=\begin{pmatrix}1&1&1&1\\ 1&-\mathrm{i}&-1&\mathrm{i}\\ 1&-1&1&-1\\ 1&\mathrm{i}&-1&-\mathrm{i}\end{pmatrix}$$

Depending on which definition is used, a factor $\frac{1}{4}$ or $\frac{1}{\sqrt{4}}=\frac{1}{2}$ is also possible

b) We obtain (2 P.)

$$\hat{\mathbf{f}}=\mathcal{F}_4\mathbf{f}=\mathcal{F}_4\begin{pmatrix}\hat{f}_0\\ \hat{f}_1\\ \hat{f}_2\\ \hat{f}_3\end{pmatrix}=\begin{pmatrix}\frac{1}{2}+1+\frac{1}{2}+0\\ \frac{1}{2}-\mathrm{i}-\frac{1}{2}+0\mathrm{i}\\ \frac{1}{2}-1+\frac{1}{2}-0\\ \frac{1}{2}+\mathrm{i}-\frac{1}{2}-0\mathrm{i}\end{pmatrix}=\begin{pmatrix}2\\ -\mathrm{i}\\ 0\\ \mathrm{i}\end{pmatrix}$$

or the two scaled versions mentioned at the end of a).

c) If we obtain the Fourier transform $\hat{\mathbf{g}}=(0,c,0,c)$ then the inverse Fourier transform is $\mathbf{g}=\frac{1}{2}(c,0,-c,0)$. Which is a cosine. (2 P.)

*Alternatively* one can argue that with a Fourier shift these correspond to $c_0(g)=0=c_{-2}(g)=0$ and $c_{\pm 1}(g)=c$ and this corresponds to $a_1=2c_1=2c$ and all other coefficients $a_0a_n=0$ ($n\ne 1$) and $b_n=0$, $n=1,2,\ldots$. Hence $\mathbf{g}$ are the sampling values $g_j=g(t_j)$ at $t_j=\frac{\pi j}{2}$, $j=0,1,2,3$ of

$$g(x)=2c\cos(x).$$

d) No, since with the Fourier shift this corresponds to $c_{-4}=\hat{h}_4$, $c_{-3}=\hat{h}_5$, ..., so with $c_{-1}=\hat{h}_7=1$ but $c_1=\hat{h}_1=0$ the condition that $c_k=\overline{c_{-k}}$ does not hold. (2 P.)

Alternatively one can argue that the inverse Fourier transform consists of the seventh column of $\mathcal{F}_8^{-1}$ and that this column contains for example $\mathrm{i}$ which is then an entry of $\mathbf{h}$.


Kildesett: course=TMA4125 term=var year=2022 problem=7 points=8 file=TMA4125-Matematikk-4N-2022v_lf.pdf
