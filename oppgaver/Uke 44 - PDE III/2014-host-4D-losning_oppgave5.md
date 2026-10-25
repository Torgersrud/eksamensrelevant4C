### **Løsning til Oppgave 5**

**a)** Setter vi inn $u(x,t)=F(x)G(t)$ i PDE-en i oppgaven får vi

$$F(x)G'(t)=F''(x)G(t)-F(x)G(t),$$

som etter omforming blir

$$\frac{F''(x)}{F(x)}-1=\frac{G'(t)}{G(t)}.$$

Siden ligningen holder for alle $x$ og $t$, og venstre side ikke avhenger av $t$ mens høyre side ikke avhenger av $x$, må begge sider være lik en konstant $k$. Vi får da to ODE-er:

$$F''(x)-(1+k)F(x)=0\tag{1}$$

$$G'(t)-kG(t)=0.\tag{2}$$

Løsningen av ligning (1) kan ha tre former, avhengig av hva $k$ er:

1. Dersom $k>-1$, er løsningen på formen

$$F(x)=Ae^{\sqrt{1+k}x}+Be^{-\sqrt{1+k}x}.$$

Randbetingelsen $u(0,t)=0$ gir $F(0)=0$, som gir $A=-B$, altså $F(x)=A(e^{\sqrt{1+k}x}-e^{-\sqrt{1+k}x})$. Randbetingelsen $u(1,t)=0$ gir $F(1)=0$, altså $A=0$ og triviell løsning.

2. Dersom $k=-1$, er løsningen på formen

$$F(x)=Ax+B.$$

Randbetingelsen $u(0,t)=0$ gir $F(0)=0$, som gir $B=0$. Randbetingelsen $u(1,t)=0$ gir $F(1)=0$, altså $A=0$ og triviell løsning.

3. Dersom $k<-1$, er løsningen på formen

$$F(x)=C\cos px+D\sin px,$$

hvor vi har definert $p=\sqrt{-(k+1)}$. Randbetingelsen $u(0,t)$ gir $F(0)=0$, som gir $C=0$ og $F(x)=D\sin px$. Randbetingelsen $u(1,t)=0$ gir $0=F(1)=D\sin p$. For at vi ikke skal ha triviell løsning, har vi bare mulighetene $p=n\pi$ for $n=1,2,3,\ldots$ (og $p=-\pi,-2\pi,\ldots$, men siden sinus er odde kan vi la konstanten $D$ ta hånd om disse).

Ligning (1) har altså løsninger på formen

$$F_n(x)=D_n\sin n\pi x$$

for $n=1,2,3,\ldots$. Siden $n\pi=\sqrt{-(k+1)}$, blir ligning (2)

$$G'(t)+(1+n^2\pi^2)G(t)=0.$$

Denne har løsninger på formen

$$G_n(t)=C_ne^{-(1+n^2\pi^2)t}.$$

De ikke-trivielle løsningene på oppgavens PDE er altså

$$u_n(x,t)=F_n(x)G_n(t)=A_ne^{-(1+n^2\pi^2)t}\sin n\pi x$$

for $n=1,2,3,\ldots$.

**b)** Den generelle løsningen fra deloppgave 5a er

$$u(x,t)=\sum_{n=1}^{\infty}A_ne^{-(1+n^2\pi^2)t}\sin n\pi x.$$

Vi har da

$$\sin\pi x\cos\pi x=u(x,0)=\sum_{n=1}^{\infty}A_n\sin n\pi x$$

Høyre side er altså *Fourier-sinus-rekken* til funksjonen på venstre side. Vi kan derfor regne ut $A_1,A_2,\ldots$ ved hjelp av de vanlige integralene, eller vi kan spare oss tid ved å bruke dobbelvinkelsetningene til å skrive $\sin(\pi x)\cos(\pi x)=\sin(2\pi x)/2$, slik at

$$\frac{1}{2}\sin 2\pi x=\sum_{n=1}^{\infty}A_n\sin n\pi x.$$

Da er venstre side allerede en sinusrekke, og vi kan derfor lese av koeffisientene direkte: $A_2=1/2$ og $A_n=0$ for alle $n\neq 2$. Dermed er løsningen som tilfredsstiller den gitte initialbetingelsen

$$u(x,t)=\frac{1}{2}e^{-(1+4\pi^2)t}\sin 2\pi x.$$

**c)** Fremoverdifferens i tid er tilnærmingen

$$\frac{\partial u}{\partial t}(ih,jk)\approx\frac{1}{k}(U_{i,j+1}-U_{i,j})$$

og sentraldifferens i rom er tilnærmingen

$$\frac{\partial^2u}{\partial x^2}(ih,jk)\approx\frac{1}{h^2}(U_{i+1,j}-2U_{i,j}+U_{i-1,j}).$$

Vi får da skjemaet

$$\frac{1}{k}(U_{i,j+1}-U_{i,j})=\frac{1}{h^2}(U_{i+1,j}-2U_{i,j}+U_{i-1,j})-U_{i,j}.$$

Med $h=1/4$ og $k=1/32$, er $j\ge 0$ og $1\le i\le 3$, og skjemaet blir

$$U_{i,j+1}=\frac{1}{2}(U_{i+1,j}+U_{i-1,j})-\frac{1}{32}U_{i,j}.$$

For $i=3$ og $j=0$ finner vi

$$\begin{aligned}U_{3,1}&=\frac{1}{2}(U_{4,0}+U_{2,0})-\frac{1}{32}U_{3,0}\\
&=\frac{1}{2}\left(\sin\left(\pi\frac{4}{4}\right)\cos\left(\pi\frac{4}{4}\right)+\sin\left(\pi\frac{2}{4}\right)\cos\left(\pi\frac{2}{4}\right)\right)-\frac{1}{32}\sin\left(\pi\frac{3}{4}\right)\cos\left(\pi\frac{3}{4}\right)\\
&=\frac{1}{64},\end{aligned}$$

og

$$u(3/4,1/32)=\frac{1}{2}e^{-(1+4\pi^2)/32}\sin\left(\frac{3}{2}\pi\right)=-\frac{1}{2}e^{-(1+4\pi^2)/32}\approx-0.1411.$$

Avviket vi ble bedt om å finne er altså $1/64+e^{-(1+4\pi^2)/32}/2\approx 0.1568$.

Kildesett: course=TMA4135 term=host year=2014 problem=5 file=tma4135_14h.pdf
