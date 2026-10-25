### **Solution to Problem 4**

**a)** We write $u=F(x)G(y)$, and thus

$$u_{xx}+u_{yy}=F''G+FG''=0,$$

Rearranging gives

$$\frac{F''}{F}=-\frac{G''}{G},$$

and as the left hand side is a function of $x$ alone, and the right hand side is a function of $y$ alone, they must both be equal to some constant, $k$, i.e

$$F''-kF=0,\quad G''+kG=0$$

The boundary conditions give (for non-trivial solutions) $F(0)=F'(2)=0$. We solve the equation for $F$ subject to these conditions. There are three possible cases:

1. $k=p^2>0$. Then

   $$F(x)=A\cosh px+B\sinh px,$$

   whereupon $F(0)=0\Rightarrow A=0$. It follows that $F'(x)=Bp\cosh px$. As $\cosh$ is never zero, the condition $F'(2)=0$ gives $B=0$, and hence we obtain only the trivial solution.

2. $k=0$. Then

   $$F(x)=Ax+B$$

   and $F(0)=0$ gives $B=0$. However, $F'(x)=A$, and hence $F'(2)=0$ forces $A=0$, giving again only the trivial solution

3. $k=-p^2<0$. Now

   $$F(x)=A\cos px+B\sin px$$

   As $F(0)=0$ we have $A=0$. We then differentiate to find $F'(x)=Bp\cos px$. To satisfy $F'(2)=0$, we require

   $$\cos 2p=0\Rightarrow p=\frac{(2n+1)\pi}{4},\ n=1,2,3,\ldots$$

We now solve

$$G''-p^2G=0$$

which has a general solution

$$G_n=A_n\cosh\frac{(2n+1)\pi y}{4}+B_n\sinh\frac{(2n+1)\pi y}{4}$$

We therefore have the general solution

$$u(x,t)=\sum_{n=1}^{\infty}\left(A_n\cosh\frac{(2n+1)\pi y}{4}+B_n\sinh\frac{(2n+1)\pi y}{4}\right)\sin\frac{(2n+1)\pi x}{4}$$

**b)** Differentiation gives

$$u_y(x,0)=\sum_{n=1}^{\infty}\frac{(2n+1)\pi B_n}{4}\sin\frac{(2n+1)\pi x}{4}=0,$$

hence $B_n=0$ for all $n$. We then have

$$u(x,1)=\sum_{n=1}^{\infty}A_n\cosh\frac{(2n+1)\pi}{4}\sin\frac{(2n+1)\pi x}{4}=50\sin\frac{5\pi x}{4}$$

The middle term is the Fourier series for the rightmost term, and comparing the two we see that $A_n=0$ for $n\neq 2$, whilst

$$A_2=\frac{50}{\cosh\frac{5\pi}{4}}$$

We then have

$$u(x,t)=\frac{50\sin\frac{5\pi x}{4}\cosh\frac{5\pi y}{4}}{\cosh\frac{5\pi}{4}}$$

Kildesett: course=TMA4125 term=var year=2017 problem=4 file=exam.pdf
