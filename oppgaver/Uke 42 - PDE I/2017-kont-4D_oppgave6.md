### **Oppgave 6**

La $u(x,t)$ være det vertikale utsvinget til en streng relativt til en horisontal $x$-akse ved tidspunkt $t$.

**a)** Anta at $0\leq x\leq L$ og at $u(0,t)=u(L,t)=0$ for alle $t\geq 0$. Tegn en figur A med figurtekst som forklarer disse antagelsene. Illustrer den geometriske tolkningen av den partiell deriverte $u'(x,t)=u_x(x,t)$ i figur A.

**b)** En vertikal linje gjennom et punkt $x$ på $x$-aksen deler strengen logisk i en venstre del og en høyre del. La $\vec{T}(x,t)$ være kraften som virker på strengens venstre del fra strengen høyre del. For en ideell streng er $\vec{T}$ en tangentvektor til strengen. Tegn en figur B med figurtekst som forklarer disse antagelsene. Vis at for en ideell streng gjelder

$$u'=\frac{F}{H}\tag{1}$$

hvor $F$ og $H$ er den vertikale og horisontale komponenten til $\vec{T}$. Illustrer ligning (1) i figur B.

**c)** Dersom strengen kun har vertikal bevegelse, så vil massen $m=\int_x^{x+\Delta x}\rho(s)\,ds$ til strengen mellom $x$ og $x+\Delta x$ ikke avhenge av tiden $t$. Forklar dette.

Det vertikale massemiddelpunktet til en bit av strengen er definert ved $\bar{u}(x,t)=m^{-1}\int_x^{x+\Delta x}\rho(s)u(s,t)\,ds$. I det følgende tas det som gitt at $m/\Delta x\to\rho$ og at $\bar{\ddot{u}}=\bar{u}_{tt}\to\ddot{u}$ når $\Delta x\to 0$.

**d)** Forklar at Newton's andre lov gir $m\ddot{u}=F(x+\Delta x,t)-F(x,t)-mg$ hvor $g$ er tyngdens akselerasjon. Gi en begrunnelse for at

$$\rho\ddot{u}=F'-\rho g\tag{2}$$

**e)** Vis at bølgeligningen

$$\ddot{u}=c^2u''-g\tag{3}$$

er en konsekvens av ligning (1) og (2). Her er $c^2=H/\rho$, $\ddot{u}=u_{tt}$ og $u''=u_{xx}$ og det antas som gitt at $H$ er konstant.
I lærebokas utledning av bølgeligningen antas det at utsvinget $u$ er lite, men denne antagelsen har vi ikke gjort her. Diskuter kort om antagelsen om et lite utsving er nødvendig i forhold til antagelsene vi har gjort over.

Kildesett: course=TMA4135 term=kont year=2017 problem=6 file=tma4135_17k.pdf
