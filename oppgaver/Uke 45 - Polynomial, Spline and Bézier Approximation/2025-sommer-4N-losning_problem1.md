### **Solution to Problem 1** **Interpolation (10 points)**

a) Originally, we would have to compute 3 Lagrange polynomials $\ell_j$, $j=0,1,2$. But since $y_1=y_2=0$, we will not need these two later on. These additional one is still provided here for completeness, but with the reasoning above it can also be skipped.

$$\ell_0(x)=\frac{x-x_1}{x_0-x_1}\cdot\frac{x-x_2}{x_0-x_2}=\frac{x-1}{0-1}\cdot\frac{x-2}{0-2}=\frac{1}{2}(x^2-3x+2)=\frac{1}{2}x^2-\frac{3}{2}x+1$$

$$\ell_1(x)=\frac{x-x_0}{x_1-x_0}\cdot\frac{x-x_2}{x_1-x_2}=\frac{x-0}{1-0}\cdot\frac{x-2}{1-2}=-x(x-2)=-x^2+2x$$

$$\ell_2(x)=\frac{x-x_0}{x_2-x_0}\cdot\frac{x-x_1}{x_2-x_1}=\frac{x-0}{2-0}\cdot\frac{x-1}{2-1}=\frac{1}{2}x(x-1)=\frac{1}{2}x^2-\frac{1}{2}x$$

Hence the interpolation polynomial is
$$p(x)=2\ell_0(x)+0\cdot\ell_1(x)+3\ell_2(x)=x^2-3x+2+\frac{3}{2}x^2-\frac{3}{2}x=\frac{5}{2}x^2-\frac{9}{2}x+2$$

b) Since the new node $(x_3,y_3)=(4,0)$ we do not have to compute it's Lagrange polynomial, but we have to add factors to the two existing ones.

We get
$$\ell_0(x)=\frac{x-x_1}{x_0-x_1}\cdot\frac{x-x_2}{x_0-x_2}\cdot\frac{x-x_3}{x_0-x_3}=\frac{1}{2}(x^2-3x+2)\cdot\frac{x-4}{-4}=-\frac{1}{8}(x^3-7x^2+14x-8)=-\frac{1}{8}x^3+\frac{7}{8}x^2-\frac{7}{4}x+1$$

$$\ell_2(x)=\frac{x-x_0}{x_2-x_0}\cdot\frac{x-x_1}{x_2-x_1}\cdot\frac{x-x_3}{x_2-x_3}=\frac{1}{2}x(x-1)\cdot\frac{x-4}{-2}=-\frac{1}{4}x^3+\frac{5}{4}x^2-x$$

Hence the new interpolation polynomial is
$$q(x)=2\ell_0(x)+0\cdot\ell_1(x)+3\ell_2(x)+0\cdot\ell_3(x)=-x^3+\frac{11}{2}x^2-\frac{13}{2}x+2$$

is not one of the original nodes, we have to update the interpolation polynomial.

c) We are lucky, since the new node $x_4,y_4=(\frac{1}{2},0)$ is a zero of the resulting polynomial $q$ already, the result stays the same.

While in principle the possible degree is 4, since this one is covered, it stays 3.

**Grading manual**

a) (4p)

b) (4p)

c) (2p)

Kildesett: course=TMA4125 term=sommer year=2025 problem=1 points=10 file=math4n-2025s-en-lf.pdf
