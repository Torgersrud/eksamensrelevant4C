### **Løsning til Oppgave 7**

Projeksjonen $P_{\mathbf{v}}(\mathbf{w})$ av $\mathbf{w}$ på $\mathbf{v}$ er definert som

$$P_{\mathbf{v}}(\mathbf{w})=\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}.\tag{1}$$

At $P_{\mathbf{v}}(\mathbf{w})$ er en lineærtransform følger essensielt av det faktum at skalarproduktet er lineært i andre faktor. For å se at skalarproduktet er lineært i andre faktor, må vi vise at

$$\mathbf{v}\cdot(a\mathbf{w}+b\mathbf{u})=a\mathbf{v}\cdot\mathbf{w}+b\mathbf{v}\cdot\mathbf{u}.\tag{2}$$

Husk at $\mathbf{v}\cdot\mathbf{w}$ er matriseproduktet $\mathbf{v}^{\top}\mathbf{w}$. Det er med andre ord lineærtransformasjonen som er gitt av $1\times n$-matrisen $\mathbf{v}^{\top}$. Dette gir automatisk at skalarproduktet er lineært, fordi matriseproduktet er distributivt.

Nå er det rett frem å vise at projeksjonen på $\mathbf{v}$ er en lineærtransformasjon:

$$\begin{aligned}P_{\mathbf{v}}(a\mathbf{w}+b\mathbf{u})&=\frac{\mathbf{v}\cdot(a\mathbf{w}+b\mathbf{u})}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}\\
&=\frac{a\mathbf{v}\cdot\mathbf{w}+b\mathbf{v}\cdot\mathbf{u}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}\\
&=a\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}+b\frac{\mathbf{v}\cdot\mathbf{u}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}\\
&=aP_{\mathbf{v}}(\mathbf{w})+bP_{\mathbf{v}}(\mathbf{u}).\end{aligned}$$

Til slutt viser vi at $P_{\mathbf{v}}(\mathbf{w})$ og $\mathbf{w}-P_{\mathbf{v}}(\mathbf{w})$ er ortogonale:

$$\begin{aligned}P_{\mathbf{v}}(\mathbf{w})\cdot(\mathbf{w}-P_{\mathbf{v}}(\mathbf{w}))=&\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}\cdot\bigl(\mathbf{w}-\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}\bigr)\\
=&\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}\cdot\mathbf{w}-\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}\cdot\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}\\
=&\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}\cdot\mathbf{w}-\bigl(\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\bigr)\bigl(\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\bigr)\mathbf{v}\cdot\mathbf{v}\\
=&\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}\cdot\mathbf{w}-\frac{\mathbf{v}\cdot\mathbf{w}}{\mathbf{v}\cdot\mathbf{v}}\mathbf{v}\cdot\mathbf{w}\\
=&0.\end{aligned}$$

*Kjeldevarsel: identiteten $P_{\mathbf{v}}(\mathbf{w})\cdot(\mathbf{w}-P_{\mathbf{v}}(\mathbf{w}))=0$ og lineariteten til $P_{\mathbf{v}}$ er kontrollrekna symbolt med sympy.*

Kildesett: course=TMA4110 term=kont year=2019 problem=7 file=TMA4110_TMA4115_kont_sommer2019_bokmaal.pdf
