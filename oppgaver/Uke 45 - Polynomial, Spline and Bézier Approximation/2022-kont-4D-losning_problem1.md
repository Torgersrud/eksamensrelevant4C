### **Solution to Problem 1**

a) Lagrange polynomial and resulting interpolation polynomial for the first 3 data points:

$$L_0 = \frac{x(x-1)}{6}$$

$$L_1 = -\frac{(x-1)(x+2)}{2}$$

$$L_2 = \frac{x(x+2)}{3}$$

$$p_2(x) = \frac{x(x-1)}{3} - (x-1)(x+2) + \frac{4x(x+2)}{3} = \frac{2x^2}{3} + \frac{4x}{3} + 2$$

b) The Newton polynomials for the first three data points are

$$\omega_0 = 1$$

$$\omega_1 = x + 2$$

$$\omega_2 = x(x+2)$$

The divided difference table is given by

| $x_i$ | $f(x_i)$ | | |
|---|---|---|---|
| $-2$ | $2$ | | |
| $0$ | $2$ | $0$ | |
| $1$ | $4$ | $2$ | $2/3$ |

and thus the interpolation polynomial in Newton form is

$$p_2(x) = 2\cdot 1 + 0\cdot(x+2) + 2/3\cdot x(x+2) = \frac{2x^2}{3} + \frac{4x}{3} + 2$$

c) We compute the interpolation polynomial in Newton form which only requires to extend the divided difference table from a) accordingly using the 4th data point.

| $x_i$ | $f(x_i)$ | | | |
|---|---|---|---|---|
| $-2$ | $2$ | | | |
| $0$ | $2$ | $0$ | | |
| $1$ | $4$ | $2$ | $2/3$ | |
| $2$ | $6$ | $2$ | $0$ | $-1/6$ |

The 4th Newton polynomial and final interpolation polynomial are given by

$$\omega_3 = x(x-1)(x+2)$$

$$p_3(x) = 2\cdot 1 + 0\cdot(x+2) + 2/3\cdot x(x+2) - 1/6\cdot x(x-1)(x+2)$$

$$= -\frac{x^3}{6} + \frac{x^2}{2} + \frac{5x}{3} + 2$$

Kildesett: course=TMA4135 term=kont year=2022 problem=1 points=12 file=TMA4135-Matematikk-4D-2022s_lf.pdf
