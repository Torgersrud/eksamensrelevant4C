### **Løsning til Oppgave 3**

**a)** Fourierrekken til $f$ svarer til fouriercosinusrekken til $g$, der

$$a_0=\int_0^1\sin\pi x\,\mathrm{d}x=\left[-\frac{1}{\pi}\cos\pi x\right]_0^1=\frac{2}{\pi},$$

$$a_1=2\int_0^1\sin\pi x\cos\pi x\,\mathrm{d}x=\int_0^1\sin 2\pi x\,\mathrm{d}x=0,$$

og

$$\begin{aligned}a_n&=2\int_0^1\sin\pi x\cos n\pi x\,\mathrm{d}x\\
&=\int_0^1\big(\sin(1-n)\pi x+\sin(1+n)\pi x\big)\,\mathrm{d}x\\
&=\left[\frac{1}{(n-1)\pi}\cos(1-n)\pi x-\frac{1}{(n+1)\pi}\cos(1+n)\pi x\right]_0^1\\
&=-\frac{2}{\pi}\frac{1}{n^2-1}+\frac{1}{(n-1)\pi}\cos(1-n)\pi-\frac{1}{(n+1)\pi}\cos(1+n)\pi\\
&=\begin{cases}-\frac{4}{\pi}\frac{1}{n^2-1}&\text{for}\quad n=2,4,6,\ldots\\ 0&\text{for}\quad n=3,5,7,\ldots\end{cases}\end{aligned}$$

der vi har benyttet at $2\sin\alpha x\cos\beta x=\sin(\alpha-\beta)x+\sin(\alpha+\beta)x$ (se også side 88 i formsamlingen).

Altså er fourierrekken til $f$ gitt ved

$$\frac{2}{\pi}-\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{\cos 2n\pi x}{4n^2-1}\,.$$

**b)** Innsatt for $u(x,t)=F(x)G(t)$ i $u_t(x,t)=u_{xx}(x,t)$ får vi

$$F(x)\dot{G}(t)=F''(x)G(t).$$

Det vil si,

$$\underbrace{\frac{F''(x)}{F(x)}}_{k}=\underbrace{\frac{\dot{G}(t)}{G(t)}}_{k},$$

som gir to ordinære differensialligninger

$$F''(x)-kF(x)=0\tag{3}$$

$$\dot{G}(t)-kG(t)=0\tag{4}$$

Randbetingelsene $u_x(0,t)=u_x(1,t)=0$ for $t\ge 0$ gir at

$$F'(0)=F'(1)=0.\tag{5}$$

Vi har tre muligheter for konstanten $k$: (i) $k>0$, (ii) $k=0$ og (iii) $k<0$.

(i) Innsatt for $k=\mu^2>0$ i (3) får vi $F''(x)-\mu^2F(x)=0$ som har løsning $F(x)=Ae^{\mu x}+Be^{-\mu x}$. Fra (5) kan vi slutte at $A=B=0$, og dermed at $F(x)=0$, som kun gir den trivielle løsningen $u(x,t)=0$.

(ii) Innsatt for $k=0$ i (3) får vi $F''(x)=0$ som har løsning $F(x)=Ax+B$. Fra (5) kan vi slutte at $A=0$, og dermed at $F(x)=B$ (der $B$ kan være forskjellig fra 0).

Innsatt for $k=0$ i (4) får vi $\dot{G}(t)=0$ som har løsning $G(t)=C$.

Altså gir $k=0$ løsningen

$$u(x,t)=F(x)G(t)=A_0,$$

der $A_0=BC$.

(iii) Innsatt for $k=-p^2<0$ i (3) får vi $F''(x)+p^2F(x)=0$ som har løsning $F(x)=A\cos px+B\sin px$. Fra $F'(0)=0$ får vi at $B=0$. Fra $F'(1)=0$ får vi at $A=0$ eller $p=n\pi$ for $n=1,2,3,\ldots$ Tilfellet $A=0$ gir kun den trivielle løsningen $u(x,t)=0$. Altså har vi at

$$F_n(x)=\tilde{A}_n\cos n\pi x$$

for $n=1,2,3,\ldots$

Innsatt for $k=-n^2\pi^2$ i (4) får vi $\dot{G}(t)+n^2\pi^2G(t)=0$ som har løsning

$$G_n(t)=C_ne^{-n^2\pi^2t}$$

for $n=1,2,3,\ldots$

Altså gir $k<0$ løsningen

$$u_n(x,t)=F_n(x)G_n(t)=A_n\cos n\pi x\,e^{-n^2\pi^2t},$$

for $n=1,2,3,\ldots$ og der $A_n=\tilde{A}_nC_n$.

Ved å kombinere (ii) og (iii) sitter vi igjen med at de ikke-trivielle løsningene er gitt ved

$$u_n(x,t)=A_n\cos n\pi x\,e^{-n^2\pi^2t}$$

for $n=0,1,2,\ldots$

**c)** La

$$u(x,t)=\sum_{n=0}^{\infty}u_n(x,t)=\sum_{n=0}^{\infty}A_n\cos n\pi x\,e^{-n^2\pi^2t}\,.$$

Fra $u(x,0)=\sin\pi x$ for $0\le x\le 1$ får vi

$$u(x,0)=\sum_{n=0}^{\infty}A_n\cos n\pi x=\sin\pi x.$$

Altså er $A_n$ fourierkoeffisientene til fouriercosinusrekken til $\sin\pi x$. Fra **a)** vet vi at

$$A_0=\frac{2}{\pi},\quad A_{2n-1}=0\quad\text{og}\quad A_{2n}=-\frac{4}{\pi}\frac{1}{4n^2-1}$$

for $n=1,2,3,\ldots$ Det gir

$$u(x,t)=\frac{2}{\pi}-\frac{4}{\pi}\sum_{n=1}^{\infty}\frac{\cos 2n\pi x}{4n^2-1}e^{-4n^2\pi^2t}.$$

Kildesett: course=TMA4135 term=host year=2013 problem=3 file=tma4135_13h.pdf
