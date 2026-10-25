### **Solution to Problem 6** **Separation of Variables (10 points)**

We insert the equation $u(x,t)=F(x)G(t)$ into the PDE and obtain the equation
$$F(x)\dot G(t)=3F''(x)G(t).$$
Dividing by $3G(t)$ and $F(x)$ yields the equation
$$\frac{\dot G(t)}{3G(t)}=\frac{F''(x)}{F(x)}=k,$$
where $k$ is some constant. From this we obtain the two ODEs
$$\begin{cases}F''&=kF\\ \dot G&=3kG\end{cases}$$
We consider now the possible solutions of the equation for $F$. Thus we have three possibilities:

$k>0$: Denote $p=\sqrt{k}>0$. Then we have the solution
$$F(x)=Ae^{px}+Be^{-px}.$$
From the boundary conditions $F(2\pi)=F(-2\pi)=0$ we get
$$F(\frac{\pi}{2})=Ae^{2p\pi}+Be^{-2p\pi}=0\qquad\text{and }F(-2\pi)=Ae^{-2p\pi}+Be^{2p\pi}=0$$
Which is equivalent to $A=-Be^{-4p\pi}$, plugging this into the second yields $B=0$ and hence with the first $A=0$. So this only yields the trivial solution, $F\sim 0$ we are not interested in.

$k=0$: Here we have the ODE $F''=0$, which has the general solution
$$F(x)=A+Bx.$$
Now we get from the boundary conditions that
$$\begin{aligned}F(-2\pi)=A-2B\pi=0,\\ F(2\pi)=A+2B\pi=0.\end{aligned}$$
Adding both yields $2A=0$ and hence $A=0$ subtracting both yields $\pi B=0$ and hence $B=0$.
We again only obtain the trivial solution.

$k<0$: Denote $p=\sqrt{-k}>0$. Then we have the solution
$$F(x)=A\cos(px)+B\sin(px).$$
Now the boundary conditions become
$$\begin{aligned}F(-2\pi)=A\cos(-2p\pi)+B\sin(-2p\pi)=0,\\ F(2\pi)=A\cos(2p\pi)+B\sin(2p\pi)=0.\end{aligned}$$
Because the cosine is an even function and the sine is an odd function, we can rewrite this as
$$\begin{aligned}A\cos(2p\pi)-B\sin(2p\pi)=0,\\ A\cos(2p\pi)+B\sin(2p\pi)=0.\end{aligned}$$
If we now add the two equations, we get that $A\cos(2p\pi)=0$. Thus either $A=0$ or $\cos(2p\pi)=0$. Moreover, $\cos(2p\pi)=0$ if and only if $p=\frac{2n+1}{4}$ with $n=0,1,2,3,\dots$, since these yield arguments $\frac{m}{2}\pi$ with $m$ odd.

If we subtract the second equation from the first, we get that $B\sin(p)=0$, which holds if either $B=0$ or $\sin(2p\pi)=0$, the latter implying that $p=\frac{n}{2}$ with $n=1,2,3,\dots$

We thus have two different types of solutions:

- On the one hand, we have the solutions
$$F(x)=\cos(\frac{2n+1}{4}x)\qquad\text{for }n=0,1,2,\dots$$
Here $p=\frac{2n+1}{4}$ and $k=-p^2=-\frac{(2n+1)^2}{16}$, and thus the corresponding solution for $G$ is
$$G(t)=Ce^{-3kt}=Ce^{-\frac{3}{16}(2n+1)^2t}.$$
- On the other hand, we have the solutions
$$F(x)=\sin(\frac{n}{2}x)\qquad\text{for }n=1,2,\dots$$
Here $p=\frac{n}{2}$ and $k=-p^2=-\frac{n^2}{4}$, and thus the corresponding solution for $G$ is
$$G(t)=Ce^{-3kt}=Ce^{-\frac{3n^2}{4}t}.$$

In total, we have the non-trivial solutions
$$u(x,t)=Ae^{-\frac{3}{16}(2n+1)^2t}\cos(\frac{2n+1}{4}x)\quad\text{for }n=0,1,2,\dots$$
and
$$u(x,t)=Ae^{-\frac{3n^2}{4}t}\sin(\frac{n}{2}x)\quad\text{for }n=1,2,\dots$$
and of course the (weighted) superposition of all of these function.

**Grading manual** (1p) for inserting the ansatz, (1p) for dividing to separate variables, (1p) for the two ODEs, (1p) for excluding $k>0$, (1p) for excluding $k=0$, (2p) for the boundary conditions for $k<0$, (1p) for the cosine family, (1p) for the sine family, (1p) for the non-trivial solutions in total.

Kildesett: course=TMA4125 term=var year=2024 problem=6 points=10 file=math4n-2024v-en_lf.pdf
