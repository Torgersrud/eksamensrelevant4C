### **Løsning til Oppgave 6**

Ved fempunktsformelen får vi differanseskjema

$$\frac{U_{i+1,j}+U_{i,j+1}+U_{i-1,j}+U_{i,j-1}-4U_{i,j}}{h^2}=4x_iy_j=4h^2ij=\frac{1}{4}ij.$$

Det vil si,

$$U_{i+1,j}+U_{i,j+1}+U_{i-1,j}+U_{i,j-1}-4U_{i,j}=\frac{h^2}{4}ij=\frac{1}{64}ij.$$

Fra randbetingelsene får vi

$$U_{i,4}=0,\quad i=0,1,\ldots,4$$

$$U_{i,i}=4x_i(1-x_i)=4hi(1-hi)=i\left(1-\frac{1}{4}i\right),\quad i=0,1,\ldots,4$$

$$U_{0,j}=0,\quad j=0,1,\ldots,4.$$

Fra differanseskjemaet får vi følgende ligningssystem

$$U_{2,2}+U_{1,3}+U_{0,2}+U_{1,1}-4U_{1,2}=\frac{1}{64}\cdot1\cdot2=\frac{1}{32}$$

$$U_{2,3}+U_{1,4}+U_{0,3}+U_{1,2}-4U_{1,3}=\frac{1}{64}\cdot1\cdot3=\frac{3}{64}$$

$$U_{3,3}+U_{2,4}+U_{1,3}+U_{2,2}-4U_{2,3}=\frac{1}{64}\cdot2\cdot3=\frac{3}{32}.$$

Innsatt for randbetingelsene, og $X=U_{1,2}$, $Y=U_{1,3}$ og $Z=U_{2,3}$ kan vi skrive dette som

$$1+Y+0+\frac{3}{4}-4X=\frac{1}{32}$$

$$Z+0+0+X-4Y=\frac{3}{64}$$

$$\frac{3}{4}+0+Y+1-4Z=\frac{3}{32}.$$

Det vil si,

$$\begin{bmatrix}-4&1&0\\ 1&-4&1\\ 0&1&-4\end{bmatrix}\begin{bmatrix}X\\ Y\\ Z\end{bmatrix}=\begin{bmatrix}-55/32\\ 3/64\\ -53/32\end{bmatrix}\approx\begin{bmatrix}-1.7188\\ 0.0469\\ -1.6563\end{bmatrix}.$$

Kildesett: course=TMA4135 term=host year=2012 problem=6 file=tma4135_12h.pdf
