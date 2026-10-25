### **Løsning til Oppgave 4**

**a)** Vi beregner

$$\begin{aligned}a_0&=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)\,\mathrm{d}x=\frac{1}{2\pi}\int_0^{\pi}x\,\mathrm{d}x=\frac{\pi}{4}\\
a_n&=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\cos nx\,\mathrm{d}x=\frac{1}{\pi}\int_0^{\pi}x\cos nx\,\mathrm{d}x\\
&=\frac{1}{n\pi}\left[x\sin nx\right]_{x=0}^{\pi}-\frac{1}{n\pi}\int_0^{\pi}\sin nx\,\mathrm{d}x\\
&=\frac{1}{n^2\pi}\left[\cos nx\right]_{x=0}^{\pi}\\
&=\frac{1}{n^2\pi}((-1)^n-1)\\
&=\begin{cases}0&\text{når }n=2,4,6,\ldots\\ -\frac{2}{n^2\pi}&\text{når }n=1,3,5,\ldots\end{cases}\end{aligned}$$

$$\begin{aligned}b_n&=\frac{1}{\pi}\int_{-\pi}^{\pi}f(x)\sin nx\,\mathrm{d}x=\frac{1}{\pi}\int_0^{\pi}x\sin nx\,\mathrm{d}x\\
&=\frac{-1}{n\pi}\left[x\cos nx\right]_{x=0}^{\pi}+\frac{1}{n\pi}\int_0^{\pi}\cos n\pi x\,\mathrm{d}x\\
&=\frac{(-1)^{n+1}}{n}\end{aligned}$$

Fourier-rekken til $f$ er i punktet $x$ altså

$$\frac{\pi}{4}-\frac{2}{\pi}\sum_{m=1}^{\infty}\frac{1}{(2m-1)^2}\cos((2m-1)x)+\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin nx.$$

**b)** Parsevals identitet sier at

$$2a_0^2+\sum_{n=1}^{\infty}(a_n^2+b_n^2)=\frac{1}{\pi}\int_{-\pi}^{\pi}(f(x))^2\,\mathrm{d}x.$$

Siden

$$\frac{1}{\pi}\int_{-\pi}^{\pi}(f(x))^2\,\mathrm{d}x=\frac{1}{\pi}\int_0^{\pi}x^2\,\mathrm{d}x=\frac{\pi^2}{3}$$

får vi

$$2\cdot\frac{\pi^2}{16}+\sum_{n=1}^{\infty}\left(\frac{4}{\pi^2(2n-1)^4}+\frac{1}{n^2}\right)=\frac{\pi^2}{3},$$

som gir

$$\sum_{n=1}^{\infty}\left(\frac{4}{\pi^2(2n-1)^4}+\frac{1}{n^2}\right)=\frac{5}{24}\pi^2.$$

Kildesett: course=TMA4135 term=host year=2014 problem=4 file=tma4135_14h.pdf
