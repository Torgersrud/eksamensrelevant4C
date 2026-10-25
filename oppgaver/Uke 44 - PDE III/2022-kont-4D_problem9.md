### **Problem 9.** (Heat equation, 12 pts)

Consider the following heat equation

$$u_t(x, t) = c^2 u_{xx}(x, t), \quad t > 0, \; x \in (0, 4\pi)$$

with boundary conditions

$$u(0, t) = u(4\pi, t) = 0, \quad t > 0$$

and initial condition

$$u(x, 0) = \max\{0, -\sin(x/2)\}, \quad x \in (0, 4\pi).$$

a) Show that the Fourier sine series solution of this above heat equation with boundary conditions is

$$u(x, t) = \sum_{n=1}^{\infty} u_n(x, t) = \sum_{n=1}^{\infty} B_n \sin\left(\frac{nx}{4}\right) e^{-\frac{c^2 n^2 t}{16}}$$

with real numbers $B_n$, $n \geq 1$, by using the separation of variables method.

b) Compute the Fourier sine series solution of the above heat equation with the given boundary conditions and initial conditions. Write down the three first non-zero terms of the solution.

Hint: You may use the following identities:

$$\sin(a + b) \sin(a - b) = \sin^2(a) - \sin^2(b) \tag{1}$$

$$\int \sin^2(kx) \, dx = -\frac{x}{2} + \frac{\sin(2kx)}{4k} + \text{constant} \qquad \text{for some } k \in \mathbb{R}. \tag{2}$$

Kildesett: course=TMA4135 term=kont year=2022 problem=9 points=12 file=TMA4135-Matematikk-4D-2022s_lf.pdf
