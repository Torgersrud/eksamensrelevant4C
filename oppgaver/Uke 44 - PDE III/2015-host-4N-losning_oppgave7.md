### **Løsning til Oppgave 7**

The problem we are looking at

[Figure: The square $0<x<1$, $0<y<1$ with horizontal $x$-axis and vertical $y$-axis, the side $x=1$ and $y=1$ ticked at $1$. The square is shaded and its boundary and the interior $3\times 3$ grid points $(i\cdot h,j\cdot h)$, $h=1/3$, are marked with dots. Boundary labels: $u=2x$ along the top side, $u=0$ along the left side (written vertically), $u=1+y$ along the right side (written vertically) and $u=x$ along the bottom side. Inside the square the label $2\,\partial_{xx}^2u+\partial_{yy}u=2y-x$.]

The standard discretization of the second derivatives with finite differences gives us the equations

$$\frac{2}{h^2}(u_{i-1,j}-2u_{i,j}+u_{i+1,j})+\frac{1}{h^2}(u_{i,j-1}-2u_{i,j}+u_{i,j+1})=2y_j-x_i,$$

or, inserting $h=1/3$, $y_j=j/3$, $x_i=i/3$,

$$18u_{i-1,j}-54u_{i,j}+18u_{i+1,j}+9u_{i,j-1}+9u_{i,j+1}=\frac{2j}{3}-\frac{i}{3}.$$

Moreover we have the boundary conditions

$$u_{1,3}=\frac{2}{3},\quad u_{2,3}=\frac{4}{3},$$

$$u_{0,2}=0,\qquad\qquad u_{3,2}=\frac{5}{3},$$

$$u_{0,1}=0,\qquad\qquad u_{3,1}=\frac{4}{3},$$

$$u_{1,0}=\frac{1}{3},\quad u_{2,0}=\frac{2}{3}.$$

Thus we obtain the following equations:

- At $u_{11}$:

$$-54u_{11}+18u_{21}+3+9u_{12}=\frac{1}{3}.$$

- At $u_{21}$:

$$18u_{11}-54u_{21}+24+6+9u_{22}=0.$$

- At $u_{12}$:

$$-54u_{12}+18u_{22}+9u_{11}+6=1.$$

- At $u_{22}$:

$$18u_{12}-54u_{22}+30+9u_{21}+12=\frac{2}{3}.$$

Or, if we want to write the system in matrix form

$$\begin{pmatrix}-54&18&9&0\\ 18&-54&0&9\\ 9&0&-54&18\\ 0&9&18&-54\end{pmatrix}\begin{pmatrix}u_{11}\\ u_{21}\\ u_{12}\\ u_{22}\end{pmatrix}=\begin{pmatrix}-\frac{8}{3}\\[4pt] -30\\[4pt] -5\\[4pt] -\frac{124}{3}\end{pmatrix}.$$

Kildesett: course=TMA4130 term=host year=2015 problem=7 file=bokmal.pdf
