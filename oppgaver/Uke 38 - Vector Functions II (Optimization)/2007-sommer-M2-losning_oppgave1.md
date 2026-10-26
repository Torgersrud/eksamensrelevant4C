### **Løsning til Oppgave 1**

Normalvektoren til planet er $\mathbf{N} = \langle 1, 1, -3 \rangle$. Hvis vi dekomponerer vektoren $\mathbf{b} = \langle 22, 0, 0 \rangle$ (som svarer til et punkt i planet) til summen av en vektor $\mathbf{b}_{\parallel}$ som er paralell med $\mathbf{N}$ og en vektor $\mathbf{b}_{\perp}$ som står normalt på $\mathbf{N}$, vil $\mathbf{b}_{\parallel}$ gi oss det nærmeste punktet:

$$\mathbf{b}_{\parallel} = \frac{\mathbf{b} \cdot \mathbf{N}}{|\mathbf{N}|^2} \, \mathbf{N} = \frac{\langle 22, 0, 0 \rangle \cdot \langle 1, 1, -3 \rangle}{1^2 + 1^2 + 3^2} \, \langle 1, 1, -3 \rangle = 2 \langle 1, 1, -3 \rangle = \langle 2, 2, -6 \rangle.$$

Punktet i planet som ligger nærmest origo, er $(2, 2, -6)$.

Oppgaven kan også løses ved å minimere funksjonen $f(x, y, z) = x^2 + y^2 + z^2$ under bibetingelsen $x + y - 3z = 22$ (Lagrange).

Kildesett: course=TMA4105 term=sommer year=2007 problem=1 file=tma4105_07k.pdf
