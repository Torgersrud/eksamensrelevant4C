### **Oppgave 2**

a) Beregn Fourercosinusrekka til funksjonen $f$ definert ved,

$$f(x) = \begin{cases} 0 & \text{if} \quad 0 \le x < 1, \\ 1 & \text{if} \quad 1 \le x < 2. \end{cases}$$

b) Finn løsningen av rand- og initialverdiproblemet

$$
\begin{aligned}
(1) \qquad u_t &= u_{xx} && \text{(den éndimensjonale varmeligningen)}, \\
(2) \qquad u_x(0, t) &= u_x(2, t) = 0 && \text{for } t \ge 0, \\
(3) \qquad u(x, 0) &= f(x) && \text{for } 0 < x < 2,
\end{aligned}
$$

når det oppgis at alle funksjoner av formen $u(x, t) = F(x)G(t)$ som oppfyller (1) og (2) er enten en konstant eller en konstant ganger funksjonen $u_n(x, t) = e^{-(n\frac{\pi}{2})^2 t} \cos n\frac{\pi}{2}x$, for $n = 1, 2, 3, \ldots$.

c) Finn alle løsningene av ligning (1) av formen $u(x, t) = F(x)G(t)$ som oppfyller randbetingelsene

$$(4) \qquad u(0, t) = u_x(2, t) = 0 \qquad \text{for } t \ge 0.$$

Kildesett: course=TMA4135 term=kont year=2009 problem=2 file=tma4135_09k.pdf
