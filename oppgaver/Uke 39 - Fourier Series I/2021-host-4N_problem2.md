### **Problem 2** Fourier series [15 pts]

**a)** Assume that $f \colon \mathbb{R} \to \mathbb{R}$ is a $2\pi$-periodic function and that $a \in \mathbb{N} \setminus \{0\}$ is a constant. Decide for all the following functions whether they are also necessarily periodic. If they are, what is their (fundamental) period?

1. $g_1(x) := f(a \cdot x)$,
2. $g_2(x) := f(x + a)$,
3. $g_3(x) := f(x^a)$,
4. $g_4(x) := a + a \cdot (f(x/a + a))^a$.

**b)**
1. Calculate the Fourier series of the function $f(x) = |\sin x|$ defined on $[-\pi, \pi]$. Explicitly write down the first five non-vanishing terms of the Fourier sum. **Hint:** You can use the fact that the sine is an odd function, and use your knowledge about Fourier series of even functions.
2. With $f$ from b) 1., how many terms in the partial Fourier sum $F_N(x) = a_0 + \sum_{n=1}^{N} (a_n \cos(nx) + b_n \sin nx)$ need to be taken into account such that the square error

   $$E_N = \int_{-\pi}^{\pi} (f(x) - F_N(x))^2 \, dx,$$

   is less than 0.01?

   **Hint:** The number is not very large. We recommend that you just calculate (to four digits) the error for the first few partial sums. You can use that $\int_{-\pi}^{\pi} (f(x))^2 \, dx = \pi$.

Kildesett: course=TMA4130 term=host year=2021 problem=2 points=15 file=tma4130_2021h_exam.pdf
