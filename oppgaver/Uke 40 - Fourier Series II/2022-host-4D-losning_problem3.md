### **Solution to Problem 3**

The odd extension $g$ of $f$ is shown in the picture below:

[Figure: plot with arrowed axes, the $y$-axis marked $1$, $2$, $3$ above the origin and the $x$-axis marked $1$, $2$, $3$ to the right. The graph of the odd period-2 extension $g$ consists of six disjoint parallel line segments of slope $1$: segments rising from $2$ to $3$ on the intervals $(-2, -1)$, $(0, 1)$ and $(2, 3)$ — the middle one being the line $2 + x$ — and segments rising from $-3$ to $-2$ on the intervals $(-3, -2)$, $(-1, 0)$ and $(1, 2)$.]

Since $g$ is an odd function, all its Fourier cosine coefficients $a_n$ (including $a_0$) are equal to 0 and we have

$$\begin{aligned}b_n &= 2 \int_0^1 (2 + x) \sin(n\pi x) \, dx\\
&= 4 \int_0^1 \sin(n\pi x) \, dx + 2 \int_0^1 x \sin(n\pi x) \, dx\\
&= -4 \left. \frac{\cos(n\pi x)}{n\pi} \right|_0^1 - \left. \frac{2x \cos(n\pi x)}{n\pi} \right|_0^1 + \frac{2}{n\pi} \int_0^1 \cos(n\pi x) \, dx\\
&= -4 \frac{\cos(n\pi)}{n\pi} + 4 \frac{1}{n\pi} - 2 \frac{\cos(n\pi)}{n\pi} + 0 + \left. \frac{2 \sin(n\pi x)}{n^2 \pi^2} \right|_0^1\\
&= \frac{2}{n\pi} - 6 \frac{(-1)^{n+1}}{n\pi}.\end{aligned}$$

Thus we get the Fourier series

$$g(x) = \sum_{n=1}^\infty \frac{2 + 6(-1)^n}{n\pi} \sin(n\pi x).$$

Kildesett: course=TMA4135 term=host year=2022 problem=3 file=math4nd-2022h_published.pdf
