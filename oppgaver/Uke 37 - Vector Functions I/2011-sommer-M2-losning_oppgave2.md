### **Løsning til Oppgave 2**

Gradienten til $f$ er gitt ved

$$\nabla f = \frac{2}{x^2 + y^2 + z^2} (x \, \mathbf{i} + y \, \mathbf{j} + z \, \mathbf{k}).$$

For å ta den retningsderiverte til $f$ med hensyn på retningen $\mathbf{v} = 3\mathbf{i} - \mathbf{k}$, må vi normalisere $\mathbf{v}$. La så

$$\mathbf{u} = \frac{\mathbf{v}}{|\mathbf{v}|} = \frac{1}{\sqrt{10}} (3\mathbf{i} - \mathbf{k}).$$

Altså er den retningsderiverte til $f$ i punktet $(1, 2, -2)$ med hensyn på retningen $3\mathbf{i} - \mathbf{k}$ gitt ved

$$D_{\mathbf{u}} f(1, 2, -2) = \nabla f\big|_{(1, 2, -2)} \cdot \mathbf{u} = \frac{2}{9} (\mathbf{i} + 2\mathbf{j} - 2\mathbf{k}) \cdot \frac{1}{\sqrt{10}} (3\mathbf{i} - \mathbf{k}) = \frac{\sqrt{10}}{9}.$$

Kildesett: course=TMA4105 term=sommer year=2011 problem=2 file=tma4105_11k.pdf
