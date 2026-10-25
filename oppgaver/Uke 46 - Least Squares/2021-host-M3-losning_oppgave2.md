### **Løsning til Oppgave 2**

La $T\colon\mathcal{P}_2\to\mathbb{R}^3$ være lineærtransformasjonen som evaluerer et andregradspolynom $p(x)=ax^2+bx+c$ i de tre punktene $x=0$, $x=1$ og $x=2$. Da har vi at

$$T(x^2)=\begin{bmatrix}0\\ 1\\ 4\end{bmatrix},\quad T(x)=\begin{bmatrix}0\\ 1\\ 2\end{bmatrix},\quad T(1)=\begin{bmatrix}1\\ 1\\ 1\end{bmatrix}.$$

Følgelig vil matrisen til $T$ med hensyn på standardbasisen $\{x^2,x,1\}$ være

$$A=\begin{bmatrix}0&0&1\\ 1&1&1\\ 4&2&1\end{bmatrix}.$$

Da kan vi finne $p(x)$ ved å løse systemet

$$\left[\begin{array}{ccc|c}0&0&1&-3\\ 1&1&1&-1\\ 4&2&1&5\end{array}\right]\sim\left[\begin{array}{ccc|c}0&0&1&-3\\ 1&1&0&2\\ 4&2&0&8\end{array}\right]\sim\left[\begin{array}{ccc|c}0&0&1&-3\\ 1&1&0&2\\ 2&0&0&4\end{array}\right]\sim\left[\begin{array}{ccc|c}0&0&1&-3\\ 0&1&0&0\\ 1&0&0&2\end{array}\right].$$

Altså har vi at $p(x)=2x^2-3$. Hvis vi dobbeltsjekker ser vi at $p(0)=-3$, $p(1)=-1$, og $p(2)=5$, slik oppgaven ber om.

Gjør vi det tilsvarende for førstekgradspolynom $q(x)=dx+e$ får vi systemet

$$\left[\begin{array}{cc|c}0&1&-3\\ 1&1&-1\\ 2&1&5\end{array}\right].$$

Dette har ingen løsning, så vi anvender minste kvadraters metode

$$\begin{bmatrix}0&1&2\\ 1&1&1\end{bmatrix}\left[\begin{array}{cc|c}0&1&-3\\ 1&1&-1\\ 2&1&5\end{array}\right]=\left[\begin{array}{cc|c}5&3&9\\ 3&3&1\end{array}\right]\sim\left[\begin{array}{cc|c}1&0&4\\ 0&1&-11/3\end{array}\right].$$

Førstekgradspolynomet $q(x)$ som best passer punktene blir da $q(x)=4x-11/3$.

*Kjeldevarsel: $p(x)=2x^2-3$ og minste kvadraters-løysinga $d=4$, $e=-\frac{11}{3}$ er kontrollrekna med sympy.*

Kildesett: course=TMA4110 term=host year=2021 problem=2 file=tma4110-eksamen-h21-bokmaal.pdf
