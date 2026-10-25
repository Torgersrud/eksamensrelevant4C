### **Løsning til Oppgave 6**

**a)** Inserting $F(x)G(t)$ into the PDE, we obtain

$$F\ddot G-2F\dot G+FG=F''G,$$

which we can write as

$$F(\ddot G-2\dot G+G)=F''G.$$

Dividing by $F$ and $G$ this becomes

$$\frac{\ddot G-2\dot G+G}{G}=\frac{F''}{F},$$

which necessarily has to be a constant, say $k\in\mathbb R$. Thus we obtain the two ODEs

$$F''=kF,$$

$$\ddot G-2\dot G+G=kG.$$

Moreover, the boundary conditions imply that

$$F'(0)=0\qquad\text{and}\qquad F'(\pi)=0.$$

We now have three possibilities:

- $k=p^2>0$ with $p>0$: Here

$$F(x)=Ae^{px}+Be^{-px}.$$

The condition $F'(0)=0$ gives

$$0=pA-pB$$

and thus

$$A=B.$$

Now the condition $F'(\pi)=0$ implies that

$$pAe^{p\pi}-pAe^{-p\pi}=0$$

or

$$pA(e^{p\pi}-e^{-p\pi})=0.$$

Since $e^{p\pi}>1$ and $e^{-p\pi}<1$, this implies that

$$A=0.$$

Thus we only have trivial solutions.

- $k=0$: Here

$$F(x)=A+Bx.$$

Now the condition $F'=0$ implies that

$$B=0.$$

However, the function $F(x)=A$ satisfies both boundary conditions, and thus we have found a non-trivial solution. Now we solve the equation for $G$, which, for $k=0$ gives

$$\ddot G-2\dot G+G=0.$$

The solutions of the equation are of the form

$$G(t)=Ce^t+Dte^t.$$

Thus we obtain the solutions

$$F(x)G(t)=Ce^t+Dte^t.$$

- $k=-p^2<0$: Here

$$F(x)=A\cos(px)+B\sin(px).$$

The condition $F'(0)=0$ implies that

$$0=F'(0)=-pA\sin(0)+Bp\cos(0)=Bp.$$

Thus $B=0$ and

$$F(x)=A\cos(px).$$

Now the condition $F'(\pi)=0$ implies that

$$-Ap\sin(p\pi)=0,$$

and thus we obtain the non-trivial solutions

$$F(x)=A\cos(px)\qquad\text{for }p=1,2,\ldots.$$

Now we compute the solution of the ODE for $G$, which, with $k=-p^2$ reads as

$$\ddot G-2\dot G+G=-p^2G.$$

This equation has the solutions

$$G(t)=e^t\bigl(C\cos(pt)+D\sin(pt)\bigr).$$

Thus we obtain the solutions (ignoring the unnecessary constant $A$)

$$F(x)G(t)=e^t\bigl(C\cos(pt)+D\sin(pt)\bigr)\cos(px).$$

All in all, we have found the solutions

$$F(x)G(t)=Ce^t+Dte^t$$

and

$$F(x)G(t)=e^t\bigl(C\cos(pt)+D\sin(pt)\bigr)\cos(px)\qquad\text{with }p=1,2,\ldots.$$

*Remark:* It is perfectly fine and viable to solve the ODE for $G$ using the Laplace transform: Denoting $Y=\mathcal L(G)$, the equation

$$\ddot G-2\dot G+(1+p^2)G=0$$

with $p>0$ transforms to

$$s^2Y-sG(0)-\dot G(0)-2sY+2G(0)+(1+p^2)Y=0,$$

which can be simplified as

$$(s^2-2s+(1+p^2))Y=sG(0)-2G(0)+\dot G(0)$$

or

$$((s-1)^2+p^2)Y=sG(0)-2G(0)+\dot G(0).$$

Thus

$$\begin{array}{rl}Y=&\displaystyle\frac{s}{(s-1)^2+p^2}G(0)+\frac{1}{(s-1)^2+p^2}\bigl(\dot G(0)-2G(0)\bigr)\\[10pt] =&\displaystyle\frac{s-1}{(s-1)^2+p^2}G(0)+\frac{1}{(s-1)^2+p^2}\bigl(\dot G(0)-G(0)\bigr).\end{array}$$

Applying the inverse Laplace transform, we obtain that

$$G(t)=e^t\cos(pt)G(0)+e^t\sin(pt)\,\frac{\dot G(0)-G(0)}{p}.$$

**b)** The general solution of the equation has the form

$$u(x,t)=C_0e^t+D_0te^t+\sum_{p=1}^{\infty}e^t\bigl(C_p\cos(pt)+D_p\sin(pt)\bigr)\cos(px).$$

The initial condition $u(x,0)=x^2$ thus implies that

$$x^2=C_0+\sum_{p=1}^{\infty}C_p\cos(px)\qquad\text{for }0<x<\pi.$$

Thus the coefficients $C_0$ and $C_p$ are the Fourier-cosine coefficients of the function $x^2$. From problem 2 we thus obtain that

$$C_0=\frac{\pi^2}{3},$$

$$C_p=(-1)^p\,\frac{4}{p^2},\qquad p=1,2,\ldots.$$

In order to use the second initial condition, we compute

$$\begin{array}{rl}\displaystyle\frac{\partial u}{\partial t}(x,t)=C_0e^t+D_0(te^t+e^t)+&\displaystyle\sum_{p=1}^{\infty}e^t\bigl(C_p\cos(pt)+D_p\sin(pt)\bigr)\cos(px)\\[10pt] &+\displaystyle\sum_{p=1}^{\infty}e^t\bigl(-pC_p\sin(pt)+pD_p\cos(pt)\bigr)\cos(px).\end{array}$$

Now the initial condition $\partial_t u(x,0)=0$ implies that

$$0=C_0+D_0+\sum_{p=1}^{\infty}(C_p+pD_p)\cos(px).$$

Thus

$$D_0=-C_0$$

and

$$D_p=-\frac{C_p}{p},\qquad p=1,2,\ldots.$$

Thus we see that

$$u(x,t)=\frac{\pi^2}{3}e^t-\frac{\pi^2}{3}te^t+4e^t\sum_{p=1}^{\infty}(-1)^p\cos(px)\Bigl(\frac{1}{p^2}\cos(pt)-\frac{1}{p^3}\sin(pt)\Bigr).$$

Kildesett: course=TMA4130 term=host year=2015 problem=6 file=bokmal.pdf
