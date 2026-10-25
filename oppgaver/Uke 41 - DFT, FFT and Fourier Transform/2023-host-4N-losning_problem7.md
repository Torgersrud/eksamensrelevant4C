### **Solution to Problem 7** **Fourier transform [10 pts], 4N**

a) We use the definition to compute the Fourier transform of $g$:
$$\hat g(w)=\frac{1}{\sqrt{2\pi}}\int_{-1}^{1}(1-|x|)e^{-iwx}\,dx.$$
We note that $g$ is an even function and
$$\hat g(w)=\frac{2}{\sqrt{2\pi}}\int_{0}^{1}(1-x)\cos wx\,dx=\sqrt{\frac{2}{\pi}}\int_{0}^{1}\cos wx\,dx-\sqrt{\frac{2}{\pi}}\int_{0}^{1}x\cos wx\,dx.$$
We compute the second integral integrating by parts:
$$\int_{0}^{1}x\cos wx\,dx=x\frac{\sin wx}{w}\Big|_0^1-\int_{0}^{1}\frac{\sin wx}{w}\,dx=\frac{\sin w}{w}+\frac{\cos wx}{w^2}\Big|_0^1=\frac{\sin w}{w}-\frac{1-\cos w}{w^2}.$$
Then
$$\hat g(w)=\sqrt{\frac{2}{\pi}}\left(\frac{\sin wx}{w}\Big|_0^1-\frac{\sin w}{w}+\frac{1-\cos w}{w^2}\right)=\sqrt{\frac{2}{\pi}}\frac{1-\cos w}{w^2}.$$

b) We know that $\hat f=F(g*g)=\sqrt{2\pi}\hat f^2$. Therefore
$$\hat g(w)=\frac{\sqrt{2}\,2(1-\cos w)^2}{\sqrt{\pi}\,w^4}.$$

**Grading manual** (8p) for a), (2p) for b).

Kildesett: course=TMA4135 term=host year=2023 problem=7 points=10 file=tma4130_2023h_exam.pdf
