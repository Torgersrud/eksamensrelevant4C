### **Solution to Problem 9**

- *Discretisation of the domain and equation:*

  We start by defining the grid points $x_i = ih = 0.25i$, $i = 0, \ldots, 4$, and $t_n = nk = 0.1n$, $n = 0, 1, 2, \ldots$

  Next we use that

  $$u_t(x_i, t_n) = \frac{u(x_i, t_{n+1}) - u(x_i, t_n)}{k} + O(k),$$
  $$u_{xx}(x_i, t_n) = \frac{u(x_{i+1}, t_n) - 2u(x_i, t_n) + u(x_{i-1}, t_n)}{h^2} + O(h^2).$$

  We now ignore the error terms, approximate $U_i^n \approx u(x_i, t_n)$, and insert the finite difference approximations in the PDE. Then we obtain the equation

  $$\frac{U_i^{n+1} - U_i^n}{k} = \frac{1}{4} \frac{U_{i-1}^n - 2U_i^n + U_{i+1}^n}{h^2}.$$

  Solving this for $U_i^{n+1}$, we obtain the expressions

  $$U_i^{n+1} = U_i^n + \frac{k}{4h^2} \left( U_{i-1}^n - 2U_i^n + U_{i+1}^n \right) = 0.2 U_i^n + 0.4 (U_{i-1}^n + U_{i+1}^n) \qquad (1)$$

  for $i = 1, 2, 3$, and $n = 1, 2, 3, \ldots$, where we have used that $k/4h^2 = 0.1/0.25 = 0.4$.

- *Boundary conditions:*

  For $i = 1$ and $i = 3$, the expressions above depend on $U_0^n$ and $U_4^n$, which we need to define using the boundary conditions $u(0, t) = \cos(t)$ and $u(1, t) = 0$. From these we obtain that

  $$U_0^n = \cos(t_n) = \cos(0.1n) \qquad \text{and} \qquad U_4^n = 0,$$

  which we use in (1)

- *Initial conditions:*

  For $n = 0$ we make use of the initial condition $u(x, 0) = 1 - x$, which yields

  $$U_i^0 = 1 - x_i = 1 - 0.25i \qquad \text{for } i = 0, \ldots, 4.$$

- *Complete algorithm:*

  Summarising everything above, we obtain the following method:

  *Initialise:* Define

  $$U_i^0 = 1 - 0.25i \qquad \text{for } i = 1, 2, 3.$$

  *Iteration:* For $n = 1, 2, \ldots$ define

  $$U_0^n = \cos(0.1n) \qquad \text{and} \qquad U_4^n = 0,$$

  and compute

  $$U_i^{n+1} = 0.2 U_i^n + 0.4 (U_{i-1}^n + U_{i+1}^n) \qquad \text{for } i = 1, 2, 3.$$

Finally, we use this method for approximating $u(0.25, 0.2)$. We are using a step length $h = 0.25$ in spatial direction and a step length $k = 0.1$ in temporal direction, and thus $(0.25, 0.2) = (h, 2k) = (x_1, t_2)$. That is, we have the approximation $u(0.25, 0.2) \approx U_1^2$, which means that we have to compute $U_1^2$ with the algorithm defined above. We initialise

$$U_0^0 = 1, \quad U_1^0 = 0.75, \quad U_2^0 = 0.5, \quad U_3^0 = 0.25, \quad U_4^0 = 0.$$

Next we compute the values $U_i^1$ for $i = 1, 2, 3$ (we actually do not need $U_3^1$ for the computation of $U_1^2$):

$$U_1^1 = 0.2 U_1^0 + 0.4 (U_0^0 + U_2^0) = 0.75,$$
$$U_2^1 = 0.2 U_2^0 + 0.4 (U_1^0 + U_3^0) = 0.5,$$
$$U_3^1 = 0.2 U_3^0 + 0.4 (U_2^0 + U_4^0) = 0.25.$$

Finally, we set $U_0^1 = \cos(0.1)$ and compute

$$U_1^2 = 0.2 U_1^1 + 0.4 (U_0^1 + U_2^1) = 0.15 + 0.4 \cos(0.1) + 0.2 \approx 0.748.$$

Thus

$$u(0.25, 0.2) \approx U_1^2 \approx 0.748.$$

Kildesett: course=TMA4135 term=sommer year=2023 problem=9 file=tma4125-30-35-matematikk4n-d-2023s_lf_correct.pdf
