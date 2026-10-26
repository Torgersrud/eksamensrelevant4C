### **Løsning til Oppgave 1**

Vi bruker Lagranges multiplikatormetode for å finne kandidater for største og minste verdi av $f(x, y) = xy$ på ellipsen $x^2/2 + y^2 = 1$. Lagrangefunksjonen

$$L(x, y, \lambda) = f(x, y) - \lambda\left(\frac{1}{2}x^2 + y^2 - 1\right) = xy - \lambda\left(\frac{1}{2}x^2 + y^2 - 1\right)$$

har kritiske punkter der $\nabla L(x, y, \lambda) = (0, 0, 0)$. I vårt tilfelle er

$$\nabla L(x, y, \lambda) = \left(\frac{\partial L}{\partial x}(x, y, \lambda), \frac{\partial L}{\partial y}(x, y, \lambda), \frac{\partial L}{\partial \lambda}(x, y, \lambda)\right) = \left(y - \lambda x,\; x - 2\lambda y,\; \frac{1}{2}x^2 + y^2 - 1\right),$$

slik at $\nabla L(x, y, \lambda) = (0, 0, 0)$ gir ligningene

$$y - \lambda x = 0 \tag{1}$$
$$x - 2\lambda y = 0 \tag{2}$$
$$\frac{1}{2}x^2 + y^2 = 1. \tag{3}$$

Fra (1) får vi $y = \lambda x$, som innsatt i (2) gir

$$x - 2\lambda^2 x = x(1 - 2\lambda^2) = 0.$$

Altså må vi ha $x = 0$ eller $\lambda = \pm 1/\sqrt{2}$. Hvis $x = 0$, har vi fra (3) at $y = \pm 1$. Punktene $(0, \pm 1)$ oppfyller imidlertid ikke (1). Hvis $\lambda = \pm 1/\sqrt{2}$, så er $y = \pm x/\sqrt{2}$, og innsatt i (3) gir dette $x = \pm 1$.

Kandidatene for største og minste verdi av $f$ er dermed

$$f\left(1, \frac{1}{\sqrt{2}}\right) = f\left(-1, -\frac{1}{\sqrt{2}}\right) = \frac{1}{\sqrt{2}}, \qquad f\left(-1, \frac{1}{\sqrt{2}}\right) = f\left(1, -\frac{1}{\sqrt{2}}\right) = -\frac{1}{\sqrt{2}}.$$

Siden $f$ er en kontinuerlig funksjon og kurven $x^2/2 + y^2 = 1$ er en lukket og begrenset mengde, må $f$ oppnå en største og minste verdi blant punktene vi har funnet. Det vil si at den minste verdien av $f$ er $-1/\sqrt{2}$ og den største verdien av $f$ er $1/\sqrt{2}$.

Oppgaven kan også løses uten bruk av Lagranges multiplikatormetode. Ellipsen $x^2/2 + y^2 = 1$ er gitt ved parametriseringen

$$\mathbf{r}(t) = \left(\sqrt{2}\cos t, \sin t\right), \quad -\pi \leq t < \pi,$$

og innsatt i $f$ får vi

$$f(x, y) = f\left(\sqrt{2}\cos t, \sin t\right) = \sqrt{2}\sin t\cos t = \frac{1}{\sqrt{2}}\sin 2t.$$

Funksjonen $g(t) = \sin 2t/\sqrt{2}$ har sine ekstremalverdier der

$$g'(t) = \sqrt{2}\cos 2t = 0 \quad \Longrightarrow \quad t = \pm\frac{\pi}{4}, \quad t = \pm\frac{3\pi}{4}.$$

Innsatt i $g$ finner vi igjen at

$$g\left(\frac{\pi}{4}\right) = g\left(-\frac{3\pi}{4}\right) = \frac{1}{\sqrt{2}} \quad \text{og} \quad g\left(-\frac{\pi}{4}\right) = g\left(\frac{3\pi}{4}\right) = -\frac{1}{\sqrt{2}}.$$

Kildesett: course=TMA4105 term=var year=2022 problem=1 file=tma4105_2022v.pdf
