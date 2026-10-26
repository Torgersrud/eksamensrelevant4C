### **Løsning til Oppgave 4**

**a)** Gausseliminasjon gir

$$A = \begin{bmatrix} 1 & -3 & 0 & 1 & 0\\ -2 & 6 & -2 & 0 & -3\\ 1 & -3 & 6 & -5 & 9 \end{bmatrix} \xrightarrow[2R_1+R_2]{-R_1+R_3} \begin{bmatrix} 1 & -3 & 0 & 1 & 0\\ 0 & 0 & -2 & 2 & -3\\ 0 & 0 & 6 & -6 & 9 \end{bmatrix} \xrightarrow{3R_2+R_3} \begin{bmatrix} 1 & -3 & 0 & 1 & 0\\ 0 & 0 & -2 & 2 & -3\\ 0 & 0 & 0 & 0 & 0 \end{bmatrix} = E.$$

Vi finner alle løsningene til ligningen $A\mathbf{x} = 0$. Med $x_2 = r$, $x_4 = s$ og $x_5 = t$ får vi $x_3 = s - 1{,}5t$ og $x_1 = 3r - s$. Generell løsning blir $(x_1, x_2, x_3, x_4, x_5) = (3,1,0,0,0)r + (-1,0,1,1,0)s + (0,0,-1{,}5,0,1)t$. Da er $\mathbf{u}_1 = (3,1,0,0,0)$, $\mathbf{u}_2 = (-1,0,1,1,0)$, $\mathbf{u}_3 = (0,0,-1{,}5,0,1)$ en basis for $\mathrm{Null}(A)$.

Ikkenullradene i $E$ gir en basis for $\mathrm{Row}(A)$, $\mathbf{r}_1 = (1,-3,0,1,0)$, $\mathbf{r}_2 = (0,0,-2,2,-3)$.

**b)** Kolonner til $A$ som tilsvarer til de ledendevariabler danner en basis for $\mathrm{Col}(A)$, vi får: $\mathbf{v}_1 = (1,-2,1)$, $\mathbf{v}_2 = (0,-2,6)$.

For å finne en basis for $\mathrm{Col}(A)^{\perp}$ skal vi løse systemet:

$$0 = \mathbf{v}_1 \cdot \mathbf{x} = x_1 - 2x_2 + x_3, \qquad 0 = \mathbf{v}_2 \cdot \mathbf{x} = -2x_2 + 6x_3.$$

Vi får $x_3 = a$, $x_2 = 3a$ og $x_1 = 5a$; $(x_1, x_2, x_3) = (5,3,1)a$. Basis for $\mathrm{Col}(A)^{\perp}$ blir $\mathbf{u} = (5,3,1)$.

**c)** Den ortogonale projeksjonen av $\mathbf{b}$ inn i $\mathrm{Col}(A)^{\perp}$ er

$$\mathbf{q} = \frac{\mathbf{b} \cdot \mathbf{u}}{\mathbf{u} \cdot \mathbf{u}} \mathbf{u} = \frac{35}{35} (5,3,1) = (5,3,1).$$

Da er den ortogonale projeksjonen av $\mathbf{b}$ inn i $\mathrm{Col}(A)$ lik $\mathbf{p} = \mathbf{b} - \mathbf{q} = (6,1,2) - (5,3,1) = (1,-2,1)$.

*Alternativt:* Vi finner en ortogonal basis for $\mathrm{Col}(A)$ ved å bruke Gramm-Schmidt på basisen $\mathbf{v}_1, \mathbf{v}_2$. Vi får $\mathbf{u}_1 = \mathbf{v}_1 = (1,-2,1)$ og $\mathbf{u}_2 = \mathbf{v}_2 - \frac{\mathbf{v}_2 \cdot \mathbf{u}_1}{\mathbf{u}_1 \cdot \mathbf{u}_1} \mathbf{u}_1 = (0,-2,6) - \frac{5}{3}(1,-2,1)$ og vi tar $\mathbf{u}_2 = (-5,4,13)$. Dette gir

$$\mathbf{p} = \frac{\mathbf{b} \cdot \mathbf{u}_1}{\mathbf{u}_1 \cdot \mathbf{u}_1} \mathbf{u}_1 + \frac{\mathbf{b} \cdot \mathbf{u}_2}{\mathbf{u}_2 \cdot \mathbf{u}_2} \mathbf{u}_2 = \mathbf{u}_1 = (1,-2,1).$$

*Alternativt:* La

$$C = \begin{bmatrix} 1 & 0\\ -2 & -2\\ 1 & 6 \end{bmatrix}.$$

Da har vi $\mathrm{Col}(A) = \mathrm{Col}(C)$. Vi finner den ortogonale projeksjon av $\mathbf{b}$ inn i $\mathrm{Col}(C)$ ved den minste kvadraters metodcn. Det tilhørende normallsystemet blir $C^T C \mathbf{x} = C^T \mathbf{b}$, dette er $\begin{bmatrix} 6 & 10\\ 10 & 40 \end{bmatrix} \mathbf{x} = \begin{bmatrix} 6\\ 10 \end{bmatrix}$ og vi finner løsningen $x_1 = 1$, $x_2 = 0$. Så får vi $\mathbf{p} = C\mathbf{x} = (1,-2,1)$.

*Kjeldevarsel: lausningsarket `lftma4110des09.pdf` er typesett bokmål («løsningsforslag», 7 sider) og dekkjer alle 12 delpunkta; arket gjentek oppgåveteksten under kvart delhovud — dei gjentekne partane er utelatte her sidan dei allereie står i oppgåvefila; arket skriv «Gramm-Schmidt» (vanleg rettskriving er Gram-Schmidt), «tilsvarer til de ledendevariabler», «metodcn» (typo for «metoden») og «normallsystemet» (normalsystemet) — alt er teke med ordrett; nullromsbasisvektorane, radromsbasisvektorane, kolonnebasisvektorane, u=(5,3,1), p=(1,-2,1), C^TC=[[6,10],[10,40]] og C^Tb=(6,10) er kontrollreikna med sympy (rref av A gir E, nullromsbasis svarer til arket, Col(A)-basis er søylene 1 og 3, komplementær vektor (5,3,1) står ortogonalt på begge kolonner, og b-(1,-2,1)=(5,3,1) står i Col(A)^⊥; alternativ Gram-Schmidt gir u2=(0,-2,6)-(5/3)(1,-2,1)=(-5/3,4/3,13/3) som er parallell med (-5,4,13), og minste kvadraters alternativ gir x=(1,0) og p=(1,-2,1)).*

Kildesett: course=TMA4110 term=host year=2009 problem=4 file=tma4110des09.pdf
