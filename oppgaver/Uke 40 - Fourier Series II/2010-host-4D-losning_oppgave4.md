### **Løsning til Oppgave 4**

a)  Grafen til den $2\pi$-periodiske utvidelsen til $f(x)$ er gitt ved figuren under.

[Figur: $x$-akse tallfestet med merker fra $-3\pi$ til $3\pi$ og $y$-akse merket $f(x)$ med merker i høyde $e^{-\pi}$ og $e^{\pi}$. Kurven består av kongruente stykker av den avtakende eksponentialfunksjonen på hvert intervall $((2k-1)\pi,(2k+1)\pi)$: på hvert intervall starter kurven ved høyde $e^{\pi}$ like etter venstre endepunkt, minker raskt mot høyre og ender like over høyde $e^{-\pi}$ like før høyre endepunkt, der den hopper vertikalt opp til $e^{\pi}$ igjen. Hoppene skjer i $x=\pm\pi$ og $x=\pm3\pi$ (og utenfor tallfestingen).]

Den komplekse Fourier-rekken til $f(x)$ er gitt ved

$$f(x)\sim\sum_{n=-\infty}^{\infty}c_n e^{inx},$$

der

$$
\begin{aligned}
c_n&=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,\mathrm{d}x=\frac{1}{2\pi}\int_{-\pi}^{\pi}e^{-x}e^{-inx}\,\mathrm{d}x=\frac{1}{2\pi}\left[-\frac{1}{1+in}e^{-(1+in)x}\right]_{-\pi}^{\pi}\\
&=\frac{1}{2\pi}\left(-\frac{1}{1+in}e^{-\pi}e^{-in\pi}+\frac{1}{1+in}e^{\pi}e^{in\pi}\right)=\frac{1}{2\pi}\frac{1}{1+in}(-1)^n(e^{\pi}-e^{-\pi})\\
&=\frac{\sinh\pi}{\pi}\frac{(-1)^n(1-in)}{1+n^2}.
\end{aligned}
$$

Altså er den komplekse Fourier-rekken til $f(x)$ gitt ved

$$f(x)\sim\frac{\sinh\pi}{\pi}\sum_{n=-\infty}^{\infty}\frac{(-1)^n(1-in)}{1+n^2}e^{inx}.$$

b)  Ettersom $f(x)$ er kontinuerlig i $x=0$ får vi at

$$
\begin{aligned}
f(0)=1&=\frac{\sinh\pi}{\pi}\sum_{n=-\infty}^{\infty}\frac{(-1)^n(1-in)}{1+n^2}\\
&=\frac{\sinh\pi}{\pi}\left(\cdots-\frac{1+3i}{1+3^2}+\frac{1+2i}{1+2^2}-\frac{1+i}{1+1^2}+1-\frac{1-i}{1+1^2}+\frac{1-2i}{1+2^2}-\frac{1-3i}{1+3^2}+\cdots\right)\\
&=\frac{2\sinh\pi}{\pi}\sum_{n=2}^{\infty}\frac{(-1)^n}{1+n^2},
\end{aligned}
$$

slik at

$$\sum_{n=2}^{\infty}\frac{(-1)^n}{1+n^2}=\frac{\pi}{2\sinh\pi}.$$

Ettersom $f(x)$ har et sprang i $x=\pi$ får vi at

$$
\begin{aligned}
\frac{1}{2}\big[f(\pi^{+})+f(\pi^{-})\big]=\cosh\pi&=\frac{\sinh\pi}{\pi}\sum_{n=-\infty}^{\infty}\frac{(-1)^n(1-in)}{1+n^2}e^{in\pi}\\
&=\frac{\sinh\pi}{\pi}\sum_{n=-\infty}^{\infty}\frac{(-1)^n(1-in)}{1+n^2}(-1)^n\\
&=\frac{\sinh\pi}{\pi}\sum_{n=-\infty}^{\infty}\frac{1-in}{1+n^2}\\
&=\frac{2\sinh\pi}{\pi}\left(1+\sum_{n=2}^{\infty}\frac{1}{1+n^2}\right),
\end{aligned}
$$

slik at

$$\sum_{n=2}^{\infty}\frac{1}{1+n^2}=\frac{\pi\cosh\pi}{2\sinh\pi}-1=\frac{\pi}{2\tanh\pi}-1.$$

Kildesett: course=TMA4135 term=host year=2010 problem=4 file=tma4135_10h.pdf
