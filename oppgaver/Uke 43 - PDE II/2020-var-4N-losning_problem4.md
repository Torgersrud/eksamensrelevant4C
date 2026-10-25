### **Solution to Problem 4** (wave equation)

$$\partial_t^2 u = 16\, \partial_x^2 u, \qquad x \in \mathbb{R},\ t > 0$$

Initial condition:

$$u(x,0) = x, \qquad \partial_t u(x,0) = \cos(x)$$

**Solution:**

Use d'Alembert representation formula, then with $c = 4$

$$\begin{aligned} u(x,t) &= \frac{1}{2} \big( (x-4t) + (x+4t) \big) + \frac{1}{2 \cdot 4} \int_{x-4t}^{x+4t} \cos z\, dz \\ &= x + \frac{1}{8} \big( \sin(x+4t) - \sin(x-4t) \big) \\ &= x + \frac{1}{8} \big( 2 \sin 4t \cos x \big). \end{aligned}$$

(5 pts for d'Alembert, 5 pts for simplification.)

- [?] In the handwritten scheme the factor in front of the integral is rendered as "2·4"; the following line's evaluation $1/8$ corroborates this reading ($2c = 2\cdot 4 = 8$).

Kildesett: course=TMA4125 term=var year=2020 problem=4 file=exam_v20_short.pdf
