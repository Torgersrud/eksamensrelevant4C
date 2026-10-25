### **Løsning til Oppgave 32**

Vi ønsker å finne et andregradspolynomial $p(x)=ax^2+bx+c$, som går gjennom alle punktene. Det betyr at vi må løse ligningssystemet

$$\begin{cases}a-b+c=0=p(-1)\\ c=1=p(0)\\ 4a+2b+c=2=p(2)\end{cases}$$

Vi radreduserer totalmatrisen til systemet:

$$\left[\begin{array}{ccc|c}1&-1&1&0\\ 0&0&1&1\\ 4&2&1&2\end{array}\right]\sim\left[\begin{array}{ccc|c}1&-1&1&0\\ 0&1&-1/2&1/3\\ 0&0&1&1\end{array}\right]\sim\left[\begin{array}{ccc|c}1&0&0&-1/6\\ 0&1&0&5/6\\ 0&0&1&1\end{array}\right].$$

Polynomet er altså $p(x)=-\frac{1}{6}x^2+\frac{5}{6}x+1$.

*Kjeldevarsel: interpolasjonspolynomet er kontrollrekna med sympy — rettsvar er fjerde alternativ.*

Kildesett: course=TMA4110 term=kont year=2020 problem=32 file=TMA4110_TMA4115_kont_2020_bokmaal.pdf
