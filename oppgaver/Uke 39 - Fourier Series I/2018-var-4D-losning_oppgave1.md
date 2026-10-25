### **Løsning til Oppgave 1**

**a)** The Fourier sine series is of the form

$$\sum_{n=1}^{\infty}b_n\sin\left(\frac{n\pi x}{L}\right),$$

where $L=3$ is the half-range period, and

$$b_n=\frac{2}{L}\int_0^L f(x)\sin\left(\frac{n\pi x}{L}\right)dx.$$

We compute the coefficients $b_n$:

$$b_n=\frac{2}{3}\int_0^3 x\sin\left(\frac{n\pi x}{3}\right)dx.$$

To compute this integral, we use integration by parts. We obtain

$$b_n=\frac{2}{3}\left(\left[x\frac{-3}{n\pi}\cos\left(\frac{n\pi x}{3}\right)\right]_0^3+\frac{3}{n\pi}\int_0^3\cos\left(\frac{n\pi x}{3}\right)dx\right)$$

$$=\frac{2}{3}\left(\frac{(-1)^{n+1}\cdot 9}{n\pi}+0\right)=\frac{(-1)^{n+1}\cdot 6}{n\pi}.$$

Thus the Fourier sine series of $f(x)$ is given by

$$\sum_{n=1}^{\infty}\frac{(-1)^{n+1}\cdot 6}{n\pi}\sin\left(\frac{n\pi x}{3}\right).$$

**b)** We use Parseval's identity:

$$\sum_{n=1}^{\infty}b_n^2=\frac{2}{L}\int_0^L f(x)^2dx.$$

We have

$$\frac{36}{\pi^2}\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{2}{3}\int_0^3 x^2dx=6.$$

Thus

$$\sum_{n=1}^{\infty}\frac{1}{n^2}=\frac{\pi^2}{6}.$$

Kildesett: course=TMA4135 term=var year=2018 problem=1 file=tma4125_final_exam_may_bm.pdf
