### **Oppgave 5**

La $R$ være det triangulære området i $x, y$-planet bestemt av ulikhetene $0 < x < 1$ og $0 < y < x$. Vi skal løse Laplaces ligning med randbetingelser i området $R$.

Ligningen med randbetingelser er

$$
\begin{aligned}
u_{xx} + u_{yy} = 0 \quad \text{for alle} \quad (x, y) \in R, \\
u(x, x) = 0, \quad u(1, y) = 0, \quad u(x, 0) = 16 \, x(1 - x).
\end{aligned}
$$

Bruk gitteret bestemt av punktene $(x_i, y_j) = (ih, jh)$, med $h = 0.25$. La $U_{i,j} \approx u(ih, jh)$ og bruk 5-punkts approksimasjonen for $u_{xx} + u_{yy}$ til å sette opp et ligningssystem for de tre ukjente verdiene $X = U_{2,1}$, $Y = U_{3,1}$ og $Z = U_{3,2}$ i det indre av området.

Kildesett: course=TMA4130 term=host year=2009 problem=5 file=eksamen-bok_2009.pdf
