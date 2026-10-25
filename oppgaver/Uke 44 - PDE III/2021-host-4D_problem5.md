### **Problem 5**

In an alternative (and perhaps more realistic) model of the temperature distribution in the steel beam, we take into account that the beam has finite length $2L > 2$. The beam is again insulated – also at the ends $x = \pm L$.

**a)** Prove that if a function $v \colon (-L, L) \to \mathbb{R}$ is even and differentiable, then $v'(0) = 0$.

**b)** Under the same assumptions as in the previous Problem (except for the finite length), argue that the temperature $u(x,t)$ in the **right half** of the beam ($0 \leq x \leq L$) at time $t > 0$, can be modelled as

$$u_t(x,t) = u_{xx}(x,t), \quad t > 0, x \in (0, L),$$

with boundary conditions

$$u_x(0,t) = 0 = u_x(L,t),$$

and with initial condition

$$u(x,0) = \begin{cases}1, & \text{ if } 0 \leq x < 1,\\ 0, & \text{ if } 1 \leq x \leq L.\end{cases}$$

Solve the problem using separation of variables and Fourier series.

**c)** Find a formula for the function $E \colon [0, \infty) \to \mathbb{R}$ given by

$$E(t) := \int_0^L u(x,t) \, \mathrm{d}x.$$

**Hint:** What is $E'(t)$?

What is the physical interpretation of $E$?

**d)** At what time is the temperature at $x = 0$ reduced to one half of the initial temperature according to this new model? You just need to state the equation. Don´t try to solve it. From physical considerations, what will happen if $L \leq 2$?

Kildesett: course=TMA4135 term=host year=2021 problem=5 file=tma4135_2021h_exam-4.pdf
