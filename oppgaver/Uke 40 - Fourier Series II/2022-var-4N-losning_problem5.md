### **Solution to Problem 5** (Fourier Series, 14 points)

a) The sketch looks for example like (2 P.)

[Plot: the $2\pi$-periodic curve $g$ drawn in blue over $[-2\pi,2\pi]$: it is zero on $\left[-\frac{\pi}{2},\frac{\pi}{2}\right]$ and on the remaining outer part of each period, and each period contains two parallel slope-$-1$ line segments — one from $\left(\frac{\pi}{2},0\right)$ down to $\left(\pi,-\frac{\pi}{2}\right)$ (repeated one period earlier from $\left(-\frac{3\pi}{2},0\right)$ to $\left(-\pi,-\frac{\pi}{2}\right)$), and one jumping up to $\left(\pi,\frac{\pi}{2}\right)$ and descending to $\left(\frac{3\pi}{2},0\right)$ (repeated from $\left(-\pi,\frac{\pi}{2}\right)$ to $\left(-\frac{\pi}{2},0\right)$). Vertical axis labelled $g(x)$ with ticks $\frac{\pi}{2}$ and $-\frac{\pi}{2}$; horizontal axis labelled $x$ with ticks $-2\pi$, $-\frac{3\pi}{2}$, $-\pi$, $-\frac{\pi}{2}$, $\frac{\pi}{2}$, $\pi$, $\frac{3\pi}{2}$, $2\pi$.]

where the important points are at $\frac{k\pi}{2},k=-4,\ldots,4$.

b) The Fourier coefficients are $a_0=a_n=0$ for $n\in\mathbb{N}$, since $g$ is odd. (1 P.)
For the $b_n$ we can use the formula for odd functions and compute (checking for example the $2L$ periodic formula, then $L=\pi$) (2 P.)

$$\begin{aligned}b_n&=\frac{2}{\pi}\int_0^{\pi}f(x)\sin(nx)\mathrm{d}x\\
&=\frac{2}{\pi}\int_{\frac{\pi}{2}}^{\pi}\left(\frac{\pi}{2}-x\right)\sin(nx)\mathrm{d}x\\
&=\frac{2}{\pi}\frac{\pi}{2}\int_{\frac{\pi}{2}}^{\pi}\sin(nx)\mathrm{d}x-\frac{2}{\pi}\int_{\frac{\pi}{2}}^{\pi}x\sin(nx)\mathrm{d}x\end{aligned}$$

The first term we can just integrate and for the second we use integration by parts (note that integrating the sin here introduces a minus) (4 P.)

$$\begin{aligned}b_n&=\left[-\frac{1}{n}\cos(nx)\right]_{\frac{\pi}{2}}^{\pi}-\frac{2}{\pi}\left[-\frac{x}{n}\cos(nx)\right]_{\frac{\pi}{2}}^{\pi}+\frac{2}{\pi}\int_{\frac{\pi}{2}}^{\pi}1\cdot\left(-\frac{1}{n}\cos(nx)\right)\mathrm{d}x\\
&=-\frac{1}{n}\left(\cos(n\pi)-\cos\frac{n\pi}{2}\right)+\frac{2}{n\pi}\left(\pi\cos(n\pi)-\frac{\pi}{2}\cos\frac{n\pi}{2}\right)+\frac{2}{\pi}\left[-\frac{1}{n^2}\sin(nx)\right]_{\frac{\pi}{2}}^{\pi}\\
&=-\frac{1}{n}\cos(n\pi)+\frac{1}{n}\cos\frac{n\pi}{2}+\frac{2}{n}\cos(n\pi)-\frac{1}{n}\cos\frac{n\pi}{2}-\frac{2}{\pi n^2}\left(\sin(n\pi)-\sin\frac{n\pi}{2}\right)\\
&=\frac{1}{n}\cos(n\pi)+\frac{2}{\pi n^2}\sin\frac{n\pi}{2}\end{aligned}$$

Now $\cos(n\pi)=(-1)^n$ and $\sin\frac{n\pi}{2}=0$ if $n$ is even and $\sin\frac{(2k+1)\pi}{2}=(-1)^k$ so we can simplify further (1 P.)

$$g\sim\sum_{n=1}^{\infty}\frac{(-1)^n}{n}\sin(nx)+\frac{2}{\pi}\sum_{k=1}^{\infty}\frac{(-1)^k}{(2k+1)^2}\sin\big((2k+1)x\big)$$

c) The function $g$ is piecewise continuously differentiable and the limits of both the function $g$ as well as the derivative $g'$ exist at every point. The left and right limits of $g$ at $x_0$ and $x_1$ are They are (2 P.)

$$\lim_{x\to x_0^-}g(x)=-\frac{\pi}{2},\quad\lim_{x\to x_0^+}g(x)=\frac{\pi}{2},\quad\lim_{x\to x_1^-}g(x)=\lim_{x\to x_1^+}g(x)=0$$

since at $x_1$ the function $g$ is even continuous. Hence the Fourier partial sum converges to $\lim\limits_{n\to\infty}S_n(x_0)=\dfrac{1}{2}\left(\dfrac{\pi}{2}-\dfrac{\pi}{2}\right)=0$ and $\lim\limits_{n\to\infty}S_n(x_1)=0$. (2 P.)

The second limit at $x_0$ can *alternatively* also be obtained, seeing that setting $x=x:0$ in the series from the previous point, all terms vanish.

Kildesett: course=TMA4125 term=var year=2022 problem=5 points=14 file=TMA4125-Matematikk-4N-2022v_lf.pdf
