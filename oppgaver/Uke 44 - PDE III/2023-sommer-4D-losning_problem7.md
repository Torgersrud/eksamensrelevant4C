### **Solution to Problem 7**

We insert the equation $u(x, t) = F(x)G(t)$ into the PDE and obtain the equation

$$F(x) \dot{G}(t) = F''(x) G(t) + F(x) G(t).$$

Dividing by $G(t)$ and $F(x)$ yields the equation

$$\frac{\dot{G}(t)}{G(t)} = \frac{F''(x) + F(x)}{F(x)} = k,$$

where $k$ is some constant. From this we obtain the two ODEs

$$\left. \begin{array}{l} F'' = (k - 1) F \\ \dot{G} = kG \end{array} \right\}$$

We consider now the possible solutions of the equation for $F$. Thus we have three possibilities:

$k > 1$: Denote $p = \sqrt{k - 1} > 0$. Then we have the solution

$$F(x) = A e^{px} + B e^{-px}.$$

From the boundary condition $F(0) = 0$ we get the condition $A = -B$, which implies that $F(x) = A(e^{px} - e^{-px})$. From the boundary condition $F(\pi) = 0$, we now obtain that

$$A (e^{p\pi} - e^{-p\pi}) = 0,$$

which is only possible if $A = 0$, as $e^{p\pi} > 1$ and $e^{-p\pi} < 1$. Thus we only end up with the trivial solution.

$k = 1$: Here we have the ODE $F'' = 0$, which has the general solution

$$F(x) = A + Bx.$$

From the boundary condition $F(0) = 0$ we get that $A = 0$ and thus $F(x) = Bx$. Now the condition $F(\pi) = 0$ implies that also $B = 0$. Thus we obtain, again, only trivial solutions.

$k < 1$: Denote $p = \sqrt{1 - k} > 0$. Then we have the solution

$$F(x) = A \cos(px) + B \sin(px).$$

From the boundary condition $F(0) = 0$ we obtain that $A = 0$ and thus $F(x) = B \sin(px)$. Now the boundary condition $F(\pi) = 0$ implies that either $B = 0$ (which gives the trivial solution) or $\sin(p\pi) = 0$. The latter is satisfied if $p = n$ for some $n = 1, 2, \ldots$

We thus obtain the non-trivial solutions

$$F(x) = B \sin(nx) \qquad \text{for } n = 1, 2, \ldots$$

Since

$$k = 1 - p^2 = 1 - n^2,$$

the corresponding solution for $G$ is

$$G(t) = C e^{kt} = C e^{(1 - n^2)t}.$$

In total, we have the non-trivial solutions

$$u_n(x, t) = C e^{(1 - n^2)t} \sin(nx) \qquad \text{for } n = 1, 2, \ldots$$

Kildesett: course=TMA4135 term=sommer year=2023 problem=7 file=tma4125-30-35-matematikk4n-d-2023s_lf_correct.pdf
