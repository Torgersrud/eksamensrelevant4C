### **Oppgave 5**

Gitt varmelikningsproblemet

$$\begin{array}{rl}u_{t}=u_{xx}& t\geq 0,\ -1\leq x\leq 1\\ u(-1,t)=0& t\geq 0\\ u(1,t)=1& t\geq 0\end{array}$$

med initialbetingelse

$$u(x,0)=\begin{cases}0&-1\leq x\leq 0\\ 1&0\leq x\leq 1\end{cases}$$

**a)** Bruk gitteret $(x_i, t_j)$ med $i = 0, \ldots, n$ hvor $x_i = -1 + ih$, $h = 2/n$, og $t_j = jk$. Sett opp Euler eksplisitte metode for å finne en numerisk tilnærming $u_i^{j+1}$ av løsningen $u$ i punktet $(x_i, t_{j+1})$. Bruk da

$$\begin{array}{rcl}u_{t}(x,t)&\approx&(u(x,t+k)-u(x,t))/k\\ u_{xx}(x,t)&\approx&(u(x+h,t)-2u(x,t)+u(x-h,t))/h^{2}\end{array}$$

**b)** Sett $n = 5$ og $k = 0.01$ og beregn $[u_{1}^{1}, u_{2}^{1}, u_{3}^{1}, u_{4}^{1}]$ fra de kjente verdiene $[u_{0}^{0}, u_{1}^{0}, u_{2}^{0}, u_{3}^{0}, u_{4}^{0}, u_{5}^{0}]$.

*Kjeldevarsel: initialbetingelsen er trykt med overlappinge tilfelle — begge tilffa har $\leq$ og dekkjer dermed $x = 0$ med både $0$ og $1$; gitteret $x_i = -1 + 2i/5$ treffer likevel aldri $x = 0$, så oppgåva er brukbar som trykt. Elles ordrett frå skannen.*

Kildesett: course=TMA4123 term=var year=2007 problem=5 file=TMA4123_v07.pdf
