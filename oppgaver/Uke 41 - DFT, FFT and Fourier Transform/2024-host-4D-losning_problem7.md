### **Solution to Problem 7** **Fourier Transform [10 pts]**

a) We compute

$$(f*g)(t)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)\cos(a(t-x))dx\tag{1}$$

$$=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)\Big(\cos(at)\cos(ax)+\sin(at)\sin(ax)\Big)dx.\tag{2}$$

b) Since the function $f$ is even ($f(-t)=f(t)$, for all $t$), we have that the product $f(t)\sin(at)$ is an odd function, and therefore the integral $\int_{-\infty}^{\infty}f(x)\sin(ax)dx=0$.

c) We continue the computation of $(f*g)(t)$:

$$(f*g)(t)\stackrel{c1)}{=}\cos(at)\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)\cos(ax)dx\tag{3}$$

$$\stackrel{c2)}{=}\cos(at)\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)(\cos(ax)-i\sin(ax))dx\tag{4}$$

$$\stackrel{c3)}{=}\cos(at)\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)\exp(-iax)dx\tag{5}$$

$$\stackrel{c4)}{=}\cos(at)\hat{f}(a).\tag{6}$$

**Grading manual** (10p)

a) (1p)

b) (2p)

c) (7p):

c1) (1p), c2) (3p), c3) (2p), c4) (1p)

Kildesett: course=TMA4135 term=host year=2024 problem=7 points=10 file=exam_math_4n_4d_tma4130_35-8.pdf
