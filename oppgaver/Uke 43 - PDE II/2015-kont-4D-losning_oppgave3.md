### **Løsning til Oppgave 3**

*(Løsningsforslaget nummererer underpunktene a)–d): losningens c) tilsvarer siste del av eksamensoppgavens b), og losningens d) tilsvarer eksamensoppgavens c).)*

**a)** Vi finner

$$\begin{aligned}u_{xx}(x,t)&=\varphi''(x+ct)+\psi''(x-ct),\\ u_{tt}(x,t)&=c^2\varphi''(x+ct)+c^2\psi''(x-ct).\end{aligned}$$

Innsatt i ligningen viser at $u$ er en løsning.

**b)** Vi setter inn $t=0$ i uttrykket for $u$ og for $u_t(x,t)=c\varphi'(x+ct)-c\psi'(x-ct)$. Det gir

$$\begin{aligned}u(x,0)&=\varphi(x)+\psi(x)=f(x), & (3)\\ u_t(x,0)&=c\varphi'(x)-c\psi'(x)=g(x). & (4)\end{aligned}$$

Integrasjon av ligningen for $u_t$ gir

$$\varphi(x)-\psi(x)=\frac{1}{c}\int_0^x g(y)\,dy+A \qquad (5)$$

der $A$ er en vilkårlig integrasjonskonstant.

**c)** Addisjon og subtraksjon av de to ligningene (3) og (5) gir

$$\begin{aligned}\varphi(x)&=\frac{1}{2}\left(f(x)+\int_0^x g(y)\,dy+A\right), & (6)\\ \psi(x)&=\frac{1}{2}\left(f(x)-\int_0^x g(y)\,dy-A\right). & (7)\end{aligned}$$

Erstatt $x$ med $x+ct$ i ligning (6) og med $x-ct$ i (7) og adder uttrykkene. Det gir d'Alemberts formel

$$u(x,t)=\frac{1}{2}\big(f(x+ct)+f(x-ct)\big)+\frac{1}{2c}\int_{x-ct}^{x+ct} g(y)\,dy, \qquad (8)$$

når vi bruker

$$\int_0^{x+ct} g(y)\,dy-\int_0^{x-ct} g(y)\,dy=\int_{x-ct}^{x+ct} g(y)\,dy. \qquad (9)$$

**d)** Innsetting i d'Alemberts formel gir

$$\begin{aligned}u(x,t)&=\frac{1}{2}\big(\sin(x+ct)+\sin(x-ct)\big)+\frac{1}{2c}\int_{x-ct}^{x+ct}\sin(y)\,dy\\
&=\sin(x)\cos(ct)-\frac{1}{2c}\Big|_{x-ct}^{x+ct}\cos(y)\\
&=\sin(x)\cos(ct)-\frac{1}{2c}\big(\cos(x+ct)-\cos(x-ct)\big)\\
&=\sin(x)\cos(ct)+\frac{1}{c}\sin(x)\sin(ct)\\
&=\sin(x)\left(\cos(ct)+\frac{1}{c}\sin(ct)\right).\end{aligned}$$

Kildesett: course=TMA4135 term=kont year=2015 problem=3 file=tma4135_15k.pdf
