### **Løsning til Oppgave 2**

I vårt tilfelle er

$$\nabla f(x, y) = \frac{1}{(x^2 + y^2 + 4)^2}(-2xy, \; x^2 - y^2 + 4).$$

Observer at $x^2 + y^2 + 4 > 0$ for alle $(x, y) \in \mathbb{R}^2$. Altså har vi ingen singulære punkter. De kritiske punktene må tilfredstille

$$-2xy = 0 \tag{1}$$
$$x^2 - y^2 + 4 = 0. \tag{2}$$

Fra (1) får vi at $x = 0$ eller $y = 0$. Setter vi inn for $y = 0$ i (2) får vi at $x^2 + 4 = 0$, som har ingen løsning. Altså kan ikke $y = 0$. Setter vi inn for $x = 0$ i (2) får vi at $y^2 - 4 = 0$, det vil si, $y = \pm 2$. Punktene $(0, \pm 2)$ ligger på randen, og vi har dermed ingen kritiske punkter i det indre av definisjonsmengden til $f$.

På randen er $x^2 + y^2 = 4$, slik at

$$f(x, y) = \frac{y}{x^2 + y^2 + 4} = \frac{y}{8}.$$

La så $g(y) = y/8$, der $-2 \le y \le 2$. Da $g$ er kontinuerlig og definert på et lukket intervall, gir ekstremalverdisetningen at $g$ må oppnå en største og en minste verdi på intervallet $[-2, 2]$. Observer at $g$ har ingen kritiske eller singulære punkter. De eneste kandidatene til største og minste verdi er dermed endepunktene, altså $y = -2$ og $y = 2$. Observer at $g(\pm 2) = \pm 1/4$.

Dermed er $1/4$ den største verdien og $-1/4$ den minste verdien $f$ oppnår på sirkelskiven $x^2 + y^2 \le 4$.

Kildesett: course=TMA4105 term=var year=2016 problem=2 file=tma4105_2016v.pdf
