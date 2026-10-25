### **Løsning til Oppgave 5**

Vi setter opp en minste kvadraters løsning: (Sett inn $a(-1)+b=2$ osv.). Dette gir oss matrisen

$$A=\begin{bmatrix}-1&1\\ 0&1\\ 1&1\\ 2&1\\ 3&1\end{bmatrix},\ \mathbf{b}=\begin{bmatrix}2\\ 0\\ 2\\ -2\\ 1/2\end{bmatrix}\ \rightarrow A^{T}A=\begin{bmatrix}15&5\\ 5&5\end{bmatrix},\ A^{T}\mathbf{b}=\begin{bmatrix}-5/2\\ 5/2\end{bmatrix}$$

Vi løser nå $A^{T}A=A^{T}\mathbf{b}$ ved hjelp av gausseliminasjon og finner

$$\begin{bmatrix}15&5&-5/2\\ 5&5&5/2\end{bmatrix}\rightarrow\begin{bmatrix}5&5/3&-5/6\\ 0&10/3&20/6\end{bmatrix}\rightarrow\begin{bmatrix}1&0&-1/2\\ 0&1&1\end{bmatrix}$$

Dermed er linja som passer best $g(x)=-\frac{1}{2}x+1$.

Kildesett: course=TMA4110 term=kont year=2024 problem=5 file=tma4115_2024v_kont_nb.pdf
