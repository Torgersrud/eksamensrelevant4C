### **Solution to Problem 7** **Wave Equation [10 pts]**

a) First we compute the Fourier transform of $h_t$. We have

$$\hat h_t(w)=\frac{1}{\sqrt{2\pi}}\int_{-ct}^{ct}\frac{1}{2c}e^{-iwx}dx=\frac{1}{-2iwc\sqrt{2\pi}}\left(e^{-icwt}-e^{icwt}\right)=\frac{\sin xwt}{\sqrt{2\pi wc}}.$$

We will use the shift rule for the Fourier transform, $\mathcal{F}(f(x-a))(w)=e^{-iaw}\hat f(w)$ and the convolution rule for the Fourier transform $\mathcal{F}(f*h)=\sqrt{2\pi}\mathcal{F}(f)\mathcal{F}(h)$. Then we get

$$\hat u(t,w)=\frac{1}{2}\hat f(w)(e^{-ictw}+e^{ictw})+\sqrt{2\pi}\frac{2\sin cwt}{2\sqrt{2\pi wc}}\hat g(w)=\hat f(w)\cos ctw+\hat g(w)\frac{\sin cwt}{cw}.$$

b) From the first part of the problem, we see that

$$v(t,w)=\hat f(w)\cos ctw+\hat g(w)\frac{\sin cwt}{cw}.$$

Then $v(0,w)=\hat f(w)$ and $v_t(0,w)=\hat g(w)$. Moreover,

$$v_{tt}(t,w)=-c^2w^2\hat f(w)\cos ctw-cw\hat g(w)\sin ctw=-c^2w^2v(t,w).$$

**Grading manual**

a) (5p)

b) (5p)

Kildesett: course=TMA4135 term=kont year=2023 problem=7 points=10 file=tma4130_2023h_exam-19.pdf
