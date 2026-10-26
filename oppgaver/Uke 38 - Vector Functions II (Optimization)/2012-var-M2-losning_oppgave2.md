### **Løsning til Oppgave 2**

La $g(x, y) = x^2 + 3y^2$. For å benytte Lagranges multiplikatormetode trenger vi $\nabla f$ og $\nabla g$:

$$\nabla f = 2(1 - x) \, \mathbf{i} - 2y \, \mathbf{j}, \qquad \nabla g = 2x \, \mathbf{i} + 6y \, \mathbf{j}.$$

De nødvendige betingelsene for største og minste verdi er:

$$\nabla f = \lambda \nabla g, \quad g(x, y) = 1.$$

Fra $\nabla f = \lambda \nabla g$ får vi

$$1 - x = \lambda x \tag{1}$$

$$-y = 3\lambda y. \tag{2}$$

Ligning (2) gir for $y \neq 0$ at $\lambda = -1/3$, som innsatt i (1) gir $x = 3/2$. Ettersom $g(3/2, y) = 9/4 + 3y^2 > 1$ for alle $y \in \mathbb{R}$ er ikke $(3/2, y)$ et punkt på ellipsen $x^2 + 3y^2 = 1$ for noen $y$. Da står vi igjen med at $y = 0$, som gir $g(x, 0) = x^2 = 1$, det vil si $x = \pm 1$. Altså har vi

$$f(x, 0) = \begin{cases} 5 & x = 1, \\ 1 & x = -1. \end{cases}$$

Største verdi til $f$ på ellipsen er $5$ og minste verdi er $1$.

Kildesett: course=TMA4105 term=var year=2012 problem=2 file=tma4105_12v_ny.pdf
