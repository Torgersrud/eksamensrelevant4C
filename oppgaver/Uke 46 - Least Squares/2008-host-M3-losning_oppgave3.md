### **Løsning til Oppgave 3**

**a)** Totalmatrisa blir

$$\begin{bmatrix} 1 & 2 & 1 & 0 & 2 & 3\\ 2 & 4 & 2 & 1 & 3 & 4\\ 5 & 10 & 5 & 1 & 9 & 13 \end{bmatrix}$$

som er rad-ekvivalent til

$$\begin{bmatrix} 1 & 2 & 1 & 0 & 2 & 3\\ 0 & 0 & 0 & 1 & -1 & -2\\ 0 & 0 & 0 & 0 & 0 & 0 \end{bmatrix}.$$

Dette gir løsning

$$\mathbf{x} = \begin{bmatrix} 3\\ 0\\ 0\\ -2\\ 0 \end{bmatrix} + \mathbf{t} \begin{bmatrix} -2\\ 0\\ 0\\ 1\\ 1 \end{bmatrix} + \mathbf{s} \begin{bmatrix} -1\\ 0\\ 1\\ 0\\ 0 \end{bmatrix} + \mathbf{u} \begin{bmatrix} -2\\ 1\\ 0\\ 0\\ 0 \end{bmatrix}, \quad \mathbf{t}, \mathbf{s}, \mathbf{u} \in \mathbb{R}.$$

**b)** Matrisa her er den samme som koeffisientmatrisa i a). Altså er en basis for $\mathrm{Null}(A)$ gitt ved (siden løsninga i a) er $\mathbf{x} = \mathbf{x}_p + \mathbf{x}_H$, der $\mathbf{x}_H$ er løsning på den homogene ligninga)

$$\begin{bmatrix} -2\\ 0\\ 0\\ 1\\ 1 \end{bmatrix}, \begin{bmatrix} -1\\ 0\\ 1\\ 0\\ 0 \end{bmatrix}, \begin{bmatrix} -2\\ 1\\ 0\\ 0\\ 0 \end{bmatrix},$$

basis for $\mathrm{Row}(A)$ leser vi av trappeformen som er er $[1\ 2\ 1\ 0\ 2]$, $[0\ 0\ 0\ 1\ -1]$, mens første og fjerde søyle i trappeformen har ledende element. D.v.s. første og fjerde søyle i A, $\begin{bmatrix} 1\\ 2\\ 5 \end{bmatrix}$ og $\begin{bmatrix} 0\\ 1\\ 1 \end{bmatrix}$ er en basis for $\mathrm{Col}(A)$.

**c)** La $C = \begin{bmatrix} 1 & 0\\ 2 & 1\\ 5 & 1 \end{bmatrix}$. Da er $\mathrm{Col}(A) = \mathrm{Col}(C)$. Den ortogonale projeksjonen av $\mathbf{b}$ inn i $\mathrm{Col}(C)$ er gitt ved $\mathbf{p} = C\overline{\mathbf{x}}$, der $\overline{\mathbf{x}}$ er løsninga på normaligninga $C^T C \overline{\mathbf{x}} = C^T \mathbf{b}$. Vi har

$$C^T C = \begin{bmatrix} 30 & 7\\ 7 & 2 \end{bmatrix} \ \text{og}\ C^T \mathbf{b} = \begin{bmatrix} 15\\ 2 \end{bmatrix}.$$

Dette gir $\overline{\mathbf{x}} = \begin{bmatrix} \frac{16}{11}\\[4pt] -\frac{45}{11} \end{bmatrix}$. Altså er

$$\mathbf{p} = C\overline{\mathbf{x}} = \frac{1}{11} \begin{bmatrix} 16\\ -13\\ 35 \end{bmatrix}.$$

*Kjeldevarsel: lausningsarket `lftma4110des08.pdf` er typesett bokmål («Løsningsforslag for eksamen i TMA4110, Matematikk 3, 4. desember 2008», 6 sider, Word-filsti i felten) og dekkjer alle 12 delpunkta; arket inneheld ikkje gjenteken oppgåvetekst under delhovuda; arket skriv «normaligninga» (normallikninga) og ei dobbel «er» etter «trappeformen som» — teke med ordrett; totalmatrisereduksjonen, løysingsvektorane, nullromsbasis, radromsbasis, kolonnebasis (søylene 1 og 4), C^TC=[[30,7],[7,2]], C^Tb=(15,2), x̄=(16/11,−45/11) og p=(16,−13,35)/11 er kontrollreikna med sympy (rang 2, nullromsbasis som arket, restvektorn b−p=(6,2,−2)/11 står ortogonalt på begge kolonnebasisvektorane).*

Kildesett: course=TMA4110 term=host year=2008 problem=3 file=tma4110des08.pdf
