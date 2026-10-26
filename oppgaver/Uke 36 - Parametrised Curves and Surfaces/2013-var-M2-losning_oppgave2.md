### **Løsning til Oppgave 2**

Ettersom $\mathbf{v}(t) = \mathbf{i} + \left(t^{1/2} - \frac{1}{2}t^{-1/2}\right)\mathbf{j} + \mathbf{k}$, får vi at

$$\int_1^4 |\mathbf{v}(t)| \, dt = \int_1^4 \sqrt{\frac{(1 + 2t)^2}{4t}} \, dt.$$

Substitusjonen $u = \sqrt{t}$ gir $du = \frac{1}{2\sqrt{t}} \, dt$ med nye integrasjonsgrenser $u = 1$ og $u = 2$. Dermed er

$$\int_1^4 |\mathbf{v}(t)| \, dt = \int_1^2 (1 + 2u^2) \, du = \frac{17}{3}.$$

Kildesett: course=TMA4105 term=var year=2013 problem=2 file=tma4105_13v.pdf
