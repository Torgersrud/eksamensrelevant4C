### **Problem 8.** (Heat equation, 12 points)

Consider the following partial differential equation: find $u(x,t)$ that fulfils

$$\begin{aligned}\frac{\partial u}{\partial t}-\frac{\partial^{2}u}{\partial x^{2}}&=\sin(3\pi x)\,,&&\text{(2)}\\ u(0,t)&=u(1,t)=0\,,\quad t\ge 0&&\text{(3)}\\ u(x,0)&=0\,,\quad 0\le x\le 1\,.&&\text{(4)}\end{aligned}$$

which is an inhomogeneous heat equation.

a) Consider the functions $u_{n}(x,t)=\mathrm{e}^{-\omega_{n}^{2}t}\sin(\omega_{n}x)$, with $n\in\mathbb{N}$ and $\omega_{n}\in\mathbb{R}$. Determine the values $\omega_{n}$ such that $u_{n}(0,t)=u_{n}(1,t)=0$, and show that

$$\frac{\partial u_{n}}{\partial t}-\frac{\partial^{2}u_{n}}{\partial x^{2}}=0\,.$$

b) Show that $v(x,t)=\frac{1}{9\pi^{2}}\sin(3\pi x)$ satisfies the equation

$$\frac{\partial v}{\partial t}-\frac{\partial^{2}v}{\partial x^{2}}=\sin(3\pi x)$$

and the boundary conditions $v(0,t)=v(1,t)=0$.

c) Using superposition, the general solution for Eq. (2) with boundary conditions (3) can be written as

$$u(x,t)=\frac{1}{9\pi^{2}}\sin(3\pi x)+\sum_{n=1}^{\infty}B_{n}\mathrm{e}^{-\omega_{n}^{2}t}\sin(\omega_{n}x)\,.$$

Determine the real coefficients $B_{n}$ so that the initial condition (4) is satisfied.

Kildesett: course=TMA4125 term=var year=2022 problem=8 points=12 file=TMA4125-Matematikk-4N-2022v_lf.pdf
