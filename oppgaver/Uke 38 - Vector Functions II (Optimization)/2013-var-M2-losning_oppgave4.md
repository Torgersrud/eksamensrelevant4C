### **Løsning til Oppgave 4**

La

$$f(x, y, z) = x^2 + y^2 + z^2 \qquad \text{og} \qquad g(x, y, z) = 2x + 2y + z - 4.$$

Ved Lagranges multiplikatormetode, så er de nødvendige og tilstrekkelige betingelsene for minste verdi av $f$ under bibetingelsen $g(x, y, z) = 0$ gitt ved $\nabla f = \lambda \nabla g$, for $\lambda$ et reelt tall. I vårt tilfelle er

$$\nabla f(x, y, z) = 2x \, \mathbf{i} + 2y \, \mathbf{j} + 2z \, \mathbf{k} \qquad \text{og} \qquad \nabla g(x, y, z) = 2 \, \mathbf{i} + 2 \, \mathbf{j} + \mathbf{k},$$

slik at

$$2x = 2\lambda, \quad 2y = 2\lambda, \quad \text{og} \quad 2z = \lambda,$$

er de nødvendige betingelsene for $x$, $y$, $z$ og $\lambda$. Den eneste løsningen til dette systemet er

$$(x, y, z) = \lambda \left(1, 1, \frac{1}{2}\right),$$

som innsatt i $g(x, y, z) = 0$ gir at

$$2\lambda + 2\lambda + \frac{\lambda}{2} = 4 \quad \text{det vil si} \quad \lambda = \frac{8}{9}.$$

Ettersom vi har funnet kun én løsning $(x, y, z)$, og ethvert plan har en minste avstand til origo, har vi funnet den minste avstanden fra origo til planet $2x + 2y + z = 4$. Den minste avstanden er så

$$\sqrt{\left(\frac{8}{9}\right)^2 + \left(\frac{8}{9}\right)^2 + \left(\frac{4}{9}\right)^2} = \frac{4}{3}.$$

Kildesett: course=TMA4105 term=var year=2013 problem=4 file=tma4105_13v.pdf
