### **Løsning til Oppgave 6**

Den Fouriertransformerte til $f(x)$ er

$$\hat f(\omega)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-i\omega x}dx=\frac{1}{\sqrt{2\pi}}\int\limits_0^2e^{-i\omega x}dx=\frac{1}{\sqrt{2\pi}}\frac{1-e^{-i2\omega}}{i\omega}\,.$$

Fourierintegralet er

$$\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\left(\frac{1}{\sqrt{2\pi}}\frac{1-e^{-i2\omega}}{i\omega}\right)e^{i\omega x}d\omega=\frac{1}{2\pi i}\int_{-\infty}^{\infty}\frac{e^{i\omega x}-e^{i\omega(x-2)}}{\omega}d\omega=$$

$$\frac{1}{2\pi i}\int_{-\infty}^{\infty}\frac{\cos\omega x+i\sin\omega x-\cos\omega(x-2)-i\sin\omega(x-2)}{\omega}d\omega=$$

$$\frac{1}{2\pi}\int_{-\infty}^{\infty}\frac{\sin\omega x-\sin\omega(x-2)}{\omega}d\omega\ ,$$

siden

$\dfrac{\cos\omega x-\cos\omega(x-2)}{\omega}$ er en odde funksjon av $\omega$ for fast $x$ . Siden $\dfrac{\sin\omega x-\sin\omega(x-2)}{\omega}$ er en like funksjon av $\omega$ , kan Fourierintegralet skrives som

$$\frac{1}{\pi}\int_0^{\infty}\frac{\sin\omega x-\sin\omega(x-2)}{\omega}d\omega=\frac{1}{\pi}\int_0^{\infty}\frac{\sin\omega x+\sin\omega(2-x)}{\omega}d\omega\,.$$

Siden $f(x)$ er kontinuerlig for $x=1$ , er

$$1=f(1)=\frac{1}{\pi}\int_0^{\infty}\frac{\sin\omega+\sin\omega}{\omega}d\omega\Leftrightarrow\int_0^{\infty}\frac{\sin\omega}{\omega}d\omega=\frac{\pi}{2}\,.$$

Kildesett: course=TMA4125 term=var year=2016 problem=6 file=tma4123_4125.pdf
