### **Løsning til Oppgave 3**

La $f(x, y) = (x^2 - y^2)e^{-(x + y)}$ slik at

$$\nabla f(x, y) = e^{-(x + y)}\bigl(2x - x^2 + y^2, \, y^2 - 2y - x^2\bigr) = (0, 0)$$

gir ligningene

$$2x - x^2 + y^2 = 0 \qquad\qquad (1)$$

$$y^2 - 2y - x^2 = 0. \qquad\qquad (2)$$

Fra (1) får vi $2x = x^2 - y^2$ som innsatt i (2) gir $2x + 2y = 0$, det vil si, $x = -y$. Ved å sette inn for $x = -y$ i (1) får vi

$$2x - x^2 + x^2 = 0, \qquad \text{det vil si,} \qquad x = 0,$$

som igjen gir $y = 0$. Altså har $f$ et kritisk punkt i $(x, y) = (0, 0)$, hvor $f(0, 0) = 0$.

La $D = \{(x, y) \in \mathbb{R}^2 \mid x + y \leqslant 4, \ x \geqslant 0, \ y \geqslant 0\}$. Vi må undersøke hvilke verdier $f$ tar i $D$. Det eneste kritiske punktet til $f$ ligger i $D$, så det som gjenstår å sjekke er hvilke verdier $f$ oppnår langs randen til $D$.

Vi undersøker hvilke verdier $f$ oppnår langs $x = 0$, $0 \leqslant y \leqslant 4$. La

$$g(y) = f(0, y) = -y^2 e^{-y}$$

slik at

$$g'(y) = -2y e^{-y} + y^2 e^{-y} = y(y - 2)e^{-y}$$

der $g'(y) < 0$ for $0 < y < 2$, $g'(2) = 0$ og $g'(y) > 0$ for $2 < y < 4$. Altså er

$$-4e^{-2} \leqslant g(2) \leqslant g(y) \leqslant g(0) = 0$$

for alle $0 \leqslant y \leqslant 4$.

Helt tilsvarende får vi

$$0 \leqslant f(0, 0) \leqslant f(x, 0) \leqslant f(2, 0) = 4e^{-2}$$

for alle $0 \leqslant x \leqslant 4$.

Til slutt undersøker vi verdiene $f$ oppnår langs $0 \leqslant x \leqslant 4$, $y = 4 - x$. La $h(x) = f(x, 4 - x)$, det vil si,

$$h(x) = f(x, 4 - x) = \bigl(x^2 - (4 - x)^2\bigr)e^{-(x + 4 - x)} = 8(x - 2)e^{-4}.$$

Siden $h'(x) = 8e^{-4} > 0$ for alle $x$ må

$$-16e^{-4} = h(0) \leqslant h(x) \leqslant h(4) = 16e^{-4}$$

for alle $0 \leqslant x \leqslant 4$. Legg merke til at $4e^{-2} > 16e^{-4}$.

Dermed er den største verdien til $f$ i $D$ lik $4e^{-2}$, mens den minste verdien til $f$ i $D$ er $-4e^{-2}$.

Kildesett: course=TMA4105 term=sommer year=2025 problem=3 file=tma4105_2025k.pdf
