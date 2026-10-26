### **Løsning til Oppgave 3**

For lagrangefunksjonen $L(x, y, \lambda) = f(x, y) + \lambda(x^3 + y^3 - 16)$ får vi at

$$\nabla L(x, y, \lambda) = \left(ye^{xy} + 3\lambda x^2, \; xe^{xy} + 3\lambda y^2, \; x^3 + y^3 - 16\right) = (0, 0, 0)$$

som gir ligningene

$$ye^{xy} + 3\lambda x^2 = 0 \tag{1}$$
$$xe^{xy} + 3\lambda y^2 = 0 \tag{2}$$
$$x^3 + y^3 - 16 = 0. \tag{3}$$

Ved å gange ligning (1) med $x$ og gange ligning (2) med $y$ får vi

$$xye^{xy} + 3\lambda x^3 = 0 \tag{1'}$$
$$xye^{xy} + 3\lambda y^3 = 0. \tag{2'}$$

Ved å ta differansen mellom ligning (1') og ligning (2') får vi at

$$3\lambda(x^3 - y^3) = 3\lambda(2x^3 - 16) = 6\lambda(x^3 - 8) = 0,$$

der vi har utnyttet at $y^3 = 16 - x^3$ (fra ligning (3)). Altså er enten $\lambda = 0$ eller $x = 2$. I tilfellet $\lambda = 0$ må $y = 0$ og $x = 0$ fra henholdsvis ligning (1) og (2). Men ligning (3) er ikke tilfredsstilt for $x = y = 0$, og altså må $\lambda \neq 0$.

Dermed står vi igjen med at $x = 2$, som innsatt i ligning (3) gir at $y = 2$, og hvor $f(2, 2) = e^4$.

Endepunktene til kurven $x^3 + y^3 = 16$ i 1. kvadrant er gitt ved $(2\sqrt[3]{2}, 0)$ og $(0, 2\sqrt[3]{2})$, der $f(2\sqrt[3]{2}, 0) = f(0, 2\sqrt[3]{2}) = e^0 = 1$.

Siden $f(2, 2) > f(2\sqrt[3]{2}, 0) = f(0, 2\sqrt[3]{2})$ er den største verdien til $f(x, y) = e^{xy}$ på kurven $x^3 + y^3 = 16$, der $(x, y)$ ligger i 1. kvadrant, gitt ved $f(2, 2) = e^4$.

Kildesett: course=TMA4105 term=sommer year=2018 problem=3 file=tma4105_2018k.pdf
