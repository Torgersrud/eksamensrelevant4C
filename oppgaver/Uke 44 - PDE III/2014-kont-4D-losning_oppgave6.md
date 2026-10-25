### **Løsning til Oppgave 6**

**a)** Innsatt for $u(x,t)=F(x)G(t)$ i $u_{xx}(x,t)-u_{tt}(x,t)-2u_t(x,t)-u(x,t)=0$ får vi

$$F''(x)G(t)-F(x)\ddot{G}(t)-2F(x)\dot{G}(t)-F(x)G(t)=0.$$

Det vil si,

$$\underbrace{\frac{F''(x)}{F(x)}}_{k}=\underbrace{\frac{\ddot{G}(t)+2\dot{G}+G(t)}{G(t)}}_{k},$$

som gir to ordinære differensialligninger

$$F''(x)-kF(x)=0\tag{2}$$

$$\ddot{G}(t)+2\dot{G}(t)+(1-k)G(t)=0.\tag{3}$$

Randbetingelsene $u(0,t)=0$ og $u(\pi,t)=0$ for alle $t$ gir at

$$F(0)=F(\pi)=0.\tag{4}$$

Vi har tre muligheter for konstanten $k$: (i) $k>0$, (ii) $k=0$ og (iii) $k<0$.

(i) Innsatt for $k=\mu^2>0$ i (2) får vi $F''(x)-\mu^2F(x)=0$ som har løsning $F(x)=Ae^{\mu x}+Be^{-\mu x}$. Fra (4) kan vi slutte at $A=B=0$, og dermed at $F(x)=0$, som kun gir den trivielle løsningen $u(x,t)=0$.

(ii) Innsatt for $k=0$ i (2) får vi $F''(x)=0$ som har løsning $F(x)=Ax+B$. Fra (4) kan vi slutte at $A=B=0$, og dermed at $F(x)=0$, som kun gir den trivielle løsningen $u(x,t)=0$.

(iii) Innsatt for $k=-p^2<0$ i (2) får vi $F''(x)+p^2F(x)=0$ som har løsning $F(x)=A\cos px+B\sin px$. Fra $F(0)=0$ får vi at $A=0$. Fra $F(\pi)=0$ får vi at $B=0$ eller $p=n=1,2,3,\dots$. Tilfellet $B=0$ gir kun den trivielle løsningen $u(x,t)=0$. Altså har vi at

$$F_n(x)=\hat{B}_n\sin nx$$

for $n=1,2,3,\dots$. Innsatt for $k=-n^2$ i (3) får vi $\ddot{G}(t)+2\dot{G}(t)+(1+n^2)G(t)=0$ som har løsning

$$G_n(t)=\hat{A}_ne^{-t}\cos nt+\hat{B}_ne^{-t}\sin nt$$

for $n=1,2,3,\dots$ der vi har gjort bruk av vinket gitt i oppgaven.

Altså gir $k<0$ den ikke-trivielle løsningen

$$u_n(x,t)=F_n(x)G_n(t)=(A_ne^{-t}\cos nt+B_ne^{-t}\sin nt)\sin nx$$

for $n=1,2,3,\dots$ og der $A_n=\tilde{B}_n\hat{A}_n$ og $B_n=\tilde{B}_n\hat{B}_n$.

**b)** La

$$u(x,t)=\sum_{n=1}^\infty u_n(x,t)=\sum_{n=1}^\infty\left(A_ne^{-t}\cos nt+B_ne^{-t}\sin nt\right)\sin nx.$$

Fra $u(x,0)=0$ får vi

$$u(x,0)=\sum_{n=1}^\infty A_n\cos nx=0,$$

slik at $A_n=0$ for $n=1,2,3,\dots$. Dermed er

$$u(x,t)=\sum_{n=1}^\infty B_ne^{-t}\sin nt\sin nx$$

slik at

$$u_t(x,t)=\sum_{n=1}^\infty B_n(n\cos nt-\sin nt)e^{-t}\sin nx.$$

Fra $u_t(x,0)=2\sin x-\sin 2x$ får vi

$$u_t(x,0)=\sum_{n=1}^\infty nB_n\sin nx=B_1\sin x+2B_2\sin 2x+\cdots=2\sin x-\sin 2x.$$

Det vil si, $B_1=2$, $B_2=-1/2$ og $B_n=0$ for $n=3,4,5,\dots$. Det gir

$$u(x,t)=2e^{-t}\sin t\sin x-\frac{1}{2}e^{-t}\sin 2t\sin 2x.$$

Kildesett: course=TMA4135 term=kont year=2014 problem=6 file=tma4135_14k.pdf
