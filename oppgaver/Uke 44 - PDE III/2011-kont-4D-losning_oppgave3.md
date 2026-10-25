### **Løsning til Oppgave 3**

a)  Fra oppgaveteksten ser vi at $u_0(x)$ tilfredstiller ligningen

$$u_0^{\prime\prime}(x)+r=0,\quad u_0(0)=0,\quad u_0^{\prime}(L)=0,$$

som har løsning

$$u_0(x)=rx\left(L-\frac{x}{2}\right).$$

Fra oppgaveteksten vet vi at $u(x,t)$ tilfredstiller ligningen

$${\frac{\partial u}{\partial t}}={\frac{\partial^{2}u}{\partial x^{2}}}+r,\quad u(0,t)=0,\quad{\frac{\partial u(L,t)}{\partial x}}=0,\eqno(1)$$

for $0\leq x\leq L$ og $t\geq 0$.

Ved å sette inn for $u(x,t)=u_0(x)+v(x,t)$ i (1) får vi

$${\frac{\partial u}{\partial t}}={\frac{\partial v}{\partial t}}={\frac{\partial^{2}u}{\partial x^{2}}}+r\qquad\text{der}\qquad{\frac{\partial^{2}u}{\partial x^{2}}}=u_0^{\prime\prime}(x)+{\frac{\partial^{2}v}{\partial x^{2}}}=-r+{\frac{\partial^{2}v}{\partial x^{2}}},$$

det vil si

$${\frac{\partial v}{\partial t}}={\frac{\partial^{2}v}{\partial x^{2}}}.\eqno(2)$$

Ettersom $u(0,t)=u_0(0)+v(0,t)=v(0,t)=0$ og ${\frac{\partial u(L,t)}{\partial x}}=u_0^{\prime}(L)+{\frac{\partial v(L,t)}{\partial x}}={\frac{\partial v(L,t)}{\partial x}}=0$, blir randbetingelse for $v(x,t)$ de samme som for $u(x,t)$, det vil si

$$v(0,t)=0\qquad\text{og}\qquad{\frac{\partial v(L,t)}{\partial x}}=0.\eqno(3)$$

b)  Ettersom $u(x,t)=u_0(x)+v(x,t)$ og vi er gitt initialbetingelsen

$$u(x,0)=u_0(x)+\sin{\frac{\pi x}{2L}}+2\sin{\frac{5\pi x}{2L}},\quad 0\leq x\leq L,$$

får vi initialbetingelsen

$$v(x,0)=\sin{\frac{\pi x}{2L}}+2\sin{\frac{5\pi x}{2L}},\quad 0\leq x\leq L.\eqno(4)$$

For å finne temperaturen i staven for $0\leq x\leq L$ og $t\geq 0$, trenger vi å finne løsningen til (2), gitt randbetingelser (3) og initialbetingelse (4).

La så $v(x,t)=F(x)G(t)$. Innsatt i (2) får vi

$$F(x)\dot{G}(t)=F^{\prime\prime}(x)G(t),$$

det vil si

$$\underbrace{\frac{F^{\prime\prime}(x)}{F(x)}}_{=k}=\underbrace{\frac{\dot{G}(t)}{G(t)}}_{=k}.$$

Dette gir oss to ligninger å løse

$$F^{\prime\prime}(x)-kF(x)=0,\eqno(5)$$

$$\dot{G}(t)-kG(t)=0.\eqno(6)$$

Løser så (5). Anta at $k=-p^2$. Det vil si,

$$F^{\prime\prime}(x)+p^2F(x)=0,$$

som har generell løsning

$$F(x)=A\cos px+B\sin px.$$

Randbetingelsene (3) gir at $F(0)=0$ og at $F^{\prime}(L)=0$. Fra $F(0)=0$ får vi at $A=0$. Fra $F^{\prime}(L)=0$ får vi at

$$pL=\frac{(2n-1)\pi}{2},\quad n=1,2,3,\ldots$$

slik at

$$p=p_n=\frac{(2n-1)\pi}{2L},\quad n=1,2,3,\ldots$$

(For $k\geq 0$ står vi kun igjen med den trivielle løsningen $v(x,t)=0$.)

Altså har vi at

$$F_n(x)=B_n\sin p_nx=B_n\sin{\frac{(2n-1)\pi x}{2L}},\quad n=1,2,3,\ldots$$

Innsatt for $k=-p_n^2$ i (6) får vi

$$\dot{G}(t)+p_n^2G(t)=0,$$

som har løsning

$$G_n(t)=C_ne^{-p_n^2t}=C_n\exp\left\{-\left(\frac{(2n-1)\pi}{2L}\right)^2t\right\},\quad n=1,2,3,\ldots$$

Dermed har vi at

$$v(x,t)=\sum_{n=1}^{\infty}F_n(x)G_n(t)=\sum_{n=1}^{\infty}A_n\exp\left\{-\left(\frac{(2n-1)\pi}{2L}\right)^2t\right\}\sin{\frac{(2n-1)\pi x}{2L}},$$

der $A_n=B_nC_n$.

Initialbetingelsen (4) gir så at

$$v(x,0)=\sum_{n=1}^{\infty}A_n\sin{\frac{(2n-1)\pi x}{2L}}=\sin{\frac{\pi x}{2L}}+2\sin{\frac{5\pi x}{2L}},$$

det vil si $A_1=1$, $A_3=2$ og $A_n=0$ for alle andre verdier av $n$.

Altså er

$$v(x,t)=\exp\left\{-\left(\frac{\pi}{2L}\right)^2t\right\}\sin{\frac{\pi x}{2L}}+2\exp\left\{-\left(\frac{5\pi}{2L}\right)^2t\right\}\sin{\frac{5\pi x}{2L}},$$

som igjen gir at temperaturen i staven er gitt ved

$$u(x,t)=u_0(x)+v(x,t)$$

$$=rx\left(L-\frac{x}{2}\right)+\exp\left\{-\left(\frac{\pi}{2L}\right)^2t\right\}\sin{\frac{\pi x}{2L}}+2\exp\left\{-\left(\frac{5\pi}{2L}\right)^2t\right\}\sin{\frac{5\pi x}{2L}},$$

for $0\leq x\leq L$, og $t\geq 0$.

Kildesett: course=TMA4135 term=kont year=2011 problem=3 file=tma4135_11k.pdf
