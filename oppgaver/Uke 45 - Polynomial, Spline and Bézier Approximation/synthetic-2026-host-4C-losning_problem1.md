### **Solution to Problem 1** (Cubic Bézier curve, 10 points)

a) $B_0^3(t)=(1-t)^3$, $B_1^3(t)=3t(1-t)^2$, $B_2^3(t)=3t^2(1-t)$, $B_3^3(t)=t^3$. (1 P.)

At $t=0$ only $B_0^3(0)=1$ is non-zero and all others vanish, and at $t=1$ only $B_3^3(1)=1$ is non-zero, so the curve interpolates the outer control points: $\mathbf{c}(0)=\mathbf{b}_0=(0,0)^{\top}$ and $\mathbf{c}(1)=\mathbf{b}_3=(4,0)^{\top}$. (1 P.)

b) The de Casteljau recursion at $t=\tfrac12$ takes midpoints, $\mathbf{b}_i^{(j+1)}=\tfrac{1}{2}\mathbf{b}_i^{(j)}+\tfrac{1}{2}\mathbf{b}_{i+1}^{(j)}$:

$$\begin{array}{llll}
\mathbf{b}_0^{(0)}=(0,0) & \mathbf{b}_1^{(0)}=(0,2) & \mathbf{b}_2^{(0)}=(4,2) & \mathbf{b}_3^{(0)}=(4,0)\\[2pt]
& \mathbf{b}_0^{(1)}=(0,1) & \mathbf{b}_1^{(1)}=(2,2) & \mathbf{b}_2^{(1)}=(4,1)\\[2pt]
& & \mathbf{b}_0^{(2)}=(1,\tfrac32) & \mathbf{b}_1^{(2)}=(3,\tfrac32)\\[2pt]
& & & \mathbf{b}_0^{(3)}=(2,\tfrac32)
\end{array}$$

so $\mathbf{c}\left(\tfrac{1}{2}\right)=\left(2,\tfrac{3}{2}\right)^{\top}$. (4 P.)

c) With the coordinates of the control points,

$$x(t)=0\cdot(1-t)^3+0\cdot 3t(1-t)^2+4\cdot 3t^2(1-t)+4t^3=12t^2-8t^3,$$
$$y(t)=0\cdot(1-t)^3+2\cdot 3t(1-t)^2+2\cdot 3t^2(1-t)+0\cdot t^3=6t-6t^2.$$ (1 P.)

At $t=\tfrac12$: $x=12\cdot\tfrac14-8\cdot\tfrac18=3-1=2$ and $y=6\cdot\tfrac12-6\cdot\tfrac14=3-\tfrac32=\tfrac32$, confirming $\mathbf{c}\left(\tfrac12\right)=\left(2,\tfrac32\right)^{\top}$. (1 P.)

d) $\mathbf{c}'(0)=3(\mathbf{b}_1-\mathbf{b}_0)=3(0,2)^{\top}=(0,6)^{\top}$: the tangent at the start is vertical, the line $x=0$. $\mathbf{c}'(1)=3(\mathbf{b}_3-\mathbf{b}_2)=3(0,-2)^{\top}=(0,-6)^{\top}$: the tangent at the end is likewise vertical, the line $x=4$. (2 P.)
