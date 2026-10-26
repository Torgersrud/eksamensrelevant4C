### **Løsning til Oppgave 1**

**a)**

$$f_x(x, y) = 3x^2 y + y^2 = 0 \ \Rightarrow\ y = 0 \ \text{eller}\ y = -3x^2$$
$$f_y(x, y) = x^3 + 2xy + 40 = 0$$

Tilfellet $y = 0$ gir $x^3 = -40$ slik at $(-\sqrt[3]{40}, 0) = (-2\sqrt[3]{5}, 0)$ er et kritisk punkt.

Tilfellet $y = -3x^2$ gir at $x^3 - 6x^3 + 40 = 0$, det vil si, $x = 2$, slik at $(2, -12)$ er et kritisk punkt.

Flere kritiske punkt finnes ikke.

Klassifisering ved annenderiverttesten: Testfunksjonen

$$\Delta(x, y) = f_{xx}(x, y) f_{yy}(x, y) - f_{xy}^2(x, y) = 6xy \cdot 2x - (3x^2 + 2y)^2$$

gir at $\Delta(-\sqrt[3]{40}, 0) < 0$ og $\Delta(2, -12) < 0$. Begge de kritiske punktene er derfor sadelpunkter.

**b)** $f(x, y)$ vokser med $x$ og vokser med $y$ i første kvadrant. Maksimum ligger derfor i punktet $(1, 1)$ der både $x$ og $y$ er størst, mens minimum ligger i $(0, 0)$ der både $x$ og $y$ er minst i området. Største verdi er derfor $f(1, 1) = 42$ og minste verdi er $f(0, 0) = 0$.

Kildesett: course=SIF5005 term=sommer year=2001 problem=1 file=sif5005_01k.pdf
