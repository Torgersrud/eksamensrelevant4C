### **Solution to Problem 9**

**a)** Inserting the function $u(x,y)=F(x)G(y)$ into the PDE, we obtain the equation

$$F''(x)G(y)+F(x)G''(y)+5F(x)G(y)=0,$$

which we rewrite as

$$\frac{F''(x)}{F(x)}=-\frac{G''(y)}{G(y)}-5.$$

Now the left hand side only depends on $x$ while the right hand side only depends on $y$, which implies that both sides need to be constant, say equal to $k$ for some $k\in\mathbb{R}$. We thus obtain that

$$\begin{array}{c}F''(x)=kF(x),\\[6pt] G''(y)=(-5-k)G(y).\end{array}$$

We now consider the different possibilities for $k$.

- $k=0$:

  Here the equation for $F$ has the solution

  $$F(x)=Ax+B.$$

  The boundary condition $F(0)=0$ implies that $B=0$, and the boundary condition $F(\pi)=0$ then implies that $0=A\pi$, and thus $A=0$. Thus we only obtain the trivial solution $F(x)=0$.

- $k=p^2>0$:

  Here the equation for $F$ has the solution

  $$F(x)=A\sinh px+B\cosh px.$$

  Now the boundary condition $F(0)=0$ implies that $B=0$, and the boundary condition $F(\pi)=0$ then implies that $0=A\sinh p\pi$, and therefore $A=0$. Again, we only obtain the trivial solution.

- $k=-p^2<0$:

  Here we obtain for $F$ the solutions

  $$F(x)=A\sin px+B\cos px.$$

  Again the boundary condition $F(0)=0$ implies that $B=0$. The boundary condition $F(\pi)=0$, however, then implies that either $A=0$ or $p\in\mathbb{N}$. Thus we obtain the non-trivial solution

  $$F(x)=\sin px$$

  with $p\in\mathbb{N}$.

Now we turn to the solution of the equation

$$G''(y)=-(5+k)G(y)=-(5-p^2)G(y),$$

which has the solution

$$G_p(y)=A\cos(\sqrt{5-p^2}\cdot y)+B\sin(\sqrt{5-p^2}\cdot y).$$

when $p=1,2$ and

$$G_p(y)=A\cosh(\sqrt{p^2-5}\cdot y)+B\sinh(\sqrt{p^2-5}\cdot y).$$

when $p\ge 3$.

In total, we therefore obtain the nontrivial solutions

$$u_p(x,y)=\sin(px)\left(A\cos(\sqrt{5-p^2}\cdot y)+B\sin(\sqrt{5-p^2}\cdot y)\right)$$

for $p=1,2$, and

$$u_p(x,y)=\sin(px)\left(A\cosh(\sqrt{p^2-5}\cdot y)+B\sinh(\sqrt{p^2-5}\cdot y)\right)$$

when $p\ge 3$.

**b)** Using the results of Problem 9a, we obtain that

$$\begin{array}{l}\displaystyle u(x,y)=\sum_{p=1}^{2}\sin(px)\left(A_p\cos(\sqrt{5-p^2}\cdot y)+B_p\sin(\sqrt{5-p^2}\cdot y)\right)+\\[10pt]
\displaystyle\qquad+\sum_{p=3}^{\infty}\sin(px)\left(A_p\cosh(\sqrt{p^2-5}\cdot y)+B_p\sinh(\sqrt{p^2-5}\cdot y)\right)\end{array}$$

for some coefficients $A_p$, $B_p\in\mathbb{R}$.

The boundary condition $u(x,0)=\sin(x)$ now yields that

$$\sin x=u(x,0)=\sum_{p=1}^{\infty}\sin(px)A_p\,,$$

which immediately implies that

$$A_1=1\qquad\text{and }A_p=0\text{ for }p\ge 2.$$

That is,

$$u(x,y)=\sin(x)\cos(2y)+\sum_{p=1}^{2}B_p\sin(px)\sin(\sqrt{5-p^2}\cdot y)+\sum_{p=3}^{\infty}B_p\sin(px)\sinh(\sqrt{p^2-5}\cdot y).$$

Now we insert the second boundary condition $u(x,\pi/4)=\sin(x)$ and obtain that

$$\begin{array}{l}\displaystyle\sin(x)=\sin(x)\cos(2\cdot\pi/4)+\sum_{p=1}^{2}B_p\sin(px)\sin(\sqrt{5-p^2}\cdot\pi/4)+\sum_{p=3}^{\infty}B_p\sin(px)\sinh(\sqrt{p^2-5}\cdot\pi/4)\\[10pt]
\displaystyle\qquad=0+\sum_{p=1}^{2}B_p\sin(px)\sin(\sqrt{5-p^2}\cdot\pi/4)+\sum_{p=3}^{\infty}B_p\sin(px)\sinh(\sqrt{p^2-5}\cdot\pi/4).\end{array}$$

This implies that $B_p=0$ for $p\ge 2$ and

$$B_1=\frac{1}{\sin(2\cdot\pi/4)}=1$$

Thus

$$u(x,y)=\sin x\cdot(\cos(2y)+\sin(2y)).$$

Kildesett: course=TMA4125 term=kont year=2016 problem=9 file=english.pdf
