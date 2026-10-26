### **Løsning til Oppgave 2**

Vi skal maksimere funksjonen $f(x, y, z) = xyz$ under bibetingelsen

$$g(x, y, z) = \frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1.$$

Lagrange' multiplikatormetode gir ligningssystemet

$$\nabla f(x, y, z) = \lambda \cdot \nabla g(x, y, z) \qquad \text{og} \qquad g(x, y, z) = 1.$$

Det vil si,

$$\begin{array}{ll} (1) & yz = \lambda \cdot \dfrac{2x}{a^2} \\[2mm] (2) & xz = \lambda \cdot \dfrac{2y}{b^2} \\[2mm] (3) & xy = \lambda \cdot \dfrac{2z}{c^2} \\[2mm] (4) & \dfrac{x^2}{a^2} + \dfrac{y^2}{b^2} + \dfrac{z^2}{c^2} = 1 \end{array}$$

Det er klart at maksimum må inntreffe i et punkt der $x \neq 0$, $y \neq 0$ og $z \neq 0$. Vi kan derfor multiplisere ligningene (1) - (3) med henholdsvis $x$, $y$ og $z$. Det gir

$$xyz = \lambda \cdot \frac{2x^2}{a^2} = \lambda \cdot \frac{2y^2}{b^2} = \lambda \cdot \frac{2z^2}{c^2}$$

slik at $\dfrac{x^2}{a^2} = \dfrac{y^2}{b^2} = \dfrac{z^2}{c^2}$. Innsatt i (4) gir det $3 \cdot \dfrac{x^2}{a^2} = 1$ slik at $x = \pm a/\sqrt{3}$, $y = \pm b/\sqrt{3}$ og $z = \pm c/\sqrt{3}$. Maksimum for $f(x, y, z)$ er derfor $\dfrac{a}{\sqrt{3}} \cdot \dfrac{b}{\sqrt{3}} \cdot \dfrac{c}{\sqrt{3}} = \dfrac{abc}{3\sqrt{3}}$ (og minimum er $-\dfrac{abc}{3\sqrt{3}}$).

Kildesett: course=SIF5005 term=var year=2001 problem=2 file=sif5005_01v.pdf
