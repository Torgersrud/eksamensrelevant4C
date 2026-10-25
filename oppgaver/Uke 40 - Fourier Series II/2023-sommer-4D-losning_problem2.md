### **Solution to Problem 2**

The sketch looks like

$$(3 \text{ P}.)$$

[Figure: plot with $x$-axis ticked from $-3\pi$ to $3\pi$ and $y$-axis ticked at $\pm\pi$ and $\pm\pi^2$, curve labelled $g(x)$. The graph shows the odd $2\pi$-periodic extension $f$ of $x^2$: a dark blue central branch following $-x^2$ on $[-\pi, 0]$ from $(-\pi, -\pi^2)$ through the origin and $x^2$ on $[0, \pi]$ up to $(\pi, \pi^2)$; light blue shifted copies: rising on $[-2\pi, -\pi]$ from $(-2\pi, 0)$ up to height $\pi^2$ and falling to $(-3\pi, -\pi^2)$ at the left edge, falling from $(\pi, -\pi^2)$ up to $(2\pi, 0)$ and rising on $[2\pi, 3\pi]$ to height $\pi^2$ at the right edge.]

We can use that the odd extension is an odd function. Hence $a_n = 0$ for $n = 0, 1, 2, \ldots$.

$$(1 \text{ P}.)$$

For the $b_n$ we use, that integrating over half an interval and multiplying that by 2 yields the result. Hence We get

$$b_n = \frac{2}{\pi} \int_0^\pi g(x) \sin(nx) \mathrm{d}x = \frac{2}{\pi} \int_0^\pi x^2 \sin(nx) \mathrm{d}x$$

We apply integration by parts. We have in $\int f g' \mathrm{d}x = fg - \int f' g \mathrm{d}x$ here with $f(x) = x^2$ and $g'(x) = \sin(nx)$ so $f'(x) = 2x$ and $g(x) = -\frac{1}{n} \cos(nx)$ We obtain

$$(2 \text{ P}.)$$

$$b_n = \frac{2}{\pi} \left( -\frac{x^2}{n} \cos(nx) \Big|_0^\pi + \int_0^\pi \frac{2x}{n} \cos(nx) \mathrm{d}x. \right)$$

We perform another integration by parts on the second term with $f(x) = x$ and $g'(x) = \frac{1}{n} \cos(nx)$ and hence $f'(x) = 1$ and $g(x) = \frac{2}{n^2} \sin(nx)$. We obtain

$$(2 \text{ P}.)$$

$$b_n = \frac{2}{\pi} \left( -\frac{\pi^2}{n} \cos(n\pi) + 0 + \frac{2x}{n^2} \sin(nx) \Big|_0^\pi - \int_0^\pi \frac{2}{n^2} \sin(nx) \mathrm{d}x \right)$$

We keep the first term, the central term vanishes since $\sin(n\pi) = \sin(0) = 0$ and we can compute the anti-derivative of the last integral

$$(2 \text{ P}.)$$

$$\begin{aligned}b_n = \frac{2}{\pi} \left( -\frac{\pi^2}{n} \cos(n\pi) + \frac{2}{n^3} \cos(nx) \Big|_0^\pi \right) &= \frac{2}{\pi} \left( -\frac{\pi^2}{n} \cos(n\pi) + \frac{2}{n^3} \cos(n\pi) - \frac{2}{n^3} \right)\\
&= \frac{2\pi}{n} (-1)^{n+1} + \frac{4}{\pi n^3} (-1)^n - \frac{4}{\pi n^3}\end{aligned}$$

The last simplification is not necessary to get the points for this computation.

Kildesett: course=TMA4135 term=sommer year=2023 problem=2 file=tma4125-30-35-matematikk4n-d-2023s_lf_correct.pdf
