### **Løsning til Oppgave 4**

(a) Vi bruker formler for retningsderivert av en funksjon $f(x, y, z) = 2x^2 + y^2 + z^2$:

$$D_{\mathbf{u}} f(1, 1, 2) = \nabla f(1, 1, 2) \cdot \mathbf{u} = (4, 2, 4) \cdot \frac{1}{\sqrt{3}}(1, 1, 1) = \frac{10}{\sqrt{3}}$$

(b) For å finne retningen som gir den raskeste stigningen, bruker vi gradienten $\nabla f$:

$$\nabla f = (4x, 2y, 2z)$$

$$\nabla f(1, 1, 2) = (4, 2, 4)$$

Den raskeste stigningen skjer i retning av gradienten. Vi normaliserer gradienten

$$\mathbf{u} = \frac{\nabla f(1, 1, 2)}{|\nabla f(1, 1, 2)|} = \frac{1}{6}(4, 2, 4) = \left(\frac{2}{3}, \frac{1}{3}, \frac{2}{3}\right)$$

(c) Gradienten $\nabla f(1, 1, 2) = (4, 2, 4)$ er normal til flata $f(x, y, z) = 6$ i punktet $(1, 1, 2)$. Dermed kan vi parameterfremstille den rette linjen som går gjennom punktet $(1, 1, 2)$ normalt på flata som

$$\mathbf{r}(t) = (1 + 4t,\; 1 + 2t,\; 2 + 4t)$$

Kildesett: course=TMA4105 term=sommer year=2023 problem=4 file=tma4105_2023k.pdf
