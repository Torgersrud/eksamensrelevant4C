### **Løsning til Oppgave 6**

**a)**

$$\mathbf{r}(t) = \langle \sqrt{2} \cos t, \sqrt{2} \cos t, 2 \sin t \rangle$$
$$\mathbf{r}'(t) = \langle -\sqrt{2} \sin t, -\sqrt{2} \sin t, 2 \cos t \rangle$$
$$|\mathbf{r}'(t)| = \sqrt{2 \sin^2 t + 2 \sin^2 t + 4 \cos^2 t} = 2$$
$$\mathbf{T} = \frac{\mathbf{r}'(t)}{|\mathbf{r}'(t)|} = \frac{\mathbf{r}'(t)}{2} = \left\langle -\sin t \, \frac{\sqrt{2}}{2}, \; -\sin t \, \frac{\sqrt{2}}{2}, \; \cos t \right\rangle$$
$$\mathbf{r}''(t) = \langle -\sqrt{2} \cos t, -\sqrt{2} \cos t, -2 \sin t \rangle$$
$$\mathbf{r}'(t) \times \mathbf{r}''(t) = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ -\sqrt{2} \sin t & -\sqrt{2} \sin t & 2 \cos t \\ -\sqrt{2} \cos t & -\sqrt{2} \cos t & -2 \sin t \end{vmatrix} = \langle 2\sqrt{2}, -2\sqrt{2}, 0 \rangle$$
$$|\mathbf{r}'(t) \times \mathbf{r}''(t)| = \sqrt{8 + 8} = 4$$
$$\kappa = \frac{|\mathbf{r}'(t) \times \mathbf{r}''(t)|}{|\mathbf{r}'(t)|^3} = \frac{4}{8} = \frac{1}{2}.$$

**b)** Hvis vi skriver $\mathbf{r}(t) = \langle x(t), y(t), z(t) \rangle$, har vi $x(t) = y(t) = \sqrt{2} \cos t$, så kurven ligger i planet $x = y$. Videre har vi $x(t)^2 + y(t)^2 + z(t)^2 = 2 \cos^2 t + 2 \cos^2 t + 4 \sin^2 t = 4$, så kurven ligger også på kuleflaten $x^2 + y^2 + z^2 = 4$. ($C$ er dessuten en lukket kurve, så den utgjør hele skjæringskurven mellom disse to flatene.) Siden planet $x = y$ går gjennom kulens sentrum (origo), er $C$ en storsirkel på kuleflaten. Det følger at sirkelen $C$ har sentrum i origo og radius lik $2$.

Kildesett: course=SIF5005 term=var year=2000 problem=6 file=sif5005_00v.pdf
