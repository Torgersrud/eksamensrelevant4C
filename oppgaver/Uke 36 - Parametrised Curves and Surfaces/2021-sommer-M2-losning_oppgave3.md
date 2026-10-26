### **Løsning til Oppgave 3**

Vi kan parametrisere sylinderen $x^2 + (y - 1)^2 = 1$ som

$$x = \cos\theta, \quad y = 1 + \sin\theta, \quad z = z,$$

der $0 \leq \theta < 2\pi$. Ligningen $z = x^2 + 2y^2$ gir da

$$z = \cos^2\theta + 2(1 + \sin\theta)^2 = \cos^2\theta + 2 + 4\sin\theta + 2\sin^2\theta = 3 + 4\sin\theta + \sin^2\theta,$$

slik at skjæringskurven er gitt ved

$$\mathbf{r}(\theta) = (\cos\theta, \; 1 + \sin\theta, \; 3 + 4\sin\theta + \sin^2\theta), \quad (0 \leq \theta < 2\pi).$$

Deriverer vi dette, får vi

$$\mathbf{r}'(\theta) = (-\sin\theta, \; \cos\theta, \; 4\cos\theta + 2\sin\theta\cos\theta).$$

Punktet $(-1, 1, 3)$ svarer til $\theta$ der $\cos\theta = -1$ og $\sin\theta = 0$, som gir $\theta = \pi$. Da har vi

$$\mathbf{r}'(\pi) = (0, -1, -4), \qquad |\mathbf{r}'(\pi)| = \sqrt{17}, \qquad \widehat{\mathbf{T}} = \left(0, \; \frac{-1}{\sqrt{17}}, \; \frac{-4}{\sqrt{17}}\right).$$

Kildesett: course=TMA4105 term=sommer year=2021 problem=3 file=tma4105_2021k.pdf
