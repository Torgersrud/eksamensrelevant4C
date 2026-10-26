### **Løsning til Oppgave 5**

**a)** Matrisa til ligningssystemet er

$$A = \begin{bmatrix} 1 & 1 & -1 & 1\\ 1 & 2 & -2 & 1 \end{bmatrix},$$

etter Gauss-eliminasjon blir det

$$\begin{bmatrix} 1 & 1 & -1 & 1\\ 1 & 2 & -2 & 1 \end{bmatrix} \to \begin{bmatrix} 1 & 0 & 0 & 1\\ 0 & 1 & -1 & 0 \end{bmatrix} = B.$$

Systemet blir $x_1 + x_4 = 0$, $x_2 + x_3 = 0$, så

$$\begin{bmatrix} x_1\\ x_2\\ x_3\\ x_4 \end{bmatrix} = z \begin{bmatrix} 0\\ 1\\ 1\\ 0 \end{bmatrix} + w \begin{bmatrix} -1\\ 0\\ 0\\ 1 \end{bmatrix}.$$

En basis for $V$ er $\{(0,1,1,0), (-1,0,0,1)\}$ som også er ortogonal. Sett $v_1 = (0,1,1,0)$, $v_2 = (-1,0,0,1)$.

**b)** Den ortogonale projeksjonen blir

$$p = \frac{b \cdot v_1}{v_1 \cdot v_1} v_1 + \frac{b \cdot v_2}{v_2 \cdot v_2} v_2 = \frac{2}{2}(0,1,1,0) + \frac{0}{2}(-1,0,0,1) = (0,1,1,0).$$

**c)** Vi har $V = \mathrm{Null}(A)$ så $V^{\perp} = \mathrm{Row}(A) = \mathrm{Row}(B)$ og $v_3 = (1,0,0,1)$ og $v_4 = (0,-1,1,0)$ gir en ortogonal basis for $V^{\perp}$; $\{v_1, v_2, v_3, v_4\}$ er da ortogonal basis for $R^4$ som ønsket.

*Kjeldevarsel: lausningsarket `lftma4110des10.pdf` er typesett bokmål («Løsningsforslag», 6 sider) og dekkjer alle 12 delpunkta; arket gjentek oppgåveteksten under kvart delhovud — dei gjentekne partane er utelatte her sidan dei allereie står i oppgåvefila; notasjonen $R^4$ med vanleg kursiv R (ikkje dobbelstreka) følgjer både eksamen og ark; Gauss-eliminasjonen, den ortogonale basisen $(0,1,1,0)$ og $(-1,0,0,1)$, projeksjonen $p = (0,1,1,0)$ og at firetalssettet i c) er parvis ortogonalt, er kontrollreikna med sympy (restvektoren $b - p = (1,0,0,1)$ står ortogonalt på begge basisvektorane i $V$).*

Kildesett: course=TMA4110 term=host year=2010 problem=5 file=tma4110des10.pdf
