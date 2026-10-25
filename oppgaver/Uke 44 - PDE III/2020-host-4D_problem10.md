### **Problem 10** [12 points]

We consider the time-dependent PDE

$$u_t=u_{xx}+xu_x$$

with initial conditions

$$u(x,0)=x^2\qquad\text{for }0<x<1$$

and boundary conditions

$$u(0,t)=t\quad\text{and }u(1,t)=1\qquad\text{for }t>0.$$

**a)** Perform a semi-discretisation of the PDE using central differences for the approximations of the $x$-derivatives. Use equidistant grid points $x_i=i\Delta x$ with a grid size $\Delta x=1/M$.

**b)** We now want to use the trapezoidal rule for ODEs in order to compute a numerical solution of the system obtained in part **a)**. Set up the linear system that has to be solved in each step for an arbitrary time step $\Delta t>0$.

Set up specifically the system for $M=2$ and $\Delta t=1/2$, and compute a numerical approximation of $u(1/2,1)$.

Kildesett: course=TMA4135 term=host year=2020 problem=10 points=12 file=completeexam_nosolutions.pdf
