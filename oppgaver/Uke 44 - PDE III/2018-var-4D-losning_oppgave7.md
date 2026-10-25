### **Løsning til Oppgave 7**

**a)** We plug $u(x,t)=F(x)G(t)$ into the wave equation and obtain two ODEs

$$F''-kF=0$$

$$G''-kG=0.$$

We split into three cases $k=0$, $k>0$ and $k<0$. The only non-trivial solution is for $k=-p^2<0$. The first equation then have solution

$$F(x)=A\cos px+B\sin px.$$

From the boundary conditions, we get $F(0)=0$ and $F(4)=0$, so $A=0$ and

$$\sin 4p=0,\quad\text{ hence }\quad p=\frac{n\pi}{4},\qquad n=1,2,\ldots$$

We can set $B=1$. We now solve the second equation with $k=-p^2=-{(\frac{n\pi}{4})}^2$ . It has a solution of the form

$$G_n(t)=B_n\cos pt+B_n^*\sin pt.$$

The solutions of the form $F(x)G(t)$ are thus given by

$$u_n(x,t)=\left(B_n\cos\left(\frac{n\pi}{4}t\right)+B_n^*\sin\left(\frac{n\pi}{4}t\right)\right)\sin\left(\frac{n\pi}{4}x\right)$$

**b)** To find a solution that satisfies the initial condition, we need to sum over those functions. We have

$$u(x,t)=\sum_{n=1}^{\infty}\left(B_n\cos\left(\frac{n\pi}{4}t\right)+B_n^*\sin\left(\frac{n\pi}{4}t\right)\right)\sin\left(\frac{n\pi}{4}x\right).$$

We thus have, using the initial condition,

$$3\sin(\pi x)=u(x,0)=\sum_{n=1}^{\infty}B_n\sin\frac{n\pi x}{4}.$$

This is a Fourier sine series. Comparing the two Fourier series, we see that the coefficients $B_n$ are given by

$$B_4=3,\qquad B_n=0,\quad\text{if }n\neq 4.$$

To obtain the coefficients $B_n^*$, we take the derivative of the series with respect to $t$:

$$u_t(x,t)=\sum_{n=1}^{\infty}\left(-B_n\frac{n\pi}{4}\sin\left(\frac{n\pi}{4}t\right)+B_n^*\frac{n\pi}{4}\cos\left(\frac{n\pi}{4}t\right)\right)\sin\left(\frac{n\pi}{4}x\right).$$

Using the other initial condition:

$$\sin(4\pi x)=u_t(x,0)=\frac{n\pi}{4}\sum_{n=1}^{\infty}B_n^*\sin\left(\frac{n\pi}{4}x\right).$$

Comparing again the two Fourier series, we have

$$B_{16}^*=\frac{1}{4\pi},\qquad B_n^*=0,\quad\text{if }n\neq 16.$$

Thus, the solution to the differential equation is

$$u(x,t)=3\cos(\pi t)\sin(\pi x)+\frac{1}{4\pi}\sin(4\pi t)\sin(4\pi x).$$

**c)**

- The corresponding difference equations for the point $(x_i,t_n)$ using central differences becomes

$$\frac{U_i^{n+1}-2U_i^n+U_i^{n-1}}{\Delta t^2}=\frac{U_{i+1}^n-2U_i^n+U_{i-1}^n}{\Delta x^2}.$$

Solve this with respect to $U_i^{n+1}$, set $r=\Delta x/\Delta t$ for simplicity (not required), and the algorithm becomes: For $n=1,2,\ldots$:

$$U_i^{n+1}=r^2(U_{i+1}^n+U_{i-1}^n)+2(1-r^2)U_i^n-U_i^{n-1},\qquad i=1,\ldots,M-1$$

$$U_0^{n+1}=0,\qquad U_M^{n+1}=0. \tag{1}$$

- Extend the solution domain to $t=-\Delta t$, and use a central difference formula to approximate the starting condition $u_t(x,0)=\sin(4\pi x)$. For $n=0$ we have the following two equations:

$$U_i^1=r^2(U_{i+1}^0+U_{i-1}^0)+2(1-r^2)U_i^0-U_i^{-1},$$

$$\frac{U_i^1-U_i^{-1}}{2\Delta t}=\sin(4\pi x_i)$$

Solve the last with respect to $U_i^{-1}$ and insert this into the first expressions gives the following expression for $U_i^1$:

$$U_i^1=\frac{r^2}{2}(U_{i+1}^0+U_{i-1}^0)+(1-r^2)U_i^0+\Delta t\sin(4\pi x_i),\qquad i=1,\ldots,M-1 \tag{2}$$

$$U_i^0=3\sin(\pi x_i).$$

- With $\Delta x=\Delta t=0.1$ the pararmeter $r=1$ and thus $r^2-1=0$. To find an approximation $U_1^2\approx u(0.1,0.2)$ we need *in this particular case* only to calculate $U_2^1$ from (2) first, and then $U_1^2$ from (1). Use also the boundary condition $U_0^n=0$: So

$$U_2^1=\frac{3}{2}(\sin(0.1\pi)+\sin(0.3\pi))+0.1\sin(0.8\pi)=1.735830,$$

$$U_1^2=U_2^1-U_1^0=\frac{3}{2}\Big((\sin 0.3\pi)-\sin(0.1\pi)\Big)+0.1\cdot\sin(0.8\pi)=0.808779.$$

To compare, the exact solution is $u(0.1,0.2)=0.79449$.

Kildesett: course=TMA4135 term=var year=2018 problem=7 file=tma4125_final_exam_may_bm.pdf
