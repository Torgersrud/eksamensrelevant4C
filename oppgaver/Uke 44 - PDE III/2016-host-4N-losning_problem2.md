### **Solution to Problem 2**

If $u(x,t)=F(x)G(t)$ we have that

$$u_{xx}=F''G\qquad\text{and}\qquad u_t=FG'\,.$$

Then if we replace this into the heat equation we have that $FG'=2F''G$, so it follows that

$$\frac{F''}{F}=\frac{G'}{2G}=K\qquad\text{where }K\in\mathbb{R}\,.$$

From this we deduce the two following ODEs

$$F''-KF=0\qquad\text{and}\qquad G'-2KG=0\,.$$

Additionally, observe that from the boundary conditions it follows that

$$u(0,t)=F(0)G(t)=0\qquad\text{implies}\qquad F(0)=0\,,$$
$$u_x(2\pi,t)=F'(2\pi)G(t)=0\qquad\text{implies}\qquad F'(2\pi)=0\,.$$

First we solve the ODE $F''-KF=0$.

Suppose that $\underline{K=0}$, then $F''=0$, from where we have that $F(x)=Ax+B$. But

$$0=F(0)=A\cdot0+B=B\qquad\text{and}\qquad 0=F'(2\pi)=A\,,$$

thus $F=0$. This gives us a trivial solution.

Now suppose that $\underline{K>0}$. Then the solution of $F''-KF=0$ is of the form $F(x)=A\cosh(\sqrt{K}x)+B\sinh(\sqrt{K}x)$. But

$$0=F(0)=A\cosh(0)+B\sinh(0)=A\qquad\text{and}\qquad 0=F'(2\pi)=B\sqrt{K}\cosh(0)=B\sqrt{K}=0\,,$$

thus $F=0$. This gives us also a trivial solution.

Finally suppose that $\underline{K<0}$. We write $K=-p^2$ where $p>0$. Then the ODE $F''+p^2F=0$ has solution $F(x)=A\cos(px)+B\sin(px)$. But

$$0=F(0)=A\cos 0+B\sin 0=A\qquad\text{and}\qquad 0=F'(2\pi)=Bp\cos(p2\pi)\,.$$

But this means that $p2\pi=\frac{2n+1}{2}\pi$ for $n\in\mathbb{Z}$, from where it follows that

$$p=\frac{2n+1}{4}\qquad\text{with }n\in\mathbb{Z}\,.$$

Then we define the functions

$$F_n(x)=\sin\left(\frac{2n+1}{4}x\right)\qquad\text{for }n\in\mathbb{Z}\,.$$

Observe that since $\sin$ is an odd function for every $n\in\mathbb{N}$ we have that

$$F_{-n}(x)=\sin\left(\frac{-2n+1}{4}x\right)=-\sin\left(\frac{2n-1}{4}x\right)=-F_{n-1}(x)\,.$$

So the negative $n$'s do not give us any new solutions. Then it is enough to use the functions

$$F_n(x)=\sin\left(\frac{2n+1}{4}x\right)\qquad\text{for }n=0,1,2,\ldots$$

Now we are going to solve the ODE $G'-2KG=0$, but since $K=-p^2=-\big(\frac{2n+1}{4}\big)^2$ for $n=0,1,2,\ldots$, we can write the ODE

$$G'+2\left(\frac{2n+1}{4}\right)^2G=0\,,$$

that has solution $G_n(t)=e^{-2\left(\frac{2n+1}{4}\right)^2t}$ for $n=0,1,2,\ldots$.

Then our desired solutions are

$$u_n(x,t)=F_n(x)G_n(t)=\sin\left(\frac{2n+1}{4}x\right)e^{-2\left(\frac{2n+1}{4}\right)^2t}\qquad\text{for }n=0,1,2,\ldots$$

Now we want to find a linear combination $u(x,t)=\sum_{n=0}^{\infty}B_nu_n(x,t)$ such that

$$\begin{array}{rcl}
u(x,0)&=&\displaystyle\sum_{n=0}^{\infty}B_nu_n(x,0)=\sum_{n=0}^{\infty}B_nF_n(x)G_n(0)\\[8pt]
&=&\displaystyle\sum_{n=0}^{\infty}B_n\sin\left(\frac{2n+1}{4}x\right)=\cos(x)\sin\left(\frac{x}{4}\right)\,.
\end{array}$$

But $\cos(x)\sin\left(\frac{x}{4}\right)=-\frac{1}{2}\sin\left(\frac{3}{4}x\right)+\frac{1}{2}\sin\left(\frac{5}{4}x\right)$, so it follows that $B_1=-\frac{1}{2}$ and $B_2=\frac{1}{2}$ and the rest of $B_n$'s are zero. Therefore our desired solution is

$$u(x,t)=-\frac{1}{2}\sin\left(\frac{3}{4}x\right)e^{-2\left(\frac{3}{4}\right)^2t}+\frac{1}{2}\sin\left(\frac{5}{4}x\right)e^{-2\left(\frac{5}{4}\right)^2t}\,.$$

Kildesett: course=TMA4130 term=host year=2016 problem=2 file=n16h.pdf
