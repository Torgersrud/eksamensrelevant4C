### **Solution to Problem 4**

**a)** We compute

$$\mathscr{F}(f)(\omega)=\hat{f}(\omega)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-i\omega x}\,\mathrm{d}x=\frac{1}{\sqrt{2\pi}}\int_{0}^{\infty}e^{-ax}e^{-i\omega x}\,\mathrm{d}x$$

$$=\frac{1}{\sqrt{2\pi}}\int_{0}^{\infty}e^{-(a+i\omega)x}\,\mathrm{d}x=\frac{1}{\sqrt{2\pi}(a+i\omega)}.$$

From now on, set $a=1$ to get

$$\hat{f}(\omega)=\frac{1}{\sqrt{2\pi}(1+i\omega)}.$$

Observe that

$$0=f(-1)=\mathscr{F}^{-1}(\hat{f})(-1)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi}(1+i\omega)}e^{i\omega\cdot(-1)}\,\mathrm{d}\omega$$

$$=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{1}{1+i\omega}(\cos\omega-i\sin\omega)\,\mathrm{d}\omega$$

$$=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{1-i\omega}{1+\omega^2}(\cos\omega-i\sin\omega)\,\mathrm{d}\omega$$

$$=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{\cos\omega-i\sin\omega-i\omega\cos\omega-\omega\sin\omega}{1+\omega^2}\,\mathrm{d}\omega$$

$$=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{\cos\omega-\omega\sin\omega}{1+\omega^2}\,\mathrm{d}\omega-\frac{i}{2\pi}\int_{-\infty}^{\infty}\frac{\sin\omega+\omega\cos\omega}{1+\omega^2}\,\mathrm{d}\omega.$$

The second integral on the last line must be zero since the left hand side is real (in fact, the integrand is odd, so the integral is indeed zero). The integrand in the first integral is even, so

$$0=\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{\cos\omega-\omega\sin\omega}{1+\omega^2}\,\mathrm{d}\omega=\frac{1}{\pi}\int_{0}^{\infty}\frac{\cos\omega-\omega\sin\omega}{1+\omega^2}\,\mathrm{d}\omega,$$

and so the integral we were asked to compute is 0.

**b)** For $b>0$, define $g_b:\mathbb{R}\to\mathbb{R}$ by $g_b(x)=e^{-bx^2}$. We recognize the integral as a convolution, so that the equation in the problem becomes

$$f*g_2=g_1.$$

Fourier transforming gives

$$\sqrt{2\pi}\hat{f}\cdot\hat{g}_2=\hat{g}_1,$$

and we know well that

$$\hat{g}_b(\omega)=\frac{1}{\sqrt{2b}}e^{-\omega^2/4b},$$

so we have

$$\hat{f}(\omega)=\frac{1}{\sqrt{2\pi}}\frac{\frac{1}{\sqrt{2}}e^{-\omega^2/4}}{\frac{1}{\sqrt{4}}e^{-\omega^2/8}}=\frac{1}{\sqrt{\pi}}e^{-\omega^2/8}=\frac{2}{\sqrt{\pi}}\hat{g}_2(\omega).$$

Taking the inverse Fourier transform gives

$$f(x)=\frac{2}{\sqrt{\pi}}g_2(x)=\frac{2}{\sqrt{\pi}}e^{-2x^2}.$$

Kildesett: course=TMA4130 term=host year=2013 problem=4 file=eksamen-bok_2013h.pdf
