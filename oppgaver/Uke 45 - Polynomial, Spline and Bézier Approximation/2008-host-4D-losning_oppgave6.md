### **Løsning til Oppgave 6**

a) For de tre foreslåtte fikspunktiturasjonene(på formen $x_{n+1} = g(x_n)$) sjekker vi $g'(x)$.

- For nummer 1) er $g'(x) = 3x^2$. Siden $g'(1) > 1$ og $g'(x)$ er monotont økende er $g'(x) > 1$ for $x \in I$, og vi vet da at iterasjonen ikke vil konvergere til en løsning i $I$, uansett startverdi $x_0 \in I$.
- For nummer 2) er $g'(x) = -\frac{1}{x^2} - \frac{2}{x^3}$ og $g'(1.5) < -1$. $g'(x)$ er monotont økende, og $|g'(x)| > 1$ for $x \in I$
- For nummer 3) er $g'(x) = \frac{1}{3}(x+1)^{-2/3}$. Siden $g'(1) < 1$, $g'(1.5) < 1$, og $g'(x)$ er monotont minkende, vil $|g'(x)| < 1$ for $x \in I$, og iterasjonen konvergerer for alle $x_0 \in I$. Dette er den vi bør bruke.

Utfører vi iterasjonen får vi $x_0 = 1$, $x_1 = 1.2599$, $x_2 = 1.3122$, $x_3 = 1.3223$, $x_4 = 1.3242$. Videre vil de tre første sifrene forbli uforandret, og vi kan konkludere at $s = 1.32\ldots$.

b) Bruker vi metoden med Newtons dividerte differanser, får vi skjemaet

$$
\begin{array}{c|lll}
0 & -1 & 0 & 3 \\
1 & -1 & 6 & \\
2 & 5 & &
\end{array}
$$

Polynomet blir $-1 + 0 \cdot (x - 0) + 3 \cdot (x - 0)(x - 1) = 3x^2 - 3x - 1$, med nullpunkter $1.26376$ og $-0.26376$. Vi må velge det nullpunktet som ligger inne i intervallet, altså blir vår approksimasjon $s^* = 1.26376$.

NB: Om interpolasjonspunktene hadde ligget tettere ville vi selvsagt fått et mer nøyaktig resultat. Denne metoden er faktisk en av komponentene i matlabes *fminsearch*.

Kildesett: course=TMA4135 term=host year=2008 problem=6 file=tma4135_08h.pdf
