### **Solution to Problem 9** **Numerical integration [10 pts]**

Since the integration interval is $[-1,1]$, we can use the data from the table as it is:

$$\begin{aligned}a_1&=\frac{1}{1}\int_{-1}^{1}[\sin(\cos\pi x)]\cos\pi x\,\mathrm{d}x\\
&\approx\frac{5}{9}\sin(\cos(-\pi\sqrt{0.6}))\cos(-\pi\sqrt{0.6})+\frac{8}{9}\sin(\cos 0)\cos 0+\frac{5}{9}\sin(\cos(\pi\sqrt{0.6}))\cos(\pi\sqrt{0.6})\\
&\approx 2\times\frac{5}{9}(-0.76)\sin(-0.76)+\frac{8}{9}\sin(1)\\
&\approx 0.8642\end{aligned}$$

**Alternative solution**

Since $f(x)$ is an even function, we could also write

$$a_1=2\int_{0}^{1}[\sin(\cos\pi x)]\cos\pi x\,\mathrm{d}x$$

In this case, we have to transform each $\xi_i$ into a corresponding $x_i$ using

$$x(\xi)=\frac{1-0}{2}\xi+\frac{1+0}{2}=\frac{1+\xi}{2}$$

This gives us $x_1\approx 0.1127$, $x_2=0.5$, $x_3\approx 0.8873$ and $\mathrm{d}\xi=2\mathrm{d}x$. Hence:

$$\begin{aligned}a_1&=2\int_{0}^{1}[\sin(\cos\pi x)]\cos\pi x\,\mathrm{d}x\\
&=\int_{-1}^{1}[\sin(\cos\pi x)]\cos\pi x\,\mathrm{d}\xi\\
&\approx\frac{5}{9}\sin(\cos(0.1127\pi))\cos(0.1127\pi)+\frac{8}{9}\sin\left(\cos\frac{\pi}{2}\right)\cos\frac{\pi}{2}+\frac{5}{9}\sin(\cos(0.8873\pi))\cos(0.8873\pi)\\
&\approx 0.8404\end{aligned}$$

**Grading manual** (10p)

Kildesett: course=TMA4135 term=kont year=2023 problem=9 points=10 file=tma4130_2023h_exam-19.pdf
