### **Løsning til Oppgave 6**

**a)** Standard separation of variables gives

$$F''+kF=0,\quad G''-kG=0$$

for some constant $k\in\mathbb R$. Three cases to be considered:

(i) $k=-\lambda^2<0$. Using the boundary condition $0=F'(0)=F'(\pi)$ we see that $F$ is identically zero.

(ii) $k=0$. Using the boundary condition $0=F'(0)=F'(\pi)$, we see that $F$ constant is the only solution.

(iii) $k=\lambda^2>0$. Using the boundary condition $0=F'(0)=F'(\pi)$, we see in the standard manner that $\lambda=n\in\mathbb Z$ and

$$F(x)=\beta_n\cos(nx),\quad n\in\mathbb Z,$$

for any constant $\beta_n\in\mathbb R$. Since cosinus is an even function it suffices to consider nonnegative integers.

Using this result for the equation for $G$, we infer that

$$G(y)=A_ne^{ny}+B_ne^{-ny},\quad n\in\mathbb N,$$

for any constants $A_n,B_n\in\mathbb R$. For $n=0$ we find $G(y)=A_0y+B_0$ for constants $A_0,B_0\in\mathbb R$.

Thus the general solution of the form $u=FG$ reads

$$u(x,y)=F(x)G(y)=u_n(x,y)=\begin{cases}A_0y+B_0,&\text{for }n=0,\\ \cos(nx)(A_ne^{ny}+B_ne^{-ny}),&\text{for }n\in\mathbb N.\end{cases}$$

**b)** The general solution reads

$$u(x,y)=\sum_{n=0}^{\infty}u_n(x,y)=A_0y+B_0+\sum_{n=1}^{\infty}\cos(nx)(A_ne^{ny}+B_ne^{-ny}).$$

The boundary condition at $y=0$ yields

$$u(x,0)=B_0+\sum_{n=1}^{\infty}\cos(nx)(A_n+B_n)=0.$$

By the uniqueness of Fourier series we conclude that $B_0=0$ and $A_n=-B_n$ for $n\in\mathbb N$. The boundary condition at $y=0$ yields

$$\begin{aligned}u_y\left(x,\frac{\pi}{2}\right)&=A_0+\sum_{n=1}^{\infty}\cos(nx)nA_n(e^{n\pi/2}+e^{-n\pi/2})\\
&=(1+\cos(x))^2\\
&=1+2\cos(x)+\cos^2(x)\\
&=\frac{3}{2}+2\cos(x)+\frac{1}{2}\cos(2x).\end{aligned}$$

Again by the uniqueness of Fourier series we conclude that $A_0=3/2$, $1A_1(e^{\pi/2}+e^{-\pi/2})=2$, and $2A_2(e^{\pi}+e^{-\pi})=1/2$, while all the other constants vanish. We may write

$$A_1=\frac{1}{\cosh(\pi/2)},\quad A_2=\frac{1}{8\cosh(\pi)}.$$

Thus

$$u(x,y)=\frac{3}{2}y+\frac{1}{\cosh(\pi/2)}\cos(x)(e^y-e^{-y})+\frac{1}{8\cosh(\pi)}\cos(2x)(e^{2y}-e^{-2y}).$$

Kildesett: course=TMA4135 term=kont year=2016 problem=6 file=tma4135_16k.pdf
