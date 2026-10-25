### **Solution to Problem 6** **Fourier series [10 pts]**

Since $x^3$ is an odd function, the function $f$ is even and can be expressed by cosine-terms only (i.e., $b_n=0$ for all $n$). To get rid of the absolute-value, we treat the problem as an even half-range expansion of $x^3$. The Fourier coefficients are now given by

$$a_0=\frac{1}{\pi}\int_0^{\pi}x^3dx=\frac{1}{\pi}\cdot\left[\frac{1}{4}x^4\right]_0^{\pi}=\frac{\pi^4}{4\pi}=\frac{\pi^3}{4}\,,$$

$$\begin{aligned}a_n&=\frac{2}{\pi}\int_0^{\pi}x^3\cdot\cos(nx)dx\\
&=\frac{2}{\pi}\left(\underbrace{\left[x^3\frac{1}{n}\sin(nx)\right]_0^{\pi}}_{=0}-\int_0^{\pi}3x^2\frac{1}{n}\sin(nx)dx\right)\\
&=-\frac{6}{\pi n}\int_0^{\pi}x^2\sin(nx)dx\\
&=-\frac{6}{\pi n}\left(\left[x^2\frac{1}{n}(-\cos(nx))\right]_0^{\pi}-\int_0^{\pi}2x\frac{1}{n}(-\cos(nx))dx\right)\\
&=\frac{6\pi}{n^2}\cos(n\pi)-\frac{12}{\pi n^2}\int_0^{\pi}x\cos(nx)dx\\
&=\frac{6\pi}{n^2}\cos(n\pi)-\frac{12}{\pi n^2}\left(\underbrace{\left[\frac{x}{n}\sin(nx)\right]_0^{\pi}}_{=0}-\int_0^{\pi}\frac{1}{n}\sin(nx)dx\right)\\
&=\frac{6\pi}{n^2}\cos(n\pi)+\frac{12}{\pi n^3}\left[\frac{1}{n}(-\cos(nx))\right]_0^{\pi}\\
&=\frac{6\pi}{n^2}\cos(n\pi)-\frac{12}{\pi n^4}(\cos(n\pi)-\cos(0))\\
&=\begin{cases}-\frac{6\pi}{n^2}-\frac{12}{\pi n^4}(-1-1)=-\frac{6\pi}{n^2}+\frac{24}{\pi n^4},&n\ \mathrm{odd}\\[6pt]\frac{6\pi}{n^2}+\frac{12}{\pi n^4}\cdot 0=\frac{6\pi}{n^2},&n\ \mathrm{even}\end{cases}\end{aligned}$$

So, the Fourier series is given by

$$\begin{aligned}f(x)&\sim\frac{\pi^3}{4}+\sum_{n=1}^{\infty}\left(-\frac{6\pi}{n^2}\cos(n\pi)-\frac{12}{\pi n^4}(\cos(n\pi)-\cos(0))\right)\\
&=\frac{\pi^3}{4}+\underbrace{\left(-6\pi+\frac{24}{\pi}\right)\cdot\cos(x)}_{n=1}+\underbrace{\left(\frac{3\pi}{2}\right)\cdot\cos(2x)}_{n=2}+\underbrace{\left(-\frac{6\pi}{9}+\frac{24}{\pi 3^4}\right)\cdot\cos(3x)}_{n=3}\\
&\hspace{27.5em}+\underbrace{\left(\frac{6\pi}{16}\right)\cdot\cos(4x)}_{n=4}+\ldots\end{aligned}$$

**Grading manual** (3p) for $a_0$, (5p) for $a_n$ and (2p) for the formulation of the Fourier series.

Kildesett: course=TMA4135 term=host year=2023 problem=6 points=10 file=tma4130_2023h_exam.pdf
