### **Løsning til Oppgave 3**

Kurven er beskrevet ved

$$\mathbf{r}(t) = \int_0^t \cos(u^2) \, du \; \mathbf{i} + \int_0^t \sin(u^2) \, du \; \mathbf{j}, \quad t \ge 0.$$

Fundamentalsetningen i kalkulus gir

$$\mathbf{v}(t) = \frac{d\mathbf{r}}{dt} = \cos(t^2) \, \mathbf{i} + \sin(t^2) \, \mathbf{j}.$$

Buelengden er gitt ved

$$s(t) = \int_0^t |\mathbf{v}(\tau)| \, d\tau = \int_0^t d\tau = t.$$

Altså er $s = t$ og $\mathbf{T} = \mathbf{v}$. Dette gir

$$\frac{d\mathbf{T}}{ds} = \frac{d\mathbf{T}}{dt} = 2t\left(-\sin(t^2) \, \mathbf{i} + \cos(t^2) \, \mathbf{j}\right),$$

og at krumningen er gitt ved

$$\kappa(t) = \left|\frac{d\mathbf{T}}{ds}\right| = 2t.$$

Fra uttrykkene for krumningen og buelengden ser vi at $\kappa(t) = 2s(t)$, altså at de er proporsjonale.

Kildesett: course=TMA4105 term=var year=2012 problem=3 file=tma4105_12v_ny.pdf
