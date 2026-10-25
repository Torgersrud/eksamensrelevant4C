### **Løsning til Oppgave 2**

a) Likeutvidelsen $\tilde{f}$ av $f$ er periodisk med periode $2L = 4$, så vi har

$$\tilde{f}(x) = a_0 + \sum_{n=1}^{\infty} a_n \cos n\frac{\pi}{2} x.$$

Vi finner

$$
\begin{aligned}
a_0 &= \frac{1}{2}, \quad \text{og} \\
a_n &= \int_1^2 \cos n\frac{\pi}{2} x \, dx = \begin{cases} 0 & \text{if} \quad n = 2k, \\ \frac{2}{\pi} \frac{(-1)^{k+1}}{2k+1} & \text{if} \quad n = 2k+1. \end{cases}
\end{aligned}
$$

Skriver vi dette ut ser vi at

$$\tilde{f}(x) = \frac{1}{2} - \frac{2}{\pi} \left( \frac{\cos \frac{\pi}{2} x}{1} - \frac{\cos 3\frac{\pi}{2} x}{3} + \frac{\cos 5\frac{\pi}{2} x}{5} - \cdots \right).$$

b) Siden ligningen og randkravene er homogene gjelder superposisjonsprinsippet, så

$$u(x, t) = A_0 + \sum_{1}^{\infty} A_n e^{-(n\frac{\pi}{2})^2 t} \cos n\frac{\pi}{2} x$$

er løsning av (1) og (2).

For også å få tilfredsstilt initialkravet (3) må vi velge $A_n = a_n$. Altså

$$u(x, t) = \frac{1}{2} - \frac{2}{\pi} \left( e^{-(\frac{\pi}{2})^2 t} \frac{\cos \frac{\pi}{2} x}{1} - e^{-(3\frac{\pi}{2})^2 t} \frac{\cos 3\frac{\pi}{2} x}{3} + e^{-(5\frac{\pi}{2})^2 t} \frac{\cos 5\frac{\pi}{2} x}{5} - \cdots \right).$$

c) Setter vi inn $u(x, t) = F(x)G(t)$ i ligningen, finner vi etter litt drøfting at

$$F'' = -\lambda^2 F \qquad \text{og} \qquad G' = -\lambda^2 G$$

med $\lambda > 0$. Vi har da at

$$F(x) = A \cos \lambda x + B \sin \lambda x \quad \text{og} \quad G(t) = C e^{-\lambda^2 t}$$

som insatt i (2) gir

$$A \cos \lambda 0 + B \sin \lambda 0 = 0 \quad \text{og} \quad \lambda B \cos \lambda 2 - \lambda A \sin \lambda 2 = 0.$$

Siden $\lambda > 0$ får vi ikke-triviell løsning når

$$A = 0 \quad \text{og} \quad 2\lambda = \left( n + \frac{1}{2} \right) \pi \quad \text{for} \quad n = 1, 2, 3, \ldots$$

eller

$$\lambda = \frac{(2n+1)\pi}{4} \quad \text{for} \quad n = 1, 2, 3, \ldots.$$

Altså

$$u_n(x, t) = B_n e^{-\left( \frac{(2n+1)\pi}{4} \right)^2 t} \sin \frac{(2n+1)\pi}{4} x.$$

Kildesett: course=TMA4135 term=kont year=2009 problem=2 file=tma4135_09k.pdf
