### **Løsning til Oppgave 5**

**a)** Vi lar $S_1$ betegne flaten $z + \frac{\pi}{4} - \arctan \frac{y}{x} = 0$ og $S_2$ betegne flaten $x^2 + y^2 - z - 2 = 0$. Vektoren $\mathbf{v} = [3, -5, -4]$ er en tangentvektor til $C$ i punktet $(1, 1, 0)$ hvis og bare hvis $\mathbf{v}$ står normalt både på en normalvektor $\mathbf{N}_1$ til $S_1$ i $(1, 1, 0)$ og en normalvektor $\mathbf{N}_2$ til $S_2$ i $(1, 1, 0)$.

$$\mathbf{N}_1 = \nabla \left. \left( z + \frac{\pi}{4} - \arctan \frac{y}{x} \right) \right|_{(1,1,0)} = \left[ -\frac{1}{1 + (y/x)^2} \left( -\frac{y}{x^2} \right), \; -\frac{1}{1 + (y/x)^2} \cdot \frac{1}{x}, \; 1 \right]_{(1,1,0)} = \left[ \frac{1}{2}, -\frac{1}{2}, 1 \right]$$

$$\mathbf{N}_2 = \nabla \left. (x^2 + y^2 - z - 2) \right|_{(1,1,0)} = [2x, 2y, -1]_{(1,1,0)} = [2, 2, -1].$$

Vi har at $\mathbf{N}_1 \perp \mathbf{v}$ og $\mathbf{N}_2 \perp \mathbf{v}$ hvis og bare hvis $\mathbf{N}_1 \cdot \mathbf{v} = 0$ og $\mathbf{N}_2 \cdot \mathbf{v} = 0$. Her er

$$\mathbf{N}_1 \cdot \mathbf{v} = \left[ \tfrac{1}{2}, -\tfrac{1}{2}, 1 \right] \cdot [3, -5, -4] = \tfrac{3}{2} + \tfrac{5}{2} - 4 = 0$$

$$\mathbf{N}_2 \cdot \mathbf{v} = [2, 2, -1] \cdot [3, -5, -4] = 6 - 10 + 4 = 0.$$

Altså er $\mathbf{v}$ en tangentvektor.

**b)** Ballongen går i retningen $[3, -5, -4]$ gjennom punktet $(1, 1, 0)$ (den følger kurven med økende $x$-koordinat, og $x$-komponenten i tangentvektoren er positiv). Temperaturendringen per lengdeenhet idet den passerer punktet, er derfor den retningsderiverte av $T(x, y, z)$ i retningen $[3, -5, -4]$ i punktet $(1, 1, 0)$.

$$\mathbf{u} = \frac{[3, -5, -4]}{|[3, -5, -4]|} = \frac{[3, -5, -4]}{\sqrt{9 + 25 + 16}} = \frac{[3, -5, -4]}{5\sqrt{2}}.$$

$$D_{\mathbf{u}} T(x, y, z) = \nabla T(x, y, z) \cdot \mathbf{u} = \left[ \frac{1}{1 + z^2}, \frac{-1}{1 + z^2}, -\frac{x - y}{(1 + z^2)^2} \cdot 2z \right] \cdot \mathbf{u}.$$

$$D_{\mathbf{u}} T(1, 1, 0) = [1, -1, 0] \cdot \frac{[3, -5, -4]}{5\sqrt{2}} = \frac{8}{5\sqrt{2}} = \frac{4}{5}\sqrt{2}.$$

Kildesett: course=TMA4105 term=sommer year=2004 problem=5 file=tma4105_04k.pdf
