### **Løsning til Oppgave 1**

La $f(x, y, z) = x^3 + 2xyz + x\cos(z^2) - 2$. Da er

$$\nabla f(x, y, z) = \bigl(3x^2 + 2yz + \cos(z^2), \, 2xz, \, 2xy - 2xz\sin(z^2)\bigr)$$

som gir

$$\nabla f(1, -1, 0) = (3 + 1, \, 0, \, -2) = (4, 0, -2).$$

Siden $\nabla f(1, -1, 0)$ står normalt på nivåflaten $f(x, y, z) = 0$ i punktet $(1, -1, 0)$ er

$$\nabla f(1, -1, 0) \cdot (x - 1, \, y + 1, \, z) = (4, 0, -2) \cdot (x - 1, \, y + 1, \, z) = 4x - 4 - 2z = 0.$$

En ligning for tangentplanet til flaten gitt som nivåflaten $f(x, y, z) = 0$ i punktet $(1, -1, 0)$ er dermed gitt ved

$$2x - z = 2.$$

Kildesett: course=TMA4105 term=sommer year=2024 problem=1 file=tma4105_2024k.pdf
