### **Solution to Problem 2**

**a.** By inspection (or Gauss elimination): $-\text{col}_{1}+\text{col}_{2}=b$, so

$$x=\begin{bmatrix}-1\\ 1\\ 0\end{bmatrix}.$$

**b.** $Ay$ is the nearest point to $c$ precisely when $y$ solves the normal equations $A^{\top}Ay=A^{\top}c$. Expanding out,

$$A^{\top}A=\begin{bmatrix}30&0&30\\ 0&15&15\\ 30&15&45\end{bmatrix},\qquad A^{\top}c=\begin{bmatrix}-30\\ 15\\ -15\end{bmatrix}.$$

Gauss elimination on the augmented matrix gives the solution line

$$\left\{\begin{bmatrix}-1+t\\ 1+t\\ -t\end{bmatrix}:t\in\mathbb{R}\right\},$$

i.e. the particular solution $(-1,1,0)^{\top}$ of $Ax=b$ (from a) plus the kernel $\ker A=\operatorname{span}\{(1,1,-1)^{\top}\}$.

**c.** Among these $y$'s, the one of smallest norm is the point where the vector to the origin is orthogonal to the direction $(1,1,-1)^{\top}$ of the line:

$$(-1+t,\,1+t,\,-t)\cdot(1,1,-1)=-1+t+1+t+t=3t=0\implies t=0,$$

so

$$z=\begin{bmatrix}-1\\ 1\\ 0\end{bmatrix}.$$

(Here the nearest point to $c$ is $Az=b$ itself.)

Kildesett: course=TMA4145 term=host year=2008 problem=2 file=tma4145eksh08en.pdf
