### **Solution to Problem 2** (Quadratic Bézier curve and degree elevation, 8 points)

a) Inserting the control points,

$$x(t)=0\cdot(1-t)^2+2\cdot 3\,t(1-t)+6t^2=6t-6t^2+6t^2=6t,\qquad y(t)=0+2\cdot 3\,t(1-t)+0=6t-6t^2,$$

so $\mathbf{c}(t)=\left(6t,\;6t-6t^2\right)^{\top}$. (1 P.)

Hence $\mathbf{c}(0)=(0,0)^{\top}=\mathbf{a}_0$, $\mathbf{c}\left(\tfrac12\right)=\left(3,\tfrac32\right)^{\top}$ and $\mathbf{c}(1)=(6,0)^{\top}=\mathbf{a}_2$. With $\mathbf{c}'(t)=(6,6-12t)^{\top}$ the tangent direction at $t=0$ is $\mathbf{c}'(0)=(6,6)^{\top}$, i.e. the diagonal direction $(1,1)^{\top}$ — in general $2(\mathbf{a}_1-\mathbf{a}_0)$. (2 P.)

b) From the elevation formula,

$$\mathbf{b}_1=\frac{1}{3}\mathbf{a}_0+\frac{2}{3}\mathbf{a}_1=\begin{pmatrix}2\\ 2\end{pmatrix},\qquad \mathbf{b}_2=\frac{2}{3}\mathbf{a}_1+\frac{1}{3}\mathbf{a}_2=\begin{pmatrix}4\\ 2\end{pmatrix},$$

together with $\mathbf{b}_0=\mathbf{a}_0=(0,0)^{\top}$ and $\mathbf{b}_3=\mathbf{a}_2=(6,0)^{\top}$. (2 P.)

c) Quadratic form at $t=\tfrac13$:

$$\mathbf{c}\left(\tfrac13\right)=\left(6\cdot\tfrac13,\;6\cdot\tfrac13-6\cdot\tfrac19\right)^{\top}=\left(2,\tfrac43\right)^{\top}.$$

Cubic form with $B_0^3\left(\tfrac13\right)=\tfrac{8}{27}$, $B_1^3\left(\tfrac13\right)=\tfrac{12}{27}$, $B_2^3\left(\tfrac13\right)=\tfrac{6}{27}$, $B_3^3\left(\tfrac13\right)=\tfrac{1}{27}$ and $\mathbf{b}_0=(0,0)$, $\mathbf{b}_1=(2,2)$, $\mathbf{b}_2=(4,2)$, $\mathbf{b}_3=(6,0)$:

$$x=\frac{12\cdot 2+6\cdot 4+1\cdot 6}{27}=\frac{54}{27}=2,\qquad y=\frac{12\cdot 2+6\cdot 2}{27}=\frac{36}{27}=\frac43,$$

the same point $\left(2,\tfrac43\right)^{\top}$. (In fact $\tilde{\mathbf{c}}(t)=\mathbf{c}(t)$ for all $t$, since $\sum_i\mathbf{b}_iB_i^3(t)$ simplifies to $(6t,6t-6t^2)^{\top}$ as well.) (2 P.)

d) Convex hull property: every Bézier curve lies in the convex hull of its control points, because the Bernstein polynomials are non-negative on $[0,1]$ and sum to $1$, so $\mathbf{c}(t)$ is a convex combination of the $\mathbf{b}_i$. (1 P.)

Here the convex hull is the triangle with corners $(0,0)$, $(3,3)$, $(6,0)$. The point $(3,4)^{\top}$ lies strictly above the triangle (its highest point is $(3,3)^{\top}$), so the curve cannot pass through $(3,4)^{\top}$ — one can also see it directly, since the curve's maximum height is $y\left(\tfrac12\right)=\tfrac32<4$. The point $(3,1)^{\top}$ does lie inside the triangle, but the convex hull property is a one-sided statement: lying in the hull does not imply the curve visits the point, so nothing can be concluded — in fact the curve at $x=3$ (that is $t=\tfrac12$) passes through $\left(3,\tfrac32\right)^{\top}$, not $(3,1)^{\top}$. (Reasoning accepted; the two conclusions are what count.)
