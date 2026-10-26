### **Løsning til Oppgave 2**

Kurven $C$ er gitt ved

$$\mathbf{r}(t) = \langle \cos t, \sin t, t \rangle, \quad t \ge 0.$$

Vi får

$$\mathbf{r}'(t) = \langle -\sin t, \cos t, 1 \rangle, \qquad v(t) = |\mathbf{r}'(t)| = \sqrt{\sin^2 t + \cos^2 t + 1} = \sqrt{2},$$

$$\mathbf{T}(t) = \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|} = \frac{1}{\sqrt{2}} \langle -\sin t, \cos t, 1 \rangle,$$

$$\frac{d\mathbf{T}}{ds} = \frac{d\mathbf{T}}{dt} \frac{dt}{ds} = \frac{1}{\sqrt{2}} \langle -\cos t, -\sin t, 0 \rangle \cdot \frac{1}{v(t)}$$

og dermed

$$\kappa(t) = \left| \frac{d\mathbf{T}}{ds} \right| = \frac{1}{\sqrt{2}} \frac{\sqrt{\cos^2 t + \sin^2 t + 0}}{\sqrt{2}} = \frac{1}{2}.$$

Krumningen $\kappa(t) = 1/2$ er konstant langs hele kurven.

Kildesett: course=TMA4105 term=sommer year=2008 problem=2 file=tma4105_08k.pdf
