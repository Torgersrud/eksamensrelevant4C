### **Solution to Problem 5**

The Fourier coefficient $a_0$ computes as

$$a_0=\frac{1}{6}\int_{-3}^{3}x+3\,dx=3.$$

If $n\ge 1$, we obtain

$$a_n=\frac{1}{3}\int_{-3}^{3}(x+3)\cos\frac{n\pi x}{3}\,dx.$$

Now note that the function $x$ is odd, while $\cos$ is even, which implies that $x\cos\frac{n\pi x}{3}$ is odd, and thus its integral from $-3$ to $3$ equal to $0$. Thus

$$a_n=\frac{1}{3}\int_{-3}^{3}3\cos\frac{n\pi x}{3}\,dx=\left.\frac{3}{n\pi}\sin\frac{n\pi x}{3}\right|_{-3}^{3}=0.$$

For the computation of the coefficients $b_n$ we obtain

$$b_n=\frac{1}{3}\int_{-3}^{3}(x+3)\sin\frac{n\pi x}{3}\,dx,$$

which reduces, because $\sin$ is odd, to

$$b_n=\frac{1}{3}\int_{-3}^{3}x\sin\frac{n\pi x}{3}\,dx,$$

Integration by parts yields

$$\begin{array}{rcl}
\displaystyle b_n&=&\displaystyle-\frac{1}{3}x\frac{3}{n\pi}\cos\frac{n\pi x}{3}\bigg|_{-3}^{3}-\frac{1}{3}\int_{-3}^{3}\left(-\frac{3}{n\pi}\cos\frac{n\pi x}{3}\right)dx\\[10pt]
&=&\displaystyle-\frac{1}{n\pi}\left(3(-1)^n-(-3)(-1)^n\right)+\left.\frac{1}{n\pi}\frac{3}{n\pi}\sin\frac{n\pi x}{3}\right|_{-3}^{3}\\[10pt]
&=&\displaystyle\frac{6(-1)^{n+1}}{n\pi}\,.
\end{array}$$

Thus we obtain the Fourier series expansion

$$f(x)=3+\sum_{n=1}^{\infty}\frac{6(-1)^{n+1}}{n\pi}\sin\frac{n\pi x}{3}\,.$$

Kildesett: course=TMA4125 term=kont year=2016 problem=5 file=english.pdf
