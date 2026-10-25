### **Løsning til Oppgave 3**

a)

[Figur: Grafen til $f$: glatt klokkeformet kurve med topp $1$ ved $x = 0$, avtakande mot $0$ som $e^{-|x|}$ på begge sider.]

[Figur: Grafen til $g$: glatt, symmetrisk, positiv klokkeformet kurve med topp $1$ ved $x = 0$, som går mot $0$ når $x \to \pm\infty$.]

Fourierinversjon gir oss $f$ og $g$ tilbake

$$f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{2}{1 + w^2} e^{ixw} \, dw, \qquad g(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{4}{(1 + w^2)^2} e^{ixw} \, dw.$$

Sidon $f$ og $g$, og derfor også $\hat{f}$ og $\hat{g}$ er likefunksjoner forsvinner sinusdelen og vi har

$$f(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{2}{1 + w^2} \cos xw \, dw, \qquad g(x) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{4}{(1 + w^2)^2} \cos xw \, dw.$$

$$\int_{-\infty}^{\infty} \frac{\sin w}{(1 + w^2)^2} \, dw = 0, \quad \text{fordi integranden er odde.}$$

$$\int_{-\infty}^{\infty} \frac{1}{(1 + w^2)^2} \, dw = \frac{2\pi}{4} g(0) = \frac{\pi}{2}.$$

$$\int_{-\infty}^{\infty} \frac{\cos^2 w}{(1 + w^2)^2} \, dw = \int_{-\infty}^{\infty} \frac{\frac{1}{2} + \frac{1}{2}\cos 2w}{(1 + w^2)^2} \, dw = \frac{2\pi}{8} (g(0) + g(2)) = \frac{\pi}{4} (1 + 3e^{-2}).$$

b)

$$\int_{-\infty}^{\infty} e^{-|v|} e^{-|x - v|} \, dv = (f * f)(x).$$

Tar vi Fouriertransformeren ser vi at

$$\mathcal{F}(f * f)(w) = \sqrt{2\pi} \left( \frac{1}{\sqrt{2\pi}} \frac{2}{1 + w^2} \right)^2 = \hat{g}(w), \qquad \text{og følgelig er } (f * f)(x) = g(x).$$

Kildesett: course=TMA4135 term=host year=2008 problem=3 file=tma4135_08h.pdf
