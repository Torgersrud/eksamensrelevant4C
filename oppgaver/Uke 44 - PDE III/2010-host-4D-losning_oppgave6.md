### **Løsning til Oppgave 6**

a)  Setter inn $u(x,t)=F(x)G(t)$ i $u_t=u_{xx}+2u$. Det gir

$$F(x)\dot{G}(t)=F''(x)G(t)+2F(x)G(t)\quad\text{det vil si}\quad F''(x)G(t)=F(x)\big(\dot{G}(t)-2G(t)\big),$$

slik at

$$\underbrace{\frac{F''(x)}{F(x)}}_{k}=\underbrace{\frac{\dot{G}(t)-2G(t)}{G(t)}}_{k}.$$

Dette gir følgende to 2. ordens ordinære differensialligninger

$$F''(x)-kF(x)=0,\qquad(1)$$

$$\dot{G}(t)-(k+2)G(t)=0.\qquad(2)$$

Løser så (1), gitt randbetingelsene $u_x(0,t)=0$ og $u_x(\pi,t)=0$, det vil si $F'(0)=0$ og $F'(\pi)=0$. Med andre ord,

$$F''(x)-kF(x)=0,\qquad F'(0)=0,\quad F'(\pi)=0.\qquad(1')$$

Vi har tre muligheter for $k$:

(i)  $k=p^2>0$: Innsatt for $k=p^2$ i $(1')$ får vi

$$F''(x)-p^2F(x)=0.$$

Denne ligningen har løsning

$$F(x)=Ae^{px}+Be^{-px}.$$

Ettersom

$$F'(x)=p\big(Ae^{px}-Be^{-px}\big),$$

gir $F'(0)=0$ at $A=B$. Fra $F'(\pi)=0$ får vi

$$F'(\pi)=Ap(e^{p\pi}-e^{-p\pi})=2Ap\sinh p\pi=0.$$

Altså må $A=0$. Dermed står vi kun igjen med den trivielle løsningen $u(x,t)=0$. Altså er $k\le 0$.

(ii)  $k=0$: Innsatt for $k=0$ i $(1')$ får vi

$$F''(x)=0,$$

som har løsning $F(x)=Ax+B$. Fra $F'(0)=0$ og $F'(\pi)=0$ får vi $A=0$. Altså står vi igjen med løsningen $F(x)=$ konstant.

(iii)  $k=-p^2<0$: Innsatt for $k=-p^2$ i $(1')$ får vi

$$F''(x)+p^2F(x)=0,$$

som har løsning

$$F(x)=A\cos px+B\sin px.$$

Ettersom

$$F'(x)=p\big(B\cos px-A\sin px\big),$$

får vi at $F'(0)=Bp=0$, det vil si $B=0$. Altså har vi at $F(x)=A\cos px$. Fra $F'(\pi)=0$, får vi

$$F'(\pi)=-pA\sin p\pi=0.$$

Ettersom $A=0$ kun gir den trivielle løsningen $u(x,t)=0$, ser vi på tilfellet der $\sin p\pi=0$. Det gir $p=n=1,2,3,\ldots$. Altså er $k=-n^2$.

Ved å kombinere (ii) og (iii) har vi funnet at alle mulige løsninger for $(1')$, gitt våre randbetingelser, er på formen

$$F_n(x)=\tilde{A}_n\cos nx,\qquad n=0,1,2,\ldots$$

Setter så inn for $k=-n^2$ i (2). Det gir

$$\dot{G}(t)+(n^2-2)G(t)=0\quad\text{det vil si}\quad\dot{G}(t)=(2-n^2)G(t),$$

som har løsning

$$G_n(t)=C_n e^{(2-n^2)t},\qquad n=0,1,2,\ldots$$

Altså er alle løsninger på formen $u(x,t)=F(x)G(t)$, som tilfredstiller $u_t=u_{xx}+2u$ og de gitte randbetingelsene, gitt ved

$$u(x,t)=\sum_{n=0}^{\infty}F_n(x)G_n(t)=\sum_{n=0}^{\infty}A_n e^{(2-n^2)t}\cos nx.$$

b)  Legg merke til at $\cos^2 x=\frac{1}{2}(1+\cos 2x)$, slik at

$$u(x,0)=(\cos x+1)^2=\cos^2 x+2\cos x+1=\frac{3}{2}+2\cos x+\frac{1}{2}\cos 2x.$$

De løsningene vi fant i oppgave **a)** som i tillegg tilfredstiller initialbetingelsen gitt over, er da gitt ved

$$u(x,t)=\frac{3}{2}e^{2t}+2e^{t}\cos x+\frac{1}{2}e^{-2t}\cos 2x.$$

Kildesett: course=TMA4135 term=host year=2010 problem=6 file=tma4135_10h.pdf
