### **Problem 7** **Discretize a PDE (10 points)**

We want to (continue to) observe how the temperature $u$ of a heated wire evolves over time. This can be modelled by the following PDE
$$\frac{\partial u}{\partial t}=4\frac{\partial^2 u}{\partial x^2},\qquad\text{where}\quad 0<x<2\qquad\text{and}\quad t>0,$$
be given with boundary conditions
$$u(0,t)=u(2,t)=0\quad\text{where}\quad t\ge 0.$$
Where we take a more realistic initial temperature of
$$u(x,0)=\begin{cases}5x&\text{for }0<x\le 1,\\ 5(2-x)&\text{for }1<x\le 2.\end{cases}$$
We consider grid points $(x_i,t_n)$ with $i=0,\dots,M$, and $n=0,1,2,\dots$, where the $M+1$ points in $x$ direction are equidistantly distributed and we set a time step size of $k>0$.

a) Use first order forward finite differences and second order finite differences to discretize the PDE $(x_i,t_n)$ on the grid points $(x_i,t_n)$ by values $U_i^n\approx u(x_i,t_n)$. State the resulting finite difference equation.

b) What can we say about the discretization errors?

c) Consider the case with 5 points in space, i. e. $M=4$, and a time step of $k=0.1$. Use the initial conditions to perform one step of the explicit Euler method.

d) Is the method performed in Item c) stable?
What is the largest time step size $k$ for which the method is stable?

e) How can we improve both the stability and the discretization error?

Kildesett: course=TMA4125 term=sommer year=2025 problem=7 points=10 file=math4n-2025s-en-lf.pdf
