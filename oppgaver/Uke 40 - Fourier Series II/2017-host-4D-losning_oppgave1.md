### **Løsning til Oppgave 1**

**a)** Vi skal ha

$$f(x)=a_0+\sum_{n=1}^{\infty}a_n\cos nx\quad\text{for}\quad 0<x<\pi$$

Da må

$$a_0=\frac{1}{\pi}\int_0^{\pi}\left(\frac{\pi}{4}-\frac{x}{2}\right)\mathrm{d}x=0,$$

og

$$a_n=\frac{2}{\pi}\int_0^{\pi}\left(\frac{\pi}{4}-\frac{x}{2}\right)\cos nx\ \mathrm{d}x=\begin{cases}0&\text{hvis }n\text{ jevn}\\\frac{2}{\pi}\cdot\frac{1}{n^2}&\text{hvis }n\text{ er odde.}\end{cases}$$

Altså er

$$f(x)=\frac{2}{\pi}\sum_{n=0}^{\infty}\frac{1}{(2n+1)^2}\cos(2n+1)x\quad\text{for}\quad 0<x<\pi.$$

**b)** Merk at cosinusrekken konvergerer til den jevne $2\pi$-periodiske utvidelsen

$$g(x)=\begin{cases}\frac{\pi}{4}-\frac{x}{2}&\text{for }0\leq x\leq\pi\\\frac{\pi}{4}+\frac{x}{2}&\text{for }-\pi\leq x\leq 0\end{cases}$$

for alle $x$. Altså kan vi velge $x=0$ og beregne

$$\frac{\pi}{4}=f(0)=\frac{2}{\pi}\sum_{n=0}^{\infty}\frac{1}{(2n+1)^2}$$

slik at

$$\sum_{n=0}^{\infty}\frac{1}{(2n+1)^2}=\frac{\pi^2}{8}.$$

Kildesett: course=TMA4135 term=host year=2017 problem=1 file=tma4135_eksamen_h17.pdf
