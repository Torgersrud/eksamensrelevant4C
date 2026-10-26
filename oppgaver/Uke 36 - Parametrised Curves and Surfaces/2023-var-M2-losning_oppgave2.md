### **Løsning til Oppgave 2**

La $f(x, y, z) = x^2 + 2y^2 + 3z^2$, slik at $S$ er en nivåflate av funksjonen $f$. Vi har $\nabla f(x, y, z) = (2x, 4y, 6z)$; siden gradienten alltid er normal til nivåflatene har tangentplanet i punktet $(a, b, c)$ normalvektoren $\nabla f(a, b, c) = (2a, 4b, 6c)$. Planet gjennom $(a, b, c)$ med denne normalvektoren har ligning

$$(2a, 4b, 6c) \cdot (x - a, \, y - b, \, z - c) = 0,$$

eller $2a(x - a) + 4b(y - b) + 6c(z - c) = 0$, som vi kan forenkle til

$$ax + 2by + 3cz = 1$$

siden $a^2 + 2b^2 + 3c^2 = 1$ ettersom punktet $(a, b, c)$ ligger på $S$. Tangentplanet er parallelt med det gitte planet hvis og bare hvis normalvektorene til de to planene er parallelle. Planet $x + 2y + 3z = 0$ har normalvektor $(1, 2, 3)$, så vi ser etter punkter $(a, b, c)$ på $S$ hvor $(2a, 4b, 6c) = \lambda(1, 2, 3)$ for $\lambda \in \mathbb{R}$. Siden vi da har $\lambda = 2a$ kan vi forenkle dette til

$$4a = 4b, \quad 6a = 6c,$$

slik at $a = b = c$. Setter vi dette inn i ligningen for $S$ får vi $a^2 + 2a^2 + 3a^2 = 6a^2 = 1$, som gir de to punktene

$$\pm\frac{1}{\sqrt{6}}(1, 1, 1).$$

Kildesett: course=TMA4105 term=var year=2023 problem=2 file=tma4105_2023v.pdf
