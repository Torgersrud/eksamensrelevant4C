### **Løsning til Oppgave 3**

a) Enten man regner komplekst, bruker formlene i Rottmann eller bruker 2 ganger delvisintegrasjon, får man, om man regner rett,

$$A(w) + iB(w) = \frac{1}{\pi} \int_{-\infty}^{\infty} f(x) \cos wx \, dx + i \frac{1}{\pi} \int_{-\infty}^{\infty} f(x) \sin wx \, dx.$$

Siden $f(x) = 0$ for $x < 0$ er dette

$$
\begin{aligned}
A(w) + iB(w) &= \frac{1}{\pi} \int_0^{\infty} e^{-x} e^{iwx} \, dx = \frac{1}{\pi} \int_0^{\infty} e^{-x + iwx} \, dx = \frac{1}{\pi} \left[ \frac{e^{(-1+iw)x}}{-1 + iw} \right]_0^{\infty} \\
&= \frac{1}{\pi} \frac{-1}{-1 + iw} = \frac{1}{\pi} \left( \frac{1}{1 + w^2} + i \frac{w}{1 + w^2} \right),
\end{aligned}
$$

og siden $A(w)$ og $B(w)$ er reelle funksjoner er

$$A(w) = \frac{1}{\pi} \frac{1}{1 + w^2} \qquad \text{og} \qquad B(w) = \frac{1}{\pi} \frac{w}{1 + w^2}.$$

b) Vi har

$$\frac{1}{2} (f(x^-) + f(x^+)) = \int_0^{\infty} A(w) \cos wx \, dw + \int_0^{\infty} B(w) \sin wx \, dw$$

Spesielt har vi for den odde delen av $f$, $f^{\text{odde}} = \frac{1}{2}(f(x) - f(-x))$, at

$$\frac{1}{2} (f(x) - f(-x)) = \int_0^{\infty} B(w) \sin wx \, dw.$$

Setter vi inn for $x = 2$ får vi

$$\frac{1}{2} e^{-2} = \frac{1}{\pi} \int_0^{\infty} \frac{w \sin 2}{1 + w^2} \, dw.$$

Følgelig er

$$\int_0^{\infty} \frac{w \sin 2w}{1 + w^2} \, dw = \frac{\pi}{2} e^{-2}.$$

Kildesett: course=TMA4135 term=kont year=2008 problem=3 file=tma4135_08k.pdf
