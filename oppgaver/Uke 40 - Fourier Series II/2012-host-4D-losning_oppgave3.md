### **Løsning til Oppgave 3**

**a)** Fourierrekka til $f$ er gitt ved

$$a_0+\sum_{n=1}^{\infty}\left(a_n\cos nx+b_n\sin nx\right)$$

der

$$\begin{aligned}a_0&=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)\,\mathrm{d}x=0 && (f\ \text{odde})\\ a_n&=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos nx\,\mathrm{d}x=0,\quad n=1,2,3,\ldots && (f\ \text{odde})\\ b_n&=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin nx\,\mathrm{d}x=\frac{2}{\pi}\int_0^{\pi}\sin\frac{x}{2}\sin nx\,\mathrm{d}x && (f\ \text{odde})\\ &=\frac{1}{\pi}\int_0^{\pi}\left[\cos(n-1/2)x-\cos(n+1/2)x\right]\mathrm{d}x=\frac{1}{\pi}\left[\frac{\sin(n-1/2)x}{n-1/2}-\frac{\sin(n+1/2)x}{n+1/2}\right]_0^{\pi}\\ &=\frac{1}{\pi}\left(\frac{(-1)^{n+1}}{n-1/2}-\frac{(-1)^n}{n+1/2}\right)=\frac{(-1)^{n+1}}{\pi}\left(\frac{1}{n-1/2}+\frac{1}{n+1/2}\right)=\frac{8}{\pi}\frac{(-1)^{n+1}n}{4n^2-1},\quad n=1,2,3,\ldots\end{aligned}$$

Altså er fourierrekka til $f$ gitt ved

$$\frac{8}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}n}{4n^2-1}\sin nx.$$

**b)** Innsatt for $x=\pi/2$ får vi

$$\frac{8}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^{n+1}n}{4n^2-1}\sin\frac{n\pi}{2}=\frac{8}{\pi}\sum_{m=0}^{\infty}\frac{(-1)^{2m+2}(2m+1)}{4(2m+1)^2-1}(-1)^m=\frac{8}{\pi}\sum_{m=0}^{\infty}\frac{(-1)^m(2m+1)}{4(2m+1)^2-1}=f(\pi/2)=\frac{1}{\sqrt{2}}.$$

Det vil si,

$$\sum_{m=0}^{\infty}\frac{(-1)^m(2m+1)}{4(2m+1)^2-1}=\frac{\pi}{8\sqrt{2}}=\frac{\pi}{16}\sqrt{2}.$$

Kildesett: course=TMA4135 term=host year=2012 problem=3 file=tma4135_12h.pdf
