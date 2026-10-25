### **Solution to Problem 6**

a) $\exp(x) - 2 = 0$ is equivalent to $x = \ln(2)$. These are all solutions, as the function $f(x) = \exp(x) - 2$ is strictly monotone.

b) The fixed point of $g_1$ is $x = \ln(2)$. $x = -M\cdot(\exp(x) - 2)/4 + x$ is equivalent to $x = \ln(2)$, and so $\ln(2)$ is a fixed point of $g_1$. We have $|g_1'(x)| = |-\frac{M}{4}\cdot\exp(x) + 1|\Big|_{x=\ln(2)} = |-\frac{M}{2} + 1|$. We have the following variants:

- $M = -2$: $|g_1'(x)| = |1 + 1| = 2 \not< 1$. So the fixed point iteration does not converge towards a solution of $f(x) = 0$.
- $M = -1$: $|g_1'(x)| = |\frac{1}{2} + 1| = \frac{3}{2} \not< 1$. So the fixed point iteration does not converge towards a solution of $f(x) = 0$.
- $M = 1$: $|g_1'(x)| = |-\frac{1}{2} + 1| = \frac{1}{2} < 1$. So the fixed point iteration converges towards a solution of $f(x) = 0$.
- $M = 2$: $|g_1'(x)| = |-\;1 + 1| = 0 < 1$. So the fixed point iteration converges towards a solution of $f(x) = 0$.

We can easily see that $x = \ln(2)$ satisfies $x = g_2(x)$, and therefore, $x = \ln(2)$ is a fixed point of $g_2$. We have $|g_2'(x)| = |\;\exp(x) - 2|\Big|_{x=\ln(2)} = 0 < 1$. So the fixed point iteration converges towards a solution of $f(x) = 0$.

As the value of the derivative is zero, one should locally expect (at least) second order convergence (as in the proof for convergence of Newton's method)

(c) For the above function $f$, the derivative is given by $f'(x) = \exp(x)$. For Newton's method, one therefore obtains

$$x_{k+1} = x_k - f(x_k)/f'(x_k) = g_{Newton}(x_k) = x_k - \frac{\exp(x) - 2}{\exp(x)}$$

As Python code, this can be implemented in various ways, straightforward, it is similar to

```python
def gNewton(x):
    return x - (exp(x)-2)/exp(x)
```

Kildesett: course=TMA4135 term=kont year=2021 problem=6 file=retake_lf.pdf
