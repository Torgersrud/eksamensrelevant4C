### **Løsning til Oppgave 2**

Vi har

$$\mathbf{r}(t) = \langle t, \; \tfrac{1}{\sqrt{2}} t^2, \; \tfrac{1}{3} t^3 \rangle, \qquad \mathbf{r}'(t) = \langle 1, \; \sqrt{2}\, t, \; t^2 \rangle, \qquad \mathbf{r}''(t) = \langle 0, \; \sqrt{2}, \; 2t \rangle.$$

**a)** Da er

$$|\mathbf{r}'(t)| = \sqrt{1^2 + (\sqrt{2} t)^2 + (t^2)^2} = \sqrt{1 + 2t^2 + t^4} = 1 + t^2.$$

Enhetstangentvektoren blir

$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|} = \frac{1}{1 + t^2} \langle 1, \; \sqrt{2}\, t, \; t^2 \rangle.$$

Vi deriverer:

$$\mathbf{T}'(t) = \frac{\sqrt{2}}{(1 + t^2)^2} \langle -\sqrt{2}\, t, \; 1 - t^2, \; \sqrt{2}\, t \rangle, \qquad |\mathbf{T}'(t)| = \frac{\sqrt{2}}{1 + t^2},$$

og dermed

$$\mathbf{N}(t) = \frac{\mathbf{T}'(t)}{|\mathbf{T}'(t)|} = \frac{1}{1 + t^2} \langle -\sqrt{2}\, t, \; 1 - t^2, \; \sqrt{2}\, t \rangle.$$

**b)** I origo ($t = 0$) er

$$\mathbf{r}''(0) = \langle 0, \; \sqrt{2}, \; 0 \rangle, \qquad \mathbf{T}(0) = \langle 1, 0, 0 \rangle, \qquad \mathbf{N}(0) = \langle 0, 1, 0 \rangle,$$

slik at akselerasjonsvektoren dekomponeres som

$$\mathbf{r}''(0) = 0 \cdot \mathbf{T}(0) + \sqrt{2} \cdot \mathbf{N}(0).$$

Vi vet også fra del (a) at $v(0) = |\mathbf{r}'(0)| = 1$, og siden den normative komponenten oppfyller $\sqrt{2} = \kappa(0) \, v(0)^2$, får vi

$$\kappa(0) = \sqrt{2}.$$

Kildesett: course=TMA4105 term=var year=2006 problem=2 file=tma4105_06v.pdf
