### **Solution to Problem 6**

a) The sketch looks for example like

$$(3 \text{ P}.)$$

[Figure: plot with $x$-axis from $-2\pi$ to $2\pi$ and ticks at every $k\pi/2$, $k = -4, \ldots, 4$. The blue solid curve $g(x)$ is the $2\pi$-periodic continuation of the even extension: a triangular pulse of height $\pi/2$ at $x = 0$ decreasing linearly to $0$ at $x = \pm\pi/2$, equal to $0$ for $\pi/2 \leq |x| < 3\pi/2$, and rising linearly again to height $\pi/2$ at $x = \pm 2\pi$ (rising off the plot at both ends). The black dashed curve $f_o(x)$ shows the odd extension on one period: on $[0, \pi/2)$ it coincides with the decreasing branch of $g$ from $(0, \pi/2)$ down to $(\pi/2, 0)$, continues dashed along the axis to $\pi$; on $(-\pi/2, 0)$ it is the dashed segment from $(-\pi/2, 0)$ down to $(0, -\pi/2)$. Legend at bottom right: blue solid $g(x)$, black dashed $f_o(x)$.]

where the important points are at $\frac{k\pi}{2}, k = -4, \ldots, 4$.

b) The Fourier coefficients are $b_n = 0$ for $n \in \mathbb{N}$, since $g$ is odd.

$$(1 \text{ P}.)$$

For the $a_0, a_n$ we can use the formula for even functions and compute (checking for example the $2L$ periodic formula, then $L = \pi$).

We obtain

$$(1 \text{ P}.)$$

$$a_0 = \frac{2}{\pi} \int_0^{\pi} f(x) \, \mathrm{d}x = \frac{2}{\pi} \int_0^{\frac{\pi}{2}} \frac{\pi}{2} - x \, \mathrm{d}x = \frac{2}{\pi} \left[\frac{\pi}{2} x - \frac{1}{2} x^2\right]_0^{\frac{\pi}{2}} = \frac{2}{\pi}\left(\frac{\pi^2}{4} - \frac{\pi^2}{8}\right) = \frac{\pi}{4}.$$

For the remaining terms we compute

$$(2 \text{ P}.)$$

$$\begin{aligned} a_n &= \frac{2}{\pi} \int_0^{\pi} f(x) \cos(nx) \, \mathrm{d}x \\ &= \frac{2}{\pi} \int_0^{\frac{\pi}{2}} \left(\frac{\pi}{2} - x\right) \cos(nx) \, \mathrm{d}x \\ &= \frac{2}{\pi}\frac{\pi}{2} \int_0^{\frac{\pi}{2}} \cos(nx) \, \mathrm{d}x - \frac{2}{\pi} \int_0^{\frac{\pi}{2}} x \cos(nx) \, \mathrm{d}x \end{aligned}$$

The first term we can just integrate and for the second we use integration by parts (note that integrating the cos here does not introduce a minus)

$$(3 \text{ P}.)$$

$$\begin{aligned} a_n &= \left[\frac{1}{n}\sin(nx)\right]_0^{\frac{\pi}{2}} - \frac{2}{\pi}\left[\frac{x}{n}\sin(nx)\right]_0^{\frac{\pi}{2}} + \frac{2}{\pi} \int_0^{\frac{\pi}{2}} 1 \cdot \frac{1}{n}\sin(nx) \, \mathrm{d}x \\ &= \frac{1}{n}\left(\sin\left(\frac{n\pi}{2}\right) - \sin(0)\right) - \frac{2}{\pi}\left(\frac{\pi}{2n}\sin\left(\frac{n\pi}{2}\right) - 0 \sin(0)\right) + \frac{2}{\pi}\left[-\frac{1}{n^2}\cos(nx)\right]_0^{\frac{\pi}{2}} \\ &= \frac{1}{n}\sin\left(\frac{n\pi}{2}\right) + \frac{1}{n}\sin\left(\frac{n\pi}{2}\right) - \frac{2}{\pi n^2}\left(\cos\frac{n\pi}{2} - 1\right) \\ &= \frac{2}{n}\sin\left(\frac{n\pi}{2}\right) + \frac{2}{\pi n^2}\left(\cos\frac{n\pi}{2} - 1\right) \end{aligned}$$

c) The function $g$ is piecewise continuously differentiable and hence for every $x$ the Fourier partial sum converges to $g$.

$$(2 \text{ P}.)$$

d) The derivative of the Fourier partial sum is itself a Fourier series.

Indeed it approximates $g'(x) = \begin{cases}1 & \text{for } -\frac{\pi}{2} < x < 0\\ -1 & \text{for } 0 < x < \frac{\pi}{2}\\ 0 & \text{else}\end{cases}, x \in [-\pi, \pi) \backslash \{-\frac{\pi}{2}, 0, \frac{\pi}{2}\},$

which is not defined for $x \in \{-\frac{\pi}{2}, 0, \frac{\pi}{2}\}$ since $g$ is not differentiable there. The Fourier series however converges to the mean of the limits, so we get $\lim\limits_{n \to \infty} S_n'(0) = 0$.

$$(2 \text{ P}.)$$

Kildesett: course=TMA4135 term=kont year=2022 problem=6 points=14 file=TMA4135-Matematikk-4D-2022s_lf.pdf
