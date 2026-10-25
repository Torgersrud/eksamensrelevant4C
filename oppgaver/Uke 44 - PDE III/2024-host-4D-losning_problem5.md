### **Solution to Problem 5** **Heat Equation [10 pts]**

a) We start by separation of variables setting $u(t,x)=F(x)G(t)$. Substituting this into the equation itself and dividing by $9F(x)G(t)$ gives

$$\frac{F''(x)}{F(x)}=\frac{G'(t)}{9G(t)}=k,$$

where the left hand side is independent of $t$ and the right-hand side is independent of $x$, so they have to equal the same constant $k$. In other words we get the equations

$$F''(x)-kF(x)=0,$$

and

$$G'(t)-9kG(t)=0.$$

b) For $u(t,x)$ to satisfy the boundary conditions (and not be $u(t,x)\equiv 0$), we need $F'(0)=F'(\pi)=0$. The general solution to the equation for $F$ depends on the sign of $k$ and we get

$$\begin{array}{ll}k=p^2>0&\text{gives }F(x)=Ae^{px}+Be^{-px},\\ k=0&\text{gives }F(x)=Ax+B,\\ k=-p^2<0&\text{gives }F(x)=A\sin(px)+B\cos(px).\end{array}$$

In the first case the boundary conditions are satisfied only for $A=B=0$ and in the second case they are satisfied for $A=0$ and for an arbitrary $B$. In the third case we can differentiate the expression to obtain $F'(x)=pA\cos(px)-pB\sin(px)$, so the conditions become

$$0=F'(0)=pA$$

which gives $A=0$ because $p^2\neq 0$ and (with $A=0$)

$$0=F'(\pi)=-pB\sin(p\pi),$$

which gives $B=0$ unless $p=n\in Z$, then it holds for an arbitrary $B$. So we get the nonzero solutions

$$F_n(x)=B_n\cos(nx),\qquad n\in Z.$$

c) The corresponding $G_n$ then solve $G'(t)+(3n)^2G(t)=0$, which has general solution

$$G_n(t)=Ce^{-(3n)^2t}=0,\qquad n\in Z.$$

d) Since we already have an arbitrary constant in $F_n$ we can set $C=1$ and we obtain the solutions

$$u_n(t,x)=F_n(x)G_n(t)=B_n\cos(nx)e^{-(3n)^2t},\qquad n\in Z.$$

Due to linearity and homogeneity, the linear combination of two solutions is still a solution, so to obtain a solution that satisfies the initial condition we can sum $u_1$ with $B_n=3$ and $u_3$ with $B_3=-1$. Thus the solution to the problem is

$$u(t,x)=3\cos(x)e^{-9t}-\cos(3x)e^{-81t}.$$

**Grading manual**

a) (3p)

b) (4p)

c) (1p)

d) (2p)

Kildesett: course=TMA4135 term=host year=2024 problem=5 points=10 file=exam_math_4n_4d_tma4130_35-8.pdf
