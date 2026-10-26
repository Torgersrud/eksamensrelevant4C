### **Løsning til Oppgave 6**

**a)** Vi observerer at $\mathbf{v}_2$ og $\mathbf{v}_3$ allerede er ortogonale. Vi setter derfor $\mathbf{u}_1 = \mathbf{v}_2 = (2,1,0,-2)$ og $\mathbf{u}_2 = \mathbf{v}_3 = (2,0,-1,2)$. Gram-Schmidt gir da den siste vektoren

$$\begin{aligned}
\tilde{\mathbf{u}}_3 &= \mathbf{v}_1 - \frac{\mathbf{v}_1 \cdot \mathbf{u}_1}{\mathbf{u}_1 \cdot \mathbf{u}_1} \mathbf{u}_1 - \frac{\mathbf{v}_1 \cdot \mathbf{u}_2}{\mathbf{u}_2 \cdot \mathbf{u}_2} \mathbf{u}_2\\
&= (1,1,-1,0) - \tfrac{3}{9}(2,1,0,-2) - \tfrac{3}{9}(2,0,-1,2) = (-\tfrac{1}{3}, \tfrac{2}{3}, -\tfrac{2}{3}, 0).
\end{aligned}$$

Ortogonal basis for $V = \mathrm{Span}\{\mathbf{v}_1, \mathbf{v}_2, \mathbf{v}_3\}$ er

$$\mathbf{u}_1 = (2,1,0,-2), \quad \mathbf{u}_2 = (2,0,-1,2), \quad \mathbf{u}_3 = (-1,2,-2,0).$$

**b)** Vi benytter at basisen i a) er ortogonal: Ortogonalprojeksjonen av $\mathbf{w} = (1,4,4,2)$ ned på underrommet $V$ er

$$\begin{aligned}
\mathbf{p} &= \frac{\mathbf{w} \cdot \mathbf{u}_1}{\mathbf{u}_1 \cdot \mathbf{u}_1} \mathbf{u}_1 + \frac{\mathbf{w} \cdot \mathbf{u}_2}{\mathbf{u}_2 \cdot \mathbf{u}_2} \mathbf{u}_2 + \frac{\mathbf{w} \cdot \mathbf{u}_3}{\mathbf{u}_3 \cdot \mathbf{u}_3} \mathbf{u}_3\\
&= \tfrac{2}{9}(2,1,0,-2) + \tfrac{2}{9}(2,0,-1,2) - \tfrac{1}{9}(-1,2,-2,0) = (1,0,0,0).
\end{aligned}$$

*Kjeldevarsel: lausningsarket `lftma4115aug08.pdf` er typesett bokmål («TMA 4110/4115 Matematikk 3 eksamen 14. august 2008, Løsningsforslag», 4 sider) utan tekstlag, og dekkjer Oppgave 1-7; arket har typo i felten på alle sider: datoen er skriven «1. august 2008» medan eksamen er 14. august 2008 — varsla, elles ingen saklege skrivefeil funne; arket gjenbrukar ikkje oppgåveteksten under delhovuda; observasjonen v2·v3=0, Gram-Schmidt-vektorn ũ3=(-1/3,2/3,-2/3,0), den skalerte u3=(-1,2,-2,0), koeffisientane 2/9, 2/9, -1/9 og projeksjonen p=(1,0,0,0) er kontrollreikna med sympy (restvektorn w-p=(0,4,4,2) står ortogonalt på v1, v2 og v3).*

Kildesett: course=TMA4110 term=kont year=2008 problem=6 file=tma4115aug08.pdf
