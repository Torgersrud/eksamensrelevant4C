### **Solution to Problem 5**

Postulating the ansatz $u(t,x)=F(x)G(t)$, and inserting it into the heat equation we find

$$F(x)\frac{\mathrm{d}G}{\mathrm{d}t}=\frac{\mathrm{d}^{2}F}{\mathrm{d}x^{2}}G(t).$$

This gives us

$$\frac{1}{G}\frac{\mathrm{d}G}{\mathrm{d}t}=\frac{1}{F}\frac{\mathrm{d}^{2}F}{\mathrm{d}x^{2}},$$

which is an equation with a function of $t$ on the left and a function of an independent variable $x$ on the right. Therefore both sides must be equal to some constant $k$, i.e.,

$$\frac{1}{G_k}\frac{\mathrm{d}G_k}{\mathrm{d}t}=\frac{1}{F_k}\frac{\mathrm{d}^{2}F_k}{\mathrm{d}x^{2}}=k.$$

The boundary conditions applied to the ansatz give:

$$G(t)F(0)=G(t)F(\pi)=0.$$

The only non-trivial solution is $F(0)=F(\pi)=0$.

If $k=0$, we find that

$$\frac{\mathrm{d}^{2}F_k}{\mathrm{d}x^{2}}=0\qquad\Longrightarrow\qquad F_0(x)=a_0x+b_0.$$

This is only compatible with the boundary conditions if $a_0=b_0=0$.

Likewise if $k>0$, we find

$$\frac{\mathrm{d}^{2}F_k}{\mathrm{d}x^{2}}=kF_k,\tag{1}$$

which has the general solution

$$F_k(x)=A_ke^{\sqrt{k}t}+B_ke^{-\sqrt{k}t}.$$

Again, there are no non-zero constants $A_k$, $B_k$ for which $F_k$ can satisfy the boundary conditions.

It remains then to $k=-p^2<0$ for existence of non-trivial solutions. We find general solutions to (1) are

$$F_p(x)=A_p\cos(px)+B_p\sin(px),$$

where we have re-labelled the solutions $F_k$ by $F_p$ with $p>0$.

The boundary conditions impose the following restrictions:

$$F_p(0)=0\implies A_p=0,\qquad F_p(\pi)=0\implies p\in\mathbb{Z}.$$

But we also assumed (in order not to double-count) that $p>0$. Hence $p\in\mathbb{N}\backslash\{0\}$.

Turning to the equation for $G_p$, we find

$$G_p(t)=C_pe^{-p^2t}.$$

Writing $D_p=B_pC_p$, we use the linearity of the PDE to write a solution of the form

$$u(t,x)=\sum_{p=1}^{\infty}D_p\sin(px)e^{-p^2t}.$$

This is enough for us to fit the initial condition. Assuming continuity in $t$ of the series, we can write

$$f(x)=u(0,x)=\sum_{p=1}^{\infty}D_p\sin(px).$$

By extending $f$ in an odd fashion to $[-\pi,\pi]$, to

$$\tilde{f}(x)=\begin{cases}f(x)&0\leq x<\pi\\ -f(-x)&-\pi\leq x<0\end{cases},$$

and then periodically over $\mathbb{R}$

$$f_-(x)=\sum_{n\in\mathbb{Z}}\tilde{f}(x-2n\pi)\mathbb{1}_{[(2n-1)\pi,(2n+1)\pi)}$$

$$=\sum_{n\in\mathbb{Z}}f(x-2n\pi)\mathbb{1}_{[2n\pi,(2n+1)\pi)}-f(-x+2n\pi)\mathbb{1}_{[-(2n+1)\pi,-2n\pi)}$$

we see that $f_-(x)$ is an odd function whose restriction to $[0,\pi)$ is $f$.

Therefore using the inversion formula, we can write

$$D_n=\frac{1}{2\pi}\int_{0}^{\pi}f_-(x)\sin(nx)\,\mathrm{d}x=\frac{1}{2\pi}\int_{0}^{\pi}f(x)\sin(nx)\,\mathrm{d}x.$$

This determines a solution $u(t,x)$ completely.

Kildesett: course=TMA4135 term=kont year=2020 problem=5 points=14 file=tma4130_kont.pdf
