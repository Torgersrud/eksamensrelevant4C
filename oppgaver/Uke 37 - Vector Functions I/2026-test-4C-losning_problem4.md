### **Solution to Problem 4** (Newton's method, 7 points)

We rearrange the system so that we look for a zero of (1 P.)

$$\mathbf{F}(x,y)=\begin{pmatrix}x^{2}-x+\cos(y)\\ \sin(x)+y^{3}-y\end{pmatrix}\overset{!}{=}\begin{pmatrix}0\\ 0\end{pmatrix}.$$

We first need its Jacobian (2 P.)

$$J_F(x,y)=\begin{pmatrix}2x-1&-\sin(y)\\ \cos(x)&3y^{2}-1\end{pmatrix}.$$

For the step we have the following. At our starting point we have

$$\mathbf{F}(0,0)=\begin{pmatrix}0+1\\ 0\end{pmatrix}=\begin{pmatrix}1\\ 0\end{pmatrix}\quad\text{and}\quad J_F(0,0)=\begin{pmatrix}-1&0\\ 1&-1\end{pmatrix}.$$

So for the next step we get (2 P.)

$$J_F(x_0,y_0)\begin{pmatrix}\delta x\\ \delta y\end{pmatrix}=\begin{pmatrix}-1&0\\ 1&-1\end{pmatrix}\begin{pmatrix}\delta x\\ \delta y\end{pmatrix}=-\begin{pmatrix}1\\ 0\end{pmatrix}=-\mathbf{F}(0,0).$$

Thus $\delta x=1$ from the first equation, and since $\delta x-\delta y=0$ in the second equation, we get the same $\delta y=1$. Hence, $(x_1,y_1)=(x_0,y_0)+(\delta x,\delta y)=(1,1)$. (2 P.)

Kildesett: course=TMA4432 term=test year=2026 problem=4 points=7 file=test-exam-math4c_web.pdf
