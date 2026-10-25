### **Problem 1** **Interpolation, Quadrature (15 points)**

Consider the function $f(x)=4x^2+x-5+\frac{3}{x}+\cos(\pi x)$.
This function has the following function values

$$\begin{array}{cccc}i&0&1&2\\ x_i&\frac{1}{2}&1&\frac{3}{2}\\ f(x_i)&\frac{5}{2}&2&\frac{15}{2}\end{array}$$

a) Compute the polynomial $p(x)$ of lowest degree interpolating the given points $(x_i,f(x_i))$, $i=0,1,2$.

b) Approximate the Integral $I[f]=\int_{\frac{1}{2}}^{\frac{3}{2}}f(x)\,\mathrm{d}x$ by

1) integrating the polynomial $p(x)$ from a).

2) the Simpson rule.

3) the composite trapezoidal rule with $m=2$ subintervals.

Two of the three approximations yield the same result.

4) Explain why two of the approximations yield the same result.

c) Compare the Simpson rule and the composite trapezoidal rule with respect to their degree of precision.
Which of these two do you expect to have a smaller error?

Kildesett: course=TMA4125 term=var year=2024 problem=1 points=15 file=math4n-2024v-en_lf.pdf
