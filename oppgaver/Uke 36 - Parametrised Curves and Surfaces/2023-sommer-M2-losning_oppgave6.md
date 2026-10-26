### **Løsning til Oppgave 6**

(a) Vi deriverer $\mathbf{r}(t) = (t + \sin t, \sqrt{2} \cos t, t - \sin t)$ to ganger. Da får vi at

$$\mathbf{r}'(t) = (1 + \cos t, -\sqrt{2} \sin t, 1 - \cos t)$$

$$\mathbf{r}''(t) = (-\sin t, -\sqrt{2} \cos t, \sin t)$$

Vi finner da

$$\mathbf{r}'(t) \times \mathbf{r}''(t) = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 1 + \cos t & -\sqrt{2} \sin t & 1 - \cos t \\ -\sin t & -\sqrt{2} \cos t & \sin t \end{vmatrix}$$

$$= \left(-\sqrt{2}\sin^2 t + \sqrt{2}\cos^2 t - \sqrt{2}(1 - \cos^2 t)\right)\mathbf{i} - \left(\sin t + \sin t \cos t + \sin t - \sin t \cos t\right)\mathbf{j}$$

$$+ \left(-\sqrt{2}\cos t - \sqrt{2}\cos^2 t - \sqrt{2}\sin^2 t\right)\mathbf{k}$$

$$= \left(-\sqrt{2} + \sqrt{2}\cos(2t)\right)\mathbf{i} - 2\sin t\,\mathbf{j} - \sqrt{2}(1 + \cos t)\mathbf{k}$$

Vi bruker så at

$$|\mathbf{r}'(t)| = \sqrt{(1 + \cos t)^2 + 2\sin^2 t + (1 - \cos t)^2} = \sqrt{2 + 2\cos^2 t + 2 - 2\cos^2 t} = 2$$

Videre ser vi at

$$|\mathbf{r}'(t) \times \mathbf{r}''(t)| = \sqrt{\left(-\sqrt{2} + \sqrt{2}\cos(2t)\right)^2 + 4\sin^2 t + \left(-\sqrt{2} - \sqrt{2}\cos t\right)^2}$$

$$= \sqrt{2 - 4\cos(2t) + 2\cos^2(2t) + 4\sin^2 t + 2 + 4\cos t + 2\cos^2 t}$$

$$= \sqrt{8}$$

Dermed får vi at krumningen

$$K = \frac{|\mathbf{r}'(t) \times \mathbf{r}''(t)|}{|\mathbf{r}'(t)|^3} = \frac{\sqrt{8}}{2^3} = \frac{2\sqrt{2}}{8} = \frac{1}{\sqrt{2}}$$

Vi ser at krumningen er konstant.

(b) Buelengden er gitt ved

$$L = \int_0^{2\pi} |\mathbf{r}'(t)| dt = \int_0^{2\pi} 2 dt = 4\pi$$

Kildesett: course=TMA4105 term=sommer year=2023 problem=6 file=tma4105_2023k.pdf
