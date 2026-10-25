### **Løsning til Oppgave 2**

Punktene gir oss ligningene

$$\begin{array}{rccc}p(0)=&b=&1\\ p(1)=&a+b=&-1\\ p(2)=&2a+b=&2\\ p(3)=&3a+b=&2\end{array}$$

Dette tilsvarer matriseligningen $A\mathbf{x}=\mathbf{b}$ med

$$A=\begin{bmatrix}0&1\\ 1&1\\ 2&1\\ 3&1\end{bmatrix}\quad\text{og}\quad\mathbf{b}=\begin{bmatrix}1\\ -1\\ 2\\ 2\end{bmatrix}.$$

Vi finner $A^{T}A$ og $A^{T}\mathbf{b}$:

$$A^{T}A=\begin{bmatrix}0&1&2&3\\ 1&1&1&1\end{bmatrix}\begin{bmatrix}0&1\\ 1&1\\ 2&1\\ 3&1\end{bmatrix}=\begin{bmatrix}14&6\\ 6&4\end{bmatrix}$$

$$A^{T}\mathbf{b}=\begin{bmatrix}0&1&2&3\\ 1&1&1&1\end{bmatrix}\begin{bmatrix}1\\ -1\\ 2\\ 2\end{bmatrix}=\begin{bmatrix}9\\ 4\end{bmatrix}$$

Så reduserer vi totalmatrisen til normallikningene $A^{T}A\mathbf{x}=A^{T}\mathbf{b}$:

$$\left[\begin{array}{cc|c}14&6&9\\ 6&4&4\end{array}\right]\sim\left[\begin{array}{cc|c}1&0&3/5\\ 0&1&1/10\end{array}\right]$$

Altså er $a=\frac{3}{5}$ og $b=\frac{1}{10}$, og $p(x)=\frac{3}{5}x+\frac{1}{10}$ er førstegradspolynomet som passer best til punktene.

Kildesett: course=TMA4110 term=kont year=2025 problem=2 file=tma4115-kont25-bokmal.pdf
