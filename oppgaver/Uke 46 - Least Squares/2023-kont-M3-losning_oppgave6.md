### **Løsning til Oppgave 6**

- Siden $\begin{bmatrix}1\\ 1\\ 1\end{bmatrix}\cdot\begin{bmatrix}0\\ 1\\ 2\end{bmatrix}=3\neq 0$, må vi konstruere en ortogonal basis for $V$. Gram–Schmidts metode gir en ortogonal basis $\{\boldsymbol{v}_1,\boldsymbol{v}_2\}$, hvor

$$\boldsymbol{v}_1=\begin{bmatrix}1\\ 1\\ 1\end{bmatrix}$$

og

$$\boldsymbol{v}_2=\begin{bmatrix}0\\ 1\\ 2\end{bmatrix}-\frac{\begin{bmatrix}0\\ 1\\ 2\end{bmatrix}\cdot\boldsymbol{v}_1}{\boldsymbol{v}_1\cdot\boldsymbol{v}_1}\,\boldsymbol{v}_1=\begin{bmatrix}0\\ 1\\ 2\end{bmatrix}-\frac{3}{3}\,\boldsymbol{v}_1=\begin{bmatrix}-1\\ 0\\ 1\end{bmatrix}.$$

- La $\boldsymbol{b}=\begin{bmatrix}3\\ -2\\ 1\end{bmatrix}$. Prosjeksjonen blir så

$$P_V(\boldsymbol{b})=P_{\boldsymbol{v}_1}(\boldsymbol{b})+P_{\boldsymbol{v}_2}(\boldsymbol{b})=\frac{\boldsymbol{b}\cdot\boldsymbol{v}_1}{\boldsymbol{v}_1\cdot\boldsymbol{v}_1}\boldsymbol{v}_1+\frac{\boldsymbol{b}\cdot\boldsymbol{v}_2}{\boldsymbol{v}_2\cdot\boldsymbol{v}_2}\boldsymbol{v}_2=\frac{2}{3}\begin{bmatrix}1\\ 1\\ 1\end{bmatrix}+\frac{-2}{2}\begin{bmatrix}-1\\ 0\\ 1\end{bmatrix}=\frac{1}{3}\begin{bmatrix}5\\ 2\\ -1\end{bmatrix}.$$

Kildesett: course=TMA4110 term=kont year=2023 problem=6 file=tma4115_2023k_nb.pdf
