### **Solution to Problem 7**

a) We have the fixed-point equation $x = g(x)$, where $g(x) = \sqrt{x + 2}$. The fixed-point theorem, which guarantees the existence of the unique root $r$ and also the convergence of the fixed-point iterations, depend on properties of the function $g(x)$. We need to verify the following conditions:

1) There exists a positive constant $L < 1$ so that $|g(x)'| \leq L$ for all $x \in [1, 9]$

2) The function $g(x)$ stays within the interval of interest, that is: $g(x) \in [1, 9]$ for all $x \in [1, 9]$.

To check the first one, we must differentiate $g(x)$:

$$g(x) = x^{\frac{1}{2}} + 2 \Rightarrow g'(x) = \frac{1}{2} x^{\frac{1}{2} - 1} = \frac{1}{2\sqrt{x}}.$$

Since $\sqrt{x} > 0$ for all $x > 0$, we have simply

$$|g'(x)| = g'(x) = \frac{1}{2\sqrt{x}},$$

which is of course a strictly decreasing function, because the square root function $\sqrt{x}$ in the denominator is increasing. Since $|g'(x)|$ is strictly decreasing, we know that its maximum value in the interval $x \in [1, 9]$ is simply $|g'(1)|$. Hence:

$$|g'(x)| \leq |g'(1)| = \frac{1}{2\sqrt{1}} = \frac{1}{2} \quad \text{for all } x \in [1, 9].$$

The first condition of the theorem is therefore met, with $L = 1/2$.

Then, since $g(x)$ is clearly an increasing function, we know that its minimum and maximum values within the interval happen for $x = 1$ and $x = 9$, respectively:

$$g(1) \leq g(x) \leq g(9) \Rightarrow 3 \leq g(x) \leq 5.$$

Having $g(x) \in [3, 5]$ implies, in particular, $g(x) \in [1, 9]$, since the interval $[1, 9]$ contains $[3, 5]$. The last condition is thus fulfilled, which shows that the fixed-point iterations will convergence to the root $r$, for any initial guess $x_0 \in [1, 9]$.

b) As a consequence of the fixed-point theorem, we have the a-priori error estimate

$$|x_{k+1} - r| \leq \frac{L^{k+1}}{1 - L} |g(x_0) - x_0|.$$

Therefore, if we find $k$ such that

$$\frac{L^{k+1}}{1 - L} |g(x_0) - x_0| = 2^{-10},$$

then we know for sure that we will also have $|x_{k+1} - r| \leq 2^{-10}$. We therefore have to solve the equation above for $k$, with $L = 1/2$, $x_0 = 2$ and $g(x_0) = \sqrt{x_0} + 2 = \sqrt{2} + 2$. This gives us

$$2^{-10} = \frac{(1/2)^{k+1}}{1 - 1/2} \left| (\sqrt{2} + 2) - 2 \right| = \left( \frac{1}{2} \right)^{k} |\sqrt{2}| \iff 2^{-k} = 2^{-10.5} \iff k = 10.5.$$

Since we cannot perform “half an iteration”, we must round $k$ up to 11.

Kildesett: course=TMA4135 term=host year=2022 problem=7 file=math4nd-2022h_published.pdf
