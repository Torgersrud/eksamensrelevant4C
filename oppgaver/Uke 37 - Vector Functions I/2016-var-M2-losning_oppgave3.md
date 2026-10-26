### **Løsning til Oppgave 3**

Ved å sette inn for $(x, y) = (0, 1)$ i ligningen for skalarfeltet $z(x, y)$,

$$3x^2z^4 + 2y^3z = 5x^2 + 2y^4x, \tag{3}$$

får vi at $z(0, 1) = 0$. Implisitt derviasjon av (3) med hensyn på $x$ gir

$$6xz^4 + 12x^2z^3\frac{\partial z}{\partial x} + 2y^3\frac{\partial z}{\partial x} = 10x + 2y^4$$

som innsatt for $(x, y) = (0, 1)$ gir

$$\frac{\partial z}{\partial x}(0, 1) = 1.$$

Implisitt derviasjon av (3) med hensyn på $y$ gir

$$12x^2z^3\frac{\partial z}{\partial y} + 6y^2z + 2y^3\frac{\partial z}{\partial y} = 8xy^3$$

som innsatt for $(x, y) = (0, 1)$ gir

$$\frac{\partial z}{\partial y}(0, 1) = 0.$$

Altså er $\nabla z(0, 1) = (1, 0)$.

*Kjeldevarsel: løsningsforslaget trykkjer «Implisitt derviasjon» i begge delane av løysinga — trykkfeil for «derivasjon»; teksten er teken vare på som han står.*

Kildesett: course=TMA4105 term=var year=2016 problem=3 file=tma4105_2016v.pdf
