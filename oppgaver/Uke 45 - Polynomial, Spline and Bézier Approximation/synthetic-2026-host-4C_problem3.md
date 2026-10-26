### **Problem 3** (Composite Bézier curves, 10 points)

A composite curve $\gamma$ is formed by first running along the cubic Bézier segment $\Gamma_1$ with control points

$$\mathbf{b}_0=\begin{pmatrix}0\\ 0\end{pmatrix},\ \mathbf{b}_1=\begin{pmatrix}1\\ 1\end{pmatrix},\ \mathbf{b}_2=\begin{pmatrix}2\\ 1\end{pmatrix},\ \mathbf{b}_3=\begin{pmatrix}3\\ 0\end{pmatrix},\qquad t\in[0,1],$$

and then along the cubic Bézier segment $\Gamma_2$ with control points

$$\mathbf{c}_0=\begin{pmatrix}3\\ 0\end{pmatrix},\ \mathbf{c}_1=\begin{pmatrix}4\\ 1\end{pmatrix},\ \mathbf{c}_2=\begin{pmatrix}5\\ 1\end{pmatrix},\ \mathbf{c}_3=\begin{pmatrix}6\\ 0\end{pmatrix},\qquad t\in[0,1].$$

a) State conditions on the control points that make $\gamma$ continuous at the junction, and respectively continuously differentiable ($C^1$). Use that $\mathbf{c}'(1)=3(\mathbf{b}_3-\mathbf{b}_2)$ and $\mathbf{c}'(0)=3(\mathbf{b}_1-\mathbf{b}_0)$.

b) Are the given segments continuous at the junction? Are they $C^1$? Justify by computing both tangent vectors at the junction.

c) We replace $\mathbf{b}_2$ by $(2,h)^{\top}$ and keep all other control points. Determine $h$ so that $\gamma$ becomes $C^1$.

d) The left half of $\Gamma_1$ (the piece $t\in[0,\tfrac12]$) is again a cubic Bézier curve: its control points, after the parametrization is stretched back to $[0,1]$, are the left branch $\mathbf{b}_0^{(0)},\mathbf{b}_0^{(1)},\mathbf{b}_0^{(2)},\mathbf{b}_0^{(3)}$ of the de Casteljau triangle of $\Gamma_1$ at $t=\tfrac12$. Give these four control points, and verify that the resulting curve $\mathbf{q}(\tau)$ satisfies $\mathbf{q}\left(\tfrac12\right)=\Gamma_1\left(\tfrac14\right)$ by computing both sides. Why is the check value $\Gamma_1\left(\tfrac14\right)$ and not $\Gamma_1\left(\tfrac12\right)$?

e) A composite of $N$ cubic Bézier segments is described by $4N$ control points, and $C^2$-continuity at each of the $N-1$ inner junctions imposes three vector conditions (function value, first and second derivative must match). Count the free parameters of a $C^2$ composite curve and explain why the result agrees with the dimension formula $\dim\mathcal{S}_{3,\Delta}=n+k$ for the cubic spline space with $n+1$ distinct knots.
