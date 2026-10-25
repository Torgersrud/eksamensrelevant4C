### **Solution to Problem 5** (Interpolation, 9 pts)

Lagrange and Newton polynomial for the first 3 data points are given by

$$\begin{aligned}L_0 &= \frac{(x-3)(x-1)}{8}\\ L_1 &= -\frac{(x-3)(x+1)}{4}\\ L_2 &= \frac{(x-1)(x+1)}{8}\\ p_2(x) &= \frac{(x-3)(x-1)}{8} - (x-3)(x+1) + \frac{3(x-1)(x+1)}{8}\\ p_2(x) &= -\frac{x^2}{2} + \frac{3x}{2} + 3\\ \omega_0 &= 1\\ \omega_1 &= x+1\\ \omega_2 &= (x-1)(x+1)\end{aligned}$$

    Divided difference table =
    [[-1, 1, 3], [1, 4, 3], [3/2, -1/2, None], [-1/2, None, None]]

Using Newton form for the 4th data point.

    Divided difference table =
    [[-1, 1, 3, 4], [1, 4, 3, 6], [3/2, -1/2, 3, None], [-1/2, 7/6, None, None], [1/3, None, None, None]]

4th Newton polynomial and final interpolation polynomial.

$$\begin{aligned}\omega_3 &= (x-3)(x-1)(x+1)\\ p_3(x) &= \frac{x^3}{3} - \frac{3x^2}{2} + \frac{7x}{6} + 4\end{aligned}$$

**Grading manual**

**a)** (3p): 2 pts for interpolation polynomial in Lagrange form, 1 pt for final polynomial
no points for systematic major blunders when setting up Lagrange basis function, e.g. calculating $l_0$ via

$$l_0(x) = (x-x_1)(x-x_2) \qquad \text{instead of} \quad l_0(x) = \frac{(x-x_1)(x-x_2)}{(x_0-x_1)(x_0-x_2)}$$

**b)** (3p): 2 pts for computation of divided difference table, 1 pt for interpolation polynomial in Newton form
Only Newton form is required, no point deduction for miscalculations during additional rewriting into monomial form $p_n(x) = a_n x^n + \cdots + a_1 x + a_0$.

**c)** (3p): Can be computed using either the Lagrange or Newton (simpler!) form,
2 pts for computation of divided difference table or Lagrange polynomials,
1 pt for interpolation polynomial in either Newton or Lagrange form
Only correct Newton (or Lagrange) form is required, no point deduction for miscalculations during additional rewriting into monomial form $p_n(x) = a_n x^n + \cdots + a_1 x + a_0$.

Kildesett: course=TMA4130 term=host year=2021 problem=5 points=9 file=tma4130_2021h_exam.pdf
