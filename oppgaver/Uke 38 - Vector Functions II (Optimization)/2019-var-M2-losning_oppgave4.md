### **Løsning til Oppgave 4**

Vi bruker Lagranges multiplikatormetode for å finne kandidater for største og minste verdi av $f(x, y) = 4x^2 y$ på sirkelen $x^2 + y^2 = 3$. Lagrangefunksjonen

$$L(x, y, \lambda) = f(x, y) + \lambda(x^2 + y^2 - 3) = 4x^2 y + \lambda(x^2 + y^2 - 3)$$

har kritiske punkter der $\nabla L(x, y, \lambda) = (0, 0, 0)$. I vårt tilfelle er

$$\nabla L(x, y, \lambda) = \left(\frac{\partial L}{\partial x}(x, y, \lambda), \; \frac{\partial L}{\partial y}(x, y, \lambda), \; \frac{\partial L}{\partial \lambda}(x, y, \lambda)\right) = (8xy + 2\lambda x, \; 4x^2 + 2\lambda y, \; x^2 + y^2 - 3),$$

slik at $\nabla L(x, y, \lambda) = (0, 0, 0)$ gir ligningene

$$x(4y + \lambda) = 0 \tag{1}$$
$$2x^2 + \lambda y = 0 \tag{2}$$
$$x^2 + y^2 - 3 = 0. \tag{3}$$

Fra (1) vet vi at $x = 0$ eller $\lambda = -4y$. Innsatt for $x = 0$ i (3) får vi at $y = \pm\sqrt{3}$. Innsatt for $\lambda = -4y$ i (2) får vi at $2x^2 - 4y^2 = 0$, det vil si, $x^2 = 2y^2$. Setter vi inn for $x^2 = 2y^2$ i (3) får vi at $3y^2 - 3 = 0$ som har løsning $y = \pm 1$, og som igjen gir at $x = \pm\sqrt{2}$.

Kandidatene til største og minste verdi av $f(x, y)$ er dermed

$$f(0, \pm\sqrt{3}) = 0, \qquad f(\pm\sqrt{2}, -1) = -8 \quad \text{og} \quad f(\pm\sqrt{2}, 1) = 8.$$

Siden $f$ er en kontinuerlig funksjon og kurven $x^2 + y^2 = 3$ er en lukket og begrenset mengde, må $f$ oppnå en største og minste verdi blant punktene vi har funnet. Det vil si, den minste verdien av $f(x, y)$ er $-8$ og den største verdien av $f(x, y)$ er $8$.

Kildesett: course=TMA4105 term=var year=2019 problem=4 file=tma4105_2019v.pdf
