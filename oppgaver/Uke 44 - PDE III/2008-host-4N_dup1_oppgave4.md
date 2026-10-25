### **Oppgave 5**

a) Vi vil løse ligningen

$$u_{xx}(x, y) + u_{yy}(x, y) = 27(x + y),$$

på firkanten $[0, 1] \times [0, 1]$ med randbetingelser

$$u(0, y) = u(x, 0) = 0, \quad u(x, 1) = 3x, \quad u(1, y) = 3y.$$

Finn en tilnærming til løsningen $u(x, y)$ ved å bruke sentraldifferanser for å approksimere $u_{xx}$ og $u_{yy}$. La $h = 1/3$ være skrittlengden, og la gitteret være gitt av punktene $(x_i, y_j) = (ih, jh)$ for $i, j = 0, \ldots, 3$. Sett opp et system av ligninger for $U_1^1, U_2^1, U_1^2, U_2^2$, der $U_i^j \approx u(x_i, y_j)$

b) Utfør én Gauss-Seidel-iterasjon på systemet du fikk i oppgave a). Hvis du ikke fikk til oppgave a), bruk systemet

$$\begin{bmatrix} -5 & 1 & 1 & 1 \\ 1 & -5 & 1 & 1 \\ 1 & 1 & -5 & 1 \\ 1 & 1 & 1 & -5 \end{bmatrix} \begin{bmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{bmatrix} = \begin{bmatrix} 2.5 \\ 2 \\ 2 \\ -0.5 \end{bmatrix}.$$

Bruk startvektoren $\boldsymbol{x}^{(0)} = -[1, 1, 1, 1]^T$ i begge tilfellene.

Kildesett: course=TMA4130 term=host year=2008 problem=4 file=eksamen-bok_2008.pdf
