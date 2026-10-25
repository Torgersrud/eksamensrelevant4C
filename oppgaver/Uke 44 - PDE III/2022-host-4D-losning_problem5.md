### **Solution to Problem 5**

By taking the Fourier transform of the equation with respect to the $x$-variable we obtain the equation

$$\frac{\partial \hat{u}}{\partial t}(\omega, t) = i\omega \hat{u}(\omega, t) + \hat{u}(\omega, t),$$

which simplifies to

$$\frac{\partial \hat{u}}{\partial t}(\omega, t) = (1 + i\omega) \hat{u}(\omega, t).$$

For fixed $\omega$, the solution of this equation is

$$\hat{u}(\omega, t) = C(\omega) e^{(1+i\omega)t}$$

(where the “constant” $C$ depends on the frequency $\omega$). In particular, we obtain for $t = 0$ the equation

$$\hat{u}(\omega, 0) = C(\omega).$$

On the other hand, we can compute the Fourier transform of the initial condition, which gives

$$C(\omega) = \hat{u}(\omega, 0) = \mathcal{F}\left( \frac{\sin x}{x} \right)(\omega) = \begin{cases}\sqrt{\dfrac{\pi}{2}} & \text{for } |\omega| < 1,\\[1em] 0 & \text{for } |\omega| > 1.\end{cases}$$

We obtain therefore that

$$\hat{u}(\omega, t) = C(\omega) e^{(1+i\omega)t} = \begin{cases}\sqrt{\dfrac{\pi}{2}} \, e^{(1+i\omega)t} & \text{for } |\omega| < 1,\\[1em] 0 & \text{for } |\omega| > 1.\end{cases}$$

Finally, we obtain the actual solution $u(x, t)$, by applying the inverse Fourier transform to $\hat{u}(\omega, t)$. Using the formula for the inverse Fourier transform, we thus obtain that

$$\begin{aligned}u(x, t) &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} \hat{u}(\omega, t) e^{i\omega x} \, d\omega\\
&= \frac{1}{\sqrt{2\pi}} \int_{-1}^{1} \sqrt{\frac{\pi}{2}} \, e^{(1+i\omega)t} e^{i\omega x} \, d\omega\\
&= \frac{e^t}{2} \int_{-1}^{1} e^{i\omega(x+t)} \, d\omega\\
&= \frac{e^t}{2i(x+t)} \left. e^{i\omega(x+t)} \right|_{-1}^{1}\\
&= \frac{e^t}{2i(x+t)} \left( e^{i(x+t)} - e^{-i(x+t)} \right)\\
&= e^t \, \frac{\sin(x + t)}{x + t}.\end{aligned}$$

Kildesett: course=TMA4135 term=host year=2022 problem=5 file=math4nd-2022h_published.pdf
