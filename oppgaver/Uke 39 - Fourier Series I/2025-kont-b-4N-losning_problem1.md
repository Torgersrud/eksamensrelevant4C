### **Solution to Problem 1** **Fourier Series (10 points)**

a) Step 1: Check parity on the base interval $(-\pi,\pi)$

- For $t\in(0,\pi)$:
$$f(-t)=f(\text{value in }(-\pi,0))=-1=-f(t).$$

- For $t\in(-\pi,0)$:
$$f(-t)=f(\text{value in }(0,\pi))=1=-f(t).$$

- At $t=0$, $f(0)=0$ and $-f(0)=0$, so the parity relation holds.

Conclusion: $f$ is odd on $[-\pi,\pi]$.

Step 2: Extend the parity check to all $t\in\mathbb{R}$

- $f$ is periodic with period $2\pi$. - For a periodic function, if it is odd on one full period, it remains odd for all $t\in\mathbb{R}$.

Conclusion: $f$ is odd for all real numbers.

Step 3: Consequence for the Fourier series

- Since $f$ is odd, all cosine coefficients vanish:
$$a_0=0,\qquad a_n=0\ \text{for all}\ n\geq1.$$

- Only sine coefficients $b_n$ may be nonzero. - Therefore, the Fourier series of $f$ contains only sine terms.

b) For a $2\pi$-periodic function:
$$b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\sin(nt)\,dt$$

Since $f(t)$ is odd, we can integrate from 0 to $\pi$ and double the integral:
$$b_n=\frac{2}{\pi}\int_{0}^{\pi}f(t)\sin(nt)\,dt$$

On $0<t<\pi$, $f(t)=1$:
$$b_n=\frac{2}{\pi}\int_{0}^{\pi}\sin(nt)\,dt=\frac{2}{\pi}\left[-\frac{\cos(nt)}{n}\right]_{0}^{\pi}=\frac{2}{\pi}\left(-\frac{(-1)^n-1}{n}\right)=\frac{2}{\pi}\cdot\frac{1-(-1)^n}{n}$$

- For even n: $b_n=0$
- For odd n: $b_n=\frac{4}{n\pi}$.

c) The Fourier series is:
$$f(t)=\sum_{n=1,3,5,\ldots}^{\infty}\frac{4}{n\pi}\sin(nt)$$

First three nonzero terms ($n=1,3,5$):
$$f(t)\approx\frac{4}{\pi}\sin(t)+\frac{4}{3\pi}\sin(3t)+\frac{4}{5\pi}\sin(5t)$$

Grading manual: a) 3 points (1 points for f odd in $(−\pi,\pi)$, 1 points for the rest of R, 1 point for the consequence for the Fourier coefficients) b) 5 points c) 2 points

Kildesett: course=TMA4130 term=kont year=2025 problem=1 points=10 file=exam_math_4n_4d_tma4130_35-15.pdf
