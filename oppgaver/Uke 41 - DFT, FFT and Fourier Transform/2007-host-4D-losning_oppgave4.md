### **Løsning til Oppgave 4**

Siden funksjonen $\sin(xw)$ er en odde funksjon blir $\int_{-1}^{1} e^{-ixw} dx = \int_{-1}^{1} \cos(xw) dx$. Altså blir

$$\frac{1}{\sqrt{2\pi}} \int_{-1}^{1} e^{-ixw} dx = \frac{1}{\sqrt{2\pi}} \int_{-1}^{1} \cos(xw) dx = \sqrt{\frac{2}{\pi}} \int_0^1 \cos(xw) dx = \sqrt{\frac{2}{\pi}} \left[ \frac{\sin(xw)}{w} \right]_0^1 = \sqrt{\frac{2}{\pi}} \frac{\sin(w)}{w}.$$

Dersom $f(x)$ betegner funksjonen som er gitt ved

$$f(x) = \begin{cases} 0 & \text{for} \quad |x| > 1 \\ \frac{1}{2} & \text{for} \quad |x| = 1 \\ 1 & \text{for} \quad |x| < 1 \end{cases}$$

har vi nettopp regnet ut at $\hat{f}(w) = \sqrt{\frac{2}{\pi}} \frac{\sin(w)}{w}$, og derfor er $f(x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} e^{ixw} \hat{f}(w) dw$. Siden $\hat{f}(w)$ er en likefunksjon er $f(x) = \sqrt{\frac{2}{\pi}} \int_0^{\infty} \cos(xw) \hat{f}(w) dw$. Ved å sette inn $\hat{f}(w)$ har vi $f(x) = \frac{2}{\pi} \int_0^{\infty} \frac{\cos(xw) \sin w}{w} dw$. Ved å velge $x = \frac{1}{2}$ får vi

$$\int_0^{\infty} \frac{\cos(\frac{1}{2}w) \sin w}{w} dw = \frac{\pi}{2}.$$

Kildesett: course=TMA4135 term=host year=2007 problem=4 file=tma4135_07h.pdf
