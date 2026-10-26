### **Løsning til Oppgave 2**

La $f(x, y) = x^2 + e^{xy}$ slik at

$$\nabla f(x, y) = \left(\frac{\partial f}{\partial x}(x, y), \; \frac{\partial f}{\partial y}(x, y)\right) = (2x + ye^{xy}, \; xe^{xy}).$$

Dermed er $\nabla f(1, 0) = (2, 1)$.

Siden $f$ er en deriverbar funksjon vet vi at $D_{\mathbf{u}} f(1, 0) = \nabla f(1, 0) \cdot \mathbf{u}$. Altså må $\nabla f(1, 0) \cdot \mathbf{u} = (2, 1) \cdot \mathbf{u} = 0$ for at $D_{\mathbf{u}} f(1, 0) = 0$.

Siden $\pm(-1, 2) \cdot (2, 1) = 0$, er retningene $\mathbf{u}$ gitt ved

$$\mathbf{u} = \pm \frac{1}{|(-1, 2)|}(-1, 2) = \pm \frac{1}{\sqrt{5}}(-1, 2).$$

Kildesett: course=TMA4105 term=var year=2019 problem=2 file=tma4105_2019v.pdf
