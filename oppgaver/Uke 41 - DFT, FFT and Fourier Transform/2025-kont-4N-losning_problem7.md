### **Solution to Problem 7** **Fourier Transform [10 pts]**

a) We must consider the cases $a>0$ and $a<0$.

$a>0$:
$$\begin{aligned}F(f(at))(\omega)&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(ax)\exp(-i\omega x)dx\\&=\frac{1}{a\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)\exp\left(-i\frac{\omega}{a}x\right)dx\\&=\frac{1}{a}F(f(t))\left(\frac{\omega}{a}\right)\end{aligned}$$

Here we used a change of variables: $ax=y$, $a\,dx=dy$.

$a<0$:
$$\begin{aligned}F(f(at))(\omega)&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(ax)\exp(-i\omega x)dx\\&=\frac{1}{a\sqrt{2\pi}}\int_{\infty}^{-\infty}f(x)\exp\left(-i\frac{\omega}{a}x\right)dx\\&=-\frac{1}{a}F(f(t))\left(\frac{\omega}{a}\right)\end{aligned}$$

From this we conclude that
$$F(f(at))(\omega)=\frac{1}{|a|}F(f(t))\left(\frac{\omega}{a}\right).$$

b)
$$\tilde{h}=\tilde{f}\tilde{g}=\exp(-\omega^2)\frac{1}{1+\omega^2}.$$
$$\tilde{f}=\mathcal{F}\left(\frac{1}{\sqrt{2}}\exp\left(\frac{-t^2}{4}\right)\right)$$
$$\tilde{g}=\mathcal{F}\left(\sqrt{\frac{\pi}{2}}\exp(-|t|)\right)$$

Recall that we defined the convolution product without the $\frac{1}{\sqrt{2\pi}}$ coefficient. Therefore
$$\begin{aligned}h(t)&=f*g(t)\\&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{1}{\sqrt{2}}\exp\left(\frac{-(t-x)^2}{4}\right)\sqrt{\frac{\pi}{2}}\exp(-|x|)dx\\&=\frac{1}{2\sqrt{2}}\int_{-\infty}^{\infty}\exp\left(\frac{-(t-x)^2}{4}\right)\exp(-|x|)dx\end{aligned}$$

**Grading manual** (10p)

a) (6p)

b) (4p)

Kildesett: course=TMA4130 term=kont year=2025 problem=7 points=10 file=exam_math_4n_4d_tma4130_35-5.pdf
