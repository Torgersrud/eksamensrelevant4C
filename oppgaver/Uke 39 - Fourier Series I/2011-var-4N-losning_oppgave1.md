### **Løsning til Oppgave 1**

**a)** Vi ser at utvidelsen av $f$ til en odde, $2\pi$-periodisk funksjon nettopp blir $\sin x$. Dermed blir fourierrekken for $g(x)$ ingenting annet enn $\sin x$.

Funksjonen $h(x)$ defineres på $[-\pi,0]$ som $h(x)=\sin(-x)=|\sin x|$. Det siste uttrykket kan benyttes for alle $x$, med andre ord, $h(x)=|\sin x|$. Funksjonene er vist på Fig. 1.

[Figur: To stablede plott med vannrett akse merket $x/\pi$ fra $-2$ til $2$ med merker for hver halv eining og loddrett akse fra $-1$ til $1$. Øvste panel, aksetittel «g og f»: heile $2\pi$-periodiske $\sin x$-kurva i grønt, med stykket $f(x)=\sin x$ på $[0,\pi]$ teikna i raudt. Nedste panel, aksetittel «h og f»: den like kurva $h(x)=|\sin x|$ med typiske «buer» i blått over heile aksen, med same raude stykke av $f$ på $[0,\pi]$.]

Figure 1: Funksjonen $g$ og $f$ (øverst), og $h$ og $f$ (nederst).

**b)** Siden $h$ er en like funksjon med periode $2\pi$, blir det bare snakk om å finne cos-rekken. For $a_0$ får vi

$$a_0=\frac{1}{2\pi}\int_{-\pi}^{\pi}h(x)\,dx=\frac{1}{\pi}\int_0^{\pi}\sin x\,dx=\frac{2}{\pi}.$$

På samme måte finner vi $a_n$ for $n=2,4,\cdots$ ved bruk av den oppgitte formelen:

$$a_n=\frac{2}{2\pi}\int_{-\pi}^{\pi}\sin x\cos nx\,dx=\frac{2}{\pi}\int_0^{\pi}\sin x\cos nx\,dx=\frac{2}{\pi}\left(-\frac{2}{(n-1)(n+1)}\right).$$

Merk at $a_n$ for $n=1,3,\cdots$ er oppgitt til å være lik 0, slik at

$$h(x)=\frac{2}{\pi}-\frac{4}{\pi}\sum_{n=2,4,\cdots}^{\infty}\frac{1}{n^2-1}\cos nx=\frac{2}{\pi}-\frac{4}{\pi}\sum_{k=1}^{\infty}\frac{1}{(2k)^2-1}\cos 2kx.$$

For $x\in[0,\pi]$ er $h(x)=f(x)=\sin x$. For $x=0$ finner vi spesielt

$$0=\frac{2}{\pi}-\frac{4}{\pi}\sum_{k=1}^{\infty}\frac{1}{(2k)^2-1}\cos 0,$$

og dermed

$$\sum_{k=1}^{\infty}\frac{1}{(2k)^2-1}=\frac{1}{2}.$$

Denne summen kan alternativt finnes direkte uten bruk av fourierrekke ved å observere at $\frac{1}{n^2-1}=\frac{1}{2}\left(\frac{1}{n-1}-\frac{1}{n+1}\right)$ og skrive

$$\sum_{n=2,4,\cdots}^{\infty}\frac{1}{n^2-1}=\frac{1}{2}\left(1-\frac{1}{3}+\frac{1}{3}-\frac{1}{5}+\frac{1}{5}-\frac{1}{7}+\cdots\right)=\frac{1}{2}.$$

For den andre summen ser vi først at

$$\cos 2k\left(\frac{\pi}{2}\right)=\cos k\pi=(-1)^k,$$

og kan dermed sette opp

$$h\left(\frac{\pi}{2}\right)=\sin\frac{\pi}{2}=1=\frac{2}{\pi}-\frac{4}{\pi}\sum_{k=1}^{\infty}\frac{1}{(2k)^2-1}\,(-1)^k\ .$$

Følgelig blir

$$\sum_{k=1}^{\infty}\frac{(-1)^k}{(2k)^2-1}=-\frac{\pi-2}{4}\approx-0.2854.$$

Kildesett: course=TMA4125 term=var year=2011 problem=1 file=tma4125nbokmaal.pdf
