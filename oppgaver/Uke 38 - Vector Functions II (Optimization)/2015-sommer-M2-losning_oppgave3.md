### **Løsning til Oppgave 3**

**a.** Vi får $f_x = 4(x - x^3)$ og $f_y = 2y$, så kritiske punkter er gitt ved $x = x^3$ og $y = 0$, altså $(0, 0)$, $(1, 0)$ og $(-1, 0)$.

Videre blir $f_{xx} = 4 - 12x^2$, $f_{yy} = 2$ og $f_{xy} = 0$, så $f_{xx}f_{yy} - f_{xy}^2 = 8 - 24x^2$.

I $(x, y) = (0, 0)$ blir $f_{xx}f_{yy} - f_{xy}^2 = 8 > 0$, og $f_{xx} = 4 > 0$, så $(0, 0)$ er et lokalt minimum.

I $(x, y) = (\pm 1, 0)$ blir $f_{xx}f_{yy} - f_{xy}^2 = -16 < 0$, så $(\pm 1, 0)$ er sadelpunkter.

**b.** For Lagrangefunksjonen $L(x, y, \lambda) = f(x, y) + \lambda(x^4 + y^2 - 4)$ blir $L_x = 4(x - x^3) + 4\lambda x^3$, $L_y = 2(1 + \lambda)y$ og $L_\lambda = x^4 + y^2 - 4$.

I et kritisk punkt er $L_y = 0$, så $y = 0$ eller $\lambda = -1$.

For $y = 0$ gir $L_\lambda = 0$ at $x^4 = 4$, så $x^2 = 2$, og $f(x, y) = 0$.

Dersom i stedet $\lambda = -1$, gir $L_x = 0$ at $x = 2x^3$, så $x = 0$ eller $x^2 = \frac{1}{2}$.

For $x = 0$ gir $L_\lambda = 0$ at $y^2 = 4$, så $f(x, y) = 4$.

For $x^2 = \frac{1}{2}$ blir $x^4 = \frac{1}{4}$, og $L_\lambda = 0$ gir at $y^2 = 4 - \frac{1}{4}$, så $f(x, y) = 2 \cdot \frac{1}{2} - \frac{1}{4} + 4 - \frac{1}{4} = 4\tfrac{1}{2}$.

Kurven $x^4 + y^2 = 4$ er en lukket og begrenset mengde, og $f$ er kontinuerlig, så $f$ oppnår både maksimum og minimum på kurven. Disse må være blant punktene vi har funnet, og vi slutter at minste verdi for $f$ på kurven er $0$, mens største verdi for $f$ på kurven er $4\tfrac{1}{2} = \frac{9}{2}$.

Alternativt (og enklere) kan vi merke oss at om $y^2 = 4 - x^4$ så er $f(x, y) = 2x^2 + 4 - 2x^4 = g(x^2)$, der $g(t) = 2t + 4 - 2t^2$. Vi må altså finne største og minste verdi for $g(t)$ for $t \in [0, 2]$ (siden $x^4 \le 4 \Leftrightarrow x^2 \le 2$). Nå er $g'(t) = 2 - 4t = 0$ for $t = \frac{1}{2}$. Vi må også undersøke verdien i endepunktene $t = 0$ og $t = 2$.

Vi finner $g(0) = 4$, $g(\frac{1}{2}) = 4\tfrac{1}{2}$ og $g(2) = 0$, og konklusjonen blir som over.

Kildesett: course=TMA4105 term=sommer year=2015 problem=3 file=tma4105_2015_15k.pdf
