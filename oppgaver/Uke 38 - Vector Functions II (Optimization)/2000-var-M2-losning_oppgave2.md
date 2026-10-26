### **Løsning til Oppgave 2**

Kritiske punkter:

$$\frac{\partial f}{\partial x} = 3x^2 - 3y = 0 \ \Rightarrow\ y = x^2$$

og

$$\frac{\partial f}{\partial y} = -3x + y = 0 \ \Rightarrow\ y = 3x.$$

Dette gir $x^2 = 3x$, som har løsninger $x = 0$ og $x = 3$.

$x = 0$ gir $y = 0$, og $x = 3$ gir $y = 9$. Så de kritiske punktene er $(0, 0)$ og $(3, 9)$.

Klassifisering:

$$A = \frac{\partial^2 f}{\partial x^2} = 6x, \quad B = \frac{\partial^2 f}{\partial x \partial y} = -3, \quad C = \frac{\partial^2 f}{\partial y^2} = 1, \quad \Delta = AC - B^2 = 6x - 9.$$

$\Delta(0, 0) = -9 < 0$: $(0, 0)$ er et sadelpunkt.

$\Delta(3, 9) = 9 > 0$ og $A(3, 9) = 18 > 0$: $(3, 9)$ er et lokalt minimumspunkt.

Kildesett: course=SIF5005 term=var year=2000 problem=2 file=sif5005_00v.pdf
