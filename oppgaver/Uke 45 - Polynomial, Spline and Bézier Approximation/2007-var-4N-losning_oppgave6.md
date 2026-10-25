### **Løsning til Oppgave 6**

a) Sett opp Newtons skjema for dividerte differanser:

$$\begin{array}{c|ccc}0.0&0.1& &\\ & &4.500&\\ 0.2&1.0& &-5.125\\ &-0.625& &\\ 1.0&0.5& &\end{array}$$

Da blir

$$p(x)=0.1+4.500\cdot(x-0.0)-5.125\cdot(x-0.0)\cdot(x-0.2)$$

$$=0.1+4.500\cdot x-5.125\cdot x\cdot(x-0.2)$$

og videre

$$p(0.5)=0.1+4.500\cdot 0.5-5.125\cdot 0.5\cdot(0.5-0.2)=1.58125$$

Oppgaven kan også løses med Lagrangeinterpolasjon. Det er mer jobb, spesielt siden en kan få gode hint om Newtoninterpolasjonen i oppgaveteksten til b). Vi må da sette opp og evaluere de tre kardinalpolynomene:

$$\begin{array}{rcl}l_{0}(x)&=&\frac{(x-0.2)(x-1.0)}{(-0.2)(-1.0)}\\ l_{1}(x)&=&\frac{(x-0.0)(x-1.0)}{(0.2)(0.2-1.0)}\\ l_{2}(x)&=&\frac{(x-0.0)(x-0.2)}{(1.0)(1.0-0.2)}\end{array}$$

$$\begin{array}{rcl}l_{0}(0.5)&=&\frac{(0.5-0.2)(0.5-1.0)}{(-0.2)(-1.0)}=-0.75\\ l_{1}(0.5)&=&\frac{(0.5-0.0)(0.5-1.0)}{(0.2)(0.2-1.0)}=1.5625\\ l_{2}(0.5)&=&\frac{(0.5-0.0)(0.5-0.2)}{(1.0)(1.0-0.2)}=0.1875\end{array}$$

Det interpolerende polynomet blir

$$p(x)=0.1\cdot l_{0}(x)+1.0\cdot l_{1}(x)+0.5\cdot l_{2}(x),$$

og verdien som etterspørres er

$$p(0.5)=0.1\cdot l_{0}(0.5)+1.0\cdot l_{1}(0.5)+0.5\cdot l_{2}(0.5)$$

$$=0.1\cdot(-0.75)+1.0\cdot 1.5625+0.5\cdot 0.1875=1.58125$$

*Kjeldevarsel: facit er trykt på bokmål (PDF-s. 14–15) og er sitert ordrett; facits del b) om matlabkoden følgjer ikkje med (Matlab-regel). Newton-skjemaet er gjengjeve med same talplassering som i trykket. Dei dividerte differansane $4.500$, $-0.625$ og $-5.125$, polynomet $p(x)=0.1+4.500x-5.125x(x-0.2)$ og $p(0.5)=1.58125$ er kontrollreikna med sympy, det same er kardinalpolynoma $l_{0}(0.5)=-0.75$, $l_{1}(0.5)=1.5625$ og $l_{2}(0.5)=0.1875$. Bokmålssetninga med det engelske ordet «hint» står trykt slik og er teken med uendra.*

Kildesett: course=TMA4123 term=var year=2007 problem=6 file=TMA4123_v07.pdf
