### **Løsning til Oppgåve 2**

**a)** De kritiske punktene til $f$ er de punktene der de partiell-deriverte er 0. Vi løser likningene $f_x(x, y) = 0$ og $f_y(x, y) = 0$ og får

$$f_x = \frac{1 + x^2 + y^2 - x \cdot 2x}{(1 + x^2 + y^2)^2} = \frac{1 - x^2 + y^2}{(1 + x^2 + y^2)^2} = 0$$

$$f_y = \frac{-2xy}{(1 + x^2 + y^2)^2} = 0.$$

Den andre likninga impliserer $x = 0$ eller $y = 0$. Setter vi inn $x = 0$ i den første likninga gir får vi $1 + y^2 = 0$ som er umulig, og setter vi inn $y = 0$ får vi $1 - x^2 = 0$, det vil si $x = \pm 1$. Vi har to kritiske punkter, $(x, y) = (-1, 0)$ og $(x, y) = (1, 0)$.

På randa er $f(x, y) = \frac{x}{1 + 9} = \frac{x}{10}$, som har minste verdi når $x = -3$ og største verdi når $x = 3$. Verdiene er da henholdsvis lik $-\frac{3}{10}$ og $\frac{3}{10}$.

For å finne minimum og maksimum må vi sjekke 4 punkter, $(x, y) = (-1, 0)$, $(x, y) = (1, 0)$, $(x, y) = (-3, 0)$ og $(x, y) = (3, 0)$. Ved innsetting ser vi at $f(-1, 0) = -\frac{1}{2}$ er minimum og $f(1, 0) = \frac{1}{2}$ er maksimum, siden $f(\pm 3, 0) = \pm \frac{1}{10}$.

**b)** På randa til $A_r$ er $f(x, y) = \frac{x}{1 + r^2}$, så $f(x, y)$ har minste verdi når $x = -r$ og største verdi når $x = r$.

For hver $r$ må vi sjekke punktene $(\pm r, 0)$ og, hvis $r > 1$, de indre kritiske punktene $(\pm 1, 0)$. Siden $f(r, 0) > f(-r, 0)$ er $f(r, 0) = \frac{r}{1 + r^2}$ maksimum for alle $r \le 1$, og $f(-r, 0) = -\frac{r}{1 + r^2}$ minimum for alle $r \le 1$.

La $h(x) = f(x, 0) = \frac{x}{1 + x^2}$. Da er $h'(x) = f_x(x, 0) = \frac{1 - x^2}{(1 + x^2)^2}$. For $|x| \ge 1$ er $h'(x) < 0$, så $h$ er synkende der.

Siden $h(x)$ er synkende for $|x| > 1$ vet vi at $f(r, 0) < f(1, 0)$ og $f(-r, 0) > f(-1, 0)$ for alle $r > 1$. Vi ser også at $f(-r, 0) < 0 < f(r, 0)$ for alle $r > 0$. Dette gir $f(-1, 0) < f(-r, 0) < 0 < f(r, 0) < f(1, 0)$ for alle $r > 1$, så $(1, 0)$ og $(-1, 0)$ er absolutt maksimums- og minimumspunkt i $A_r$ for alle $r > 1$.

Siden ethvert punkt $(x, y)$ i $\mathbb{R}^2$ ligger inne i en $A_r$ for en tilstrekkelig stor $r$, må $f(x, y) \le f(1, 0)$ for alle punkter $(x, y)$ (tilsvarende $f(x, y) \ge f(-1, 0)$) og derved har $f$ absolutt minimum i $f(-1, 0) = -\frac{1}{2}$ og maksimum i $f(1, 0) = \frac{1}{2}$.

Kildesett: course=TMA4105 term=var year=2007 problem=2 file=tma4105_07v.pdf
