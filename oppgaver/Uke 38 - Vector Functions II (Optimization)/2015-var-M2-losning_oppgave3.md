### **Løsning til Oppgave 3**

Vi partiellderiverer og forenkler:

$$\frac{\partial f}{\partial x} = -6x\,\frac{2 + x^2 + y^2}{1 + x^2 + y^2}, \qquad \frac{\partial f}{\partial y} = 2y\,\frac{x^2 + y^2 - 2}{1 + x^2 + y^2}.$$

Vi ser at $\partial f/\partial x = 0$ bare for $x = 0$, og da blir $\partial f/\partial y = 0$ for $y = 0$ og $y = \pm\sqrt{2}$. Det eneste kritiske punktet for $f$ innenfor $D$ er $(x, y) = (0, 0)$, med tilhørende funksjonsverdi $f(0, 0) = 5$.

Vi må også søke ekstremverdier for $f$ på randkurven $x^2 + y^2 = 1$.

Det enkleste er å sette inn $y^2 = 1 - x^2$, og få at $f(x, y) = 6 - 4x^2 - 3\ln 2$ når $x^2 + y^2 = 1$. Ekstremverdiene for $-1 \le x \le 1$ er i $x = 0$ og $x = \pm 1$, som gir løsningene $(x, y) = (\pm 1, 0)$ og $(x, y) = (0, \pm 1)$, med tilhørende funksjonsverdier $f(\pm 1, 0) = 2 - 3\ln 2 \approx -0{,}08$ og $f(0, \pm 1) = 6 - 3\ln 2 \approx 3{,}92$.

Funksjonen har maksimumsverdi $f(0, 0) = 5$ og minimumsverdi $f(\pm 1, 0) = 2 - 3\ln 2$.

Alternativt kan man bruke Lagranges metode. Regningen blir litt enklere om vi benytter at $f(x, y) = 5 - 3x^2 + y^2 - 3\ln 2$ når $x^2 + y^2 = 1$. Alle ekstrempunkter til denne funksjonen på randkurven er kritiske punkter til Lagrangefunksjonen $L$ gitt ved

$$L(x, y, \lambda) = 5 - 3x^2 + y^2 - 3\ln 2 + \lambda(x^2 + y^2 - 1).$$

Vi finner

$$\frac{\partial L}{\partial x} = -6x + 2\lambda x = 2x(\lambda - 3), \qquad \frac{\partial L}{\partial y} = 2y + 2\lambda y = 2y(\lambda + 1), \qquad \frac{\partial L}{\partial \lambda} = x^2 + y^2 - 1,$$

så kritiske punkter for $L$ er gitt ved $2x(\lambda - 3) = 0$, $2y(\lambda + 1) = 0$ og $x^2 + y^2 = 1$. Siden $\lambda - 3$ og $\lambda + 1$ ikke kan være null samtidig, må enten $x = 0$ eller $y = 0$. Løsningen avsluttes på samme måte som før.

Kildesett: course=TMA4105 term=var year=2015 problem=3 file=tma4105_15v.pdf
