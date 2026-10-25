### **Løsning til Oppgave 2**

Den komplekse Fourierrekken er

$$\sum_{n=-\infty}^{\infty}c_ne^{inx},\quad\text{der } c_n=\frac{1}{2\pi}\int_{-\pi}^{\pi}f(x)e^{-inx}\,\mathrm{d}x\,.$$

For $n\ne 0$ har vi

$$c_n=\frac{1}{2\pi}\int_{0}^{\pi}(\pi-x)e^{-inx}\,\mathrm{d}x$$

$$=\frac{1}{2\pi}\left(\left[-\frac{\pi}{in}e^{-inx}\right]_{0}^{\pi}-\int_{o}^{\pi}xe^{-inx}\,\mathrm{d}x\right)$$

$$=\frac{1}{2\pi}\left(\frac{\pi}{in}-\frac{\pi}{in}e^{-in\pi}-\int_{o}^{\pi}xe^{-inx}\,\mathrm{d}x\right).$$

Det siste integralet kan løses via delvis integrasjon:

$$\int_{o}^{\pi}xe^{-inx}\,\mathrm{d}x=\left[-\frac{x}{in}e^{-inx}+\frac{1}{n^2}e^{-inx}\right]_{0}^{\pi}$$

$$=-\frac{\pi}{in}e^{-in\pi}+\frac{1}{n^2}e^{-in\pi}-\frac{1}{n^2}.$$

Dermed får vi

$$c_n=\frac{1}{2\pi}\left(\frac{\pi}{in}-\frac{\pi}{in}e^{-in\pi}+\frac{\pi}{in}e^{-in\pi}-\frac{1}{n^2}e^{-in\pi}+\frac{1}{n^2}\right)$$

$$=\frac{1}{2\pi n^2}\left(-i\pi n-e^{-i\pi n}+1\right),$$

der den siste likheten følger av at $1/i=-i$.

I tillegg får vi

$$c_0=\frac{1}{2\pi}\int_{0}^{\pi}(\pi-x)dx=\frac{\pi}{4}.$$

Fourierrekken til $f$ er altså

$$\frac{\pi}{4}+\sum_{\substack{n=-\infty\\ n\ne 0}}^{\infty}\frac{1}{2\pi n^2}\left(-i\pi n-e^{-i\pi n}+1\right)e^{inx}.$$

*Kjeldevarsel: Nedre integrasjonsgrense i dei tre integrala med $xe^{-inx}$ er trykt med bokstaven «o» i staden for talet 0; bevart ordrett.*

Kildesett: course=TMA4123 term=var year=2013 problem=2 file=eksamen2013v.pdf
