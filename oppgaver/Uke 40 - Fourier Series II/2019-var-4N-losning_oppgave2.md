### **Løsning til Oppgave 2**

**a)** Vi antar at det er mulig å skrive

$$f(x)=\sum_{n=-\infty}^{\infty}c_ne^{inx}$$

på intervallet $[-\pi,\pi]$. Først observerer vi at

$$\int_{-\pi}^{\pi}e^{i(n-m)x}\,dx=\begin{cases}2\pi & n=m\\ 0 & n\neq m\end{cases}$$

Dersom vi ganger likningen

$$f(x)=\sum_{n=-\infty}^{\infty}c_ne^{inx}$$

med $e^{-imx}$ på begge sider og integrerer fra $-\pi$ til $\pi$, får vi

$$\int_{-\pi}^{\pi}f(x)e^{-imx}\,dx=\int_{-\pi}^{\pi}\sum_{n=-\infty}^{\infty}c_ne^{inx}e^{-inx}\,dx=\sum_{n=-\infty}^{\infty}c_n\int_{-\pi}^{\pi}e^{i(n-m)x}\,dx=2\pi c_m$$

eller

$$c_n=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,dx.$$

*Kjeldevarsel: i utgangspunktet for leddet $e^{inx}e^{-inx}$ i mellomsteget står det $e^{-inx}$ der det må stå $e^{-imx}$ — skrivefeil i fasitfila, sluttresultatet er riktig.*

**b)** Vi beregner

$$\begin{aligned}c_n&=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,dx=\frac{1}{2\pi}\int_{-\pi}^{0}e^{x}e^{-inx}\,dx+\frac{1}{2\pi}\int_{0}^{\pi}e^{-x}e^{-inx}\,dx\\
&=\frac{1}{2\pi}\int_{-\pi}^{0}e^{(1-in)x}\,dx+\frac{1}{2\pi}\int_{0}^{\pi}e^{(1+in)x}\,dx\\
&=\frac{1}{2\pi(1-in)}\left(1-e^{-(1-in)\pi}\right)+\frac{1}{2\pi(1+in)}\left(1-e^{-(1+in)\pi}\right)\\
&=\frac{\left(1-e^{-\pi}(-1)^n\right)}{2\pi}\left(\frac{1}{1-in}+\frac{1}{1+in}\right)=\frac{1}{\pi}\frac{\left(1-e^{-\pi}(-1)^n\right)}{1+n^2}\end{aligned}$$

slik at

$$f(x)=\frac{1}{\pi}\sum_{n=-\infty}^{\infty}\frac{\left(1-e^{-\pi}(-1)^n\right)}{1+n^2}e^{inx}=\frac{1-e^{-\pi}}{\pi}+\frac{2}{\pi}\sum_{n=1}^{\infty}\frac{\left(1-e^{-\pi}(-1)^n\right)}{1+n^2}\cos nx.$$

Merk at det er trygt å skrive likhetstegn mellom $f$ og fourierrekken siden $f$ er kontinuerlig og $f(-\pi)=f(\pi)$. Under er et plot av $f$ og $S_5$.

[Figure: plot over $[-4,4]$ med $f(x)=e^{-|x|}$ (glatt, spiss topp ved $1$ i $x=0$) og den femte partisums-svingen $S_5$ rundt kurven med Gibbs-liknende topp like over $1$ ved $0$.]

Kildesett: course=TMA4125 term=var year=2019 problem=2 file=eksamen-TMA4125-v19-BM.pdf
