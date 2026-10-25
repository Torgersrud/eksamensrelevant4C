### **Oppgave 3**

Funksjonene $f$ og $g$ er definert ved

$$f(x) = \begin{cases} e^{-x} & \text{for} \quad x > 0, \\ e^{x} & \text{for} \quad x < 0, \end{cases} \qquad \text{og} \qquad g(x) = \begin{cases} (x+1)e^{-x} & \text{for} \quad x > 0, \\ (-x+1)e^{x} & \text{for} \quad x < 0. \end{cases}$$

Det oppgis at Fouriertransformene er

$$\hat{f}(w) = \frac{1}{\sqrt{2\pi}} \frac{2}{1 + w^2} \qquad \text{og} \qquad \hat{g}(w) = \frac{1}{\sqrt{2\pi}} \frac{4}{(1 + w^2)^2}.$$

a) Tegn skisse av grafene til $f$ og $g$, og bruk Fourier-inversjon til å finne verdiene av

$$\int_{-\infty}^{\infty} \frac{\sin w}{(1 + w^2)^2} \, dw, \quad \int_{-\infty}^{\infty} \frac{1}{(1 + w^2)^2} \, dw \quad \text{og} \quad \int_{-\infty}^{\infty} \frac{\cos^2 w}{(1 + w^2)^2} \, dw.$$

Hint: $\cos 2w = 2\cos^2 w - 1$.

b) Finn et eksplisitt uttrykk for konvolusjonsintegralet

$$h(x) = \int_{-\infty}^{\infty} e^{-|v|} e^{-|x-v|} \, dv = (f * f)(x).$$

Kildesett: course=TMA4135 term=host year=2008 problem=3 file=tma4135_08h.pdf
