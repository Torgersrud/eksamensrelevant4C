### **Løsning til Oppgave 3**

**a)** Ved å sette $u(x,t)=F(x)G(t)$ inn i differensialligningen får vi at $F(x)G'(t)=F''(x)G(t)$, slik at

$$\frac{F''(x)}{F(x)}=\frac{G'(t)}{G(t)}=k,$$

der $k$ er en konstant. Dette gir de to ordinære differensialligningene

$$F''(x)-kF(x)=0\qquad(1)$$

$$G'(t)-kG(t)=0.\qquad(2)$$

Randbetingelsene gir at $F(0)=F(L)=0$. Vi løser først ODE (1) med disse randbetingelsene. Formen på løsningen er avhengig av om $k$ er positiv, null eller negativ.

$\underline{k>0}$: Skriv $k=\mu^2$. Generell løsning av (1) er

$$F(x)=C_1e^{\mu x}+C_2e^{-\mu x}.$$

Randbetingelsene gir

$$0=F(0)=C_1+C_2,\quad 0=F(L)=C_1e^{\mu L}+C_2e^{-\mu L}.$$

Den første av disse gir at $C_1=-C_2$, og den andre gir dermed at $C_1=C_2=0$ (siden $e^{\mu L}>e^{-\mu L}$). Vi får altså kun den trivielle løsningen $u(x,t)=0$.

$\underline{k=0}$: ODE (1) blir $F''(x)=0$ som har generell løsning

$$F(x)=ax+b.$$

Randbetingelsene gir

$$0=F(0)=b,\quad 0=F(L)=b,$$

så vi får igjen kun den trivielle løsningen.

$\underline{k<0}$: Skriv $k=-\mu^2$. Generell løsning er

$$F(x)=C_1\cos\mu x+C_2\sin\mu x.$$

Randbetingelsene gir

$$0=F(0)=C_1,\quad 0=F(L)=C_2\sin\mu L.$$

Dersom $\sin\mu L=0$ får vi altså ikke-trivielle løsninger. Dvs. $\mu L=n\pi$, eller

$$\mu=\frac{n\pi}{L},$$

gir løsningene

$$F_n(x)=C_2\sin\frac{n\pi}{L}x,\quad n=1,2,3,\ldots$$

Vi putter disse verdiene av $\mu$ inn i ODE (2) og får

$$G'(t)+\left(\frac{n\pi}{L}\right)^2G(t)=0,$$

som har generell løsning

$$G_n(t)=C_ne^{-\left(\frac{n\pi}{L}\right)^2t},\quad n=1,2,3,\ldots.$$

Dette gir oss *egenfunksjonene*

$$u_n(x,t)=B_n\sin\frac{n\pi x}{L}e^{-\left(\frac{n\pi}{L}\right)^2t},\quad n=1,2,3,\ldots$$

(der $B_n$ er konstanten $C_2C_n$).

**b)** For å finne løsningene som tilfredstiller initialbetingelsene bruker vi superposisjonsprinsippet til å danne løsningen

$$u(x,t)=\sum_{n=1}^{\infty}u_n(x,t)=\sum_{n=1}^{\infty}B_n\sin\frac{n\pi x}{L}e^{-\left(\frac{n\pi}{L}\right)^2t}$$

av PDE og randbetingelser.

(i) Initialbetingelsen gir

$$-3\sin\frac{13\pi}{L}x=\sum_{n=1}^{\infty}B_n\sin\frac{n\pi x}{L},$$

som er (pga entydighet) er Fourierrekken til initialbetingelsen. Vi kan lese av koeffisienten $B_n$ direkte: vi har $B_n=0$ for alle $n\ne 13$, og $B_{13}=-3$. Løsningen av PDE med randbetingelser og denne initialbetingelsen er altså

$$u(x,t)=-3\sin\frac{13\pi x}{L}e^{-\left(\frac{13\pi}{L}\right)^2t}.$$

(ii) Initialbetingelsen gir

$$10=\sum_{n=1}^{\infty}B_n\sin\frac{n\pi x}{L},$$

som er Fourier-sinus-rekken til 10. Dermed er

$$B_n=\frac{2}{L}\int_{0}^{L}10\sin\frac{n\pi}{L}x\,\mathrm{d}x$$

$$=-\frac{20}{L}\frac{L}{n\pi}\left[\cos\frac{n\pi}{L}x\right]_{0}^{L}$$

$$=-\frac{20}{n\pi}(\cos n\pi-1)$$

$$=\frac{20}{n\pi}(1-(-1)^n).$$

Løsningen på PDE med randbetingelser og denne initialbetingelsen er altså

$$u(x,t)=\sum_{n=1}^{\infty}\frac{20}{n\pi}(1-(-1)^n)\sin\frac{n\pi x}{L}e^{-\left(\frac{n\pi}{L}\right)^2t}$$

*Kjeldevarsel: I b)(i) står det «som er (pga entydighet) er Fourierrekken» med «er» to gonger, og i første linje av b) står det «tilfredstiller» utan dobbel-s; begge deler bevart ordrett.*

Kildesett: course=TMA4123 term=var year=2013 problem=3 file=eksamen2013v.pdf
