### **Løsning til Oppgave 4**

Ligningene skrives på matriseform som $Ax=b$ der

$$A=\begin{bmatrix}1&2\\ 3&4\\ 4&6\end{bmatrix},\quad b=\begin{bmatrix}1\\ 2\\ 3\end{bmatrix}.$$

Den tilnærmede løsningen oppfyller normalligningene $A^TAx=A^Tb$ som vi finner er

$$\begin{bmatrix}26&38\\ 38&56\end{bmatrix}\cdot\begin{bmatrix}x\\ y\end{bmatrix}=\begin{bmatrix}19\\ 28\end{bmatrix}.$$

Dette løses på vanlig måte, og en får $x=0$, $y=\frac{1}{2}$. Setter vi denne tilnærmede løsningen tilbake i det opprinnelige systemet finner vi at den eksakt oppfyller ligningene, siden høyresiden $b$ er nøyaktig lik $\frac{1}{2}$ multiplisert med $A$ sin andre kolonne.

*Kjeldevarsel: $A^TA$, $A^Tb$, løysinga $x=0$, $y=\frac{1}{2}$ og at $A\hat{x}=b$ (løysinga dusman eksakt) er kontrollrekna med sympy.*

Kildesett: course=TMA4110 term=kont year=2022 problem=4 file=EksamenTMA4110-15Kont.pdf
