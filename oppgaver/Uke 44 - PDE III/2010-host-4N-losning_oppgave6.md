### **Løsning til Oppgave 6**

**a)** Setter inn $u(x,t)=X(x)T(t)$ i $u_t=u_{xx}+2u$. Det gir

$$X(x)\dot{T}(t)=X''(x)T(t)+2X(x)T(t)\quad\text{det vil si}\quad X''(x)T(t)=X(x)\big(\dot{T}(t)-2T(t)\big),$$

slik at

$$\underbrace{\frac{X''(x)}{X(x)}}_{k}=\underbrace{\frac{\dot{T}(t)-2T(t)}{T(t)}}_{k}.$$

Dette gir følgende to 2. ordens ordinære differensialligninger

$$X''(x)-kX(x)=0,\tag{1}$$

$$\dot{T}(t)-(k+2)T(t)=0.\tag{2}$$

Løser så (1), gitt randbetingelsene $u_x(0,t)=0$ og $u_x(\pi,t)=0$, det vil si $X'(0)=0$ og $X'(\pi)=0$. Med andre ord,

$$X''(x)-kX(x)=0,\qquad X'(0)=0,\quad X'(\pi)=0.\tag{1′}$$

Vi har tre muligheter for $k$:

* (i) $k=p^2>0$: Innsatt for $k=p^2$ i (1′) får vi

$$X''(x)-p^2X(x)=0.$$

Denne ligningen har løsning

$$X(x)=Ae^{px}+Be^{-px}.$$

Ettersom

$$X'(x)=p\big(Ae^{px}-Be^{-px}\big),$$

gir $X'(0)=0$ at $A=-B$. Fra $X'(\pi)=0$ får vi

$$X'(\pi)=Ap(e^{p\pi}-e^{-p\pi})=2Ap\sinh p\pi=0.$$

Altså må $A=0$. Dermed står vi kun igjen med den trivielle løsningen $u(x,t)=0$. Altså er $k\leq0$.

* (ii) $k=0$: Innsatt for $k=0$ i (1′) får vi

$$X''(x)=0,$$

som har løsning $X(x)=Ax+B$. Fra $X'(0)=0$ og $X'(\pi)=0$ får vi $A=0$. Altså står vi igjen med løsningen $X(x)=$ konstant.

* (iii) $k=-p^2<0$: Innsatt for $k=-p^2$ i (1′) får vi

$$X''(x)+p^2X(x)=0,$$

som har løsning

$$X(x)=A\cos px+B\sin px.$$

Ettersom

$$X'(x)=p\big(B\cos px-A\sin px\big),$$

får vi at $X'(0)=Bp=0$, det vil si $B=0$. Altså har vi at $X(x)=A\cos px$. Fra $X'(\pi)=0$, får vi

$$X'(\pi)=-pA\sin p\pi=0.$$

Ettersom $A=0$ kun gir den trivielle løsningen $u(x,t)=0$, ser vi på tilfellet der $\sin p\pi=0$. Det gir $p=n=1,2,3,\ldots$. Altså er $k=-n^2$.

Ved å kombinere (ii) og (iii) har vi funnet at alle mulige løsninger for (1′), gitt våre randbetingelser, er på formen

$$X_n(x)=\tilde{A}_n\cos nx,\qquad n=0,1,2,\ldots$$

Setter så inn for $k=-n^2$ i (2). Det gir

$$\dot{T}(t)+(n^2-2)T(t)=0\quad\text{det vil si}\quad\dot{T}(t)=(2-n^2)T(t),$$

som har løsning

$$T_n(t)=C_ne^{(2-n^2)t},\qquad n=0,1,2,\ldots$$

Altså er alle løsninger på formen $u(x,t)=X(x)T(t)$, som tilfredsstiller $u_t=u_{xx}+2u$ og de gitte randbetingelsene, gitt ved

$$u(x,t)=\sum_{n=0}^{\infty}X_n(x)T_n(t)=\sum_{n=0}^{\infty}A_ne^{(2-n^2)t}\cos nx.$$

**b)** Legg merke til at $\cos^2x=\frac{1}{2}(1+\cos2x)$, slik at

$$u(x,0)=(\cos x+1)^2=\cos^2x+2\cos x+1=\frac{3}{2}+2\cos x+\frac{1}{2}\cos2x.$$

De løsningene vi fant i oppgave **a)** som i tillegg tilfredsstiller initialbetingelsen gitt over, er da gitt ved

$$u(x,t)=\frac{3}{2}e^{2t}+2e^{t}\cos x+\frac{1}{2}e^{-2t}\cos2x.$$

Kildesett: course=TMA4130 term=host year=2010 problem=6 file=eksamen-bok_2010.pdf
