### **Løsning til Oppgave 1**

La $g(x, y) = x + y$. For å benytte Lagranges multiplikatormetode trenger vi $\nabla p$ og $\nabla g$:

$$\nabla p(x, y) = \bigl(10x + 2y, \, 2x + 6y\bigr), \qquad \nabla g(x, y) = (1, 1).$$

De nødvendige betingelsene for minste produksjonskostnad er:

$$\nabla p = \lambda \nabla g, \qquad g(x, y) = 39.$$

Fra $\nabla p = \lambda \nabla g$ får vi

$$10x + 2y = \lambda$$

$$2x + 6y = \lambda$$

som gir

$$10x + 2y = \lambda = 2x + 6y \quad \text{det vil si} \quad 2x = y.$$

Fra $g(x, 2x) = 3x = 39$ får vi $x = 13$ og $y = 2x = 26$.

Den minste produksjonskostnaden er dermed

$$p(13, 26) = 5 \cdot 13^2 + 2 \cdot 13 \cdot 26 + 3 \cdot 26^2 = 4349.$$

*Kjeldevarsel: i løysingsarket manglar leddet $800$ i den siste utrekninga — summen $5 \cdot 13^2 + 2 \cdot 13 \cdot 26 + 3 \cdot 26^2$ blir $3549$, og svaret $4349$ er først rett for det fulle uttrykket $p(13, 26) = 5 \cdot 13^2 + 2 \cdot 13 \cdot 26 + 3 \cdot 26^2 + 800$ (kontrollrekna).*

Kildesett: course=TMA4105 term=var year=2024 problem=1 file=tma4105_2024v.pdf
