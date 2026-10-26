### **Løsning til Oppgave 3**

a) Hastigheten til en partikkel er bestemt ved

$$\mathbf{v}(t) = \frac{d\mathbf{r}}{dt} = \frac{1}{t} \, \mathbf{i} + \sqrt{2} \, \mathbf{j} + t \, \mathbf{k}, \quad t > 0.$$

Farten er lengden til hastigheten, det vil si

$$v(t) = |\mathbf{v}(t)| = \sqrt{\frac{1}{t^2} + 2 + t^2} = \sqrt{\frac{1 + 2t^2 + t^4}{t^2}} = \sqrt{\frac{(1 + t^2)^2}{t^2}} = \frac{1 + t^2}{t}, \quad t > 0.$$

Akselerasjonen til en partikkel er bestemt ved

$$\mathbf{a}(t) = \frac{d\mathbf{v}}{dt} = -\frac{1}{t^2} \, \mathbf{i} + \mathbf{k}, \quad t > 0.$$

b) For å regne ut krumningen $\kappa$ og torsjonen $\tau$ trenger vi å finne $|\mathbf{v} \times \mathbf{a}|$. Vi har at

$$(\mathbf{v} \times \mathbf{a})(t) = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ \frac{1}{t} & \sqrt{2} & t \\ -\frac{1}{t^2} & 0 & 1 \end{vmatrix} = \sqrt{2} \, \mathbf{i} - \frac{2}{t} \, \mathbf{j} + \frac{\sqrt{2}}{t^2} \, \mathbf{k}, \quad t > 0,$$

slik at

$$|(\mathbf{v} \times \mathbf{a})(t)| = \sqrt{2 + \frac{4}{t^2} + \frac{2}{t^4}} = \frac{\sqrt{2(t^4 + 2t^2 + 1)}}{t^2} = \frac{\sqrt{2}(1 + t^2)}{t^2}, \quad t > 0.$$

Dermed er

$$\kappa(t) = \frac{|(\mathbf{v} \times \mathbf{a})(t)|}{(v(t))^3} = \frac{t^3 (1 + t^2)}{(1 + t^2)^3} \cdot \frac{\sqrt{2}(1 + t^2)}{t^2} = \frac{\sqrt{2} \, t}{(1 + t^2)^2}, \quad t > 0.$$

For å regne ut torsjonen $\tau$ ser vi på trippelproduktet $((\mathbf{v} \times \mathbf{a}) \cdot \mathbf{a}')(t)$. Ettersom

$$\mathbf{a}'(t) = \frac{d\mathbf{a}}{dt} = \frac{2}{t^3} \, \mathbf{i}, \quad t > 0,$$

får vi at

$$\tau(t) = \frac{((\mathbf{v} \times \mathbf{a}) \cdot \mathbf{a}')(t)}{|(\mathbf{v} \times \mathbf{a})(t)|^2} = \frac{t^4}{2(1 + t^2)^2} \cdot \frac{2\sqrt{2}}{t^3} = \frac{\sqrt{2} \, t}{(1 + t^2)^2}, \quad t > 0.$$

Kildesett: course=TMA4105 term=sommer year=2011 problem=3 file=tma4105_11k.pdf
