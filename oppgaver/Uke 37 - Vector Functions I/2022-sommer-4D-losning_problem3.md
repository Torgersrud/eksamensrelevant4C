### **Solution to Problem 3**

We have

$$f_1'(x) = \begin{cases}\frac{4}{3}\sqrt[3]{x}, & x > 0\\ \frac{4}{3}\sqrt[3]{-x}, & x < 0\end{cases}$$

Newton’s method yields

$$x_{k+1} = x_k - \frac{f_1(x_k)}{f_1'(x_k)} = \frac{1}{4}x_k,$$

for $x \neq 0$. In this case, Newton’s method converges only lineary to zero, i.e.,

$$|x_{k+1} - 0| \leq c\, |x_k - 0|$$

with $0 < c < 1$. Therefore, the method converges for any starting value in $\mathbb{R}$.

For the second function, we have $f_2'(x) = \frac{1}{2\sqrt{|x|}}$ for $x \neq 0$. Using Newton’s method, we get for $x_k > 0$

$$x_{k+1} = x_k - 2\sqrt{x_k}\sqrt{x_k} = -x_k,$$

and for $x_k < 0$

$$x_{k+1} = x_k + 2\sqrt{-x_k}\sqrt{-x_k} = -x_k.$$

This means that the sequence jumps with $x_{2n} = x_0$ and $x_{2n+1} = -x_0$. Hence, Newton’s method does not converge for $f_2$, which means that no interval of convergence can be determined.

Kildesett: course=TMA4135 term=sommer year=2022 problem=3 points=10 file=TMA4125-Matematikk-4N-2022s_lf.pdf
