### **Solution to Problem 2** (Fourier series, 15 pts)

**a)**
1. The function is periodic with period $2\pi/a$. To see this, we calculate:

   $$g_1(x + (2\pi/a)) = f(a(x + 2\pi/a)) = f(ax + 2\pi) = f(ax) = g_1(x)\,.$$

2. The function is also periodic and has period $2\pi$. (trivial observation) $g_2(x + 2\pi) = f(x + 2\pi + a) = f(x + a) = g_2(x)$.
3. Unless $a = 1$, the function is not necessarily periodic.
4. The function is periodic and has period $2\pi a$:

   $$\begin{aligned}g_4(x + 2\pi a) = a + a \cdot (f((x + 2\pi a)/a + a))^a &= a + a \cdot (f(x/a + 2\pi + a))^a\\ &= a + a \cdot (f(x/a + a))^a = g_4(x)\,.\end{aligned}$$

**b)**
1. Since the sine-function is odd, the function $f$ is even and can be expressed by cosine-terms only (i.e., $b_n = 0$ for all $n$). To get rid of the absolute-value, we treat the problem as an even half-range expansion of $\sin(x)$. The Fourier coefficients are now given by

   $$a_0 = \frac{1}{\pi} \cdot \int_{0}^{\pi} \sin x dx = \frac{2}{\pi}\,,$$

   $$\begin{aligned}a_n &= \frac{2}{\pi} \int_{0}^{\pi} \sin(x) \cdot \cos(nx) dx\\ &= \frac{2}{\pi} \int_{0}^{\pi} \frac{1}{2} \left( \sin(x - nx) + \sin(x + nx) \right) dx \quad \sin\alpha\cos\beta = \frac{1}{2}(\sin(\alpha-\beta) + \sin(\alpha+\beta))\\ &= \frac{1}{\pi} \int_{0}^{\pi} \left( -\sin((n-1)x) + \sin((n+1)x) \right) dx\\ &= \frac{1}{\pi} \left[ \frac{1}{n-1} \cos((n-1)x) - \frac{1}{n+1} \cos((n+1)x) \right]_0^{\pi}\\ &= -\frac{2}{\pi \cdot (n-1) \cdot (n+1)} \cdot \left( 1 + (-1)^n \right).\end{aligned}$$

   So, the Fourier series is given by

   $$\begin{aligned}f(x) \sim \frac{2}{\pi} - \frac{2}{\pi} \cdot \sum_{n=1}^{\infty} \frac{1 + (-1)^n}{(n-1)(n+1)} \cdot \cos(nx)\\ = \frac{2}{\pi} - \frac{4}{\pi} \cdot \sum_{k=1}^{\infty} \frac{1}{(2k-1)(2k+1)} \cdot \cos(2kx)\\ = \frac{2}{\pi} - \frac{4}{\pi} \cdot \left( \frac{\cos 2x}{1 \cdot 3} + \frac{\cos 4x}{3 \cdot 5} + \frac{\cos 6x}{5 \cdot 7} + \frac{\cos 8x}{7 \cdot 9} + \cdots \right)\end{aligned}$$

2. We know that the error can be expressed as

   $$E_N = \int_{-\pi}^{\pi} (f(x))^2 dx - \pi \cdot \left( 2a_0^2 + \sum_{n=1}^{N} (a_n^2 + b_n^2) \right)\,.$$

   For the given function and its Fourier sum, this leads to

   | $N$ | $a_N$ | $E_N$ |
   |---|---|---|
   | 0 | $2/\pi$ | $\pi - 8/\pi \approx 0.5911$ |
   | 1 | $0$ | |
   | 2 | $\frac{-4}{3\pi}$ | $\pi - 8/\pi - 16/(9\pi) \approx 0.0292$ |
   | 3 | $0$ | |
   | 4 | $\frac{-4}{15\pi}$ | $\pi - 8/\pi - 16/(9\pi) - 16/(225\pi) \approx 0.00659 < 0.01$ |

**Grading manual**

**a)** (5p): 1,2,3 gives 1 pt each, 4 gives 2 pts.

**b)** (10p):
**Subproblem 1** (7p):
2 pts identification as even function, realize that it can be written as $\cos(x)$ series/Fourier series of the even extension of $\sin(x)$,
1 pt for computation of $a_0$,
3 pts for computation of $a_n$,
1 pt for final series.
**Subproblem 2** (3p) for using the error formula and finding the correct $N$. If coefficients in b) Subproblem 1 were miscalculated, there is no chance to answer this correctly, but give 1 pt for realizing that a mistake must have happened.
1-2 pts deduction for each minor/major miscalculations (but no minus points)

Kildesett: course=TMA4130 term=host year=2021 problem=2 points=15 file=tma4130_2021h_exam.pdf
