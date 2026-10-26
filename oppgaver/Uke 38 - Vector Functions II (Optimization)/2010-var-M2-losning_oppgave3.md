### **Løsning til Oppgave 3**

Vi bruker metoden med Lagrange-multiplikatorer for å finne minimumsverdien til funksjonen $f(x, y, z) = 2x^2 + y^2 + 3z^2$ gitt bibetingelsen $g(x, y, z) = 2x + 3y + 4z = 49$.

Vi får fire ligninger,

$$\nabla f = \lambda \nabla g, \quad g(x, y, z) = 49,$$

eller

$$4x = \lambda \cdot 2, \qquad 2y = \lambda \cdot 3, \qquad 6z = \lambda \cdot 4, \qquad 2x + 3y + 4z = 49,$$

innsatt i $g$ blir dette

$$2\left(\frac{1}{2}\lambda\right) + 3\left(\frac{3}{2}\lambda\right) + 4\left(\frac{2}{3}\lambda\right) = 49,$$

altså

$$\lambda = 6 \quad \text{og} \quad (x, y, z) = (3, 9, 4).$$

Verdien er

$$f(3, 9, 4) = 147.$$

Det er opplagt at dette er et minimum, siden funksjonen vokser når vi fjerner oss fra origo. Vi kan også se eksplisitt at det er et minimum ved å parametrisere flaten f. eks. ved ved $x = u + 3$, $y = 9 + v$ og $z = 4 - \frac{1}{2}u - \frac{3}{4}v$. Innsatt i $f$ får vi da $f(x(u, v), y(u, v), z(u, v)) = 147 + 2u^2 + v^2 + \left(\frac{1}{2}u + \frac{3}{4}v\right)^2$, og dette viser $147$ er minimumsverdien.

*Kjeldevarsel: trykkjen har «ved ved» (dobbelt ord), og leddet $\left(\frac{1}{2}u + \frac{3}{4}v\right)^2$ manglar faktoren $3$; riktig innsatt uttrykk er $147 + 2u^2 + v^2 + 3\left(\frac{1}{2}u + \frac{3}{4}v\right)^2$ (kontroll: $u = 2$, $v = 0$ gir $f = 158$, ikkje $156$). Konklusjonen med minimumsverdi $147$ i $(3, 9, 4)$ er likevel korrekt.*

Kildesett: course=TMA4105 term=var year=2010 problem=3 file=tma4105_10v.pdf
