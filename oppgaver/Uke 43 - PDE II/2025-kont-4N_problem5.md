### **Problem 5** **Heat Equation [10 pts]**

Consider the heat equation modeling a thin metal rod with isolated ends
$$\begin{cases}\dfrac{\partial}{\partial t}u(t,x)=c^2\dfrac{\partial^2}{\partial x^2}u(t,x),&\text{for }0\le t,\ 0\le x\le L,\\[3mm]\dfrac{\partial}{\partial x}u(t,0)=\dfrac{\partial}{\partial x}u(t,L)=0,&\text{for }0\le t,\\[3mm]u(0,x)=f(x),&\text{for }0\le x\le L.\end{cases}$$

If $f(x)=\cos\left(\frac{n\pi}{L}x\right)$ then the solution is given by $u_n(t,x)=\cos\left(\frac{n\pi}{L}x\right)e^{-\left(\frac{n\pi c}{L}\right)^2t}$ ($n$ is a positive integer).

a) Show that the average temperature
$$\frac{1}{L}\int_0^Lu_n(t,x)dx$$
is 0 for every $t$.

b) Show that the $L^2$-norm (with respect to $x$)
$$\left(\int_0^L|u_n(t,x)|^2dx\right)^{1/2}$$
is decreasing with $t$ and find a $T$ such that
$$\left(\int_0^L|u_n(T,x)|^2dx\right)^{1/2}=\frac{1}{2}\left(\int_0^L|u_n(0,x)|^2dx\right)^{1/2}.$$

Now consider a solution $u(t,x)$ for a general $f(x)$.

c) Show that the average temperature of $u(t,x)$ is constant with respect to $t$ and that the $L^2$-norm of $u(t,x)$ is non-increasing with $t$.

Kildesett: course=TMA4130 term=kont year=2025 problem=5 points=10 file=exam_math_4n_4d_tma4130_35-5.pdf
