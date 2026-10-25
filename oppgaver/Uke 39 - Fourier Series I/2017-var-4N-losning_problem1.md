### **Solution to Problem 1**

The graph of $g(x)$ is displayed below. We have

$$\begin{array}{rcl}
b_n &=& \displaystyle\frac{2}{2}\int_{0}^{2}(1-x)\sin\frac{n\pi x}{2}dx\\[8pt]
&=& \displaystyle\int_{1}^{2}\sin\frac{n\pi x}{2}dx-\int_{1}^{2}x\sin\frac{n\pi x}{2}dx\\[8pt]
&=& \displaystyle\left[-\frac{2}{n\pi}\cos\frac{n\pi x}{2}\right]_{1}^{2}-\left[-\frac{2}{n\pi}x\cos\frac{n\pi x}{2}\right]_{1}^{2}+\int_{1}^{2}-\frac{2}{n\pi}\cos\frac{n\pi x}{2}dx\\[8pt]
&=& \displaystyle\frac{2}{n\pi}\left(-\cos n\pi+\cos\frac{n\pi}{2}+2\cos n\pi-\cos\frac{n\pi}{2}\right)+\left[-\frac{4}{(n\pi)^2}\sin\frac{n\pi x}{2}\right]_{1}^{2}\\[8pt]
&=& \displaystyle\frac{2}{n\pi}\cos n\pi+\frac{4}{(n\pi)^2}\sin\frac{n\pi}{2}
\end{array}$$

Now $\cos n\pi=(-1)^n$, and moreover $\sin\frac{n\pi}{2}$ is zero if $n$ is even, whilst $\sin\frac{(2k+1)\pi}{2}=(-1)^k$, we may write the Fourier series of $g$ as

$$g(x)=\frac{2}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^n}{n}\sin\frac{n\pi x}{2}+\frac{4}{\pi^2}\sum_{k=1}^{\infty}\frac{(-1)^k}{(2k+1)^2}\sin\frac{(2k+1)\pi x}{2}$$

Kildesett: course=TMA4125 term=var year=2017 problem=1 file=exam.pdf
