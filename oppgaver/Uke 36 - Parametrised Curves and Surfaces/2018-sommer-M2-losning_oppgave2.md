### **Løsning til Oppgave 2**

I vårt tilfelle er

$$\mathbf{r}'(t) = \left(-\sqrt{2}\sin t, \; -\cos t, \; \cos t\right)$$

slik at $|\mathbf{r}'(t)| = \sqrt{2}$. Dermed er enhetstangentvektoren i et vilkårlig punkt på kurven gitt ved

$$\hat{\mathbf{T}}(t) = \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|} = \left(-\sin t, \; -\frac{\cos t}{\sqrt{2}}, \; \frac{\cos t}{\sqrt{2}}\right).$$

Siden

$$\hat{\mathbf{T}}'(t) = \left(-\cos t, \; \frac{\sin t}{\sqrt{2}}, \; -\frac{\sin t}{\sqrt{2}}\right)$$

og $|\hat{\mathbf{T}}'(t)| = 1$ får vi at enhetsnormalvektoren i et vilkårlig punkt på kurven er gitt ved

$$\hat{\mathbf{N}}(t) = \frac{\hat{\mathbf{T}}'(t)}{|\hat{\mathbf{T}}'(t)|} = \hat{\mathbf{T}}'(t) = \left(-\cos t, \; \frac{\sin t}{\sqrt{2}}, \; -\frac{\sin t}{\sqrt{2}}\right).$$

Ved å utnytte at akselerasjonsvektoren kan dekomponeres i en tangentkomponent og en normalkomponent,

$$\mathbf{r}''(t) = \frac{d}{dt}|\mathbf{r}'(t)|\,\hat{\mathbf{T}}(t) + \kappa(t)\,|\mathbf{r}'(t)|^2\,\hat{\mathbf{N}}(t),$$

får vi i vårt tilfelle at

$$\mathbf{r}''(t) = \left(-\sqrt{2}\cos t, \; \sin t, \; -\sin t\right) = 2\kappa(t)\,\hat{\mathbf{N}}(t)$$

som gir at krumningen i et vilkårlig punkt på kurven er gitt ved

$$\kappa(t) = \frac{1}{\sqrt{2}}.$$

Kildesett: course=TMA4105 term=sommer year=2018 problem=2 file=tma4105_2018k.pdf
