### **Løsning til Oppgave 5**

**a)** Vi lager *Newtons divided difference interpolation* tabell

$$\begin{array}{|c|c|cccc|} \hline x_j & f_j = f(x_j) & f[x_j, x_{j+1}] & f[x_j, x_{j+1}, x_{j+2}] & f[x_j, \ldots, x_{j+3}] & f[x_j, \ldots, x_{j+4}] \\ \hline 0 & 1 & & & & \\ & & 5 & & & \\ 0.25 & 2.25 & & 12 & & \\ & & 11 & & 16 & \\ 0.5 & 5 & & 24 & & 0 \\ & & 23 & & 16 & \\ 0.75 & 10.75 & & 36 & & \\ & & 41 & & & \\ 1 & 21 & & & & \\ \hline \end{array}$$

og man får

$$P(x) = 1 + 5x + 12x(x - 0.25) + 16x(x - 0.25)(x - 5)$$

som forenkler seg til

$$P(x) = 16x^3 + 4x + 1.$$

**b)** Vi har

$$\begin{aligned} \int_0^1 P(x) \, dx &= \int_0^1 (16x^3 + 4x + 1) \, dx \\ &= \left[ 16 \frac{x^4}{4} + 4 \frac{x^2}{2} + x \right]_0^1 \\ &= 7. \end{aligned}$$

Simpsons regel gir

$$\begin{aligned} \int_0^1 P(x) \, dx \approx S_n &= \frac{\Delta x}{3} (P(0) + 4P(0.25) + 2P(0.5) + 4P(0.75) + P(1)) \\ &= \frac{0.25}{3} (1 + 4 \cdot 2.25 + 2 \cdot 5 + 4 \cdot 10.75 + 21) \\ &= 7. \end{aligned}$$

Feilestimat for feilen er gitt av

$$\left| \int_a^b f(x) \, dx - S_n \right| \leq \frac{f^4(c)(b-a)^5}{180n^2}$$

for noen $c \in [0, 1]$. Siden $P$ har graden 3 har vi $P^{(4)}(x) = 0$. Det vil si at feilen blir null for $P$. Den *degree of precision* til Simpsons metode er lik 3 og metoden gir den eksakte verdien av integralet til $P$.

*Kjeldevarsel: newtonleddet er trykt som $16x(x - 0.25)(x - 5)$ — med den tredje noden $(x - 0.5)$ blir uttryktet nettop $16x^3 + 4x + 1$ (sympy-stadfesta; med $(x-5)$ gir det $-7$ i $x = 1$, ikkje $21$). Feilestimatet er trykt med $f^4(c)$ (meinast $f^{(4)}(c)$), og tabellverdie og sluttresultat er elles konsistente. Ordrett elles, incl. «degree of precision».*

Kildesett: course=TMA4125 term=var year=2008 problem=5 file=eksamen-bok_2008v.pdf
