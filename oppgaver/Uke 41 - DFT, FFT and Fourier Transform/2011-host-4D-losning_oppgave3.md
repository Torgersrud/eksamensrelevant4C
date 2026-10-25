### **Løsning til Oppgave 3**

a)  The transform is given by

$$\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{0}e^{x(a-i\omega)}dx=\frac{1}{\sqrt{2\pi}}1/(a-i\omega)=\frac{1}{\sqrt{2\pi}}\frac{a+i\omega}{a^2+\omega^2}.$$

The Fourier inversion formula gives at $x=-1$, for $a=1$

$$e^{-1}=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{(1+i\omega)(\cos\omega-i\sin\omega)}{1+\omega^2}d\omega=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{(\cos\omega+\omega\sin\omega)}{1+\omega^2}d\omega$$

Similarly, for $x=1$ we obtain

$$0=f(1)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{(1+i\omega)(\cos\omega+i\sin\omega)}{1+\omega^2}d\omega=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{(\cos\omega-\omega\sin\omega)}{1+\omega^2}d\omega$$

Hence, if the two integrals are $I_1$ and $I_2$ we have $I_1=I_2$ and $I_1+I_2=2\pi e^{-1}$, and thus

$$I_1=I_2=\pi e^{-1}.$$

*Kjeldevarsel: I løsningsforslagets punkt a) er transformen rekna ut ved å integrere over $x<0$ for $e^{ax}$, dvs. den speilte funksjonen, og gir $\frac{1}{\sqrt{2\pi}}\frac{a+i\omega}{a^2+\omega^2}$. For den oppgitte funksjonen ($e^{-ax}$ for $x>0$, $0$ for $x<0$) blir transformen $\frac{1}{\sqrt{2\pi}}\frac{a-i\omega}{a^2+\omega^2}$, og rollene til $x=1$ og $x=-1$ byttes i punkt b). Sluttresultatet påverkas ikke: vi har numerisk kontrollert at $I_1=I_2=\pi e^{-1}$.*

Kildesett: course=TMA4135 term=host year=2011 problem=3 file=tma4135_11h.pdf
