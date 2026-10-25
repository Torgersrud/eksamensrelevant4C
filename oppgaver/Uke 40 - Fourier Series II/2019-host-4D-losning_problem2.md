### **Solution to Problem 2**

**a)** We have $c_0=\frac{1}{2\pi}\int_{-\pi}^{\pi}(1+x)\,dx=1$. Thus it is enough to show, for $n\neq 0$, we have $c_n=\frac{i(-1)^n}{n}$. In fact

$$c_n=\frac{1}{2\pi}\int_{-\pi}^{\pi}(1+x)e^{-inx}dx=\frac{1}{2\pi}\int_{-\pi}^{\pi}xe^{-inx}dx=\left.\frac{xe^{-inx}}{-2\pi i n}\right|_{-\pi}^{\pi}=\frac{i(-1)^n}{n}.$$

**b)** Because f is smooth, that is, $f$ is continuously differentiable on the interval $-\pi<x<\pi$.

**c)** We have

$$\hat{f}(\omega)=\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}e^{-ix\omega}\sin x\,dx.$$

Notice that

$$e^{-ix\omega}=\cos x\omega-i\sin x\omega,$$

$\cos x\omega\sin x$ is odd and $\sin x\omega\sin x$ is even. Thus

$$\int_{-1}^{1}e^{-ix\omega}\sin x\,dx=2(-i)\int_{0}^{1}\sin x\omega\sin x\,dx.$$

Recall that

$$2\sin a\sin b=\cos(a-b)-\cos(a+b).$$

Thus

$$\int_{-1}^{1}e^{-ix\omega}\sin x\,dx=(-i)\int_{0}^{1}\cos(x\omega-x)-\cos(x\omega+x)\,dx,$$

which gives

$$\int_{-1}^{1}e^{-ix\omega}\sin x\,dx=(-i)\left(\left.\frac{\sin(x\omega-x)}{\omega-1}\right|_{0}^{1}-\left.\frac{\sin(x\omega+x)}{\omega+1}\right|_{0}^{1}\right).$$

Thus

$$\hat{f}(\omega)=\frac{-i}{\sqrt{2\pi}}\left(\frac{\sin(\omega-1)}{\omega-1}-\frac{\sin(\omega+1)}{\omega+1}\right).$$

Kildesett: course=TMA4135 term=host year=2019 problem=2 points=14 file=unred.pdf
