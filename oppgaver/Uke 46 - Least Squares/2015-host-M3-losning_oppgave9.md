### **Løsning til Oppgave 9**

We are looking for the least square solution of the system $A\mathbf{x}=\mathbf{b}$ with

$$A=\begin{bmatrix}0&1\\ 1&1\\ 2&1\\ 3&1\end{bmatrix},\ \mathbf{x}=\begin{bmatrix}m\\ c\end{bmatrix},\ \mathbf{b}=\begin{bmatrix}1\\ -2\\ 3\\ 6\end{bmatrix}.$$

To find the solution we solve the system $A^T A\mathbf{x}=A^T\mathbf{b}$ which is

$$\begin{bmatrix}14&6\\ 6&4\end{bmatrix}\begin{bmatrix}m\\ c\end{bmatrix}=\begin{bmatrix}22\\ 8\end{bmatrix}.$$

Gauss elimination gives

$$\begin{bmatrix}14&6&22\\ 6&4&8\end{bmatrix}\to\begin{bmatrix}7&3&11\\ 3&2&4\end{bmatrix}\to\begin{bmatrix}1&-1&3\\ 3&2&4\end{bmatrix}\to\begin{bmatrix}1&-1&3\\ 0&5&-5\end{bmatrix}\to\begin{bmatrix}1&0&2\\ 0&1&-1\end{bmatrix}.$$

The solution is $m=2$ and $c=-1$. Thus the best fitting line is $y=2x-1$.

*Kjeldevarsel: det publiserte løysingsarkivet for 2015h finst berre på engelsk (`tma4110h15_english_solution.pdf`, «Problem 9», side 11 av 12), og løysinga er difor skriven ordrett på engelsk. Provensfoten peikar på eksamensarket, jf. OPEN-1.*

Kildesett: course=TMA4110 term=host year=2015 problem=9 file=tma4110h15_norsk.pdf
