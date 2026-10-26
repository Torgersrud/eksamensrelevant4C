### **Løsning til Oppgave 5**

**(a)** Flaten $S$ er gitt ved $z = f(x, y)$ der $f(x, y) = 4 - x^2 - y^2$. Ligningen for tangentplanet i $(1, 1, 2)$ er gitt ved

$$z = f(1, 1) + (x - 1) f_x(1, 1) + (y - 1) f_y(1, 1),$$

dvs. $z = 2 + (x - 1)(-2) + (y - 1)(-2)$, som forenkles til

$$z = 6 - 2x - 2y.$$

**(b)** Her er det flere muligheter.

*Alternativ 1.* Projeksjonen av $C$ i $xy$-planet er gitt ved $4x^2 y = 1$ ($x > 0$), dvs. $y = \frac{1}{4x^2}$. Dette gir

$$z = 4 - x^2 - y^2 = 4 - x^2 - \left( \frac{1}{4x^2} \right)^2 = 4 - x^2 - \frac{1}{16x^4},$$

som skal maksimeres for $x > 0$. Vi finner kritisk punkt:

$$\frac{dz}{dx} = -2x + \frac{1}{4x^5} = 0 \iff 8x^6 = 1 \iff x = \pm \frac{1}{\sqrt{2}},$$

men vi skal ha $x > 0$, derfor er $x = \frac{1}{\sqrt{2}}$, $y = \frac{1}{4x^2} = \frac{1}{2}$, og svaret blir

$$z = 4 - x^2 - y^2 = 4 - \frac{1}{2} - \frac{1}{4} = \frac{13}{4}.$$

*Alternativ 2 (Lagrange).* Vi skal maksimere $f(x, y) = 4 - x^2 - y^2$ under bibetingelsen $g(x, y) = 0$ der $g(x, y) = 4x^2 y - 1$, med $x > 0$. Dette gir ligningene $\nabla f = \lambda \nabla g$ og $g(x, y) = 0$, dvs.

$$-2x = \lambda 8xy \;(1), \qquad -2y = \lambda 4x^2 \;(2), \qquad 4x^2 y = 1 \;(3).$$

Fra (1) får vi $\lambda = -\frac{1}{4y}$, som innsatt i (2) gir $-2y = -\frac{x^2}{y}$, dvs. $x^2 = 2y^2$. Innsatt i (3) gir dette $8y^3 = 1$, dvs. $y = \frac{1}{2}$, og (3) gir da $x = \frac{1}{\sqrt{2}}$. Resten går som i alternativ 1: det høyeste punktet på $C$ er $\left( \frac{1}{\sqrt{2}}, \frac{1}{2}, \frac{13}{4} \right)$.

**(c)** *Alternativ 1.* La $\alpha$ være vinkelen vi skal bestemme. Stigningstallet $\tan \alpha$ er lik den retningsderiverte av $f(x, y) = 4 - x^2 - y^2$ i punktet $(1, 1/4)$, i retningen bestemt av kurven $C$. Mer presist,

$$\tan \alpha = D_{\mathbf{u}} f(1, 1/4) = \nabla f(1, 1/4) \cdot \mathbf{u},$$

der $\mathbf{u} = u_1 \mathbf{i} + u_2 \mathbf{j}$ skal være tangent til projeksjonen av $C$ i $xy$-planet og skal ha lengde $1$. Projeksjonen av $C$ er gitt ved $y = \frac{1}{4x^2}$ for $x > 0$, dvs. vi kan parametrisere den ved

$$\mathbf{r}(t) = t \, \mathbf{i} + \frac{1}{4t^2} \, \mathbf{j} \quad (t > 0), \qquad \mathbf{r}'(t) = \mathbf{i} - \frac{1}{2t^3} \, \mathbf{j}.$$

Vi ser på punktet som svarer til $t = 1$, og tar derfor

$$\mathbf{u} = \frac{\mathbf{r}'(1)}{|\mathbf{r}'(1)|} = \frac{\mathbf{i} - \frac{1}{2} \mathbf{j}}{\left| \mathbf{i} - \frac{1}{2} \mathbf{j} \right|} = \frac{2}{\sqrt{5}} \left( \mathbf{i} - \frac{1}{2} \mathbf{j} \right).$$

Dette gir (siden $\nabla f = -2x \, \mathbf{i} - 2y \, \mathbf{j}$)

$$\tan \alpha = \nabla f(1, 1/4) \cdot \mathbf{u} = \left( -2 \mathbf{i} - \frac{1}{2} \mathbf{j} \right) \cdot \frac{2}{\sqrt{5}} \left( \mathbf{i} - \frac{1}{2} \mathbf{j} \right) = \frac{2}{\sqrt{5}} \left( -2 + \frac{1}{4} \right) = -\frac{7}{2\sqrt{5}},$$

som gir $\alpha = \arctan\left( -\frac{7}{2\sqrt{5}} \right) \approx -57{,}4^\circ$. Vi fikk en negativ vinkel pga. orienteringen av $\mathbf{r}$. Både $\alpha \approx 57{,}4^\circ$ og $\alpha \approx -57{,}4^\circ$ er fullgode svar, siden det kun står «finn vinkelen i forhold til horisontalplanet» i oppgaven.

*Alternativ 2.* $z$-verdien svarende til $(x, y) = (1, 1/4)$ er $z = 4 - 1 - (1/4)^2 = 47/16$, så punktet vi ser på er $P = (1, 1/4, 47/16)$. $C$ er skjæringskurven mellom to flater $F(x, y, z) = z - 4 + x^2 + y^2 = 0$ og $G(x, y, z) = 4x^2 y - 1 = 0$. En tangentvektor til $C$ i $P$ er derfor

$$\mathbf{T} = \nabla F(P) \times \nabla G(P) = [2, 1/2, 1] \times [2, 4, 0] = [-4, 2, 7].$$

Stigningstallet er da gitt ved

$$\tan \alpha = \frac{7}{\left| -4 \mathbf{i} + 2 \mathbf{j} \right|} = \frac{7}{\sqrt{20}} = \frac{7}{2\sqrt{5}},$$

som gir $\alpha = \arctan \frac{7}{2\sqrt{5}} \approx 57{,}4^\circ$. (Ekvivalent: $\alpha$ er vinkelen mellom $\mathbf{T}$ og projeksjonen $-4 \mathbf{i} + 2 \mathbf{j}$, slik at $\cos \alpha = \sqrt{20/69}$, som gir samme vinkel.)

Kildesett: course=TMA4105 term=var year=2005 problem=5 file=tma4105_05v.pdf
