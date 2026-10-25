### **Problem 3**

**a)** Let $a<b$ be real numbers, and $\hat{g}(w)$ be the Fourier transform of $g(x)$. Derive the identity

$$\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{\hat{g}(w)(e^{iwb}-e^{iwa})}{iw}dw=\int_{a}^{b}g(x)dx$$

**b)** Take Fourier transforms with respect to $x$ on both sides of the wave equation

$$\frac{\partial^2 u}{\partial t^2}=c^2\frac{\partial^2 u}{\partial x^2}$$

Suppose we wish to solve the equation with respect to the initial conditions $u(x,0)=0$, $u_t(x,0)=g(x)$. By solving the equation for $\hat{u}$, show that the Fourier transform of $u$ is given by

$$\hat{u}(w,t)=\frac{\hat{g}(w)}{cw}\sin cwt$$

**c)** Deduce from the above that

$$u(x,t)=\frac{1}{2c}\int_{x-ct}^{x+ct}g(x)dx$$

Kildesett: course=TMA4125 term=var year=2017 problem=3 file=exam.pdf
