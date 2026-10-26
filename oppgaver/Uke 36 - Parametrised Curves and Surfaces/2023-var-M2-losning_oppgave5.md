### **Løsning til Oppgave 5**

Buelengden $s(T)$ fra $t = 1$ til $t = T$ er gitt ved

$$s(T) = \int_1^T |\mathbf{r}'(t)| \, dt.$$

Vi har $\mathbf{r}'(t) = (-\sin t, \cos t, (t - 1)^{1/2})$ og

$$|\mathbf{r}'(t)| = \sqrt{\sin^2 t + \cos^2 t + (t - 1)} = \sqrt{t},$$

slik at

$$s(T) = \int_1^T \sqrt{t} \, dt = \left[\frac{2}{3}t^{3/2}\right]_{t=1}^{t=T} = \frac{2}{3}\bigl(T^{3/2} - 1\bigr).$$

Kildesett: course=TMA4105 term=var year=2023 problem=5 file=tma4105_2023v.pdf
