### **Problem 9** (Discretize a PDE, 10 points)

Consider the 2-dimensional unit square $\Omega=[0,1]^{2}\subset\mathbb{R}^{2}$ and the 2-dimensional Laplace equation

$$\Delta u(x,y)=0,\qquad\text{where}\quad\Delta u(x,y)=\frac{\partial^{2}}{\partial x^{2}}u(x,y)+\frac{\partial^{2}}{\partial y^{2}}u(x,y).$$

We consider equidistant grid points $\{(x_i,y_j)\}$, $i,j=0,\ldots,N$ for some $N\in\mathbb{N}$ that uniformly subdivide each axis into $N$ subintervals.

a) Use finite differences to discretize the Laplace equation on the points $(x_i,y_j)$ from the grid by values $U_{i,j}\approx u(x_i,y_j)$. State the discrete two-dimensional Laplace operator at all suitable discretization points.

b) How large is the discretization error?

c) To extend the Laplace equation, we consider the 3-dimensional unit cube $\tilde{\Omega}=[0,1]^{3}$ and the 3-dimensional Laplace equation

$$\Delta u(x,y,z)=0,\quad\text{where}\quad\Delta u(x,y,z)=\frac{\partial^{2}}{\partial x^{2}}u(x,y,z)+\frac{\partial^{2}}{\partial y^{2}}u(x,y,z)+\frac{\partial^{2}}{\partial z^{2}}u(x,y,z).$$

We use a similar discretization as before but now construct it on all three axes to obtain the equidistant grid $(x_i,y_j,z_k)$, $i,j,k=0,\ldots,N$.

Formulate the corresponding discretization for the 3-dimensional Laplace operator $\Delta$, and give a short rationale on how you arrived at the formula.

Kildesett: course=TMA4432 term=test year=2026 problem=9 points=10 file=test-exam-math4c_web.pdf
