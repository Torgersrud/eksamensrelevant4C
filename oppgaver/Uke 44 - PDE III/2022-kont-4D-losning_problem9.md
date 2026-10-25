### **Solution to Problem 9**

a) We set

$$u(x, t) = F(x)G(t).$$

This gives

$$F(x)G'(t) = c^2 F''(x)G(t).$$

Separation of variables leads to

$$\frac{G'}{c^2 G} = \frac{F''}{F}.$$

As the left-hand side depends only on $t$ and the right-hand side only on $x$, both fractions must be equal to a constant, say $k$. For $k \geq 0$ we get the trivial solution $u \equiv 0$. Therefore, $k < 0$, and we set $k = -p^2$. We get the two ODEs:

$$F'' + p^2 F = 0$$

$$G' + c^2 p^2 G = 0.$$

The first ODE has the general solution

$$F(x) = A \cos(px) + B \sin(px).$$

Using the boundary conditions, we get

$$u(0, t) = F(0)G(t) = 0 = u(4\pi, t) = F(4\pi)G(t).$$

This gives $F(0) = F(4\pi) = 0$, as otherwise we would get $G(t) \equiv 0$. Then $F(0) = A = 0$ and $F(4\pi) = B \sin(4p\pi) = 0$ with $B \neq 0$, thus $p = \frac{n\pi}{4\pi} = \frac{n}{4}$, $n = 1, 2, \ldots$. We can set $B = 1$ and obtain $F_n(x) = \sin\frac{nx}{4}$. The second ODE has the form (with $p = \frac{n}{4}$)

$$G' + c^2 p^2 G = G' + (cn/4)^2 G = 0.$$

Its general solution is

$$G_n = B_n e^{-(cn/4)^2 t}$$

Hence (for $n = 1, 2, 3, \ldots$), the function

$$u_n(x, t) = F_n G_n = B_n \sin\left(\frac{nx}{4}\right) e^{-(cn/4)^2 t}$$

solves the heat equation with the given boundary conditions. Therefore (i.e. because of the superposition principle), the series

$$u(x, t) = \sum_{n=1}^{\infty} u_n(x, t) = \sum_{n=1}^{\infty} B_n \sin\left(\frac{nx}{4}\right) e^{-\frac{c^2 n^2 t}{16}}$$

is also a solution of the problem.

b) The solution of the problem is

$$u(x, t) = \sum_{n=1}^{\infty} u_n(x, t) = \sum_{n=1}^{\infty} B_n \sin\left(\frac{nx}{4}\right) e^{-\frac{c^2 n^2 t}{16}}.$$

The initial condition gives

$$\begin{aligned} u(x, 0) = \sum_{n=1}^{\infty} u_n(x, t) = \sum_{n=1}^{\infty} B_n \sin\left(\frac{nx}{4}\right) &= \max(0, -\sin(x/2)) \\ &= \begin{cases}0 & \text{if } 0 \leq x \leq 2\pi,\\ -\sin(x/2) & \text{if } 2\pi < x \leq 4\pi\end{cases}\end{aligned}$$

with

$$\begin{aligned} B_n &= \frac{2}{4\pi} \int_0^{4\pi} \max\left(0, -\sin(x/2)\right) \sin\left(\frac{nx}{4}\right) dx \\ &= \frac{1}{2\pi} \int_{2\pi}^{4\pi} -\sin(x/2) \cdot \sin(nx/4) dx. \end{aligned}$$

For even $n$, this is zero (shift interval around zero and cf. lecture)

$$\begin{aligned} &\overset{n\ \mathrm{odd}}{=} \frac{-1}{2\pi} \cdot \int_{2\pi}^{4\pi} \sin\left(\frac{(n+2)x}{8} - \frac{(n-2)x}{8}\right) \cdot \sin\left(\frac{(n+2)x}{8} + \frac{(n-2)x}{8}\right) dx \\ &\overset{(1)}{=} \frac{-1}{2\pi} \cdot \int_{2\pi}^{4\pi} \sin^2\left(\frac{n+2}{8}x\right) - \sin^2\left(\frac{n-2}{8}x\right) dx \\ &\overset{(2)}{=} \frac{-1}{2\pi} \cdot \left[-\frac{x}{2} + \frac{\sin(2(n+2)x/8)}{4\frac{n+2}{8}} - \frac{x}{2} + \frac{\sin(2(n-2)x/8)}{4\frac{n-2}{8}}\right]_{2\pi}^{4\pi} \\ &= \frac{-1}{\pi} \cdot \left[\frac{\sin((n-2)x/4)}{n-2} - \frac{\sin((n+2)x/4)}{n+2}\right]_{2\pi}^{4\pi} \\ &= \frac{-1}{\pi} \cdot \left(\frac{(-1)^{\frac{n-1}{2}}}{n-2} - \frac{(-1)^{\frac{n-1}{2}}}{n+2}\right), \end{aligned}$$

where we only needed the lower integration bounds in the last step. Therefore, we have

$$B_1 = \frac{-8}{3\pi}, \quad B_2 = 0, \quad B_3 = \frac{8}{5\pi}, \quad B_4 = 0, \quad B_5 = \frac{-8}{21\pi}, \ldots$$

Finally, we have

$$\begin{aligned} u(x, t) &= \sum_{n=1}^{\infty} u_n(x, t) = \sum_{n=1}^{\infty} B_n \sin(nx/4) e^{-c^2 n^2 t/16} \\ &= \frac{8}{\pi} \left(-\frac{\sin(x/4)}{3} e^{-c^2 t/16} + \frac{\sin(3x/4)}{5} e^{-9c^2 t/16} - \frac{\sin(5x/4)}{21} e^{-25c^2 t/16} \pm \ldots\right) \end{aligned}$$

Kildesett: course=TMA4135 term=kont year=2022 problem=9 points=12 file=TMA4135-Matematikk-4D-2022s_lf.pdf
