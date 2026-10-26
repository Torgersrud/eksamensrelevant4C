### **Løsning til Oppgave 3**

**a)** De partielle deriverte til $f$ eksisterer over alt, så vi finner de kritiske punktene ved å løse $\frac{\partial f}{\partial x} = 0$ og $\frac{\partial f}{\partial y} = 0$. Nå er

$$\frac{\partial f}{\partial x} = \frac{1}{2}(x - 1), \qquad \frac{\partial f}{\partial y} = 2y,$$

så det eneste kritiske punktet er $(x, y) = (1, 0)$.

La $g(x, y) = x^2 + y^2 - 4$, slik at bibetingelsen kan skrives $g(x, y) = 0$. Vi finner gradientene

$$\nabla f = \left[ \tfrac{1}{2}(x - 1), \; 2y \right], \qquad \nabla g = [2x, \; 2y].$$

Siden $\nabla g \neq 0$ over alt hvor bibetingelsen $g(x, y) = 0$ er oppfylt, kan vi bruke Lagranges metode, og vi skal løse ligningssystemet $\nabla f = \lambda \nabla g$, $g(x, y) = 0$, som skrevet ut blir

$$\frac{1}{2}(x - 1) = 2\lambda x, \qquad 2y = 2\lambda y, \qquad x^2 + y^2 = 4.$$

Om vi multipliserer den første ligningen med $y$ og den andre med $x$, ser vi at

$$xy - y = 4xy,$$

som gir enten $y = 0$ eller $x = -1/3$. Hvis $y = 0$ gir bibetingelsen at $x = \pm 2$, og hvis $x = -1/3$ gir bibetingelsen $y = \pm \sqrt{35}/3$. Vi har derfor fire kandidater

$$(2, 0), \quad (-2, 0), \quad \left( -\frac{1}{3}, \; \frac{\sqrt{35}}{3} \right), \quad \left( -\frac{1}{3}, \; -\frac{\sqrt{35}}{3} \right)$$

for maksima eller minima på randen. Ved innsetting finner vi

$$f(2, 0) = \frac{1}{4}, \qquad f(-2, 0) = \frac{9}{4}, \qquad f\left( -\frac{1}{3}, \; \pm \frac{\sqrt{35}}{3} \right) = \frac{13}{3}.$$

Vi konkluderer med at $f$ oppnår sin største verdi $\dfrac{13}{3}$ på randen i de to punktene $\left( -\tfrac{1}{3}, \pm \tfrac{\sqrt{35}}{3} \right)$ og sin minste verdi $\dfrac{1}{4}$ i punktet $(2, 0)$.

**b)** I figuren i løsningsforslaget er randkurven $g(x, y) = 0$ markert med tykk strek, mens de tynne ellipsene er nivåkurver for $f$. Nivåkurvene til $f$ tangerer kurven $g(x, y) = 0$ i de fire punktene på randen, og det indre kritiske punkt $(1, 0)$ ligger i nivåkurvenes felles sentrum.

Siden absolutt maksimum og absolutt minimum må være et av de fem punktene vi har funnet i del (a), ser vi ved innsetting at $f$ oppnår sin **maksimalverdi $\mathbf{13/3}$** i de to punktene $\left( -\tfrac{1}{3}, \pm \tfrac{\sqrt{35}}{3} \right)$ (på randen av $D$), og sin **minimalverdi $0$** i punktet $(1, 0)$ (i det indre av $D$).

*Kjeldevarsel: løsningsforslaget oppgir i del (b) maksimalverdien $39/4$, men verdien i punktene $\left(-\tfrac{1}{3}, \pm\tfrac{\sqrt{35}}{3}\right)$ er $\tfrac{4}{9} + \tfrac{35}{9} = \tfrac{39}{9} = \tfrac{13}{3}$ — slik del (a) i samme løsningsforslag selv regner den ut. Korrekt global maksimalverdi er $13/3$; punktene og minimalverdi $0$ i $(1,0)$ er urørte.*

Kildesett: course=TMA4105 term=var year=2006 problem=3 file=tma4105_06v.pdf
