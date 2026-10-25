### **Løsning til Oppgave 2**

We first compute $\mathcal{F}(f*g)$, the Fourier transform of the convolution. By the convolution theorem, we get

$$\mathcal{F}(f*g)=\sqrt{2\pi}\mathcal{F}(f)\mathcal{F}(g).$$

Using the tables, we see that

$$\mathcal{F}(f)=2\sqrt{\pi}e^{-\sqrt{2}|\omega|}.$$

We note that

$$g(x)=-\left(\frac{1}{x^2+1}\right)'$$

Using the properties of the tables, we obtain

$$\mathcal{F}(g)=-i\omega\sqrt{\frac{\pi}{2}}e^{-|\omega|}.$$

Thus,

$$\mathcal{F}(f*g)=-2i\pi\sqrt{\pi}\omega e^{-(\sqrt{2}+1)|\omega|}.$$

Applying the inverse Fourier transform on both sides, we obtain

$$(f*g)(x)=-\sqrt{2}\pi i\int_{-\infty}^{\infty}\omega e^{-(\sqrt{2}+1)|\omega|}e^{i\omega x}d\omega.$$

Kildesett: course=TMA4135 term=var year=2018 problem=2 file=tma4125_final_exam_may_bm.pdf
