### **Løsning til Oppgave 3**

Siden $f(x, y)$ er et polynom, har funksjonen ingen singulære punkter. Ekstremalpunktene må derfor være enten kritiske punkter eller punkter på randen av $D$. Vi har

$$\frac{\partial f}{\partial x} = 2x(2 - y),$$

$$\frac{\partial f}{\partial y} = 2y(2 - y) + (x^2 + y^2)(-1) = 4y - 2y^2 - x^2 - y^2 = 4y - 3y^2 - x^2.$$

Vi ser at for å få $\frac{\partial f}{\partial x} = 0$ må vi ha enten $x = 0$ eller $y = 2$. Hvis $x = 0$ får vi

$$\frac{\partial f}{\partial y} = 4y - 3y^2 = y(4 - 3y)$$

som er 0 når $y = 0$ eller $y = \frac{4}{3}$. Hvis $y = 2$ får vi

$$\frac{\partial f}{\partial y} = 8 - 12 - x^2 = -4 - x^2$$

som ikke er 0 for noen $x \in \mathbb{R}$.

De kritiske punktene til $f$ er dermed $(0, 0)$ og $\left(0, \frac{4}{3}\right)$ med verdier

$$f(0, 0) = 0, \quad f\left(0, \frac{4}{3}\right) = \frac{32}{27}.$$

Randen til $D$ er sirkelen gitt ved $x^2 + y^2 = 4$, som vi kan parametrisere ved $(x, y) = (2\cos t, 2\sin t)$ for $0 \leq t \leq 2\pi$. Da får vi

$$f(2\cos t, 2\sin t) = 4(2 - 2\sin t).$$

Siden $-1 \leq \sin t \leq 1$ der begge endepunktene oppnås, får vi at maksimumsverdien på randen er $4(2 - 2 \cdot (-1)) = 16$ som oppnås når

$$\sin t = -1 \quad \Longleftrightarrow \quad t = 3\pi/2 \quad \Longleftrightarrow \quad (x, y) = (0, -2),$$

mens minimumsverdien er $4(2 - 2) = 0$ som oppnås når

$$\sin t = 1 \quad \Longleftrightarrow \quad t = \pi/2 \quad \Longleftrightarrow \quad (x, y) = (0, 2).$$

Siden $16 > \frac{32}{27}$ får vi at

* minimumsverdien er $0$ og oppnås i punktene $(0, 0)$ og $(0, 2)$,
* maksimumsverdien er $16$ og oppnås i punktet $(0, -2)$.

Kildesett: course=TMA4105 term=var year=2021 problem=3 file=tma4105_2021v.pdf
