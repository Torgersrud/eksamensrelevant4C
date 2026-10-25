### **Løsning til Oppgave 2**

**a)** Vi har

[Figur: Plot med $x$-akse fra $-2$ til $2$ og $y$-akse fra $-1$ til $1$. Tett tykk svart strek er $f(x) = x$ på $[0, 1]$. Bla kurve er den like periodiske utvidelsen $g$: stigande svart strek på $[0,1]$, spegla synande på $[-1,0]$ og seinare sageblad med topp $1$ i $x = \pm 1$ og botn $0$ i $x = 0, \pm 2$. Raud stipla kurve er den oddde periodiske utvidelsen $h$: rett linje med stigningstal $1$ gjennom origo på $(-1,1)$ med hopp frå $-1$ opp til $0$ i $x = -1$ og frå $1$ ned til $0$ i $x = 1$, og seinare sageblad mellom $-1$ og $1$ med periode $2$. Teiknforklaring med $f$, $g$ og $h$.]

Grafene til $f$, $g$ og $h$.

Sinus-rekken til $f$ er gitt av

$$f(x) \sim \sum_{n=1}^{\infty} b_n \sin(n\pi x)$$

der

$$b_n = 2 \int_0^1 f(x) \sin(n\pi x) \, dx$$

Vi bruker delvis integrasjon og får

$$\begin{aligned} b_n &= 2 \int_0^1 x \sin(n\pi x) \, dx \\ &= 2 \left[ x \frac{-\cos(n\pi x)}{n\pi} \right]_0^1 + 2 \int_0^1 \frac{\cos(n\pi x)}{n\pi} \, dx \\ &= -2 \frac{\cos(n\pi)}{n\pi} + 2 \left[ \frac{\sin(n\pi x)}{(n\pi)^2} \right]_0^1 \\ &= 2 \frac{(-1)^{n+1}}{n\pi}. \end{aligned}$$

Cosinusrekken til $f$ er Fourierrekken til den like periodiske utvidelsen av $f$, det vil si $g$. Siden $g$ er kontinuerlig i $x = 1$ får vi at summen til cosinusrekken til $f$ er lik $g(1) = 1$. Sinurekken til $f$ er Fourierrekken til den odde periodiske utvidelsen av $f$, det vil si $h$. Nå er $h$ ikke kontinuerlig i $x = 1$ og vi har at summen til sinusrekken til $f$ er lik $\frac{h(1-) + h(1+)}{2} = 0$.

**b)** Cosinusrekken til $f$ er gitt av

$$f(x) \sim a_0 + \sum_{n=1}^{\infty} a_n \cos(n\pi x)$$

der

$$a_0 = \int_0^1 f(x) \, dx, \ a_n = 2 \int_0^1 f(x) \cos(n\pi x) \, dx.$$

Vi får

$$a_0 \int_0^1 x \, dx = \frac{1}{2}$$

og, ved hjelp av delvis integrasjon,

$$\begin{aligned} a_n &= 2 \int_0^1 x \cos(n\pi x) \, dx \\ &= 2 \left[ x \frac{\sin(n\pi x)}{n\pi} \right]_0^1 - 2 \int_0^1 \frac{\sin(n\pi x)}{n\pi} \, dx \\ &= 2 \left[ \frac{\cos(n\pi x)}{(n\pi)^2} \right]_0^1 \qquad \text{siden } \sin(n\pi) = \sin(0) = 0 \\ &= 2 \frac{(-1)^n - 1}{(n\pi)^2} \qquad \text{siden } \cos(n\pi) = (-1)^n. \end{aligned}$$

Vi tar $x = 0$. I dette punktet er summen til cosinusrekken lik $g(0) = 0$ fordi $g$ er kontinuerlig. Vi får

$$\frac{1}{2} + 2 \sum_{n=1}^{\infty} \frac{(-1)^n - 1}{(n\pi)^2} = 0 \tag{L-5}$$

Vi har

$$(-1)^n - 1 = \begin{cases} 0 & \text{hvis } n \text{ er like} \\ -2 & \text{hvis } n \text{ er odde}. \end{cases}$$

Vi kan skrive om summen i (L-5) ved å bare ta de odde $n$ og vi får

$$\frac{1}{2} + 2 \sum_{n=0}^{\infty} \frac{-2}{((2n+1)\pi)^2} = 0.$$

Det følger at

$$\sum_{n=0}^{\infty} \frac{1}{(2n+1)^2} = \frac{\pi^2}{8}.$$

*Kjeldevarsel: samanhengen for $a_0$ er trykt som «$a_0 \int_0^1 x \, dx = \frac{1}{2}$» utan likskapstegn mellom $a_0$ og integralet; meiner er $a_0 = \int_0^1 x \, dx = \frac{1}{2}$, og utrekninga vidare går ut frå denne. Ordrett elles, incl. «Sinurekken».*

Kildesett: course=TMA4125 term=var year=2008 problem=2 file=eksamen-bok_2008v.pdf
