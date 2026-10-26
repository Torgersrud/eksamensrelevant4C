### **Solution to Problem 3** (Composite Bézier curves, 10 points)

a) Continuity at the junction requires the end point of $\Gamma_1$ to meet the start point of $\Gamma_2$: $\mathbf{b}_3=\mathbf{c}_0$. Beyond that, $C^1$-continuity requires the two tangent vectors at the junction to be equal,

$$3(\mathbf{b}_3-\mathbf{b}_2)=3(\mathbf{c}_1-\mathbf{c}_0)\qquad\text{i.e.}\qquad \mathbf{c}_1-\mathbf{c}_0=\mathbf{b}_3-\mathbf{b}_2,$$

so $\mathbf{b}_2$, $\mathbf{b}_3=\mathbf{c}_0$ and $\mathbf{c}_1$ must be collinear with $\mathbf{c}_0$ in the middle. (2 P.)

b) With $\mathbf{b}_3=(3,0)^{\top}=\mathbf{c}_0$ the composite is continuous. (1 P.)

The tangents at the junction are

$$\Gamma_1'(1)=3(\mathbf{b}_3-\mathbf{b}_2)=3\left[\begin{pmatrix}3\\ 0\end{pmatrix}-\begin{pmatrix}2\\ 1\end{pmatrix}\right]=\begin{pmatrix}3\\ -3\end{pmatrix},\qquad \Gamma_2'(0)=3(\mathbf{c}_1-\mathbf{c}_0)=3\left[\begin{pmatrix}4\\ 1\end{pmatrix}-\begin{pmatrix}3\\ 0\end{pmatrix}\right]=\begin{pmatrix}3\\ 3\end{pmatrix}.$$

They differ (the curve has a corner at the junction, descending into it and climbing out of it), so the composite is not $C^1$. (1 P.)

c) The $C^1$-condition from a) reads

$$\mathbf{b}_3-\mathbf{b}_2=\begin{pmatrix}3\\ 0\end{pmatrix}-\begin{pmatrix}2\\ h\end{pmatrix}=\begin{pmatrix}1\\ -h\end{pmatrix}\overset!{=}\begin{pmatrix}1\\ 1\end{pmatrix}=\mathbf{c}_1-\mathbf{c}_0,$$

so $h=-1$. (Then both junction tangents equal $(3,3)^{\top}$.) (2 P.)

d) The de Casteljau triangle of $\Gamma_1$ at $t=\tfrac12$ (midpoints again) has left branch

$$\mathbf{b}_0^{(0)}=\begin{pmatrix}0\\ 0\end{pmatrix},\quad \mathbf{b}_0^{(1)}=\begin{pmatrix}1/2\\ 1/2\end{pmatrix},\quad \mathbf{b}_0^{(2)}=\begin{pmatrix}1\\ 3/4\end{pmatrix},\quad \mathbf{b}_0^{(3)}=\begin{pmatrix}3/2\\ 3/4\end{pmatrix},$$

since $\mathbf{b}_0^{(1)}=\tfrac12(\mathbf{b}_0+\mathbf{b}_1)$, $\mathbf{b}_1^{(1)}=\tfrac12(\mathbf{b}_1+\mathbf{b}_2)=\left(\tfrac32,1\right)^{\top}$, $\mathbf{b}_0^{(2)}=\tfrac12(\mathbf{b}_0^{(1)}+\mathbf{b}_1^{(1)})$, and $\mathbf{b}_0^{(3)}=\tfrac12(\mathbf{b}_0^{(2)}+\mathbf{b}_1^{(2)})$ with $\mathbf{b}_1^{(2)}=(2,\tfrac34)^{\top}$. (1 P.)

Evaluating $\mathbf{q}$ at $\tau=\tfrac12$ with $B_i^3\left(\tfrac12\right)=\tfrac18(1,3,3,1)$:

$$\mathbf{q}\left(\tfrac12\right)=\frac{\mathbf{b}_0^{(0)}+3\mathbf{b}_0^{(1)}+3\mathbf{b}_0^{(2)}+\mathbf{b}_0^{(3)}}{8}=\frac{1}{8}\left[\begin{pmatrix}0\\ 0\end{pmatrix}+\begin{pmatrix}3/2\\ 3/2\end{pmatrix}+\begin{pmatrix}3\\ 9/4\end{pmatrix}+\begin{pmatrix}3/2\\ 3/4\end{pmatrix}\right]=\frac{1}{8}\begin{pmatrix}6\\ 9/2\end{pmatrix}=\begin{pmatrix}3/4\\ 9/16\end{pmatrix}.$$

On the other side, with $B_0^3\left(\tfrac14\right)=\tfrac{27}{64}$, $B_1^3\left(\tfrac14\right)=\tfrac{27}{64}$, $B_2^3\left(\tfrac14\right)=\tfrac{9}{64}$, $B_3^3\left(\tfrac14\right)=\tfrac{1}{64}$,

$$x=\frac{27\cdot 0+27\cdot 1+9\cdot 2+1\cdot 3}{64}=\frac{48}{64}=\frac34,\qquad y=\frac{27\cdot 0+27\cdot 1+9\cdot 1+1\cdot 0}{64}=\frac{36}{64}=\frac{9}{16},$$

so indeed $\mathbf{q}\left(\tfrac12\right)=\Gamma_1\left(\tfrac14\right)$.

The left half is reparametrized onto $[0,1]$: its own parameter $\tau$ stands for $t=\tfrac{\tau}{2}$, so $\mathbf{q}(\tau)=\Gamma_1\left(\tfrac{\tau}{2}\right)$; $\tau=\tfrac12$ corresponds to $t=\tfrac14$. The endpoint $\mathbf{q}(1)=\mathbf{b}_0^{(3)}=\Gamma_1\left(\tfrac12\right)=\left(\tfrac32,\tfrac34\right)^{\top}$ is where the halves are glued. (1 P.)

e) The count gives

$$4N-3(N-1)=4N-3N+3=N+3$$

free parameters. Each $C^2$ junction imposes three vector conditions (value, first, second derivative), and conditions at different junctions involve different neighbouring control points, so they are independent and each removes three degrees of freedom. (1 P.)

A $C^2$ composite of $N$ cubic polynomial pieces is precisely a cubic spline on $N$ intervals, i.e. on the knot vector $\Delta$ consisting of the $N+1$ junction abscissas $x_0,\ldots,x_N$. Writing $n+1=N+1$ for the number of distinct knots in the lecture's notation ($\dim\mathcal{S}_{k,\Delta}=n+k$) gives $\dim\mathcal{S}_{3,\Delta}=N+3$ — the same number: the Bézier control points with $C^2$ gluing conditions and the spline space parametrize exactly the same curves. (Example check: the test exam's $\Delta=[-1,0,1,2,3]$ has $n=4$, $\dim=7$; here $N=4$ intervals likewise give $N+3=7$.) (1 P.)
