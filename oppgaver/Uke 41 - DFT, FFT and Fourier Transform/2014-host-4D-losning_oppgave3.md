### **Løsning til Oppgave 3**

La $g_a(x)=e^{-ax^2}$. Da er ligningen vår

$$(g_4*f)(x)=g_2(x).$$

Fourier-transformerer vi, får vi

$$\sqrt{2\pi}\hat{g}_4\hat{f}=\hat{g}_2.$$

Vi vet at

$$\hat{g}_a(\omega)=\mathscr{F}(g_a)(\omega)=\frac{1}{\sqrt{2a}}e^{-\omega^2/(4a)},$$

så vi har

$$\hat{f}(\omega)=\frac{\hat{g}_2(\omega)}{\sqrt{2\pi}\hat{g}_4(\omega)}=\frac{1}{\sqrt{2\pi}}\frac{\frac{1}{2}e^{-\omega^2/8}}{\frac{1}{2\sqrt{2}}e^{-\omega^2/16}}=\frac{\sqrt{2}}{\sqrt{2\pi}}e^{-\omega^2/16}=\frac{1}{\sqrt{\pi}}\frac{\sqrt{2\cdot4}}{\sqrt{2\cdot4}}e^{-\omega^2/(4\cdot4)}=\frac{2\sqrt{2}}{\sqrt{\pi}}\hat{g}_4(\omega).$$

Dermed er

$$f(x)=\frac{2\sqrt{2}}{\sqrt{\pi}}\mathscr{F}^{-1}(\hat{g}_4)(x)=\frac{2\sqrt{2}}{\sqrt{\pi}}e^{-4x^2}.$$

Kildesett: course=TMA4135 term=host year=2014 problem=3 file=tma4135_14h.pdf
