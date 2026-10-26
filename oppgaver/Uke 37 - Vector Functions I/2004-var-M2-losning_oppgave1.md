### **Løsning til Oppgave 1**

**a)** Partiell derivasjon gir, ved hjelp av kjerneregelen og formelen $\frac{d}{du}(\arctan u) = \frac{1}{1 + u^2}$, at

$$f_x = y^2 + \frac{z}{1 + (xz)^2}, \qquad f_y = 2xy, \qquad f_z = \frac{x}{1 + (xz)^2}.$$

Innsatt $(x, y, z) = (1, 1, -1)$ gir dette svaret:

$$\nabla f(1, 1, -1) = \frac{1}{2} \, \mathbf{i} + 2 \, \mathbf{j} + \frac{1}{2} \, \mathbf{k}.$$

**b)** Ligningen for $S$ er $f(x, y, z) = f(1, 1, -1)$, dvs.

$$xy^2 + \arctan(xz) = 1 - \frac{\pi}{4},$$

siden $f(1, 1, -1) = 1 + \arctan(-1)$ og $\arctan(-1) = -\arctan(1) = -\pi/4$.

Ligningen for tangentplanet til $S$ i $P_0$ er gitt ved

$$\nabla f(1, 1, -1) \cdot ([x, y, z] - [1, 1, -1]) = 0,$$

dvs. $[\tfrac{1}{2}, 2, \tfrac{1}{2}] \cdot [x - 1, y - 1, z + 1] = 0$, som gir oss

$$\frac{1}{2}(x - 1) + 2(y - 1) + \frac{1}{2}(z + 1) = 0.$$

Dette er svar godt nok, men det blir penere hvis vi ganger med $2$ og rydder opp:

$$x + 4y + z = 4.$$

Kildesett: course=TMA4105 term=var year=2004 problem=1 file=tma4105_04v.pdf
