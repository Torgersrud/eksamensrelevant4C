### **Problem 6** [10 points]

**There are four versions of this exercise with slightly different assumptions.**

We are given a continuously differentiable function $g\colon[0,1]\to\mathbb{R}$ with the following properties:

**Version I:**

- $g(0)=0.2$ and $g(1)=0.7$.
- $0.1\leq g'(x)\leq 0.9$ for all $0\leq x\leq 1$.

**Version II:**

- $g(0)=0.7$ and $g(1)=0.2$.
- $-0.9\leq g'(x)\leq-0.1$ for all $0\leq x\leq 1$.

**Version III:**

- $g(0)=0.4$ and $g(1)=0.8$.
- $0.2\leq g'(x)\leq 0.8$ for all $0\leq x\leq 1$.

**Version IV:**

- $g(0)=0.8$ and $g(1)=0.4$.
- $-0.8\leq g'(x)\leq-0.2$ for all $0\leq x\leq 1$.

**The remaining part of the exercise is the same for all versions.**

We consider now the fixed point iteration

$$x_{k+1}=g(x_k)$$

with $x_0=0$.

**a)** Show that the function $g$ has a unique fixed point $r$ in the interval $[0,1]$ and that the fixed point iteration converges to $r$.

**b)** Provide an upper bound for the number of iterations that are required until $|x_k-r|\leq 10^{-6}$.

Kildesett: course=TMA4135 term=host year=2020 problem=6 points=10 file=completeexam_nosolutions.pdf
