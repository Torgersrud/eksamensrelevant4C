### **Solution to Problem 4**

(Problem 3 for Math 4M)

**a)** Assuming $u$ to be of the form $u(x,t)=F(x)G(t)$, we get

$$u_{t}=F\dot{G},\qquad u_{xx}=F^{\prime\prime}G.$$

Substituting into the given PDE, we have $F\dot{G}=(F^{\prime\prime}-5F)G$. Since we seek non-trivial solutions, $FG$ cannot be identically zero. Therefore, we divide the last equation by $FG$ to get

$$\frac{\dot{G}}{G}(t)+5=\frac{F^{\prime\prime}(x)}{F(x)}\ \ \forall t>0\ \text{and}\ x\in(0,\pi).$$

This can only be possible if both sides of the above equation are constant. This gives us the following ODEs for $F$ and $G$:

$$\dot{G}+(5-k)G=0,\qquad(3)$$

$$F^{\prime\prime}-kF=0,\qquad(4)$$

where $k$ is a yet-undetermined constant.

As $u\neq 0$, the boundary conditions imply that

$$F^{\prime}(0)=0=F^{\prime}(\pi).$$

The equation (4) has three different types of solutions depending on the sign of $k$

**Case 1.** *When $k>0$.*

In this situation, $F(x)=C_{1}e^{\sqrt{k}x}+C_{2}e^{-\sqrt{k}x}$. If $F$ has to satisfy the boundary conditions at $x=0,\pi$, then a routine argument shows that $C_{1}=C_{2}=0$. Thus, the case $k>0$ does not yield any non-trivial solutions.

**Case 2.** *When $k=0$.*

In this situation, $F(x)=C_{1}x+C_{2}$, whence $F^{\prime}(x)=C_{1}$. The boundary conditions imply that $C_{1}=0$, *but the constant $C_{2}$ can be non-zero*. Thus, we now need to consider the equation that determines $G$. As $k=0$, (3) implies that $G(t)=Ae^{-5t}$, where $A$ is some constant. Thus

$$u_{0}(x,t)=A_{0}e^{-5t}\qquad(5)$$

is a solution of the PDE $(\ast)$ of the product form satisfying the boundary conditions, where $A_{0}$ is an undetermined constant.

**Case 3.** *When $k<0$.*

In this situation, it is notationally simpler to write $k=-p^{2}$. Then, $F(x)=C_{1}\cos(px)+C_{2}\sin(px)$. The boundary conditions give us the equations

$$pC_{2}=0,\quad-pC_{1}\sin(p\pi)+pC_{2}\cos(p\pi)=0.$$

In the present case, $p\neq 0$. Hence, $C_{2}=0$, and we are faced with the condition $\sin(p\pi)=0$. This implies

$$p\pi=n\pi,\ \ n=0,\pm 1,\pm 2,\ldots$$

As $p\neq 0$, and as $\cos(-px)=\cos(px)$, it suffices to only consider $p=1,2,3,\ldots$ Corresponding to each of these values of $p$, $k=-n^{2}$, and solving (3) yields $G(t)=Ae^{-(n^{2}+5)t}$. Thus, corresponding to each $n$, we have the solution

$$u_{n}(x,t)=A_{n}\cos(nx)e^{-(5+n^{2})t},\quad n=1,2,3,\ldots,\qquad(6)$$

where $A_{n}$ is an undetermined constant.

All possible solutions of $(\ast)$ of the product form that satisfy the given boundary conditions are given by (5) and (6).

**b)** For the given problem, we can use superposition to look for a solution of the form

$$u(x,t)=A_{0}e^{-5t}+\sum_{n=1}^{\infty}A_{n}\cos(nx)e^{-(5+n^{2})t}.$$

Imposing the initial condition gives us

$$A_{0}+\sum_{n=1}^{\infty}A_{n}\cos(nx)=\cos^{2}\left(\frac{x}{2}\right)-2\cos(5x).\qquad(7)$$

We use a half-range expansion, with period $2\pi$, for the function on the right-hand side, and the above equation suggests a Fourier cosine series. But, rather than setting up the integrals to determine the Fourier coefficients, we recall the trigonometric identity:

$$\cos^{2}\left(\frac{x}{2}\right)=\frac{1+\cos(x)}{2}.$$

By (7) and orthogonality, $A_{n}=0$ for all $n$ except $n=0$, $1$ and $5$. In the latter case: $A_{0}=1/2$, $A_{1}=1/2$ and $A_{5}=-2$. Hence

$$u(x,t)=\frac{e^{-5t}}{2}+\frac{e^{-6t}\cos(x)}{2}-2\cos(5x)e^{-30t}$$

is the desired solution.

*Kjeldevarsel: Eksamen-PDF-en for dette haustsettet blei aldri publisert, og løysingsfila gjentek ikkje oppgåveteksten — PDE-en $(\ast)$ $u_t=u_{xx}-5u$ på $(0,\pi)$ med randvilkår $u_x(0,t)=u_x(\pi,t)=0$ og initialvilkåret i b) følgjer berre implisitt av utrekninga.*

Kildesett: course=TMA4130 term=host year=2012 problem=4 file=solutions_2012h.pdf
