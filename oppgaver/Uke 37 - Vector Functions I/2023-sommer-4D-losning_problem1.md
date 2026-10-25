### **Solution to Problem 1**

a) We have the fixed-point equation $x = g(x)$, where $g(x) = \sqrt{\sin x}$. The fixed-point theorem, which guarantees the existence of the unique root $r$ and also the convergence of the fixed-point iterations, depend on properties of the function $g(x)$. We need to verify the following conditions:

1) There exists a positive constant $L < 1$ so that $|g(x)'| \leq L$ for all $x \in [\pi/6, \pi/2]$

2) The function $g(x)$ stays within the interval of interest, that is: $g(x) \in [\pi/6, \pi/2]$ for all $x \in [\pi/6, \pi/2]$.

To check the first one, we must differentiate $g(x)$:

$$g(x) = (\sin x)^{\frac{1}{2}} \ \ \Rightarrow g'(x) = \frac{1}{2} (\sin x)^{\frac{1}{2} - 1} (\sin x)' = \frac{\cos x}{2 \sqrt{\sin x}} \, .$$

Since $\cos x > 0$ for all $x \in [\pi/6, \pi/2]$, we have simply

$$|g'(x)| = g'(x) = \frac{\cos x}{2 \sqrt{\sin x}} \, ,$$

which is a **decreasing** function for $x \in [\pi/6, \pi/2]$, since the numerator is decreasing and the denominator is increasing (in the interval considered). Because $|g'(x)|$ is decreasing, we know that its maximum value in the interval $x \in [\pi/6, \pi/2]$ is simply $|g'(\pi/6)|$. Hence:

$$|g'(x)| \leq |g'(\pi/6)| = \frac{\sqrt{3/2}}{2 \sqrt{1/2}} = \frac{\sqrt{6}}{4} < 1 \, .$$

The first condition of the theorem is therefore met, with $L = \sqrt{6}/4 \approx 0.612$.

Then, since $g(x)$ is clearly an **increasing function**, we know that its minimum and maximum values within the interval happen for $x = \pi/6$ and $x = \pi/2$, respectively:

$$g(\pi/6) \leq g(x) \leq g(\pi/2) \ \ \Rightarrow \sqrt{2}/2 \leq g(x) \leq 1 \, .$$

Having $g(x) \in [\sqrt{2}/2, 1]$ implies, in particular, $g(x) \in [\pi/6, \pi/2]$, since the interval $[\pi/6, \pi/2]$ contains $[\sqrt{2}/2, 1]$. The last condition is thus fulfilled, which shows that the fixed-point iterations will convergence to the root $r$, for any initial guess $x_0 \in [\pi/6, \pi/2]$.

b) As a consequence of the fixed-point theorem, we have the a-priori error estimate

$$|x_{k+1} - r| \leq \frac{L^{k+1}}{1 - L} |g(x_0) - x_0|.$$

Therefore, for $k = 60$ we have

$$|x_{61} - r| \leq \frac{(\sqrt{6}/4)^{60+1}}{1 - \sqrt{6}/4} \Big| \sqrt{\sin \pi/2} - \pi/2 \Big| \approx 1.5 \times 10^{-13} \, .$$

*If the student found the wrong constant $L$ in item a), used this wrong value in b) but proceeded correctly, that is OK for item b). It is also OK if the student did the calculations considering $k + 1 = 60$ instead of $k = 60$.*

Kildesett: course=TMA4135 term=sommer year=2023 problem=1 file=tma4125-30-35-matematikk4n-d-2023s_lf_correct.pdf
