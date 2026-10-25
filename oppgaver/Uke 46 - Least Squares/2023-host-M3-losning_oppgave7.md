### **Løsning til Oppgave 7**

- Siden $\mathrm{Col}\,A$ har ortogonal basis $\{u_1,u_2,u_3\}$, får vi at projeksjonen blir

$$\begin{aligned}\widehat{\boldsymbol{b}}=P_{\mathrm{Col}\,A}(\boldsymbol{b})&=\frac{\langle\boldsymbol{b},\boldsymbol{u}_1\rangle}{\langle\boldsymbol{u}_1,\boldsymbol{u}_1\rangle}\boldsymbol{u}_1+\frac{\langle\boldsymbol{b},\boldsymbol{u}_2\rangle}{\langle\boldsymbol{u}_2,\boldsymbol{u}_2\rangle}\boldsymbol{u}_2+\frac{\langle\boldsymbol{b},\boldsymbol{u}_3\rangle}{\langle\boldsymbol{u}_3,\boldsymbol{u}_3\rangle}\boldsymbol{u}_3\\ &=\frac{0}{4}\boldsymbol{u}_1+\frac{-2}{4}\boldsymbol{u}_2+\frac{0}{4}\boldsymbol{u}_3\\[4pt] &=\frac{1}{2}\begin{bmatrix}-1\\ 1\\ 1\\ -1\end{bmatrix}.\end{aligned}$$

- Minste-kvadratsløsningen til det overbestemte systemet $A\boldsymbol{x}=\boldsymbol{b}$ er løsningen $\widehat{\boldsymbol{x}}$ på systemet $A\boldsymbol{x}=\widehat{\boldsymbol{b}}$, siden $\widehat{\boldsymbol{b}}$ er vektoren i $\mathrm{Col}\,A$ som minimerer avstanden til $\boldsymbol{b}$. Gausseliminasjon gir at

$$\bigl[A\ \big|\ \widehat{\boldsymbol{b}}\bigr]=\left[\begin{array}{ccc|c}1&3&5&-1/2\\ 1&1&0&1/2\\ 1&1&2&1/2\\ 1&3&3&-1/2\end{array}\right]\sim\left[\begin{array}{ccc|c}1&0&0&1\\ 0&1&0&-1/2\\ 0&0&1&0\\ 0&0&0&0\end{array}\right],$$

så $\widehat{\boldsymbol{x}}=\left(1,-\frac{1}{2},0\right)$. Alternativt kan man løse normallikningene $A^{\top}A\boldsymbol{x}=A^{\top}\boldsymbol{b}$ direkte, men det blir mer arbeidsomt.

Kildesett: course=TMA4110 term=host year=2023 problem=7 file=tma4110_2023h_nb.pdf
