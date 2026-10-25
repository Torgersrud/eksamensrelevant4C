### **Løsning til Oppgave 4**

Vi finner først andregradspolyomet $p(x)=ax^2+bx+c$ som passer eksakt til de tre punktene. Da må vi ha

$$p(0)=-1,\quad p(1)=1\quad\text{og}\quad p(2)=7,$$

så vi kan sette opp likningssystemet

$$\begin{cases}c=-1\\ a+b+c=1\\ 4a+2b+c=7\end{cases}$$

for koeffisientene i $p$. Dette systemet har én løsning: $a=2$, $b=0$ og $c=-1$. Polynomet blir altså $p(x)=2x^2-1$.

Nå skal vi finne det førsteordens polynomet $q(x)=dx+e$ som passer best til punktene. Hvis $q$ skulle passet eksakt til punktene, ville vi hatt

$$q(0)=-1,\quad q(1)=1\quad\text{og}\quad q(2)=7,$$

som gir følgende likningssystem for koeffisientene:

$$\begin{cases}e=-1\\ d+e=1\\ 2d+e=7\end{cases}$$

Skrevet på matriseform ser det slik ut:

$$\begin{bmatrix}0&1\\ 1&1\\ 2&1\end{bmatrix}\begin{bmatrix}a\\ b\end{bmatrix}=\begin{bmatrix}-1\\ 1\\ 7\end{bmatrix}.$$

Vi finner den beste tilnærmingen til en løsning ved å bruke minste kvadraters metode. Da må vi gange begge sider av likningen med den transponerte

$$\begin{bmatrix}0&1&2\\ 1&1&1\end{bmatrix}$$

av koeffisientmatrisen. Det gir oss likningssystemet

$$\begin{bmatrix}5&3\\ 3&3\end{bmatrix}\begin{bmatrix}d\\ e\end{bmatrix}=\begin{bmatrix}15\\ 7\end{bmatrix},$$

som har løsning $d=4$ og $e=-\frac{5}{3}$. Polynomet er $q(x)=4x-\frac{5}{3}$.

[Figur: Koordinatplot med $x$- og $y$-akse. Parabelen $p(x)=2x^2-1$ og linja $q(x)=4x-\frac{5}{3}$ er tegna gjennom punkta $(0,-1)$, $(1,1)$ og $(2,7)$, som er markerte med blå prikkar; parabelen går gjennom alle tre, linja gjennom det midtre området.]

*Kjeldevarsel: på matriseforma i fasiten står koeffisientvektoren for $q$ som $\begin{bmatrix}a\\ b\end{bmatrix}$, men etter likningssystemet like over skal det vere $\begin{bmatrix}d\\ e\end{bmatrix}$ — trykkfeil i fasiten. Teksten over fylgjer fasiten som det står. $A^{\top}A=\begin{bmatrix}5&3\\ 3&3\end{bmatrix}$, $A^{\top}\mathbf{b}=(15,7)$, $d=4$, $e=-\frac{5}{3}$ og $p(x)=2x^2-1$ er kontrollrekna med sympy.*

Kildesett: course=TMA4110 term=host year=2018 problem=4 file=tma4110-2018h-nb.pdf
