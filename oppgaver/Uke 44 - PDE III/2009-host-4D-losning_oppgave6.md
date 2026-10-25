### **Løsning til Oppgave 6**

Vi skriver de tre ligningene på følgende form:

$$
\begin{aligned}
4x &= 4 + y \\
4y &= 3 + x + z \\
4z &= y
\end{aligned}
$$

Gauss-Seidel gir da (bruker hele tiden sist tilgjengelige informasjon):

$$
\begin{aligned}
x^{(n+1)} &= \frac{1}{4} \cdot (4 + y^{(n)}) \\
y^{(n+1)} &= \frac{1}{4} \cdot (3 + x^{(n+1)} + z^{(n)}) \\
z^{(n+1)} &= \frac{1}{4} \cdot y^{(n+1)}
\end{aligned}
$$

Med de gitte startverdiene ($n = 0$) får vi da:

$$
\begin{aligned}
x^{(1)} &= \frac{1}{4} \cdot (4 + 1) = \frac{5}{4} = 1.25 \\
y^{(1)} &= \frac{1}{4} \cdot (3 + \frac{5}{4} + 0) = \frac{17}{16} = 1.06 \\
z^{(1)} &= \frac{1}{4} \cdot \frac{17}{16} = \frac{17}{64} = 0.266
\end{aligned}
$$

Løsningsvektoren etter en iterasjon er altså $(5/4, \; 17/16, \; 17/64)^T$.

Kildesett: course=TMA4135 term=host year=2009 problem=6 file=tma4135_09h.pdf
