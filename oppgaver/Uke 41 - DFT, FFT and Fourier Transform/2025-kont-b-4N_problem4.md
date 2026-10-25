### **Problem 4** **Fourier Transform (10 points)**

a) Consider the function $f:\mathbb{R}\to\mathbb{R}$
$$f(t)=\begin{cases}-1&-1<t<0\\ 1&0<t<1\\ 0&\text{else}\end{cases}$$
Compute its Fourier transform
$$\mathcal{F}[f](w):=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\infty}f(s)\exp(-iws)ds.$$
Note that $\exp(-iws)=e^{-iws}$.

b) From the lectures you know that
$$\mathcal{F}[g'] (w)=iw\mathcal{F}[g](w),$$
where $g'$ denotes the derivative of $g$. Compute the Fourier transform of the function
$$f(t)=\frac{t}{(t^2+c^2)^2},\quad c>0.$$
Hint: Use the fact that the Fourier transform of the function $h(t)=c(t^2+c^2)^{-1}$ is the function $\hat{h}(w)=\sqrt{\pi/2}\exp(-c|w|)=\sqrt{\pi/2}e^{-c|w|}$.

Kildesett: course=TMA4130 term=kont year=2025 problem=4 points=10 file=exam_math_4n_4d_tma4130_35-15.pdf
