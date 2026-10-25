### **Solution to Problem 4**

**a)** We first deduce the solution using Fourier transform. Let $\hat{u}(w,t)$ be the Fourier transform of $u(\cdot, t)$. Then

$$\hat{u}_t(w,t) = \widehat{u_t}(w,t) = \widehat{u_{xx}}(w,t) = -w^2 \hat{u}(w,t)$$

with solution

$$\hat{u}(w,t) = C(w) e^{-w^2 t}.$$

Next,

$$\begin{aligned} C(w) &= \hat{u}(w,0) \\ &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} u(x,0) e^{-iwx} \, \mathrm{d}x \\ &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} h(x) e^{-iwx} \, \mathrm{d}x \\ &= \hat{h}(w). \end{aligned}$$

From the Formula sheet we find that $e^{-w^2 t}$ is the transform of $g(x,t) := \frac{1}{\sqrt{2t}} e^{-\frac{x^2}{4t}}$, and by the convolution theorem it follows that

$$\begin{aligned} u(x,t) &= \mathcal{F}^{-1}\{\hat{u}(\cdot, t)\}(x) \\ &= \mathcal{F}^{-1}\{\hat{h}\hat{g}(\cdot, t)\}(x) \\ &= \frac{1}{\sqrt{2\pi}} (h * g(\cdot, t))(x) \\ &= \frac{1}{\sqrt{2\pi}} \int_{-\infty}^{\infty} h(y) g(x-y, t) \, \mathrm{d}y \\ &= \frac{1}{2\sqrt{\pi t}} \int_{-1}^{1} e^{-\frac{(x-y)^2}{4t}} \, \mathrm{d}y. \end{aligned}$$

Confirming $u$ is a solution:

$$\begin{aligned} u_t(x,t) &= -\frac{1}{4\sqrt{\pi} t^{3/2}} \int_{-1}^{1} e^{-\frac{(x-y)^2}{4t}} \, \mathrm{d}y + \frac{1}{2\sqrt{\pi t}} \int_{-1}^{1} e^{-\frac{(x-y)^2}{4t}} \frac{(x-y)^2}{4t^2} \, \mathrm{d}y. \\ u_x(x,t) &= -\frac{1}{2\sqrt{\pi t}} \int_{-1}^{1} e^{-\frac{(x-y)^2}{4t}} \frac{x-y}{2t} \, \mathrm{d}y, \\ u_{xx}(x,t) &= -\frac{1}{2\sqrt{\pi t}} \left( \int_{-1}^{1} e^{-\frac{(x-y)^2}{4t}} \frac{1}{2t} - e^{-\frac{(x-y)^2}{4t}} \frac{(x-y)^2}{4t^2} \, \mathrm{d}y \right) = u_t(x,t) \end{aligned}$$

ok.

The simplest way to argue that the initial conditions are fulfilled, is to make the substitution $z := \frac{y-x}{2\sqrt{t}}$ (because then $\frac{(x-y)^2}{4t} = z^2$). Now, $\mathrm{d}y = 2\sqrt{t} \, \mathrm{d}z$ and

$$\begin{aligned} u(x,t) &= \frac{1}{2\sqrt{\pi t}} \int_{-\infty}^{\infty} h(y) e^{-\frac{(x-y)^2}{4t}} \, \mathrm{d}y \\ &= \frac{1}{\sqrt{\pi}} \int_{-\infty}^{\infty} h(x + 2\sqrt{t}z) e^{-z^2} \, \mathrm{d}z, \end{aligned}$$

which is valid for all $t > 0$. Thus,

$$\begin{aligned} \lim_{t \to 0^+} u(x,t) &= \frac{1}{\sqrt{\pi}} \int_{-\infty}^{\infty} h(x) e^{-z^2} \, \mathrm{d}z \\ &= h(x) \frac{1}{\sqrt{\pi}} \int_{-\infty}^{\infty} e^{-z^2} \, \mathrm{d}z \\ &= h(x), \end{aligned}$$

again by the 'famous identity' mentioned in Problem 3.

**b)** Since

$$y = 1 \quad \iff \quad z = \frac{1-x}{2\sqrt{t}}, \qquad \text{and} \qquad y = -1 \quad \iff \quad z = -\frac{1+x}{2\sqrt{t}},$$

we can also write

$$\begin{aligned} u(x,t) &= \frac{1}{2\sqrt{\pi t}} \int_{-1}^{1} e^{-\frac{(x-y)^2}{4t}} \, \mathrm{d}y \\ &= \frac{1}{\sqrt{\pi}} \int_{-\frac{1+x}{2\sqrt{t}}}^{\frac{1-x}{2\sqrt{t}}} e^{-z^2} \, \mathrm{d}z \\ &= \frac{1}{\sqrt{\pi}} \int_0^{\frac{1-x}{2\sqrt{t}}} e^{-z^2} \, \mathrm{d}z + \frac{1}{\sqrt{\pi}} \int_{-\frac{1+x}{2\sqrt{t}}}^0 e^{-z^2} \, \mathrm{d}z \\ &= \frac{1}{\sqrt{\pi}} \int_0^{\frac{1-x}{2\sqrt{t}}} e^{-z^2} \, \mathrm{d}z - \frac{1}{\sqrt{\pi}} \int_0^{-\frac{1+x}{2\sqrt{t}}} e^{-z^2} \, \mathrm{d}z \\ &= \frac{1}{2} \left( \operatorname{erf}\left(\frac{1-x}{2\sqrt{t}}\right) - \operatorname{erf}\left(-\frac{1+x}{2\sqrt{t}}\right) \right) \\ &= \frac{1}{2} \left( \operatorname{erf}\left(\frac{1-x}{2\sqrt{t}}\right) + \operatorname{erf}\left(\frac{1+x}{2\sqrt{t}}\right) \right). \end{aligned}$$

In the last step we used that erf is an odd function.

The temperature at $x = 0$ is reduced to one half of $1$ (i.e. $0.5$) when

$$0.5 = u(0,t) = \frac{1}{2} \left( \operatorname{erf}\left(\frac{1-0}{2\sqrt{t}}\right) + \operatorname{erf}\left(\frac{1+0}{2\sqrt{t}}\right) \right) = \operatorname{erf}\left(\frac{1}{2\sqrt{t}}\right).$$

This is the equation we tried to solve in Problem 2. Our best guess at the solution $T$ was $T = 0.9810$.

Kildesett: course=TMA4135 term=host year=2021 problem=4 file=tma4135_2021h_exam-4.pdf
