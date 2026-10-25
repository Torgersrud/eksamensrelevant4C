### **Solution to Problem 7** **Discretize a PDE (10 points)**

a) We use (forwards) first order differences in time and second order finite differences in space
$$f'(t)=\frac{f(t+k)-f(t)}{k}\qquad\text{and}\qquad f''(x)\approx\frac{f(x-h)-2f(x)+f(x+h)}{h^2},$$
where $h$ is the distance between the grid points in $x$ direction.

We rewrite the given PDE with finite differences as
$$\frac{u(x_i,t_n+k)-u(x_i,t_n)}{k}+O(k)=4\frac{u(x_i-h,t_n)-2u(x_i,t_n)+u(x_i+h,t_n)}{h^2}+O(h^2)$$
Leaving out the error terms and approximating the $u(x_i,t_n)$ by $U_i^n$ and using that $t_n+k=t_{n+1}$ as well as $x_i\pm h=x_{i\pm1}$, we obtain
$$\frac{U_i^{n+1}-U_i^n}{k}=4\frac{U_{i-1}^n-2U_i^n+U_{i+1}^n}{h^2}.$$
Rearranging this yields the finite difference equation
$$U_i^{n+1}=U_i^n+4\frac{k}{h^2}\bigl(U_{i-1}^n-2U_i^n+U_{i+1}^n\bigr).$$

b) For the discretization error, we have to compare the derivative to its finite difference approximation.

Hence we have a $O(h^2)$ error term in space and a $O(k)$ error term in time.

c) For the case $M=4$ and $k=0.1$, we have
$$h=\frac{2}{M}=\frac{2}{4}=0.5.$$
and hence the initial values are
$$U_0^0=u(0,0)=0,\qquad U_1^0=u(0.5,0)=2.5,\qquad U_2^0=u(1,0)=5,$$
$$U_3^0=u(1.5,0)=2.5,\qquad U_4^0=u(2,0)=0.$$
We can now compute the next time step $n=1$. At the boundary we can use the boundary conditions
$$U_0^1=0,\qquad U_4^1=0$$
and for the remaining three points we compute
$$U_1^1=U_1^0+4\frac{k}{h^2}\bigl(U_0^0-2U_1^0+U_2^0\bigr)=2.5+4\cdot\frac{0.1}{(0.5)^2}\bigl(0-2\cdot 2.5+5\bigr)=2.5+4\cdot 0.4\cdot\bigl(0-5+5\bigr)=2.5.$$
$$U_2^1=U_2^0+4\frac{k}{h^2}\bigl(U_1^0-2U_2^0+U_3^0\bigr)=5+4\cdot\frac{0.1}{(0.5)^2}\bigl(2.5-10+2.5\bigr)=5+4\cdot 0.4\cdot(-5)=5-8=-3.$$
$$U_3^1=U_3^0+4\frac{k}{h^2}\bigl(U_2^0-2U_3^0+U_4^0\bigr)=2.5+4\cdot\frac{0.1}{(0.5)^2}\bigl(5-5+0\bigr)=2.5,$$
where one can also argue that $U_3^1=U_1^1$ due to symmetry of both the initial conditions and the finite differences in space.

d) For stability we have to consider the Courant-Friedrichs-Lewy (CFL) condition
$$\alpha=\frac{c^2k}{h^2}\le\frac{1}{2}.$$
Here we have $c^2=4$ and $h=\frac{2}{M}=\frac{2}{4}=0.5$ and $k=0.1$, hence
$$\alpha=\frac{4\cdot 0.1}{(0.5)^2}=\frac{0.4}{0.25}=1.6.$$
Since $\alpha>\frac{1}{2}$, the method is unstable for these parameters.

The largest time step size $k$ for which the method is stable is given by
$$\frac{4k}{(\frac{1}{2})^2}\le\frac{1}{2}\Leftrightarrow 4k\le\frac{\frac{1}{4}}{2}=\frac{1}{8}\Leftrightarrow k\le\frac{1}{8}\cdot\frac{1}{4}=\frac{1}{32}=0.03125.$$

e) for stability we can use an implicit Euler method or a Crank-Nicolson method.
For the discretization error we can either use a central difference or again a Crank-Nicolson method.

**Grading manual**

a) (3p)

b) (2p)

c) (2p)

d) (2p)

e) (1p)

Kildesett: course=TMA4125 term=sommer year=2025 problem=7 points=10 file=math4n-2025s-en-lf.pdf
