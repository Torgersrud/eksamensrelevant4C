### **Løsning til Oppgave 1**

Vi introduserer funksjonen $g(x, y, z) = x^2 + 2y^2 - z^2$ slik at flaten $z^2 = x^2 + 2y^2$ er gitt ved $g(x, y, z) = 0$. I dette tilfellet utgjør gradienten til $g$ en normalvektor til flaten. Vi har

$$\nabla g = [2x, \; 4y, \; -2z] \tag{1}$$

og, i punktet $P$, er $\mathbf{N} = [2, 8, -6]$ en normalvektor. Et punkt $M$ med koordinater $[x, y, z]$ tilhører tangentplanet hvis og bare hvis vektoren $\vec{PM}$ er perpendikulær på $\mathbf{N}$, dvs. $\vec{PM} \cdot \mathbf{N} = 0$. Derfor er tangentplanet gitt ved

$$2(x - 1) + 8(y - 2) - 6(z - 3) = 0,$$

som gir

$$2x + 8y - 6z = 0.$$

Et punkt $M$ med koordinater $[x, y, z]$ som har det samme tangentplanet som $P$, må ha sin normalvektor paralell til $\mathbf{N}$. Derfor må vi ha $\nabla g \times \mathbf{N} = 0$. Fra (1) får vi

$$\nabla g \times \mathbf{N} = [16z - 24y, \; -4z + 12x, \; -8y + 16x].$$

Betingelsen gir da 3 ligninger, men bare 2 av dem er uavhengige:

$$z = 3x, \qquad y = 2x.$$

Det er lett å sjekke at alle punktene som tilfredsstiller disse to betingelsene tilfredsstiller både tangentplanlikningen og $g(x, y, z) = 0$. Alle disse punktene, som dessuten utgjør en rett linje (generatrisen $\{(t, 2t, 3t)\}$ gjennom $P$), har altså det samme tangentplanet som $P$.

*Kjeldevarsel: løsningsforslaget seier at «alle disse punktene» på linja har det same tangentplanet som $P$; unntaket er origo $t = 0$, der $\nabla g = 0$ og kjeglespissen ikkje har noko tangentplan i det heile.*

Kildesett: course=TMA4105 term=sommer year=2005 problem=1 file=tma4105_05k.pdf
