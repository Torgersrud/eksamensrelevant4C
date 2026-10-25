### **Solution to Problem 5** **Separation of Variables (14 points)**

We insert the equation $u(x,t)=F(x)G(t)$ into the PDE and obtain the equation
$$F(x)\dot G(t)=2F''(x)G(t).$$
Dividing by $2G(t)$ and $F(x)$ yields the equation
$$\frac{\dot G(t)}{2G(t)}=\frac{F''(x)}{F(x)}=k,$$
where $k$ is some constant. From this we obtain the two ODEs
$$\begin{cases}F''&=kF\\ \dot G&=2kG\end{cases}$$
We consider now the possible solutions of the equation for $F$. Thus we have three possibilities:

$k>0$: Denote $p=\sqrt{k}>0$. Then we have the solution
$$F(x)=Ae^{px}+Be^{-px}.$$
From the boundary conditions $F(\frac{\pi}{2})=F(-\frac{\pi}{2})=0$ we get
$$F(\frac{\pi}{2})=Ae^{p\frac{\pi}{2}}+Be^{-p\frac{\pi}{2}}=0\qquad\text{and }F(-\frac{\pi}{2})=Ae^{-p\frac{\pi}{2}}+Be^{p\frac{\pi}{2}}=0$$
Which is equivalent to $A=-Be^{-p\pi}$, plugging this into the second yields $B=0$ and hence with the first $A=0$. So this only yields the trivial solution, $F\sim 0$ we are not interested in.

$k=0$: Here we have the ODE $F''=0$, which has the general solution
$$F(x)=A+Bx.$$
Now we get from the boundary conditions that
$$\begin{aligned}F(-\frac{\pi}{2})=A-B\frac{\pi}{2}=0,\\ F(\frac{\pi}{2})=A+B\frac{\pi}{2}=0.\end{aligned}$$
Adding both yields $2A=0$ and hence $A=0$ subtracting both yields $\pi B=0$ and hence $B=0$.
We again only obtain the trivial solution.

$k<0$: Denote $p=\sqrt{-k}>0$. Then we have the solution
$$F(x)=A\cos(px)+B\sin(px).$$
Now the boundary conditions become
$$\begin{aligned}F(-\frac{\pi}{2})=A\cos(-p\frac{\pi}{2})+B\sin(-\frac{\pi}{2}p)=0,\\ F(\frac{\pi}{2})=A\cos(p\frac{\pi}{2})+B\sin(p\frac{\pi}{2})=0.\end{aligned}$$
Because the cosine is an even function and the sine is an odd function, we can rewrite this as
$$\begin{aligned}A\cos(p\frac{\pi}{2})-B\sin(p\frac{\pi}{2})=0,\\ A\cos(p\frac{\pi}{2})+B\sin(p\frac{\pi}{2})=0.\end{aligned}$$
If we now add the two equations, we get that $A\cos(p\frac{\pi}{2})=0$. Thus either $A=0$ or $\cos(p\frac{\pi}{2})=0$. Moreover, $\cos(p\frac{\pi}{2})=0$ if and only if $p=2(n+1/2)$ with $n=1,2,3,\dots$

If we subtract the second equation from the first, we get that $B\sin(p)=0$, which holds if either $B=0$ or $\sin(p\frac{\pi}{2})=0$, the latter implying that $p=2n$ with $n=1,2,3,\dots$

We thus have two different types of solutions:

- On the one hand, we have the solutions
$$F(x)=\cos\bigl(2(n+1/2)x\bigr)\qquad\text{for }n=1,2,\dots$$
Here $p=2(n+1/2)$ and $k=-p^2=-4(n+1/2)^2$, and thus the corresponding solution for $G$ is
$$G(t)=Ce^{-2kt}=Ce^{-8(n+1/2)^2t}.$$
- On the other hand, we have the solutions
$$F(x)=\sin(2nx)\qquad\text{for }n=1,2,\dots$$
Here $p=2n$ and $k=-p^2=-4n^2$, and thus the corresponding solution for $G$ is
$$G(t)=Ce^{2kt}=Ce^{-8n^2t}.$$

In total, we have the non-trivial solutions
$$u(x,t)=Ae^{-8(n+1/2)^2t}\cos\bigl(2(n+1/2)x\bigr)\quad\text{for }n=1,2,\dots$$
and
$$u(x,t)=Ae^{-8n^2t}\sin(2nx).\qquad\text{for }n=1,2,\dots$$

In order to obtain a unique solution we would need *initial conditions* $u(x,0)=f(x),x\in[-\frac{\pi}{2},\frac{\pi}{2}]$.

**Grading manual** (1p) for inserting the ansatz, (1p) for dividing to separate variables, (1p) for the two ODEs, (2p) for excluding $k>0$, (2p) for excluding $k=0$, (2p) for the boundary conditions for $k<0$, (1p) for the cosine family, (1p) for the sine family, (1p) for the non-trivial solutions in total, (2p) for the initial conditions.

Kildesett: course=TMA4125 term=var year=2023 problem=5 points=14 file=tma4125-matematikk-4n-2023v_lf.pdf
