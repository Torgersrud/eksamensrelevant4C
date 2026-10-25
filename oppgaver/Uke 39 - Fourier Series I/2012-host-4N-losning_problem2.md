### **Solution to Problem 2**

**a)** A sketch of the graph of the given $f$ on the interval $[-3\pi,3\pi)$ is given at the top of the next page.

[Figur: $x$-akse tallfestet fra $-3\pi$ til $3\pi$ med merker i $\pm\pi$, $\pm2\pi$, $\pm3\pi$ og $y$-akse merket $y$ med merke i høyde $\pi$. Funksjonen er null (tykk linje langs $x$-aksen) på intervallene $(2k\pi-\pi,2k\pi)$ og stiger lineært fra $(2k\pi,0)$ til høyde $\pi$ like før $x=2k\pi+\pi$, der den ender med åpen sirkel; mønsteret gjentar seg med periode $2\pi$.]

The Fourier coefficient

$$A_{0}=\frac{1}{2\pi}\int_{0}^{\pi}x\,dx=\pi/4.$$

The Fourier coefficients

$$A_{n}=\frac{1}{\pi}\int_{0}^{\pi}x\cos(nx)\,dx=\frac{1}{\pi}\left[\frac{x\sin(nx)}{n}\bigg|_{x=0}^{\pi}-\frac{1}{n}\int_{0}^{\pi}\sin(nx)\,dx\right]$$

$$=\frac{\cos(nx)}{\pi n^{2}}\bigg|_{x=0}^{\pi}$$

$$=\frac{(-1)^{n}-1}{\pi n^{2}},$$

for $n=1,2,3,\ldots$ The Fourier coefficients

$$B_{n}=\frac{1}{\pi}\int_{0}^{\pi}x\sin(nx)\,dx=\frac{1}{\pi}\left[-\frac{x\cos(nx)}{n}\bigg|_{x=0}^{\pi}+\frac{1}{n}\int_{0}^{\pi}\cos(nx)\,dx\right]$$

$$=\frac{(-1)^{n+1}}{n}+\frac{\sin(nx)}{\pi n^{2}}\bigg|_{x=0}^{\pi}$$

$$=\frac{(-1)^{n+1}}{n},$$

for $n=1,2,3,\ldots$ Therefore, the Fourier series of $f$ is

$$\frac{\pi}{4}+\sum_{n=1}^{\infty}\left[\frac{(-1)^{n}-1}{\pi n^{2}}\cos(nx)+\frac{(-1)^{n+1}}{n}\sin(nx)\right].\qquad(1)$$

**b)** We can substitute $x=0$ in (1). This procedure is *completely straightforward*.

We could also compute the given series by taking $x=\pi$ in (1). However, we need to be **careful** with this option because $f$ has a jump-discontinuity at $x=\pi$. This implies that

$$\frac{f(\pi+)+f(\pi-)}{2}=\frac{\pi}{4}+\sum_{n=1}^{\infty}\frac{(-1)^{n}-1}{\pi n^{2}}\cos(n\pi).$$

Observe that $f(\pi-)=\pi$ and $f(\pi+)=0$. Rearranging terms in the above equation, we get

$$\sum_{k=0}^{\infty}\frac{1}{(2k+1)^{2}}=\frac{\pi^{2}}{8}.$$

*Kjeldevarsel: Eksamen-PDF-en for dette haustsettet blei aldri publisert; løysingsfila `solutions_2012h.pdf` er difor Kildesett for heile settet, og oppgåveteksten er ikkje gjenteken i løysinga — oppgåvedataet følgjer berre implisitt av fasiten (jf. figuren over og koeffisientintegrala).*

Kildesett: course=TMA4130 term=host year=2012 problem=2 file=solutions_2012h.pdf
