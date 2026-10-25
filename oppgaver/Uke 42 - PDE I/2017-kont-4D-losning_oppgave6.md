### **Løsning til Oppgave 6**

**a)** og **b)** [Figur: Strengkurven $y=u(x,t)$ ved gitt $t$, festet i $(0,0)$ og $(L,0)$, med et punkt $(x,y)$ på kurven og tangentvektoren $\vec{T}$ som tangerer kurven, med vertikal komponent $F$ og horisontal komponent $H$. Oppgitt i figuren: $u'=$ stigningstall til kurven $=\frac{F}{H}$, og $y=u(x,t)$ ved gitt $t$.]

Fig. A og B: Ved et gitt tidspunkt $t$ er strengen gitt av kurven, festet i $(0,0)$ og $(L,0)$. $u'$ er stigningstallet $=\frac{F}{H}$ ved antagelse om ideell streng: $\vec{T}$ er tangent til kurven.

**c)** Ingen masse passerer $x$ eller $x+\Delta x$, så dermed er massen bevart!

**d)** Det er kun netto kraft i vertikalretning: $F(x+\Delta x)=$ kraft fra høgre del (oppover), $-F(x)=$ kraft fra venstre del, $-mg=$ tyngdekraft, og dette er lik masse $\times$ akselerasjon:

$$m\cdot\ddot{u}=F(x+\Delta x,t)-F(x,t)-mg$$

$$\frac{m}{\Delta x}\cdot\ddot{u}=\frac{F(x+\Delta x)-F(x)}{\Delta x}-\frac{m}{\Delta x}\cdot g$$

når $\Delta x\to 0$ får vi

$$\rho\ddot{u}=F'-\rho g\tag{2}$$

**e)** Vi setter $F=u'\cdot H$ inn i (2) og dividerer med $\rho$:

$$\ddot{u}=\frac{H}{\rho}\cdot u''-g\tag{3}$$

som skulle vises $\left(c^2=\frac{H}{\rho}\right)$.

I utledningen over ble det antatt at bevegelsen er rent vertikal. Dette er kun mulig for den eulerske beskrivelsen; da er (3) eksakt ✓. Dette er en approksimasjon generelt, og er gyldig ved små utsving.

Kildesett: course=TMA4135 term=kont year=2017 problem=6 file=tma4135_17k.pdf
