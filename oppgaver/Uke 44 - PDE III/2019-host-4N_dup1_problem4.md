### **Problem 4** [20 points]

Consider the following heat equation

$$u_t(x,t)=\frac{1}{2}u_{xx}(x,t),\quad t\geq 0,\quad 0\leq x\leq\pi,$$

with boundary conditions

$$u(0,t)=u(\pi,t)=0,\quad t\geq 0;$$

and the initial condition

$$u(x,0)=x(\pi-x),\quad 0\leq x\leq\pi.$$

**a)** Find the Fourier sine series solution of the above heat equation by using the separation of variables method.

**b)** Let $M,N$ be two natural numbers, and define $h=\pi/M$ and $k=1/N$. Introduce $x_i=ih$ for $i=0,\ldots,M$ and $t_n=nk$ for $n=0,1,2,\ldots$. Write down an explicit difference scheme (based on finite differences and (forward) Euler's method) for $U_i^n\approx u(x_i,t_n)$.

**c)** Let $M=4$ and $N=20$, and compute the approximate solution for $u(\pi/4,0.1)$.

Kildesett: course=TMA4135 term=host year=2019 problem=4 points=20 file=unred.pdf
