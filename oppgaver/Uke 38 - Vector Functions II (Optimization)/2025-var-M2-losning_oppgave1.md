### **Løsning til Oppgave 1**

La $f(x, y) = x^2 + y^2 - xy + x + y$ slik at

$$\nabla f(x, y) = (2x - y + 1, \, 2y - x + 1) = (0, 0)$$

gir ligningene

$$2x - y + 1 = 0 \qquad\qquad (1)$$

$$2y - x + 1 = 0. \qquad\qquad (2)$$

Fra (1) får vi $y = 2x + 1$ som innsatt i (2) gir $2(2x + 1) - x + 1 = 3x + 3 = 0$, det vil si, $x = -1$ som igjen gir $y = 2x + 1 = -1$.

Altså har $f$ et kritisk punkt i $(x, y) = (-1, -1)$, hvor $f(-1, -1) = -1$.

Vi må så undersøke hvilke verdier $f$ tar i området $D = \{(x, y) \in \mathbb{R}^2 \mid x \leqslant 0, \ y \leqslant 0 \ \text{og} \ x + y \geqslant -3\}$. Det eneste kritiske punktet til $f$ ligger i $D$, så det som gjenstår å sjekke er hvilke verdier $f$ oppnår langs randen til $D$.

Vi undersøker verdiene $f$ oppnår langs $x = 0$, $-3 \leqslant y \leqslant 0$. La $g(y) = f(0, y)$, det vil si,

$$g(y) = f(0, y) = y^2 + y = y(y + 1)$$

slik at $g'(y) = 2y + 1 < 0$ for $-3 < y < -1/2$, $g'(-1/2) = 0$ og $g'(y) > 0$ for $-1/2 < y < 0$. Altså er

$$-\frac{1}{4} = f\left(0, -\frac{1}{2}\right) \leqslant f(0, y) \leqslant f(0, -3) = 6$$

for alle $-3 \leqslant y \leqslant 0$.

Helt tilsvarende får vi

$$-\frac{1}{4} = f\left(-\frac{1}{2}, 0\right) \leqslant f(x, 0) = x^2 + x = x(x + 1) \leqslant f(-3, 0) = 6$$

for alle $-3 \leqslant x \leqslant 0$.

Til slutt undersøker vi verdiene $f$ oppnår langs $-3 \leqslant x \leqslant 0$, $y = -x - 3$. La $h(x) = f(x, -x - 3)$, det vil si,

$$h(x) = f(x, -x - 3) = x^2 + (-x - 3)^2 - x(-x - 3) + x(-x - 3) = 3x^2 + 9x + 6 = 3(x + 2)(x + 1).$$

Fra $h'(x) = 6x + 9 < 0$ for $-3 < x < -3/2$, $h'(-3/2) = 0$ og $h'(x) > 0$ for $-3/2 < x < 0$ får vi

$$-\frac{3}{4} \leqslant h\left(-\frac{3}{2}\right) \leqslant h(x) \leqslant h(-3) = h(0) = 6$$

for alle $-3 \leqslant x \leqslant 0$.

Den minste verdien til $f$ i $D$ er derfor $-1$, mens den største verdien til $f$ i $D$ er $6$.

Kildesett: course=TMA4105 term=var year=2025 problem=1 file=tma4105_2025v.pdf
