### **Løsning til Oppgave 6**

Vi bruker følgende approksimasjoner til de deriverte i henholdsvis $t$- og $x$-retningen:

$$u_t(x_i, t_j) \approx \frac{u(x_i, t_j + k) - u(x_i, t_j)}{k}$$

$$u_{xx}(x_i, t_j) \approx \frac{u(x_i + h, t_j) - 2u(x_i, t_j) + u(x_i - h, t_j)}{h^2}$$

[Figur: Gitter i $(x,t)$-planet for $0 \leq x \leq 1$ med fire steg av lengd $h$, tidsreta horisontale linjer med avstand $k$; venstre rand merkt $u = 1$, høgre rand merkt $u = 0$; nedre rad merkt $u = \cos(\pi x/2)$.]

Sett dette inn i differenesialligningen, og la $u_{x_i,t_j} \approx u_{i,j}$ i hvert gitterpunkt, og vi få differanseligninen

$$\frac{u_{i,j+1} - u_{i,j}}{k} = \frac{u_{i+1,j} - 2u_{i,j} + u_{i-1,j}}{h^2} + x_i$$

Løs dette med hensyn på $u_{i,j+1}$, sett inn rand- og startbetingelser, og vi får følgende eksplisitte metode:

La $u_{i,0} = 1 - x_i$, $i = 0, 1, \cdots, N$, med $N = 1/h$.

*for* $j = 0, 1, 2, 3$

$$u_{i,j+1} = u_{i,j} + \frac{k}{h^2}(u_{i+1,j} - 2u_{i,j} + u_{i-1,j}) + k\,x_i, \qquad i = 1, \cdots, N-1$$

$$u_{0,j+1} = 1, \qquad u_{N,j+1} = 1$$

*end*

Med $h = 0.25$ og $k = 0.01$ får vi at $k/h^2 = 0.16$. Startbetingelsen gir

$$u_{00} = 1.0, \quad u_{10} = 0.9239, \quad u_{20} = 0.7071, \quad u_{30} = 0.3827, \quad u_{40} = 0.0,$$

slik at

$$u(0.25, 0.01) \approx u_{11} = 0.9239 + 0.16(1.0 - 2 \cdot 0.9239 + 0.7071) + +0.01 \cdot 0.25 = 0.9039$$

$$u(0.5, 0.01) \approx u_{21} = 0.7071 + 0.16(0.9239 - 2 \cdot 0.7071 + 0.3827) + 0.01 \cdot 0.5 = 0.6949$$

$$u(0.75, 0.01) \approx u_{31} = 0.3827 + 0.16(0.7071 - 2 \cdot 0.3827 + 0) + 0.01 \cdot 0.75 = 0.3809.$$

**Kjeldevarsel:** Fleire trykkfeil i kjelda er tekne vare på ordrett over: (i) $u_{N,j+1} = 1$ skal vere $u_{N,j+1} = 0$, sidan randbetingelsen er $u(1,t) = 0$ (figuren i fasiten markerer òg $u = 0$ på høgre rand); (ii) startraden $u_{i0}$ er rekna ut frå $u(x,0) = \cos(\pi x/2)$, ikkje frå den oppgitte startbetingelsen $u(x,0) = 1 - x$ (figurtiksten $\cos(\pi x/2)$ høyrer til denne mesma varianten); (iii) det dobbelte pluss-teiknet i "+ +" i den første utrekninga. Med dei oppgitte dataa $u(x,0) = 1 - x$ blir det andre differanseleddet null i alle indre punkt, og eitt steg med $k/h^2 = 0.16$ gir $u(0.25, 0.01) = 0.75 + 0.16 \cdot 0 + 0.0025 = 0.7525$, $u(0.5, 0.01) = 0.505$ og $u(0.75, 0.01) = 0.2575$.

Kildesett: course=TMA4135 term=kont year=2006 problem=6 file=tma4135_06k.pdf
