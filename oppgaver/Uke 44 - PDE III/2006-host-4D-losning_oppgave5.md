### **Løsning til Oppgave 5**

**a)** Vi tilnærmer den andre deriverte med hensyn på $x$ i punktet $P_{i,j}=(ih,jh)$ ved

$$u_{xx}(P_{i,j})=\frac{U_{i+1,j}+U_{i-1,j}-2U_{i,j}}{h^2}.$$

På den samme måten har vi

$$u_{yy}(P_{i,j})=\frac{U_{i,j+1}+U_{i,j-1}-2U_{i,j}}{h^2}.$$

Ligningen $u_{xx}+2u_{yy}=0$ medfører derfor

$$\frac{U_{i+1,j}+U_{i-1,j}-2U_{i,j}}{h^2}+2\frac{U_{i,j+1}+U_{i,j-1}-2U_{i,j}}{h^2}=0$$

og

$$U_{i+1,j}+U_{i-1,j}+2U_{i,j+1}+2U_{i,j-1}-6U_{i,j}=0.$$

**b)** I punktet $P_{1,1}$, har vi

$$-6U_{1,1}+U_{2,1}+U_{0,1}+2U_{1,2}+2U_{1,0}=0$$

og, siden $U_{0,1}=U_{1,0}=0$,

$$-6U_{1,1}+U_{2,1}+2U_{1,2}=0.\tag{6}$$

I punktet $P_{2,1}$, har vi

$$U_{3,1}+U_{1,1}+2U_{2,2}+2U_{2,0}-6U_{2,1}=0$$

og, siden $U_{3,1}=1$, $U_{2,0}=0$,

$$U_{1,1}-6U_{2,1}+2U_{2,2}=-1.\tag{7}$$

I punktet $P_{1,2}$, har vi

$$U_{2,2}+U_{0,2}+2U_{1,3}+2U_{1,1}-6U_{1,2}=0$$

og, siden $U_{0,2}=0$ og $U_{1,3}=1$,

$$2U_{1,1}-6U_{1,2}+U_{2,2}=-2.\tag{8}$$

I punktet $P_{2,2}$, har vi

$$U_{3,2}+U_{1,2}+2U_{2,3}+2U_{2,1}-6U_{2,2}=0$$

og, siden $U_{3,2}=U_{2,3}=1$,

$$2U_{2,1}+U_{1,2}-6U_{2,2}=-3\tag{9}$$

Vi samler ligningene (6), (7), (8) og (9), og vi får den følgende systemet:

$$\begin{pmatrix}-6&1&2&0\\ 1&-6&0&2\\ 2&0&-6&1\\ 0&2&1&-6\end{pmatrix}\begin{pmatrix}U_{1,1}\\ U_{2,1}\\ U_{1,2}\\ U_{2,2}\end{pmatrix}=\begin{pmatrix}0\\ -1\\ -2\\ -3\end{pmatrix}.$$

Den første steg av Gauss-Seidels iterasjon er gitt ved

$$\begin{cases}-6U_{1,1}^1+U_{2,1}^0+2U_{1,2}^0=0\\ \phantom{-6}U_{1,1}^1-6U_{2,1}^1+2U_{2,2}^0=-1\\ \phantom{-6}2U_{1,1}^1-6U_{1,2}^1+U_{2,2}^0=-2\\ \phantom{-6}2U_{2,1}^1+U_{1,2}^1-6U_{2,2}^1=-3\end{cases}$$

Vi får

$$U_{1,1}^1=\frac{1}{4},$$

og

$$U_{2,1}^1=-\frac{1}{6}\left(-1-1-\frac{1}{4}\right)=\frac{3}{8},$$

og

$$U_{1,2}^1=-\frac{1}{6}\left(-2-\frac{1}{2}-\frac{1}{2}\right)=\frac{1}{2},$$

og

$$U_{2,2}^1=-\frac{1}{6}\left(-3-\frac{1}{2}-\frac{6}{8}\right)=\frac{17}{24}$$

Derfor,

$$(U_{1,1}^1,U_{2,1}^1,U_{1,2}^1,U_{2,2}^1)=\left(\frac{1}{4},\frac{3}{8},\frac{1}{2},\frac{17}{24}\right).$$

Kildesett: course=TMA4135 term=host year=2006 problem=5 file=tma4135_06h.pdf
