### **Løsning til Oppgave 1**

Siden funksjonen $f(x, y)$ opplagt ikke har singulære punkter må den største verdien oppnås enten i et kritisk punkt eller på randen. Vi ser først etter kritiske punkter, altså punkter hvor $\nabla f(x, y) = 0$. Her er

$$\nabla f(x, y) = (2y, 2x),$$

så det eneste kritiske punktet er $(0, 0)$, hvor $f(0, 0) = 0$. Randen av området er sirkelen $x^2 + y^2 = 1$. For å finne maksimumsverdien her er det enkleste å parametrisere sirkelen med polarkoordinater; da får vi $f(\cos\theta, \sin\theta) = 2\cos\theta\sin\theta = \sin 2\theta$, så den største verdien er $1$ når $\theta = \pi/4, \, 5\pi/4$; dette er da den største verdien av $f(x, y)$ på disken.

Vi kan også bruke Lagrange-multiplikatorer; da ser vi etter punkter $(x, y)$ hvor $x^2 + y^2 = 1$ og

$$\nabla f(x, y) = \lambda \nabla\bigl(x^2 + y^2\bigr),$$

altså $(y, x) = \lambda (x, y)$. Dette gir

$$y = \lambda x = \lambda^2 y,$$

slik at $y = 0$ eller $\lambda^2 = 1$. Hvis $y = 0$ får vi $x = \lambda y = 0$, men $(0, 0)$ ligger ikke på sirkelen. Vi må dermed ha $\lambda = \pm 1$ og $x = \pm y$. Setter vi dette inn i ligningen for sirkelen får vi

$$x^2 + y^2 = 2y^2 = 1$$

slik at $y = \pm 1/\sqrt{2}$. Vi har altså fire kritiske punkter: $\pm\frac{1}{\sqrt{2}}(1, 1), \pm\frac{1}{\sqrt{2}}(1, -1)$. Det gjenstår å evaluere funksjonen her: $f\bigl(\pm\frac{1}{\sqrt{2}}(1, 1)\bigr) = 1$, $f\bigl(\pm\frac{1}{\sqrt{2}}(1, -1)\bigr) = -1$, så den største verdien er igjen $1$.

Kildesett: course=TMA4105 term=var year=2023 problem=1 file=tma4105_2023v.pdf
