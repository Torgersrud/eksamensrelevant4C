### **Løsning til Oppgave 5**

We take the Fourier transform (Kreyszig, p. 527)

$$\begin{aligned}\mathcal F(f*g)&=\sqrt{2\pi}\hat f\hat g\\
&=\sqrt{2\pi}\,\frac{1}{\sqrt2}e^{-\omega^2/4}\left(-\frac{1}{2}\right)\mathcal F\left(\frac{d}{dx}e^{-x^2}\right)\\
&=-\frac{\sqrt{2\pi}}{2\sqrt2}\,e^{-\omega^2/4}\,i\omega\mathcal F(e^{-x^2})\\
&=-\frac{\sqrt{2\pi}\,i}{4}\,\omega\,e^{-\omega^2/4}e^{-\omega^2/4}\\
&=-\frac{\sqrt{2\pi}\,i}{4}\omega\,e^{-\omega^2/2}\end{aligned}$$

Here we also used the formula for the Fourier transform of the derivative (Kreyszig, p. 526).

Using that $\mathcal F^{-1}(h)(x)=\mathcal F(h)(-x)$ (Kreyszig, p. 523f) we see that

$$\begin{aligned}f*g=\mathcal F^{-1}\left(\frac{\sqrt{2\pi}\,i}{4}\frac{d}{d\omega}e^{-\omega^2/2}\right)&=\frac{\sqrt{2\pi}i}{4}\mathcal F^{-1}\left(\frac{d}{d\omega}e^{-\omega^2/2}\right)\\
&=\frac{\sqrt{2\pi}i}{4}\mathcal F\left(\frac{d}{d\omega}e^{-\omega^2/2}\right)(-x)\\
&=\frac{\sqrt{2\pi}i}{4}i(-x)\frac{1}{\sqrt2/2}e^{-(-x)^2/(4/2)}\\
&=\frac{\sqrt{2\pi}}{4}\,x\,e^{-x^2/2}.\end{aligned}$$

Kildesett: course=TMA4135 term=kont year=2016 problem=5 file=tma4135_16k.pdf
