### **Løsning til Oppgave 4**

**a)** Innsatt for $u(x,t)=F(x)G(t)$ i $tu_t=u_{xx}$ får vi

$$tF\dot{G}=F''G,\qquad F''=\frac{\mathrm{d}^2F}{\mathrm{d}x^2},\quad\dot{G}=\frac{\mathrm{d}G}{\mathrm{d}t}.$$

Det gir

$$\underbrace{\frac{F''}{F}}_{k}=\underbrace{\frac{t\dot{G}}{G}}_{k}.$$

Altså får vi to ordinære differensiallikninger

$$F''-kF=0 \tag{1}$$

$$t\,\dot{G}-kG=0. \tag{2}$$

Fra randbetingelsene, $u(0,t)=u(\pi,t)=0$, får vi $F(0)=F(\pi)=0$. Vi må se på tilfellene

(i) $k>0$
(ii) $k=0$
(iii) $k<0$.

(i) La $k=\mu^2>0$. Innsatt i (1) gir det

$$F''-\mu^2F=0$$

som har løsning

$$F(x)=Ae^{\mu x}+Be^{-\mu x}.$$

Fra $F(0)=0$ får vi $A+B=0$. Det vil si,

$$F(x)=A\left(e^{\mu x}-e^{-\mu x}\right)=2A\sinh\mu x.$$

Fra $F(\pi)=0$ får vi $A=0$ ettersom $\sinh\mu\pi\neq 0$. Dermed får vi kun den trivielle løsningen $F(x)=0$.

(ii) Innsatt for $k=0$ i (1) får vi

$$F''=0$$

som har løsning

$$F(x)=Ax+B.$$

Fra $F(0)=F(\pi)=0$ får vi $A=B=0$. Dermed får vi kun den trivielle løsningen $F(x)=0$.

(iii) La $k=-p^2<0$. Innsatt i (1) gir det

$$F''+p^2F=0$$

som har løsning

$$F(x)=A\cos px+B\sin px.$$

Fra $F(0)=0$ får vi $A=0$. Fra $F(\pi)=0$ får vi

$$B\sin p\pi=0$$

som medfører enten $B=0$ eller $p\pi=n\pi$, $n=1,2,3,\ldots$ Da $B=0$ kun gir den trivielle løsningen er vi interessert i tilfellet $p=n$, $n=1,2,3,\ldots$ som gir

$$F_n(x)=\tilde{B}_n\sin nx.$$

Innsatt for $k=-n^2$ i (2) får vi

$$t\dot{G}+n^2G=0.$$

Det vil si,

$$\dot{G}=-\frac{n^2}{t}G$$

som har løsning

$$G_n(t)=C_nt^{-n^2}.$$

Altså er de løsningene av $tu_t=u_{xx}$ som kan skrives på formen $u(x,t)=F(x)G(t)$, og som tilfredstiller randbetingelsene $u(0,t)=u(\pi,t)=0$, gitt ved

$$u_n(x,t)=F_n(x)G_n(t)=B_nt^{-n^2}\sin nx,\quad n=1,2,3,\ldots,$$

der $B_n=\tilde{B}_nC_n$. Den generelle løsningen er så gitt ved

$$u(x,t)=\sum_{n=1}^{\infty}u_n(x,t)=\sum_{n=1}^{\infty}B_nt^{-n^2}\sin nx.$$

**b)** Fra

$$u(x,1)=\sum_{n=1}^{\infty}B_n1^{-n^2}\sin nx=\sum_{n=1}^{\infty}B_n\sin nx=\sin 2x+5\sin 5x$$

får vi $B_2=1$, $B_5=5$ og $B_n=0$ for $n\neq 2,5$. Det gir

$$u(x,t)=t^{-4}\sin 2x+5t^{-25}\sin 5x.$$

Kildesett: course=TMA4135 term=host year=2012 problem=4 file=tma4135_12h.pdf
