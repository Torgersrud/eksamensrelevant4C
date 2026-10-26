### **Løsning til Oppgave 5**

La $f(x, y) = x^2 + y^2$ og $g(x, y) = 5x^2 + 6xy + 5y^2 - 8$, slik at

$$\nabla f = 2x \, \mathbf{i} + 2y \, \mathbf{j}, \qquad \nabla g = (10x + 6y) \, \mathbf{i} + (6x + 10y) \, \mathbf{j}.$$

Lagrange multiplikatormetode gir så

$$\nabla f = \lambda \nabla g,$$

det vil si,

$$x = \lambda(5x + 3y), \tag{1}$$

$$y = \lambda(3x + 5y). \tag{2}$$

Anta at $5x + 3y = 0$. Da gir (1) at $x = 0$, som ved antagelsen om at $5x + 3y = 0$ gir at $y = 0$. Anta at $3x + 5y = 0$. Da gir (2) at $y = 0$, som ved antagelsen om at $3x + 5y = 0$ gir at $x = 0$. Ettersom $g(0, 0) = -8 \neq 0$ kan vi se bort fra $x = y = 0$.

Fra (1) og (2) får vi

$$\lambda = \frac{x}{5x + 3y} = \frac{y}{3x + 5y}. \tag{3}$$

Ligning (3) gir så $3x^2 + 5xy = 3y^2 + 5xy$, det vil si $x^2 = y^2$.

La så $y = x$. Innsatt i $g(x, y)$ gir dette

$$g(x, x) = 5x^2 + 6x^2 + 5x^2 - 8 = 16x^2 - 8 = 0,$$

det vil si $x = \pm 1/\sqrt{2}$, som igjen gir

$$f\left(\pm \frac{1}{\sqrt{2}}, \pm \frac{1}{\sqrt{2}}\right) = \frac{1}{2} + \frac{1}{2} = 1.$$

La så $y = -x$. Innsatt i $g(x, y)$ gir dette

$$g(x, -x) = 5x^2 - 6x^2 + 5x^2 - 8 = 4x^2 - 8 = 0,$$

det vil si $x = \pm\sqrt{2}$, som igjen gir

$$f\left(\pm\sqrt{2}, \mp\sqrt{2}\right) = 2 + 2 = 4.$$

Avstanden fra origo til kurven $5x^2 + 6xy + 5y^2 = 8$ er gitt ved $h(x, y) = \sqrt{x^2 + y^2} = \sqrt{f(x, y)}$. Den største avstanden fra origo til kurven er dermed $\sqrt{4} = 2$, og den minste avstanden er $\sqrt{1} = 1$.

Kildesett: course=TMA4105 term=var year=2011 problem=5 file=tma4105_11v.pdf
