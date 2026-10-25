### **Solution to Problem 2** **Numerical integration [10 pts]**

$$\begin{aligned}a_0&=\frac{1}{2\pi}\int_{-\pi}^{\pi}2^{\sin x}\,\mathrm{d}x\\
&\approx\frac{1}{2\pi}\left\{\frac{\pi}{6}\left[2^{\sin(-\pi)}+4\times 2^{\sin(-\pi/2)}+2^{\sin 0}\right]+\frac{\pi}{6}\left[2^{\sin 0}+4\times 2^{\sin(\pi/2)}+2^{\sin\pi}\right]\right\}\\
&=\frac{1}{12}\left\{\left[2^0+4\times 2^{-1}+2^0\right]+\left[2^0+4\times 2^{1}+2^0\right]\right\}\\
&=7/6=1.1666...\end{aligned}$$

and, similarly,

$$\begin{aligned}b_1&=\frac{1}{\pi}\int_{-\pi}^{\pi}2^{\sin x}\sin x\,\mathrm{d}x\\
&\approx\frac{1}{6}\left[2^0\sin(-\pi)+4\times 2^{-1}\sin(-\pi/2)+2\times 2^0\sin 0+4\times 2^1\sin(\pi/2)+2^0\sin\pi\right]\\
&=\frac{1}{6}[0-2+2\times 0+8+0]\\
&=1\end{aligned}$$

**Grading manual** (5p) for $a_0$ and (5p) for $b_1$. For each coefficient, give

- 2p for having written (stated) the integral correctly.
- 2p for stating the correct formulas for each subinterval.
- 1p for applying the formulas correctly.

Kildesett: course=TMA4135 term=host year=2023 problem=2 points=10 file=tma4130_2023h_exam.pdf
