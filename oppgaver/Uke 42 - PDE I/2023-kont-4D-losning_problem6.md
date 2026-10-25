### **Solution to Problem 6** **Heat Equation [10 pts]**

a) For solutions of the form $u(x,y)=F(x)G(y)$ we get the following equation $F''(x)G(y)+F(x)G''(y)=0$. Separating the variables, we obtain $F''(x)=-kF(x)$ and $G''(y)=kG(y)$. To satisfy the boundary conditions $u_x(0,y)=u_x(1,y)=0$ we should have $F'(0)=F'(1)=0$.

When $k=0$ we get a constant solution $F_0(x)=C_0$ and $G_0(y)=ay+b$, and $u_0(x,y)=A_0y+B_0$.

When $k=w^2>0$ we obtain $F(x)=C_1\cos wx+C_2\sin wx$ and $F'(x)=-wC_1\sin wx+C_2w\cos wx$. The condition $F'(0)=F'(1)=0$ implies that $C_2=0$ and if $F\neq 0$ then $w=n\pi$ for some $n=1,2,...$. We have $w_n=n\pi$, $F_n=C_n\cos n\pi x$ and $G_n(y)=A_ne^{w_ny}+B_ne^{-w_ny}$. Then

$$u_n(x,y)=\cos n\pi x(A_ne^{w_ny}+B_ne^{-w_ny}),\;\; w_n=n\pi, n=1,2,....$$

For $k=-\kappa^2<0$ we have $F(x)=C_1e^{\kappa x}+C_2e^{-\kappa x}$, $F'(x)=C_1\kappa e^{\kappa x}-C_2\kappa e^{-\kappa x}$ and the condition $F'(0)=F'(1)=0$ implies that $F'=0$. We obtain only the trivial solution $F=0$.

b) To satisfy the two other boundary conditions we first look for solutions with separated variables which satisfy $G'(0)=1$. We have $G_0(y)=A_0y+B_0$ and $G_0'(0)=A_0$, thus we get the solution $G_0=B_0$ and $u_0(x,y)=C_0$ is a constant solution.

For $n=1,2,...$, $G_n(y)=A_ne^{w_ny}+B_ne^{-w_ny}$, $G'(y)=A_nw_ne^{w_ny}-B_nw_ne^{-w_ny}$. Then $G'(0)=0$ implies that $A_n=B_n$ and we can write $G_n=C_n\cosh w_ny$. The solutions are of the form

$$u_n(x,y)=C_n\cos n\pi x\cosh n\pi y.$$

Using superposition principle, we obtain solutions

$$u(x,y)=C_0+\sum_{n}C_n\cos n\pi x\cosh n\pi y.$$

Finally, to satisfy the condition $u_y(x,1)=\cos 5\pi x$ we compute

$$u_y(x,y)=\sum_{n}C_nn\pi\cos n\pi x\sinh n\pi y$$

and see that $u_y(x,1)=\sin 5\pi x$ when

$$C_5=\frac{1}{5\pi\sinh 5\pi}, C_n=0, n=1,2,3,4,6,...,$$

and $C_0$ is arbitrary. Then

$$u(x,y)=C_0+\frac{1}{5\pi\sinh 5\pi}\cos 5\pi x\cosh 5\pi y.$$

**Grading manual**

a) (5p)

b) (5p)

Kildesett: course=TMA4135 term=kont year=2023 problem=6 points=10 file=tma4130_2023h_exam-19.pdf
