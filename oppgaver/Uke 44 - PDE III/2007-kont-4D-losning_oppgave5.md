### **Løsning til Oppgave 5**

a) Vi har at $f(x,y) = v_{xx} + v_{yy} = (u_{xx} + u_{yy})_{xx} + (u_{xx} + u_{yy})_{yy} = u_{xxxx} + 2u_{xxyy} + u_{yyyy}$. Videre er $\nabla^2 u = u_{xx} + u_{yy} = v(x,y)$, så $v(x,y) = 0$ på randen er ekvivalent med at $\nabla^2 u = 0$ på randen.

b) Vi har tilnærmelsen

$$f''(x) \approx \frac{1}{h^2} \big( f(x-h) - 2f(x) + f(x+h) \big)$$

Vi har da at $v_{ij} = v(ih, jh)$ må tilfredstille

$$\frac{1}{1/9} (v_{01} + v_{21} + v_{10} + v_{12} - 4v_{11}) = -1$$

$$\frac{1}{1/9} (v_{11} + v_{31} + v_{20} + v_{22} - 4v_{21}) = -1$$

$$\frac{1}{1/9} (v_{02} + v_{22} + v_{11} + v_{13} - 4v_{12}) = -1$$

$$\frac{1}{1/9} (v_{12} + v_{32} + v_{21} + v_{23} - 4v_{22}) = -1$$

Innsetter randverdiar $v_{21} + v_{12} - 4v_{11} = -\frac{1}{9}$, $v_{11} + v_{22} - 4v_{21} = -\frac{1}{9}$, $v_{22} + v_{11} - 4v_{12} = -\frac{1}{9}$ og $v_{12} + v_{21} - 4v_{22} = -\frac{1}{9}$. Vi har alså $A\mathbf{v} = -\frac{1}{9}(1,1,1,1)$, der $\mathbf{v} = (v_{11}, v_{12}, v_{21}, v_{22})$.

Videre får vi tilsvarende at

$$\frac{1}{1/9} (u_{01} + u_{21} + u_{10} + u_{12} - 4u_{11}) = v_{11}$$

$$\frac{1}{1/9} (u_{11} + u_{31} + u_{20} + u_{22} - 4u_{21}) = v_{21}$$

$$\frac{1}{1/9} (u_{02} + u_{22} + u_{11} + u_{13} - 4u_{12}) = v_{12}$$

$$\frac{1}{1/9} (u_{12} + u_{32} + u_{21} + u_{23} - 4u_{22}) = v_{22}$$

Dvs at $A\mathbf{u} = \mathbf{v}$, der $\mathbf{u} = (u_{11}, u_{12}, u_{21}, u_{22})$. Dvs at $A^2\mathbf{u} = -\frac{1}{9}(1,1,1,1)$.

**Kjeldevarsel:** Likningane er trykte med faktoren skriven som $1/(1/9)$, dvs. $1/h^2 = 9$ framfor parentesen. Linja $A\mathbf{v} = -\frac{1}{9}(1,1,1,1)$ stemmer med $A = \text{tridiag}(1, -4, 1)$-matrisa (utan $1/h^2$-faktor): $9 \cdot A\mathbf{v} = -(1,1,1,1)$. Men då skal det same steget for $u$-systemet gje $A\mathbf{u} = \frac{1}{9}\mathbf{v}$, ikkje $A\mathbf{u} = \mathbf{v}$ som trykt, og følgjeleg $A^2\mathbf{u} = -\frac{1}{81}(1,1,1,1)$, ikkje $-\frac{1}{9}(1,1,1,1)$. Trykkfeila er altså ein faktor 9 i dei to siste stega; strukturen — to koplede 5-punkts Laplace-system — er korrekt. Ordtøya "tilfredstille" og "alså" er som i kjelda.

Kildesett: course=TMA4135 term=kont year=2007 problem=5 file=tma4135_07k.pdf
