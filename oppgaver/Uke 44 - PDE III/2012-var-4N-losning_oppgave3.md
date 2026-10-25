### **Løsning til Oppgave 3**

**a)** (Dette punktet teller dobbelt).

Separasjon av variable:

$$u(x,t)=F(x)G(t)$$

som innsatt i ligningen gir

$$F\cdot\ddot{G}=4F''\cdot G\qquad\Rightarrow\qquad\frac{F''}{F}=\frac{1}{4}\frac{\ddot{G}}{G}=k$$

for en foreløbig helt ukjent konstant $k$. I tillegg har vi at

$$u_x(0,t)=0,\qquad u(2,t)=0\qquad\Rightarrow\qquad F'(0)=0,\quad F(2)=0. \tag{1}$$

Løser ligningen

$$F''=kF \tag{2}$$

som har tre mulige løsninger:

- $k=\lambda^2>0$:

  $$F(x)=Ce^{\lambda x}+De^{-\lambda x}\qquad\text{og dermed}\qquad F'(x)=C\lambda e^{\lambda x}-D\lambda e^{-\lambda x}.$$

  Setter inn randbetingelsene:

  $$F'(0)=0\quad\Rightarrow\quad C-D=0$$
  $$F(2)=0\quad\Rightarrow\quad Ce^{2}+De^{-2}=0\quad\Rightarrow\quad C(e^{2}-e^{-2})=0$$
  $$\Rightarrow\quad C=D=0.$$

  og $F(x)=0$ (triviell løsning)

- $k=0$:

  $$F(x)=C+Dx\qquad\text{og dermed}\qquad F'(x)=D.$$

  Setter inn randbetingelsene:

  $$F'(0)=0\quad\Rightarrow\quad D=0$$
  $$F(2)=0\quad\Rightarrow\quad 2C=0$$

  og $F(x)=0$ (triviell løsning).

- $k=-\alpha^2<0$:

  $$F(x)=A\cos(\alpha x)+B\sin(\alpha x)\qquad\text{og dermed}\qquad F'(x)=-A\alpha\sin(\alpha x)+B\alpha\cos(\alpha x).$$

  Setter inn randbetingelsene og får:

  $$F'(0)=0\quad\Rightarrow\quad B\alpha=0$$
  $$F(2)=0\quad\Rightarrow\quad A\cos(\alpha\cdot 2)=0\quad\Rightarrow\quad 2\alpha=(n+\tfrac{1}{2})\pi,\quad n=0,1,2,\ldots.$$

Så alle mulige løsninger av (2) og (1) er på formen $F(x)=\cos(\alpha_n x)$ med $\alpha_n=(2n+1)\pi/4$.

Løser nå ligningen ($k=-\alpha_n^2$):

$$\ddot{G}=-4\alpha_n^2 G$$

som har løsningene:

$$G(t)=A_n\cos(2\alpha_n t)+B_n\sin(2\alpha_n t).$$

Vi får da at alle løsninger av (1a) og (1b) på formen $G(t)F(x)$ er gitt ved

$$A_n\cos(2\alpha_n t)\cos(\alpha_n x)\quad\text{og}\quad B_n\sin(2\alpha_n t)\cos(\alpha_n x),\qquad \alpha_n=\frac{(2n+1)\pi}{4},\quad n=0,1,2,\ldots$$

for vilkårlige konstanter $A_n$ og $B_n$, men med Den generelle løsningen er

$$u(x,t)=\sum_{n=0}^{\infty}\big(A_n\cos(2\alpha_n t)\cos(\alpha_n x)+B_n\sin(2\alpha_n t)\cos(\alpha_n x)\big)$$

og dermed

$$u_t(x,t)=\sum_{n=0}^{\infty}\big(-A_n 2\alpha_n\sin(2\alpha_n t)\cos(\alpha_n x)+B_n 2\alpha_n\cos(2\alpha_n t)\cos(\alpha_n x)\big)$$

Fra startbetingelsen $u_t(x,0)=0$ får vi at $B_n=0$, slik at

$$u(x,0)=\sum_{n=0}^{\infty}A_n\cos(\alpha_n x)=A_0\cos\Big(\frac{\pi}{4}x\Big)+A_1\cos\Big(\frac{3\pi}{4}x\Big)+A_2\cos\Big(\frac{5\pi}{4}x\Big)+\cdots.$$

Ved å sammenligne med den oppgitte startbetingelsen $u(x,0)=2\cos(\pi x/4)+\cos(5\pi x/4)$ ser vi at $A_0=3$, $A_2=1$ og $A_n=0$ for $n\neq 0,2$. Løsningen blir dermed

$$u(x,t)=3\cos\Big(\frac{\pi t}{2}\Big)\cos\Big(\frac{\pi x}{4}\Big)+\cos\Big(\frac{5\pi t}{2}\Big)\cos\Big(\frac{5\pi x}{4}\Big).$$

**b)** Vi har oppgitt at $v(x,t)=u(x,t)+g(x)$, slik at $v_{tt}=u_{tt}$ og $v_{xx}=u_{xx}+g_{xx}$. Sett dette inn i ligningen,

$$u_{tt}=u_{xx}+g\_xx,\qquad u_x(0,t)+g_x(0)=1,\qquad u(2,t)+g(2)=0.$$

Siden $u(x,t)$ er en løsning av (1a), (1b) i punkt **a)**, må $g(x)$ tilfredstille

$$g_{xx}=0,\qquad g_x(0)=-1,\quad g(2)=0,$$

slik at

$$g(x)=2-x.$$

Den generelle løsningen av dette problemet er gitt ved $v=u+g$, eller, som vi setter inn den generelle løsningen $u(x,t)$ fra **a)**

$$v(x,t)=\sum_{n=0}^{\infty}\big(A_n\cos(2\alpha_n t)\cos(\alpha_n x)+B_n\sin(2\alpha_n t)\cos(\alpha_n x)\big)+2-x.$$

Siden $v_t(x,0)=0$ må $B_n=0$. Siden $v(x,0)=0$ må

$$\sum_{n=0}^{\infty}A_n\cos(\alpha_n x)=A_0\cos\Big(\frac{\pi x}{4}\Big)+A_1\cos\Big(\frac{3\pi x}{4}\Big)+A_2\cos\Big(\frac{5\pi x}{4}\Big)+\cdots \tag{3}$$

$$=-g(x)=x-2,$$

der $\alpha_n=(2n+1)\pi/4$. Vi trenger altså å uttrykke $x-2$ for $0<x<2$ som en cosinusrekke, og gjennom det finne et uttrykk for $A_n$. Sagt på en annen måte: Vi trenger en periodisk, like utvidelse av -g(x), la oss kalle den $h(x)$, slik at

$$h(x)=a_0+\sum_{m=1}^{\infty}a_m\cos\Big(\frac{m\pi x}{L}\Big)$$

og

$$h(x)=2-x\ \text{for}\ 0<x<2.$$

Ved å sammenligne dette med (3) kan vi trekke følgende konklusjoner:

1. $L=4$ (periode 8).
2. $a_0=0$, dvs. $\int_0^4 h(x)dx=0$.
3. $a_m=0$ når $m$ er et partall.

Skissen under viser hvordan $h(x)$ kan se ut, dvs. at $h(x)$ er den like, 8-periodiske utvidelsen av funksjonen $x-2$, $0<x<4$.

[Figur: koordinataksar med $x$-akse merket $-4$, $-2$, $0$, $2$, $4$ og $y$-akse merket $2$ og $-2$. Den blå kurva $h(x)$ er ein like, tannhjulsforma sigeinkurve av rette linjestykke mellom $(0,-2)$, $(\pm2,0)$ og $(\pm4,2)$; den raude kurva er linjestykket frå $(0,-2)$ til $(2,0)$, merkt $-g(x)$.]

Dette valget av $h(x)$ tilfredstiller også

$$a_m=\frac{1}{2}\int_0^4 (x-2)\cos\Big(\frac{m\pi x}{4}\Big)dx=0\ \text{for}\ m\ \text{partall}$$

fordi bidraget til integralet fra 0 til 2 er like stort, men med motsatt fortegn som bidraget fra 2 til 4. Setter vi helt til sist $m=2n+1$ får vi rekka (3) med

$$A_n=a_{2n+1}=\frac{1}{2}\int_0^4 (x-2)\cos\frac{(2n+1)\pi x}{4}dx.$$

*Kjeldevarsel: Fleire trykkfeil i LF er bevarte ordrett: (i) I tilfellet $k=\lambda^2>0$ er faktoren trykt som $C(e^{2}-e^{-2})=0$; med $D=C$ frå fyrste betingelse følgjer $C(e^{2}+e^{-2})=0$ — konklusjonen $C=D=0$ er rett uansett. (ii) Setninga «for vilkårlige konstanter $A_n$ og $B_n$, men med Den generelle løsningen er» er øydelagd i kjelda. (iii) Startbetingelsen er gjenteken som $u(x,0)=2\cos(\pi x/4)+\cos(5\pi x/4)$; oppgåva seier $3\cos(\pi x/4)$, og $A_0=3$ krev også 3. (iv) Innsettinga i b) er trykt som $u_{tt}=u_{xx}+g\_xx$ og $u_x(0,t)+g_x(0)=1$ — med $v_{tt}=4v_{xx}$ og $v_x(0,t)=-1$ skal det vere høvesvis $u_{tt}=4u_{xx}+4g_{xx}$ og $=-1$, slik LF sjølv brukar det i betingelsene for $g$ like etter. (v) Linja $h(x)=2-x$ for $0<x<2$ er i strid med figuren, $a_m$-integralet og rekkja (3), som alle bruker $-g(x)=x-2$. Løysinga er kontrollert med sympy: $u_{tt}-4u_{xx}\equiv 0$, start- og randvilkåra er oppfylte, $g(x)=2-x$ oppfyller vilkåra i b), og rekkjekoeffisientane har sluttformen $A_n=-\frac{16}{(2n+1)^2\pi^2}$ som konvergerer mot $x-2$ på prueba punkt.*

Kildesett: course=TMA4125 term=var year=2012 problem=3 file=tma4123_25_v12.pdf
