### **Løsning til Oppgave 2**

I vårt tilfelle er

$$\mathbf{r}'(t) = \left(\frac{1}{2t}, \, \sqrt{3}, \, 3t\right)$$

slik at buelengden til kurven gitt ved $\mathbf{r}(t)$ for $1 \leqslant t \leqslant 2$ er

$$s = \int_1^2 |\mathbf{r}'(t)| \, dt = \int_1^2 \sqrt{\left(\frac{1}{2t}\right)^2 + \left(\sqrt{3}\right)^2 + (3t)^2} \, dt$$

$$= \int_1^2 \sqrt{\frac{1}{4t^2} + 3 + 9t^2} \, dt = \int_1^2 \sqrt{\frac{1 + 12t^2 + 36t^4}{4t^2}} \, dt$$

$$= \int_1^2 \sqrt{\frac{\left(1 + 6t^2\right)^2}{(2t)^2}} \, dt = \int_1^2 \frac{1 + 6t^2}{2t} \, dt$$

$$= \int_1^2 \left(\frac{1}{2t} + 3t\right) dt = \left[\frac{1}{2}\ln(t) + \frac{3}{2}t^2\right]_1^2 = \frac{1}{2}\ln(2) + \frac{9}{2}.$$

Kildesett: course=TMA4105 term=sommer year=2025 problem=2 file=tma4105_2025k.pdf
