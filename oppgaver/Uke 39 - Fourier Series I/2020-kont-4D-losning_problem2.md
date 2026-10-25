### **Solution to Problem 2**

Notice that $f$ is an even function. Therefore the sine coefficients $b_n$ are all zero. And from Chapter 11.2 of Kreyszig 10th ed, the cosine coefficients for $n>0$ are

$$a_n=\frac{2}{\pi}\int_{0}^{\pi}f(x)\cos(nx)\,\mathrm{d}x$$

$$=\frac{2}{\pi}\int_{\pi/2}^{\pi}(x-\pi/2)\cos(nx)\,\mathrm{d}x$$

$$=\frac{2}{n\pi}(x-\pi/2)\sin(nx)\Big|_{\pi/2}^{\pi}-\frac{2}{n\pi}\int_{\pi/2}^{\pi}\sin(nx)\,\mathrm{d}x$$

$$=0+\frac{2}{n^2\pi}\cos(nx)\Big|_{\pi/2}^{\pi}$$

$$=\frac{2}{n^2\pi}\Big(\cos(n\pi)-\cos(n\pi/2)\Big),$$

which can be expressed as

$$=\frac{2}{n^2\pi}\cdot\begin{cases}1-1&n/4\in\mathbb{Z}\\ 1-(-1)&(n-2)/4\in\mathbb{Z}\\ -1-0&(n-1)/2\in\mathbb{Z}\end{cases}$$

$$=\frac{2}{n^2\pi}\cdot\begin{cases}0&n/4\in\mathbb{Z}\\ 2&(n-2)/4\in\mathbb{Z}\\ -1&(n-1)/2\in\mathbb{Z}\end{cases}.$$

and the 0th coefficient is the average over the period of length $2\pi$, which is $(\pi/2)^2/(2\pi)=a_0$, by the formula for the area of a triangle.

Therefore the complex coefficients are $c_0=a_0$, and

$$c_n=(a_{|n|}-\operatorname{sgn}(n)ib_{|n|})/2=a_{|n|}/2=\frac{1}{n^2\pi}\cdot\begin{cases}0&n/4\in\mathbb{Z}\\ 2&(n-2)/4\in\mathbb{Z}\\ -1&(n-1)/2\in\mathbb{Z}\end{cases},\quad n\neq 0.$$

Kildesett: course=TMA4135 term=kont year=2020 problem=2 points=10 file=tma4130_kont.pdf
