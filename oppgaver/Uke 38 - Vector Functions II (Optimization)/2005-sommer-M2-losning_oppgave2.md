### **Løsning til Oppgave 2**

**a)** Maksima og minima som ligger inne i området, er kritiske punkter, det vil si punkter hvor $\nabla f = 0$. Vi har

$$\nabla f(x, y) = \left[ (1 - 2x^2) e^{-x^2 - y^2}, \; -2xy \, e^{-x^2 - y^2} \right].$$

Kritiske punkter tilfredsstiller altså

$$1 - 2x^2 = 0, \qquad -2xy = 0,$$

og derfor

$$x = \pm \frac{1}{\sqrt{2}}, \quad y = 0.$$

Her må vi se på to tilfeller:

*Tilfelle 1: $R \le \frac{1}{\sqrt{2}}$.* Da finnes det ingen kritiske punkter i området, og maksima og minima ligger på randen. Vi parametriserer randen ved å skrive $[x, y] = [R \cos \theta, R \sin \theta]$, $\theta \in [0, 2\pi]$. På randen er $f$ lik $g(\theta) = R \cos \theta \, e^{-R^2}$. Vi får maksimum og minimum til $g$ når $\theta = 0$ og $\theta = \pi$. Maksimum og minimum er nådd i punktene $(R, 0)$ og $(-R, 0)$, og vi har

$$f_{\max} = R e^{-R^2}, \qquad f_{\min} = -R e^{-R^2}.$$

*Tilfelle 2: $R > \frac{1}{\sqrt{2}}$.* De to kritiske punktene $\left( \frac{1}{\sqrt{2}}, 0 \right)$ og $\left( -\frac{1}{\sqrt{2}}, 0 \right)$ ligger inne i området. De gir henholdsvis $f = \frac{1}{\sqrt{2}} e^{-1/2}$ og $f = -\frac{1}{\sqrt{2}} e^{-1/2}$. Vi må undersøke randen, og gjør det på samme måte som før: maksimum og minimum på randen finnes i punktene $(R, 0)$ og $(-R, 0)$. For å finne maksimum og minimum verdier, må vi sammenligne verdien til $f$ i disse punktene med den i de kritiske punktene. Vi merker at alle disse punktene ligger på den horisontale aksen, og derfor er det nok å betrakte restriksjonen til $f$ til $x$-aksen: $h(x) = x e^{-x^2}$. Vi har

$$h'(x) = (1 - 2x^2) e^{-x^2}.$$

Når $x > 1/\sqrt{2}$, er $h'(x) < 0$ og $h$ er en avtagende funksjon. Av dette følger at $h(R) < h\left( \frac{1}{\sqrt{2}} \right)$, og $f$ er derfor maksimal i punktet $\left( \frac{1}{\sqrt{2}}, 0 \right)$. På samme måte får vi at $f$ er minimal i punktet $\left( -\frac{1}{\sqrt{2}}, 0 \right)$, og

$$f_{\max} = \frac{1}{\sqrt{2}} e^{-1/2}, \qquad f_{\min} = -\frac{1}{\sqrt{2}} e^{-1/2}.$$

**b)** I dette tilfellet er maksimum og minimum til $f$ nådd enten i de kritiske punktene eller når $x, y$ går mot $\pm \infty$. Siden $\lim_{(x,y) \to \pm\infty} f(x, y) = 0$, tar funksjonen sine maksimale og minimale verdier henholdsvis i $\left( \frac{1}{\sqrt{2}}, 0 \right)$ og $\left( -\frac{1}{\sqrt{2}}, 0 \right)$, og

$$f_{\max} = \frac{1}{\sqrt{2}} e^{-1/2}, \qquad f_{\min} = -\frac{1}{\sqrt{2}} e^{-1/2}.$$

Kildesett: course=TMA4105 term=sommer year=2005 problem=2 file=tma4105_05k.pdf
