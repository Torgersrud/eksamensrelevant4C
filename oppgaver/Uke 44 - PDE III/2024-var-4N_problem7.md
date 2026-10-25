### **Problem 7** **Finite Difference Scheme (10 points)**

Consider the Boundary value problem
$$3u-u''=\sin(x),\qquad 0\le x\le 1,$$
with mixed boundary conditions
$$u'(0)=1\qquad\text{and }u(1)=3.$$
We want to set up a finite difference scheme to find an approximate solution. Let $N\in\mathbb{N}$ be the number of grid points with distance $h=\frac{1}{N}$. The goal is then to approximate $u(x_i)$ at the points $x_i=ih$, $j=0,\dots,N$ by numbers $U_i\approx u(x_i)$.

Set up the finite difference scheme for this approximation of the form
$$AU=b,$$
where $U=(U_0,U_1,\cdots,U_N)^T$ and set up the matrix $A$ and the right hand side $b$.

When you need to approximate a first derivative, take central differences.

Kildesett: course=TMA4125 term=var year=2024 problem=7 points=10 file=math4n-2024v-en_lf.pdf
