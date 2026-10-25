### **Solution to Problem 2**

**a)** Setting $u(x,t)=X(x)T(t)$ gives

$$\frac{X''}{X}=\frac{T'}{c^2T}=k$$

for some constant $k$, so we have the two ordinary differential equations

$$X''-kX=0\qquad(1)$$

$$T'-c^2kT=0\qquad(2)$$

subject to $X(0)=0$ and $X(1)=0$. It is easily verified that $k\ge 0$ yields only trivial solutions (use the boundary conditions for equation (1)), so consider $k=-p^2<0$. The solutions of equation (1) are then of the form

$$X(x)=A_p\cos px+B_p\sin px,$$

and since $0=X(0)=A_p$, we have

$$X(x)=B_p\sin px.$$

Since $0=X(1)=B_p\sin p$, non-trivial solutions must have $p\in\{\pi,2\pi,\ldots\}$, giving

$$X_l(x)=B_l\sin l\pi x$$

for $l=1,2,\ldots$. Thus equation (2) becomes

$$T_l'(t)+(c\pi l)^2T_l(t)=0,$$

which has solutions

$$T_l(t)=e^{-(c\pi l)^2t}.$$

The solutions asked for are therefore linear combinations of

$$u_l(x,t)=B_le^{-(c\pi l)^2t}\sin l\pi x.$$

**b)** Letting $v(x,t)=u(x,t)-x$, we see that $v$ satisfies the same PDE as $u$, i.e.

$$\frac{\partial v}{\partial t}=c^2\frac{\partial^2 v}{\partial x^2}.$$

The boundary condition $u(1,t)=1$ gives $v(1,t)=0$, so in fact $v$ satisfies the same boundary conditions as $u$ did in problem 2a, and hence the general solution is (from 2a)

$$v(x,t)=\sum_{l=1}^{\infty}B_le^{-(c\pi l)^2t}\sin l\pi x.$$

The initial condition $x(2-x)=u(x,0)=v(x,0)+x$ gives $v(x,0)=x-x^2$, and so

$$x-x^2=v(x,t)=\sum_{l=1}^{\infty}B_l\sin l\pi x.$$

Since the left hand side of this equation defines a continuous function $f:[0,1]\to\mathbb{R}$, the Fourier series theorem gives that the $B_l$'s are in fact the Fourier coeffieients of the 2-periodic odd extension of $f$. We compute these:

$$B_l=2\int_{0}^{1}(x-x^2)\sin l\pi x\,\mathrm{d}x=2\int_{0}^{1}x\sin l\pi x\,\mathrm{d}x-2\int_{0}^{1}x^2\sin l\pi x\,\mathrm{d}x.$$

Calling the first term $\alpha_1$ and the second term $\alpha_2$, we find by partial integration

$$\alpha_1=\frac{2}{l\pi}(-1)^{l+1}$$

$$\alpha_2=-\alpha_1-\frac{4}{(l\pi)^3}\left((-1)^l-1\right).$$

Thus

$$B_l=\alpha_1+\alpha_2=-\frac{4}{(l\pi)^3}\left((-1)^l-1\right)=\begin{cases}0&\text{if $l$ even}\\[6pt] \dfrac{8}{(l\pi)^3}&\text{if $l$ odd,}\end{cases}$$

and hence the solution of the PDE with given boundary conditions is

$$u(x,t)=v(x,t)+x=x+\frac{8}{\pi^3}\sum_{m=0}^{\infty}\frac{1}{(2m+1)^3}e^{-(c\pi(2m+1))^2t}\sin(2m+1)\pi x.$$

*Kjeldevarsel: Leddet "x−x² = v(x,t) = …" er trykt med v(x,t); etter setningen over skal det vere v(x,0).*

Kildesett: course=TMA4130 term=host year=2013 problem=2 file=eksamen-bok_2013h.pdf
