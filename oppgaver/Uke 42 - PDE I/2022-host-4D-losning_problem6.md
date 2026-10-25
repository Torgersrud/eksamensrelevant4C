### **Solution to Problem 6** (4D only)

The PDE is nonlinear, due the $u \frac{\partial u}{\partial x}$ term.

To check the solution, use:

$$u_t = -\frac{2a}{(at + x + b)^2}, \qquad u_x = -\frac{2}{(at + x + b)^2}, \qquad u_{xx} = \frac{4}{(at + x + b)^3}.$$

Inserting this into the right hand side of the PDE gives

$$u_{xx} + u u_x = \frac{4}{(at + x + b)^3} + \left( a + \frac{2}{at + x + b} \right) \left( -\frac{2}{(at + x + b)^2} \right) = -\frac{2a}{(at + x + b)^2} = u_t$$

so $u(x, t)$ is a solution of the PDE.

Kildesett: course=TMA4135 term=host year=2022 problem=6 file=math4nd-2022h_published.pdf
