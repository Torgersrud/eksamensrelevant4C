### **Løsning til Oppgave 4**

Ved å benytte den inverse Fouriertransformen får vi

$$e^{-ax^2}=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{1}{\sqrt{2a}}e^{\frac{-w^2}{4a}}\left(\cos wx+i\sin wx\right)\,dw.$$

Siden $\sin$ er en odde funksjon og $\cos$ og $e^{\frac{-w^2}{4a}}$ er likefunksjoner har vi

$$e^{-ax^2}=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{1}{\sqrt{2a}}e^{\frac{-w^2}{4a}}\cos wx\,dw.$$

Ved å sette $a=\frac{1}{4}$ finner vi at

$$\int_{-\infty}^{\infty}e^{-w^2}\cos wx\,dw=\sqrt{\pi}e^{-\frac{x^2}{4}},$$

og ved å sette $x=1$ finner vi at

$$\int_{-\infty}^{\infty}e^{-w^2}\cos w\,dw=\sqrt{\pi}e^{-\frac{1}{4}},\quad\text{og}\quad\int_{-\infty}^{\infty}e^{-w^2}\sin w\,dw=0.$$

Kildesett: course=TMA4135 term=kont year=2010 problem=4 file=tma4135_10k.pdf
