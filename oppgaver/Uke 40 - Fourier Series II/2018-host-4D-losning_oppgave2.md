### **Løsning til Oppgave 2**

**a)** Observe that $f(x)$ is an even function ($f(x)=f(-x)$). Its Fourier cosine series computes

$$f(x)=1-\frac{\pi^2}{3}+\sum_{n>0}\frac{4(-1)^{n+1}}{n^2}\cos(nx).$$

Now, using that $e^{inx}=\cos(nx)+i\sin(nx)$ and noticing that $f(x)\sin(nx)$ is an odd function, a direct computation gives

$$1-x^2=1-\frac{\pi^2}{3}-\sum_{n\in\mathbb{Z},\,n\neq 0}\frac{2(-1)^{n}}{n^2}e^{inx}.$$

Thus

$$c_0=1-\frac{\pi^2}{3},$$

and

$$c_n=\frac{2(-1)^{n+1}}{n^2},\qquad n\neq 0.$$

**b)** We can either compute it directly or use the identity $\frac{d}{d\omega}\hat{f}(\omega)=\mathcal{F}(-ixf(x))(\omega)$. In fact, we have

$$\mathcal{F}(e^{-|x|})(\omega)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}e^{-|x|}e^{-i\omega x}dx$$

$$=\frac{1}{\sqrt{2\pi}}\int_{0}^{\infty}e^{-x}e^{-i\omega x}dx+\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{0}e^{x}e^{-i\omega x}dx.$$

After a few steps, this yields

$$\mathcal{F}(e^{-|x|})(\omega)=\sqrt{\frac{2}{\pi}}\frac{1}{\omega^2+1}.$$

Thus, using $\frac{d}{d\omega}\hat{f}(\omega)=\mathcal{F}(-ixf(x))(\omega)$, gives

$$\mathcal{F}(-ixe^{-|x|})(\omega)=\sqrt{\frac{2}{\pi}}\frac{-2\omega}{(\omega^2+1)^2},$$

which yields

$$\mathcal{F}(xe^{-|x|})(\omega)=\sqrt{\frac{2}{\pi}}\frac{-2i\omega}{(\omega^2+1)^2}.$$

Kildesett: course=TMA4135 term=host year=2018 problem=2 points=14 file=exam_fall18_tma4130_norsk.pdf
