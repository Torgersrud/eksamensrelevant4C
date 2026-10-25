### **Problem 9.** (Separation of Variables, 8 points)

Consider the fourth order PDE

$$\frac{\partial^{2}u}{\partial t^{2}}+\frac{\partial^{4}u}{\partial x^{4}}=0,\qquad x\in[0,1],\,t\ge 0.$$

a) Use the Ansatz $u(x,t)=F(x)G(t)$ to transform the PDE into a system of ODEs.

b) Verify that for $\beta>0,A,B\in\mathbb{R}$ all functions of the form

$$F(x)=A\sin(\beta x)+B\cos(\beta x)\qquad\text{(5)}$$

satisfy the ODE for F in a).

We add the following (four) boundary conditions for $t>0$

$$\begin{cases}u(0,t)=u(1,t)=0,\\ \displaystyle\frac{\partial^{2}}{\partial x^{2}}u(0,t)=\frac{\partial^{2}}{\partial x^{2}}u(1,t)=0.\end{cases}$$

For which $\beta,A,B$ do the functions in (5) fulfil the boundary conditions?

c) How many initial conditions would you expect to be given to have a unique solution for $G$?

*Hint.* Compare this PDE to what you know about the heat and wave equation and their second ODE to solve.

d) Which other non-trivial function(s) $F$ also fulfil the ODE derived in a)? State an example. You can ignore the boundary conditions.

Kildesett: course=TMA4125 term=var year=2022 problem=9 points=8 file=TMA4125-Matematikk-4N-2022v_lf.pdf
