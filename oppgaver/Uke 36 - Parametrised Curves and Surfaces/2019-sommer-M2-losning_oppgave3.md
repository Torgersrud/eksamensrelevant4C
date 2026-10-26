### **Løsning til Oppgave 3**

I vårt tilfelle er

$$\mathbf{r}'(t) = \left(\frac{4}{t}, \; 2t, \; 4\right)$$

slik at

$$|\mathbf{r}'(t)| = \sqrt{\frac{16}{t^2} + 4t^2 + 16} = \sqrt{\frac{4t^4 + 16t^2 + 16}{t^2}} = \frac{2\sqrt{(t^2 + 2)^2}}{t} = \frac{2(t^2 + 2)}{t} = 2t + \frac{4}{t}.$$

Buelengden til $C$ er dermed

$$s = \int_C ds = \int_1^e |\mathbf{r}'(t)| \, dt = \int_1^e \left(2t + \frac{4}{t}\right) dt = \left[t^2 + 4\ln t\right]_1^e = e^2 + 3.$$

Kildesett: course=TMA4105 term=sommer year=2019 problem=3 file=tma4105_2019k_web.pdf
