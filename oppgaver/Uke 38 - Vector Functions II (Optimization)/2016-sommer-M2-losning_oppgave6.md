### **Løsning til Oppgave 6**

La $g(x, y, z) = x^2 + y^2 + z^2 - 4$. De nødvendige og tilstrekkelige betingelsene for største og minste verdi er:

$$\nabla f(x, y, z) = \lambda \nabla g(x, y, z) \quad \text{og} \quad g(x, y, z) = 0.$$

I vårt tilfelle er

$$\nabla f(x, y, z) = (2x, 4y, 6z) \quad \text{og} \quad \nabla g(x, y, z) = (2x, 2y, 2z).$$

Fra $\nabla f(x, y, z) = \lambda \nabla g(x, y, z)$ får vi

$$x = \lambda x \tag{1}$$
$$2y = \lambda y \tag{2}$$
$$3z = \lambda z. \tag{3}$$

Anta at $x \neq 0$. Da gir (1) at $\lambda = 1$, som innsatt i (2) og (3) gir $y = z = 0$. Fra $g(x, 0, 0) = x^2 - 4 = 0$ får vi at $x = \pm 2$. Observer at $f(\pm 2, 0, 0) = 4$.

Anta at $y \neq 0$. Da gir (2) at $\lambda = 2$, som innsatt i (1) og (3) gir $x = z = 0$. Fra $g(0, y, 0) = y^2 - 4 = 0$ får vi at $y = \pm 2$. Observer at $f(0, \pm 2, 0) = 8$.

Anta at $z \neq 0$. Da gir (3) at $\lambda = 3$, som innsatt i (1) og (2) gir $x = y = 0$. Fra $g(0, 0, z) = z^2 - 4 = 0$ får vi at $z = \pm 2$. Observer at $f(0, 0 \pm 2) = 12$.

Altså er $12$ den største verdien $f$ tar på kuleflaten $x^2 + y^2 + z^2 = 4$.

*Kjeldevarsel: løsningsforslaget trykkjer «$f(0, 0 \pm 2) = 12$» utan komma mellom nullane; punkta meint er $(0, 0, \pm 2)$.*

Kildesett: course=TMA4105 term=sommer year=2016 problem=6 file=tma4105_2016k.pdf
