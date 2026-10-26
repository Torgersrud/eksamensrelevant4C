### **Løsning til Oppgave 1**

De kritiske punktene til $f(x, y)$ tilfredsstiller

$$f_x(x, y) = 6y + 12x^2 + 3y^2 = 0, \tag{1}$$

$$f_y(x, y) = 6x + 6xy = 0. \tag{2}$$

Fra (2) får vi $x(1 + y) = 0$, altså er $x = 0$ eller $y = -1$.

Innsatt for $x = 0$ gir (1) at $y(y + 2) = 0$, det vil si $y = 0$ eller $y = -2$. Innsatt for $y = -1$ gir (1) at $4x^2 - 1 = 0$, det vil si $x = \pm\frac{1}{2}$. Altså er $(0, 0)$, $(0, -2)$, $(\frac{1}{2}, -1)$ og $(-\frac{1}{2}, -1)$ kritiske punkter.

Diskriminanten er så gitt ved

$$D(x, y) = \Delta(x, y) = f_{xx} f_{yy} - f_{xy}^2 = 24x \cdot 6x - (6 + 6y)^2 = 144x^2 - 36(1 + y)^2.$$

Ettersom

$$D(0, 0) = -36 < 0, \qquad D\left(\frac{1}{2}, -1\right) = 36 > 0,$$
$$D(0, -2) = -36 < 0, \qquad D\left(-\frac{1}{2}, -1\right) = 36 > 0,$$

gir annenderiverttesten at $(0, 0)$ og $(0, -2)$ er begge sadelpunkter. For å avgjøre hvorvidt $(\frac{1}{2}, -1)$ og $(-\frac{1}{2}, -1)$ er lokale maksimums- eller minimumspunkter, ser vi på fortegnet til $f_{xx}(\pm\frac{1}{2}, -1)$. Ettersom

$$f_{xx}\left(\frac{1}{2}, -1\right) = 12 > 0 \qquad \text{og} \qquad f_{xx}\left(-\frac{1}{2}, -1\right) = -12 < 0,$$

får vi fra annenderiverttesten at $(\frac{1}{2}, -1)$ er et lokalt minimumspunkt og at $(-\frac{1}{2}, -1)$ er et lokalt maksimumspunkt.

Altså har vi funnet følgende klassifkasjon av de kritiske punktene til funksjonen $f$:

$$(0, 0) : \text{sadelpunkt}, \qquad \left(\frac{1}{2}, -1\right) : \text{lokalt minimumspunkt},$$

$$(0, -2) : \text{sadelpunkt}, \qquad \left(-\frac{1}{2}, -1\right) : \text{lokalt maksimumspunkt}.$$

Kildesett: course=TMA4105 term=sommer year=2011 problem=1 file=tma4105_11k.pdf
