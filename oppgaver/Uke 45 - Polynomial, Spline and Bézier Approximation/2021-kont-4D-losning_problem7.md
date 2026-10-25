### **Solution to Problem 7**

a) The degree of an interpolating polynomial is at most 2.

(b) The Lagrange polynomials $\ell_i(x)$ are quadratic functions. Since $f(x_2) = 0$, we only need to consider $\ell_1$ and $\ell_3$

$$\ell_1(x) = \prod_{j \neq 1} \frac{x - x_j}{x_1 - x_j} = \frac{(x - 0)\cdot(x - 1)}{(-1)\cdot(-2)} = \frac{x^2}{2} - \frac{x}{2}$$

$$\ell_3(x) = \prod_{j \neq 3} \frac{x - x_j}{x_3 - x_j} = \frac{((x + 1)\cdot(x - 0)}{2\cdot 1} = \frac{x^2}{2} + \frac{x}{2}$$

The interpolating polynomial (in Lagrange form) is given by

$$p(x) = f(x_1)\cdot\ell_1(x) + f(x_3)\cdot\ell_3(x) = (-\sin 1)\cdot\left(\frac{x^2}{2} - \frac{x}{2}\right) + \ln 2\cdot\left(\frac{x^2}{2} + \frac{x^2}{2}\right)\,.$$

(Further simplified is this identical to $\frac{\ln 2 - \sin 1}{2}\cdot x^2 + \frac{\sin 1 - + \ln 2}{2} x \approx -0.07416\cdot x^2 + 0.7673\cdot x$)

(c) Interpolating polynomial in Newton form

| | | | |
|---|---|---|---|
| $x = -1$ | $f = -\sin 1$ | | |
| | | $\sin 1$ | |
| $x = 0$ | $f = 0$ | | $\frac{-\sin 1 + \ln 2}{2}$ |
| | | $\ln 2$ | |
| $x = 1$ | $f = \ln 2$ | | |

So, we get the polynomial

$$p(x) = -\sin 1 + (x + 1)\cdot\left(\sin 1 + (x - 0)\cdot\frac{-\sin 1 + \ln 2}{2}\right)$$

Kildesett: course=TMA4135 term=kont year=2021 problem=7 file=retake_lf.pdf
