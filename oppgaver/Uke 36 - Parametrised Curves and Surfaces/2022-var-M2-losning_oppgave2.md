### **Løsning til Oppgave 2**

La $f(x, y, z) = x^2 + 2y^2 + z^2$. Vi har

$$\nabla f(x, y, z) = (2x, 4y, 2z),$$

og tangentplanet til ellipsoiden $f(x, y, z) = 1$ i punktet $(a, b, c)$ har normalvektor

$$\nabla f(a, b, c) = (2a, 4b, 2c).$$

Altså er tangentplanet gitt ved ligningen

$$2a(x - a) + 4b(y - b) + 2c(z - c) = 0 \quad \text{eller} \quad ax + 2by + cz = a^2 + 2b^2 + c^2 = 1.$$

Vi skal så finne alle punkter på ellipsoiden hvor tangentplanet er parallelt med planet $x + y + z = 0$. Vi må da finne alle punkter hvor normalvektoren $\nabla f(a, b, c)$ er parallell med vektoren $(1, 1, 1)$. Dette gir oss ligningene

$$a = \lambda, \qquad 2b = \lambda, \qquad c = \lambda,$$

hvor $\lambda$ er et reelt tall. Innsatt i $f$ får vi

$$f\left(\lambda, \frac{\lambda}{2}, \lambda\right) = \frac{5}{2}\lambda^2 = 1 \quad \Rightarrow \quad \lambda = \pm\sqrt{\frac{2}{5}}.$$

Dette gir punktene

$$\left(\sqrt{\frac{2}{5}},\; \sqrt{\frac{1}{10}},\; \sqrt{\frac{2}{5}}\right) \quad \text{og} \quad \left(-\sqrt{\frac{2}{5}},\; -\sqrt{\frac{1}{10}},\; -\sqrt{\frac{2}{5}}\right)$$

hvor tangentplanet til ellipsoiden er parallelt med planet $x + y + z = 0$.

Kjeldevarsel: Løsningsforslaget skriv i denne oppgåva planet $x + y + z = 1$ (to stader), medan eksamen oppgåveteksten seier $x + y + z = 0$. Parallelleiet berre avheng av normalvektoren, så utrekninga er upåverka.

Kildesett: course=TMA4105 term=var year=2022 problem=2 file=tma4105_2022v.pdf
