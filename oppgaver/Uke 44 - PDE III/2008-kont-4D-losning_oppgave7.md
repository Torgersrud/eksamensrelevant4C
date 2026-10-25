### **Løsning til Oppgave 7**

For å bruke Gauss–Seidel, skriver vi om systemet, slik at de dominante diagonalleddene kommer på venstre side.

$$
\begin{aligned}
x &= \phantom{0.25x + \;} 0.25y \phantom{{}+ 0.25z} - \phantom{1.}1.50, \\
y &= 0.25x \phantom{{}+ y} + \phantom{0.}0.25z - \phantom{1.}1.75, \\
z &= \phantom{0.25x + \;} 0.25y \phantom{{}+ 0.25z} - \phantom{1.}2.00.
\end{aligned}
$$

Gauss–Seidels metode er følgende

$$
\begin{aligned}
x^{(n+1)} &= \phantom{0.25x^{(n+1)} + \;} 0.25y^{(n)} \phantom{{}+ 0.25z^{(n)}} - \phantom{1.}1.50, \\
y^{(n+1)} &= 0.25x^{(n+1)} \phantom{{}+ y^{(n)}} + 0.25z^{(n)} - \phantom{1.}1.75, \\
z^{(n+1)} &= \phantom{0.25x^{(n+1)} + \;} 0.25y^{(n+1)} \phantom{{}+ 0.25z^{(n)}} - \phantom{1.}2.00.
\end{aligned}
$$

Med startverdiene $x^{(0)} = -2$, $y^{(0)} = -3$, $z^{(0)} = -3$ får vi

$$
\begin{aligned}
x^{(1)} &= \phantom{-0.5625 - 0.75} -0.75 \phantom{{}+ 0.75} - \phantom{1.}1.50 &= -2.25, \\
y^{(1)} &= -0.5625 \phantom{{}+ 0.75} - \phantom{0.}0.75 - \phantom{1.}1.75 &= -3.0625, \\
z^{(1)} &= \phantom{-0.5625} -0.765625 \phantom{{}+ 0.75} - \phantom{1.}2.00 &= -2.765625.
\end{aligned}
$$

Kildesett: course=TMA4135 term=kont year=2008 problem=7 file=tma4135_08k.pdf
