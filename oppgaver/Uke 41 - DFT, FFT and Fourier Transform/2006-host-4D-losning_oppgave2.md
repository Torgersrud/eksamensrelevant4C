### **Løsning til Oppgave 2**

Vi bruker formelen (Rottman s.176):

$$\mathcal{F}(f*g)=\sqrt{2\pi}\mathcal{F}(f)\mathcal{F}(g)$$

og får

$$\begin{aligned}\mathcal{F}(h)&=\mathcal{F}(e^{-x^2}*e^{-x^2})\\
&=\sqrt{2\pi}\mathcal{F}(e^{-x^2})\mathcal{F}(e^{-x^2})\\
&=\sqrt{2\pi}\left(\frac{1}{\sqrt{2}}e^{-\frac{w^2}{4}}\right)^2.\end{aligned}$$

Derfor,

$$\mathcal{F}(h)=\sqrt{\frac{\pi}{2}}e^{-\frac{w^2}{2}}.$$

For $a=\frac{1}{2}$, formlen som er gitt i oppgaveteksten gir $\mathcal{F}(e^{-\frac{1}{2}x^2})=e^{-\frac{w^2}{2}}$. Derfor,

$$h=\mathcal{F}^{-1}\mathcal{F}(h)=\sqrt{\frac{\pi}{2}}\mathcal{F}^{-1}(e^{-\frac{w^2}{2}})$$

og

$$h=\sqrt{\frac{\pi}{2}}e^{-\frac{x^2}{2}}.$$

Kildesett: course=TMA4135 term=host year=2006 problem=2 file=tma4135_06h.pdf
