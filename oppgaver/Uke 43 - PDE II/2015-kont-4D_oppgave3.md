### **Oppgave 3**

**a)** Vis at

$$u(x,t)=\varphi(x+ct)+\psi(x-ct)$$

oppfyller

$$\frac{\partial^2 u}{\partial t^2}-c^2\frac{\partial^2 u}{\partial x^2}=0 \qquad (3)$$

for alle funksjoner $\varphi$ og $\psi$ som er to ganger kontinuerlig deriverbare. Her er $c$ en konstant.

**b)** Anta at

$$u(x,0)=f(x),\qquad u_t(x,0)=g(x) \qquad (4)$$

for to gitte funksjoner $f$ og $g$ som er to ganger kontinuerlig deriverbare. Vis at da må

$$\begin{aligned}\varphi(x)+\psi(x)&=f(x),\\ \varphi(x)-\psi(x)&=\frac{1}{c}\int_0^x g(y)\,dy+A\end{aligned}$$

der $A$ er en konstant. Vis også at

$$\begin{aligned}\varphi(x)&=\frac{1}{2}\left(f(x)+\frac{1}{c}\int_0^x g(y)\,dy+A\right),\\ \psi(x)&=\frac{1}{2}\left(f(x)-\frac{1}{c}\int_0^x g(y)\,dy-A\right).\end{aligned}$$

Bruk dette til å vise d'Alemberts formel

$$u(x,t)=\frac{1}{2}\Big(f(x+ct)+f(x-ct)\Big)+\frac{1}{2c}\int_{x-ct}^{x+ct} g(y)\,dy. \qquad (5)$$

**c)** La

$$f(x)=\sin(x),\qquad g(x)=\sin(x).$$

Bestem løsningen av ligning (3) med initialbetingelser (4).

Kildesett: course=TMA4135 term=kont year=2015 problem=3 file=tma4135_15k.pdf
