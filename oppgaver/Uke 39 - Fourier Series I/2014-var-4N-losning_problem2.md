### **Solution to Problem 2**

**a)** The graph of $g$ takes the following form:

[Figure: Rutenettplott med horisontal akse merkt frå $-10$ til $10$ (merkt $x$) og vertikal akse merkt ved $-1$, $-0.5$, $0.5$ og $1$ (merkt $y$). Grafen til $g$ er ei trekkebølgje med periode $2\pi$: rett linje som stig frå $0$ til $1$ på $(0,\pi/2)$, fell gjennom $0$ i $\pi$ til $-1$ i $3\pi/2$ og stig tilbake til $0$ i $2\pi$, og gjentek seg; toppar med høgde $1$ ved $x=\pi/2+2\pi k$, botnar med $-1$ ved $x=-\pi/2+2\pi k$, nullpunkt i alle heile multiplar av $\pi$.]

From the theory developed in the course, we know that $g(x)$ has the Fourierseries representation

$$g(x)=a_{0}+\sum_{n=1}^{\infty}a_{n}\cos(nx)+b_{n}\sin(nx),$$

where $a_{0}$, $\{a_{n}\}_{n>1}$, and $\{b_{n}\}_{n>1}$ are determined by the Euler formulas

$$a_{0}=\frac{1}{2\pi}\int_{-\pi}^{\pi}g(x)\ dx,$$

$$a_{n}=\frac{1}{\pi}\int_{-\pi}^{\pi}g(x)\cos(nx)\ dx,$$

$$b_{n}=\frac{1}{\pi}\int_{-\pi}^{\pi}g(x)\sin(nx)\ dx.$$

Since $g(x)$ and $g(x)\cos(nx)$ are odd functions, we know that $a_{0}=0$ and $a_{n}=0$, for all $n\ge 1$. Moreover, since $g(x)\sin(nx)$ is an even function

$$\begin{aligned} b_{n}&=\frac{1}{\pi}\int_{-\pi}^{\pi}g(x)\sin(nx)\ dx\\ &=\frac{2}{\pi}\int_{0}^{\pi}f(x)\sin(nx)\ dx\\ &=\frac{4}{\pi^{2}}\int_{0}^{\frac{\pi}{2}}x\sin(nx)\ dx+\frac{4}{\pi^{2}}\int_{\frac{\pi}{2}}^{\pi}(\pi-x)\sin(nx)\ dx\\ &=\frac{4}{\pi^{2}}\left[-\frac{x\cos(nx)}{n}\bigg{|}_{x=0}^{x=\frac{\pi}{2}}+\int_{0}^{\frac{\pi}{2}}\frac{\cos(nx)}{n}\ dx\right]\\ &\qquad+\frac{4}{\pi^{2}}\left[-\frac{(\pi-x)\cos(nx)}{n}\bigg{|}_{x=\frac{\pi}{2}}^{x=\pi}-\int_{\frac{\pi}{2}}^{\pi}\frac{\cos(nx)}{n}\ dx\right]\\ &=\frac{4}{\pi^{2}n}\left[-\frac{\pi}{2}\cos\left(\frac{\pi}{2}n\right)+\frac{\pi}{2}\cos\left(\frac{\pi}{2}n\right)\right]+\frac{8}{\pi^{2}n^{2}}\sin\left(n\frac{\pi}{2}\right)\\ &=\frac{8}{\pi^{2}n^{2}}\sin\left(n\frac{\pi}{2}\right).\end{aligned}$$

We can further write this as

$$b_{n}=\begin{cases}\frac{8}{\pi^{2}n^{2}},&n=1,5,9,\ldots,\\[4pt] 0,&n=2,4,6,8,\ldots,,\\[4pt] -\frac{8}{\pi^{2}n^{2}}&n=3,7,11,\ldots,\end{cases}$$

Hence, $b_{n}$ is totally described by

$$b_{2n+1}=(-1)^{n}\frac{8}{\pi^{2}(2n+1)^{2}},\quad n=0,1,2,\ldots,\qquad b_{2n}=0,\quad n=1,2,3,\ldots.$$

The Fourier series of $g(x)$ is thus given by

$$g(x)=\sum_{n=0}^{\infty}\frac{(-1)^{n}8}{\pi^{2}(2n+1)^{2}}\sin((2n+1)x),$$

which concludes the answer.

**b)** By setting $x=\frac{\pi}{2}$ in the Fourierseries of $g(x)$, we find that

$$\begin{aligned} g\left(\frac{\pi}{2}\right)&=\sum_{n=0}^{\infty}\frac{(-1)^{n}8}{\pi^{2}(2n+1)^{2}}\sin\left((2n+1)\frac{\pi}{2}\right)\\ &=\sum_{n=0}^{\infty}\frac{(-1)^{n}8}{\pi^{2}(2n+1)^{2}}\sin\left(n\pi+\frac{\pi}{2}\right)\\ &=\sum_{n=0}^{\infty}\frac{(-1)^{n}8}{\pi^{2}(2n+1)^{2}}\left(-1\right)^{n}=\sum_{n=0}^{\infty}\frac{8}{\pi^{2}(2n+1)^{2}}.\end{aligned}$$

Since $g(\frac{\pi}{2})=1$, we see that

$$\sum_{n=0}^{\infty}\frac{1}{(2n+1)^{2}}=\frac{\pi^{2}}{8},$$

which is what we were asked to show.

**c)** From Parseval's identity, we have that

$$\begin{aligned} E&=\frac{2}{\pi}\int_{0}^{\pi}\left|S^{N}(x)-f(x)\right|^{2}\ dx\\ &=\frac{1}{\pi}\int_{-\pi}^{\pi}\left|S^{N}(x)-g(x)\right|^{2}\ dx\\ &=\sum_{n=N}^{\infty}b_{n}^{2}\\ &=\sum_{n=N}^{\infty}\frac{64}{\pi^{4}(2n+1)^{4}}\\ &\le\frac{64}{\pi^{4}}\left(\frac{1}{(2N+1)^{2}}\right)\sum_{n=N}^{\infty}\frac{1}{(2n+1)^{2}}\\ &<\frac{64}{\pi^{4}}\left(\frac{1}{(2N+1)^{2}}\right)\sum_{n=0}^{\infty}\frac{1}{(2n+1)^{2}}.\end{aligned}$$

From the previous exercise, we know the value of the sum on the right-hand side and hence we may conclude that

$$E<\frac{64}{\pi^{4}}\left(\frac{1}{(2N+1)^{2}}\right)\frac{\pi^{2}}{8}=\frac{8}{\pi^{2}}\frac{1}{(2N+1)^{2}}.$$

*Kjeldevarsel: Kasuslinja for $b_n$ er trykt med dobbel komma i andre kasus («$n=2,4,6,8,\ldots,,$») og utan komma etter brøken i tredje kasus; Euler-formlane er trykte for $\{a_n\}_{n>1}$ og $\{b_n\}_{n>1}$ medan det like etter står «for all $n\ge 1$». Alt er avtrykt som trykt. I c) er leddet $\sum_{n=N}^{\infty}b_n^2$ trykt med $b_n$-indeksing, men meint er halen $\sum_{n=N}^{\infty}b_{2n+1}^2$ av rekkja i a); sluttsummen og ulikskapen er korrekt.*

Kildesett: course=TMA4123 term=var year=2014 problem=2 file=v14-english.pdf
