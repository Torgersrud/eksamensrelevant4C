### **Løsning til Oppgave 2**

a)  Delbrøkoppspalting gir at

$$f(x)=\frac{1}{(1+x^2)(4+x^2)}=\frac{1}{3}\left(\frac{1}{1+x^2}-\frac{1}{4+x^2}\right),$$

slik at Fourier-transformasjonen til $f(x)$ er gitt ved

$$\hat{f}(w)=\frac{1}{3}\left(\frac{1}{1}\sqrt{\frac{\pi}{2}}e^{-|w|}-\frac{1}{2}\sqrt{\frac{\pi}{2}}e^{-2|w|}\right)=\frac{1}{3}\sqrt{\frac{\pi}{2}}\left(e^{-|w|}-\frac{1}{2}e^{-2|w|}\right).$$

b)  Ved å utnytte symmetrien kan vi skrive

$$\int_0^{\infty}\left(e^{-w}-e^{-2w}\right)\cos wx\,\mathrm{d}w=\frac{1}{2}\int_{-\infty}^{\infty}e^{-|w|}e^{iwx}\,\mathrm{d}w-\frac{1}{2}\int_{-\infty}^{\infty}e^{-2|w|}e^{iwx}\,\mathrm{d}w.$$

Dette minner om den oppgitte Fourier-transformen, og vi ser nå at

$$\frac{1}{2}\int_{-\infty}^{\infty}e^{-|w|}e^{iwx}\,\mathrm{d}w=\frac{1}{2}\sqrt{\frac{2}{\pi}}\int_{-\infty}^{\infty}\sqrt{\frac{\pi}{2}}e^{-|w|}e^{iwx}\,\mathrm{d}w$$

$$=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\left(\sqrt{\frac{\pi}{2}}e^{-|w|}\right)e^{iwx}\,\mathrm{d}w$$

$$=\frac{1}{1+x^2}.$$

På tilsvarende måte finner vi

$$\frac{1}{2}\int_{-\infty}^{\infty}e^{-2|w|}e^{iwx}\,\mathrm{d}w=\frac{1}{2}\frac{2}{1}\sqrt{\frac{2}{\pi}}\int_{-\infty}^{\infty}\frac{1}{2}\sqrt{\frac{\pi}{2}}e^{-2|w|}e^{iwx}\,\mathrm{d}w$$

$$=2\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}\left(\frac{1}{2}\sqrt{\frac{\pi}{2}}e^{-2|w|}\right)e^{iwx}\,\mathrm{d}w$$

$$=2\frac{1}{4+x^2}.$$

Følgelig blir

$$\int_0^{\infty}\left(e^{-w}-e^{-2w}\right)\cos wx\,\mathrm{d}w=\frac{1}{1+x^2}-\frac{2}{4+x^2}.$$

Kildesett: course=TMA4135 term=kont year=2011 problem=2 file=tma4135_11k.pdf
