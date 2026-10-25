### **Solution to Problem 8** (Solving a PDE with Separation of Variables, 14 points)

a) The PDE is a second order linear homogeneous PDE, namely the wave equation with $c=2$. (2 P.)

b) We insert the equation $u(x,t)=F(x)G(t)$ into the PDE and obtain the equation (1 P.)

$$F(x)G''(t)=4F''(x)G(t).$$

Dividing by $4G(t)$ and $F(x)$ yields the equation (1 P.)

$$\frac{G''(t)}{4G(t)}=\frac{F''(x)}{F(x)}=k,$$

where $k$ is some constant. From this we obtain the two ODEs (1 P.)

$$\begin{cases}F''(x)&=kF(x)\\ G''(t)&=4kG(t)\end{cases}$$

We consider now the possible solutions of the equation for $F$. We have three possibilities:

$k>0$: Denote $p=\sqrt{k}>0$. Then we have the solution

$$F(x)=Ae^{px}+Be^{-px}.$$

From the boundary conditions $F(1)=F(-1)=0$ we get

$$F(1)=Ae^{p}+Be^{-p}=0\qquad\text{and}\ F(-1)=Ae^{-p}+Be^{p}=0$$

This is equivalent to $A=-Be^{-2p}$, plugging this into the second yields $B=0$ and hence with the first $A=0$. So this only yields the trivial solution $F\sim 0$, which we are not interested in. (1 P.)

$k=0$: Here we have the ODE $F''=0$, which has the general solution

$$F(x)=A+Bx.$$

Now we get from the boundary conditions that

$$F(-1)=A-B=0,\qquad F(1)=A+B=0.$$

Adding both yields $2A=0$ and hence $A=0$; subtracting both yields $2B=0$ and hence $B=0$.

We again only obtain the trivial solution. (1 P.)

$k<0$: Denote $p=\sqrt{-k}>0$. Then we have the solution

$$F(x)=A\cos(px)+B\sin(px).$$

Now the boundary conditions become (1 P.)

$$F(-1)=A\cos(-p)+B\sin(-p)=0,\qquad F(1)=A\cos(p)+B\sin(p)=0.$$

Because the cosine is an even function and the sine is an odd function, we can rewrite this as

$$A\cos(p)-B\sin(p)=0,\qquad A\cos(p)+B\sin(p)=0.$$

If we subtract the second equation from the first, we get that $B\sin(p)=0$, which holds if either $B=0$ or $\sin(p)=0$, the latter implying that $p=\pi n$ with $n=1,2,3,\ldots$.

If we now add the two equations, we get that $A\cos(p)=0$. Thus, either $A=0$ or $\cos(p)=0$. Moreover, $\cos(p)=0$ if and only if $p=\frac{\pi(2m-1)}{2}$ with $m=1,2,3,\ldots$, since these yield arguments $\frac{r}{2}\pi$ with $r$ odd.

We thus have two different types of solutions:

- On one hand, we have the solutions

$$F(x)=\sin(\pi nx)\qquad\text{for}\ n=1,2,3,\ldots$$

For $p_n=\pi n$ we have $k=-\pi^{2}n^{2}$ and hence in the second PDE

$$G''(t)=4kG(t)=-4\pi^{2}n^{2}G(t)=-(2\pi n)^{2}G(t)$$

so that for each $p_n$ we have a $\lambda_n=2\pi n$. (1 P.)

- On the other hand, we have the solutions

$$F(x)=\cos\left(\frac{(2m-1)\pi}{2}x\right)\qquad\text{for}\ m=1,2,\ldots$$

For $p_m=\frac{\pi(2m-1)}{2}$ we have $k=-\left(\frac{\pi(2m-1)}{2}\right)^{2}$ and hence in the second PDE

$$G''(t)=4kG(t)=-4\left(\frac{\pi(2m-1)}{2}\right)^{2}G(t)=-(\pi(2m-1))^{2}G(t)$$

so that for each $p_m$ we have a $\mu_m=(2m-1)\pi$. (1 P.)

Each of these cases yields one of the solution families stated in the task.

c) At $t=0$ we have $u_n(x,0)=A_n\sin(\pi nx)$ and $v_m(x,0)=C_m\cos(\frac{\pi(2m-1)}{2}x)$.

Since the initial conditions are given in sine-terms, the second family of solutions does not contribute to the solution, all $C_m$ are zero and also all $D_m$. (1 P.)

Comparing coefficients for the first, we get $A_4=1$ and $A_7=3$. (1 P.)

Since the derivative is zero, all $B_n=0$. (1 P.)

Hence the solution reads (1 P.)

$$u(x,t)=1\cdot\cos(8\pi t)\sin(4\pi x)+3\cdot\cos(14\pi t)\sin(7\pi x).$$

Kildesett: course=TMA4432 term=test year=2026 problem=8 points=14 file=test-exam-math4c_web.pdf
