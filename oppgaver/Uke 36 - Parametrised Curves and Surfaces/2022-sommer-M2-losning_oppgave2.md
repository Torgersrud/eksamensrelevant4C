### **Løsning til Oppgave 2**

Viss me skriv $\mathbf{r}(t) = (x(t), y(t), z(t))$, har me

$$x(t)^2 + y(t)^2 + z(t)^2 = t^4 + t^2(1 - t^2) + (1 - t^2) = t^4 + t^2 - t^4 + 1 - t^2 = 1.$$

Kurva ligg altso på kuleskalet med radius 1 og sentrum origo. For å finna einingstangenten reknar me ut

$$\mathbf{r}'(t) = \left(2t,\; \sqrt{1 - t^2} + t \cdot \frac{-2t}{2\sqrt{1 - t^2}},\; \frac{-2t}{2\sqrt{1 - t^2}}\right) = \left(2t,\; \sqrt{1 - t^2} - \frac{t^2}{\sqrt{1 - t^2}},\; \frac{-t}{\sqrt{1 - t^2}}\right) = \left(2t,\; \frac{1 - 2t^2}{\sqrt{1 - t^2}},\; \frac{-t}{\sqrt{1 - t^2}}\right),$$

$$|\mathbf{r}'(t)|^2 = 4t^2 + \frac{(1 - 2t^2)^2}{1 - t^2} + \frac{t^2}{1 - t^2} = \frac{4t^2 - 4t^4 + 1 - 4t^2 + 4t^4 + t^2}{1 - t^2} = \frac{1 + t^2}{1 - t^2},$$

$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|} = \frac{\sqrt{1 - t^2}}{\sqrt{1 + t^2}} \left(2t, \frac{1 - 2t^2}{\sqrt{1 - t^2}}, \frac{-t}{\sqrt{1 - t^2}}\right) = \left(\frac{2t\sqrt{1 - t^2}}{\sqrt{1 + t^2}},\; \frac{1 - 2t^2}{\sqrt{1 + t^2}},\; \frac{-t}{\sqrt{1 + t^2}}\right).$$

Kildesett: course=TMA4105 term=sommer year=2022 problem=2 file=tma4105_2022k.pdf
