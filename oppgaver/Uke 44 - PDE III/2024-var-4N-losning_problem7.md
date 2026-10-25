### **Solution to Problem 7** **Finite Difference Scheme (10 points)**

We first approximate the given BVP by using second order differences
$$u''(x_i)\approx\frac{u(x_{i+1})-2u(x_i)+u(x_{i-1})}{h^2}$$
Replacing $U_i\approx u(x_i)$ to approximate the function at discrete points, we can approximate the differential equation at each inner point by
$$3U_i-\frac{U_{i+1}-2U_i+U_{i-1}}{h^2}=\sin(x_i),\qquad i=1,2,\dots,N-1$$
At the right boundary we can just set $U_N=u(x_N)=u(1)=3$.

At the left boundary, we have to approximate the derivative with a central difference. We have to introduce an artificial node $x_{-1}$ and $U_{-1}\approx u(x_{-1})$ to obtain
$$u'(0)=\frac{u(x_1)-u(x_{-1})}{2h}=1\Rightarrow\frac{U_1-U_{-1}}{2h}=1\text{ and hence }U_{-1}=U_1-2h$$
We can now extend the differential equations from the inner points to also include the left boundary, that is we get for $i=0$ that
$$3U_0-\frac{U_1-2U_0+U_{-1}}{h^2}=\sin(x_0)=0$$
We can plug in what we know about $U_{-1}$ to obtain
$$3U_0-\frac{U_1-2U_0+U_1-2h}{h^2}=0\quad\Leftrightarrow\quad 3U_0-\frac{U_1-2U_0+U_1}{h^2}=\frac{2}{h}$$
Multiplying this and the inner Equation by $h^2$ we get the following scheme
$$\begin{cases}(2+3h^2)U_0+2U_1=2h\\ -U_{i-1}+(2+3h^2)U_i-U_{i+1}=h^2\sin(x_i),\qquad i=1,2,\dots,N_1\\ U_N=3\end{cases}$$
This can be written into a matrix $A$ and a right hand side $b$ as
$$\begin{pmatrix}2+3h^2&2&0&&\cdots&0\\ -1&2+3h^2&-1&0&&\cdots&0\\ 0&-1&\ddots&\ddots&0&\cdots&0\\ \vdots&&\ddots&\ddots&\ddots&&\vdots\\ \vdots&&\ddots&\ddots&\ddots&&\vdots\\ 0&\cdots&0&-1&2+3h^2&-1&0\\ 0&\cdots&&0&-1&2+3h^2&-1\\ 0&\cdots&&&0&0&1\end{pmatrix}\begin{pmatrix}U_0\\ U_1\\ U_2\\ \vdots\\ \vdots\\ \vdots\\ U_{N-1}\\ U_N\end{pmatrix}=\begin{pmatrix}2h\\ h^2\sin(x_1)\\ h^2\sin(x_2)\\ \vdots\\ \vdots\\ \vdots\\ h^2\sin(x_{N-1})\\ 3\end{pmatrix}.$$

**Grading manual** (1p) for the second order difference formula, (2p) for the inner equations, (1p) for the right boundary, (1p) for the central difference with artificial node at the left boundary, (1p) for extending the equation to $i=0$, (1p) for plugging in $U_{-1}$, (1p) for the scheme multiplied by $h^2$, (2p) for the matrix $A$ and right hand side $b$.

Kildesett: course=TMA4125 term=var year=2024 problem=7 points=10 file=math4n-2024v-en_lf.pdf
