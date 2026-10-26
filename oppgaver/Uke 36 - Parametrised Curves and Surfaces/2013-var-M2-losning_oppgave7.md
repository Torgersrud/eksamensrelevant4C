### **Løsning til Oppgave 7**

Sylinderen har radius $r = 1$, og kan derfor parametriseres ved $(\theta, z)$ der

$$S : (\cos \theta, \sin \theta, z), \quad 0 \le \theta < 2\pi, \; z \ge 0.$$

I disse koordinatene så korresponderer $P_1$ til $(r, \theta, z) = (1, 0, 0)$, og $P_2$ til $(r, \theta, z) = (1, \pi/2, h)$. For

$$C : \mathbf{r}(\theta) = (\cos \theta, \sin \theta, f(\theta)), \quad 0 \le \theta \le \frac{\pi}{2}, \qquad f(0) = 0, \quad f\left(\frac{\pi}{2}\right) = h,$$

en kurve på $S$ fra $P_1$ til $P_2$, så er avstanden mellom $P_1$ og $P_2$ gitt ved

$$L(C) = \int_0^{\pi/2} \left|\frac{d\mathbf{r}}{d\theta}\right| d\theta = \int_0^{\pi/2} \sqrt{\cos^2 \theta + \sin^2 \theta + \left(\frac{df}{d\theta}\right)^2} \, d\theta = \int_0^{\pi/2} \sqrt{1 + \left(\frac{df}{d\theta}\right)^2} \, d\theta,$$

der $f(0) = 0$ og $f(\pi/2) = h$.

Dermed sammenfaller $L(C)$ med lengden til grafen til $f$ på intervallet $0 \le \theta \le \pi/2$, som igjen betyr at den optimale $f(\theta)$ beskriver den korteste veien mellom $(0, 0)$ og $(\pi/2, h)$ i $(\theta, z)$-planet. Løsningen på dette problemet er å ta den rette linjen mellom $(0, 0)$ og $(\pi/2, h)$ gitt ved

$$f(\theta) = \frac{2h}{\pi}\theta, \quad 0 \le \theta \le \frac{\pi}{2}.$$

Lengden til den korteste veien er så

$$\int_0^{\pi/2} \sqrt{1 + \left(\frac{2h}{\pi}\right)^2} \, d\theta = \frac{\pi}{2}\sqrt{1 + \left(\frac{2h}{\pi}\right)^2} = \sqrt{\left(\frac{\pi}{2}\right)^2 + h^2},$$

som, i den flate formuleringen av problemet, kan sjekkes direkte ved å benytte Pytagoras' teorem.

Kildesett: course=TMA4105 term=var year=2013 problem=7 file=tma4105_13v.pdf
