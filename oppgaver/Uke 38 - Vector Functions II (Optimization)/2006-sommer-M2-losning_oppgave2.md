### **Løsning til Oppgave 2**

**a)** De kritiske punktene $(x, y)$ for $f$ er løsningene av ligningssystemet

$$(1) \quad f_x(x, y) = (2xy - 4x)e^{-y} = 0$$

$$(2) \quad f_y(x, y) = (x^2 - 1)e^{-y} - (x^2 y - 2x^2 - y + 2)e^{-y} = 0.$$

Siden $e^{-y} \neq 0$ for alle $y$, kan vi dividere ligningene med $e^{-y}$:

$$(1) \quad 2xy - 4x = 0, \qquad (2) \quad x^2 - 1 - x^2 y + 2x^2 + y - 2 = 0.$$

Av (1) følger det at $x = 0$ eller $y = 2$. Vi sjekker tilfellet $x = 0$ først. Innsatt i (2) gir det $-1 + y - 2 = 0$, altså $y = 3$. Punktet $(0, 3)$ er derfor et kritisk punkt. Vi sjekker så tilfellet $y = 2$. Innsatt i (2) gir det

$$x^2 - 1 - 2x^2 + 2x^2 + 2 - 2 = x^2 - 1 = 0 \implies x = \pm 1.$$

Punktene $(1, 2)$ og $(-1, 2)$ er derfor også kritiske, og det finnes ikke flere kritiske punkter enn disse tre.

For klassifisering av et kritisk punkt ved andrederiverttesten trenger vi

$$f_{xx}(x, y) = (2y - 4)e^{-y},$$

$$f_{yy}(x, y) = -(x^2 - 1)e^{-y} - (x^2 - 1)e^{-y} + (x^2 y - 2x^2 - y + 2)e^{-y},$$

$$f_{xy}(x, y) = 2x e^{-y} - (2xy - 4x)e^{-y}.$$

Vi sjekker for eksempel det kritiske punktet $(1, 2)$. Siden

$$f_{xx}(1, 2) f_{yy}(1, 2) - f_{xy}(1, 2)^2 = -f_{xy}(1, 2)^2 < 0$$

(merket at $f_{xx}(1, 2) = (2 \cdot 2 - 4)e^{-2} = 0$ mens $f_{xy}(1, 2) = 2e^{-2} \neq 0$), er dette et sadelpunkt.

**b)** En kontinuerlig funksjon oppnår alltid sitt maksimum og minimum på et lukket område. Og $f(x, y)$ er en kontinuerlig funksjon for alle $x$ og $y$, og da spesielt på det lukkede området $-1 \le x \le 1$, $0 \le y \le 100$.

Vi har funnet de kritiske punktene $(0, 3)$, $(1, 2)$ og $(-1, 2)$ som alle ligger i $R$. Der er funksjonsverdiene

$$f(0, 3) = -e^{-3}, \qquad f(1, 2) = 0, \qquad f(-1, 2) = 0.$$

Siden $f(x, y) \to 0$ når $y \to \infty$ (leddet $(x^2 - 1)(y - 2)e^{-y}$ går mot null), vil verken maksimum eller minimum ligge på den øvre kuttekanten $y = 100$ eller utenfor den; dermed oppnår $f(x, y)$ både maksimum og minimum i $R$.

Det gjenstår å sjekke randen. Langs $y$-aksen, dvs. $y = 0$, er $f(x, 0) = -2x^2 + 2$ med maksimum i $x = 0$ og minimum i $(\pm 1, 0)$, med $f(0, 0) = 2$ og $f(\pm 1, 0) = 0$. Langs de to linjene $x = 1$ og $x = -1$ er $f(\pm 1, y) = 0$.

Konklusjon: Absolutt maksimum $2$ ligger i $(0, 0)$ og absolutt minimum $-e^{-3}$ ligger i $(0, 3)$.

Kildesett: course=TMA4105 term=sommer year=2006 problem=2 file=tma4105_06k.pdf
