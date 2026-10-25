### **Solution to Problem 3** (Tangent plane to a surface, 8 points)

We consider the function $f(x,y,z)=x^{3}+2xyz+x\cos(z^{2})-2$.

Its level set $f(x,y,z)=0$ is the surface $S$. The gradient $\nabla f$ of $f$ is orthogonal to $S$ and hence also orthogonal to the tangent plane. We compute

$$\nabla f(x,y,z)=\begin{pmatrix}3x^{2}+2yz+\cos(z^{2})\\ 2xz\\ 2xy-2xz\sin(z^{2})\end{pmatrix}$$

which yields at our point of interest

$$\nabla f(1,\ -1,\ 0)=\begin{pmatrix}4\\ 0\\ -2\end{pmatrix}.$$

The tangent plane consists of all points $(x,y,z)^{\top}$ whose difference to $\mathbf{p}$ is tangent to $S$, that is, such that

$$\langle\nabla f(\mathbf{p}),\ (x,y,z)^{\top}-\mathbf{p}\rangle=0.$$

Plugging in the values yields

$$0=\left\langle\begin{pmatrix}4\\ 0\\ -2\end{pmatrix},\ \begin{pmatrix}x-1\\ y+1\\ z\end{pmatrix}\right\rangle=4x-4-2z$$

and hence the tangent plane consists of all points $(x,y,z)^{\top}$ that fulfil

$$2x-z=2.$$

*In other words*, you can also conclude that the tangent plane consists of the points

$$\mathbf{p}+s\begin{pmatrix}0\\ 1\\ 0\end{pmatrix}+t\begin{pmatrix}1\\ 0\\ 2\end{pmatrix},\qquad s,t\in\mathbb{R}.$$

Kildesett: course=TMA4432 term=test year=2026 problem=3 points=8 file=test-exam-math4c_web.pdf
