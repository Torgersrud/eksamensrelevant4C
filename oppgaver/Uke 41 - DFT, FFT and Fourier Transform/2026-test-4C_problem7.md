### **Problem 7** (Discrete Fourier Transform, 10 points)

Let a signal

$$\hat{\mathbf{f}}=(\hat{f}_0,\hat{f}_1,\hat{f}_2,\hat{f}_3,\hat{f}_4,\hat{f}_5)=(2,1,0,0,0,1)\in\mathbb{C}^{6}$$

of length $N=6$ be given. It is the result of the Fourier transform $\hat{\mathbf{f}}=\mathcal{F}_6\mathbf{f}$ of some unknown real-valued signal $\mathbf{f}=(f_0,\ldots,f_5)\in\mathbb{R}^{6}$ that was sampled from a $2\pi$-periodic function $f$, i.e. $f_j=f(\frac{2\pi}{6}j),j=0,\ldots,5$.

A function $g$ is called *bandlimited* if there exists some $B\in\mathbb{N}$ such that the Fourier coefficients $c_k(g)$, $k\in\mathbb{Z}$, fulfil

$$c_k(g)=0\quad\text{if}\quad|k|>B.$$

a) Let the sampled function $f$ be bandlimited with $B=4$. Is it possible to reconstruct the $c_k(f)$, $k\in\mathbb{Z}$, from the $\hat{f}_j$, $j=0,\ldots,5$? If so, state the values of the Fourier coefficients.

b) Let the sampled function $f$ be bandlimited with $B=2$. Is it possible to reconstruct the $c_k(f)$, $k\in\mathbb{Z}$, from the $\hat{f}_j$, $j=0,\ldots,5$? If so, state the values of the Fourier coefficients.

c) For the cases from Item a) and Item b) where a reconstruction is possible, compute the resulting function $f$.

Kildesett: course=TMA4432 term=test year=2026 problem=7 points=10 file=test-exam-math4c_web.pdf
