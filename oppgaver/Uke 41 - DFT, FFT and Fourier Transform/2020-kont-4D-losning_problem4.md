### **Solution to Problem 4**

We have

$$\hat{f}(\omega)=\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}e^{-ix\omega}(x+2)\,dx.$$

Notice that

$$\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}e^{-ix\omega}(x+2)\,dx=\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}e^{-ix\omega}x\,dx+\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}2e^{-ix\omega}\,dx.$$

We have

$$\int_{-1}^{1}e^{-ix\omega}x\,dx=\int_{-1}^{1}\left(\frac{e^{-ix\omega}}{-i\omega}\right)'x\,dx=\frac{e^{-ix\omega}}{-i\omega}x\Big|_{-1}^{1}-\int_{-1}^{1}\left(\frac{e^{-ix\omega}}{-i\omega}\right)\,dx,$$

which gives

$$\int_{-1}^{1}e^{-ix\omega}x\,dx=\frac{e^{-i\omega}+e^{i\omega}}{-i\omega}-\frac{e^{-i\omega}-e^{i\omega}}{(-i\omega)^{2}}=\frac{2\cos(\omega)}{-i\omega}-\frac{2i\sin(\omega)}{\omega^{2}}=\frac{2i(\omega\cos(\omega)-\sin(\omega))}{\omega^{2}}.$$

We also have

$$\int_{-1}^{1}2e^{-ix\omega}\,dx=\frac{2(e^{-i\omega}-e^{i\omega})}{-i\omega}=\frac{4\sin(\omega)}{\omega}.$$

Thus

$$\hat{f}(\omega)=\frac{1}{\sqrt{2\pi}}\left(\frac{2i(\omega\cos(\omega)-\sin(\omega))}{\omega^{2}}+\frac{4\sin(\omega)}{\omega}\right).$$

Kildesett: course=TMA4135 term=kont year=2020 problem=4 points=6 file=tma4130_kont.pdf
