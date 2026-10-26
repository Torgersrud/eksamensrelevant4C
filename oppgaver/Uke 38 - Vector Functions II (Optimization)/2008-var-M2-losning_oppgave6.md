### **Løsning til Oppgave 6**

Vi setter opp variablene på de tre sidene av lagerteltet, som vist på figuren (bredd $2a$, lengde $b$, høgd $c$; gavlen er et rektangel med en halvsirkel med radius $a$ oppå).

Volumet av lagerteltet er da

$$V = f(a, b, c) = 2a \cdot b \cdot c + \frac{1}{2}\pi a^2 \cdot b = 2abc + \frac{1}{2}\pi a^2 b$$

og overflaten av teltet (inkludert bunn) er

$$A = g(a, b, c) = 2a \cdot b + 2 \cdot (2a) \cdot c + 2 \cdot b \cdot c + 2 \cdot \frac{1}{2}\pi a^2 + \frac{1}{2} \cdot 2\pi a \cdot b.$$

Vi vil finne maksimum for $V$ under betingelsen av at $A = 20$. Vi bruker Lagranges multiplikatormetode som gir ligningene

$$\nabla f(a, b, c) = \lambda \nabla (g(a, b, c) - 20), \qquad g(a, b, c) = 20$$

Det vil si, vi har de ligningene

$$\text{(1)} \quad 2bc + \pi ab = \lambda(2b + 4c + 2\pi a + \pi b)$$

$$\text{(2)} \quad 2ac + \frac{1}{2}\pi a^2 = \lambda(2a + 2c + \pi a)$$

$$\text{(3)} \quad 2ab = \lambda(4a + 2b)$$

$$\text{(4)} \quad (2 + \pi)ab + 4ac + 2bc + \pi a^2 = 20$$

Det er klart at i et maksimumpunkt kan verken $a$, $b$ eller $c$ være lik null. Derfor ser vi av ligning (3) at $4a + 2b \neq 0$, slik at

$$\lambda = \frac{2ab}{4a + 2b}.$$

Innsatt i (1) gir dette

$$(4a + 2b)(2bc + \pi ab) = (2b + 4c + 2\pi a + \pi b) \cdot 2ab$$

$$4b^2 c = 4ab^2, \qquad a = c.$$

Innsatt i (2) gir dette

$$(2ac + \frac{1}{2}\pi a^2)(4a + 2b) = (2a + 2c + \pi a) \cdot 2ab$$

$$(2c^2 + \frac{1}{2}\pi c^2)(4c + 2b) = (4c + \pi c) \cdot 2cb$$

$$(8 + 2\pi)c = 4b + \pi b, \qquad b = 2c.$$

Innsatt i (4) gir dette

$$(2 + \pi) \cdot 2c^2 + 4c^2 + 4c^2 + \pi c^2 = 20$$

$$c^2(12 + 3\pi) = 20$$

$$c = \sqrt{\frac{20}{3(4 + \pi)}} = 2\sqrt{\frac{5}{3(4 + \pi)}}.$$

Målene på teltet er derfor (med den valgte notasjonen her):

$$a = 2\sqrt{\frac{5}{3(4 + \pi)}}, \qquad b = 4\sqrt{\frac{5}{3(4 + \pi)}}, \qquad c = 2\sqrt{\frac{5}{3(4 + \pi)}}.$$

*Kjeldevarsel: løsningsforslaget oppgir ikkje ei kontroll av at den kritiske løysinga faktisk gir maksimum (verken andreversjonstest eller kompaktheitsargument); grensetilfella der ei sidelengd går mot null gir volum 0, og overflatelikninga binds av ei kompakt flate, slik at maksimum finst — den eine kritiske løysinga må då vere det.*

Kildesett: course=TMA4105 term=var year=2008 problem=6 file=tma4105_08v.pdf
