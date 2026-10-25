### **Løsning til Oppgave 7**

a) Fra Crank-Nicolsons skjema (når $r = 1$)

$$\begin{array}{ll} i = 1: & 4U_1^1 - U_2^1 - U_0^1 = U_2^0 + U_0^0, \\ i = 2: & 4U_2^1 - U_3^1 - U_1^1 = U_3^0 + U_1^0, \\ i = 3: & 4U_3^1 - U_4^1 - U_2^1 = U_4^0 + U_2^0, \end{array}$$

hvor $U_0^0 = U_4^0 = 0$ er randbetingelsen for $t = 0$ og $U_4^1 = U_0^1 = k$ er randbetingelsen for $t = k$. Vi får

$$\left[ \begin{array}{rrr} 4 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 4 \end{array} \right] \left[ \begin{array}{c} U_1^1 \\ U_2^1 \\ U_3^1 \end{array} \right] = \left[ \begin{array}{rrr} 0 & 1 & 0 \\ 1 & 0 & 1 \\ 0 & 1 & 0 \end{array} \right] \left[ \begin{array}{c} U_1^0 \\ U_2^0 \\ U_3^0 \end{array} \right] + \left[ \begin{array}{c} k \\ 0 \\ k \end{array} \right],$$

hvor

$$\left[ \begin{array}{c} U_1^0 \\ U_2^0 \\ U_3^0 \end{array} \right] = \left[ \begin{array}{c} f(h) \\ f(2h) \\ f(3h) \end{array} \right] = \left[ \begin{array}{c} 3/2 \\ 2 \\ 3/2 \end{array} \right], \quad f(x) = 8x(1 - x^2),$$

er initialbetingelsen ($h = 1/4$) og $k = 1/16$ er randbetingelsen, $U_0^1$ og $U_4^1$. Ligningssystemet blir

$$\left[ \begin{array}{rrr} 4 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 4 \end{array} \right] \left[ \begin{array}{c} U_1^1 \\ U_2^1 \\ U_3^1 \end{array} \right] = \left[ \begin{array}{c} \frac{33}{16} \\ 3 \\ \frac{33}{16} \end{array} \right].$$

b) En iterasjon med Gauss-Seidel, med $x_0 = 3/2$, $y_0 = 2$, $z_0 = 3/2$, gir

$$x_1 = \frac{1}{4} \left[ \frac{33}{16} - (-1) \cdot y_0 - 0 \cdot z_0 \right] \approx 1.0156,$$

$$y_1 = \frac{1}{4} \left[ 3 - (-1) \cdot x_1 - (-1) \cdot z_0 \right] \approx 1.3789,$$

$$z_1 = \frac{1}{4} \left[ \frac{33}{16} - 0 \cdot x_1 - (-1) \cdot y_1 \right] \approx 0.8604.$$

**Kjeldevarsel:** Formelen $f(x) = 8x(1 - x^2)$ i kjelda er trykkfeil for initialbetingelsen $u(x,0) = 8x(1 - x)$ som oppgåva og tala i fasiten brukar: $8 \cdot \frac{1}{4}(1 - \frac{1}{4}) = \frac{3}{2}$, $8 \cdot \frac{1}{2}(1 - \frac{1}{2}) = 2$, $8 \cdot \frac{3}{4}(1 - \frac{3}{4}) = \frac{3}{2}$, mens $8x(1-x^2)$ ville gjeve andre tal. Gauss-Seidel-tala er kontrollrekna og stemmer med systemet i a): $x_1 = \frac{1}{4}(\frac{33}{16} + 2) = \frac{65}{64} \approx 1.0156$.

Kildesett: course=TMA4135 term=host year=2007 problem=7 file=tma4135_07h.pdf
