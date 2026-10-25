### **Problem 10**

Let $\mathcal{R}$ be the region defined by the lines

$$L_1:\,y=4-x\qquad L_2:\,y=0\qquad L_3:\,x=0\,.$$

Let $u(x,y)$ be the function defined in $\mathcal{R}$ that satisfies the Poisson equation

$$\frac{\partial^2u}{\partial x^2}+\frac{\partial^2u}{\partial y^2}=2xy$$

and boundary conditions

$$\begin{array}{ll}
u(x,y)=4&\text{if }(x,y)\in L_1\\
u(x,y)=x&\text{if }(x,y)\in L_2\\
u(x,y)=y&\text{if }(x,y)\in L_3
\end{array}$$

[Figure: $x$- and $y$-axes with the origin at the lower left; the shaded triangular region $\mathcal{R}$ with vertices $(0,0)$, $(4,0)$ and $(0,4)$; grid points with spacing $h=1$ on the boundary and inside the triangle, the three interior points $(1,1)$, $(2,1)$ and $(1,2)$ drawn as larger dots; boundary labels $u=y$ along the left edge, $u=x$ along the bottom edge and $u=4$ (rotated) along the line $y=4-x$; the $x$-axis marked $4$ at the corner with $L_1$.]

Let us define the points $(x_i,y_j)=(i\cdot h,j\cdot h)$ with $h=1$. Use the method of difference equations with $h=1$ in order to set up a linear system for finding approximations of the values $u(1,1)$, $u(1,2)$ and $u(2,1)$.

Kildesett: course=TMA4130 term=host year=2016 problem=10 file=n16h.pdf
