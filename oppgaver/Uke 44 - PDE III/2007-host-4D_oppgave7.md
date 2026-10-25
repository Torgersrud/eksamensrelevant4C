### **Oppgave 7**

Gitt problemet

$$\left\{ \begin{array}{ll} u_t = u_{xx} & (t > 0, \, 0 < x < 1) \\ u(0,t) = u(1,t) = t & (t \geq 0) \\ u(x,0) = 8x(1-x) & (0 \leq x \leq 1) \end{array} \right.$$

a) Bruk Crank-Nicolsons skjema

$$(2 + 2r)U_i^{j+1} - r\left(U_{i+1}^{j+1} + U_{i-1}^{j+1}\right) = (2 - 2r)U_i^j + r\left(U_{i+1}^j + U_{i-1}^j\right),$$

med $\Delta x = h = 1/4$, $\Delta t = k = 1/16$, Couranttallet $r = k/h^2 = 1$, $U_i^0 = u(ih, 0)$ og hvor $U_i^j \approx u(x_i, t_j) = u(hi, kj)$, til å finne et lineært ligningssystem for $U_i^1 \approx u(ih, k)$, $i = 1, 2, 3$.

b) La $x_0 = 3/2$, $y_0 = 2$, $z_0 = 3/2$, og gjør én iterasjon med Gauss-Seidel på ligningssystemet

$$\begin{array}{rcl} 4x - y & = & 33/16, \\ -x + 4y - z & = & 3, \\ -y + 4z & = & 33/16. \end{array}$$

Kildesett: course=TMA4135 term=host year=2007 problem=7 file=tma4135_07h.pdf
