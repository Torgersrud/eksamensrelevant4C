### **Løsning til Oppgave 2**

**a)** Ved derivasjon får vi

$$\frac{\partial T}{\partial x} = 16 - 4x - 2y \qquad \text{og} \qquad \frac{\partial T}{\partial y} = 18 - 2x - 6y.$$

I det kritiske punktet er begge de partiellderiverte lik null, altså $2x + y = 8$ og $x + 3y = 9$. Av den første ligningen får vi $y = 8 - 2x$ som innsatt i den andre gir $x + 3(8 - 2x) = 9$, det gir $x = 3$ og følgelig $y = 2$. Det kritiske punktet er altså $(3, 2)$.

Av figuren med nivåkurver for $T(x, y)$ ser vi at ekstremaltemperaturene oppnås i det kritiske punktet (som vi har regnet ut til å være $(3, 2)$) og i et av (eller begge) hjørnepunktene $(0, 0)$ og $(5, 5)$. Regner vi ut temperaturen i disse tre punktene, får vi

$$T(3, 2) = 54, \qquad T(0, 0) = 12, \qquad T(5, 5) = 7.$$

Følgelig er $T_{\max} = 54$ og $T_{\min} = 7$.

Ved å telle nivåkurvene, kunne vi sett at det må være i hjørnet $(5, 5)$ (og ikke i $(0, 0)$) at vi har ekstremaltemperatur. Vi kunne også funnet $T_{\max}$ og $T_{\min}$ uten bruk av nivåkurvene ved å drøfte temperaturen på randkurven, og sammenlignet den høyeste og laveste temperaturen på randkurven med temperaturen i det kritiske punktet $(3, 2)$.

**b)** Vi søker maksimum for $T(x, y)$ under bibetingelsen

$$g(x, y) = 2x + y - 4 = 0$$

og kan bruke Lagranges multiplikatormetode. Vi har

$$\nabla T(x, y) = \lambda \nabla g(x, y) \iff \left\{ \begin{array}{l} 16 - 4x - 2y = 2\lambda, \\ 18 - 2x - 6y = \lambda, \end{array} \right.$$

og får følgelig $8 - 2x - y = \lambda = 18 - 2x - 6y$. Det gir $y = 2$ som innsatt i $2x + y - 4 = 0$ gir $x = 1$. Maksimumstemperaturen på linjen $2x + y = 4$ er følgelig $T(1, 2) = 46$. At dette er maksimum (og ikke minimum), ser vi av nivåkurvene til $T$.

Som kontroll kan vi tegne inn linjen $2x + y = 4$ på figuren med nivåkurver, og se at $2x + y = 4$ tangerer en nivåkurve (som må være $T(x, y) = 46$) i punktet $(1, 2)$.

**c)** Den retningsderiverte $D_{\mathbf{u}}T(P)$ for $T$ i punktet $P(1, 1)$ i retningen $\mathbf{u}$ mot punktet $Q(3, 2)$ er gitt ved

$$D_{\mathbf{u}}T(P) = \nabla T(P) \cdot \mathbf{u} = \nabla T(P) \cdot \frac{\overrightarrow{PQ}}{|\overrightarrow{PQ}|} = \langle 10, 10 \rangle \cdot \frac{\langle 2, 1 \rangle}{\sqrt{5}} = \frac{30}{\sqrt{5}} = 6\sqrt{5}.$$

Størst retningsderivert i punktet $P$ har $T$ i retningen $\nabla T(P)/|\nabla T(P)| = \langle 1, 1 \rangle/\sqrt{2}$.

For gradientvektoren $\nabla g(P)$ har vi

$$\nabla g(P) = 5\mathbf{u} = 5 \cdot \frac{\langle 2, 1 \rangle}{\sqrt{5}} = \sqrt{5}\,\langle 2, 1 \rangle$$

siden $\nabla g(P)$ skal ha lengde lik $5$ (maksimal retningsderivert for $g$ i $P$) og retning lik enhetsvektoren $\mathbf{u}$ (retningen der den maksimale retningsderiverte for $g$ i $P$ oppnås). For den retningsderiverte $D_{\mathbf{w}}g(P)$ for $g$ i punktet $P$ i retningen $\mathbf{w}$ mot punktet $R(2, 3)$ får vi dermed

$$D_{\mathbf{w}}g(P) = \nabla g(P) \cdot \mathbf{w} = \nabla g(P) \cdot \frac{\overrightarrow{PR}}{|\overrightarrow{PR}|} = \sqrt{5}\,\langle 2, 1 \rangle \cdot \frac{\langle 1, 2 \rangle}{\sqrt{5}} = 4.$$

Kildesett: course=SIF5005 term=sommer year=2002 problem=2 file=sif5005_02k.pdf
