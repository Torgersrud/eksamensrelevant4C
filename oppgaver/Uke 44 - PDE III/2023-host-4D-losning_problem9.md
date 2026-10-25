### **Solution to Problem 9** **Heat Equation [10 pts]**

First we look for solutions of the form $u(t,x)=G(t)F(x)$. We obtain two separate ODEs, $F''=-kF$ and $G'=-kG$.

The boundary conditions imply that we are looking for a solution with $F'(0)=F'(2)=0$. When $k=0$ we get a constant solution $F_0=C_0$ and $G_0=1$, and $u_0(t,x)=C_0$. When $k=w^2>0$ we obtain $F(x)=C_1\cos wx+C_2\sin wx$ and $F'(x)=-wC_1\sin wx+C_2w\cos wx$. The condition $F'(0)=F'(2)=0$ implies that $C_2=0$ and if $F\neq 0$ then $w=n\pi/2$ for some $n=1,2,...$. We have $w_n=n\pi/2$, $F_n=C\cos n\pi x/2$. For $k=-\kappa^2<0$ we have $F(x)=C_1e^{\kappa x}+C_2e^{-\kappa x}$, $F'(x)=C_1\kappa e^{\kappa x}-C_2\kappa e^{-\kappa x}$ and the condition $F'(0)=F'(2)=0$ implies that $F'=0$. We obtain only the trivial solution.

For the values $w_n=n\pi/2$, we solve the second equation $G'=-w_n^2G$ and get $G_n(t)=\exp(-w_n^2t)$. Then solutions of the form $u(t,x)=G(t)F(x)$ are given by

$$u_n(t,x)=\cos(n\pi x/2)\exp(-n^2\pi^2t/4).$$

The superposition principles implies that linear combinations of such solutions is also a solution

$$u(t,x)=c_0+\sum_nc_n\cos(n\pi x/2)\exp(-n^2\pi^2t/4).$$

Our initial condition $u(0,x)=1-\cos 3\pi x$ is satisfied if we choose $c_0=1$ and $c_6=-1$ while all other coefficients are zeros. We obtain the following solution

$$u(t,x)=1-\cos(3\pi x)\exp(-9\pi^2t).$$

**Grading manual** (10p).

Kildesett: course=TMA4135 term=host year=2023 problem=9 points=10 file=tma4130_2023h_exam.pdf
