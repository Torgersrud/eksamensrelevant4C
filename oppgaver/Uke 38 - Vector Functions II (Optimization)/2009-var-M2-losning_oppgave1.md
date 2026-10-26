### **Løsning til Oppgave 1**

a) Vi regner ut

$$f_x = \frac{1}{1 + x^2 + y^2} - \frac{x \cdot 2x}{(1 + x^2 + y^2)^2} = \frac{1 + x^2 + y^2 - 2x^2}{(1 + x^2 + y^2)^2} = \frac{1 - x^2 + y^2}{(1 + x^2 + y^2)^2},$$

$$f_y = \frac{x \cdot 2y}{(1 + x^2 + y^2)^2},$$

og løser $f_x = 0$, $f_y = 0$, dvs.

$$1 - x^2 + y^2 = 0 \quad (1), \qquad xy = 0 \quad (2).$$

Den siste ligningen gir $x = 0$ eller $y = 0$. Men $x = 0$ er umulig, siden (1) blir $1 + y^2 = 0$. Vi må derfor ha $y = 0$, og da sier (1) at $x^2 = 1$. Altså:

$$\text{De kritiske punktene er } (-1, 0) \text{ og } (1, 0).$$

b) $R$ inneholder ingen av de kritiske punktene, så maksimumspunktet må ligge på randen. Randen består av fire rette linjestykker som vi sjekker hver for seg:

* Linjestykket $y = 0$, $0 \le x \le \frac{1}{2}$. Da er funksjonsverdien $g(x) = f(x, 0) = \frac{x}{1 + x^2}$, som har kritiske punkter i $x = \pm 1$ (der $g'(x) = 0$), men disse ligger ikke i intervallet $0 \le x \le 1/2$, så vi står igjen med endepunktene $x = 0$ og $x = 1/2$, der vi har verdiene $g(0) = 0$ og $g(1/2) = 2/5$. Så vi tar kun med oss verdien $2/5$ som mulig kandidat til maksimumsverdi.
* Linjestykket $y = 2$, $0 \le x \le \frac{1}{2}$. Da er funksjonsverdien $h(x) = f(x, 2) = \frac{x}{5 + x^2}$, men denne er mindre enn $g(x)$ for $0 \le x \le 1/2$.
* Linjestykket $x = 0$, $0 \le y \le 2$. Da er funksjonsverdien $f(0, y) = 0$.
* Linjestykket $x = 1/2$, $0 \le y \le 2$. Da er funksjonsverdien $k(y) = f(1/2, y) = \frac{1/2}{5/4 + y^2}$, som har maksimumsverdi $2/5$ i $y = 0$.

Altså:

$$\text{Maksimumsverdien er } 2/5.$$

*Kjeldevarsel: løsningsforslaget trykkjer $f_y = \frac{x \cdot 2y}{(1 + x^2 + y^2)^2}$ utan minusteikn; korrekt derivert er $f_y = -\frac{x \cdot 2y}{(1 + x^2 + y^2)^2}$ (brøkregel). Feilen endrar ikkje svaret, sidan $f_y = 0$ gir $xy = 0$ uansett forteikn.*

Kildesett: course=TMA4105 term=var year=2009 problem=1 file=tma4105_09v.pdf
