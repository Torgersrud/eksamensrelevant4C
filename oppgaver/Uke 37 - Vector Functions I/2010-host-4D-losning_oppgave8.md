### **Løsning til Oppgave 8**

Her er

$$J(\mathbf{x})=\begin{bmatrix}20&-1\\ \cos(x_1)&-20\end{bmatrix},\qquad \mathbf{f}(\mathbf{x})=\begin{bmatrix}20x_1-x_2-10\pi\\ \sin(x_1)-20x_2+1\end{bmatrix}.$$

Med oppgitte startverdier blir $J(\mathbf{x}^{(0)})\Delta\mathbf{x}=-\mathbf{f}(\mathbf{x}^{(0)})$ til

$$\begin{bmatrix}20&-1\\ 0&-20\end{bmatrix}\begin{bmatrix}\Delta x_1\\ \Delta x_2\end{bmatrix}=-\begin{bmatrix}0\\ 2\end{bmatrix}$$

med løsning $\Delta x_2=\frac{1}{10}=0.1$ og $\Delta x_1=\frac{1}{200}=0.0005$. Dermed blir

$$x_1^{(1)}=\frac{\pi}{2}+\frac{1}{200}\approx 1.5758,\qquad x_2^{(1)}=0.1000.$$

Kildesett: course=TMA4135 term=host year=2010 problem=8 file=tma4135_10h.pdf
