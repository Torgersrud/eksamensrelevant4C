### **Løsning til Oppgave 4**

**a)** Vi har at

$$\nabla f(x, y) = 2x(y - 1) \, \mathbf{i} + (x^2 + y^2 - 2) \, \mathbf{j}.$$

For å finne de kritiske punktene ser vi på $\nabla f(x, y) = 0$, det vil si,

$$2x(y - 1) = 0 \tag{1}$$

$$x^2 + y^2 - 2 = 0. \tag{2}$$

Ligning (1) medfører $x = 0$ eller $y = 1$. Innsatt for $x = 0$ i (2) får vi $y = \pm\sqrt{2}$. Innsatt for $y = 1$ i (2) får vi $x = \pm 1$.

Altså er $(0, \pm\sqrt{2})$ og $(\pm 1, 1)$ kritiske punkter.

La $\Delta \colon \mathbb{R}^2 \to \mathbb{R}$ være gitt ved

$$\Delta(x, y) = f_{xx}(x, y) \, f_{yy}(x, y) - [f_{xy}(x, y)]^2 = 4y(y - 1) - 4x^2.$$

Da

$$\Delta(0, -\sqrt{2}) = -4\sqrt{2}(-\sqrt{2} - 1) > 0, \qquad f_{xx}(0, -\sqrt{2}) = 2(-\sqrt{2} - 1) < 0$$

$$\Delta(0, \sqrt{2}) = 4\sqrt{2}(\sqrt{2} - 1) > 0, \qquad f_{xx}(0, \sqrt{2}) = 2(\sqrt{2} - 1) > 0$$

$$\Delta(\pm 1, 1) = -4 < 0,$$

så gir annenderiverttesten at $(0, -\sqrt{2})$ er et lokalt maksimum, $(0, \sqrt{2})$ et lokalt minimum og at $(\pm 1, 1)$ er sadelpunkter.

**b)** La $g \colon \mathbb{R}^2 \to \mathbb{R}$ være gitt ved

$$g(x, y) = x^2 + y^2,$$

som gir $\nabla g(x, y) = 2x \, \mathbf{i} + 2y \, \mathbf{j}$.

De nødvendige og tilstrekkelige betingelsene for minste verdi er gitt ved

$$\nabla f = \lambda \nabla g, \quad g(x, y) = 6.$$

Fra $\nabla f = \lambda \nabla g$ får vi

$$2x(y - 1) = \lambda \cdot 2x \tag{3}$$

$$x^2 + y^2 - 2 = \lambda \cdot 2y. \tag{4}$$

Innsatt for $g(x, y) = x^2 + y^2 = 6$ kan vi skrive (4) som

$$4 = \lambda \cdot 2y. \tag{4'}$$

Ved å gange (3) med $y/2$ og (4′) med $x/2$, for deretter å trekke de fra hverandre får vi

$$x(y(y - 1) - 2) = x(y + 1)(y - 2) = 0,$$

som gir $x = 0$, $y = -1$ eller $y = 2$. Innsatt for $x = 0$ i $g(x, y) = 6$ får vi $y = \pm\sqrt{6}$. Innsatt for $y = -1$ i $g(x, y) = 6$ får vi $x = \pm\sqrt{5}$. Innsatt for $y = 2$ i $g(x, y) = 6$ får vi $x = \pm\sqrt{2}$.

Ettersom

$$f(x, y) = \begin{cases} 0 & \text{for } (x, y) = (0, \pm\sqrt{6}) \\[2pt] \frac{2}{3} & \text{for } (x, y) = (\pm\sqrt{2}, 2) \\[2pt] -\frac{25}{3} & \text{for } (x, y) = (\pm\sqrt{5}, -1) \end{cases}$$

får vi at den minste verdien til $f$ på sirkelen $x^2 + y^2 = 6$ er lik $-25/3$.

Alle de kritiske punktene vi fant i a) ligger i området $x^2 + y^2 \le 6$. Da $f(0, \pm\sqrt{2}) = \mp\frac{4}{3}\sqrt{2}$, og $f(\pm 1, 1) = -\frac{5}{3}$, får vi at den minste verdien til $f$ på området $x^2 + y^2 \le 6$ inntreffer langs randen, nærmere bestemt i punktene $(\pm\sqrt{5}, -1)$ og har verdien $-25/3$.

Kildesett: course=TMA4105 term=sommer year=2013 problem=4 file=tma4105_13k.pdf
