### **Løsning til Oppgave 3**

Den komplekse fourierrekken til $f$ er gitt ved

$$\sum_{n=-\infty}^{\infty}c_ne^{inx}$$

der

$$\begin{aligned}c_n&=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,\mathrm{d}x=\int_0^{K}e^{-inx}\,\mathrm{d}x\\
&=\begin{cases}K,&n=0,\\ \frac{1}{in}(1-e^{-inK})&n\neq 0.\end{cases}\end{aligned}$$

Altså er den komplekse fourierrekken til $f$ gitt ved

$$K+\sum_{\substack{n=-\infty\\ n\neq 0}}^{\infty}\frac{1}{in}(1-e^{-inK})e^{inx}.$$

Kildesett: course=TMA4135 term=kont year=2013 problem=3 file=tma4135_13k.pdf
