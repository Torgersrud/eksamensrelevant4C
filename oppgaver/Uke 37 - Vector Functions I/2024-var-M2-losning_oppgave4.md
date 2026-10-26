### **Løsning til Oppgave 4**

Vi har $\nabla f(x, y, z) = \bigl(e^y, x e^y, 2z\bigr)$ slik at

$$\nabla f\left(1, \ln(2), \frac{1}{2}\right) = \left(e^{\ln(2)}, \, 1 \cdot e^{\ln(2)}, \, 2 \cdot \frac{1}{2}\right) = (2, 2, 1).$$

Den retningsderiverte til $f$ i punktet $(1, \ln(2), 1/2)$ langs retningen $\mathbf{u}$ er gitt ved

$$D_{\mathbf{u}} f\left(1, \ln(2), \frac{1}{2}\right) = \left|\nabla f\left(1, \ln(2), \frac{1}{2}\right)\right| \cdot |\mathbf{u}| \cdot \cos(\theta) = \left|\nabla f\left(1, \ln(2), \frac{1}{2}\right)\right| \cdot \cos(\theta)$$

der $\theta$ er vinkelen mellom $\nabla f(1, \ln(2), 1/2)$ og $\mathbf{u}$, og hvor vi har brukt at $|\mathbf{u}| = 1$. Retningen $\mathbf{u}$ som gir at den retningsderiverte blir størst mulig er altså den retningen som peker i samme retning som $\nabla f(1, \ln(2), 1/2)$, det vil si, $\theta = 0$.

Altså gir retningen

$$\mathbf{u} = \frac{(2, 2, 1)}{|(2, 2, 1)|} = \left(\frac{2}{3}, \, \frac{2}{3}, \, \frac{1}{3}\right)$$

at den retningsderiverte til $f$ i punktet $(1, \ln(2), 1/2)$ blir størst mulig.

Kildesett: course=TMA4105 term=var year=2024 problem=4 file=tma4105_2024v.pdf
