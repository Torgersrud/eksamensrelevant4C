### **Solution to Problem 3** (Heat equation, 12 pts)

**a)** We set

$$u(x,t) = F(x) G(t).$$

This gives

$$F(x) G'(t) = c^2 F''(x) G(t).$$

Separation of variables leads to

$$\frac{G'}{c^2 G} = \frac{F''}{F}.$$

As the left-hand side depends only on $t$ and the right-hand side only on $x$, both fractions must be equal to a constant, say $k$. For $k \ge 0$ we get the trivial solution $u \equiv 0$. Therefore, $k < 0$, and we set $k = -p^2$. We get the two ODEs:

$$\begin{aligned}F'' + p^2 F &= 0\\ G' + c^2 p^2 G &= 0.\end{aligned}$$

The first ODE has the general solution

$$F(x) = A \cos(px) + B \sin(px).$$

Using the boundary conditions, we get

$$u(0,t) = F(0) G(t) = 0 = u(\pi,t) = F(\pi) G(t).$$

This gives $F(0) = F(\pi) = 0$, as otherwise we would get $G(t) \equiv 0$. Then $F(0) = A = 0$ and $F(\pi) = B \sin(p\pi) = 0$ with $B \neq 0$, thus $p = \frac{n\pi}{\pi} = n$, $n = 1, 2, \ldots$. We can set $B = 1$ and obtain $F_n(x) = \sin(nx)$. The second ODE has the form (with $p = n$)

$$G' + c^2 p^2 G = G' + (cn)^2 G = 0.$$

Its general solution is

$$G_n = B_n e^{-(cn)^2 t}$$

Hence, the function

$$u(x,t) = F_n G_n = B_n \sin(nx) e^{-(cn)^2 t}$$

solves the heat equation with the given boundary conditions. Therefore, the series

$$u(x,t) = \sum_{n=1}^{\infty} u_n(x,t) = \sum_{n=1}^{\infty} B_n \sin(nx) e^{-c^2 n^2 t}$$

is also a solution of the problem.

**b)** The solution of the problem is

$$u(x,t) = \sum_{n=1}^{\infty} u_n(x,t) = \sum_{n=1}^{\infty} B_n \sin(nx) e^{-c^2 n^2 t}.$$

The initial condition gives

$$u(x,0) = \sum_{n=1}^{\infty} u_n(x,t) = \sum_{n=1}^{\infty} B_n \sin(nx) = \frac{\pi}{2} - \left| x - \frac{\pi}{2} \right|$$

with

$$\begin{aligned}B_n &= \frac{2}{\pi} \int_{0}^{\pi} \left( \frac{\pi}{2} - \left| x - \frac{\pi}{2} \right| \right) \sin(nx) dx\\ &= \frac{2}{\pi} \left( \int_{0}^{\pi/2} x \cdot \sin(nx) dx + \int_{\pi/2}^{\pi} (\pi - x) \cdot \sin(nx) dx \right)\\ &= \frac{2}{\pi} \cdot \left( \left[ -x \cdot \frac{\cos(nx)}{n} \right]_0^{\pi/2} + \int_{0}^{\pi/2} \frac{\cos(nx)}{n} dx + \left[ (x - \pi) \cdot \frac{\cos(nx)}{n} \right]_{\pi/2}^{\pi} - \int_{\pi/2}^{\pi} \frac{\cos(nx)}{n} dx \right)\\ &= \frac{2}{\pi} \cdot \left( -\frac{\pi}{2n} \cos(n\pi/2) + \frac{1}{n^2} \left[ \sin(nx) \right]_0^{\pi/2} + \frac{\pi}{2n} \cos(n\pi/2) - \frac{1}{n^2} \left[ \sin(nx) \right]_{\pi/2}^{\pi} \right)\\ &= \frac{2}{\pi n^2} \cdot \left( \sin(n\pi/2) + \sin(n\pi/2) \right)\\ &= \frac{4 \sin\left( \frac{\pi n}{2} \right)}{\pi n^2}\end{aligned}$$

Therefore, we have

$$b_1 = \frac{4}{\pi}, \quad b_2 = 0, \quad b_3 = -\frac{4}{\pi 3^3}, \quad b_4 = 0, \quad b_5 = \frac{4}{\pi 5^2}, \cdots$$

So, we have

$$\begin{aligned}u(x,t) &= \sum_{n=1}^{\infty} u_n(x,t) = \sum_{n=1}^{\infty} \frac{4 \sin(\frac{\pi n}{2})}{\pi n^2} \sin(nx) e^{-c^2 n^2 t}\\ &= \frac{4}{\pi} \sin(x) e^{-c^2 t} - \frac{4}{\pi 3^3} \sin(3x) e^{-c^2 3^2 t} + \frac{4}{\pi 5^2} e^{-c^2 5^2 t} \cdots\end{aligned}$$

**Grading manual** Generally, 1-2 pts deduction for each minor/major miscalculations (but no minus points)

**a)** (7p): 1 pt for ansatz/product representation $u(x,t) = F(x) G(t)$,
2 pts for inserting into PDE and deriving the 2 ODEs,
2 pts for deriving final expression for $F(x)$,
1 pt for final expression for $G(t)$,
1 pt for final series $\sum_{n=1}^{\infty} u_n(x,t)$

**b)** (5p): 1 pt for inserting initial condition and finding sin series for $u(x,0)$
3 pts for computing $B_n$
1 pt for final solution

Kildesett: course=TMA4130 term=host year=2021 problem=3 points=12 file=tma4130_2021h_exam.pdf
