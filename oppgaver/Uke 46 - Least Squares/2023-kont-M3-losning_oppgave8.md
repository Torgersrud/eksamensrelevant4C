### **Løsning til Oppgave 8**

La

$$A=\begin{bmatrix}1&-1&1\\ 0&0&1\\ 1&1&1\\ 4&2&1\end{bmatrix},\qquad \boldsymbol{x}=\begin{bmatrix}a\\ b\\ c\end{bmatrix}\qquad\text{og}\qquad \boldsymbol{b}=\begin{bmatrix}1\\ -2\\ 0\\ 5\end{bmatrix}.$$

Fra tabellen må koeffisientene til $p$ tilfredsstille systemet

$$A\boldsymbol{x}=\begin{bmatrix}p(-1)\\ p(0)\\ p(1)\\ p(2)\end{bmatrix}=\boldsymbol{b}$$

Minste kvadraters-løsningen består da i å løse $A^{\top}A\boldsymbol{x}=A^{\top}\boldsymbol{b}$, med andre ord løse

$$\begin{bmatrix}18&8&6\\ 8&6&2\\ 6&2&4\end{bmatrix}\boldsymbol{x}=\begin{bmatrix}21\\ 9\\ 4\end{bmatrix}.$$

Gausseliminasjon gir at entydig løsning er $\boldsymbol{x}=\dfrac{1}{10}\begin{bmatrix}20\\ -6\\ -17\end{bmatrix}$, hvilket betyr at

$$a=2,\qquad b=-3/5\qquad\text{og}\qquad c=-17/10$$

er de beste koeffisientene.

Kildesett: course=TMA4110 term=kont year=2023 problem=8 file=tma4115_2023k_nb.pdf
