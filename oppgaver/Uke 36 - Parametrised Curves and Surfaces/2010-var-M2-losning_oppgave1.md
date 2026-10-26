### **Løsning til Oppgave 1**

a) Vi deriverer posisjonsvektoren m.h.p. $t$. Da får vi suksessivt hastigheten og akselerasjonen.

Hastigheten er

$$\mathbf{v} = \dot{\mathbf{r}}(t) = \mathbf{i} + \sqrt{2} t \, \mathbf{j} + t^2 \, \mathbf{k},$$

akselerasjonen er

$$\mathbf{a} = \ddot{\mathbf{r}}(t) = \sqrt{2} \, \mathbf{j} + 2t \, \mathbf{k},$$

farten er

$$|\mathbf{v}| = v = \dot{s} = \sqrt{1 + 2t^2 + t^4} = 1 + t^2.$$

Vi finner buelengden ved å integrere $ds = (1 + t^2) dt$. Altså

$$S = \int_0^1 (1 + t^2) \, dt = \frac{4}{3}.$$

b) For å beregne krumningen finner vi først vektorproduktet

$$\mathbf{v} \times \mathbf{a} = \sqrt{2} t^2 \, \mathbf{i} - 2t \, \mathbf{j} + \sqrt{2} \, \mathbf{k},$$

og vi finner

$$\kappa = \frac{\sqrt{2}}{(1 + t^2)^2}.$$

Vi har $\dot{\mathbf{a}} = \mathbf{r}'''(t) = 2 \, \mathbf{k}$, så trippelvektorproduktet blir

$$(\mathbf{v} \times \mathbf{a}) \cdot \dot{\mathbf{a}} = 2\sqrt{2},$$

og torsjonen

$$\tau = \frac{\sqrt{2}}{(1 + t^2)^2}.$$

Kildesett: course=TMA4105 term=var year=2010 problem=1 file=tma4105_10v.pdf
