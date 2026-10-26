### **Løsning til Oppgave 2**

Ved å utnytte at $x^2 + y^2 = 1$ kan vi sette inn $y^2 = 1 - x^2$ i uttrykket for $f(x, y)$, det vil si,

$$f(x, y) = x^3 + x^2 + x - y^2 = x^3 + x^2 + x - (1 - x^2) = x^3 + 2x^2 + x - 1.$$

La $g(x) = x^3 + 2x^2 + x - 1$ for $-1 \leq x \leq 1$. Vi undersøker verdien av $g(x)$ i endepunktene; $g(-1) = -1$ og $g(1) = 3$. Siden $g'(x) = 3x^2 + 4x + 1 = (3x + 1)(x + 1)$, har $g(x)$ et kritisk punkt i $x = -1/3$ ($x = -1$ er allerede behandlet som et endepunkt), der $g(-1/3) = -1/27 + 2/9 - 1/3 - 1 = -31/27$.

Sirkelen $x^2 + y^2 = 1$ er en lukket og begrenset mengde, og $f$ er kontinuerlig, så $f$ må ha en største og en minste verdi på kurven. Disse må være blant punktene vi har funnet, og vi slutter at minste verdi av $f(x, y)$ er $-31/27$ på $x^2 + y^2 = 1$ og største verdi av $f(x, y)$ er $3$ på $x^2 + y^2 = 1$.

Kildesett: course=TMA4105 term=sommer year=2019 problem=2 file=tma4105_2019k_web.pdf
