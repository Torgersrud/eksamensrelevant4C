### **Løsning til Oppgave 8**

Utregning gir

$$\frac{\partial f}{\partial x} = (x - 2)\left[\frac{1}{\sqrt{(x - 2)^2 + (y - 1)^2}} - 2\right] \quad \text{og} \quad \frac{\partial f}{\partial y} = \frac{y - 1}{\sqrt{(x - 2)^2 + (y - 1)^2}}. \tag{1}$$

Merk at de partielle deriverte ikke er definert i punktet $(2, 1)$, så dette er et singulært punkt, og dermed ikke et kritisk punkt. I det videre antar vi at $(x, y) \neq (2, 1)$.

Vi får at $\partial f/\partial x = 0$ når $x = 2$ og når $\sqrt{(x - 2)^2 + (y - 1)^2} = \frac{1}{2}$, og $\partial f/\partial y = 0$ når $y = 1$. Kritiske punkter (begge de partielle deriverte lik 0) får vi da når $(x - 2)^2 = \frac{1}{4}$ og $y = 1$, dvs. i punktene $\left(\frac{5}{2}, 1\right)$ og $\left(\frac{3}{2}, 1\right)$. Utregning gir $f\left(\frac{5}{2}, 1\right) = f\left(\frac{3}{2}, 1\right) = \frac{17}{4}$.

For å bestemme maksimums- og minimumsverdier må vi ta hensyn både til de kritiske punktene og til det singulære punktet. I tillegg må vi undersøke randa til $D$. På randa til $D$ er $(x - 2)^2 + (y - 1)^2 = 1$, så her kan $f(x, y)$ skrives

$$f(x, y) = 1 + 4x - x^2 := g(x).$$

$g(x)$ har sin største verdi når $x = 2$ og sin minste verdi når $x = 1$ eller $x = 3$. Dermed får vi at største verdi på randa blir $f(2, 2) = f(2, 0) = 5$, og at minste verdi blir $f(1, 1) = f(3, 1) = 4$. Utregning av $f$ i det singulære punktet gir $f(2, 1) = 4$.

Ved å sammenligne funksjonsverdiene vi har fått i alle de aktuelle punktene får vi:

* Den absolutte maksimumsverdien for $f$ i $D$ er $5$ og den antas i punktene $(2, 2)$ og $(2, 0)$.
* Den absolutte minimumsverdien for $f$ i $D$ er $4$ og den antas i punktene $(1, 1)$, $(3, 1)$ og $(2, 1)$.

Kildesett: course=TMA4105 term=var year=2020 problem=8 file=tma4105_2020v.pdf
