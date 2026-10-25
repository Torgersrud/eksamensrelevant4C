### **Solution to Problem 1**

**a)** Using partial integration we compute

$$a_0=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(t)\,\mathrm{d}t=\frac{1}{2\pi}\int_{0}^{\pi}t^2\,\mathrm{d}t=\frac{\pi^2}{6}$$

$$a_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\cos nt\,\mathrm{d}t=\frac{1}{\pi}\int_{0}^{\pi}t^2\cos nt\,\mathrm{d}t$$

$$=\frac{1}{\pi}\left[\frac{2t}{n^2}\cos nt+\frac{-2+n^2t^2}{n^3}\sin nt\right]_{t=0}^{\pi}$$

$$=\frac{2}{n^2}\cos n\pi=(-1)^n\frac{2}{n^2}$$

$$b_n=\frac{1}{\pi}\int_{-\pi}^{\pi}f(t)\sin nt\,\mathrm{d}t=\frac{1}{\pi}\int_{0}^{\pi}t^2\sin nt\,\mathrm{d}t$$

$$=\frac{1}{\pi}\left[\frac{2t}{n^2}\sin nt+\frac{2-n^2t^2}{n^3}\cos nt\right]_{t=0}^{\pi}$$

$$=\frac{1}{\pi}\left(\frac{2}{n^3}\cos n\pi-\frac{\pi^2}{n}\cos n\pi-\frac{2}{n^3}\right)$$

$$=\begin{cases}-\dfrac{\pi}{n}&\text{if $n$ even}\\[6pt] \dfrac{\pi}{n}-\dfrac{4}{n^3\pi}&\text{if $n$ odd.}\end{cases}$$

for $n=1,2,\ldots$. The Fourier series of $f(t)$ is

$$a_0+\sum_{n=1}^{\infty}\left(a_n\cos nt+b_n\sin nt\right).$$

One could compute the complex Fourier series instead.

**b)** Look at the Fourier series of $f$ near $\pi$. Then

$$\frac{\pi^2}{2}=\frac{1}{2}\left(\lim_{t\to\pi^+}f(t)+\lim_{t\to\pi^-}f(t)\right)$$

$$=a_0+\sum_{n=1}^{\infty}\left(a_n\cos n\pi+b_n\sin n\pi\right)$$

$$=a_0+\sum_{n=1}^{\infty}a_n\cdot(-1)^n$$

$$=\frac{\pi^2}{6}+\sum_{n=1}^{\infty}(-1)^n\frac{2}{n^2}$$

$$=\frac{\pi^2}{6}+\sum_{n=1}^{\infty}\frac{2\cdot(-1)^{2n}}{n^2}$$

$$=\frac{\pi^2}{6}+2\sum_{n=1}^{\infty}\frac{1}{n^2},$$

which gives

$$\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\frac{\pi^2}{2}-\frac{\pi^2}{6}}{2}=\frac{\pi^2}{6}.$$

Kildesett: course=TMA4130 term=host year=2013 problem=1 file=eksamen-bok_2013h.pdf
