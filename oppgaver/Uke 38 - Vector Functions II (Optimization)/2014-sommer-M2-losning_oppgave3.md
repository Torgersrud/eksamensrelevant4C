### **Løsning til Oppgave 3**

Vi regner først ut

$$\nabla f = (\partial_x f, \partial_y f) = (12x^2 + 6xy, \; 6y^2 + 3x^2).$$

Så søker vi kritiske punkter for $f$ i det indre av sirkelskiven, altså punkter der $\nabla f = 0$:

$$12x^2 + 6xy = 0, \quad 6y^2 + 3x^2 = 0.$$

Den siste av disse to ligningene har kun løsningen $(x, y) = (0, 0)$, og den passer også inn i den første ligningen. Så $(0, 0)$ er eneste kritiske punkt for $f$. Vi har $f(0, 0) = 0$.

Deretter leter vi etter ekstremverdier på sirkelranden, definert ved $g(x, y) = x^2 + y^2 - 17 = 0$. Så er $\nabla g(x, y) = (2x, 2y)$, og metoden med Lagrange-multiplikator ($\nabla f = \lambda \nabla g$) gir

$$12x^2 + 6xy = 2\lambda x, \quad 6y^2 + 3x^2 = 2\lambda y. \tag{1}$$

Dersom vi multipliserer den første ligningen med $y$ og den andre med $x$, blir de to høyresidene like, så de to venstresidene må også bli like: $12x^2y + 6xy^2 = 6xy^2 + 3x^3$, som vi forenkler til $4x^2y = x^3$ og videre til $(4y - x)x^2 = 0$. Dette holder hvis og bare hvis enten $x = 0$ eller $x = 4y$.

En alternativ måte å se dette på er slik: Den første ligningen i (1) holder dersom $x = 0$. I så fall kan vi sette $\lambda = 3y$, så holder den andre ligningen uansett hva $y$ måtte være. Hvis $x \neq 0$ gir den første ligningen $\lambda = 6x + 3y$, som vi kan sette inn i den andre og få $6y^2 + 3x^2 = 2(6x + 3y)y$, som forenkles til $3x^2 = 12xy$, og dermed $x = 4y$.

Vi fortsetter nå med å sette inn i føringen $x^2 + y^2 = 17$: Dersom $x = 0$ må da $y = \pm\sqrt{17}$, mens $x = 4y$ gir $17y^2 = 17$, altså $y = \pm 1$. De fire mulige ekstrempunktene på sirkelranden er dermed $(x, y) = (0, \sqrt{17})$, $(0, -\sqrt{17})$, $(4, 1)$ og $(-4, -1)$.

Vi regner ut funksjonsverdiene $f(0, \pm\sqrt{17}) = \pm 2 \cdot 17^{3/2}$ og $f(\pm 4, \pm 1) = \pm(4 \cdot 4^3 + 2 + 3 \cdot 4^2) = \pm 306$. Merk at $2 \cdot 17^{3/2} < 2 \cdot 25^{3/2} = 2 \cdot 5^3 = 250 < 306$ (kan også sjekkes på kalkulator).

Vi vet at $f$ er en kontinuerlig funksjon, og området $x^2 + y^2 \le 17$ er lukket og begrenset, så det finnes en største og minste verdi for $f$ på området. De fem punktene vi har undersøkt er de eneste mulige ekstrempunktene, så største og minste verdi for $f$ på området er største og minste verdi blant de fem punktene, altså henholdsvis $306$ og $-306$.

Kildesett: course=TMA4105 term=sommer year=2014 problem=3 file=tma4105_14k.pdf
