### **Oppgave 9**

Gitt den partielle differensialligningen

$$
\begin{aligned}
u_t&=\kappa u_{xx}+x(1-x), &&(t>0,\quad 0<x<1),\\
u(0,t)&=u(1,t)=0, &&(t>0),\\
u(x,0)&=\sin(\pi x), &&(0<x<1).
\end{aligned}
$$

Bruk et gitter bestående av punktene $t_j=jk$ og $x_i=ih$, $h=1/N$, og sett opp et eksplisitt differanseskjema for denne ligningen, det vil si, bruk en sentraldifferanse for å approksimere $u_{xx}$ og en foroverdifferanse for å approksimere $u_t$.

La $\kappa=0.1$. Sett $h=0.25$ og $k=0.2$, og finn tilnærmelser til $u(0.25,0.2)$, $u(0.5,0.2)$ og $u(0.75,0.2)$.

*Kjeldevarsel: 4D-søstra 2010-host-4D_oppgave9 har same oppgåve, men trykt med fleirtal «bruk sentraldifferanser» (her eintal «bruk en sentraldifferanse») og $\sin\pi x$ utan parentes (her $\sin(\pi x)$) — difor ikkje fulltekst-identisk og ikkje dup.*

Kildesett: course=TMA4130 term=host year=2010 problem=9 file=eksamen-bok_2010.pdf
