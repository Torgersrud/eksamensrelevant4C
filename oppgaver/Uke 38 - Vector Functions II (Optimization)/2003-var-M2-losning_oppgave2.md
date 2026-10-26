### **Løsning til Oppgave 2**

**a) Alternativ 1:** Vi tar hintet, og forsøker å minimalisere $f(x, y, z) = x^2 + y^2$ (som er kvadratet av avstanden til $z$-aksen) med bibetingelsene $g(x, y, z) = x^2 + y^2 - z - 1 = 0$ og $h(x, y, z) = xyz - 1 = 0$. Lagranges multiplikatormetode gir $\nabla f = \lambda \nabla g + \mu \nabla h$, som skrevet ut gir de tre ligningene

$$2x = 2\lambda x + \mu yz, \qquad 2y = 2\lambda y + \mu xz, \qquad 0 = -\lambda + \mu xy.$$

Den siste ligningen gir $\lambda = \mu xy$, som vi setter inn i de to første og får

$$2x = (2x^2 y + yz)\mu, \qquad 2y = (2xy^2 + xz)\mu.$$

Dette gir videre $2x(2xy^2 + xz) = 2y(2x^2 y + yz)$, altså $x^2 z = y^2 z$. Siden $x$, $y$ og $z$ alle er positive må $x = y$.

Setter vi inn $y = x$ i bibetingelsene $g = 0$ og $h = 0$, får vi $2x^2 - z = 1$ og $x^2 z = 1$. Den siste gir $x^2 = 1/z$ som vi setter inn i den første, og får $2/z - z = 1$. Multiplikasjon med $z$ og litt rydding gir annengradsligningen $z^2 + z - 2 = 0$, med løsninger gitt ved $z = \frac{1}{2}(-1 \pm 3)$. Siden $z > 0$ har vi bare løsningen $z = 1$. Dette gir $y = x = 1/\sqrt{z} = 1$, slik at $(x, y, z) = (1, 1, 1)$ er eneste mulige kandidat for det nærmeste punktet.

**Alternativ 2:** Vi legger merke til at den første flaten, med en ligning som kan skrives $x^2 + y^2 = 1 + z$, kan betraktes som unionen av en samling horisontale sirkler med sentrum på $z$-aksen og radius $\sqrt{1 + z}$. Vi finner altså det søkte punktet på den av disse sirklene med minst radius (minst $z$) som inneholder noe punkt på kurven $C$.

Det er mange mulige fremgangsmåter for å undersøke for hvilke verdier av $z$ denne sirkelen inneholder noe punkt fra $C$. Kanskje spesielt elegant er følgende:

Vi skriver ligningen for den andre flaten som $xy = 1/z$, multipliserer den med to og både legger den til og trekker den fra ligningen for den første flaten, som gir disse to ligningene:

$$(x + y)^2 = 1 + z + \frac{2}{z}, \qquad (x - y)^2 = 1 + z - \frac{2}{z}.$$

Spesielt må vi ha $1 + z - 2/z \geq 0$. Vi finner $1 + z - 2/z = 0$ når $z = 1$ (som i alternativ 1), og dermed blir $z = 1$ minste mulige $z$ som lar oss finne et slikt punkt vi søker. Ligningssystemet over får da løsningen $x = y = 1$.

**b) Alternativ 1:** De to flatene har normalvektorer gitt ved gradientene til henholdsvis $g$ og $h$ (der $g$ og $h$ er som i alternativ 1, punkt a). En tangentvektor til kurven må stå normalt på begge disse, så den er parallell med kryssproduktet

$$\nabla g \times \nabla h = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \\ 2x & 2y & -1 \\ yz & xz & xy \end{vmatrix} = (2xy^2 + xz)\,\mathbf{i} - (2x^2 y + yz)\,\mathbf{j} + (2x^2 z - 2y^2 z)\,\mathbf{k}.$$

Setter vi inn koordinatene til det gitte punktet, får vi

$$\nabla g \times \nabla h = (3 + \tfrac{1}{2}\sqrt{2})\,\mathbf{i} + (-3 + \tfrac{1}{2}\sqrt{2})\,\mathbf{j} + 8\sqrt{2}\,\mathbf{k}.$$

Hastighetsvektoren er parallell med denne og har $y$-komponent $1$, slik at vi må ha

$$\frac{dx}{dt} = \frac{3 + \frac{1}{2}\sqrt{2}}{-3 + \frac{1}{2}\sqrt{2}} = \frac{6 + \sqrt{2}}{-6 + \sqrt{2}} = -\frac{19 + 6\sqrt{2}}{17},$$

$$\frac{dz}{dt} = \frac{8\sqrt{2}}{-3 + \frac{1}{2}\sqrt{2}} = \frac{16\sqrt{2}}{-6 + \sqrt{2}} = -\frac{16 + 48\sqrt{2}}{17}.$$

(Her og i alternativ 2 nedenfor forenkles brøkene ved å multiplisere teller og nevner med $6 + \sqrt{2}$.)

**Alternativ 2:** Vi deriverer ligningene for de to flatene med hensyn på $t$. Med notasjonen $\dot{x} = dx/dt$ osv. får vi

$$2x\dot{x} + 2y\dot{y} - \dot{z} = 0, \qquad \dot{x}yz + x\dot{y}z + xy\dot{z} = 0.$$

Setter vi inn de gitte verdiene (heriblant $\dot{y} = 1$) får vi

$$(2 + \sqrt{2})\,\dot{x} + (2 - \sqrt{2}) - \dot{z} = 0, \qquad (2 - \sqrt{2})\,\dot{x} + (2 + \sqrt{2}) + \tfrac{1}{2}\dot{z} = 0.$$

Her kan vi for eksempel eliminere $\dot{z}$ ved å gange den siste ligningen med $2$ og addere, som gir

$$\frac{dx}{dt} = \dot{x} = -\frac{6 + \sqrt{2}}{6 - \sqrt{2}}$$

og videre

$$\frac{dz}{dt} = \dot{z} = (2 + \sqrt{2})\,\dot{x} + (2 - \sqrt{2}) = -\frac{16 + 48\sqrt{2}}{17}.$$

Kildesett: course=SIF5005 term=var year=2003 problem=2 file=sif5005_03v.pdf
