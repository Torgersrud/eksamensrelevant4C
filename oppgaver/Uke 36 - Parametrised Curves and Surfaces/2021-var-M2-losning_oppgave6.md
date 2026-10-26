### **Løsning til Oppgave 6**

For hvert par $(x, z)$ med $x^2 + z^2 = 1$ finnes det en unik $t$ med $0 \leq t < 2\pi$ slik at $(x, z) = (\cos t, \sin t)$; det er også et unikt punkt på skjæringskurven $C$ med disse $x$- og $z$-koordinatene, siden $y$-koordinaten må være gitt ved $y = 2 - z = 2 - \sin t$. Et punkt i $C$ er dermed gitt ved $\mathbf{r}(t)$ for en unik $t$ med $0 \leq t < 2\pi$, slik at $\mathbf{r}(t)$ er én-én-tydig bortsett fra i endepunktene av intervallet $[0, 2\pi]$. Siden $\mathbf{r}(t)$ i tillegg er en glatt funksjon, betyr dette at $\mathbf{r}(t)$ er en (glatt) parametrisering av $C$.

For å finne krumningen bruker vi formelen

$$\kappa = \frac{|\mathbf{r}'(t) \times \mathbf{r}''(t)|}{|\mathbf{r}'(t)|^3}.$$

Vi har

$$\mathbf{r}'(t) = (-\sin t, -\cos t, \cos t),$$

$$|\mathbf{r}'(t)| = \sqrt{\sin^2 t + \cos^2 t + \cos^2 t} = \sqrt{1 + \cos^2 t},$$

$$\mathbf{r}''(t) = (-\cos t, \sin t, -\sin t),$$

$$\mathbf{r}'(t) \times \mathbf{r}''(t) = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -\sin t & -\cos t & \cos t \\ -\cos t & \sin t & -\sin t \end{vmatrix}$$

$$= (\cos t \sin t - \cos t \sin t, \; -(\sin^2 t + \cos^2 t), \; -\sin^2 t - \cos^2 t) = (0, -1, -1),$$

$$|\mathbf{r}'(t) \times \mathbf{r}''(t)| = \sqrt{0 + 1 + 1} = \sqrt{2}.$$

Dermed får vi at krumningen er gitt ved

$$\kappa = \frac{\sqrt{2}}{(1 + \cos^2 t)^{3/2}}.$$

Vi ser da at krumningen er

* størst når $\cos^2 t = 0 \iff t = \pi/2, 3\pi/2$, altså i punktene $\mathbf{r}(\pi/2) = (0, 1, 1)$, $\mathbf{r}(3\pi/2) = (0, 3, -1)$,
* minst når $\cos^2 t = 1 \iff t = 0, \pi$, altså i punktene $\mathbf{r}(0) = (1, 2, 0)$, $\mathbf{r}(\pi) = (-1, 2, 0)$.

Kildesett: course=TMA4105 term=var year=2021 problem=6 file=tma4105_2021v.pdf
