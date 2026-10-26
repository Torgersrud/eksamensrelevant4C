### **Problem 2** (Quadratic Bézier curve and degree elevation, 8 points)

A quadratic Bézier curve with control points $\mathbf{a}_0,\mathbf{a}_1,\mathbf{a}_2\in\mathbb{R}^{2}$ is

$$\mathbf{c}(t)=\mathbf{a}_0(1-t)^2+2\mathbf{a}_1t(1-t)+\mathbf{a}_2t^2,\qquad t\in[0,1],$$

with $\mathbf{a}_0=\begin{pmatrix}0\\ 0\end{pmatrix}$, $\mathbf{a}_1=\begin{pmatrix}3\\ 3\end{pmatrix}$, $\mathbf{a}_2=\begin{pmatrix}6\\ 0\end{pmatrix}$.

a) Compute $\mathbf{c}(t)$ as a pair of polynomials in $t$ and evaluate $\mathbf{c}(0)$, $\mathbf{c}\left(\tfrac{1}{2}\right)$ and $\mathbf{c}(1)$. Give the tangent direction of the curve at $t=0$.

b) The same curve can be written as a cubic Bézier curve $\tilde{\mathbf{c}}(t)=\sum_{i=0}^{3}\mathbf{b}_iB_i^3(t)$ without changing its shape (*degree elevation*). The elevated control points are

$$\mathbf{b}_i=\frac{i}{3}\,\mathbf{a}_{i-1}+\left(1-\frac{i}{3}\right)\mathbf{a}_i,\qquad i=0,\ldots,3,$$

where terms with out-of-range index are taken to be zero, so that $\mathbf{b}_0=\mathbf{a}_0$ and $\mathbf{b}_3=\mathbf{a}_2$. Compute $\mathbf{b}_1$ and $\mathbf{b}_2$.

c) Check the claim of b) at the single parameter value $t=\tfrac{1}{3}$ by evaluating $\mathbf{c}\left(\tfrac{1}{3}\right)$ from the quadratic form and $\tilde{\mathbf{c}}\left(\tfrac{1}{3}\right)$ from the elevated cubic control points with the Bernstein polynomials.

d) State the convex hull property of Bézier curves. Does it allow you to exclude that the curve passes through the point $(3,4)^{\top}$? Does it allow you to conclude that the curve passes through $(3,1)^{\top}$? Justify.
