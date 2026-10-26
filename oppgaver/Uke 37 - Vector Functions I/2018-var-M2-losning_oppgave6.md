### **Løsning til Oppgave 6**

La $f(x, y) = \dfrac{100}{1 + x^2 + 2y^2}$, slik at

$$\nabla f(x, y) = -\frac{200}{(1 + x^2 + 2y^2)^2}\,(x, 2y)$$

som igjen gir at $\nabla f(6, 3) = \dfrac{48}{121}(-1, -1)$.

La $\mathbf{u} = (-1, -1)/|(-1, -1)| = \frac{1}{\sqrt{2}}(-1, -1)$. Den retningsderiverte til $f$ i retningen $\mathbf{u}$ i punktet $(6, 3, 20/11)$ er så gitt ved

$$D_{\mathbf{u}} f(6, 3) = \nabla f(6, 3) \cdot \mathbf{u} = \frac{48}{121\sqrt{2}}(1 + 1) = \frac{48\sqrt{2}}{121}.$$

Siden $|\mathbf{u}| = 1$ blir dermed helningsvinkelen til terrenget i retningen $(-1, -1)$ i punktet $(6, 3, 20/11)$ gitt ved

$$\theta = \arctan\frac{48\sqrt{2}}{121} \approx 0.511,$$

som tilsvarer $29.3^\circ$.

Kildesett: course=TMA4105 term=var year=2018 problem=6 file=tma4105_2018v.pdf
