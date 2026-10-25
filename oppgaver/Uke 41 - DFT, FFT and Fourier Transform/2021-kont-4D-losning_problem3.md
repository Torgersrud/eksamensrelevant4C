### **Solution to Problem 3**

$$\sqrt{2\pi}\,\hat f(w)=\int_{-\infty}^{\infty}f(x)e^{-ixw}dx=\int_{-1}^{1}(x+c)e^{-ixw}dx$$

$$=\frac{(1+c)e^{-iw}-(c-1)e^{iw}}{-iw}-\frac{1}{-iw}\int_{-1}^{1}e^{-ixw}dx$$

$$=\frac{i\big((1+c)e^{-iw}-(c-1)e^{iw}\big)}{w}-\frac{2i\sin w}{w^{2}}$$

**Remark 1.** The computation above is only true for $w\neq 0$, so we will have to compute

$$\sqrt{2\pi}\,\hat f(0)=\int_{-1}^{1}(x+c)dx=2c\,.$$

**Remark 2.** One may also use $e^{\pm iw}=\cos w\pm i\sin w$ to rewrite the solution (the original form or some other equivalent forms are also ok). We get

$$\sqrt{2\pi}\,\hat f(w)=\frac{i\big((1+c)(\cos w-i\sin w)+(1-c)(\cos w+i\sin w)\big)}{w}-\frac{2i\sin w}{w^{2}}=\frac{2i\cos w+2c\sin w}{w}-\frac{2i\sin w}{w^{2}}$$

so

$$\hat f(w)=\begin{cases}\dfrac{1}{\sqrt{2\pi}}\left(\dfrac{2i\cos w+2c\sin w}{w}-\dfrac{2i\sin w}{w^{2}}\right)&w\neq 0\\[2mm]\dfrac{2c}{\sqrt{2\pi}}=\sqrt{\dfrac{2}{\pi}}\cdot c&w=0\,.\end{cases}$$

Kildesett: course=TMA4135 term=kont year=2021 problem=3 file=retake_lf.pdf
