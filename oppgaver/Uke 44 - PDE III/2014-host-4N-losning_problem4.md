### **Solution to Problem 4**

**a)** Since $u=F(x)G(t)$ we have that $u_{xx}=F''G$ and $u_t=FG'$, and inserting them in the equation we have $FG'=2F''G$. Then since

$$\frac{G'}{G}=2\frac{F''}{F}=k\qquad\text{where k is a constant,}$$

we can derive the two ODEs

$$\left\{\begin{array}{l}F''-\frac{k}{2}F=0\\ G'-kG=0\end{array}\right.$$

The boundary conditions say that $F'(0)=0$ and $F(\pi)=0$, so we can easily check that if $k=0$ or $k>0$ then $F=0$, and hence $u=0$. Since we want only non-trivial solutions, we neglect these options.

So we consider $k=-p^2<0$, and hence the solutions to the ODE $F''+\frac{p^2}{2}F=0$ are of the form

$$F(x)=A\cos\left(\frac{p}{\sqrt{2}}x\right)+B\sin\left(\frac{p}{\sqrt{2}}x\right)\,.$$

Since $F'(0)=-A\frac{p}{\sqrt{2}}\sin\left(\frac{p}{\sqrt{2}}0\right)+B\frac{p}{\sqrt{2}}\cos\left(\frac{p}{\sqrt{2}}0\right)=B\frac{p}{\sqrt{2}}=0$, we have $B=0$. Finally since $F(\pi)=A\cos\left(\frac{p}{\sqrt{2}}\pi\right)=0$, this implies $\cos\left(\frac{p}{\sqrt{2}}\pi\right)=0$, so $\frac{p}{\sqrt{2}}\pi=\frac{2n+1}{2}\pi$ for $n=0,1,\ldots$. So if we isolate $p$ we have $p=\frac{2n+1}{\sqrt{2}}$ for $n=0,1,\ldots$, so we have that

$$F_n(x)=\cos\left(\frac{2n+1}{2}x\right)\qquad n=0,1,\ldots$$

So we solve the second ODE, so $G'+p^2G=0$ and replacing $p=\frac{2n+1}{\sqrt{2}}$ we have that

$$G_n'+\frac{(2n+1)^2}{2}G_n=0\qquad n=0,1,\ldots$$

and easily we can find the solution

$$G_n=A_ne^{-\frac{(2n+1)^2}{2}t}\qquad n=0,1,\ldots$$

Therefore merging both solutions we have that

$$u_n=F_nG_n=A_ne^{-\frac{(2n+1)^2}{2}t}\cos\left(\frac{2n+1}{2}x\right)\qquad n=0,1,\ldots$$

**b)** The initial conditions say that $u(x,0)=\cos(x)\cos(\frac{3}{2}x)=\frac{1}{2}\left(\cos(\frac{1}{2}x)+\cos(\frac{5}{2}x)\right)$, so

$$u(x,0)=\sum_{n=0}^{\infty}u_n(x,0)=\sum_{n=0}^{\infty}F_n(x)G_n(0)=\sum_{n=0}^{\infty}A_n\cos\left(\frac{2n+1}{2}x\right).$$

Therefore $A_0=A_2=\frac{1}{2}$, and hence

$$u(x,t)=\frac{1}{2}e^{-\frac{1}{2}t}\cos\left(\frac{1}{2}x\right)+\frac{1}{2}e^{-\frac{25}{2}t}\cos\left(\frac{5}{2}x\right)$$

Kildesett: course=TMA4130 term=host year=2014 problem=4 file=eksam2014.pdf
