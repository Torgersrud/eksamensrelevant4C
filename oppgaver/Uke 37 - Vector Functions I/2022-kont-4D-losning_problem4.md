### **Solution to Problem 4**

a) The elements of the sequence lie obviously all in $\mathbb{R}_0^+$. The given sequence is an iteration sequence to the fixed point equation

$$x = \underbrace{\frac{3x + 1}{2x + 1}}_{f(x)}, \quad x \in \mathbb{R}_0^+.$$

Here we can directly compute the solutions of $x = f(x)$, which must be in $\mathbb{R}_0^+$:

$$x = \frac{3x + 1}{2x + 1} \iff 2x^2 + x = 3x + 1 \iff \boxed{2x^2 - 2x - 1 = 0}$$

$$x = \frac{2 \pm \sqrt{4 + 2 \cdot 2 \cdot 1}}{2 \cdot 2} = \begin{cases}\frac{1}{2}(1 + \sqrt{3}) \in \mathbb{R}_0^+\\ \frac{1}{2}(1 - \sqrt{3}) \notin \mathbb{R}_0^+\end{cases}$$

If the sequence converges, we have:

$$\lim_{n \to +\infty} x_n = \frac{1}{2}(1 + \sqrt{3}) =: \hat{x}.$$

With $x \in \mathbb{R}_0^+$, it holds $f(x) \in \mathbb{R}_0^+$.

Therefore: $f(\mathbb{R}_0^+) \subseteq \mathbb{R}_0^+$.

However: In $\mathbb{R}_0^+$, we have:

$$f'(x) = \frac{3(2x + 1) - (3x + 1)2}{(2x + 1)^2} = \frac{1}{(2x + 1)^2} > 0$$

Therefore: $f'(x) = 1$ for $x = 0$. Therefore, we consider $f$ only on $D := [1, +\infty[$. It holds $f(D) \subseteq D$, as $f(x) > 1$ for all $x > 0$, and $f'(x) \leq \left(\dfrac{1}{3}\right)^2$ for $x \in D$. Thus, we can use the Banach-fixed point theorem: $\hat{x}$ is a limit point of the given sequence.

b) $\displaystyle |x_5 - \hat{x}| \leq \frac{|x_1 - x_0|}{1 - \frac{1}{9}} \left(\frac{1}{9}\right)^5 = \frac{3}{8}\left(\frac{1}{9}\right)^5 \approx 6.35066 \cdot 10^{-6}.$

Kildesett: course=TMA4135 term=kont year=2022 problem=4 points=12 file=TMA4135-Matematikk-4D-2022s_lf.pdf
