### **Løsning til Oppgave 1**

**a)** Den Fouriertransformerte til $f$ er

$$\hat{f}(w)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(x)e^{-iwx}\,\mathrm{d}x$$

Vi får

$$\hat{f}(w)=\frac{1}{\sqrt{2\pi}}\left(\int_{-\infty}^{0}e^{ax}e^{-iwx}\,\mathrm{d}x+\int_{0}^{\infty}e^{-ax}e^{-iwx}\,\mathrm{d}x\right)$$

$$=\frac{1}{\sqrt{2\pi}}\left(\int_{-\infty}^{0}e^{(a-iw)x}\,\mathrm{d}x+\int_{0}^{\infty}e^{-(a+iw)x}\,\mathrm{d}x\right)$$

$$=\frac{1}{\sqrt{2\pi}}\left(\left[\frac{1}{a-iw}e^{(a-iw)x}\right]_{-\infty}^{0}-\left[\frac{1}{a+iw}e^{-(a+iw)x}\right]_{0}^{\infty}\right)$$

$$=\frac{1}{\sqrt{2\pi}}\left(\frac{1}{a-iw}+\frac{1}{a+iw}\right)$$

$$=\frac{1}{\sqrt{2\pi}}\frac{a+iw+a-iw}{a^2+w^2}$$

$$=\sqrt{\frac{2}{\pi}}\frac{a}{a^2+w^2}.$$

**b)** Fourierintegralet til $f(x)=e^{a|x|}$ er

$$f(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\hat{f}(w)e^{iwx}\,\mathrm{d}w$$

$$=\frac{1}{\sqrt{2\pi}}\sqrt{\frac{2}{\pi}}\int_{-\infty}^{\infty}\frac{a}{a^2+w^2}e^{iwx}\,\mathrm{d}w$$

$$=\frac{1}{\pi}\int_{-\infty}^{\infty}\frac{a}{a^2+w^2}\cos wx+i\frac{a}{a^2+w^2}\sin wx\,\mathrm{d}w$$

$$=\frac{2a}{\pi}\int_{0}^{\infty}\frac{\cos wx}{a^2+w^2}\,\mathrm{d}w,$$

der den siste likheten følger av at $a/(a^2+w^2)$ og $\cos wx$ er jamne funksjoner, og $\sin wx$ er odde. Vi får dermed at

$$\int_{0}^{\infty}\frac{\cos wx}{w^2+a^2}\,\mathrm{d}w=\frac{\pi}{2a}e^{-a|x|}.$$

*Kjeldevarsel: I første linje av b) er funksjonen trykt som $f(x)=e^{a|x|}$ utan minusteikn; utrekninga gjeld $f(x)=e^{-a|x|}$ frå a), og svaret er rett. Løysingsheftet (losning2013v.pdf) har elles tittelblad datert «Mai 2012» sjølv om det løysar 2013-eksamen.*

Kildesett: course=TMA4123 term=var year=2013 problem=1 file=eksamen2013v.pdf
