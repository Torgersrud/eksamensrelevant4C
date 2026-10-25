### **Løsning til Oppgave 6**

Siden mellomrummene er like store kan vi bruke Gregory-Newton foroverdifferanseformel.

$$
\begin{array}{|c|c|c|c|c|c|c|}
\hline
j & x_j & f_j & \Delta f_j & \Delta^2 f_j & \Delta^3 f_j & \Delta^4 f_j \\
\hline
0 & 0 & 2 & -3 & 6 & -12 & 24 \\
1 & 1 & -1 & 3 & -6 & 12 & \\
2 & 2 & 2 & -3 & 6 & & \\
3 & 3 & -1 & 3 & & & \\
4 & 4 & 2 & & & & \\
\hline
\end{array}
$$

Polynomet blir

$$P(x) = 2 - 3\binom{x}{1} + 6\binom{x}{2} - 12\binom{x}{3} + 24\binom{x}{4} = x^4 - 8x^3 + 20x^2 - 16x + 2.$$

Vi observerer at funksjonen vi skal interpolere har tre like verdier. Det betyr at vi kan skrive $P(x)$ på formen

$$P(x) = 2 + x(x - 2)(x - 4)(ax + b).$$

Ved å evaluere for $x = 1$ og $x = 3$ får vi to lineære ligninger til bestemmelse av koeffisientene $a$ og $b$. Ligningene blir

$$
\begin{aligned}
a + b &= -1, \\
3a + b &= \phantom{-}1,
\end{aligned}
$$

som gir $a = 1$ og $b = -2$. Dermed får vi $P(x) = 2 + x(x - 2)^2(x - 4)$.

Kildesett: course=TMA4135 term=kont year=2008 problem=6 file=tma4135_08k.pdf
