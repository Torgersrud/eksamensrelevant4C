### **Løsning til Oppgave 3**

Vi kaller basisvektorene for $\mathbf{e}_1$ og $\mathbf{e}_2$. Den første finner vi ved å normalisere $\mathbf{u}$, vi beregner derfor først $\|\mathbf{u}\|=\sqrt{2^2+2^2+1^2}=3$. Vi finner

$$\mathbf{e}_1=\frac{\mathbf{u}}{\|\mathbf{u}\|}=\begin{bmatrix}2/3\\ 2/3\\ 1/3\end{bmatrix}.$$

Så bruker vi Gram–Schmidt til å beregne en vektor $\mathbf{w}$ som er ortogonal på $\mathbf{e}_1$ ved

$$\mathbf{w}=v-(\mathbf{e}_1\cdot\mathbf{v})\mathbf{e}_1=\begin{bmatrix}4\\ 1\\ -1\end{bmatrix}-\Bigl(\frac{2}{3}\cdot 4+\frac{2}{3}\cdot 1+\frac{1}{3}\cdot(-1)\Bigr)\begin{bmatrix}2/3\\ 2/3\\ 1/3\end{bmatrix}=\begin{bmatrix}2\\ -1\\ -2\end{bmatrix}.$$

Vi har $\|w\|=3$ og skalerer for å finne

$$\mathbf{e}_2=\frac{w}{\|w\|}=\begin{bmatrix}2/3\\ -1/3\\ -2/3\end{bmatrix}.$$

Projeksjonsmatrisen $[P_U]$ finnes ved

$$[P_U]=\begin{bmatrix}2/3&2/3\\ 1/3&-1/3\\ 1/3&-2/3\end{bmatrix}\cdot\begin{bmatrix}2/3&2/3&1/3\\ 2/3&-1/3&-2/3\end{bmatrix}=\begin{bmatrix}8/9&2/9&-2/9\\ 2/9&5/9&4/9\\ -2/9&4/9&5/9\end{bmatrix}.$$

*Kjeldevarsel: den ortonormale basisen $\{\mathbf{e}_1,\mathbf{e}_2\}$ og projeksjonsmatrisa er kontrollrekna med sympy; matrisa er symmetrisk, idempotent og har spor 2, som ho skal for ein projeksjon ned på eit 2-dimensjonalt underrom. Oppgåva er frå skriftleg del (del 2) av eksamen.*

Kildesett: course=TMA4110 term=host year=2022 problem=3 file=tma4110_2022h_nb.pdf
