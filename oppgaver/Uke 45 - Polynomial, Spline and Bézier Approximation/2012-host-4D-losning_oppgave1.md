### **Løsning til Oppgave 1**

Ved lagrangeinterpolasjon har vi

$$\begin{aligned}p_2(x)&=f(0)\frac{(x-1/2)(x-3/2)}{(0-1/2)(0-3/2)}+f(1/2)\frac{(x-0)(x-3/2)}{(1/2-0)(1/2-3/2)}+f(3/2)\frac{(x-0)(x-1/2)}{(3/2-0)(3/2-1/2)}\\ &=-2x\left(x-\frac{3}{2}\right)-\frac{2}{3}x\left(x-\frac{1}{2}\right)\\ &=\frac{2}{3}x(5-4x),\end{aligned}$$

der vi brukte at $f(0)=\sin 0=0$. Vi kunne også brukt Newtons dividerte differanser, svaret blir det samme.

Kildesett: course=TMA4135 term=host year=2012 problem=1 file=tma4135_12h.pdf
