### **Solution to Problem 6**

Write $x_0 = -10$; $x_1 = -1$; $x_2 = 0$; $x_3 = 1$, and $y_0 = -3925$; $y_1 = -1$; $y_2 = 5$; and $y_3 = 13$ The Lagrange polynomials are $\ell_i(x) = \prod_{i \neq k=0}^{3} \frac{x - x_k}{x_i - x_k}$.

$$\begin{aligned} \ell_0(x) &= \frac{(x+1)x(x-1)}{(-10+1)(-10)(-10-1)} \\ &= -\frac{1}{990} (x^3 - x). \\ \ell_1(x) &= \frac{(x+10)x(x-1)}{(-1+10)(-1)(-1-1)} \\ &= \frac{1}{18} (x^3 + 9x^2 - 10x). \\ \ell_2(x) &= \frac{(x+10)(x+1)(x-1)}{(10)(1)(-1)} \\ &= -\frac{1}{10} (x^3 + 10x^2 - x - 10). \\ \ell_3(x) &= \frac{(x+10)(x+1)x}{(1+10)(1+1)(1)} \\ &= \frac{1}{22} (x^3 + 11x^2 + 10x). \end{aligned}$$

Thus

$$\begin{aligned} p(x) &= \sum_{i=0}^{3} y_i \ell_i(x) \\ &= \frac{3925}{990} (x^3 - x) - \frac{1}{18} (x^3 + 9x^2 - 10x) - \frac{5}{10} (x^3 + 10x^2 - x - 10) + \frac{13}{22} (x^3 + 11x^2 + 10x) \\ &= 4x^3 + x^2 + 3x + 5. \end{aligned}$$

Kildesett: course=TMA4135 term=host year=2021 problem=6 points=6 file=tma4135_2021h_exam-4.pdf
