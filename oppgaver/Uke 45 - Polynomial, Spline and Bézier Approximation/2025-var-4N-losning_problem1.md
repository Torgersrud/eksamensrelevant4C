### **Solution to Problem 1** **Interpolation (10 points)**

a) Originally, we would have to compute 4 Lagrange polynomials $\ell_j$, $j=0,\dots,3$. But since $y_0=y_2=0$, we will not need these two later on. These two are still provided here for completeness, but with the reasoning above they can also be skipped.

$$\ell_0(x)=\frac{x-x_1}{x_0-x_1}\cdot\frac{x-x_2}{x_0-x_2}\cdot\frac{x-x_3}{x_0-x_3}=\frac{(x-1)(x-2)(x-3)}{(-1)(-2)(-3)}=-\frac{1}{6}(x^3-6x^2+11x-6)=-\frac{1}{6}x^3+x^2-\frac{11}{6}x+1$$

$$\ell_1(x)=\frac{x-x_0}{x_1-x_0}\cdot\frac{x-x_2}{x_1-x_2}\cdot\frac{x-x_3}{x_1-x_3}=\frac{x(x-2)(x-3)}{(1)(-1)(-2)}=\frac{1}{2}(x^3-5x^2+6x)=\frac{1}{2}x^3-\frac{5}{2}x^2+3x$$

$$\ell_2(x)=\frac{x-x_0}{x_2-x_0}\cdot\frac{x-x_1}{x_2-x_1}\cdot\frac{x-x_3}{x_2-x_3}=\frac{x(x-1)(x-3)}{(2)(1)(-1)}=-\frac{1}{2}(x^3-4x^2+3x)=-\frac{1}{2}x^3+2x^2-\frac{3}{2}x$$

$$\ell_3(x)=\frac{x-x_0}{x_3-x_0}\cdot\frac{x-x_1}{x_3-x_1}\cdot\frac{x-x_2}{x_3-x_2}=\frac{x(x-1)(x-2)}{(3)(2)(1)}=\frac{1}{6}(x^3-3x^2+2x)=\frac{1}{6}x^3-\frac{1}{2}x^2+\frac{1}{3}x$$

b) We have 4 interpolation points. The degree is one less than that, so $k=3$. This can also be argued by looking at the degree of the Lagrange polynomials.

c) We can either compute $p(x)=3\ell_0(x)-3\ell_2(x)=x^3-3x^2-x+3$ and read off $a_3=1$ or argue that the highest monomials are $-\frac{1}{6}x^3$ and $-\frac{1}{2}x^3$ in those polynomials and hence $a_3=-\frac{3}{6}-\frac{-3}{2}=-\frac{1}{2}+\frac{3}{2}=1$.

d) We have to "update" the (two) Lagrange polynomials $\ell_0$, $\ell_2$ with an additional factor $\frac{x-x_4}{x_j-x_4}$. We also have to compute $\ell_4$.

Alternatively one can take the polynomial $p(x)$ we computed and evaluate it at $x_4=4$, compute $\ell_4$ and add $(15-p(4))\ell_4(x)$ to $p(x)$.

**Grading manual**

a) (4p)

b) (2p)

c) (2p)

d) (2p)

Kildesett: course=TMA4125 term=var year=2025 problem=1 points=10 file=math4n-2025v-en-lf.pdf
