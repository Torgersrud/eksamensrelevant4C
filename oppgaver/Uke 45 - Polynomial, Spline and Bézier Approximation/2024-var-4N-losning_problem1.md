### **Solution to Problem 1** **Interpolation, Quadrature (15 points)**

a) For example with Lagrange this reads
$$\begin{aligned}\ell_0(x)&=\frac{x-x_1}{x_0-x_1}\cdot\frac{x-x_2}{x_0-x_2}=\frac{x-1}{-\frac{1}{2}}\cdot\frac{x-\frac{3}{2}}{-1}=2(x-1)(x-\frac{3}{2})=2x^2-5x+3\\
\ell_1(x)&=\frac{x-x_0}{x_1-x_0}\cdot\frac{x-x_2}{x_1-x_2}=\frac{x-\frac{1}{2}}{\frac{1}{2}}\cdot\frac{x-\frac{3}{2}}{-\frac{1}{2}}=-4(x-\frac{1}{2})(x-\frac{3}{2})=-4x^2+8x-3\\
\ell_2(x)&=\frac{x-x_0}{x_2-x_0}\cdot\frac{x-x_1}{x_2-x_1}=\frac{x-\frac{1}{2}}{1}\cdot\frac{x-1}{\frac{1}{2}}=2(x-\frac{1}{2})(x-1)=2x^2-3x+1\end{aligned}$$

And hence the polynomial reads
$$\begin{aligned}p(x)&=\frac{5}{2}(2x^2-5x+3)+2(-4x^2+8x-3)+\frac{15}{2}(2x^2-3x+1)\\
&=(5-8+15)x^2+(-\frac{25}{2}+16-\frac{45}{2})x+(\frac{15}{2}-6+\frac{15}{2})\\
&=12x^2-19x+9\end{aligned}$$

b)

1) Since $f(x)\approx p(x)$, we can integrate $p(x)$ to approximate the integral of $f$. We obtain with the antiderivatie of $p(x)$ as $P(x)=4x^3-\frac{19}{2}x^2+9x$ that
$$Q_1[f]=P(\frac{3}{2})-P(\frac{1}{2})=\Big(4\frac{27}{8}-\frac{19}{2}\cdot\frac{9}{4}+9\cdot\frac{3}{2}\Big)-\Big(4\frac{1}{8}-\frac{19}{2}\cdot\frac{1}{4}+9\cdot\frac{1}{2}\Big)=\frac{45}{8}-\frac{21}{8}=3.$$

2) The Simpson rule reads since $h=x_2-x_0=1$ and $x_1=\frac{1}{2}$ reads
$$Q_2[f]=\frac{1}{6}\Big(f(\frac{1}{2})+4f(1)+f(\frac{3}{2})\Big)=\frac{1}{6}\Big(\frac{5}{2}+8+\frac{15}{2}\Big)=\frac{18}{6}=3.$$

3) The composite trapezoidal rule yields
$$Q_3[f]=\frac{1}{4}\Big(f(\frac{1}{2})+2f(1)+f(\frac{3}{2})\Big)=\frac{1}{4}\Big(\frac{5}{2}+4+\frac{15}{2}\Big)=\frac{14}{4}=\frac{7}{2}.$$

4) The first two are identical, since Simpson can be derived from equispaced interpolation with Lagrange polynomials

c) The degree of precision of Simpson is 3 while composite trapezoidal only achieves a degree of precision of 1, so one would expect the Simpson rule to be more precise.

For completeness: Indeed the actual antiderivative reads
$$F(x)=\frac{4}{3}x^3+\frac{1}{2}x^2-5x+3\log(x)+\frac{\sin(\pi x)}{\pi}$$
and hence the integral yields
$$\int_{\frac{1}{2}}^{\frac{3}{2}}f(x)=F(\frac{3}{2})-F(\frac{1}{2})=\frac{1}{3}-\frac{2}{\pi}+3\log(3)\approx 2.99255.$$
so this is also actually the case.

**Grading manual**

a) (6p)

b) (2p) for each quadrature, (1p) for the final reason

c) (2p)

Kildesett: course=TMA4125 term=var year=2024 problem=1 points=15 file=math4n-2024v-en_lf.pdf
