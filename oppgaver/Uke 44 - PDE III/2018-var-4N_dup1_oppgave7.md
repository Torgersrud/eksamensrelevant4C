### **Oppgave 7**

La $u(x,t)$ være utslaget ved tidspunkt $t$ og posisjon $x$ av en vibrerende streng av lengde 4. Den oppfyller bølgeligningen

$$\frac{\partial^2 u}{\partial t^2}=\frac{\partial^2 u}{\partial x^2},\quad 0\leq x\leq 4,\quad t\geq 0,$$

med startverdier

$$u(x,0)=3\sin(\pi x)\quad\text{og}\quad u_t(x,0)=\sin(4\pi x),\quad 0\leq x\leq 4,$$

og grensebetingelser

$$u(0,t)=u(4,t)=0,\quad t\geq 0.$$

**a)** Finn alle løsninger av bølgeligningen på formen $u(x,t)=F(x)G(t)$ som oppfyller grensebetingelsene.

**b)** Finn løsningen som også oppfyller startbetingelsene.

**c)** Sett opp et numerisk differanseskjema for ligningen, etter følgende retningslinjer:

Bruk steglengder $\Delta t$ og $\Delta x$ i henholdsvis $t-$ og $x-$retningen, der $\Delta x=4/M$, og $M$ er antall intervaller i $x-$retningen. Gitterpunktene er da gitt ved $t_n=n\Delta t$, $n=0,1,2,\ldots$ og $x_i=i\Delta x$, $i=0,1,\ldots,M$ La $U_i^n\approx u(x_i,t_n)$ være den numeriske tilnærmelsen i hvert gitterpunkt.

- Sett opp et endelig differanseskjema for ligningen, basert på sentraldifferanser. Skjemaet blir eksplisitt, det vil si at tilnærmelsen $U_i^{n+1}$ kan uttrykkes ved hjelp av de numeriske løsningene i tidspunkt $t_n$ og $t_{n-1}$ for $n\geq 1$.
- Bruk deretter en sentraldifferanse for $u_t(x,0)$ og ideen med en falsk rand for å finne et skjema for å beregne $U_i^1$, $i=1,\ldots,M-1$.
- La $\Delta x=0.1$ og $\Delta t=0.1$ og bruk disse skjemaene til å beregne $U_1^2\approx u(0.1,0.2)$.

Kildesett: course=TMA4135 term=var year=2018 problem=7 file=tma4125_final_exam_may_bm.pdf
