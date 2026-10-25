### **Løsning til Oppgave 3**

**a)** Dette er et standard problem med separasjon av variable, der vi først fører inn $G$ og $F$ i ligningene,

$$F(x)G'(t)=F''(x)G(t)\,,$$

og får

$$\frac{G'(t)}{G(t)}=\frac{F''(x)}{F(x)}=k,$$

eller

$$G'(t)-kG(t)=0,\quad G(0)=1,\tag{3}$$

$$F''(x)-kF(x)=0,\ F(0)=F(L)=0. \tag{4}$$

Hvis $k>0$, vil generell løsning av lign. 4 være

$$F(x)=A\cosh\left(\sqrt{k}x\right)+B\sinh\left(\sqrt{k}x\right).$$

Siden $F(0)=0$ må $A=0$, men $\sinh\left(\sqrt{k}x\right)\neq 0$ for alle $x\neq 0$, og dette fører til sinde $F(L)=0$, at også $B=0$, dvs. null-løsningen. Det samme gjelder for $k=0$. Følgelig trenger vi $k<0$ for å få akseptable løsninger forskjellig fra 0, og prøver da som vanlig $k=-p^2$. Generell løsning av lign. 4 blir

$$F(x)=A\cos px+B\sin px,$$

der $A$ må være 0 siden $F(L)=0$. Hvis vi også krever $F(L)=0$, må i tillegg

$$\sin(pL)=0.$$

Vi får dermed at mulige $p$-er og tilhørende funksjoner (egenverdier og egenfunksjoner) er

$$p_n=\frac{n\pi}{L},$$

$$F_n(x)=\sin(p_nL)=\sin\frac{n\pi x}{L},\ \ n=1,2,\cdots.$$

Ligningene for $G(t)$ blir

$$G'(t)+p_n^2G(t)=0,\ n=1,2,\cdots,$$

og med $G(0)=1$, finner vi

$$G_n(t)=\exp\left(-p_n^2t\right)\exp\left(-\left(\frac{n\pi}{L}\right)^2t\right),\ \ n=1,2,\cdots.$$

Alle ikke-trivielle løsninger på denne formen blir altså

$$C_n\exp\left(-\left(\frac{n\pi}{L}\right)^2t\right)\sin\frac{n\pi x}{L},\ n=1,2,\cdots,$$

der $\{C_n\}$ er vilkårlige konstanter.

**b)** En tidsuavhengig (stasjonær) løsning $u_s(x)$ er uavhengig av t og må følgelig tilfredsstille ligningen

$$\frac{\mathrm{d}^2u_s}{\mathrm{d}x^2}=0,$$

dvs. $u_s(x)=A+Bx$. Betingelsene $u(0)=0$ og $u(L)=T$ gir oss dermed at

$$u_s(x)=\frac{xT}{L}.$$

Generell løsning kan nå skrives på formen

$$u(x,t)=u_s(x)+v(x,t)\,,$$

der $v(x,t)$ er en løsning av lign. 2 med $v(0,t)=v(L,t)=0$, med andre ord, en kombinasjon av løsningene i (a). Siden den gitte startbetingelsen allerede inneholder $u_s$, blir startbetingelsen for $v(x,t)$ bare

$$v(x,0)=\sin\frac{\pi x}{L}+\frac{1}{3}\sin\frac{3\pi x}{L},$$

og temperaturen i staven kan dermed leses direkte ut fra resultatet i (a) som

$$u(x,t)=T\frac{x}{L}+e^{-\left(\frac{\pi}{L}\right)^2t}\sin\frac{\pi x}{L}+\frac{1}{3}e^{-\left(\frac{3\pi}{L}\right)^2t}\sin\frac{3\pi x}{L}.$$

Som forventet vil

$$\lim_{t\to\infty}u(x,t)=T\frac{x}{L}=u_s(x)\,.$$

Alternativt kan oppgaven løses ved å tippe at vi *kanskje* har en løsning på formen

$$u_s(x)+G_1(t)\sin\frac{\pi x}{L}+G_3(t)\sin\frac{3\pi x}{L},$$

og deretter enkelt finne $G_1$ og $G_3$ fra direkte innsetting i ligningen.

*Kjeldevarsel: Trykkfeilar i LF er bevarte ordrett: (i) «der $A$ må være 0 siden $F(L)=0$» må lesast som $F(0)=0$ — setninga like etter krev «også» $F(L)=0$, og det er $F(0)=0$ som gjev $A=0$ i $A\cos px+B\sin px$. (ii) Egenfunksjonen er trykt som $F_n(x)=\sin(p_nL)$; det rette mellomsteget er $\sin(p_nx)$, og sluttuttrykket $\sin\frac{n\pi x}{L}$ er rett. (iii) I formelen for $G_n(t)$ står dei to eksponentialfaktorane trykte side om side utan likskapsteikn; det eine uttrykket er $\exp(-p_n^2t)=\exp\!\big(-(\frac{n\pi}{L})^2t\ \big)$, ikkje produktet deira. (iv) «fører til sinde $F(L)=0$» har trykkfeilen «sinde» for «siden». Løysinga er kontrollert med sympy: $u_t-u_{xx}\equiv 0$ for sluttformelen, start- og randvilkåra er oppfylte, og $G_n(t)=e^{-p_n^2t}$ løyser (3) med $G(0)=1$.*

Kildesett: course=TMA4125 term=var year=2011 problem=3 file=tma4125nbokmaal.pdf
