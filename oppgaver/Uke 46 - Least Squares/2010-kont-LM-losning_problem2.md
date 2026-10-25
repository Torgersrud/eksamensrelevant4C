### **Solution to Problem 2**

There are several ways to do this; either by finding a basis for $W$, making it orthonormal, and computing the projection using it, or by using the method of least-squares.

For both, we start by finding a basis for $W$. To do this, we observe that $W$ is the null space of the matrix

$$\begin{bmatrix}1&3&-1&3&5\\ 3&9&-3&3&9\\ 2&6&-2&0&4\\ 1&3&-1&-3&-1\end{bmatrix}$$

and thus a basis is given by:

$$\left\{\begin{bmatrix}-3\\ 1\\ 0\\ 0\\ 0\end{bmatrix},\begin{bmatrix}1\\ 0\\ 1\\ 0\\ 0\end{bmatrix},\begin{bmatrix}-2\\ 0\\ 0\\ -1\\ 1\end{bmatrix}\right\}.$$

Hence $W$ is the image of the matrix:

$$B:=\begin{bmatrix}-3&1&-2\\ 1&0&0\\ 0&1&0\\ 0&0&-1\\ 0&0&1\end{bmatrix}.$$

The method of least-squares says that we should solve $B^{T}Bx=B^{T}b$. This expands to:

$$\begin{bmatrix}10&-3&6\\ -3&2&-2\\ 6&-2&6\end{bmatrix}x=\begin{bmatrix}8\\ 0\\ 2\end{bmatrix}$$

Applying Gauss elimination yields the solution $\begin{bmatrix}-2\\ -2\\ 1\end{bmatrix}$. Applying $B$ to this produces the desired result:

$$\begin{bmatrix}2\\ -2\\ -2\\ -1\\ 1\end{bmatrix}$$

This problem is worth 8 points.

*Kjeldevarsel: høgre side $B^{T}b$ er trykt som $(8,0,2)^{T}$, men med $b=(4,4,-4,-1,5)^{T}$ og den oppgitte $B$-matrisa gir reknestykket $B^{T}b=(-8,0,-2)^{T}$ (kontrollrekna). Det trykte svaret $x=(-2,-2,1)^{T}$ og sluttresultatet $Bx=(2,-2,-2,-1,1)^{T}$ er konsistente med den rette høgresida og er rette.*

Kildesett: course=TMA4145 term=kont year=2010 problem=2 points=8 file=tma4145ekss10en.pdf
