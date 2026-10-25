### **Løsning til Oppgave 9**

Differanseskjemaet blir for $U_{i,j}\approx u(x_i,t_j)$:

$$\frac{U_{i,j+1}-U_{ij}}{k}=\kappa\frac{U_{i+1,j}-2U_{i,j}+U_{i-1,j}}{h^2}+x_i(1-x_i)$$

eller

$$U_{i,j+1}=U_{i,j}+\kappa\frac{k}{h^2}(U_{i+1,j}-2U_{i,j}+U_{i-1,j})+kx_i(1-x_i),$$

for $i=1,2,\ldots,N-1$, og $j=0,1,2,\ldots,$ og med

$$U_{i,0}=\sin(\pi x_i)=\sin(i\pi h),\qquad U_{0,j}=U_{N,j}=0.$$

Med $\kappa=0.1$, $h=0.25$ og $k=0.2$ blir dette ($x_i=0.25i$)

$$U_{i,j+1}=U_{i,j}+0.32(U_{i+1,j}-2U_{i,j}+U_{i-1,j})+0.05i(1-0.25i).$$

Med startverdiene

$$
\begin{aligned}
U_{0,0}&=0,\ U_{1,0}=\sin(\pi/4)=0.70711,\ U_{2,0}=\sin(\pi/2)=1,\\
U_{3,0}&=\sin(3\pi/4)=0.70711,\ U_{4,0}=\sin(\pi)=0
\end{aligned}
$$

ender vi med

$$
\begin{aligned}
u(0.25,0.2)&\approx U_{1,1}=0.6121,\\
u(0.5,0.2)&\approx U_{2,1}=0.8625,\\
u(0.75,0.2)&\approx U_{3,1}=0.6121.
\end{aligned}
$$

*Kjeldevarsel: Losningsarket vekslar sjølv mellom notasjonane $U_{ij}$ og $U_{i,j}$ i det første skjemaet — spel av som trykt.*

Kildesett: course=TMA4130 term=host year=2010 problem=9 file=eksamen-bok_2010.pdf
