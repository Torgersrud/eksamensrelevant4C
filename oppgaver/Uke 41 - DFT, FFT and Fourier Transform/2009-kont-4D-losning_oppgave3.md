### **Løsning til Oppgave 3**

Dersom vi setter $h(x) = e^{-\frac{x^2}{2}}$ har vi $\hat{h}(w) = h(w) = e^{-\frac{w^2}{2}}$, og

$$\int_{-\infty}^{\infty} e^{-\frac{u^2}{2}} e^{-\frac{(x-u)^2}{2}} du = (h \star h)(x).$$

Konvolusjonsregelen viser at

$$\mathcal{F}\{h \star h\}(w) = \sqrt{2\pi} h(w) h(w) = \sqrt{2\pi} e^{-w^2}.$$

Fourierinversjon gir

$$\int_{-\infty}^{\infty} e^{-\frac{u^2}{2}} e^{-\frac{(x-u)^2}{2}} du = (h \star h)(x) = \sqrt{\pi} e^{-\frac{x^2}{4}}.$$

Kildesett: course=TMA4135 term=kont year=2009 problem=3 file=tma4135_09k.pdf
