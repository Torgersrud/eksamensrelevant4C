### **Løsning til Oppgave 2**

Kjerneregelen gir

$$\frac{dr}{d\theta} = \frac{1}{2}\bigl(1 + \cos(2\theta)\bigr)^{-1/2} \cdot \bigl(-2\sin(2\theta)\bigr) = -\frac{\sin(2\theta)}{\sqrt{1 + \cos(2\theta)}}$$

slik at

$$r^2 + \left(\frac{dr}{d\theta}\right)^2 = 1 + \cos(2\theta) + \frac{\sin^2(2\theta)}{1 + \cos(2\theta)} = \frac{\bigl(1 + \cos(2\theta)\bigr)^2 + \sin^2(2\theta)}{1 + \cos(2\theta)} = \frac{2 + 2\cos(2\theta)}{1 + \cos(2\theta)} = 2.$$

Buelengden er dermed

$$L = \int_0^{\pi\sqrt{2}} \sqrt{r^2 + \left(\frac{dr}{d\theta}\right)^2} \, d\theta = 2\pi.$$

Kildesett: course=TMA4105 term=var year=2024 problem=2 file=tma4105_2024v.pdf
