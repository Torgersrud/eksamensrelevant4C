### **Solution to Problem 4**

We insert the equation $u(x, t) = F(x)G(t)$ into the PDE and obtain the equation

$$F(x) \dot{G}(t) = 4 F''(x) G(t).$$

Dividing by $4G(t)$ and $F(x)$ yields the equation

$$\frac{\dot{G}(t)}{4G(t)} = \frac{F''(x)}{F(x)} = k,$$

where $k$ is some constant. From this we obtain the two ODEs

$$\left. \begin{array}{l} F'' = kF \\ \dot{G} = 4kG \end{array} \right\}$$

We consider now the possible solutions of the equation for $F$. Thus we have three possibilities:

$k > 0$: Denote $p = \sqrt{k} > 0$. Then we have the solution

$$F(x) = A e^{px} + B e^{-px}.$$

From the boundary conditions we now get that

$$F(-1) = A e^{-p} + B e^{p} = 0,$$
$$F(1) = A e^{p} + B e^{-p} = 0.$$

From the first equation we get that $A = -B e^{2p}$. Inserting that in the second equation, we then obtain that

$$0 = -B e^{3p} + B e^{-p} = -B (e^{3p} - e^{-p}).$$

This is only possible for $B = 0$. From $A = -Be^{2p}$, we then get that $A$ needs to be 0 as well. Thus we only end up with the trivial solution.

$k = 0$: Here we have the ODE $F'' = 0$, which has the general solution

$$F(x) = A + Bx.$$

Now we get from the boundary conditions that

$$F(-1) = A - B = 0,$$
$$F(1) = A + B = 0.$$

By adding these equations, we get that $A = 0$; by subtracting the second equation from the first, we get that $B = 0$. Thus we obtain, again, only trivial solutions.

$k < 0$: Denote $p = \sqrt{-k} > 0$. Then we have the solution

$$F(x) = A \cos(px) + B \sin(px).$$

Now the boundary conditions become

$$F(-1) = A \cos(-p) + B \sin(-p) = 0,$$
$$F(1) = A \cos(p) + B \sin(p) = 0.$$

Because the cosine is an even function and the sine is an odd function, we can rewrite this as

$$A \cos(p) - B \sin(p) = 0,$$
$$A \cos(p) + B \sin(p) = 0.$$

If we now add the two equations, we get that $A \cos(p) = 0$. Thus either $A = 0$ or $\cos(p) = 0$. Moreover, $\cos(p) = 0$ if and only if $p = (n + 1/2)\pi$ with $n = 1, 2, 3, \ldots$

If we subtract the second equation from the first, we get that $B \sin(p) = 0$, which holds if either $B = 0$ or $\sin(p) = 0$, the latter implying that $p = n\pi$ with $n = 1, 2, 3, \ldots$

We thus have two different types of solutions:

- On the one hand, we have the solutions

$$F(x) = \cos\left( (n + 1/2)\pi x \right) \qquad \text{for } n = 1, 2, \ldots$$

Here $p = (n + 1/2)\pi$ and $k = -p^2 = -(n + 1/2)^2 \pi^2$, and thus the corresponding solution for $G$ is

$$G(t) = C e^{-4kt} = C e^{-4(n+1/2)^2 \pi^2 t}.$$

- On the other hand, we have the solutions

$$F(x) = \sin(n\pi x) \qquad \text{for } n = 1, 2, \ldots$$

Here $p = n\pi$ and $k = -p^2 = -n^2 \pi^2$, and thus the corresponding solution for $G$ is

$$G(t) = C e^{-4kt} = C e^{-4n^2 \pi^2 t}.$$

In total, we have the non-trivial solutions

$$u(x, t) = A e^{-4(n+1/2)^2 \pi^2 t} \cos\left( (n + 1/2)\pi x \right) \qquad \text{for } n = 1, 2, \ldots$$

and

$$u(x, t) = A e^{-4n^2 \pi^2 t} \sin\left( n\pi x \right). \qquad \text{for } n = 1, 2, \ldots$$

Kildesett: course=TMA4135 term=host year=2022 problem=4 file=math4nd-2022h_published.pdf
