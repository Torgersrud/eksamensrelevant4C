### **Løsning til Oppgave 2**

For å finne en likning for tangentplanet til flaten

$$x = u^2 - v^2, \qquad y = u, \qquad z = \arctan(u/v)$$

i punktet $(0, 1, \pi/4)$, trenger vi en normalvektor til flaten i punktet. Vi kan bruke det fundamentale vektorproduktet

$$\mathbf{N}(u, v) = \frac{\partial \mathbf{r}}{\partial u} \times \frac{\partial \mathbf{r}}{\partial v} \quad \text{der} \quad \mathbf{r}(u, v) = (u^2 - v^2)\mathbf{i} + u\mathbf{j} + \arctan(u/v)\mathbf{k}.$$

Punktet $(0, 1, \pi/4)$ svarer til $u = 1$ og $v = 1$ (siden $y = u = 1$ og $\arctan(u/v) = \pi/4$ gir $u = v = 1$, og da er $x = u^2 - v^2 = 0$). Vi får

$$\mathbf{N}(u, v) = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2u & 1 & \frac{1}{1 + u^2/v^2} \cdot \frac{1}{v} \\ -2v & 0 & \frac{1}{1 + u^2/v^2} \cdot \left(-\frac{u}{v^2}\right) \end{vmatrix} = -\frac{u}{u^2 + v^2}\mathbf{i} + \frac{2u^2 - 2v^2}{u^2 + v^2}\mathbf{j} + 2v\mathbf{k}.$$

I punktet er $u = 1$ og $v = 1$, slik at $\mathbf{N}(1, 1) = -\frac{1}{2}\mathbf{i} + 0\mathbf{j} + 2\mathbf{k}$.

Tangenten har derfor en likning på formen

$$\mathbf{N}(1, 1) \cdot \left\langle x - 0, \; y - 1, \; z - \frac{\pi}{4} \right\rangle = 0$$

$$-\frac{1}{2}x + 2z - \frac{\pi}{2} = 0$$

$$z = \frac{1}{4}(x + \pi).$$

Kildesett: course=TMA4105 term=var year=2008 problem=2 file=tma4105_08v.pdf
