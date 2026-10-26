### **Løsning til Oppgave 4**

Vi bruker Lagranges multiplikatormetode. La $g(x, y, z) = x^2 + y^6 + z^4$; da ønsker vi å løse ligningssystemet

$$\nabla f = \lambda \nabla g, \qquad g(x, y, z) = 1.$$

Vi har

$$\nabla f = (4x, 18y^5, 16z^3), \qquad \nabla g = (2x, 6y^5, 4z^3),$$

slik at vi har ligningene

$$4x = 2\lambda x, \qquad 18y^5 = 6\lambda y^5, \qquad 16z^3 = 4\lambda z^3.$$

Her ser vi at vi må ha

* $\lambda = 2$ eller $x = 0$,
* $\lambda = 3$ eller $y = 0$,
* $\lambda = 4$ eller $z = 0$.

Det er bare tre kompatible alternativer; sammen med den siste ligningen $x^2 + y^6 + z^4 = 1$ får vi løsningene

* $\lambda = 2$ og $y = z = 0$, $x^2 = 1$, det vil si $(x, y, z) = (\pm 1, 0, 0)$
* $\lambda = 3$ og $x = z = 0$, $y^6 = 1$, det vil si $(x, y, z) = (0, \pm 1, 0)$,
* $\lambda = 4$ og $x = y = 0$, $z^4 = 1$, det vil si $(x, y, z) = (0, 0, \pm 1)$.

Siden $x^2 + y^6 + z^4 = 1$ er en lukket flate, vet vi at den største og minste verdien av $f$ må oppnås på ett av disse 6 kritiske punktene. Vi evaluerer:

$$f(\pm 1, 0, 0) = 2, \qquad f(0, \pm 1, 0) = 3, \qquad f(0, 0, \pm 1) = 4.$$

Dermed er den minste verdien $2$ og den største verdien $4$.

Kildesett: course=TMA4105 term=sommer year=2021 problem=4 file=tma4105_2021k.pdf
