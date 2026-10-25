### **Problem 1** (Cubic Bézier curve, 10 points)

A cubic Bézier curve with control points $\mathbf{b}_0,\mathbf{b}_1,\mathbf{b}_2,\mathbf{b}_3\in\mathbb{R}^{2}$ is given by

$$\mathbf{c}(t)=\sum_{i=0}^{3}\mathbf{b}_iB_i^3(t),\qquad t\in[0,1],$$

with the cubic Bernstein polynomials $B_i^3(t)=\binom{3}{i}t^{i}(1-t)^{3-i}$. Consider the control points

$$\mathbf{b}_0=\begin{pmatrix}0\\ 0\end{pmatrix},\quad \mathbf{b}_1=\begin{pmatrix}0\\ 2\end{pmatrix},\quad \mathbf{b}_2=\begin{pmatrix}4\\ 2\end{pmatrix},\quad \mathbf{b}_3=\begin{pmatrix}4\\ 0\end{pmatrix}.$$

a) Write out the four Bernstein polynomials $B_0^3,\ldots,B_3^3$ and state $\mathbf{c}(0)$ and $\mathbf{c}(1)$ with a brief justification.

b) Evaluate $\mathbf{c}\left(\tfrac{1}{2}\right)$ with the de Casteljau algorithm. Show all intermediate points $\mathbf{b}_i^{(j)}(t)$ of the triangle at $t=\tfrac12$.

c) Compute the two coordinate functions of $\mathbf{c}(t)$ as polynomials in $t$ and use them to confirm your value of $\mathbf{c}\left(\tfrac{1}{2}\right)$ from b).

d) The derivative of a Bézier curve at the endpoints satisfies $\mathbf{c}'(0)=3(\mathbf{b}_1-\mathbf{b}_0)$ and $\mathbf{c}'(1)=3(\mathbf{b}_3-\mathbf{b}_2)$. Determine the tangent lines of the curve at $\mathbf{c}(0)$ and $\mathbf{c}(1)$.
