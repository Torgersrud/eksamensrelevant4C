### **Løsning til Oppgave 4**

**a)** Buelengden av $C$ er gitt ved

$$S = \int_C ds = \int_{1/2}^{2} |\mathbf{v}(t)| \, dt.$$

Vi deriverer $\mathbf{r}$ og får

$$\mathbf{v}(t) = \frac{d\mathbf{r}}{dt}(t) = \left[ -\frac{1}{t^2}, \; \sqrt{2}, \; t^2 \right].$$

Vi beregner lengden av $\mathbf{v}$:

$$|\mathbf{v}(t)| = \sqrt{\frac{1}{t^4} + 2 + t^4} = \frac{\sqrt{(1 + t^4)^2}}{t^2} = \frac{1}{t^2} + t^2.$$

Da får vi

$$\int_{1/2}^{2} |\mathbf{v}(t)| \, dt = \int_{1/2}^{2} \left( \frac{1}{t^2} + t^2 \right) dt = \left[ -\frac{1}{t} + \frac{t^3}{3} \right]_{1/2}^{2} = \frac{33}{8}.$$

Buelengden av $C$ er $\dfrac{33}{8}$.

**b)** Enhetstangentvektoren er $\mathbf{T} = \dfrac{\mathbf{v}}{|\mathbf{v}|}$, og med $|\mathbf{v}|$ fra a) får vi

$$\mathbf{T}(t) = \frac{t^2}{1 + t^4} \left[ -\frac{1}{t^2}, \; \sqrt{2}, \; t^2 \right].$$

I formellista står det at

$$\mathbf{a}(t) = v'(t) \, \mathbf{T}(t) + \kappa(t) \, v^2(t) \, \mathbf{N}(t). \tag{1}$$

Ved å ta kryssprodukt av (1) med $\mathbf{T}$ får vi

$$\mathbf{a} \times \mathbf{T} = \kappa \, v^2 \, \mathbf{N} \times \mathbf{T},$$

fordi $\mathbf{T} \times \mathbf{T} = 0$. Siden $\mathbf{N}$ og $\mathbf{T}$ er enhetsvektorer med $\mathbf{N} \perp \mathbf{T}$, har vi $|\mathbf{N} \times \mathbf{T}| = 1$, og lengden av likningen gir

$$\kappa = \frac{|\mathbf{a} \times \mathbf{T}|}{v^2}.$$

Vi beregner $\mathbf{a}(t) = \dfrac{d\mathbf{v}}{dt} = \left[ \dfrac{2}{t^3}, \; 0, \; 2t \right]$. Vi setter inn $t = 1$ og får $\mathbf{a}(1) = [2, 0, 2]$ og $\mathbf{T}(1) = \left[ -\dfrac{1}{2}, \; \dfrac{\sqrt{2}}{2}, \; \dfrac{1}{2} \right]$. Derfor er

$$\mathbf{a} \times \mathbf{T} = \left[ -\sqrt{2}, \; -2, \; \sqrt{2} \right], \qquad |\mathbf{a} \times \mathbf{T}| = 2\sqrt{2}.$$

Siden $v(1) = |\mathbf{v}(1)| = 2$, følger det at

$$\kappa(1) = \frac{2\sqrt{2}}{4} = \frac{\sqrt{2}}{2}.$$

Kildesett: course=TMA4105 term=sommer year=2005 problem=4 file=tma4105_05k.pdf
