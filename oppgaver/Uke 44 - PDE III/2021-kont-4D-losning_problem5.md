### **Solution to Problem 5**

a) We have $v_t = 0$, and $v_{xx} = -\alpha/c^2 \cos(x - \pi)$, which implies that $v_t - c^2 v_{xx} = \alpha\cos(x - \pi)$.

b) Consider the function $w = u - v$. Linearity (or superposition) implies that $w$ satisfies

$$w_t = c^2 w_{xx}, \quad w_x(0,t) = w_x(\pi,t) = 0, \quad t > 0,$$

(note that $v_x$ vanishes at $x = 0$ and $\pi$), with initial data

$$w(x,0) = u(x,0) - v(x,0) = \begin{cases}0, & 0 \leq x < \frac{\pi}{2},\\ x - \pi, & \frac{\pi}{2} < x \leq \pi.\end{cases}$$

Standard separation of variables (Kreyszig, p. 563) gives that

$$w(x,t) = \sum_{n=0}^{\infty} A_n \cos(nx) e^{-(cn)^2 t}$$

where $A_n$ are given as the Fourier coefficients of the initial data, thus

$$w(x,0) = \sum_{n=0}^{\infty} A_n \cos(nx) = \begin{cases}0, & 0 \leq x < \frac{\pi}{2},\\ x - \pi, & \frac{\pi}{2} < x \leq \pi.\end{cases}$$

Standard formulas for Fourier series yield for $n > 0$

$$\begin{aligned} A_n &= \frac{2}{\pi}\int_0^{\pi} \cos(nx) w(x,0) dx \\ &= \frac{2}{\pi}\int_{\pi/2}^{\pi} \cos(nx)(x - \pi) dx \\ &= \frac{2}{\pi}\left[\left[\frac{1}{n}\sin(nx)(x - \pi)\right]_{\pi/2}^{\pi} - \frac{1}{n}\int_{\pi/2}^{\pi} \sin(nx) dx\right] \\ &= \frac{1}{n}\sin\left(\frac{n\pi}{2}\right) + \frac{2}{\pi n^2}\cos\left(\frac{n\pi}{2}\right). \end{aligned}$$

In addition,

$$A_0 = \frac{1}{\pi}\int_0^{\pi} w(x,0) dx = \frac{1}{\pi}\int_{\pi/2}^{\pi} (x - \pi) dx = -\frac{\pi}{8}$$

Thus the answer reads

$$\begin{aligned} u(x,t) &= v(x,t) + w(x,t) \\ &= \frac{\alpha}{c^2}\cos(x - \pi) - \frac{\pi}{8} + \sum_{n=1}^{\infty} \left(\frac{1}{n}\sin\left(\frac{n\pi}{2}\right) + \frac{2}{\pi n^2}\cos\left(\frac{n\pi}{2}\right)\right)\cos(nx) e^{-(cn)^2 t}. \end{aligned}$$

c) We see that each term in the infinite sum contains the exponentially decaying factor $e^{-(cn)^2 t}$. Thus these terms will all vanish in the limit when $t \to \infty$. Hence

$$u(x,t) \to \frac{\alpha}{c^2}\cos(x - \pi) - \frac{\pi}{8}, \quad t \to \infty.$$

Kildesett: course=TMA4135 term=kont year=2021 problem=5 file=retake_lf.pdf
