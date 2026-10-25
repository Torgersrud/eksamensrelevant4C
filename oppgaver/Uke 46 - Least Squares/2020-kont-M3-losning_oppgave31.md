### **Løsning til Oppgave 31**

I denne oppgaven skal vi avgjøre hvilken rett linje $y=cx+d$ som passer best til punktene. Hvis det fantes en rett linje gjennom alle punktene, kunne vi funnet $c,d\in\mathbb{R}$ slik at

$$\begin{bmatrix}-1&1\\ 0&1\\ 2&1\end{bmatrix}\begin{bmatrix}c\\ d\end{bmatrix}=\begin{bmatrix}0\\ 1\\ 2\end{bmatrix}.$$

Siden det ikke finnes en rett linje gjennom alle punktene, er det beste vi kan gjøre å finne en linje som minimerer avstanden til alle punktene. Det gjør vi ved å bruke minste kvadraters metode på

$$A=\begin{bmatrix}-1&1\\ 0&1\\ 2&1\end{bmatrix}\quad\text{og}\quad\mathbf{b}=\begin{bmatrix}0\\ 1\\ 2\end{bmatrix}.$$

Vi beregner

$$A^TA=\begin{bmatrix}-1&0&2\\ 1&1&1\end{bmatrix}\begin{bmatrix}-1&1\\ 0&1\\ 2&1\end{bmatrix}=\begin{bmatrix}5&1\\ 1&3\end{bmatrix}\quad\text{og}\quad A^T\mathbf{b}=\begin{bmatrix}-1&0&2\\ 1&1&1\end{bmatrix}\begin{bmatrix}0\\ 1\\ 2\end{bmatrix}=\begin{bmatrix}4\\ 3\end{bmatrix}.$$

Vi radreduserer så totalmatrisen til ligningssystemet $(A^TA)\mathbf{x}=A^T\mathbf{b}$:

$$\left[\begin{array}{cc|c}5&1&4\\ 1&3&3\end{array}\right]\sim\left[\begin{array}{cc|c}1&0&9/14\\ 0&1&11/14\end{array}\right].$$

Linjen er altså $y=\frac{9}{14}x+\frac{11}{14}$.

*Kjeldevarsel: $A^{\top}A$, $A^{\top}\mathbf{b}$ og løysinga $c=\frac{9}{14}$, $d=\frac{11}{14}$ er kontrollrekna med sympy — alternativa i oppgåva er gitne med $c$ og $d$ motte (rettsvar er tredje alternativ).*

Kildesett: course=TMA4110 term=kont year=2020 problem=31 file=TMA4110_TMA4115_kont_2020_bokmaal.pdf
