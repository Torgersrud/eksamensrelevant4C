### **Solution to Problem 6** **Solving a PDE with Separation of Variables (14 points)**

a) The PDE is a second order linear homogeneous PDE, namely the wave equation with $c=2$.

b) We insert the equation $u(x,t)=F(x)G(t)$ into the PDE and obtain the equation
$$F(x)G''(t)=4F''(x)G(t).$$
Dividing by $4G(t)$ and $F(x)$ yields the equation
$$\frac{G''(t)}{4G(t)}=\frac{F''(x)}{F(x)}=k,$$
where $k$ is some constant. From this we obtain the two ODEs
$$\begin{cases}F''(x)&=kF(x)\\ G''(t)&=4kG(t)\end{cases}$$
We consider now the possible solutions of the equation for $F$. We have three possibilities:

$k>0$: Denote $p=\sqrt{k}>0$. Then we have the solution
$$F(x)=Ae^{px}+Be^{-px}.$$
From the boundary conditions $F(1)=F(-1)=0$ we get
$$F(1)=Ae^{p}+Be^{-p}=0\qquad\text{and } F(-1)=Ae^{-p}+Be^{p}=0$$
Which is equivalent to $A=-Be^{-2p}$, plugging this into the second yields $B=0$ and hence with the first $A=0$. So this only yields the trivial solution $F\sim 0$, which we are not interested in.

$k=0$: Here we have the ODE $F''=0$, which has the general solution
$$F(x)=A+Bx.$$
Now we get from the boundary conditions that
$$F(-1)=A-B=0,\qquad F(1)=A+B=0.$$
Adding both yields $2A=0$ and hence $A=0$ subtracting both yields $2B=0$ and hence $B=0$.
We again only obtain the trivial solution.

$k<0$: Denote $p=\sqrt{-k}>0$. Then we have the solution
$$F(x)=A\cos(px)+B\sin(px).$$
Now the boundary conditions become
$$F(-1)=A\cos(-p)+B\sin(-p)=0,\qquad F(1)=A\cos(p)+B\sin(p)=0.$$
Because the cosine is an even function and the sine is an odd function, we can rewrite this as
$$A\cos(p)-B\sin(p)=0,\qquad A\cos(p)+B\sin(p)=0.$$
If we subtract the second equation from the first, we get that $B\sin(p)=0$, which holds if either $B=0$ or $\sin(p)=0$, the latter implying that $p=\pi n$ with $n=1,2,3,\dots$.

If we now add the two equations, we get that $A\cos(p)=0$. Thus, either $A=0$ or $\cos(p)=0$. Moreover, $\cos(p)=0$ if and only if $p=\frac{\pi(2m-1)}{2}$ with $m=1,2,3,\dots$, since these yield arguments $\frac{r}{2}\pi$ with $r$ odd.

We thus have two different types of solutions:

- On one hand, we have the solutions
$$F(x)=\sin(\pi nx)\quad\text{for } n=1,2,3,\dots$$
Here $p_n=\pi n$ we have $k=-\pi^2n^2$ and hence in the second PDE
$$G''(t)=4kG(t)=-4\pi^2n^2G(t)=-(2\pi n)^2G(t)$$
so that for each $p_n$ we have a $\lambda_n=2\pi n$

- On the other hand, we have the solutions
$$F(x)=\cos\Bigl(\frac{(2m-1)\pi}{2}x\Bigr)\quad\text{for } m=0,1,2,\dots$$
Here $p_m=\pi\frac{(2m-1)}{2}$ we have $k=-\Bigl(\pi\frac{(2m-1)}{2}\Bigr)^2$ and hence in the second PDE
$$G''(t)=4kG(t)=-4\Bigl(\frac{\pi(2m-1)}{2}\Bigr)^2G(t)=-(\pi(2m-1))^2G(t)$$
so that for each $p_m$ we have a $\mu_m=(2m-1)\pi$.

Each of these cases yields one of the solution families stated in the task.

c) At $t=0$ we have $u_n(x,0)=A_n\sin(\pi nx)$ and $v_m(x,0)=C_m\cos\bigl(\frac{\pi(2m-1)}{2}x\bigr)$. Since the initial conditions are given in sine-terms, the second family of solutions does not contribute to the solution, all $C_m$ are zero and also all $D_m$. Comparing coefficients for the first, we get $A_4=1$ and $A_7=3$. Since the derivative is zero, all $B_n=0$. Hence the solution reads
$$u(x,t)=1\cdot\cos(8\pi t)\sin(4\pi x)+3\cdot\cos(14\pi t)\sin(7\pi x)$$

**Grading manual**

a) (2p)

b) (8p)

c) (4p)

Kildesett: course=TMA4125 term=var year=2025 problem=6 points=14 file=math4n-2025v-en-lf.pdf
