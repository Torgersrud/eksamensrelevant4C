### **Løsning til Oppgave 6**

**a)** Vi kan løse ligningssystemet ved Gauss-Jordaneliminasjon:

$$A = \begin{bmatrix} 1 & -2 & 1 & 0\\ 1 & 0 & -1 & 2 \end{bmatrix} \xrightarrow{(-1)R_1+R_2} \begin{bmatrix} 1 & -2 & 1 & 0\\ 0 & 2 & -2 & 2 \end{bmatrix} \xrightarrow[(\frac{1}{2})R_2]{(1)R_2+R_1} \begin{bmatrix} 1 & 0 & -1 & 2\\ 0 & 1 & -1 & 1 \end{bmatrix}.$$

Med $x_3 = s$ og $x_4 = t$ får vi $(x_1, x_2, x_3, x_4) = (s-2t, s-t, s, t) = s(1,1,1,0) + t(-2,-1,0,1)$. En basis for løsningsrommet er følgelig vektorene $\mathbf{u}_1 = (1,1,1,0)$ og $\mathbf{u}_2 = (-2,-1,0,1)$.

**b)** Vi skal finne den ortogonale projeksjonen $\mathbf{p}$ av $\mathbf{b} = (1,2,-3,1)$ inn i underrommet $V = \mathrm{span}\{\mathbf{v}_1, \mathbf{v}_2\}$. Siden $\mathbf{v}_1 = (1,-2,1,0)$ og $\mathbf{v}_2 = (1,0,-1,2)$ er ortogonale, får vi

$$\mathbf{p} = \left(\frac{\mathbf{b} \cdot \mathbf{v}_1}{\mathbf{v}_1 \cdot \mathbf{v}_1}\right) \mathbf{v}_1 + \left(\frac{\mathbf{b} \cdot \mathbf{v}_2}{\mathbf{v}_2 \cdot \mathbf{v}_2}\right) \mathbf{v}_2 = -\begin{bmatrix} 1\\ -2\\ 1\\ 0 \end{bmatrix} + \begin{bmatrix} 1\\ 0\\ -1\\ 2 \end{bmatrix} = \begin{bmatrix} 0\\ 2\\ -2\\ 2 \end{bmatrix}.$$

**c)** Vektorene $\mathbf{v}_1$ og $\mathbf{v}_2$ er radene i koeffisientmatrisen $A$ til ligningssystemet i **a)**. Følgelig må $\mathbf{v}_3$ og $\mathbf{v}_4$ være i det ortogonale komplementet $\mathrm{Row}(A)^{\perp}$. Siden $\mathrm{Row}(A)^{\perp} = \mathrm{Null}(A)$, kan vi finne $\mathbf{v}_3$ og $\mathbf{v}_4$ ved å bruke Gram-Schmidts ortogonaliseringsalgoritme på basisen $\mathbf{u}_1 = (1,1,1,0)$ og $\mathbf{u}_2 = (-2,-1,0,1)$ for $\mathrm{Null}(A)$:

$$\mathbf{v}_3 = \mathbf{u}_1 = (1,1,1,0), \qquad \mathbf{v}_4 = \mathbf{u}_2 - \left(\frac{\mathbf{u}_2 \cdot \mathbf{v}_3}{\mathbf{v}_3 \cdot \mathbf{v}_3}\right) \mathbf{v}_3 = \begin{bmatrix} -2\\ -1\\ 0\\ 1 \end{bmatrix} + \begin{bmatrix} 1\\ 1\\ 1\\ 0 \end{bmatrix} = \begin{bmatrix} -1\\ 0\\ 1\\ 1 \end{bmatrix}.$$

Vektorene $\mathbf{v}_1 = (1,-2,1,0)$, $\mathbf{v}_2 = (1,0,-1,2)$, $\mathbf{v}_3 = (1,1,1,0)$ og $\mathbf{v}_4 = (-1,0,1,1)$ er følgelig en ortogonal basis for $\mathbb{R}^4$.

*Kjeldevarsel: lausningsarket `lftma4110des07.pdf` er typesett bokmål («TMA4110 Matematikk 3, eksamen 3. desember 2007», 4 sider, filnamn i felten) og dekkjer Oppgave 1-7; arket gjenbrukar ikkje oppgåveteksten under delhovuda; ingen saklege skrivefeil funne; Gauss-Jordan-reduksjonen, nullromsbasis (1,1,1,0) og (-2,-1,0,1), projeksjonen p=(0,2,-2,2) (koeffisientar −1 og +1) og fjerde vektor v4=(-1,0,1,1) er kontrollreikna med sympy (rref svarer til arket; restvektor b-p=(1,0,-1,-1) står ortogonalt på både v1 og v2; dei fire vektorane er parvis ortogonale).*

Kildesett: course=TMA4110 term=host year=2007 problem=6 file=tma4110des07.pdf
