### **Solution to Problem 5**

**a)** Replacing $h$ with $-h$ and using that $v(-h) = v(h)$ in the definition of $v'(0)$ gives

$$\begin{aligned} v'(0) &= \lim_{h \to 0} \frac{v(h) - v(0)}{h} \\ &= \lim_{h \to 0} \frac{v(-h) - v(0)}{-h} \\ &= -\lim_{h \to 0} \frac{v(h) - v(0)}{h} \\ &= -v'(0). \end{aligned}$$

That is, $v'(0) = 0$.

We can also use the chain rule,

$$\begin{aligned} v'(x) &= \frac{\mathrm{d}}{\mathrm{d}x} v(x) \\ &= \frac{\mathrm{d}}{\mathrm{d}x} v(-x) \\ &= v'(-x) \cdot (-1) = -v'(-x) \end{aligned}$$

proving (the more general result) that the derivative of an even functions is odd. Again, $v'(0) = -v'(0)$.

**b)** The boundary condition $u_x(L,t) = 0$ is inflicted by the fact that the beam is insulated at the end point. By the symmetry of the situation, it is reasonable to expect that, at any given time, the temperature at $x$ is the same as the temperature at $-x$. That is, $u(x,t) = u(-x,t)$. Part **a)** then explains the boundary condition $u_x(0,t) = 0$. Otherwise, the PDE and the initial condition are the same as in Problem 4.

We look for solutions of the PDE and the boundary conditions on the form $u(x,t) = F(x)G(t)$. Differentiation and separating the variables will give the two ODE´ s

$$F''(x) = kF(x) \qquad \text{and} \qquad G'(t) = kG(t),$$

where the constant $k = -\lambda^2 \leq 0$ since otherwise $G(t) \to \pm\infty$.

$\lambda = 0$ produces $F(x) = Ax + B$, and the boundary conditions $u_x = 0$ at the end points makes $F$ constant. We thus define

$$u_0(x,t) := 1.$$

With $\lambda^2 > 0$ we get $F(x) = A\cos\lambda x + B\sin\lambda x$. Then $F'(x) = \lambda(-A\sin\lambda x + B\cos\lambda x)$ and

$$0 = u_x(0,t) = F'(0)G(t) = \lambda B G(t).$$

In order to avoid setting $G$ constant equal to zero, we must have $B = 0$. Similarly,

$$0 = F'(L) = -\lambda A \sin\lambda L$$

which restricts $\lambda$ to the numbers

$$\lambda_n := \frac{\pi}{L} n, \qquad n \in \mathbb{N}.$$

The possible solutions for $G$ are then $G(t) = C e^{-\lambda_n^2 t}$. Therefore, for every $n = 1, 2, \ldots,$ the functions

$$u_n(x,t) := e^{-\lambda_n^2 t} \cos\lambda_n x,$$

together with any linear combination of them, will be a solution to the PDE and the boundary conditions.

Using Fourier series, we try to find a combination

$$u(x,t) = a_0 + \sum_{n=1}^{\infty} a_n e^{-\lambda_n^2 t} \cos\lambda_n x$$

that also satisfies the initial condition $g(x) := 1$ if $0 \leq x < 1$, $g(x) := 0$ if $1 < x \leq L$. We want

$$g(x) = u(x,0) = \sum_{n=1}^{\infty} a_n \cos\lambda_n x,$$

which we see is obtained (at least for $x \neq 1$) if we choose $a_n$ to be the Fourier coefficients of the even expansion of $g$. That is,

$$\begin{aligned} a_0 &= \frac{1}{L} \int_0^L g(x) \, \mathrm{d}x \\ &= \frac{1}{L} \int_0^1 \mathrm{d}x = \frac{1}{L}, \\ a_n &= \frac{2}{L} \int_0^L g(x) \cos\frac{\pi}{L} n x \, \mathrm{d}x \\ &= \frac{2}{L} \int_0^1 \cos\lambda_n x \, \mathrm{d}x \\ &= \frac{2}{L\lambda_n} \bigg|_0^1 \sin\lambda_n x \\ &= \frac{2}{L\lambda_n} (\sin\lambda_n - 0) \\ &= \frac{2}{\pi n} \sin\frac{\pi}{L} n. \end{aligned}$$

The solution to the problem is therefore

$$u(x,t) = \frac{1}{L} + \frac{2}{\pi} \sum_{n=1}^{\infty} \frac{\sin\frac{\pi}{L} n}{n} e^{-\left(\frac{\pi}{L} n\right)^2 t} \cos\frac{\pi}{L} n x.$$

**c)** When $u$ is a solution to the problem in **b)**, then, assuming we can take the derivative inside the integral,

$$\begin{aligned} E'(t) &= \frac{\mathrm{d}}{\mathrm{d}t} \int_0^L u(x,t) \, \mathrm{d}x \\ &= \int_0^L u_t(x,t) \, \mathrm{d}x \\ &= \int_0^L u_{xx}(x,t) \, \mathrm{d}x \\ &= \bigg|_{x=0}^L u_x(x,t) \\ &= u_x(L,t) - u_x(0,t) = 0 \end{aligned}$$

by the boundary conditions. Thus, $E$ is constant and

$$E(t) = E(0) = \int_0^L u(x,0) \, \mathrm{d}x = \int_0^1 \mathrm{d}x = 1.$$

When the material is homogenous, as in a steel beam, the temperature is proportional to the amount of heat, or energy, per unit of length. The integral $E(t)$ is therefore a measure of the total energy in the beam at time $t$. As the beam was totally insulated, it makes sense that $E$ is constant.

**d)** The equation whos solution gives the time the temperature at the middle of the beam is one half of the initial value is now

$$\frac{1}{2} = u(0,t) = \frac{1}{L} + \frac{2}{\pi} \sum_{n=1}^{\infty} \frac{\sin\frac{\pi}{L} n}{n} e^{-\left(\frac{\pi}{L} n\right)^2 t}.$$

We expect the temperature at $x = 0$ to be strictly decreasing towards the average temperature $1/L$. Thus, if $L \leq 2$, then

$$u(0,t) > \frac{1}{L} \geq \frac{1}{2}$$

and there will be **no** solution to the equation.

Kildesett: course=TMA4135 term=host year=2021 problem=5 file=tma4135_2021h_exam-4.pdf
