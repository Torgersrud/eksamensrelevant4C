### **Løsning til Oppgave 5**

Partiell derivasjon av uttrykket $f(x, y) = xy \, e^{-(x^2 + y^2)}$ gir

$$\frac{\partial f}{\partial x} = y(1 - 2x^2)e^{-(x^2 + y^2)}$$

og

$$\frac{\partial f}{\partial y} = x(1 - 2y^2)e^{-(x^2 + y^2)}.$$

De kritiske punktene får vi når begge disse partielle deriverte er lik 0. Altså vi får punktene $(0, 0)$, $\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$, $\left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$, $\left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ og $\left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$. Utregning av andre ordens partielle deriverte gir

$$A = \frac{\partial^2 f}{\partial x^2} = -2xy(3 - 2x^2)e^{-(x^2 + y^2)},$$

$$B = \frac{\partial^2 f}{\partial y^2} = -2xy(3 - 2y^2)e^{-(x^2 + y^2)}$$

og

$$C = \frac{\partial^2 f}{\partial x \partial y} = (1 - 2x^2)(1 - 2y^2)e^{-(x^2 + y^2)}.$$

Andrederiverttesten brukt på uttrykket $AB - C^2$ gir da at $(0, 0)$ er et salpunkt, $\left(\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ og $\left(-\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$ er lokale max-punkter, og $\left(-\frac{1}{\sqrt{2}}, \frac{1}{\sqrt{2}}\right)$ og $\left(\frac{1}{\sqrt{2}}, -\frac{1}{\sqrt{2}}\right)$ er lokale min-punkter.

Kildesett: course=TMA4105 term=sommer year=2020 problem=5 file=tma4105_2020k.pdf
