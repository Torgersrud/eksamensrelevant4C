### **Solution to Problem 5**

**a)** While it is perfectly OK to approach the problem directly using Newton's divided differences or a Lagrange scheme, we can save ourselves some work by noticing that the polynomial $q$ given by $q(x)=p(x)-1$ has zeros at $0$ and $1$. We thus have

$$p(x)-1=q(x)=x(x-1)r(x)$$

for some polynomial $r$. In particular, the unused interpolation data becomes

$$7=-2\cdot(-2-1)r(-2)+1=6r(-2)+1\implies r(-2)=1$$

$$3=-1\cdot(-1-1)r(-1)+1=2r(-1)+1\implies r(-1)=1$$

$$3=2\cdot(2-1)r(2)+1=2r(2)+1\implies r(2)=1.$$

It is clear, then, that $r(x)=1$. Thus,

$$p(x)=q(x)+1=x(x-1)\cdot 1+1=1-x+x^2.$$

**b)** Simpson's method is exact for polynomials of degree less than or equal to 3, and will thus give the exact value for the integral of $p$: With $n=4$ ($h=1$) we find

$$\int_{-2}^{2}p(x)\,\mathrm{d}x=\frac{1}{3}(7+4\cdot 3+2\cdot 1+4\cdot 1+3)=\frac{28}{3}.$$

Kildesett: course=TMA4130 term=host year=2013 problem=5 file=eksamen-bok_2013h.pdf
