### **Løsning til Oppgave 5**

**a)** Vi må sjekke om likningen $c_1v+c_2u+c_3w=0$ har andre løsninger enn $c_1=c_2=c_3$. Vi finner at $\det\begin{bmatrix}0&-1&0\\ 2&1&-1\\ 0&1&1\end{bmatrix}=-2\det\begin{bmatrix}-1&0\\ 1&1\end{bmatrix}=2\neq0$, altså er disse lineært uavhengige.

**b)** Korteste avstand er lik lengden av $u-\mathrm{Proj}_V(u)$. $v$ og $w$ er ortogonale, $v\cdot w=0$, og vi finner

$$\mathrm{Proj}_V(u)=\frac{\langle v,u\rangle}{\lVert v\rVert^2}v+\frac{\langle w,u\rangle}{\lVert w\rVert^2}w=\frac{2}{3}\begin{bmatrix}-1\\ 1\\ 1\end{bmatrix}+\frac{-2}{2}\begin{bmatrix}0\\ -1\\ 1\end{bmatrix}=\frac{1}{3}\begin{bmatrix}-2\\ 5\\ -1\end{bmatrix}.$$

Avstanden er da lik:

$$\left\lVert\begin{bmatrix}0\\ 2\\ 0\end{bmatrix}-\frac{1}{3}\begin{bmatrix}-2\\ 5\\ -1\end{bmatrix}\right\rVert=\left\lVert\frac{1}{3}\begin{bmatrix}2\\ 1\\ 1\end{bmatrix}\right\rVert=\sqrt{\tfrac{2}{3}}.$$

**c)** [Figure: Tre dimensjonerte koordinataksar $x$, $y$, $z$ med eit skugdegt plan $V$ gjennom origo. Vektorane $v$ og $w$ ligg i planet, og $u$ og $\mathrm{Proj}_V(u)$ er teikna raude frå origo; spissen av $\mathrm{Proj}_V(u)$ er fotpunket av normalproeksjonen av spissen av $u$ ned på planet.]

Kildesett: course=TMA4110 term=host year=2024 problem=5 file=tma4110_24h_bokmaal.pdf
