### **Solution to Problem 4** (Wave equation, 10 pts)

Recall that d'Alembert's formula gives a nice expression for the solution to the wave equation

$$\frac{\partial^2 u}{\partial t^2} - c^2 \frac{\partial^2 u}{\partial x^2} = 0$$

on the real line with initial conditions $u(x,0) = f(x)$ and $\frac{\partial u}{\partial t}(x,0) = g(x)$, namely

$$u(x,t) = \frac{1}{2} [f(x+ct) + f(x-ct)] + \frac{1}{2c} \int_{x-ct}^{x+ct} g(s) ds.$$

In our case, we have $c = \frac{1}{2}$, $f(x) = x$ and $g(x) = \cos^2 x$,

$$u(x,t) = \frac{1}{2} [(x+\frac{1}{2}t) + (x-\frac{1}{2}t)] + \int_{x-ct}^{x+ct} \cos^2(s) ds.$$

We can use the trigonometric identities

$$\begin{aligned}\cos^2(\alpha) &= \frac{1}{2} (\cos(2\alpha) + 1)\\ 2\cos\alpha\sin\beta &= \sin(\alpha+\beta) - \sin(\alpha-\beta)\end{aligned}$$

$$\begin{aligned}u(x,t) &= x + \int_{x-ct}^{x+ct} \cos^2(x) \, dx\\ &= x + \int_{x-ct}^{x+ct} \frac{1 + \cos(2s)}{2} \, dx\\ &= x + \frac{x}{2} \bigg|_{x-ct}^{x+ct} + \frac{\sin(2s)}{4} \bigg|_{x-ct}^{x+ct}\\ &= x + ct + \frac{1}{4} \Big( \sin(2(x+ct)) - \sin(2(x-ct)) \Big)\\ &= x + ct + \frac{1}{2} \cos(2x) \sin(2ct)\\ &= x + \frac{1}{2} t + \frac{1}{2} \cos(2x) \sin(t) \quad \text{with } c = \frac{1}{2}.$$

**Grading manual** [10 pts]
Generally, 1-2 pts deduction for each minor/major miscalculations (but no minus points)
4 pts for d'Alembert's formula, e.g. 1 for general d'Alembert formula, 1 pt each for identifying $c, f$ and $g$.
6 pts for computation of the integral

Kildesett: course=TMA4130 term=host year=2021 problem=4 points=10 file=tma4130_2021h_exam.pdf
