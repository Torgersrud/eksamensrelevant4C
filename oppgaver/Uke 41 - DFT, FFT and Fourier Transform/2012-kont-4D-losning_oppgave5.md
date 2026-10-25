### **Løsning til Oppgave 5**

Vi finner at

$$\begin{aligned}\hat{f}(w)&=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-|x|}\cos x\,e^{-iwx}dx\\
&=\frac{1}{2\sqrt{2\pi}}\left(\int_{-\infty}^{0}(e^{(1+i-iw)x}+e^{(1-i-iw)x})dx+\int_{0}^{\infty}(e^{(-1+i-iw)x}+e^{(-1-i-iw)x})dx\right)\\
&=\frac{1}{2\sqrt{2\pi}}\left(\frac{1}{1+i-iw}+\frac{1}{1-i-iw}-\frac{1}{-1+i-iw}-\frac{1}{-1-i-iw}\right)\\
&=\frac{1}{\sqrt{2\pi}}\left(\frac{1}{1+(1-w)^2}+\frac{1}{1+(1+w)^2}\right).\end{aligned}$$

Kildesett: course=TMA4135 term=kont year=2012 problem=5 file=tma4135_12k.pdf
