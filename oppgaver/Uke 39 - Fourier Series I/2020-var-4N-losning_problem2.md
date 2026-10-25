### **Solution to Problem 2** (Fourier series)

Recall that the Heaviside $u$ is defined by

$$u(x) = \begin{cases} 0 & x < 0 \\ 1 & x \ge 0 \end{cases}$$

**a)** Sketch the function $-u(x+\pi) + 2u(x)$ over the interval $[-\pi, \pi]$. (2 pts)

The sketch shows the function taking the value $+1$ for $x \geq 0$ and $-1$ for $x < 0$ over $[-\pi, \pi]$ (the sign function).

**b)** Compute the Fourier series $f \sim a_0 + \sum_{n=1}^{\infty} a_n \cos nx + \sum_{n=1}^{\infty} b_n \sin(nx)$ for $f(x) = \cos(3x) - \frac{1}{2}\sin(2x) - u(x+\pi) + 2u(x)$.

**Solution:** Write $f$ as $f = f_1 + f_2$ with $f_1(x) = \cos 3x - \frac{1}{2}\sin(2x)$. Then the trigonometric series of $f_1$ is just the function itself, since it is already a *trigonometric series*. (2 pts)

Turning to $f_2$, we note that $f_2$ is an **odd function**, so it is sufficient to compute the coefficients $b_n$. (2 pts) Then

$$\begin{aligned} b_n &= \frac{1}{\pi} \int_{-\pi}^{\pi} f_2(x) \sin(nx)\, dx \\ &= \frac{2}{\pi} \int_{0}^{\pi} \sin(nx)\, dx = -\frac{2}{n\pi} \cos(nx) \Big|_{0}^{\pi} \\ &= \frac{2}{n\pi} \big( 1 - \cos n\pi \big) = \frac{2}{n\pi} \big( 1 + (-1)^n \big). \end{aligned}$$

(3 pts, computation of $b_n$)

**Final solution:** $f \sim -\frac{1}{2}\sin 2x + \cos 3x + \sum_{n=1}^{\infty} \frac{2}{n\pi} \big( 1 + (-1)^n \big) \sin nx$. (1 pt)

- [?] The scheme's last simplification writes $1 - \cos n\pi = 1 + (-1)^n$; since $\cos n\pi = (-1)^n$ the intended final coefficient is presumably $\frac{2}{n\pi}\big(1 - (-1)^n\big)$ (nonzero for odd $n$, as the sketched sign function requires). The source is transcribed as written.

- **Alternative:** If you compute coefficients mechanically for the *entire* function (not only $f_2$), then 3 pts for computing $a_n$ correctly, 4 pts for computing $b_n$ correctly.

Kildesett: course=TMA4125 term=var year=2020 problem=2 file=exam_v20_short.pdf
