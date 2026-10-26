### **Løsning til Oppgave 4**

I vårt tilfelle er

$$\nabla f(x, y) = (2x - 3y + 2y^2 + 1, \; 4xy - 3x)$$

slik at $\nabla f(x, y) = (0, 0)$ svarer til

$$2x - 3y + 2y^2 + 1 = 0 \qquad (1)$$
$$4xy - 3x = 0. \qquad (2)$$

Fra (2) følger det at $x = 0$ eller $y = 3/4$. Innsatt for $x = 0$ i (1) medfører at $2y^2 - 3y + 1 = (2y - 1)(y - 1) = 0$ som har løsning $y = 1/2$ og $y = 1$. Innsatt for $y = 3/4$ i (1) medfører at $2x - 9/4 + 18/16 + 1 = 2x - 1/8 = 0$ som har løsning $x = 1/16$. Altså er $(0, 1/2)$, $(0, 1)$ og $(1/16, 3/4)$ kritiske punkter til $f$.

Legg merke til at

$$\frac{\partial^2 f}{\partial x^2}(x, y) = 2, \quad \frac{\partial^2 f}{\partial y^2}(x, y) = 4x \quad \text{og} \quad \frac{\partial^2 f}{\partial y\,\partial x}(x, y) = 4y - 3$$

slik at

$$\mathcal{D}(x, y) = \frac{\partial^2 f}{\partial x^2}(x, y) \cdot \frac{\partial^2 f}{\partial y^2}(x, y) - \left(\frac{\partial^2 f}{\partial y\,\partial x}(x, y)\right)^2 = 8x - (4y - 3)^2.$$

Siden

$$\mathcal{D}\left(0, \tfrac{1}{2}\right) = -1 < 0, \quad \mathcal{D}(0, 1) = -1 < 0 \quad \text{og} \quad \mathcal{D}\left(\tfrac{1}{16}, \tfrac{3}{4}\right) = \tfrac{1}{2} > 0$$

og $\dfrac{\partial^2 f}{\partial x^2}(x, y) = 2 > 0$ gir annenderiverttesten at $(0, 1/2)$ og $(0, 1)$ er sadelpunkter, og $(1/16, 3/4)$ er et lokalt minimumspunkt til $f$.

Kildesett: course=TMA4105 term=sommer year=2017 problem=4 file=tma4105_2017k.pdf
