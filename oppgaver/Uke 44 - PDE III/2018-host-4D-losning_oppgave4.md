### **Løsning til Oppgave 4**

**Step 1: Separating variables**: Find solutions of the form

$$u(t,x)=G(t)F(x).$$

Since

$$u_t=G'F,\;\;\;u_{xx}=GF'',$$

our equation becomes

$$G'F=\frac{1}{2}GF'',$$

thus

$$\frac{2G'}{G}=\frac{F''}{F}\equiv k.$$

**Step 2: Fit boundary conditions**: Notice that the boundary conditions

$$G(t)F(0)=G(t)F(\pi)=0,$$

are equivalent to

$$F(0)=F(\pi)=0.$$

In case $k=0$, then $F''\equiv 0$, i.e $F(x)=ax+b$. The boundary conditions imply then that $F\equiv 0$.

In case $k=\mu^2>0$, then the general solution for

$$F''=\mu^2 F$$

is $F(x)=Ae^{\mu x}+Be^{-\mu x}$. The boundary conditions imply this time that

$$A+B=0,\;\;\;Ae^{\mu\pi}+Be^{-\mu\pi}=0,$$

thus $A=B=0$.

Hence, the only possible case is $k=-p^2<0$, then the general solution for

$$F''=-p^2F$$

is $F(x)=A\cos px+B\sin px$, such that $F(0)=0$ gives $A=0$. Thus $F(x)=B\sin px$, $B\neq 0$, but $F(\pi)=0$ gives $\sin p\pi=0$, i.e.

$$p=n,\;\;\;n=1,2,\ldots$$

(notice that $\sin{-px}=-\sin px$, thus up to a constant they give the same solution).

**Summary**: The boundary condition implies that $p^2=n^2$, $n=1,2,\ldots$, and

$$F(x)=F_n(x)=\sin nx.$$

Now we can solve

$$G'=-\frac{n^2}{2}G$$

and get

$$G_n(t)=B_ne^{-\frac{n^2}{2}t}.$$

Thus the general solution is

$$u(t,x)=\sum_{n=1}^{\infty}B_ne^{-\frac{n^2}{2}t}\sin nx.$$

**Step 3: Fit the initial conditions**: We have

$$u(0,x)=\sum_{n=1}^{\infty}B_n\sin nx=f(x).$$

By the uniqueness of the Fourier sine series, we get

$$B_3=B_5=1,\;\;\;B_n=0,\quad\text{if }n\neq 3,5.$$

Thus

$$u(t,x)=e^{-\frac{9}{2}t}\sin 3x+e^{-\frac{25}{2}t}\sin 5x.$$

Kildesett: course=TMA4135 term=host year=2018 problem=4 points=10 file=exam_fall18_tma4130_norsk.pdf
