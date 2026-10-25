### **Løsning til Oppgave 2**

**a)** Skisse:

[Figur: $x$-akse tallfestet fra $-3$ til $3$, $y$-akse merket $f(x)$ med merke i høyde $1$. Funksjonen (blå kurve) stiger lineært fra $(2k-1,0)$ til $(2k,1)$ for heltallige $k$, faller loddrett ned til null i $x=2k$, og er konstant null på $(2k,2k+1)$.]

Fourierkoeffisientene:

$$a_0=\frac{1}{2}\int_{-1}^{1}f(x)dx=\frac{1}{4},$$

$$a_n=\int_{-1}^{1}f(x)\cos(n\pi x)dx=\int_{-1}^{0}(1+x)\cos(n\pi x)dx$$

$$=\left[\frac{1}{n\pi}\sin(n\pi x)+\frac{1}{n^2\pi^2}\big(\cos(n\pi x)+n\pi x\sin(n\pi x)\big)\right]_{-1}^{0}=\frac{1}{n^2\pi^2}\big(1-(-1)^n\big),$$

$$b_n=\int_{-1}^{1}f(x)\sin(n\pi x)dx=\int_{-1}^{0}(1+x)\sin(n\pi x)dx$$

$$=\left[-\frac{1}{n\pi}\cos(n\pi x)+\frac{1}{n^2\pi^2}\big(\sin(n\pi x)-n\pi x\cos(n\pi x)\big)\right]_{-1}^{0}=-\frac{1}{n\pi}.$$

Fourierrekka:

$$f(x)\sim\frac{1}{4}+\sum_{n=1}^{\infty}\left(\frac{1-(-1)^n}{n^2\pi^2}\cos(n\pi x)-\frac{1}{n\pi}\sin(n\pi x)\right).$$

**b)** Sett inn $x=0$, og vi får at

$$\frac{1}{2}\big(f(0^{+})+f(0^{-})\big)=\frac{1}{2}=\frac{1}{4}+\sum_{n=1}^{\infty}\frac{1-(-1)^n}{n^2\pi^2}=\frac{1}{4}+\sum_{m=0}^{\infty}\frac{2}{(2m+1)^2\pi^2}$$

og

$$\sum_{m=0}^{\infty}\frac{1}{(2m+1)^2}=\frac{\pi^2}{2}\Big(\frac{1}{2}-\frac{1}{4}\Big)=\frac{\pi^2}{8}.$$

Sett inn $x=1/2$ slik at

$$f\big(\tfrac{1}{2}\big)=0=\frac{1}{4}+\sum_{n=1}^{\infty}\left(\frac{1-(-1)^n}{n^2\pi^2}\cos\Big(\frac{n\pi}{2}\Big)-\frac{1}{n\pi}\sin\Big(\frac{n\pi}{2}\Big)\right)$$

er 0 når $n$ er et partall, mens det er $(-1)^{(n-1)/2}$ når $n$ er et oddetall. Dermed har vi at

$$0=\frac{1}{4}+\sum_{m=0}^{\infty}-\frac{(-1)^m}{(2m+1)\pi}\quad\Rightarrow\quad\sum_{m=1}^{\infty}\frac{(-1)^m}{2m+1}=\frac{\pi}{4}.$$

*Kjeldevarsel: Setninga som startar «er 0 når $n$ er et partall» er trykt på toppen av side 3 i LF utan gjenteken innleiing og verkar difor ufullstendig — ho høyrer til forklaringa av leddet $\sin(n\pi/2)$ etter innsettinga $x=1/2$. Summeindeksen i den siste konklusjonen er trykt som $m=1$; av likninga til venstre følgjer $\sum_{m=0}^{\infty}\frac{(-1)^m}{2m+1}=\frac{\pi}{4}$ (Leibniz-rekka), medan summen frå $m=1$ er $\frac{\pi}{4}-1$ — $m=1$ er ei trykkfeil, bevart ordrett. Koeffisientane $a_0=\frac14$, $a_n=\frac{1-(-1)^n}{n^2\pi^2}$, $b_n=-\frac{1}{n\pi}$ og begge summane er kontrollreikna med sympy utan avvik.*

Kildesett: course=TMA4125 term=var year=2012 problem=2 file=tma4123_25_v12.pdf
