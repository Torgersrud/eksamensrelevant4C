### **Solution to Problem 5** **Interpolation [10 pts]**

The interpolating polynomial $p$ is of degree not larger than three. To show that $p$ is odd, we consider the polynomial $q(x)=-p(-x)$. It interpolates the same values as $p$, $q(-2)=-p(2)=0$, $q(-1)=-p(1)=1$, $q(1)=-p(-1)=-1$, and $q(-2)=-p(2)=0$. On the other hand we know there there is only one polynomial of degree not larger than three that is interpolating for the values at four distinct points. Both $p(x)$ and $q(x)$ are such interpolating polynomials. Thus $p(x)=q(x)=-p(-x)$ and $p$ is odd.

We use the Lagrange interpolating formula to compute $p(x)$. The cardinal functions are

$$l_1=\frac{(x+1)(x-1)(x-2)}{(-2+1)(-2-1)(-2-2)}=-\frac{1}{7}(x+1)(x-1)(x-2),$$

$$l_2=\frac{(x+2)(x-1)(x-2)}{(-1+2)(-1-1)(-1-2)}=\frac{1}{6}(x+2)(x-1)(x-2),$$

$$l_3=\frac{(x+2)(x+1)(x-2)}{(1+2)(1+1)(1-2)}=-\frac{1}{6}(x+2)(x+1)(x-2),$$

$$l_4=\frac{(x+2)(x+1)(x-1)}{(2+2)(2+1)(2-1)}=\frac{1}{7}(x+2)(x+1)(x-1).$$

Then

$$\begin{aligned}p(x)=l_2-l_3=\frac{1}{6}\left(\left((x+2)(x-1)(x-2)-(x+2)(x+1)(x-2)\right.\right.\\
\left.\left.=\frac{1}{6}(x+2)(x-2)(x-1+x+1)=\frac{1}{3}(x+2)(x-2)x=\frac{x^3}{3}-\frac{4x}{3}.\right.\right.\end{aligned}$$

**Grading manual**

a) (5p)

b) (5p)

Kildesett: course=TMA4135 term=kont year=2023 problem=5 points=10 file=tma4130_2023h_exam-19.pdf
