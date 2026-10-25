### **Solution to Problem 3**

**a)** We see that $f$ can be written as $f(t) = \operatorname{erf}\left(\frac{1}{2\sqrt{t}}\right) - \frac{1}{2}$. The derivative of erf is $\operatorname{erf}'(x) = \frac{2}{\sqrt{\pi}} e^{-x^2} > 0$. By the chain rule

$$f'(t) = -\operatorname{erf}'\left(\frac{1}{2\sqrt{t}}\right) \frac{1}{4t^{3/2}} = -\frac{e^{-\frac{1}{4t}}}{2\sqrt{\pi} t^{3/2}} < 0,$$

and $f$ is strictly decreasing on $(0, \infty)$. Thus, any solution $T$ is unique.

Moreover, $f$ is continuous with $\lim_{t \to \infty} f(t) = \operatorname{erf}(0) - \frac{1}{2} = -\frac{1}{2} < 0$, and, by the famous identity,

$$\begin{aligned} \lim_{t \to 0^+} f(t) &= \lim_{x \to \infty} \operatorname{erf}(x) - \frac{1}{2} \\ &= \frac{2}{\sqrt{\pi}} \int_0^{\infty} e^{-z^2} \, \mathrm{d}z - \frac{1}{2} \\ &= \frac{2}{\sqrt{\pi}} \frac{\sqrt{\pi}}{2} - \frac{1}{2} \\ &= \frac{1}{2} > 0 \end{aligned}$$

since the integrand $e^{-z^2}$ is an even function. This shows that there is a unique number $T > 0$ such that $f(T) = 0$.

If we choose $t^*$ such that $\frac{1}{2\sqrt{t^*}} = 0.4$, then we know from Problem 2 that $f(t^*) = \operatorname{erf}(0.4) - 0.5 = 0.4284 - 0.5 = -0.0716 < 0$. Since $f$ is decreasing, the solution $T$ must be less than $t^*$. In other words, $T < t^* = \frac{1}{(2 \cdot 0.4)^2} = \left(\frac{5}{4}\right)^2 = 1.5625$ is an upper bound.

**b)** Newtons method: $t_{k+1} = t_k - \frac{f(t_k)}{f'(t_k)}$.

With $t_0 = t^* = \left(\frac{5}{4}\right)^2$, we have already computed that $f(t_0) = -0.0716$. Next,

$$\begin{aligned} f'(t_0) &= -\frac{e^{-\frac{1}{4t_0}}}{2\sqrt{\pi} t_0^{3/2}} \\ &= -\frac{4^3 e^{-\frac{4}{25}}}{2\sqrt{\pi} 5^3} \\ &= -\frac{32 e^{-\frac{4}{25}}}{125\sqrt{\pi}} \\ &\approx -0.12308. \end{aligned}$$

Thus,

$$\begin{aligned} t_1 &= t_0 - \frac{f(t_0)}{f'(t_0)} \\ &\approx \frac{25}{16} - \frac{-0.0716}{-0.12308} \\ &= 0.9810. \end{aligned}$$

(The exact solution to $f(t) = 0$ is T = 1.09905467.. We see that $t_1$ is much closer than $t_0$, but still not very accurate. However, $t_1$ is the best answer we can make at this point.)

Kildesett: course=TMA4135 term=host year=2021 problem=3 file=tma4135_2021h_exam-4.pdf
