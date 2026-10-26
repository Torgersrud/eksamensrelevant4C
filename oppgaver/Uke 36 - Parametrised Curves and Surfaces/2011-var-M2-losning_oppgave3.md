### **Løsning til Oppgave 3**

En parameterfremstilling for kurven er gitt ved

$$\mathbf{r}(t) = t \, \mathbf{i} + t^2 \, \mathbf{j}, \quad t \in \mathbb{R}.$$

Det gir

$$\mathbf{v}(t) = \frac{d\mathbf{r}}{dt} = \mathbf{i} + 2t \, \mathbf{j},$$

slik at

$$\mathbf{T}(t) = \frac{1}{|\mathbf{v}(t)|} \, \mathbf{v}(t) = \frac{1}{\sqrt{1 + 4t^2}} (\mathbf{i} + 2t \, \mathbf{j}).$$

Gitt en vektor $\mathbf{u} = a \mathbf{i} + b \mathbf{j}$ i planet, så gjelder det at $\pm(-b \mathbf{i} + a \mathbf{j})$ står normalt på $\mathbf{u}$. Da enhetsnormalvektoren står normalt på enhetstangentvektoren (og skal peke mot den siden kurven krummer), har vi at

$$\mathbf{N}(t) = \frac{1}{\sqrt{1 + 4t^2}} (-2t \, \mathbf{i} + \mathbf{j}).$$

Krumningen til en kurve gitt ved $y = f(x)$ er gitt ved

$$\kappa(x) = \frac{|f''(x)|}{\left[1 + (f'(x))^2\right]^{3/2}}.$$

I vårt tilfelle gir det at

$$\kappa(x) = \frac{2}{(1 + 4x^2)^{3/2}}.$$

Vi er bedt om finne krumningen og enhetsnormalvektoren i punktet $(x, y) = (1, 1)$, som svarer til å sette $x = t = 1$. Det vil si,

$$\kappa(1) = \frac{2}{5^{3/2}}, \qquad \text{og} \qquad \mathbf{N}(1) = \frac{1}{\sqrt{5}} (-2 \mathbf{i} + \mathbf{j}).$$

Kildesett: course=TMA4105 term=var year=2011 problem=3 file=tma4105_11v.pdf
