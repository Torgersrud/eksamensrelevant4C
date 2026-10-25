### **Løsning til Oppgave 1**

a) Løsning: fouriersinusrekken til $f(x)$: $f(x) \sim \sum_{n=1}^{\infty} b_n \sin n\pi x$, der $b_1 = 1$ og $b_i = 0$ for $i \geq 2$. Ingen regning er nødvendig.

Finn fourier cosinus rekken til $f(x) = \sin \pi x$ $0 < x < 1$. Løsning:

$$a_0 = \int_0^1 \sin \pi x \, dx = \left[ -\frac{1}{\pi} \cos \pi x \right]_0^1 = -\frac{1}{\pi} \cos \pi + \frac{1}{\pi} \cos 0 = \frac{2}{\pi} \tag{1}$$

$$a_1 = 2 \int_0^1 \sin \pi x \cos \pi x \, dx = \int_0^1 \sin 2\pi x \, dx = 0 \tag{2}$$

Det siste integralet er lik null siden $\sin 2\pi x$ integreres over en hel periode. Vi finner $a_n$ for $n \geq 2$:

$$a_n = 2 \int_0^1 \sin \pi x \cos n\pi x \, dx = 2 \int_0^1 \frac{1}{2} (\sin(1-n)\pi x + \sin(1+n)\pi x) \, dx =$$

$$\left[ -\frac{1}{(1-n)\pi} \cos(1-n)\pi x - \frac{1}{(1+n)\pi} \cos(1+n)\pi x \right]_0^1 =$$

$$- \frac{1}{(1-n)\pi} (-1)^{1-n} - \frac{1}{(1+n)\pi} (-1)^{1+n} + \frac{1}{(1-n)\pi} + \frac{1}{(1+n)\pi} =$$

$$2 \frac{1+(-1)^n}{(1-n^2)\pi} \tag{3}$$

Dvs fouriercosinusrekken er

$$f(x) \sim \frac{2}{\pi} - \frac{4}{3\pi} \cos 2\pi x - \frac{4}{15\pi} \cos 4\pi x - \frac{4}{63\pi} \cos 6\pi x + \cdots$$

$$f(x) \sim \frac{2}{\pi} - \sum_{j=1}^{\infty} \frac{4}{(4j^2-1)\pi} \cos 2j\pi x$$

b) Vi skulle finne alle løsninger til randverdifproblemet

$$\frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2} = u \tag{4}$$

$$u_x(0,y) = u_x(1,y) = 0 \tag{5}$$

på formen $u(x,y) = X(x)Y(y)$:

Randbetingelsene gir $X'(0)Y(y) = X'(1)Y(y) = 0$ for alle $y$. Dvs $X'(0) = X'(1) = 0$ eller $Y(y) = 0$. Vi har for det siste tilfellet $u(x,y) = X(x)Y(y) = 0$. Hvilket er den trivielle løsningen. Vi vil søke andre løsninger i teksten under. Dvs at vi vil anta at $Y(y) \neq 0$.

Partsiellderiverer vi $u(x,y) = X(x)Y(y)$ to ganger med hensyn på $x$ og $y$ så får vi $u_{xx}(x,y) = X''(x)Y(y)$ og $u_{yy}(x,y) = X(x)Y''(y)$.

Setter vi dette inn i den opprinnelige likningen får vi:

$$X''(x)Y(y) + X(x)Y''(y) = X(x)Y(y). \tag{6}$$

Vi omformer denne likningen og får:$^1$

$$\frac{X''(x)}{X(x)} = -\frac{Y''(y)}{Y(y)} + 1 = k. \tag{7}$$

Vi vil løse

$$\frac{X''(x)}{X(x)} = k. \tag{8}$$

Vi løser for $k = \lambda^2 > 0$. Da er $X(x) = Ae^{\lambda x} + Be^{-\lambda x}$, og $X'(x) = A\lambda e^{\lambda x} - \lambda Be^{-\lambda x}$. Randbetingelsene gir $0 = X'(0) = A\lambda - \lambda B$. Dvs $A = B$ og $0 = X'(1) = A\lambda e^{\lambda} - A\lambda e^{-\lambda}$. Dvs $A = 0$. Og derfor $F(x) = 0$. Vi har antatt at $u(x,y) \neq 0$, så vi ser bort ifra denne.

Vi løser for $k = 0$. Da er $X(x) = Ax + B$, og $X'(x) = A$. Randbetingelsene gir $0 = X'(0) = X'(1) = A$. Dvs $A = 0$. Løsning er $X_0(x) = B$. Legg merke til at vi ikke ser bort ifra konstant løsning.

Vi løser for $k = -\lambda^2 < 0$. Da er $X(x) = A\cos(\lambda x) + B\sin(\lambda x)$ og $X'(x) = B\lambda\cos(\lambda x) - A\lambda\sin(\lambda x)$. Første randbetingelse gir $0 = X'(0) = B\lambda\cos(0) - A\lambda\sin(0) = B\lambda$. Dvs $B = 0$. Andre randbetingelse gir $0 = X'(1) = -A\lambda\sin(\lambda)$. Dvs $\lambda = n\pi$ der $n = 1, 2, 3, \ldots$. Dvs $X_n(x) = A_n\cos(n\pi x)$.

Vi vil nå løse

$$\frac{Y''(y)}{Y(y)} = 1 + n^2\pi^2. \tag{9}$$

Den har løsning

$$Y_n(y) = A_n e^{\sqrt{1+n^2\pi^2}\,y} + B_n e^{-\sqrt{1+n^2\pi^2}\,y}.$$

$^1$Vi har antatt at $u(x,y) \neq 0$. Derfor kan vi dele med $u(x,y)$ på begge sider av likningen.

c) Fra randkravet $X(x)Y(1) = u(x,0) = 0$ har vi $Y(1) = 0$. Vi får derfor

$$0 = A_n e^{\sqrt{1+n^2\pi^2}} + B_n e^{-\sqrt{1+n^2\pi^2}}.$$

Dvs: $B_n = -A_n e^{2\sqrt{1+n^2\pi^2}}$.

Løsningene er på formen $u_n(x,y) = X_n(x)Y_n(y)$

Fra superposisjonsprinsippet får vi at en generell løsning for randverdi problemet

$$u(x,y) = \sum_{n=0}^{\infty} X_n(x)Y_n(y)$$

$$= A_0 e^{y} + B_0 e^{-y} + \sum_{n=1}^{\infty} \cos(n\pi x) (A_n e^{\sqrt{1+n^2\pi^2}\,y} + B_n e^{-\sqrt{1+n^2\pi^2}\,y}) \tag{10}$$

Randbetingelsen $u(x,0) = \sin \pi x$ gir

$$\sin \pi x = A_0 + B_0 + \sum_{n=1}^{\infty} \cos(n\pi x)(A_n + B_n) \tag{11}$$

Cosinusrekkeutviklingen til $\sin \pi x$ funnet i punkt a) gir

$$\begin{array}{rcl} A_0 + B_0 & = & \frac{2}{\pi} \\ A_n + B_n & = & 0, \quad \text{For } n > 0 \text{ odde} \\ A_n + B_n & = & \frac{4}{\pi(1-n^2)}, \quad \text{For } n > 0 \text{ jevn} \end{array} \tag{12}$$

Bruker så $B_n = -A_n e^{2\sqrt{1+n^2\pi^2}}$:

$$\begin{array}{rcl} A_0 & = & \frac{2}{(1-e^2)\pi} \\ B_0 & = & -\frac{2e^2}{(1-e^2)\pi} \\ A_n = B_n & = & 0, \quad \text{For } n > 0 \text{ odde} \\ A_n & = & \frac{4}{\pi(1-n^2)(1-e^{2\sqrt{1+n^2\pi^2}})}, \quad \text{For } n > 0 \text{ jevn} \\ B_n & = & -\frac{4e^{2\sqrt{1+n^2\pi^2}}}{\pi(1-n^2)(1-e^{2\sqrt{1+n^2\pi^2}})}, \quad \text{For } n > 0 \text{ jevn} \end{array} \tag{13}$$

Løsningen blir

$$u(x,y) = 2 \frac{e^{y} - e^{2-y}}{(1-e^2)\pi} + \sum_{n=1, 2|n}^{\infty} \cos(n\pi x) \frac{4e^{\sqrt{1+n^2\pi^2}\,y} - 4e^{\sqrt{1+n^2\pi^2}(2-y)}}{\pi(1-n^2)(1-e^{2\sqrt{1+n^2\pi^2}})} \tag{14}$$

**Kjeldevarsel:** I c) står det trykt "Fra randkravet $X(x)Y(1) = u(x,0) = 0$"; det rette er $u(x,1) = 0$ slik oppgåva seier (utrekninga følgjer $Y(1) = 0$, som er konsistent med $u(x,1) = 0$).

Kildesett: course=TMA4135 term=kont year=2007 problem=1 file=tma4135_07k.pdf
