### **Solution to Problem 7** **Discretize a PDE (10 points)**

a) We use the second order finite difference
$$f''(x)\approx\frac{f(x-h)-2f(x)+f(x+h)}{h^2}$$
in both the $x$ and the $y$ axis. Plugging in $U_{i,j}\approx u(x_i,y_j)$ we obtain
$$\frac{\partial^2}{\partial x^2}u(x_i,y_j)+\frac{\partial^2}{\partial y^2}u(x_i,y_j)\approx\frac{u(x_i-h,y_j)-2u(x_i,y_j)+u(x_i+h,y_j)}{h^2}+\frac{u(x_i,y_j-h)-2u(x_i,y_j)+u(x_i,y_j+h)}{h^2}$$
$$\approx\frac{U_{i-1,j}-2U_{i,j}+U_{i+1,j}}{h^2}+\frac{U_{i,j-1}-2U_{i,j}+U_{i,j+1}}{h^2}=\frac{U_{i-1,j}+U_{i+1,j}+U_{i,j-1}+U_{i,j+1}-4U_{i,j}}{h^2},$$
where $i,j=1,\dots,N-1$, since at the boundary at least one of the neighbors does not exist.

b) For the discretization error, we have to compare the second derivative to the second order finite difference. We have
$$f''(x)=\frac{f(x-h)-2f(x)+f(x+h)}{h^2}+O(h^2)$$
so that overall there error is as well $O(h^2)$.

c) We have to perform a third finite difference in $z$-direction. We obtain the so-called 7-stencil
$$\frac{U_{i-1,j,k}+U_{i+1,j,k}+U_{i,j-1,k}+U_{i,j+1,k}+U_{i,j,k-1}+U_{i,j,k+1}-6U_{i,j,k}}{h^2},$$
where (again) $i,j,k=1,\dots,N-1$, since we have to exclude the boundary.

**Grading manual**

a) (5p)

b) (3p)

c) (2p)

Kildesett: course=TMA4125 term=var year=2025 problem=7 points=10 file=math4n-2025v-en-lf.pdf
