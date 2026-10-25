### **Løsning til Oppgave 3**

**a)** Vi setter inn $u(x,t) = F(x)G(t)$ i ligningen og får

$$G''F = F''G.$$

Det følger at

$$\frac{G''}{G} = \frac{F''}{F} = k$$

der $k$ er en konstant som er uavhengig av $t$ og $x$.

Vi vil løse

$$F'' = kF \tag{L-6}$$

og vi må finne randbetingelsene for (L-6). Siden $u_x(0,t) = 0$, får vi $u_x(0,t) = F'(0)G(t) = 0$ som gir $F'(0) = 0$. På samme måten får man at $F'(\pi) = 0$.

Hvis $k > 0$, er den generelle løsningen til (L-6) gitt av

$$F(x) = Ae^{\mu x} + Be^{-\mu x}$$

der $\mu = \sqrt{k}$. Vi har $F'(x) = \mu Ae^{\mu x} - \mu Be^{-\mu x}$, og $F'(0)$ gir $A = B$ og $F'(\pi)$ gir $\mu A(e^{\mu\pi} - e^{-\mu\pi}) = 0$. Siden $\mu \neq 0$, dette fører til at $A = 0$ og vi får den trivielle løsningen $u(x,t) = 0$.

Hvis $k = 0$, er den generelle løsningen til (L-6) gitt av

$$F(x) = Ax + B$$

Vi har $F'(x) = A$. Derfor $F'(0)$ gir $A = 0$ og da har vi også at $F'(\pi) = 0$. Derfor er $F(x) = B$ en løsning til (L-6).

Hvis $k < 0$, er den generelle løsningen til (L-6) gitt av

$$F(x) = A\cos(\mu x) + B\sin(\mu x)$$

der $\mu = \sqrt{-k}$. Vi har $F'(x) = -\mu A\sin(\mu x) + \mu B\cos(\mu x)$. Derfor $F'(0)$ gir $B = 0$ og $F'(\pi) = 0$ medfører at

$$\mu B \sin(\mu\pi) = 0$$

Siden $\mu \neq 0$, får vi at $\sin(\mu\pi) = 0$ det vil si at $\mu = n$ og $k = -n^2$ for $n = 1, 2, \ldots$

Nå løser vi ligningen

$$G''(t) = kG(t)$$

For $k = 0$ får vi

$$G(t) = Bt + A.$$

For $k = -n^2$ får vi

$$G(t) = A\cos(nt) + B\sin(nt)$$

Løsningene av den form $u(x,t) = F(x)G(t)$ er

$$u_0(x,t) = B_0 t + A_0$$

og

$$u_n(x,t) = (A_n \cos(nt) + B_n \sin(nt)) \cos(nx). \tag{L-7}$$

**b)** Vi tar to løsninger $u$ og $v$ av (1) og (2). La $w(x,t) = au(x,t) + bv(x,t)$ for to vilkårlige konstanter $a$ og $b$. Ligninen (1) med randbetingelse (2) tilfredstiller superposisjonsprinsippet hvis $w$ er også en løsning. Vi har

$$\begin{aligned} w_{tt} &= au_{tt} + bv_{tt} \\ &= au_{xx} + bv_{xx} \ \text{siden } u \text{ og } v \text{ er løsninger til (1)} \\ &= aw_{xx} \end{aligned}$$

og $w$ er en løsning til (1). Vi har også at

$$w_x(0,t) = au_x(0,t) + bv_x(0,t) = 0$$

og

$$w_x(\pi,t) = au_x(\pi,t) + bv_x(\pi,t) = 0.$$

Derfor $w$ er en løsning til (1) og (2) og vi har vist at systemet som består av ligningen (1) og randbetingelsene (2) tilfredstiller superposisjonsprinsippet.

Ved å bruke superposisjonsprinsippet, får man den generelle løsningen til (1)-(2) som er gitt av

$$u(x,t) = A_0 t + B_0 + \sum_{n=1}^{\infty} (B_n \cos(nt) + A_n \sin(nt)) \cos(nx).$$

Vi må bestemme $A_n$ og $B_n$ slik at $u$ tilfredstiller startbetingelsene

$$u(x,0) = \cos^2(x) \tag{L-8}$$

og

$$u_t(x,0) = \cos(3x). \tag{L-9}$$

Vi har

$$u(x,0) = B_0 + \sum_{n=1}^{\infty} B_n \cos(nx) = \cos^2(x)$$

På venstre siden har vi Cosinusrekken til $u(x,0)$. Siden $\cos^2(x) = \frac{1}{2} + \frac{\cos(2x)}{2}$, får vi at

$$B_0 = \frac{1}{2}, \ B_2 = \frac{1}{2} \ \text{og} \ B_n = 0 \ \text{hvis} \ n \neq 0, 2.$$

Vi har

$$u_t(x,t) = A_0 + \sum_{n=1}^{\infty} (-nB_n \sin(nt) + nA_n \cos(nt)) \cos(nx)$$

som gir

$$u_t(x,0) = A_0 + \sum_{n=1}^{\infty} nA_n \cos(nx) = \cos(3x)$$

På venstre siden har vi nå Cosinusrekken til $u_t(x,0)$ og det fører til at

$$A_3 = \frac{1}{3}.$$

Til slutt får man løsningen

$$u(x,t) = \frac{1}{2} + \frac{1}{2} \cos(2t) \cos(2x) + \frac{1}{3} \sin(3t) \cos(3x).$$

*Kjeldevarsel: LF-en trykkjer «Ligninen» og «tilfredstiller» fleire stader (retta «ligningen»/«tilfredsstiller») og har «der $F'(\pi) = 0$ medfører at $\mu B \sin(\mu\pi) = 0$» — etter $B = 0$ er $\mu B\sin(\mu\pi) = 0$ identisk oppfylt, meininga er $\mu A\sin(\mu\pi)$-vilkåret frå $F'(\pi) = 0$ med $F = \cos(\mu x)$, dvs. $\sin(\mu\pi) = 0$ som brukt vidare; sluttsvar og rest er konsistente. Alt spel av ordrett.*

Kildesett: course=TMA4125 term=var year=2008 problem=3 file=eksamen-bok_2008v.pdf
