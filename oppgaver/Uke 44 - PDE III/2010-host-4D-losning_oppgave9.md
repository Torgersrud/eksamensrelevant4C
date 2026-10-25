### **Løsning til Oppgave 9**

Differanseskjemaet blir for $U_{i,j}\approx u(x_i,t_j)$

$$\frac{U_{i,j+1}-U_{i,j}}{k}=\kappa\frac{U_{i+1,j}-2U_{i,j}+U_{i-1,j}}{h^2}+x_i(1-x_i)$$

eller

$$U_{i,j+1}=U_{i,j}+\kappa\frac{k}{h^2}\big(U_{i+1,j}-2U_{i,j}+U_{i-1,j}\big)+kx_i(1-x_i),$$

for $i=1,2,\ldots,N-1$, og $j=0,1,2,\ldots$, og med

$$U_{i,0}=\sin\pi x_i=\sin i\pi h,\qquad U_{0,j}=U_{N,j}=0.$$

Med $\kappa=0.1$, $h=0.25$ og $k=0.2$ blir dette ($x_i=0.25i$)

$$U_{i,j+1}=U_{i,j}+0.32\big(U_{i+1,j}-2U_{i,j}+U_{i-1,j}\big)+0.05i(1-0.25i).$$

Med startverdiene

$$
\begin{aligned}
U_{0,0}=0,\ U_{1,0}=\sin\frac{\pi}{4}\approx 0.70711,\ U_{2,0}=\sin\frac{\pi}{2}=1,\\
U_{3,0}=\sin\frac{3\pi}{4}\approx 0.70711,\ U_{4,0}=\sin\pi=0
\end{aligned}
$$

ender vi med

$$
\begin{aligned}
u(0.25,\,0.2)&\approx U_{1,1}\approx 0.6121,\\
u(0.50,\,0.2)&\approx U_{2,1}\approx 0.8625,\\
u(0.75,\,0.2)&\approx U_{3,1}\approx 0.6121.
\end{aligned}
$$

Kildesett: course=TMA4135 term=host year=2010 problem=9 file=tma4135_10h.pdf
