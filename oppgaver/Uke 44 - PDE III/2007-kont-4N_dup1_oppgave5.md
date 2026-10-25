### **Oppgave 5**

a) Den ikke-homogene biharmoniske likningen

$$\nabla^4 u = u_{xxxx} + 2u_{xxyy} + u_{yyyy} = f(x,y)$$

er gitt på området bestemt av $0 \leq x \leq 1$ og $0 \leq y \leq 1$. Vi har i tillegg gitt randverdiene $u = 0$ og $\nabla^2 u = 0$ på alle ytre render.

Vis at dette problemet er ekvivalent med å løse de to elliptiske problemene:

$$\begin{cases} v_{xx} + v_{yy} = f(x,y), & 0 \leq x \leq 1, \quad 0 \leq y \leq 1 \\ v(x,y) = 0 & \text{på randen} \\ u_{xx} + u_{yy} = v(x,y), & 0 \leq x \leq 1, \quad 0 \leq y \leq 1 \\ u(x,y) = 0 & \text{på randen} \end{cases} \tag{2}$$

b) Bruk endelege differanser med skrittlengde $h = 1/3$ i hver retning til å finne et lineært likningssystem som størrelsene $u_{ij} \approx u(ih, jh)$ må oppfylle når funksjonen $f(x,y) = -1$ for alle $x, y$ i området $0 \leq x \leq 1$ og $0 \leq y \leq 1$.

Kildesett: course=TMA4130 term=kont year=2007 problem=5 file=TMA413X2007k_bm.pdf
