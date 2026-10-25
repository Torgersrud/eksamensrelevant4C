### **Problem 5** **Discrete Fourier Transform (10 points)**

Let a signal
$$\hat{\mathbf{f}}=(\hat f_0,\hat f_1,\hat f_2,\hat f_3,\hat f_4,\hat f_5)=(2,1,0,0,0,1)\in\mathbb{C}^6$$
of length $N=6$ be given. It is the result of the Fourier transform $\hat{\mathbf{f}}=F_6\mathbf{f}$ of some unknown real-valued signal $\mathbf{f}=(f_0,\dots,f_5)\in\mathbb{R}^6$, that was sampled from a $2\pi$-periodic function $f$, i.e. $f_j=f\left(\frac{2\pi}{6}j\right)$, $j=0,\dots,5$.

A function $g$ is called *bandlimited* if there exists some $B\in\mathbb{N}$ such that the Fourier coefficients $c_k(g)$, $k\in\mathbb{Z}$, fulfil

$$c_k(g)=0\quad\text{ if }\quad|k|>B.$$

a) Let the sampled function $f$ be bandlimited with $B=4$. Is it possible to reconstruct the $c_k(f)$, $k\in\mathbb{Z}$, from the $\hat f_j$, $j=0,\dots,5$?
If so, state the values of the Fourier coefficients.

b) Let the sampled function $f$ be bandlimited with $B=2$. Is it possible to reconstruct the $c_k(f)$, $k\in\mathbb{Z}$, from the $\hat f_j$, $j=0,\dots,5$?
If so, state the values of the Fourier coefficients.

c) For the cases from Item a) and Item b) where a reconstruction is possible, compute the resulting function $f$.

Kildesett: course=TMA4125 term=var year=2025 problem=5 points=10 file=math4n-2025v-en-lf.pdf
