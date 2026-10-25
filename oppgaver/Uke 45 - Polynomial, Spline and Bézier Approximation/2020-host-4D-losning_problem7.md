### **Solution to Problem 7**

a) With $x_0=-2$, $x_1=-1$, $x_2=1$, $x_3=2$, we get the following cardinal functions:

$$\ell_0(x)=\prod_{j=1}^{3}\frac{x-x_j}{x_0-x_j}=\frac{(x+1)(x-1)(x-2)}{(-2-(-1))(-2-1)(-2-2)}=\frac{x^3-2x^2-x+2}{-12}$$

$$\ell_2(x)=\prod_{j\neq 2}\frac{x-x_j}{x_2-x_j}=\frac{(x+2)(x+1)(x-2)}{(1+2)(1+1)(1-2)}=\frac{x^3+x^2-4x-4}{-6}$$

$$\ell_3(x)=\prod_{j\neq 3}\frac{x-x_j}{x_3-x_j}=\frac{(x+2)(x+1)(x-1)}{(2+2)(2+1)(2-1)}=\frac{x^3+2x^2-x-2}{12}$$

There is no need to compute $\ell_1(x)$ because the function value is zero.

The interpolating polynomial in Lagrange form is

$$p(x)=-5\ell_0(x)+\ell_2(x)+4\ell_3(x)$$

$$=\Big(\frac{5}{12}x^3-\frac{10}{12}x^2-\frac{5}{12}x+\frac{10}{12}\Big)+\Big(\frac{x^3+x^2-4x-4}{-6}\Big)+\Big(\frac{4}{12}x^3+\frac{8}{12}x^2-\frac{4}{12}x-\frac{8}{12}\Big)$$

$$=\frac{7}{12}x^3-\frac{1}{3}x^2-\frac{1}{12}x+\frac{10}{12}$$

b) Newton form:

| $x_i$ | $f(x_i)$ | | | |
|---|---|---|---|---|
| $-2$ | $-5$ | | | |
| $-1$ | $0$ | $5$ | | |
| $1$ | $1$ | $\frac{1}{2}$ | $-\frac{3}{2}$ | |
| $2$ | $4$ | $3$ | $\frac{5}{6}$ | $\frac{7}{12}$ |

Polynomial:

$$p(x)=-5+(x-(-2))\Big(5+(x-(-1))\Big(-\frac{3}{2}+\frac{7}{12}(x-1)\Big)\Big)$$

c) Simplify one of the forms, for example:

$$p(x)=-5+(x-(-2))\Big(5+(x-(-1))\Big(-\frac{3}{2}+\frac{7}{12}(x-1)\Big)\Big)$$

$$=-5+(x-(-2))\Big(5+(x-(-1))\Big(-\frac{3}{2}+\frac{7}{12}x-\frac{7}{12}\Big)\Big)$$

$$=-5+(x-(-2))\Big(5+(x-(-1))\Big(-\frac{25}{12}+\frac{7}{12}x\Big)\Big)$$

$$=-5+(x-(-2))\Big(5+(x+1)\Big(-\frac{25}{12}+\frac{7}{12}x\Big)\Big)$$

$$=-5+(x-(-2))\Big(5+\Big(-\frac{25}{12}x+\frac{7}{12}x^2-\frac{25}{12}+\frac{7}{12}x\Big)\Big)$$

$$=-5+(x-(-2))\Big(5+\Big(\frac{7}{12}x^2-\frac{18}{12}x-\frac{25}{12}\Big)\Big)$$

$$=-5+(x-(-2))\Big(\frac{60}{12}+\Big(\frac{7}{12}x^2-\frac{18}{12}x-\frac{25}{12}\Big)\Big)$$

$$=-5+(x-(-2))\Big(\frac{7}{12}x^2-\frac{18}{12}x+\frac{35}{12}\Big)$$

$$=-5+(x+2)\Big(\frac{7}{12}x^2-\frac{18}{12}x+\frac{35}{12}\Big)$$

$$=-5+(\frac{7}{12}x^3-\frac{18}{12}x^2+\frac{35}{12}x+\frac{14}{12}x^2-\frac{36}{12}x+\frac{70}{12})$$

$$=-\frac{60}{12}+(\frac{7}{12}x^3-\frac{1}{3}x^2-\frac{1}{12}x+\frac{70}{12})$$

$$=\frac{7}{12}x^3-\frac{1}{3}x^2-\frac{1}{12}x+\frac{10}{12}$$

d) Use the expanded form to get $f(0)\approx p(0)=\frac{7}{12}\cdot 0^3-\frac{1}{3}\cdot 0^2-\frac{1}{12}\cdot 0+\frac{10}{12}=\frac{10}{12}$.

Kildesett: course=TMA4135 term=host year=2020 problem=7 points=10 file=completeexam_nosolutions.pdf
