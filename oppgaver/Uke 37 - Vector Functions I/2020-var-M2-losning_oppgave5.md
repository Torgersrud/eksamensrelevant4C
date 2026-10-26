### **Løsning til Oppgave 5**

Utregning av gradienten gir

$$\nabla f(1, 1) = \left.\left(\frac{x}{\sqrt{x^2 + 3y}}, \; \frac{3}{2\sqrt{x^2 + 3y}}\right)\right|_{(x, y) = (1, 1)} = \left(\frac{1}{2}, \; \frac{3}{4}\right).$$

Tangenten til $y = x^2$ i punktet $(1, 1)$ kan uttrykkes som $y = 2x - 1$, så $\mathbf{u}$ har samme retning som vektoren $(1, 2)$. Siden $\mathbf{u}$ skal være en enhetsvektor får vi $\mathbf{u} = \frac{1}{\sqrt{5}}(1, 2)$. Videre får vi

$$D_{\mathbf{u}} f(1, 1) = \nabla f(1, 1) \cdot \mathbf{u} = \frac{1}{\sqrt{5}} \left(\frac{1}{2}, \; \frac{3}{4}\right) \cdot (1, 2) = \frac{2}{\sqrt{5}}.$$

Kildesett: course=TMA4105 term=var year=2020 problem=5 file=tma4105_2020v.pdf
