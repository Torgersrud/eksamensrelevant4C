### **Solution to Problem 3** **Fourier series [10 pts]** (4D)

Since $f(x)$ is even, we know that $b_n=0$, and that

$$a_0=\frac{1}{L}\int_{0}^{L}f(x)\,\mathrm{d}x=\frac{1}{1}\int_{0}^{1}1+x\,\mathrm{d}x=\frac{3}{2}$$

and

$$\begin{aligned}a_n&=\frac{2}{L}\int_{0}^{L}f(x)\cos\frac{n\pi x}{L}\,\mathrm{d}x\\
&=2\int_{0}^{1}(1+x)\cos n\pi x\,\mathrm{d}x\\
&=2\int_{0}^{1}x\cos n\pi x\,\mathrm{d}x\\
&=2\left\{x\left.\frac{\sin n\pi x}{n\pi}\right|_0^1-\int_{0}^{1}1\cdot\frac{\sin n\pi x}{n\pi}\,\mathrm{d}x\right\}\\
&=\left.\frac{2}{(n\pi)^2}\cos n\pi x\right|_0^1\\
&=2\frac{(-1)^n-1}{(n\pi)^2}\end{aligned}$$

We therefore have $a_0=1.5$, $a_1=-4/\pi^2$, $a_2=0$, $a_3=-4/(3\pi)^2$... hence:

$$f(x)=\frac{3}{2}-\frac{2}{\pi^2}\sum_{n=1}^{\infty}\frac{1+(-1)^{n+1}}{n^2}\cos n\pi x=\frac{3}{2}-\frac{4}{\pi^2}\cos n\pi x-\frac{4}{9\pi^2}\cos 3\pi x+....$$

**Grading manual** (10p)

Kildesett: course=TMA4135 term=kont year=2023 problem=3 points=10 file=tma4130_2023h_exam-19.pdf
