### **Solution to Problem 4**

**a.** The third column of $A$ is $(1,1,-1,-1)^{\top}$, so $-3$ times it equals $b$: an answer is

$$x=\begin{bmatrix}0\\ 0\\ -3\end{bmatrix}.$$

**b.** Solving $Ax=0$ (Gauss elimination, or inspection: $-\text{col}_{1}+2\,\text{col}_{2}+\text{col}_{3}=0$) gives

$$\ker A=\operatorname{span}\left\{\begin{bmatrix}-1\\ 2\\ 1\end{bmatrix}\right\}.$$

Hence the solution set of $Ay=b$ is the line

$$\left\{\begin{bmatrix}-t\\ 2t\\ -3+t\end{bmatrix}:t\in\mathbb{R}\right\}=\begin{bmatrix}0\\ 0\\ -3\end{bmatrix}+\ker A.$$

The point of this line with the smallest norm is the one where the vector to the origin is orthogonal to the line, i.e. for $t$ with

$$\begin{bmatrix}-t\\ 2t\\ -3+t\end{bmatrix}^{\top}\begin{bmatrix}-1\\ 2\\ 1\end{bmatrix}=t+4t-3+t=6t-3=0,\quad t=\tfrac{1}{2}.$$

The smallest-norm solution is therefore

$$y=\begin{bmatrix}-1/2\\ 1\\ -5/2\end{bmatrix}.$$

**c.** By the method of least squares we must solve $A^{\top}Az=A^{\top}c$. Expanding out,

$$\begin{bmatrix}44&20&4\\ 20&10&0\\ 4&0&4\end{bmatrix}\begin{bmatrix}z_{1}\\ z_{2}\\ z_{3}\end{bmatrix}=\begin{bmatrix}60\\ 30\\ 0\end{bmatrix}.$$

Gauss elimination gives the solution set $\{(-\tau,\,2\tau+3,\,\tau):\tau\in\mathbb{R}\}$; any element of it works, for instance

$$z=\begin{bmatrix}1\\ 1\\ -1\end{bmatrix}.$$

*Kjeldevarsel: fasiten oppgav i punkt a) svaret $(0,0,3)^{T}$ og i punkt b) losningsmengda $(-t,2t,3+t)^{T}$ med minstenormspunkt $(1/2,-1,5/2)^{T}$ — disse løyser $Ay=-b$, ikkje $Ay=b$ for den trykte $b=(-3,-3,3,3)^{T}$ (forteknfeil; kontrollrekna med sympy: $A(0,0,-3)^{T}=b$ og $A(-1/2,1,-5/2)^{T}=b$). Fasitens $\ker A=\operatorname{span}(-1,2,1)^{T}$ og svaret $(1,1,-1)^{T}$ i punkt c) er rette.*

Kildesett: course=TMA4145 term=kont year=2009 problem=4 file=tma4145ekss09en.pdf
