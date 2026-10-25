### **Solution to Problem 2** **Fourier series [10 pts]**

The resulting even extension is

$$f_1(x)=\begin{cases}2x&0\le x<2\\ -2x+8&2\le x<4,\end{cases}$$

$f_1(x)=f_1(x+4n)$ ($n\in\mathbb{Z}$), with period 4. We have

$$\begin{aligned}a_0&=\frac{1}{2L}\int_{-L}^{L}f_1(x)dx\\
&=\frac{1}{4}\int_{-2}^{2}f_1(x)dx\\
&=\frac{1}{2}\int_{0}^{2}f_1(x)dx\\
&=\frac{1}{2}\int_{0}^{2}2xdx\\
&=\left[\frac{x^2}{2}\right]_0^2\\
&=2.\end{aligned}$$

Moreover,

$$\begin{aligned}a_n&=\frac{1}{L}\int_{-L}^{L}\underbrace{f_1(x)}_{\text{even}}\underbrace{\cos\left(\frac{\pi nx}{L}\right)}_{\text{even}}dx\\
&=\frac{2}{L}\int_{0}^{L}f_1(x)\cos\left(\frac{\pi nx}{L}\right)dx\\
&=\int_{0}^{L}2x\cos\left(\frac{\pi nx}{L}\right)dx\\
&=\underbrace{\left[2x\frac{L}{\pi n}\sin\left(\frac{\pi nx}{L}\right)\right]_0^2}_{=0}-\int_{0}^{L}2\frac{L}{\pi n}\sin\left(\frac{\pi nx}{L}\right)dx\\
&=-\frac{2L}{\pi n}\cdot\frac{L}{\pi n}\left[-\cos\left(\frac{\pi nx}{L}\right)\right]_0^L\\
&=\frac{2L^2}{\pi^2n^2}\left(\cos\left(\frac{\pi 2n}{L}\right)-1\right)\\
&=\frac{2L^2}{\pi^2n^2}\left(\cos\left(\pi n\right)-1\right).\end{aligned}$$

Therefore, we have for

$$\begin{aligned}n=1:\quad&a_1=\frac{8}{\pi^2}\cdot(-2)=\frac{-16}{\pi^2}\\
n=2:\quad&a_2=0\\
n=3:\quad&a_3=\frac{8}{\pi^2\cdot 3^2}\cdot(-2)=\frac{-16}{9\pi^2}\\
n=4:\quad&a_4=0\\
n=5:\quad&a_5=\frac{8}{\pi^2\cdot 5^2}\cdot(-2)=\frac{-16}{25\pi^2}.\end{aligned}$$

The resulting Fourier series is

$$\begin{aligned}f_1(x)&=2+\sum_{n=1}^{\infty}\frac{2L^2}{\pi^2n^2}\left(\cos\left(\pi n\right)-1\right)\cos\left(\frac{n\pi x}{2}\right)\\
&\approx 2-\frac{16}{\pi^2}\cos\left(\frac{\pi x}{2}\right)-\frac{16}{9\pi^2}\cos\left(\frac{3\pi x}{2}\right)-\frac{16}{25\pi^2}\cos\left(\frac{5\pi x}{2}\right)-\ldots\end{aligned}$$

**Grading manual** (1p) for the proper even extension
(2p) for $a_0$
(3p) for $a_n$
(3p) for $a_1$, $a_3$, $a_5$
(1p) for the Fourier series.

Kildesett: course=TMA4135 term=host year=2024 problem=2 points=10 file=exam_math_4n_4d_tma4130_35-8.pdf
