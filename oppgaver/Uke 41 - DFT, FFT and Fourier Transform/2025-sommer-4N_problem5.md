### **Problem 5** **Discrete Fourier Transform (10 points)**

For the function
$$f(x)=3+2\cos(2x)$$
We want to look at its discrete Fourier transform, that is, for some $N\in\mathbb{N}$ we consider the sampled values
$$\mathbf{f}=(f_0,\dots,f_{N-1})\in\mathbb{R}^N,\qquad\text{where } f_j=f\Bigl(\frac{2\pi}{N}j\Bigr),\quad j=0,\dots,N-1,$$
and the corresponding discrete Fourier transform $\hat{\mathbf{f}}=F_N\mathbf{f}\in\mathbb{C}^N$.

Remember, that in general a function $g$ is called *bandlimited* if there exists some $B\in\mathbb{N}$ such that the Fourier coefficients $c_k(g)$, $k\in\mathbb{Z}$, fulfil

$$c_k(g)=0\quad\text{ if }\quad|k|>B.$$

a) Read off the Fourier coefficients $c_k(f)$, $k\in\mathbb{Z}$, of the function $f$.

b) We choose $N=4$ sample values. Without computing the samples $f_0,\dots,f_3$, compute the discrete Fourier transform $\hat f_j$ for $j=0,\dots,3$.

c) We choose $N=6$ sample values. Without computing the samples $f_0,\dots,f_5$, compute the discrete Fourier transform $\hat f_j$ for $j=0,\dots,5$.

d) Using the Aliasing Lemma, for which of the above cases Item b) and Item c) can we uniquely reconstruct the Fourier coefficients $c_k(f)$, $k\in\mathbb{Z}$, and hence $f$?

e) What is the smallest $N$ where the reconstruction is possible?

Kildesett: course=TMA4125 term=sommer year=2025 problem=5 points=10 file=math4n-2025s-en-lf.pdf
