### **Løsning til Oppgave 1**

**a)** La oss like godt gjøre unna all nødvendig derivasjon med én gang:

$$f_x = 3x^2 + y, \qquad f_y = 3y^2 + x, \qquad f_{xx} = 6x, \qquad f_{xy} = 1, \qquad f_{yy} = 6y.$$

For å finne kritiske punkter må vi løse ligningene $f_x = f_y = 0$, altså

$$3x^2 + y = 0, \qquad 3y^2 + x = 0.$$

Tar vi $y = -3x^2$ fra den første ligningen og setter inn i den andre, får vi $27x^4 + x = 0$, med løsninger gitt ved $x = 0$ eller $27x^3 + 1 = 0$. Det siste gir $x = -\frac{1}{3}$. Husker vi så at $y = -3x^2$, har vi derfor disse kritiske punktene:

$$(x, y) = (0, 0), \qquad (x, y) = \left(-\frac{1}{3}, -\frac{1}{3}\right).$$

For $(x, y) = (0, 0)$ finner vi

$$A = f_{xx}(0, 0) = 0, \qquad B = f_{xy}(0, 0) = 1, \qquad C = f_{yy}(0, 0) = 0, \qquad \Delta = AC - B^2 = -1 < 0,$$

så $(0, 0)$ er et sadelpunkt.

For $(x, y) = \left(-\frac{1}{3}, -\frac{1}{3}\right)$ finner vi

$$A = f_{xx}\left(-\tfrac{1}{3}, -\tfrac{1}{3}\right) = -2, \qquad B = f_{xy}\left(-\tfrac{1}{3}, -\tfrac{1}{3}\right) = 1, \qquad C = f_{yy}\left(-\tfrac{1}{3}, -\tfrac{1}{3}\right) = -2,$$

$$\Delta = AC - B^2 = 3 > 0,$$

og siden $A < 0$ er $\left(-\frac{1}{3}, -\frac{1}{3}\right)$ et lokalt maksimum.

**b)** Vi har

$$\nabla f(1, 2) = [f_x(1, 2),\, f_y(1, 2)] = [5, 13].$$

Det er altså i retningen langs vektoren $[5, 13]$ at den retningsderiverte er størst. Størrelsen på den retningsderiverte i denne retningen er $|\nabla f(1, 2)| = \sqrt{5^2 + 13^2} = \sqrt{194}$. Om man ønsker å angi retningen med størst retningsderivert som en enhetsvektor, er det bare å normalisere gradienten: $[5, 13]/\sqrt{194}$. Enhetsvektoren med retning fra $(1, 2)$ mot origo er $[-1, -2]/\sqrt{5}$, så den retningsderiverte av $f$ i den retningen er

$$\frac{1}{\sqrt{5}} \, [-1, -2] \cdot [5, 13] = -\frac{31}{\sqrt{5}}.$$

Kildesett: course=SIF5005 term=var year=2003 problem=1 file=sif5005_03v.pdf
