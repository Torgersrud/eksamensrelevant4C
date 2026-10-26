### **Løsning til Oppgave 3**

Sett $g(x, y, z) = x^2 + y^2 + z^2 - 25$, slik at kuleflaten er gitt ved $g(x, y, z) = 0$. Siden $f(x, y, z) = 3x + y + 2z$ er en kontinuerlig funksjon på et lukket og begrenset område (en kuleflate), vet vi at $f$ antar sin minimumsverdi i et punkt på kuleflaten. For å finne dette punktet bruker vi Lagrangemetoden, dvs. vi løser $\nabla f = \lambda \nabla g$ under tilleggsbetingelsen $g(x, y, z) = 0$. Siden $\nabla f = 3\mathbf{i} + \mathbf{j} + 2\mathbf{k}$ og $\nabla g = 2x\mathbf{i} + 2y\mathbf{j} + 2z\mathbf{k}$, får vi ligningene

$$3 = 2\lambda x, \qquad 1 = 2\lambda y, \qquad 2 = 2\lambda z,$$

som gir (merk at $\lambda$ ikke kan være lik null)

$$(x, y, z) = \left(\frac{3}{2\lambda}, \frac{1}{2\lambda}, \frac{2}{2\lambda}\right).$$

Men betingelsen $x^2 + y^2 + z^2 = 25$ gir da

$$\frac{3^2 + 1^2 + 2^2}{2^2 \lambda^2} = 25 \iff \lambda^2 = \frac{14}{100} \iff \lambda = \pm \frac{\sqrt{14}}{10},$$

og derfor er

$$(x, y, z) = \pm \left(\frac{15}{\sqrt{14}}, \frac{5}{\sqrt{14}}, \frac{10}{\sqrt{14}}\right).$$

De tilsvarende verdiene av $f$ er $f\left(\frac{15}{\sqrt{14}}, \frac{5}{\sqrt{14}}, \frac{10}{\sqrt{14}}\right) = \frac{70}{\sqrt{14}} = 5\sqrt{14}$ og $f\left(-\frac{15}{\sqrt{14}}, -\frac{5}{\sqrt{14}}, -\frac{10}{\sqrt{14}}\right) = -5\sqrt{14}$. Altså:

$$\text{Minimumsverdien er } -5\sqrt{14}.$$

Kildesett: course=TMA4105 term=var year=2009 problem=3 file=tma4105_09v.pdf
