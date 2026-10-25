### **Løsning til Oppgave 2**

a)  Skisse av grafen til $f$.

[Figur: Sagtann-kurve for $f$ på $-2\pi\le x\le 3\pi$: stigende linjestykker langs $y=x-2k\pi$ på hvert intervall $(2k\pi,(2k+1)\pi)$ og langs $y=x-(2k+1)\pi$ under $x$-aksen på intervallene $((2k-1)\pi,2k\pi)$, med sprang (avbrudd) i de odde multiplumene av $\pi$. Aksen er merket $-2\pi$, $-\pi$, $0$, $\pi$, $2\pi$, $3\pi$.]

$$f(3\pi)=0.$$

b)

$$f(x)=\sum_{n=1}^{\infty}b_n\sin nx$$

hvor koeffisientene $b_n$ er gitt ved

$$b_n=\frac{2}{\pi}\int_0^{\pi}f(x)\sin nx\,dx$$

$$=\frac{2}{\pi}\int_0^{\pi}x\sin nx\,dx$$

$$=\frac{2}{\pi}\left[\frac{-1}{n}x\cos nx+\frac{1}{n^2}\sin nx\right]_0^{\pi}$$

$$=\frac{-2}{n}\cos n\pi=\frac{2}{n}(-1)^{n+1}.$$

Altså

$$f(x)=2\left(\frac{\sin x}{1}-\frac{\sin 2x}{2}+\frac{\sin 3x}{3}-\frac{\sin 4x}{4}+\frac{\sin 5x}{5}-\cdots\right)$$

La $S=\sum_{n=0}^{\infty}(-1)^n\frac{1}{2n+1}$. Setter $x=\pi/2$ i uttrykket for Fourierrekken og får

$$\frac{\pi}{2}=f\left(\frac{\pi}{2}\right)=2\left(\frac{1}{1}-\frac{0}{2}+\frac{-1}{3}-\frac{0}{4}+\frac{1}{5}-\cdots\right)=2S,$$

altså

$$S=\frac{\pi}{4}.$$

Kildesett: course=TMA4135 term=kont year=2010 problem=2 file=tma4135_10k.pdf
