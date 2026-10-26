### **Løsning til Oppgave 4**

**a)** Direkte utregning (med litt forenkling underveis, ikke vist her) gir

$$\frac{\partial \mathbf{r}}{\partial u} = \mathbf{i} + \frac{v}{u^2 + v^2}\,\mathbf{k}, \qquad \frac{\partial \mathbf{r}}{\partial v} = \mathbf{j} - \frac{u}{u^2 + v^2}\,\mathbf{k}, \qquad \mathbf{N} = \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} = -\frac{v}{u^2 + v^2}\,\mathbf{i} + \frac{u}{u^2 + v^2}\,\mathbf{j} + \mathbf{k}.$$

Videre blir

$$|\mathbf{N}|^2 = \frac{v^2}{(u^2 + v^2)^2} + \frac{u^2}{(u^2 + v^2)^2} + 1 = \frac{1}{u^2 + v^2} + 1 = \frac{1 + u^2 + v^2}{u^2 + v^2},$$

slik at arealet av $S$ blir

$$\text{areal}(S) = \iint_{u^2 + v^2 \leq 9} |\mathbf{N}(u, v)|\, du\, dv = \iint_{u^2 + v^2 \leq 9} \sqrt{\frac{1 + u^2 + v^2}{u^2 + v^2}}\, du\, dv$$

$$= \int_0^{2\pi} \int_0^3 \sqrt{\frac{1 + r^2}{r^2}}\; r\, dr\, d\theta = 2\pi \int_0^3 \sqrt{1 + r^2}\, dr$$

$$= 2\pi \left[ \frac{1}{2} x \sqrt{1 + x^2} + \frac{1}{2} \ln\left(x + \sqrt{1 + x^2}\right) \right]_0^3 = \pi \left( 3\sqrt{10} + \ln(3 + \sqrt{10}) \right).$$

**b)** Punktet $(\sqrt{3}, 1, \frac{1}{3}\pi)$ er $\mathbf{r}(\sqrt{3}, 1)$. En normalvektor i dette punktet er

$$\mathbf{N}(\sqrt{3}, 1) = -\frac{1}{4}\,\mathbf{i} + \frac{\sqrt{3}}{4}\,\mathbf{j} + \mathbf{k}.$$

En ligning for tangentplanet i dette punktet blir da

$$-\frac{1}{4}\left(x - \sqrt{3}\right) + \frac{\sqrt{3}}{4}(y - 1) + \left(z - \frac{1}{3}\pi\right) = 0,$$

som det kanskje passer å skrive som

$$-x + \sqrt{3}\,y + 4z = \frac{4}{3}\pi.$$

Kildesett: course=SIF5005 term=sommer year=2003 problem=4 file=sif5005_03k.pdf
