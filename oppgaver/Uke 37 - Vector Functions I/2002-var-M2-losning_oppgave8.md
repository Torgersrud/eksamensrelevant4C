### **Løsning til Oppgave 8**

Implisitt derivasjon der vi antar at $x$ og $u$ er frie variabler og $t$ er en funksjon av $x$ og $u$ gir (hvor uttrykket i hakeparentesen er den partiellderiverte av uttrykket med hensyn på $t$, og leddene til venstre er de partiellderiverte med hensyn på henholdsvis $x$ og $u$):

$$2x + \left[ \ln u + \tfrac{1}{2} \big( \ln(\pi t) + 1 \big) \right] \frac{\partial t}{\partial x} = 0, \qquad \frac{t}{u} + \left[ \ln u + \tfrac{1}{2} \big( \ln(\pi t) + 1 \big) \right] \frac{\partial t}{\partial u} = 0.$$

Her er det best å sette inn de gitte verdiene $x = 1$, $t = 1$ og $u = 1/(e\sqrt{\pi})$ jo før jo heller. Siden $\ln u = -1 - \frac{1}{2} \ln \pi$ blir innholdet i hakeparentesen lik $-\frac{1}{2}$, og dermed ender vi med

$$\frac{\partial t}{\partial x} = 4, \qquad \frac{\partial t}{\partial u} = 2e\sqrt{\pi} \approx 9{,}636,$$

vel og merke kun i det gitte punktet. Vi finner videre

$$t(1{,}1;\, 0{,}2) \approx t\big(1,\, 1/(e\sqrt{\pi})\big) + \frac{\partial t}{\partial x} \cdot (1{,}1 - 1) + \frac{\partial t}{\partial u} \cdot \big(0{,}2 - 1/(e\sqrt{\pi})\big) \approx 1 + 4 \cdot 0{,}1 + 9{,}636 \cdot (-0{,}008) \approx 1{,}323.$$

*Merknad for de nysgjerrige:* Ligningen i oppgave 8 oppstår naturlig ved studiet av varmeledning. Ved en passe skalering kan varmeledningsligningen i én romdimensjon skrives $\frac{\partial u}{\partial t} = \frac{1}{4} \frac{\partial^2 u}{\partial x^2}$. En bestemt løsning av denne, som beskriver effekten av en plutselig, lokalisert tilførsel av en enhet energi i origo ved tid $t = 0$, kan skrives på formen $u = e^{-x^2/t}/\sqrt{\pi t}$. Tar vi logaritmen og rydder litt får vi formelen oppgitt i oppgaven. Å skrive $t$ som en funksjon av $x$ og $u$ svarer til å stille spørsmålet: Hvor lang tid tar det i punktet $x$ før temperaturen er steget med $u$?

Kildesett: course=SIF5005 term=var year=2002 problem=8 file=sif5005_02v.pdf
