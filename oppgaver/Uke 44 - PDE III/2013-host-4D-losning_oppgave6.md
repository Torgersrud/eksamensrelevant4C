### **Løsning til Oppgave 6**

Ved å benytte en sentraldifferanse i rom får vi tilnærmingen

$$u_{xx}(x,t)\approx\frac{1}{h^2}\left[u(x+h,t)-2u(x,t)+u(x-h,t)\right].\tag{6}$$

Ved å benytte en foroverdifferanse i tid får vi tilnærmingen

$$u_t(x,t)\approx\frac{1}{k}\left[u(x,t+k)-u(x,t)\right].\tag{7}$$

Innsatt for (6) og (7) i $u_t(x,t)=u_{xx}(x,t)+5u(x,t)$ får vi

$$\frac{1}{k}\left[u(x,t+k)-u(x,t)\right]\approx\frac{1}{h^2}\left[u(x+h,t)-2u(x,t)+u(x-h,t)\right]+5u(x,t).\tag{8}$$

La $x_i=ih$, $i=0,1,2,3,4$ og $t_j=jk$, $j=1,2,3,\ldots$, og la $U_{i,j}\approx u(x_i,t_j)=u(ih,jk)$. Da kan skrive (8) som følgende *eksplisitte* differenseskjema

$$\frac{1}{k}(U_{i,j+1}-U_{i,j})=\frac{1}{h^2}(U_{i+1,j}-2U_{i,j}+U_{i-1,j})+5U_{i,j},$$

Dette gir

$$U_{i,j+1}=U_{i+1,j}+U_{i-1,j}-\frac{11}{16}U_{i,j},\tag{9}$$

der vi har benyttet at $k/h^2=1$ i vårt tilfelle.

Randbetingelsene gir at $U_{0,0}=U_{4,0}=0$, $U_{1,0}=U_{3,0}=3/4$ og $U_{2,0}=1$. Innsatt for $i=1,2$ og 3 og $j=0$ i (9) får vi henholdsvis

$$U_{1,1}=\frac{31}{64},\quad U_{2,1}=\frac{13}{16}\quad\text{og}\quad U_{3,1}=\frac{31}{64}.$$

Det vil si, $u(1/4,1/16)\approx U_{1,1}=31/64$, $u(1/2,1/16)\approx U_{2,1}=13/16$ og $u(3/4,1/16)=31/64$.

Kildesett: course=TMA4135 term=host year=2013 problem=6 file=tma4135_13h.pdf
