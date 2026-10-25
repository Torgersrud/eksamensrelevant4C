### **Solution to Problem 8**

We apply the Fourier transformation (with respect only to the $x$-variable) to the given PDE and obtain

$$\frac{\partial\hat u}{\partial t}(\omega,t)=-t\omega^2\hat u(\omega,t).$$

For every $\omega\in\mathbb{R}$, this is an ODE with respect to $t$, with solution

$$\hat u(\omega,t)=C(\omega)e^{-\frac{\omega^2t^2}{2}}\,.$$

In order to find $C(\omega)$, we use the initial condition, which, after a Fourier transformation, reads as

$$\hat u(\omega,0)=e^{-\frac{\omega^2}{2}}\,.$$

Thus

$$C(\omega)=e^{-\frac{\omega^2}{2}},$$

and we obtain

$$\hat u(\omega,t)=e^{-\frac{\omega^2}{2}}e^{-\frac{\omega^2t^2}{2}}=e^{-\omega^2\frac{t^2+1}{2}}\,.$$

Finally we compute the inverse Fourier transform of $\hat u$ and obtain

$$u(x,t)=\mathcal{F}^{-1}(\hat u(\omega,t))=\frac{1}{\sqrt{t^2+1}}e^{-\frac{x^2}{2(t^2+1)}}\,.$$

Kildesett: course=TMA4125 term=kont year=2016 problem=8 file=english.pdf
