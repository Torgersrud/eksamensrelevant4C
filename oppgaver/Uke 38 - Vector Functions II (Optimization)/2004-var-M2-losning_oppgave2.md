### **Løsning til Oppgave 2**

Partiell derivasjon med produkt- og kjerneregel gir

$$f_x = e^{-(x^2 + y^2)/2} + x e^{-(x^2 + y^2)/2}(-x) = (1 - x^2) e^{-(x^2 + y^2)/2}, \qquad f_y = -xy \, e^{-(x^2 + y^2)/2}.$$

For å finne de kritiske punktene løser vi ligningssettet $\{f_x = 0, f_y = 0\}$. Faktoren $e^{-(x^2 + y^2)/2}$ kan strykes, siden den alltid er positiv, så vi får

$$1 - x^2 = 0 \quad \text{og} \quad xy = 0.$$

Den første ligningen gir $x^2 = 1$ og derfor $x = \pm 1$. Den andre ligningen gir da $y = 0$. Altså er det to kritiske punkter: $(1, 0)$ og $(-1, 0)$.

Vi bruker annenderiverttesten med $\Delta = f_{xx} f_{yy} - f_{xy}^2$ for å klassifisere disse punktene. Derivasjon gir

$$f_{xx} = \left[ -2x + (1 - x^2)(-x) \right] e^{-(x^2 + y^2)/2} = x (x^2 - 3) e^{-(x^2 + y^2)/2},$$

$$f_{xy} = (1 - x^2)(-y) e^{-(x^2 + y^2)/2} = y (x^2 - 1) e^{-(x^2 + y^2)/2},$$

$$f_{yy} = \left[ -x - xy(-y) \right] e^{-(x^2 + y^2)/2} = x (y^2 - 1) e^{-(x^2 + y^2)/2}.$$

I punktet $(1, 0)$ har vi da

$$f_{xx}(1, 0) = -2 e^{-1/2}, \qquad f_{xy}(1, 0) = 0, \qquad f_{yy}(1, 0) = -e^{-1/2},$$

og derfor $\Delta = 2 e^{-1} > 0$. Dessuten er $f_{xx}(1, 0) < 0$, så $(1, 0)$ er et **lokalt maksimumspunkt**.

I punktet $(-1, 0)$ har vi

$$f_{xx}(-1, 0) = 2 e^{-1/2}, \qquad f_{xy}(-1, 0) = 0, \qquad f_{yy}(-1, 0) = e^{-1/2},$$

og derfor $\Delta = 2 e^{-1} > 0$. Dessuten er $f_{xx}(-1, 0) > 0$, så $(-1, 0)$ er et **lokalt minimumspunkt**.

Svaret på det siste spørsmålet er **ja**; punktet $(1, 0)$ er et absolutt maksimumspunkt, og $(-1, 0)$ er et absolutt minimumspunkt. Begrunnelsen er som følger. Merk at

$$f(\pm 1, 0) = \pm e^{-1/2}.$$

Det vi må vise, er derfor at

$$(*) \qquad -e^{-1/2} \le f(x, y) \le e^{-1/2} \quad \text{for alle } x \text{ og } y.$$

Men $f(x, y) \to 0$ når $|(x, y)| \to +\infty$. Ved å velge $R$ tilstrekkelig stor, kan vi derfor garantere at

$$(**) \qquad |f(x, y)| < e^{-1/2} \quad \text{når } |(x, y)| \ge R,$$

og da er selvsagt $(*)$ tilfredsstilt for $|(x, y)| \ge R$.

Det gjenstår da kun å vise at $(*)$ er oppfylt når $|(x, y)| < R$. Men siden $f$ er kontinuerlig, vet vi fra en setning i boka at i den lukkede sirkeldisken $D_R$ gitt ved $x^2 + y^2 \le R^2$ har $f$ absolutte ekstremalpunkter; pga. $(**)$ må disse punktene ligge i det indre av $D_R$, og de må følgelig være kritiske punkter for $f$. Disse punktene kan derfor ikke være noe annet enn $(\pm 1, 0)$, og det følger da at $(*)$ er oppfylt også for $|(x, y)| < R$.

Til slutt, begrunnelsen av at $f(x, y) \to 0$ når $|(x, y)| \to +\infty$: i polarkoordinater $x = r \cos \theta$, $y = r \sin \theta$ (med $r \ge 0$) har vi

$$|f(x, y)| = |(r \cos \theta) e^{-r^2/2}| \le r e^{-r^2/2},$$

og fra L'Hôpitals regel ser vi at $r e^{-r^2/2} \to 0$ når $r \to +\infty$.

Kildesett: course=TMA4105 term=var year=2004 problem=2 file=tma4105_04v.pdf
