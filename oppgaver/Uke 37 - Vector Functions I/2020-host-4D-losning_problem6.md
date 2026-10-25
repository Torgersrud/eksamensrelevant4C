### **Solution to Problem 6**

**Part a), Version I:** Since $g'(x)\geq 0.1$, the function $g$ is (strictly) increasing. Since moreover $g(0)\geq 0$ and $g(1)\leq 1$, it follows that $0\leq g(x)\leq 1$ for all $x\in[0,1]$. That is, the function $g$ maps the interval $[0,1]$ to itself. Moreover, the derivative of $g$ satisfies the condition $|g'(x)|\leq L:=0.9<1$ for all $x\in[0,1]$. Thus all the conditions of the fixed point theorem are satisfied, and therefore $g$ has a unique fixed point $r$ in the interval $[0,1]$ and the fixed point iteration converges to $r$.

**Version II:** Here the function is strictly decreasing, and $g(0)\leq 1$, $g(1)\geq 0$. Else the argumentation is the same as for version I.

**Version III:** Here we have that $|g(x)|\leq L:=0.8<1$. Else the argumentation is the same as for version I.

**Version IV:** Here the function is strictly decreasing, and $g(0)\leq 1$, $g(1)\geq 0$. Moreover, $|g(x)|\leq L:=0.8<1$. Else the argumentation is the same as for version I.

**Part b)** For the number of iterations, we have the a–priori error estimate

$$|x_k-r|\leq\frac{L^k}{1-L}|g(x_0)-x_0|.$$

Thus we need that

$$\frac{L^k}{1-L}|g(x_0)-x_0|\leq 10^{-6}$$

or, as $x_0=0$,

$$L^k\leq 10^{-6}\frac{(1-L)}{|g(x_0)|}.$$

Taking logarithms on each side and dividing by $\log(L)$ (note that $\log(L)<0$, which explains why the inequality is reversed!), we obtain the condition

$$k\geq\frac{1}{\log(L)}\log\Big(10^{-6}\frac{(1-L)}{|g(x_0)|}\Big).$$

**Version I:** Here we have $L=0.9$ and $g(x_0)=0.2$. This results in the estimate

$$k\geq\frac{\log 0.5\cdot 10^{-6}}{\log 0.9}\approx 137.7.$$

That is, we need at most 138 iterations.

**Version II:** Here we have $L=0.9$ and $g(x_0)=0.7$. This results in the estimate

$$k\geq\frac{\log((1/7)\cdot 10^{-6})}{\log 0.9}\approx 149.6.$$

That is, we need at most 150 iterations.

**Version III:** Here we have $L=0.8$ and $g(x_0)=0.4$. This results in the estimate

$$k\geq\frac{\log 0.5\cdot 10^{-6}}{\log 0.8}\approx 65.01.$$

That is, we need at most 66 iterations.

**Version IV:** Here we have $L=0.8$ and $g(x_0)=0.8$. This results in the estimate

$$k\geq\frac{\log 0.25\cdot 10^{-6}}{\log 0.8}\approx 68.1.$$

That is, we need at most 69 iterations.

**Alternatives:**

Replacing $|g(x_0)-x_0|$ by $1$ (which is the length of the interval) in the a–priori error estimate yields also a valid solution, though the estimate is weaker. For versions I and II, this results in 153 iterations; for versions III and IV in 70 iterations.

Finally, an alternative is the estimate

$$|x_k-r|\leq L^k|x_0-r|\leq L^k,$$

which yields the estimate

$$k\geq\log(10(-6))/\log(L).$$

For versions I and II, this yields at most 132 iterations; for versions III and IV, at most 62 iterations.

Kildesett: course=TMA4135 term=host year=2020 problem=6 points=10 file=completeexam_nosolutions.pdf
