### **Solution to Problem 4** *TMA4130 Mathematics 4N:* [5 points]

By definition

$$\hat{f}(0)=\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}x^{2}=\frac{1}{3}\cdot\sqrt{\frac{2}{\pi}},$$

and when $w\ne 0$ we have

$$\hat{f}(w)=\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}x^{2}e^{-ixw}.$$

Integration by parts gives

$$\int_{-1}^{1}x^{2}e^{-ixw}=x^{2}\frac{e^{-ixw}}{-iw}\vert_{-1}^{1}-\int_{-1}^{1}2x\frac{e^{-ixw}}{-iw}=2\frac{\sin w}{w}+\int_{-1}^{1}2x\frac{e^{-ixw}}{iw}$$

and

$$\int_{-1}^{1}2x\frac{e^{-ixw}}{iw}=2x\frac{e^{-ixw}}{w^{2}}\vert_{-1}^{1}-\int_{-1}^{1}2\frac{e^{-ixw}}{w^{2}}=4\frac{\cos w}{w^{2}}-4\frac{\sin w}{w^{3}}$$

Hence

$$\hat{f}=\sqrt{\frac{2}{\pi}}\left(\frac{\sin w}{w}+\frac{2\cos w}{w^{2}}-\frac{2\sin w}{w^{3}}\right).$$

Kildesett: course=TMA4135 term=host year=2020 problem=4 points=5 file=completeexam_nosolutions.pdf
