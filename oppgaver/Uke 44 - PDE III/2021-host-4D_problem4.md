### **Problem 4**

You are welding on the middle ($x = 0$) of a long, cold, and insulated steel beam. After some simplifying assumptions and an appropriate scaling of the axes, the temperature $u(x,t)$ at the point $x \in \mathbb{R}$ at the time $t > 0$ after you stopped welding, is mathematically modelled as

$$u_t(x,t) = u_{xx}(x,t), \quad t > 0, x \in \mathbb{R},$$

with initial condition

$$u(x,0) = h(x) := \begin{cases}1, & \text{ if } |x| < 1,\\ 0, & \text{ otherwise}.\end{cases}$$

**a)** The problem has a unique solution. Show that the solution is

$$u(x,t) = \frac{1}{2\sqrt{\pi t}} \int_{-1}^{1} e^{-\frac{(x-y)^2}{4t}} \, \mathrm{d}y$$

either by deducing it using Fourier transformation **or** by checking directly that $u$ satisfies the equation and the initial condition in the sense $\lim_{t \to 0^+} u(x,t) = h(x)$. You don´t need to make arguments of the validity when taking differentiation and limits inside integrals. **Hint:** $z := \frac{y-x}{2\sqrt{t}}$.

**b)** Give a formula for the solution $u(x,t)$ in terms of the erf function from Problem 2. Approximately, at what time is the temperature at $x = 0$ reduced to one half of the initial temperature?

Kildesett: course=TMA4135 term=host year=2021 problem=4 file=tma4135_2021h_exam-4.pdf
