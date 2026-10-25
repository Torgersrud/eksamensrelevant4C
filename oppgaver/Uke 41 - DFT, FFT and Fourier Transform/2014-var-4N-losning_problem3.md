### **Solution to Problem 3**

Let $\widehat{u}(t,\omega)$ denote the Fouriertransform of $u(t,x)$ in $x$. That is,

$$\widehat{u}(t,\omega)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}u(t,x)e^{-ix\omega}\ dx.$$

By applying Fouriertransform to the partial differential equation and using that

$$\widehat{u_{xx}}=(i\omega)^{2}\widehat{u}=-\omega^{2}\widehat{u},$$

we obtain the first order separable ordinary differential equation:

$$\widehat{u}_{t}+\omega^{2}\widehat{u}+\widehat{u}=0.$$

The solution of this ODE is

$$\widehat{u}(t,\omega)=\widehat{u}_{0}(\omega)\ e^{-\omega^{2}t-t}.$$

From the Formulas given at the end of the exam, we see that

$$\widehat{e^{-ax^{2}}}=\frac{1}{\sqrt{2a}}e^{-\frac{\omega^{2}}{4a}}$$

With $a=\frac{1}{4t}$, we see that

$$\frac{1}{\sqrt{2t}}\widehat{e^{-\frac{x^{2}}{4t}}}=e^{-\omega^{2}t}$$

Hence, we can take the inverse transform to obtain that

$$u(t,x)=u_{0}(x)\star\left(\frac{1}{\sqrt{4\pi t}}e^{-\frac{x^{2}}{4t}}\right)e^{-t},$$

where we have used that

$$\widehat{f\star g}=\sqrt{2\pi}\widehat{f}\widehat{g},$$

which is also given in the formulas at the end of the exam.

Kildesett: course=TMA4123 term=var year=2014 problem=3 file=v14-english.pdf
