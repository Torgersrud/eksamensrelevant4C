### **Solution to Problem 2** (Fixed-point iteration, 8 pts)

- Yes there is a fixed point since

  $$-1 < \frac{e^{-1}}{10} < \frac{e^{1}}{10} < 1 \quad \text{and} \quad e^x \text{ is monotone},$$

  (otherwise only looking at end point values of $g(x)$ is not sufficient) so

  $$-1 < \frac{e^x}{10} < 1 \quad \text{for } x \in [-1, 1].$$

  thus according to our criteria in lecture (?) $g(x) = \dfrac{e^x}{10}$ has a fixed point in $[-1, 1]$. (4 pts)

  - [?] "lecture (?)": the lecture number in the handwritten scheme is not legible.

- Yes it is unique, since

  $$\big| g'(x) \big| = \left| \frac{e^x}{10} \right| \le \frac{e^1}{10} < 1 \quad \text{on } [-1, 1]$$

  since $g'(x) = g(x) > 0$ and $g'$ is monotone. (4 pts)

Kildesett: course=TMA4125 term=var year=2020 problem=2 file=exam_v20_short.pdf points=8
