### **Problem 6**

We want to use a fixed point iteration $x_{k+1} = g(x_k)$, $k = 0, 1, \ldots$ to solve the nonlinear equation

$$0 = f(x) = \exp(x) - 2\;,\qquad (3)$$

a) Find all solutions of (3) using basic calculus. Reason why these are in fact all solutions.

b) Consider the following choices for g – both given by a Python code snippet (assume that the numpy library is imported)

- (i)

  ```python
  def g1(x):
      return -2*(exp(x)-2)/4 + x
  ```

  (ii)

  ```python
  def g1(x):
      return -(exp(x)-2)/4 + x
  ```

  (iii)

  ```python
  def g1(x):
      return 2*(exp(x)-2)/4 + x
  ```

  (iv)

  ```python
  def g1(x):
      return (exp(x)-2)/4 + x
  ```

-

  ```python
  def g2(x):
      return exp(x) - 2*x - 2 + 3*log(2)
  ```

  Based on the convergence theorem for fixed point iterations (The fixed point theorem), prove or disprove in both cases whether the fixed point iteration converges towards a solution of $f(x) = 0$ if the initial guess $x_0$ is chosen sufficiently close to a solution. What order of convergence do you expect in the case of $g_2$ and why?

c) Write down Python code that implements the according fixed point iteration function of Newton's method for problem (3).

Kildesett: course=TMA4135 term=kont year=2021 problem=6 file=retake_lf.pdf
