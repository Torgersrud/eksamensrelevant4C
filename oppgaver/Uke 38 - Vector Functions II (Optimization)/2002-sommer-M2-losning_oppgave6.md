### **Løsning til Oppgave 6**

Vi deriverer den oppgitte ligningen

$$e^{2zx - x^2} - 3e^{2zy + y^2} = 2$$

med hensyn på $x$ og $y$, idet vi betrakter $z$ som en funksjon av $x$ og $y$:

$$e^{2zx - x^2} \left( 2x \frac{\partial z}{\partial x} + 2z - 2x \right) - 3e^{2zy + y^2} \left( 2y \frac{\partial z}{\partial x} \right) = 0, \qquad (*)$$
$$e^{2zx - x^2} \left( 2x \frac{\partial z}{\partial y} \right) - 3e^{2zy + y^2} \left( 2y \frac{\partial z}{\partial y} + 2z + 2y \right) = 0. \qquad (**)$$

Setter vi inn $\partial z/\partial x = 0$ i $(*)$, får vi $z = x$, og $\partial z/\partial y = 0$ i $(**)$ gir $z = -y$. Dermed har vi $x = z$ og $y = -z$ som så innsettes i den oppgitte ligningen. Det gir

$$e^{z^2} - 3e^{-z^2} = 2, \qquad \left( e^{z^2} \right)^2 - 2e^{z^2} - 3 = 0, \qquad e^{z^2} = \frac{2 \pm \sqrt{4 - 4(-3)}}{2} = 1 \pm 2.$$

Følgelig er $e^{z^2} = 3$ og $z = \pm\sqrt{\ln 3}$ siden $e^{z^2} = -1$ ikke er mulig. Punktene der $\partial z/\partial x = 0$ og $\partial z/\partial y = 0$ er altså $\left( \sqrt{\ln 3}, -\sqrt{\ln 3} \right)$ og $\left( -\sqrt{\ln 3}, \sqrt{\ln 3} \right)$.

Kildesett: course=SIF5005 term=sommer year=2002 problem=6 file=sif5005_02k.pdf
