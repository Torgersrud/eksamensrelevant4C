### **Solution to Problem 5** (Gradient Descent, 10 points)

a) We obtain (2 P.)

$$\nabla f(x,y)=\begin{pmatrix}3x^{2}+14x-2y+3\\ -2x+2y+6\end{pmatrix}.$$

b) Since $\nabla f(0,1)=(1,8)^{\top}$, the first step yields

$$(x_1,y_1)=(0,1)-0.1\,(1,8)=(-0.1,0.2).$$

With $\nabla f(-0.1,0.2)=(1.23,6.6)^{\top}$ the second step yields

$$(x_2,y_2)=(-0.1,0.2)-0.1\,(1.23,6.6)=(-0.223,-0.46).$$

The function values decrease from $f(0,1)=7$ via $f(x_1,y_1)=1.049$ to $f(x_2,y_2)\approx-3.086$. (2 P.)

c) For $s=1$ we obtain, with $\nabla f(-1,-7)=(6,-6)^{\top}$,

$$(x_1,y_1)=(0,1)-(1,8)=(-1,-7)\quad\text{and}\quad(x_2,y_2)=(-1,-7)-(6,-6)=(-7,-1),$$

and the next iterate is $(-61,-19)$. The function values decrease from $f(0,1)=7$ via $f(x_1,y_1)=-4$ and $f(x_2,y_2)=-40$ to $f(-61,-19)=-203\,188$, already after two steps far below $f(-1,-4)=-13$. The step size is too large: the iterates overshoot and run off towards $x\to-\infty$, where $f$ is unbounded from below due to the term $x^{3}$, instead of approaching the local minimum $(-1,-4)$ the iterates for $s=0.1$ tend to. (2 P.)

At $(\tilde{x}_0,\tilde{y}_0)=(-1,-4)$ we have $\nabla f(-1,-4)=(0,0)^{\top}$, so every step is zero and the method stays at this critical point. (1 P.)

d) Critical points of $f$ are zeros of the vector function $\nabla f$, so we can apply Newton's method for systems to $\nabla f(x,y)=\mathbf{0}$. (1 P.)

The further ingredient is its Jacobian, the Hessian. (1 P.)

We can even compute it here and it reads

$$\mathrm{Hess}\,f(x,y)=\begin{pmatrix}6x+14&-2\\ -2&2\end{pmatrix}.$$

In every step we solve $\mathrm{Hess}\,f(x_k,y_k)\Delta=-\nabla f(x_k,y_k)$ and set $(x_{k+1},y_{k+1})=(x_k,y_k)+\Delta$.

e) Here we have that $\nabla f(\tilde{x}_0,\tilde{y}_0)=\mathbf{0}$. This means that the new step $\Delta$ would be a solution of the system $\mathrm{Hess}\,f(-1,-4)\Delta=\mathbf{0}$. Indeed $\mathrm{Hess}\,f(-1,-4)=\begin{pmatrix}8&-2\\ -2&2\end{pmatrix}$ is invertible (its determinant is 12), the system even has the zero vector as a unique solution. (1 P.)

Another problem we might face is that the Hessian does not have full rank.

Kildesett: course=TMA4432 term=test year=2026 problem=5 points=10 file=test-exam-math4c_web.pdf
