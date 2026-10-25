### **Solution to Problem 2** **Fourier series [10 pts]**

A function $f$ is odd if $f(x)=-f(-x)$. Let $x\in[0,1)$, then, according to its definition, $f(x)=-x+1$. Because $f$ is odd, $-f(x)=f(-x)$ and $-f(x)=x-1=f(-x)$. Let $y:=-x$. Since $-x=y\in[-1,0)$, we get $f(y)=-y-1$.

We therefore get $f(-x)=-f(x)$. The resulting odd extension is
$$f(x)=\begin{cases}-x+1,&0\le x<1,\\ -x-1,&-1\le x<0,\end{cases}$$
$f(x)=f(x+2n)$ $(n\in\mathbb{Z})$, with period 2.

As the extension of $f$ is odd, we have
$$a_n=0,\qquad n=0,1,2,\ldots.$$

Moreover,
$$\begin{aligned}b_n&=\frac{1}{L}\int_{-L}^{L}\underbrace{f(x)}_{\text{odd}}\underbrace{\sin\left(\frac{\pi nx}{L}\right)}_{\text{odd}}dx\\&=\frac{2}{L}\int_{0}^{L}f(x)\sin\left(\frac{\pi nx}{L}\right)dx\\&=2\int_{0}^{1}(-x+1)\sin\left(\pi nx\right)dx\\&=-2\int_{0}^{1}x\sin\left(\pi nx\right)dx+2\int_{0}^{1}\sin\left(\pi nx\right)dx\\&=\underbrace{\left[2x\frac{1}{\pi n}\cos\left(\pi nx\right)\right]_{0}^{1}}_{=2/(\pi n)\cos(\pi n)}+\underbrace{\int_{0}^{1}2\frac{1}{\pi n}\cos\left(\pi nx\right)dx}_{=2/(\pi n)^2\sin(\pi n)=0}+\underbrace{2\int_{0}^{1}\sin\left(\pi nx\right)dx}_{=-2/(\pi n)\cos(\pi n)+2/(\pi n)}\\&=\frac{2}{\pi n}\end{aligned}$$

Therefore, we have for
$$\begin{aligned}n=1:\quad&b_1=\frac{2}{\pi}\\ n=2:\quad&b_2=\frac{2}{2\pi}=\frac{1}{\pi}\\ n=3:\quad&b_3=\frac{2}{3\pi}\\ n=4:\quad&b_4=\frac{2}{4\pi}=\frac{1}{2\pi}\\ n=5:\quad&b_5=\frac{2}{5\pi}.\end{aligned}$$

The resulting Fourier series is

$$f(x)=\sum_{n=1}^{\infty}\frac{2}{\pi n}\sin\left(n\pi x\right)$$
$$\approx\frac{2}{\pi}\sin\left(\pi x\right)+\frac{1}{\pi}\sin\left(2\pi x\right)+\frac{2}{3\pi}\sin\left(3\pi x\right)+\frac{1}{2\pi}\sin\left(4\pi x\right)+\frac{2}{5\pi}\sin\left(5\pi x\right)+\ldots$$

**Grading manual**

(2p) for the proper odd extension

(1p) for the plot

(3p) for $b_n$

(3p) for $b_1$, $b_2$, $b_3$, $b_4$, $b_5$

(1p) for the Fourier series.

Kildesett: course=TMA4130 term=kont year=2025 problem=2 points=10 file=exam_math_4n_4d_tma4130_35-5.pdf
