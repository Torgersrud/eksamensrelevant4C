### **Løsning til Oppgave 7**

La $f(x, y, z) = x^2 + y^2 + z^2$, $g(x, y, z) = x + y + z$ og $h(x, y, z) = x^2 + y^2$. Ved å sette inn for $x^2 + y^2 = 1$ i uttrykket for $f(x, y, z)$ får vi

$$f(x, y, z) = x^2 + y^2 + z^2 = 1 + z^2$$

som er opplagt minst mulig når $z = 0$. Innsatt for $z = 0$ i uttrykket for $g(x, y, z) = 1$ får vi

$$g(x, y, 0) = x + y = 1 \iff y = 1 - x.$$

Innsatt for $y = 1 - x$ i $h(x, y, 0) = 1$ får vi

$$x^2 + (1 - x)^2 = x^2 + 1 - 2x + x^2 = 2x^2 - 2x + 1 = 1 \iff x(x - 1) = 0$$

som har løsning $x = 0$ og $x = 1$. Dermed har vi at punktene

$$(0, \, 1 - 0, \, 0) = (0, 1, 0) \quad \text{og} \quad (1, \, 1 - 1, \, 0) = (1, 0, 0)$$

er de punktene på skjæringskurven som ligger nærmest origo.

Alternativt kunne vi brukt Lagranges multiplikatormetode på $f(x, y, z) = x^2 + y^2 + z^2$ med to bibetingelser:

$$g(x, y, z) = x + y + z = 1 \quad \text{og} \quad h(x, y, z) = x^2 + y^2 = 1.$$

De nødvendige betingelsene for minste verdi er:

$$\nabla f = \lambda_1 \nabla g + \lambda_2 \nabla h, \qquad g(x, y, z) = 1, \quad h(x, y, z) = 1.$$

Vi finner, ved noe regning, at $f(x, y, z)$ er minst, gitt bibetingelsene $g(x, y, z) = 1$ og $h(x, y, z) = 1$, når $(x, y, z) = (0, 1, 0)$ og $(x, y, z) = (0, 1, 0)$.

*Kjeldevarsel: i det alternative Lagrange-sporet mot slutten er punktet $(0, 1, 0)$ trykt to gonger; det andre punktet skal vere $(1, 0, 0)$, som hovudutleiinga over reknar ut (kontrollrekna: begge punkta ligg på skjæringskurva og har avstand $1$ frå origo).*

Kildesett: course=TMA4105 term=sommer year=2024 problem=7 file=tma4105_2024k.pdf
