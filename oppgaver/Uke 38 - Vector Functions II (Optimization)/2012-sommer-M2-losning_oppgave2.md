### **Løsning til Oppgave 2**

La $g_1(x, y, z) = x^2 + 2y^2$ og $g_2(x, y, z) = z - x + 4y$. For å finne største og minste verdi til $f$ langs skjæringskurven mellom flatene $g_1(x, y, z) = 1$ og $g_2(x, y, z) = 0$ benytter vi Lagranges multiplikatormetode med to bibetingelser. De nødvendige betingelsene for største og minste verdi er:

$$\nabla f = \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2, \quad g_1(x, y, z) = 1, \quad g_2(x, y, z) = 0.$$

Fra $\nabla f = \lambda_1 \nabla g_1 + \lambda_2 \nabla g_2$ får vi

$$0 = 2\lambda_1 x - \lambda_2, \qquad 0 = 4\lambda_1 y + 4\lambda_2, \qquad 1 = \lambda_2,$$

det vil si $x = \frac{1}{2\lambda_1}$ og $y = -\frac{1}{\lambda_1}$.

Innsetting av $x = 1/(2\lambda_1)$ og $y = -1/\lambda_1$ i $g_1(x, y, z) = 1$ gir $\lambda_1 = \pm 3/2$. Tilfellet $\lambda_1 = 3/2$ gir $x = 1/3$ og $y = -2/3$. Innsetting av disse verdiene for $x$ og $y$ i $g_2(x, y, z) = 0$ gir $z = 3$. Tilfellet $\lambda_1 = -3/2$ gir $x = -1/3$ og $y = 2/3$. Innsetting av disse verdiene for $x$ og $y$ i $g_2(x, y, z) = 0$ gir $z = -3$.

Altså er den største verdien til $f(x, y, z) = z$ langs skjæringskurven mellom flatene $x^2 + 2y^2 = 1$ og $z = x - 4y$ lik $3$, og den minste verdien er lik $-3$.

Kildesett: course=TMA4105 term=sommer year=2012 problem=2 file=tma4105_12k.pdf
