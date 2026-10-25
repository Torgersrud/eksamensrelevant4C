### **Løsning til Oppgave 2**

Fra formelarket eller tabeller vet vi at

$$\mathscr F(f_a)(\omega)=\frac{1}{\sqrt{2a}}e^{-\omega^2/(4a)}.$$

Fouriertransformasjonen tar konvolsjon til produkt, så

$$\begin{aligned}\mathscr F(f_a*f_b)(\omega)&=\sqrt{2\pi}\mathscr F(f_a)(\omega)\mathscr F(f_b)(\omega)=\sqrt{\frac{\pi}{2ab}}e^{-\left(\frac{1}{4a}+\frac{1}{4b}\right)\omega^2}\\
&=\sqrt{\frac{2c\pi}{2ab}}\sqrt{\frac{1}{2c}}e^{-\omega^2/(4c)}=\sqrt{\frac{c\pi}{ab}}\mathscr F(f_c)(\omega),\end{aligned}$$

hvor

$$\frac{1}{4c}=\frac{1}{4a}+\frac{1}{4b},$$

altså

$$c=\frac{1}{a^{-1}+b^{-1}}=\frac{ab}{a+b}.$$

Invers-transformasjon gir

$$(f_a*f_b)(x)=\sqrt{\frac{\pi}{a+b}}f_c(x)=\sqrt{\frac{\pi}{a+b}}e^{-cx^2}=\sqrt{\frac{\pi}{a+b}}e^{-abx^2/(a+b)}.$$

Kildesett: course=TMA4135 term=host year=2015 problem=2 file=tma4135_15h.pdf
