### **Løsning til Oppgave 4**

Siden $f$ er odde, er dens Fourier-rekke på formen

$$S(x)=\sum_{n=1}^{\infty}b_n\sin nx$$

med

$$\begin{aligned}b_n&=\frac{2}{\pi}\int_0^{\pi}x\sin nx\ \mathrm dx\\
&=\frac{2}{\pi}\left[\frac{1}{n^2}\sin nx-\frac{x}{n}\cos nx\right]_{n=0}^{x=\pi}\\
&=(-1)^{n+1}\frac{2}{n},\end{aligned}$$

altså

$$S(x)=2\sum_{n=1}^{\infty}\frac{(-1)^{n+1}}{n}\sin nx.$$

$f$ er diskontinuerlig i $\pi$, så

$$S(\pi)=\frac{1}{2}\left(\lim_{x\to\pi^+}f(x)+\lim_{x\to\pi^-}f(x)\right)=\frac{1}{2}(-\pi+\pi)=0.$$

Grafen til $S$ på $[-2\pi,2\pi]$ er vist i figur 1.

[Figur 1: Sagtannkurve for $S$ på $[-2\pi,2\pi]$: stigende linjestykker $y=x$ på $(-\pi,\pi)$ med hopp ned ved $x=\pm\pi$ (linjestykkene går fra $-3$ til $3$), og prikker i $(\pm\pi,0)$. Aksene er merket fra $-6$ til $6$ horisontalt og $-4$ til $4$ vertikalt. Prikkene er $(\pm\pi,S(\pm\pi))$.]

Kildesett: course=TMA4135 term=host year=2015 problem=4 file=tma4135_15h.pdf
