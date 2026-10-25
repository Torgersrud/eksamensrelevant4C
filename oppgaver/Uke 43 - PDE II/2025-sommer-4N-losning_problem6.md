### **Solution to Problem 6** **Solving a PDE with Separation of Variables (14 points)**

a) The PDE is a second order linear homogeneous PDE, namely the heat equation with $c=2$.

b) We insert the equation $u(x,t)=F(x)G(t)$ into the PDE and obtain the equation
$$F(x)G'(t)=4F''(x)G(t).$$
Dividing by $4G(t)$ and $F(x)$ yields the equation
$$\frac{G'(t)}{4G(t)}=\frac{F''(x)}{F(x)}=k,$$
where $k$ is some constant. From this we obtain the two ODEs
$$\begin{cases}F''(x)=kF(x)\\ G'(t)=4kG(t)\end{cases}$$
We consider now the possible solutions of the equation for $F$. We have three possibilities:

$k>0$: Denote $p=\sqrt{k}>0$. Then we have the solution
$$F(x)=Ae^{px}+Be^{-px}.$$
From the boundary conditions $F(0)=F(2)=0$ we get
$$F(0)=Ae^{0}+Be^{0}=A+B=0\qquad\text{and } F(2)=Ae^{-2p}+Be^{2p}=0$$
The first is equivalent to $A=-B$, plugging this into the second yields $B(e^{2p}-e^{-2p})=0$ which implies $B=0$ and hence $A=0$. So this only yields the trivial solution $F\equiv 0$, which we are not interested in.

$k=0$: Here we have the ODE $F''=0$, which has the general solution
$$F(x)=A+Bx.$$
Now we get from the boundary conditions that
$$F(0)=A=0,\qquad F(2)=A+2B=2B=0,$$
where we directly again only obtain the trivial solution.

$k<0$: Denote $p=\sqrt{-k}>0$. Then we have the solution
$$F(x)=A\cos(px)+B\sin(px).$$
Now the boundary conditions become
$$F(0)=A\cos(0)+B\sin(0)=A=0,\qquad F(2)=A\cos(2p)+B\sin(2p)=B\sin(2p)=0.$$
Since $B=0$ would only yield the trivial solution (yet again), we assume $B\ne 0$ and obtain that $\sin(2p)=0$, which is the case if $p=\frac{\pi n}{2}$ with $n=1,2,3,\dots$

This yields the family of solutions
$$F(x)=\sin\Bigl(\frac{\pi n}{2}x\Bigr)\qquad\text{for } n=1,2,3,\dots$$
Here $p_n=\frac{\pi n}{2}$ we have $k=-\bigl(\frac{\pi n}{2}\bigr)^2$ and hence in the second PDE
$$G'(t)=4kG(t)=-4\Bigl(\frac{\pi n}{2}\Bigr)^2G(t)=-\pi^2n^2G(t).$$
Which has the solution
$$G(t)=e^{4kt}=e^{-\pi^2n^2t}.$$
so that for each $p_n$ we have a $\lambda_n=\pi^2n^2$.

This yields the family of solutions stated in the task.

c) At $t=0$ we have $u_n(x,0)=A_n\sin\bigl(\frac{\pi n}{2}x\bigr)$.

Since the PDE is linear and homogeneous, we can use the principle of superposition to obtain the general solution
$$u(x,t)=\sum_{n=1}^{\infty}u_n(x,t)$$
and at $t=0$ we can "read off" the coefficients by comparison.

For $n=7$ we obtain the first term and can read off $A_7=3$, for $n=10$ we obtain the second term and can read off $A_{10}=4$.

Hence the solution reads
$$u(x,t)=3e^{-49\pi^2t}\sin\bigl(\frac{7}{2}\pi x\bigr)+4e^{-100\pi^2t}\sin(5\pi x).$$

**Grading manual**

a) (2p)

b) (9p)

c) (3p)

Kildesett: course=TMA4125 term=sommer year=2025 problem=6 points=14 file=math4n-2025s-en-lf.pdf
