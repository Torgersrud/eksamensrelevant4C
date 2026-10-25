### **Løsning til Oppgave 6**

Bruk:

$$u_t(x_i,t_j)\approx\frac{1}{k}(u(x_i,t_j+k)-u(x_i,t_j)),\qquad u_{xx}(x_i,t_j)\approx\frac{1}{h^2}(u(x_i+h,t_j)-2u(x_i,t_j)+u(x_i-h,t_j)).$$

Sett dette inn i ligningen, og la $U_{ij}\approx u(x_i,t_j)$:

$$\frac{1}{k}(U_{i,j+1}-U_{i,j})=\frac{1}{h^2}(U_{i+1,j}-2U_{ij}+U_{i,j-1})$$

Setter vi inn randverdiene $U_{0j}=U_{Nj}=0$ og startverdien $U_{i0}=x_i(1-x_i)$ får vi følgende skjema:

For $j=0,1,2,\ldots$:

$$U_{i,j+1}=U_{ij}+\frac{k}{h^2}(U_{i+1,j}-2U_{ij}+U_{i-1,j}),\qquad i=1,2,\cdots,N-1.$$

Med $k=1/10$, $h=1/3$ får vi at $r=9/10$. Startverdiene blir:

$$U_{00}=0,\ U_{10}=\frac{2}{9},\ U_{20}=\frac{2}{9},\ U_{30}=0,$$

og

$$u(1/3,10)\approx U_{11}=\frac{1}{45},\qquad u(2/3,1/10)\approx U_{21}=\frac{1}{45}.$$

*Kjeldevarsel: I den første utledinga er siste ledd på høgre side skrive $U_{i,j-1}$; det må vere $U_{i-1,j}$ (skjemaet lenger nede er korrekt). Også skrivemåten $u(1/3,10)$ er ein skrivefeil for $u(1/3,1/10)$; verdien $U_{11}=\frac{1}{45}$ er korrekt.*

Kildesett: course=TMA4135 term=kont year=2012 problem=6 file=tma4135_12k.pdf
