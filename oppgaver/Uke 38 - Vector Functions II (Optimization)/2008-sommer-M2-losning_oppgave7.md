### **Løsning til Oppgave 7**

Funksjonen er partiell derivbar for alle $x$ og $y$. De kritiske punktene er derfor alle punkter $(x, y)$ der både $f_x(x, y) = 0$ og $f_y(x, y) = 0$. Med andre ord: alle punkter $(x, y)$ som tilfredsstiller likningssystemet

$$\text{(1)} \quad f_x(x, y) = y - 2y^2 - 2x = 0$$
$$\text{(2)} \quad f_y(x, y) = x - 4xy - 4y^3 = 0$$

Av (1): $x = y/2 - y^2$.

Innsatt i (2):

$$\frac{y}{2} - y^2 - 2y^2 + 4y^3 - 4y^3 = 0 \iff y\left(\frac{1}{2} - 3y\right) = 0 \iff y = 0 \text{ eller } y = \frac{1}{6}.$$

For $y = 0$ blir $x = y/2 - y^2 = 0$. For $y = \frac{1}{6}$ blir $x = y/2 - y^2 = \frac{1}{12} - \frac{1}{36} = \frac{2}{36} = \frac{1}{18}$.

Funksjonen har derfor to kritiske punkter: $(0, 0)$ og $\left(\frac{1}{18}, \frac{1}{6}\right)$.

Klassifisering av punktene:

$$\Delta(x, y) = f_{xx}(x, y) f_{yy}(x, y) - [f_{xy}(x, y)]^2 = -2(-4x - 12y^2) - [1 - 4y]^2 = 8x + 24y^2 - (1 - 4y)^2$$

$$\Delta(0, 0) = 8 \cdot 0 + 0 - (1 - 0)^2 = -1 < 0,$$

$$\Delta\left(\frac{1}{18}, \frac{1}{6}\right) = \frac{8}{18} + \frac{24}{36} - \left(1 - \frac{4}{6}\right)^2 = \frac{4}{9} + \frac{6}{9} - \frac{1}{9} = 1 > 0.$$

Punktet $(0, 0)$ er derfor et sadelpunkt og siden $f_{xx}\left(\frac{1}{18}, \frac{1}{6}\right) < 0$: punktet $\left(\frac{1}{18}, \frac{1}{6}\right)$ er et lokalt maksimum.

*Kjeldevarsel: løsningsforslaget reknar $\Delta\left(\frac{1}{18}, \frac{1}{6}\right) = \frac{4}{9} + \frac{4}{9} - \frac{1}{9}$, men leddet $\frac{24}{36} = \frac{2}{3} = \frac{6}{9}$, ikkje $\frac{4}{9}$; korrekt verdi er $\Delta = 1$. Forteknet og klassifiseringa blir det ikkje endra på.*

Kildesett: course=TMA4105 term=sommer year=2008 problem=7 file=tma4105_08k.pdf
