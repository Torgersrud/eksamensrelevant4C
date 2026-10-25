### **Løsning til Oppgave 5**

Vi skriver ned matrisen til systemet

$$A = \begin{bmatrix} 1 & 0 & 1\\ 1 & 2 & 3\\ 1 & -2 & -1\\ 0 & 4 & -1 \end{bmatrix}$$

og ser på normalsystemet $A^{T}A\mathbf{x} = A^{T}\mathbf{b}$. Vi får

$$\begin{bmatrix} 1 & 1 & 1 & 0\\ 0 & 2 & -2 & 4\\ 1 & 3 & -1 & -1 \end{bmatrix} \begin{bmatrix} 1 & 0 & 1\\ 1 & 2 & 3\\ 1 & -2 & -1\\ 0 & 4 & -1 \end{bmatrix} \begin{bmatrix} x\\ y\\ z \end{bmatrix} = \begin{bmatrix} 1 & 1 & 1 & 0\\ 0 & 2 & -2 & 4\\ 1 & 3 & -1 & -1 \end{bmatrix} \begin{bmatrix} 0\\ 5\\ 1\\ -1 \end{bmatrix}$$

som etter utregning blir

$$\begin{bmatrix} 3 & 0 & 3\\ 0 & 24 & 4\\ 3 & 4 & 12 \end{bmatrix} \begin{bmatrix} x\\ y\\ z \end{bmatrix} = \begin{bmatrix} 6\\ 4\\ 15 \end{bmatrix}.$$

Vi løser dette systemet ved hjelp av Gausseliminasjon og får $z = 1$, $y = 0$ og $x = 1$. Svaret er $(x,y,z) = (1,0,1)$.

*Kjeldevarsel: lausningsarket `lftma4110des2011.pdf` er typesett bokmål og dekkjer alle sju oppgåvene på fem sider; sidotelnedslina er inkonsekvent på arket («Side 1 av 5» på første side, men «Side 2 av 6»–«Side 5 av 6» på dei neste — PDF-en har fem sider). $A^{T}A = \begin{bmatrix} 3 & 0 & 3\\ 0 & 24 & 4\\ 3 & 4 & 12 \end{bmatrix}$, $A^{T}\mathbf{b} = (6,4,15)$ og løysinga $(x,y,z)=(1,0,1)$ er kontrollreikna med sympy; $A^{T}A$ er inverterbar, så minste kvadraters-løysinga er eintydig.*

Kildesett: course=TMA4110 term=host year=2011 problem=5 file=tma4110des11.pdf
