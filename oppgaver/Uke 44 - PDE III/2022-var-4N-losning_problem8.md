### **Solution to Problem 8** (Heat equation, 12 points)

a) We have (2 P.)

$$\frac{\partial u_{n}}{\partial t}-\frac{\partial^{2}u_{n}}{\partial x^{2}}=-{\omega_{n}}^{2}\mathrm{e}^{-\omega_{n}^{2}t}\sin(\omega_{n}x)-\omega_{n}(-\omega_{n})\mathrm{e}^{-\omega_{n}^{2}t}\sin(\omega_{n}x)=0\quad\text{for all }\omega_{n}\in\mathbb{R}\,.$$

The boundary condition at $x=0$ is already satisfied for all $\omega_{n}\in\mathbb{R}$ (1 P.)

The condition at $x=1$ require $\sin(\omega_{n}\cdot 1)=0$, since $\mathrm{e}^{-\omega_{n}^{2}t}\ne 0$, that is, (1 P.)

$$\omega_{n}=n\pi\,,\quad\text{with}\quad n\in\mathbb{N}\,.$$

We can thus write $u_{n}(x,t)=\mathrm{e}^{-(n\pi)^{2}t}\sin(n\pi x)$. (1 P.)

b) We can verify by computing the derivatives (3 P.)

$$\frac{\partial v}{\partial t}=0\quad\text{and}\quad\frac{\partial^{2}v}{\partial x^{2}}=-\sin(3\pi x)\,,\quad\text{that}\quad\frac{\partial v}{\partial t}-\frac{\partial^{2}v}{\partial x^{2}}=0-(-\sin(3\pi x))=\sin(3\pi x)\,.$$

At the boundary we obtain (2 P.)

$$v(0,t)=\frac{1}{9\pi^{2}}\sin(0)=0\quad\text{and}\quad v(1,t)=\frac{1}{9\pi^{2}}\sin(3\pi)=0\,.$$

c) The initial conditions require (1 P.)

$$0=u(x,0)=\frac{1}{9\pi^{2}}\sin(3\pi x)+\sum_{n=1}^{\infty}B_{n}\sin(n\pi x)\,,\quad\text{that is,}\quad\sum_{n=1}^{\infty}B_{n}\sin n\pi x=-\frac{1}{9\pi^{2}}\sin(3\pi x)\,.$$

Hence, $B_{n}$ are the coefficients of a Fourier series. Since the right-hand side is one of the summands (with a prefactor), we can directly read of the coefficients(1 P.)

$$B_{n}=\begin{cases}-\frac{1}{9\pi^{2}}&\text{if }n=3\\ 0&\text{else.}\end{cases}$$

Kildesett: course=TMA4125 term=var year=2022 problem=8 points=12 file=TMA4125-Matematikk-4N-2022v_lf.pdf
