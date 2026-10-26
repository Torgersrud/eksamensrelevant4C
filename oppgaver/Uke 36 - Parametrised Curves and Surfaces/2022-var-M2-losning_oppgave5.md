### **Løsning til Oppgave 5**

Buelengdeparametriseringen av en kurve $\mathbf{r}(t)$ der $t \geq 0$ er gitt ved $\mathbf{r}(t(s))$, der

$$s = s(t) = \int_0^t |\mathbf{r}'(\tau)| \, d\tau.$$

I vårt tilfelle er

$$\mathbf{r}'(t) = (\cos t, -\sin t, \sqrt{3}),$$

og

$$|\mathbf{r}'(t)| = \sqrt{\cos^2 t + \sin^2 t + 3} = \sqrt{4} = 2.$$

Dermed er

$$s = s(t) = \int_0^t 2 \, d\tau = 2t.$$

Løst fort får vi $t(s) = s/2$, og innsatt gir dette buelengdeparametriseringen

$$\mathbf{r}(s) = \left(\sin\left(\frac{s}{2}\right),\; \cos\left(\frac{s}{2}\right),\; \frac{\sqrt{3}}{2}s\right).$$

Krumningen til kurven $\mathcal{C}$ er gitt ved

$$\kappa(s) = \left|\frac{d\mathbf{T}}{ds}\right|, \quad \text{der } \mathbf{T} = \frac{d\mathbf{r}}{ds}.$$

Fra buelengdeparametriseringen får vi derfor at

$$\mathbf{T}(s) = \left(\frac{1}{2}\cos\left(\frac{s}{2}\right),\; -\frac{1}{2}\sin\left(\frac{s}{2}\right),\; \frac{\sqrt{3}}{2}\right),$$

og

$$\frac{d\mathbf{T}}{ds} = \left(-\frac{1}{4}\sin\left(\frac{s}{2}\right),\; -\frac{1}{4}\cos\left(\frac{s}{2}\right),\; 0\right).$$

Dermed blir krumningen

$$\kappa(s) = \left|\frac{d\mathbf{T}}{ds}\right| = \sqrt{\left(\frac{1}{4}\right)^2 \sin^2\left(\frac{s}{2}\right) + \left(\frac{1}{4}\right)^2 \cos^2\left(\frac{s}{2}\right)} = \frac{1}{4}.$$

Kildesett: course=TMA4105 term=var year=2022 problem=5 file=tma4105_2022v.pdf
