### **Solution to Problem 9** (Discretize a PDE, 10 points)

a) We use the second order finite difference

$$f''(x)\approx\frac{f(x-h)-2f(x)+f(x+h)}{h^{2}}$$

in both the $x$ and the $y$ axis. (1 P.)

Plugging in $U_{i,j}\approx u(x_i,y_j)$ we obtain (3 P.)

$$\begin{aligned}\frac{\partial^{2}}{\partial x^{2}}u(x_i,y_j)+\frac{\partial^{2}}{\partial y^{2}}u(x_i,y_j)&\approx\frac{u(x_i-h,y_j)-2u(x_i,y_j)+u(x_i+h,y_j)}{h^{2}}\\ &\quad+\frac{u(x_i,y_j-h)-2u(x_i,y_j)+u(x_i,y_j+h)}{h^{2}}\\ &\approx\frac{U_{i-1,j}-2U_{i,j}+U_{i+1,j}}{h^{2}}+\frac{U_{i,j-1}-2U_{i,j}+U_{i,j+1}}{h^{2}}\\ &=\frac{U_{i-1,j}+U_{i+1,j}+U_{i,j-1}+U_{i,j+1}-4U_{i,j}}{h^{2}},\end{aligned}$$

where $i,j=1,\ldots,N-1$, since at the boundary at least one of the neighbors does not exist. (1 P.)

b) For the discretization error, we have to compare the second derivative to the second order finite difference. (1 P.)

We have (1 P.)

$$f''(x)=\frac{f(x-h)-2f(x)+f(x+h)}{h^{2}}+\mathcal{O}(h^{2})$$

so that overall the error is as well $\mathcal{O}(h^{2})$. (1 P.)

c) We have to perform a third finite difference in $z$-direction. (1 P.)

We obtain the so-called 7-point stencil (1 P.)

$$\frac{U_{i-1,j,k}+U_{i+1,j,k}+U_{i,j-1,k}+U_{i,j+1,k}+U_{i,j,k-1}+U_{i,j,k+1}-6U_{i,j,k}}{h^{2}},$$

where (again) $i,j,k=1,\ldots,N-1$, since we have to exclude the boundary.

Kildesett: course=TMA4432 term=test year=2026 problem=9 points=10 file=test-exam-math4c_web.pdf
